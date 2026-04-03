#!/usr/bin/env python3
"""Print gap analysis details formatted for a PR body."""

import json
import sys

report_path = "/tmp/gap-report.json"

try:
    with open(report_path) as f:
        r = json.load(f)
except FileNotFoundError:
    print("No gap report available.", file=sys.stderr)
    sys.exit(0)

gaps = r.get("gaps", [])
if gaps:
    print("## New from documentation gap analysis")
    for g in gaps:
        name = g.get("name", "Unknown")
        source = g.get("source", "unknown")
        print(f"- **{name}** (source: {source})")
else:
    print("## Documentation gap analysis")
    print("No new gaps found.")

print()
print("## Coverage report")
print(f"Overall: {r.get('coverage_pct', 'N/A')}%")
sc = r.get("source_coverage", {})
for src, stats in sc.items():
    print(f"- {src}: {stats['covered']}/{stats['total']} ({stats['pct']}%)")
