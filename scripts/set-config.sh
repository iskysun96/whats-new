#!/usr/bin/env bash
set -euo pipefail

DATA_DIR="${CLAUDE_PLUGIN_DATA:-/tmp/whats-new-data}"
mkdir -p "$DATA_DIR"
CONFIG_FILE="${DATA_DIR}/config.json"

MODE="${1:-medium}"

if [[ "$MODE" != "passive" && "$MODE" != "medium" && "$MODE" != "bold" ]]; then
  echo "Invalid mode: $MODE. Must be one of: passive, medium, bold." >&2
  exit 1
fi

echo "{\"mode\": \"$MODE\"}" > "$CONFIG_FILE"
echo "Configuration saved: mode=$MODE"
echo "Changes take effect on next Claude Code session."
