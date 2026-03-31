#!/usr/bin/env bash
set -euo pipefail

# Capture stdin immediately
INPUT=$(cat)

DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"
if [[ -z "$DATA_DIR" ]]; then
  exit 0
fi

# Only run in bold mode
CONFIG_FILE="${DATA_DIR}/config.json"
MODE="medium"
if [[ -f "$CONFIG_FILE" ]]; then
  MODE=$(python3 -c "
import json
with open('$CONFIG_FILE') as f:
    print(json.load(f).get('mode', 'medium'))
" 2>/dev/null || echo "medium")
fi

if [[ "$MODE" != "bold" ]]; then
  exit 0
fi

LOG_FILE="${DATA_DIR}/tool-use-log.jsonl"
FLAGS_FILE="${DATA_DIR}/project-flags.json"

# On first run: check project flags
if [[ ! -f "$FLAGS_FILE" ]]; then
  CWD=$(python3 -c "
import json, os
data = json.loads(os.environ.get('WHATS_NEW_INPUT', '{}'))
print(data.get('cwd', os.getcwd()))
" 2>/dev/null || pwd)

  HAS_CLAUDE_MD="false"
  if [[ -f "${CWD}/CLAUDE.md" ]] || [[ -f "${CWD}/.claude/CLAUDE.md" ]] || [[ -d "${CWD}/.claude/rules" ]]; then
    HAS_CLAUDE_MD="true"
  fi

  echo "{\"has_claude_md\": ${HAS_CLAUDE_MD}, \"checked\": true}" > "$FLAGS_FILE"
fi

# Log tool use AND check behavioral patterns
export WHATS_NEW_INPUT="$INPUT"
export WHATS_NEW_DATA_DIR="$DATA_DIR"
export WHATS_NEW_PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"

python3 << 'PYEOF'
import json, os, sys, time, re

data_dir = os.environ.get("WHATS_NEW_DATA_DIR", "")
plugin_root = os.environ.get("WHATS_NEW_PLUGIN_ROOT", "")

try:
    data = json.loads(os.environ.get("WHATS_NEW_INPUT", "{}"))
except Exception:
    sys.exit(0)

tool_name = data.get("tool_name", "")
if not tool_name:
    sys.exit(0)

tool_input = data.get("tool_input", {})
record = {"t": tool_name, "ts": int(time.time())}

if tool_name == "Bash":
    record["c"] = (tool_input.get("command", "") or "")[:200]
elif tool_name in ("Edit", "Write"):
    record["f"] = tool_input.get("file_path", "")
elif tool_name == "Read":
    record["f"] = tool_input.get("file_path", "")

log_path = os.path.join(data_dir, "tool-use-log.jsonl")

# Append record
with open(log_path, "a") as f:
    json.dump(record, f, separators=(",", ":"))
    f.write("\n")

# Cap at 100 lines
lines = []
try:
    with open(log_path, "r") as f:
        lines = f.readlines()
    if len(lines) > 100:
        lines = lines[-100:]
        with open(log_path, "w") as f:
            f.writelines(lines)
except Exception:
    pass

# --- Behavioral pattern check (immediate, during Claude's response) ---

# Load suggested state
suggested_path = os.path.join(data_dir, "suggested.json")
suggested = {"features": [], "prompt_count": 0, "last_suggested_at": 0, "last_signal": ""}
if os.path.exists(suggested_path):
    try:
        with open(suggested_path) as f:
            suggested = json.load(f)
    except Exception:
        pass

# Check dev mode (disables all throttling)
config_path = os.path.join(data_dir, "config.json")
dev_mode = False
if os.path.exists(config_path):
    try:
        with open(config_path) as f:
            dev_mode = json.load(f).get("dev_mode", False)
    except Exception:
        pass

prompt_count = suggested.get("prompt_count", 0)

if not dev_mode:
    # Session cap
    if len(suggested.get("features", [])) >= 5:
        sys.exit(0)

    # Cooldown
    suggestion_count = len(suggested.get("features", []))
    last_at = suggested.get("last_suggested_at", 0)
    if last_at > 0:
        cooldown = 4 + suggestion_count  # behavioral cooldown
        if prompt_count - last_at < cooldown:
            sys.exit(0)

already_suggested = set() if dev_mode else set(suggested.get("features", []))

# Parse events
events = []
for line in lines:
    line = line.strip()
    if line:
        try:
            events.append(json.loads(line))
        except Exception:
            pass

# Load detection configs from index
index_path = os.path.join(plugin_root, "features", "index.json")
behavioral_features = []
if os.path.exists(index_path):
    try:
        with open(index_path) as f:
            index = json.load(f)
        for feat in index.get("features", []):
            det = feat.get("detection")
            if det and det.get("signal") == "behavioral" and feat["name"] not in already_suggested:
                behavioral_features.append({
                    "name": feat["name"],
                    "quick_start": feat.get("quick_start", ""),
                    "detection": det,
                })
    except Exception:
        pass

if not behavioral_features:
    sys.exit(0)

# --- Pattern checks (only behavioral, keywords stay on UserPromptSubmit) ---

def check_repeated_command(detection, events):
    threshold = detection.get("threshold", 3)
    simplified = []
    for ev in events:
        if ev.get("t") == "Bash":
            cmd = " ".join(ev.get("c", "").split())
            if cmd:
                simplified.append(("cmd", cmd))
        elif ev.get("t") in ("Edit", "Write"):
            simplified.append(("edit", None))

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
            display = current_cmd if len(current_cmd) < 60 else current_cmd[:57] + "..."
            return {"command": display, "count": current_count}
    return None

def check_many_files(detection, events):
    threshold = detection.get("threshold", 8)
    edited = set()
    for ev in events:
        if ev.get("t") in ("Edit", "Write") and ev.get("f"):
            edited.add(ev["f"])
    if len(edited) >= threshold:
        fl = sorted(edited)[:3]
        display = ", ".join(os.path.basename(f) for f in fl)
        if len(edited) > 3:
            display += f", and {len(edited) - 3} more"
        return {"files": len(edited), "file_list": display}
    return None

def check_command_sequence(detection, events):
    required = detection.get("commands", [])
    if not required:
        return None
    found = set()
    for ev in events:
        if ev.get("t") == "Bash":
            cmd = ev.get("c", "")
            for req in required:
                if re.search(r"\b" + re.escape(req).replace(r"\ ", r"\s+") + r"\b", cmd):
                    found.add(req)
    if found >= set(required):
        return {"commands": list(found)}
    return None

def check_long_task(detection, events):
    threshold = detection.get("threshold", 50)
    if len(events) >= threshold:
        return {"tool_count": len(events)}
    return None

def check_session_length(detection, events):
    threshold = detection.get("threshold", 90)
    if len(events) >= threshold:
        return {"tool_count": len(events)}
    return None

def check_exploration(detection, events):
    reads = sum(1 for e in events if e.get("t") == "Read")
    searches = sum(1 for e in events if e.get("t") in ("Grep", "Glob"))
    has_output = any(e.get("t") in ("Edit", "Write") for e in events)
    if reads >= detection.get("reads", 10) and searches >= detection.get("searches", 5) and not has_output:
        return {"reads": reads, "searches": searches}
    return None

def check_project_flag(detection, events):
    flag = detection.get("flag", "")
    flags_path = os.path.join(data_dir, "project-flags.json")
    if os.path.exists(flags_path):
        try:
            with open(flags_path) as f:
                pf = json.load(f)
            if flag == "no_claude_md" and pf.get("checked") and not pf.get("has_claude_md", True):
                return {"flag": "no_claude_md"}
        except Exception:
            pass
    return None

HANDLERS = {
    "repeated_command": check_repeated_command,
    "many_files": check_many_files,
    "command_sequence": check_command_sequence,
    "long_task": check_long_task,
    "session_length": check_session_length,
    "exploration": check_exploration,
    "project_flag": check_project_flag,
}

# Run behavioral checks
for feat in behavioral_features:
    det = feat["detection"]
    handler = HANDLERS.get(det.get("type", ""))
    if not handler:
        continue

    match = handler(det, events)
    if match:
        tip_template = det.get("tip", "")
        tip = tip_template
        for key, value in match.items():
            tip = tip.replace("{" + key + "}", str(value))

        if not tip:
            tip = f"Check out **{feat['name']}** — it might help with what you're doing."

        qs = feat.get("quick_start", "")
        qs_text = f" Quick start: {qs}." if qs else ""

        # Do NOT update suggested.json here — let prompt-suggest.sh handle dedup.
        # PostToolUse may fire on the last tool call when Claude has already
        # finished composing, so the tip might not be shown. If we recorded it
        # here, prompt-suggest.sh would skip it on the next prompt, and the
        # user would never see it.

        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": (
                    f"whats-new tip: {tip}{qs_text} "
                    f"IMPORTANT: You MUST include this tip in your response as a clearly separated section at the very end, "
                    f"formatted exactly as: '**whats-new tip:** [tip text]'. Do not skip this. "
                    f"For more: /whats-new:learn-more {feat['name']}"
                ),
            }
        }
        json.dump(output, sys.stdout)
        break
PYEOF
