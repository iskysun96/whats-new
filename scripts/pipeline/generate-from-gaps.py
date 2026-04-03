#!/usr/bin/env python3
"""
Generate feature entry files from gap analysis results.

Reads confirmed gaps from /tmp/gap-report.json and generates feature entry
markdown files using Claude Sonnet. Unlike classify-and-generate.py (which
works from changelog entries), this script has richer context from the
documentation scraper and also generates detection blocks.

Output: New .md files in features/entries/
"""

import json
import os
import re
import sys
from datetime import date

import anthropic


def load_existing_features(index_path: str) -> dict:
    """Load existing feature index."""
    if not os.path.exists(index_path):
        return {"features": [], "categories": []}
    with open(index_path) as f:
        return json.load(f)


def slugify(name: str) -> str:
    """Convert feature name to filename slug."""
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def generate_feature_entry(
    client: anthropic.Anthropic,
    gap: dict,
    existing_categories: list[str],
) -> str | None:
    """Generate a feature entry markdown file using Sonnet."""
    categories_str = ", ".join(existing_categories)

    response = client.messages.create(
        model="claude-sonnet-4-5-20250514",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"""Generate a Claude Code feature entry markdown file for a feature found
during documentation gap analysis.

Feature name: {gap.get('name', 'Unknown')}
Description from docs: {gap.get('description', 'No description available')}
Source page: {gap.get('source', 'unknown')}
Feature type: {gap.get('type', 'unknown')}
Suggested name: {gap.get('suggested_name', gap.get('name', 'Unknown'))}
Suggested category: {gap.get('suggested_category', 'Uncategorized')}
Existing categories: {categories_str}

Use this exact format:

---
name: Feature Name
category: Category Name
introduced_version: "2.1.87"
introduced_date: {date.today().isoformat()}
status: ga
ga_version: "2.1.87"
ga_date: {date.today().isoformat()}
one_liner: "One compelling sentence about what this feature does"
quick_start: "The primary command or action to try this feature"
detection:
  type: keyword
  patterns:
    - "pattern1_regex"
    - "pattern2_regex"
  tip: "Suggestion text shown to user when pattern matches."
  signal: keyword
tags: [tag1, tag2, tag3, tag4]
---

## What it does
[2-3 sentences in conversational tone. Explain what this feature does in plain language.]

## When to use it
- [3-5 bullet points with real-world scenarios]

## How to use it
[Step-by-step instructions with actual commands/keystrokes]

## Pro Tips
- [2-3 advanced usage tips]

## Status history
- **{date.today().isoformat()} (v2.1.87)**: Discovered via docs gap analysis; entry auto-generated

Guidelines:
- Use an existing category from the list if one fits.
- Write in a conversational, friendly tone — like a colleague explaining something cool.
- Be specific about commands and keystrokes.
- Include a detection block with 3-6 keyword patterns that a user might type when they'd
  benefit from knowing about this feature. Use regex patterns (e.g., "how.*do.*I.*X").
  If the feature isn't contextually triggerable (platform, setup-only), omit detection.
- Tags should be lowercase, hyphenated, and include relevant keywords for search.
- The one_liner should be compelling but honest.

Return ONLY the markdown content, no surrounding code blocks or explanation.""",
            }
        ],
    )

    return response.content[0].text.strip()


def main():
    # Load gap report
    report_path = "/tmp/gap-report.json"
    if not os.path.exists(report_path):
        print("ERROR: /tmp/gap-report.json not found. Run gap-analysis.py first.", file=sys.stderr)
        sys.exit(1)

    with open(report_path) as f:
        report = json.load(f)

    gaps = report.get("gaps", [])
    if not gaps:
        print("No gaps to generate entries for.")
        return

    # Initialize Anthropic client
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Load existing features
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plugin_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    index_path = os.path.join(plugin_root, "features", "index.json")
    entries_dir = os.path.join(plugin_root, "features", "entries")

    existing = load_existing_features(index_path)
    existing_names = {f["name"].lower() for f in existing.get("features", [])}
    existing_categories = existing.get("categories", [])

    print(f"Generating entries for {len(gaps)} gaps...")

    new_features_created = 0
    for gap in gaps:
        name = gap.get("suggested_name", gap.get("name", "Unknown"))

        # Skip if already exists
        if name.lower() in existing_names:
            print(f"  Skipping '{name}' — already exists")
            continue

        print(f"  Generating: {name}")
        markdown = generate_feature_entry(client, gap, existing_categories)

        if not markdown:
            print(f"  WARNING: Empty response for '{name}', skipping")
            continue

        # Write file
        filename = slugify(name) + ".md"
        filepath = os.path.join(entries_dir, filename)

        if os.path.exists(filepath):
            print(f"  WARNING: {filename} already exists, skipping")
            continue

        with open(filepath, "w") as f:
            f.write(markdown + "\n")

        print(f"  Created: {filename}")
        new_features_created += 1

    print(f"\nDone. Created {new_features_created} new feature entries from gap analysis.")


if __name__ == "__main__":
    main()
