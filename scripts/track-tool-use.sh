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

# Extract minimal fields and append to log
export WHATS_NEW_INPUT="$INPUT"
python3 << 'PYEOF'
import json, os, sys, time

try:
    data = json.loads(os.environ.get("WHATS_NEW_INPUT", "{}"))
except Exception:
    sys.exit(0)

tool_name = data.get("tool_name", "")
if not tool_name:
    sys.exit(0)

tool_input = data.get("tool_input", {})
record = {"t": tool_name, "ts": int(time.time())}

# Extract relevant fields based on tool type
if tool_name == "Bash":
    record["c"] = (tool_input.get("command", "") or "")[:200]
elif tool_name in ("Edit", "Write"):
    record["f"] = tool_input.get("file_path", "")
elif tool_name == "Read":
    record["f"] = tool_input.get("file_path", "")

log_path = os.path.join(os.environ.get("CLAUDE_PLUGIN_DATA", "/tmp"), "tool-use-log.jsonl")

# Append record
with open(log_path, "a") as f:
    json.dump(record, f, separators=(",", ":"))
    f.write("\n")

# Cap at 100 lines
try:
    with open(log_path, "r") as f:
        lines = f.readlines()
    if len(lines) > 100:
        with open(log_path, "w") as f:
            f.writelines(lines[-100:])
except Exception:
    pass
PYEOF

exit 0
