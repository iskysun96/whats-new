#!/usr/bin/env bash
set -euo pipefail

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
INDEX_FILE="${PLUGIN_ROOT}/features/index.json"
FILTER="${1:-}"

python3 -c "
import json, sys
from collections import defaultdict

with open('$INDEX_FILE') as f:
    data = json.load(f)

filter_arg = '''$FILTER'''.strip()
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

# Status badge
def badge(status):
    badges = {
        'ga': '[GA]',
        'public-beta': '[PUBLIC BETA]',
        'private-beta': '[PRIVATE BETA]',
        'experimental': '[EXPERIMENTAL]',
        'deprecated': '[DEPRECATED]'
    }
    return badges.get(status, '[UNKNOWN]')

# Group by category
grouped = defaultdict(list)
for f in features:
    grouped[f['category']].append(f)

for category in sorted(grouped.keys()):
    print(f'\n## {category}')
    for f in sorted(grouped[category], key=lambda x: x['name']):
        status = badge(f.get('status', 'ga'))
        qs = f.get('quick_start', '')
        qs_str = f' — ▶ \`{qs}\`' if qs else ''
        print(f\"  - {status} **{f['name']}**: {f.get('one_liner', '')}{qs_str}\")

if not features:
    cats = ', '.join(data.get('categories', []))
    print(f'No features found matching \"{filter_arg}\".')
    print(f'Available categories: {cats}')
    print(f'Available statuses: ga, public-beta, private-beta, experimental')
"
