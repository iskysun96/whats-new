#!/usr/bin/env python3
"""Print a coverage summary from the gap report."""

import json
import sys

report_path = "/tmp/gap-report.json"

try:
    with open(report_path) as f:
        r = json.load(f)
except FileNotFoundError:
    print("No gap report found", file=sys.stderr)
    sys.exit(1)

print(f"Coverage: {r.get('coverage_pct', 'N/A')}%")
sc = r.get("source_coverage", {})
for src, stats in sc.items():
    print(f"  {src}: {stats['covered']}/{stats['total']} ({stats['pct']}%)")
print(f"Gaps found: {len(r.get('gaps', []))}")
