#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_ROOT="${SCRIPT_DIR}/.."
FEATURES_DIR="${PLUGIN_ROOT}/features"
ENTRIES_DIR="${FEATURES_DIR}/entries"
INDEX_FILE="${FEATURES_DIR}/index.json"

python3 -c "
import os, json, re, glob

entries_dir = '${ENTRIES_DIR}'
index_path = '${INDEX_FILE}'

features = []
categories = set()

for filepath in sorted(glob.glob(os.path.join(entries_dir, '*.md'))):
    with open(filepath) as f:
        content = f.read()

    # Parse YAML frontmatter between --- markers
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        print(f'WARNING: No frontmatter found in {filepath}, skipping')
        continue

    frontmatter_text = match.group(1)
    frontmatter = {}

    for line in frontmatter_text.strip().split('\n'):
        if ':' not in line:
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()

        # Handle quoted strings
        if val.startswith('\"') and val.endswith('\"'):
            val = val[1:-1]

        # Handle arrays
        if val.startswith('[') and val.endswith(']'):
            val = [t.strip().strip('\"') for t in val[1:-1].split(',') if t.strip()]

        frontmatter[key] = val

    feature_id = os.path.splitext(os.path.basename(filepath))[0]
    category = frontmatter.get('category', 'Uncategorized')
    categories.add(category)

    features.append({
        'id': feature_id,
        'name': frontmatter.get('name', feature_id),
        'category': category,
        'one_liner': frontmatter.get('one_liner', ''),
        'tags': frontmatter.get('tags', []),
        'status': frontmatter.get('status', 'ga'),
        'quick_start': frontmatter.get('quick_start', ''),
        'introduced_version': frontmatter.get('introduced_version', ''),
        'file': f'entries/{os.path.basename(filepath)}'
    })

# Read existing index for changelog_version
changelog_version = ''
if os.path.exists(index_path):
    try:
        with open(index_path) as f:
            old = json.load(f)
        changelog_version = old.get('changelog_version', '')
    except (json.JSONDecodeError, IOError):
        pass

from datetime import date

index = {
    'features': sorted(features, key=lambda x: x['name']),
    'categories': sorted(categories),
    'last_updated': str(date.today()),
    'changelog_version': changelog_version or '2.1.87'
}

with open(index_path, 'w') as f:
    json.dump(index, f, indent=2)

print(f'Index rebuilt: {len(features)} features in {len(categories)} categories')
"
