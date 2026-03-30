#!/usr/bin/env bash
set -euo pipefail

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
DATA_DIR="${CLAUDE_PLUGIN_DATA:-/tmp/whats-new-data}"
CONFIG_FILE="${DATA_DIR}/config.json"

# Read config, default to "medium"
MODE="medium"
if [[ -f "$CONFIG_FILE" ]]; then
  MODE=$(python3 -c "
import json
with open('$CONFIG_FILE') as f:
    print(json.load(f).get('mode', 'medium'))
" 2>/dev/null || echo "medium")
fi

# Passive mode: exit silently
if [[ "$MODE" == "passive" ]]; then
  exit 0
fi

# Pick feature of the day
FEATURE_FILE=$(bash "${PLUGIN_ROOT}/scripts/pick-random-feature.sh" 2>/dev/null || echo "")

if [[ -z "$FEATURE_FILE" ]]; then
  exit 0
fi

FULL_PATH="${PLUGIN_ROOT}/features/${FEATURE_FILE}"

if [[ ! -f "$FULL_PATH" ]]; then
  exit 0
fi

# Extract name and one_liner from frontmatter
FEATURE_NAME=$(python3 -c "
import re
with open('$FULL_PATH') as f:
    content = f.read()
match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
print(match.group(1).strip() if match else 'Unknown Feature')
" 2>/dev/null || echo "Unknown Feature")

ONE_LINER=$(python3 -c "
import re
with open('$FULL_PATH') as f:
    content = f.read()
match = re.search(r'^one_liner:\s*\"(.+)\"$', content, re.MULTILINE)
print(match.group(1) if match else '')
" 2>/dev/null || echo "")

STATUS=$(python3 -c "
import re
with open('$FULL_PATH') as f:
    content = f.read()
match = re.search(r'^status:\s*(.+)$', content, re.MULTILINE)
print(match.group(1).strip() if match else 'ga')
" 2>/dev/null || echo "ga")

STATUS_NOTE=""
if [[ "$STATUS" != "ga" ]]; then
  STATUS_NOTE=" (Status: ${STATUS} - may not be available to all users)"
fi

# Save last shown feature so /whats-new:learn-more can find it
mkdir -p "$DATA_DIR"
echo "$FEATURE_FILE" > "${DATA_DIR}/last-feature.txt"

TIP_MESSAGE="whats-new Feature of the Day: ${FEATURE_NAME} - ${ONE_LINER}${STATUS_NOTE}. Type /whats-new:learn-more to dive deeper into this feature."

if [[ "$MODE" == "medium" ]]; then
  cat <<ENDJSON
{
  "systemMessage": "${TIP_MESSAGE}",
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "${TIP_MESSAGE}"
  }
}
ENDJSON

elif [[ "$MODE" == "bold" ]]; then
  cat <<ENDJSON
{
  "systemMessage": "${TIP_MESSAGE}",
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "${TIP_MESSAGE}\n\nPROACTIVE FEATURE SUGGESTIONS ENABLED: You have access to a Claude Code features knowledge base via the whats-new plugin. Throughout this session, when you notice the user could benefit from a Claude Code feature they might not know about, briefly mention it in 1-2 sentences. Keep it natural and helpful, not pushy. Only suggest features with status 'ga' unless the user specifically asks about beta features. Available commands: /whats-new:discover [topic], /whats-new:surprise, /whats-new:list [category]."
  }
}
ENDJSON
fi

exit 0
