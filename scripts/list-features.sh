#!/usr/bin/env bash
set -euo pipefail

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
INDEX_FILE="${PLUGIN_ROOT}/features/index.json"
FILTER="${1:-}"

# An unfilled argument placeholder can reach us as the shell's own name
# (e.g. "$0" -> /bin/zsh) or as the literal placeholder text. Treat both as "no filter".
case "$FILTER" in
  */bash|*/zsh|*/sh|bash|zsh|sh|-bash|-zsh|'$ARGUMENTS'|'$0') FILTER="" ;;
esac

# Pass values as argv so quotes or apostrophes in a filter cannot break the Python code.
python3 - "$INDEX_FILE" "$FILTER" <<'PY'
import json, sys
from collections import defaultdict

index_file, filter_arg = sys.argv[1], sys.argv[2].strip()

with open(index_file) as f:
    data = json.load(f)

features = data['features']

if filter_arg:
    filter_lower = filter_arg.lower()
    # Try category match first
    matched = [f for f in features if f['category'].lower() == filter_lower]
    if not matched:
        # Try tag match
        matched = [f for f in features if filter_lower in [t.lower() for t in f.get('tags', [])]]
    if not matched:
        # Try status match
        matched = [f for f in features if f.get('status', '').lower() == filter_lower]
    if not matched:
        # Try substring match on name/one_liner
        matched = [f for f in features if filter_lower in f['name'].lower() or filter_lower in f.get('one_liner', '').lower()]
    features = matched

def badge(status):
    badges = {
        'ga': '[GA]',
        'public-beta': '[PUBLIC BETA]',
        'private-beta': '[PRIVATE BETA]',
        'experimental': '[EXPERIMENTAL]',
        'deprecated': '[DEPRECATED]'
    }
    return badges.get(status, '[UNKNOWN]')

grouped = defaultdict(list)
for f in features:
    grouped[f['category']].append(f)

for category in sorted(grouped.keys()):
    print(f'\n## {category}')
    for f in sorted(grouped[category], key=lambda x: x['name']):
        status = badge(f.get('status', 'ga'))
        qs = f.get('quick_start', '')
        qs_str = f' — ▶ `{qs}`' if qs else ''
        print(f"  - {status} **{f['name']}**: {f.get('one_liner', '')}{qs_str}")

if not features:
    cats = ', '.join(data.get('categories', []))
    print(f'No features found matching "{filter_arg}".')
    print(f'Available categories: {cats}')
    print('Available statuses: ga, public-beta, private-beta, experimental')
PY
