#!/usr/bin/env bash
set -euo pipefail

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"
if [[ -z "$DATA_DIR" ]]; then
  DATA_DIR="/tmp/whats-new-data"
fi
INDEX_FILE="${PLUGIN_ROOT}/features/index.json"
SEEN_FILE="${DATA_DIR}/seen.json"

mkdir -p "$DATA_DIR"

python3 -c "
import json, os, random

index_path = '$INDEX_FILE'
seen_path = '$SEEN_FILE'

with open(index_path) as f:
    data = json.load(f)

all_features = [feat['file'] for feat in data['features']]

seen = []
if os.path.exists(seen_path):
    try:
        with open(seen_path) as f:
            seen = json.load(f)
    except (json.JSONDecodeError, IOError):
        seen = []

# Filter out recently seen (last 7)
recent = set(seen[-7:])
available = [f for f in all_features if f not in recent]

# Reset if all have been seen
if not available:
    available = all_features

chosen = random.choice(available)

# Update seen list (keep last 50)
seen.append(chosen)
seen = seen[-50:]
with open(seen_path, 'w') as f:
    json.dump(seen, f)

print(chosen)
"
