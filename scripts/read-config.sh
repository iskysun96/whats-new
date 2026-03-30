#!/usr/bin/env bash
set -euo pipefail

DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"

if [[ -z "$DATA_DIR" ]]; then
  echo '{"mode": "medium"}'
  exit 0
fi

CONFIG_FILE="${DATA_DIR}/config.json"

if [[ -f "$CONFIG_FILE" ]]; then
  cat "$CONFIG_FILE"
else
  echo '{"mode": "medium"}'
fi
