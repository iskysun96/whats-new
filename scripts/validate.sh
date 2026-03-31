#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_ROOT="${SCRIPT_DIR}/.."
FEATURES_DIR="${PLUGIN_ROOT}/features"
ENTRIES_DIR="${FEATURES_DIR}/entries"
INDEX_FILE="${FEATURES_DIR}/index.json"

ERRORS=0

echo "=== whats-new Plugin Validation ==="
echo ""

# Check plugin manifest
echo "1. Checking plugin manifest..."
if [[ -f "${PLUGIN_ROOT}/.claude-plugin/plugin.json" ]]; then
  echo "   ✓ plugin.json exists"
  if python3 -c "import json; json.load(open('${PLUGIN_ROOT}/.claude-plugin/plugin.json'))" 2>/dev/null; then
    echo "   ✓ plugin.json is valid JSON"
  else
    echo "   ✗ plugin.json is NOT valid JSON"
    ERRORS=$((ERRORS + 1))
  fi
else
  echo "   ✗ plugin.json missing"
  ERRORS=$((ERRORS + 1))
fi

# Check skills
echo ""
echo "2. Checking skills..."
for skill in discover surprise-me list configure; do
  if [[ -f "${PLUGIN_ROOT}/skills/${skill}/SKILL.md" ]]; then
    echo "   ✓ skills/${skill}/SKILL.md exists"
  else
    echo "   ✗ skills/${skill}/SKILL.md missing"
    ERRORS=$((ERRORS + 1))
  fi
done

# Check hooks
echo ""
echo "3. Checking hooks..."
if [[ -f "${PLUGIN_ROOT}/hooks/hooks.json" ]]; then
  echo "   ✓ hooks/hooks.json exists"
  if python3 -c "import json; json.load(open('${PLUGIN_ROOT}/hooks/hooks.json'))" 2>/dev/null; then
    echo "   ✓ hooks.json is valid JSON"
  else
    echo "   ✗ hooks.json is NOT valid JSON"
    ERRORS=$((ERRORS + 1))
  fi
else
  echo "   ✗ hooks/hooks.json missing"
  ERRORS=$((ERRORS + 1))
fi

# Check scripts
echo ""
echo "4. Checking scripts..."
for script in session-start.sh pick-random-feature.sh list-features.sh build-index.sh track-tool-use.sh prompt-suggest.sh; do
  if [[ -f "${PLUGIN_ROOT}/scripts/${script}" ]]; then
    if [[ -x "${PLUGIN_ROOT}/scripts/${script}" ]]; then
      echo "   ✓ scripts/${script} (executable)"
    else
      echo "   ⚠ scripts/${script} exists but NOT executable"
    fi
  else
    echo "   ✗ scripts/${script} missing"
    ERRORS=$((ERRORS + 1))
  fi
done

# Check index
echo ""
echo "5. Checking feature index..."
if [[ -f "$INDEX_FILE" ]]; then
  echo "   ✓ index.json exists"

  python3 -c "
import json, os, sys

index_path = '$INDEX_FILE'
entries_dir = '$ENTRIES_DIR'
errors = 0

with open(index_path) as f:
    data = json.load(f)

features = data.get('features', [])
categories = data.get('categories', [])

print(f'   ✓ {len(features)} features in index')
print(f'   ✓ {len(categories)} categories: {\", \".join(categories)}')

# Check each feature in index has a file
ids_seen = set()
for feat in features:
    fid = feat['id']
    if fid in ids_seen:
        print(f'   ✗ Duplicate ID: {fid}')
        errors += 1
    ids_seen.add(fid)

    filepath = os.path.join(entries_dir, os.path.basename(feat['file']))
    if not os.path.exists(filepath):
        print(f'   ✗ Missing file for {fid}: {feat[\"file\"]}')
        errors += 1

    # Check required fields
    for field in ['name', 'category', 'one_liner', 'tags', 'status']:
        if field not in feat or not feat[field]:
            print(f'   ⚠ Feature {fid} missing field: {field}')

# Check for orphan files
index_files = {os.path.basename(f['file']) for f in features}
for fname in os.listdir(entries_dir):
    if fname.endswith('.md') and fname not in index_files:
        print(f'   ⚠ Orphan file not in index: {fname}')

# Check statuses are valid
valid_statuses = {'ga', 'public-beta', 'private-beta', 'experimental', 'deprecated'}
for feat in features:
    status = feat.get('status', '')
    if status not in valid_statuses:
        print(f'   ⚠ Feature {feat[\"id\"]} has invalid status: {status}')

sys.exit(errors)
" || ERRORS=$((ERRORS + $?))

else
  echo "   ✗ index.json missing"
  ERRORS=$((ERRORS + 1))
fi

# Check feature entry content
echo ""
echo "6. Checking feature entry content..."
python3 -c "
import os, re, sys

entries_dir = '$ENTRIES_DIR'
warnings = 0
errors = 0

required_sections = ['What it does', 'When to use it', 'How to use it']
required_frontmatter = ['name', 'category', 'status', 'one_liner', 'tags']

for fname in sorted(os.listdir(entries_dir)):
    if not fname.endswith('.md'):
        continue
    filepath = os.path.join(entries_dir, fname)
    with open(filepath) as f:
        content = f.read()

    # Check frontmatter exists
    if not re.match(r'^---\n', content):
        print(f'   ✗ {fname}: No frontmatter')
        errors += 1
        continue

    # Check required frontmatter fields
    for field in required_frontmatter:
        if not re.search(rf'^{field}:', content, re.MULTILINE):
            print(f'   ⚠ {fname}: Missing frontmatter field \"{field}\"')
            warnings += 1

    # Check required sections
    for section in required_sections:
        if f'## {section}' not in content:
            print(f'   ⚠ {fname}: Missing section \"## {section}\"')
            warnings += 1

total = len([f for f in os.listdir(entries_dir) if f.endswith('.md')])
print(f'   Checked {total} entries: {errors} errors, {warnings} warnings')
sys.exit(errors)
" || ERRORS=$((ERRORS + $?))

# Summary
echo ""
echo "=== Validation Complete ==="
if [[ $ERRORS -eq 0 ]]; then
  echo "✓ All checks passed!"
  exit 0
else
  echo "✗ ${ERRORS} error(s) found"
  exit 1
fi
