#!/usr/bin/env python3
"""
Extract new changelog entries since the last known version.

Reads the latest CHANGELOG.md and compares against the version stored
in features/index.json. Outputs new entries to /tmp/new-changelog-entries.json.
"""

import json
import re
import sys
import os


def parse_changelog(content: str) -> dict[str, list[str]]:
    """Parse CHANGELOG.md into a dict of version -> list of entries."""
    versions = {}
    current_version = None
    current_entries = []

    for line in content.split("\n"):
        # Match version headers like "## 2.1.87" or "## [2.1.87]"
        version_match = re.match(r"^##\s+\[?(\d+\.\d+\.\d+)\]?", line)
        if version_match:
            if current_version:
                versions[current_version] = current_entries
            current_version = version_match.group(1)
            current_entries = []
        elif current_version and line.strip().startswith("- "):
            current_entries.append(line.strip()[2:].strip())

    # Don't forget the last version
    if current_version:
        versions[current_version] = current_entries

    return versions


def version_tuple(v: str) -> tuple[int, ...]:
    """Convert version string to comparable tuple."""
    return tuple(int(x) for x in v.split("."))


def main():
    # Read current index to get last known version
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plugin_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    index_path = os.path.join(plugin_root, "features", "index.json")

    if not os.path.exists(index_path):
        print("ERROR: features/index.json not found", file=sys.stderr)
        sys.exit(1)

    with open(index_path) as f:
        index = json.load(f)

    last_version = index.get("changelog_version", "0.0.0")
    print(f"Last known version: {last_version}")

    # Read latest changelog
    changelog_path = "/tmp/changelog-latest.md"
    if not os.path.exists(changelog_path):
        print("ERROR: /tmp/changelog-latest.md not found. Run fetch step first.", file=sys.stderr)
        sys.exit(1)

    with open(changelog_path) as f:
        changelog_content = f.read()

    # Parse changelog
    versions = parse_changelog(changelog_content)
    print(f"Found {len(versions)} versions in changelog")

    # Filter to versions newer than last known
    last_tuple = version_tuple(last_version)
    new_entries = {}

    for version, entries in versions.items():
        if version_tuple(version) > last_tuple:
            new_entries[version] = entries

    if not new_entries:
        print("No new versions found since last update.")
        # Write empty result
        with open("/tmp/new-changelog-entries.json", "w") as f:
            json.dump({"new_versions": {}, "last_version": last_version}, f, indent=2)
        return

    # Sort by version
    sorted_versions = sorted(new_entries.keys(), key=version_tuple)
    latest_version = sorted_versions[-1]

    total_entries = sum(len(e) for e in new_entries.values())
    print(f"Found {len(new_entries)} new versions with {total_entries} total entries")
    print(f"Latest version: {latest_version}")

    # Write result
    result = {
        "new_versions": {v: new_entries[v] for v in sorted_versions},
        "last_version": last_version,
        "latest_version": latest_version,
    }

    with open("/tmp/new-changelog-entries.json", "w") as f:
        json.dump(result, f, indent=2)

    print(f"New entries written to /tmp/new-changelog-entries.json")


if __name__ == "__main__":
    main()
