#!/usr/bin/env python3
"""
Classify changelog entries and generate feature files for major new features.

Step 1: Use Claude Haiku to classify entries as MAJOR or MINOR.
Step 2: Use Claude Sonnet to generate feature entry markdown for MAJOR entries.
Step 3: Detect status changes for existing features.
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


def classify_entries(client: anthropic.Anthropic, entries: dict) -> dict:
    """
    Classify changelog entries as MAJOR or MINOR using Haiku.

    MAJOR: New user-facing feature, new mode, new platform, significant capability.
    MINOR: Bug fix, performance improvement, small UI tweak, internal refactor.
    """
    all_entries = []
    for version, items in entries.items():
        for item in items:
            all_entries.append({"version": version, "entry": item})

    if not all_entries:
        return {"major": [], "minor": []}

    entries_text = "\n".join(
        f"- [{e['version']}] {e['entry']}" for e in all_entries
    )

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f"""Classify each changelog entry as MAJOR or MINOR.

MAJOR means: New user-facing feature or capability, new mode, new platform/integration,
significant workflow change, new tool, or a feature transitioning from beta to GA.
Users need to learn about MAJOR features.

MINOR means: Bug fix, performance improvement, small UI tweak, internal refactor,
dependency update, typo fix, or small enhancement to existing feature.
Users don't need to specifically learn about MINOR changes.

Also detect STATUS CHANGES: If an entry mentions a feature becoming "generally available",
"public beta", "now available to all", etc., mark it as STATUS_CHANGE and note which
feature changed status.

Return valid JSON with this structure:
{{
  "major": [
    {{"version": "X.X.X", "entry": "the entry text", "suggested_name": "Feature Name", "suggested_category": "Category"}}
  ],
  "minor": [
    {{"version": "X.X.X", "entry": "the entry text"}}
  ],
  "status_changes": [
    {{"version": "X.X.X", "entry": "the entry text", "feature_name": "Existing Feature", "new_status": "ga"}}
  ]
}}

Changelog entries:
{entries_text}""",
            }
        ],
    )

    # Parse response
    response_text = response.content[0].text

    # Extract JSON from response
    json_match = re.search(r"\{[\s\S]*\}", response_text)
    if not json_match:
        print("WARNING: Could not parse classification response", file=sys.stderr)
        return {"major": [], "minor": [], "status_changes": []}

    try:
        return json.loads(json_match.group())
    except json.JSONDecodeError:
        print("WARNING: Invalid JSON in classification response", file=sys.stderr)
        return {"major": [], "minor": [], "status_changes": []}


def generate_feature_entry(
    client: anthropic.Anthropic, entry: dict, existing_categories: list
) -> str:
    """Generate a feature entry markdown file using Sonnet."""
    categories_str = ", ".join(existing_categories)

    response = client.messages.create(
        model="claude-sonnet-4-5-20250514",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"""Generate a Claude Code feature entry markdown file for this new feature.

Changelog entry: [{entry['version']}] {entry['entry']}
Suggested name: {entry.get('suggested_name', 'Unknown')}
Suggested category: {entry.get('suggested_category', 'Uncategorized')}
Existing categories: {categories_str}

Use this exact format:

---
name: Feature Name
category: Category Name
introduced_version: "{entry['version']}"
introduced_date: {date.today().isoformat()}
status: ga
ga_version: "{entry['version']}"
ga_date: {date.today().isoformat()}
one_liner: "One compelling sentence about what this feature does"
tags: [tag1, tag2, tag3, tag4]
---

## What it does
[2-3 sentences in conversational tone. Explain what this feature does in plain language.]

## When to use it
- [3-5 bullet points with real-world scenarios]

## How to use it
[Step-by-step instructions with actual commands/keystrokes]

## Pro tips
- [2-3 advanced usage tips]

## Status history
- **{date.today().isoformat()} (v{entry['version']})**: Introduced as generally available

Guidelines:
- Use an existing category from the list if one fits. Only create a new category if nothing fits.
- Write in a conversational, friendly tone — like a colleague explaining something cool.
- Be specific about commands and keystrokes.
- Set status based on the changelog language. If it says "research preview" or "beta", use private-beta or public-beta.
- Tags should be lowercase, hyphenated, and include relevant keywords for search.
- The one_liner should be compelling but honest — not marketing hype.

