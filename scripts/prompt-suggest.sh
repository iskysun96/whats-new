#!/usr/bin/env bash
set -euo pipefail

# Capture stdin immediately
INPUT=$(cat)

DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"
if [[ -z "$DATA_DIR" ]]; then
  exit 0
fi

# Only run in that-friend mode
CONFIG_FILE="${DATA_DIR}/config.json"
MODE="coworker"
if [[ -f "$CONFIG_FILE" ]]; then
  MODE=$(python3 -c "
import json
with open('$CONFIG_FILE') as f:
    print(json.load(f).get('mode', 'coworker'))
" 2>/dev/null || echo "coworker")
fi

if [[ "$MODE" != "that-friend" ]]; then
  exit 0
fi

# Run the pattern engine
export WHATS_NEW_INPUT="$INPUT"
export WHATS_NEW_DATA_DIR="$DATA_DIR"
export WHATS_NEW_PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"

python3 << 'PYEOF'
import json, os, sys, re, time

data_dir = os.environ.get("WHATS_NEW_DATA_DIR", "")
plugin_root = os.environ.get("WHATS_NEW_PLUGIN_ROOT", "")

# --- Load user prompt ---
try:
    hook_input = json.loads(os.environ.get("WHATS_NEW_INPUT", "{}"))
    prompt = hook_input.get("prompt", "").lower()
except Exception:
    prompt = ""

# --- Load suggested state ---
suggested_path = os.path.join(data_dir, "suggested.json")
suggested = {"features": [], "prompt_count": 0, "last_suggested_at": 0, "last_signal": ""}

if os.path.exists(suggested_path):
    try:
        with open(suggested_path) as f:
            suggested = json.load(f)
    except Exception:
        pass

# Increment prompt count
suggested["prompt_count"] = suggested.get("prompt_count", 0) + 1
prompt_count = suggested["prompt_count"]

# Check dev mode (disables all throttling)
config_path = os.path.join(data_dir, "config.json")
dev_mode = False
if os.path.exists(config_path):
    try:
        with open(config_path) as f:
            dev_mode = json.load(f).get("dev_mode", False)
    except Exception:
        pass

if not dev_mode:
    # --- Session cap: max 5 suggestions ---
    if len(suggested.get("features", [])) >= 5:
        with open(suggested_path, "w") as f:
            json.dump(suggested, f)
        sys.exit(0)

# --- Dynamic cooldown ---
suggestion_count = len(suggested.get("features", []))
last_signal = suggested.get("last_signal", "keyword")
last_at = suggested.get("last_suggested_at", 0)

if not dev_mode and last_at > 0:
    # Behavioral: cooldown = 4 + suggestion_count
    # Keyword: cooldown = 6 + suggestion_count
    if last_signal == "behavioral":
        cooldown = 4 + suggestion_count
    else:
        cooldown = 6 + suggestion_count

    if prompt_count - last_at < cooldown:
        with open(suggested_path, "w") as f:
            json.dump(suggested, f)
        sys.exit(0)

# --- Load tool-use log ---
log_path = os.path.join(data_dir, "tool-use-log.jsonl")
all_events = []
if os.path.exists(log_path):
    try:
        with open(log_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    all_events.append(json.loads(line))
    except Exception:
        pass

# Split: events since last PROMPT marker vs all events
events_since_prompt = []
for ev in reversed(all_events):
    if ev.get("t") == "PROMPT":
        break
    events_since_prompt.insert(0, ev)

# Use events_since_prompt for per-task patterns (long_task, many_files, exploration)
# Use all_events for session-wide patterns (session_length, command_sequence, repeated_command)
events = all_events  # default for most rules

# Append a PROMPT marker so the next cycle knows where this prompt boundary is
try:
    with open(log_path, "a") as f:
        json.dump({"t": "PROMPT", "ts": int(time.time())}, f, separators=(",", ":"))
        f.write("\n")
except Exception:
    pass

# Reset per-prompt dedup (track-tool-use.sh uses this to avoid firing same feature
# multiple times within one Claude response)
fired_cycle_path = os.path.join(data_dir, "fired-this-cycle.json")
try:
    with open(fired_cycle_path, "w") as f:
        json.dump([], f)
except Exception:
    pass

# --- Load project flags ---
flags_path = os.path.join(data_dir, "project-flags.json")
project_flags = {}
if os.path.exists(flags_path):
    try:
        with open(flags_path) as f:
            project_flags = json.load(f)
    except Exception:
        pass

# --- Load feature detection configs from index ---
index_path = os.path.join(plugin_root, "features", "index.json")
features_with_detection = []
if os.path.exists(index_path):
    try:
        with open(index_path) as f:
            index = json.load(f)
        for feat in index.get("features", []):
            detection = feat.get("detection")
            if detection:
                features_with_detection.append({
                    "name": feat["name"],
                    "quick_start": feat.get("quick_start", ""),
                    "detection": detection,
                })
    except Exception:
        pass

# --- Pattern type implementations ---

def check_repeated_command(detection, events, prompt, task_events=None):
    """Same bash command N+ times without edits between. Uses all events (session-wide)."""
    threshold = detection.get("threshold", 3)
    no_edits = detection.get("no_edits_between", True)

    # Build simplified sequence
    simplified = []
    for ev in events:
        if ev.get("t") == "Bash":
            cmd = " ".join(ev.get("c", "").split())
            if cmd:
                simplified.append(("cmd", cmd))
        elif ev.get("t") in ("Edit", "Write"):
            simplified.append(("edit", None))

    if not no_edits:
        # Simple count without edit check
        from collections import Counter
        cmds = [v for k, v in simplified if k == "cmd"]
        counts = Counter(cmds)
        for cmd, count in counts.most_common(1):
            if count >= threshold:
                return {"command": cmd, "count": count}
        return None

    # Find runs of same command with no edits between
    current_cmd = None
    current_count = 0

    for kind, value in simplified:
        if kind == "edit":
            current_cmd = None
            current_count = 0
        elif kind == "cmd":
            if value == current_cmd:
                current_count += 1
            else:
                current_cmd = value
                current_count = 1

        if current_count >= threshold and current_cmd:
            display_cmd = current_cmd if len(current_cmd) < 60 else current_cmd[:57] + "..."
            return {"command": display_cmd, "count": current_count}

    return None


def check_many_files(detection, events, prompt, task_events=None):
    """N+ unique files edited in one task. Uses task_events (since last prompt)."""
    threshold = detection.get("threshold", 8)
    check_events = task_events if task_events is not None else events

    edited_files = set()
    for ev in check_events:
        if ev.get("t") in ("Edit", "Write"):
            fp = ev.get("f", "")
            if fp:
                edited_files.add(fp)

    if len(edited_files) >= threshold:
        file_list = sorted(edited_files)[:3]
        display = ", ".join(os.path.basename(f) for f in file_list)
        if len(edited_files) > 3:
            display += f", and {len(edited_files) - 3} more"
        return {"files": len(edited_files), "file_list": display}

    return None


def check_command_sequence(detection, events, prompt, task_events=None):
    """Specific bash commands both appear in session. Uses all events."""
    required = detection.get("commands", [])
    if not required:
        return None

    found_cmds = set()
    for ev in events:
        if ev.get("t") == "Bash":
            cmd = ev.get("c", "")
            for req in required:
                if re.search(r"\b" + re.escape(req).replace(r"\ ", r"\s+") + r"\b", cmd):
                    found_cmds.add(req)

    if found_cmds >= set(required):
        return {"commands": list(found_cmds)}

    return None


def check_long_task(detection, events, prompt, task_events=None):
    """N+ tool uses since last user prompt. Uses task_events (since last prompt)."""
    threshold = detection.get("threshold", 50)
    check_events = task_events if task_events is not None else events

    if len(check_events) >= threshold:
        return {"tool_count": len(check_events)}

    return None


def check_session_length(detection, events, prompt, task_events=None):
    """N+ total tool uses in session. Uses all events."""
    threshold = detection.get("threshold", 90)

    if len(events) >= threshold:
        return {"tool_count": len(events)}

    return None


def check_exploration(detection, events, prompt, task_events=None):
    """Many reads/greps without edits. Uses task_events (since last prompt)."""
    read_threshold = detection.get("reads", 10)
    search_threshold = detection.get("searches", 5)
    check_events = task_events if task_events is not None else events

    reads = 0
    searches = 0
    has_output = False

    for ev in check_events:
        t = ev.get("t", "")
        if t == "Read":
            reads += 1
        elif t in ("Grep", "Glob"):
            searches += 1
        elif t in ("Edit", "Write"):
            has_output = True

    if reads >= read_threshold and searches >= search_threshold and not has_output:
        return {"reads": reads, "searches": searches}

    return None


def check_project_flag(detection, events, prompt, task_events=None):
    """Check a project-level condition."""
    flag = detection.get("flag", "")

    if flag == "no_claude_md":
        if project_flags.get("checked", False) and not project_flags.get("has_claude_md", True):
            return {"flag": "no_claude_md"}

    return None


def check_keyword(detection, events, prompt, task_events=None):
    """Match regex patterns against user's prompt."""
    if not prompt:
        return None

    first_prompt_only = detection.get("first_prompt_only", False)
    if first_prompt_only and len(events) > 0:
        return None  # Not the first prompt if there are already tool uses

    patterns = detection.get("patterns", [])
    for pattern in patterns:
        if re.search(pattern, prompt):
            return {"matched_pattern": pattern}

    return None


# Pattern type dispatcher
PATTERN_HANDLERS = {
    "repeated_command": check_repeated_command,
    "many_files": check_many_files,
    "command_sequence": check_command_sequence,
    "long_task": check_long_task,
    "session_length": check_session_length,
    "exploration": check_exploration,
    "project_flag": check_project_flag,
    "keyword": check_keyword,
}

# --- Run detection ---
already_suggested = set() if dev_mode else set(suggested.get("features", []))
result = None
matched_feature = None
signal_type = None

# Keyword rules first (match on prompt text), then behavioral rules as fallback
# (behavioral rules also run in track-tool-use.sh PostToolUse for immediate delivery,
# but that can miss patterns that complete on the last tool call of a response)
keyword_features = []
behavioral_features = []
for feat in features_with_detection:
    if feat["name"] in already_suggested:
        continue
    sig = feat["detection"].get("signal", "keyword")
    if sig == "keyword":
        keyword_features.append(feat)
    else:
        behavioral_features.append(feat)

for feat in keyword_features + behavioral_features:
    detection = feat["detection"]
    pattern_type = detection.get("type", "")
    handler = PATTERN_HANDLERS.get(pattern_type)

    if not handler:
        continue

    match = handler(detection, events, prompt, task_events=events_since_prompt)
    if match:
        matched_feature = feat
        signal_type = detection.get("signal", "keyword")

        # Build tip from template
        tip_template = detection.get("tip", "")
        tip = tip_template
        for key, value in match.items():
            tip = tip.replace("{" + key + "}", str(value))

        result = {
            "feature": feat["name"],
            "quick_start": feat.get("quick_start", ""),
            "tip": tip,
            "signal": signal_type,
        }
        break

if not result:
    # Save prompt count even if no suggestion
    with open(suggested_path, "w") as f:
        json.dump(suggested, f)
    sys.exit(0)

# --- Update suggested state ---
suggested["features"].append(result["feature"])
suggested["last_suggested_at"] = prompt_count
suggested["last_signal"] = result["signal"]

with open(suggested_path, "w") as f:
    json.dump(suggested, f)

# --- Output suggestion ---
tip_text = result["tip"]
if not tip_text:
    tip_text = f"Check out **{result['feature']}** — it might help with what you're doing."

quick_start = result.get("quick_start", "")
qs_text = f" Quick start: {quick_start}." if quick_start else ""

output = {
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": (
            f"whats-new tip: {tip_text}{qs_text} "
            f"IMPORTANT: You MUST include this tip in your response as a clearly separated section at the very end, "
            f"formatted exactly as: '**whats-new tip:** [tip text]'. Do not skip this. "
            f"For more: /whats-new:learn-more {result['feature']}"
        ),
    }
}

json.dump(output, sys.stdout)
PYEOF