Return ONLY the markdown content, no surrounding code blocks or explanation.""",
            }
        ],
    )

    return response.content[0].text.strip()


def slugify(name: str) -> str:
    """Convert feature name to filename slug."""
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def main():
    # Check for new entries
    entries_path = "/tmp/new-changelog-entries.json"
    if not os.path.exists(entries_path):
        print("No new entries file found. Run extract step first.")
        return

    with open(entries_path) as f:
        data = json.load(f)

    new_versions = data.get("new_versions", {})
    latest_version = data.get("latest_version", "")

    if not new_versions:
        print("No new versions to process.")
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

    # Step 1: Classify
    print("Classifying entries...")
    classified = classify_entries(client, new_versions)

    major = classified.get("major", [])
    minor = classified.get("minor", [])
    status_changes = classified.get("status_changes", [])

    print(f"Classification: {len(major)} MAJOR, {len(minor)} MINOR, {len(status_changes)} STATUS_CHANGE")

    # Step 2: Generate feature entries for MAJOR items
    new_features_created = 0
    for entry in major:
        suggested_name = entry.get("suggested_name", "Unknown Feature")

        # Skip if feature already exists
        if suggested_name.lower() in existing_names:
            print(f"  Skipping '{suggested_name}' — already exists in knowledge base")
            continue

        print(f"  Generating entry for: {suggested_name}")
        markdown = generate_feature_entry(client, entry, existing_categories)

        # Write file
        filename = slugify(suggested_name) + ".md"
        filepath = os.path.join(entries_dir, filename)

        # Avoid overwriting
        if os.path.exists(filepath):
            print(f"  WARNING: {filename} already exists, skipping")
            continue

        with open(filepath, "w") as f:
            f.write(markdown + "\n")

        print(f"  Created: {filename}")
        new_features_created += 1

    # Step 3: Handle status changes
    for change in status_changes:
        feature_name = change.get("feature_name", "")
        new_status = change.get("new_status", "ga")
        version = change.get("version", "")

        # Find matching feature file
        matching_files = []
        for fname in os.listdir(entries_dir):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(entries_dir, fname)
            with open(fpath) as f:
                content = f.read()
            name_match = re.search(r"^name:\s*(.+)$", content, re.MULTILINE)
            if name_match and name_match.group(1).strip().lower() == feature_name.lower():
                matching_files.append(fpath)

        for fpath in matching_files:
            with open(fpath) as f:
                content = f.read()

            # Update status in frontmatter
            content = re.sub(
                r"^status:\s*.+$",
                f"status: {new_status}",
                content,
                flags=re.MULTILINE,
            )

            if new_status == "ga":
                # Add ga_version and ga_date if not present
                if "ga_version:" not in content:
                    content = re.sub(
                        r"(^status:\s*.+$)",
                        f'\\1\nga_version: "{version}"\nga_date: {date.today().isoformat()}',
                        content,
                        flags=re.MULTILINE,
                    )
                else:
                    content = re.sub(
                        r'^ga_version:\s*".+"$',
                        f'ga_version: "{version}"',
                        content,
                        flags=re.MULTILINE,
                    )
                    content = re.sub(
                        r"^ga_date:\s*.+$",
                        f"ga_date: {date.today().isoformat()}",
                        content,
                        flags=re.MULTILINE,
                    )

            # Append to status history
            history_entry = f"- **{date.today().isoformat()} (v{version})**: Status changed to {new_status}"
            if "## Status history" in content:
                content = content.rstrip() + f"\n{history_entry}\n"
            else:
                content = content.rstrip() + f"\n\n## Status history\n{history_entry}\n"

            with open(fpath, "w") as f:
                f.write(content)

            print(f"  Updated status for '{feature_name}' to {new_status}")

    # Update changelog_version in index
    if latest_version:
        with open(index_path) as f:
            index = json.load(f)
        index["changelog_version"] = latest_version
        with open(index_path, "w") as f:
            json.dump(index, f, indent=2)
        print(f"Updated changelog_version to {latest_version}")

    print(f"\nDone. Created {new_features_created} new feature entries.")


if __name__ == "__main__":
    main()
