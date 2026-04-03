#!/usr/bin/env python3
"""
Scrape Claude Code documentation to extract feature names and descriptions.

Fetches key structured pages from code.claude.com/docs and extracts
features, commands, skills, and tools into a machine-readable format.

Output: /tmp/docs-features.json
"""

import json
import re
import sys
from datetime import date
from urllib.error import URLError
from urllib.request import Request, urlopen

BASE_URL = "https://code.claude.com/docs"

# Pages with structured, parseable feature lists
DOC_PAGES = {
    "commands": f"{BASE_URL}/commands",
    "skills": f"{BASE_URL}/skills",
    "tools_reference": f"{BASE_URL}/tools-reference",
    "cli_reference": f"{BASE_URL}/cli-reference",
    "features_overview": f"{BASE_URL}/features-overview",
    "platforms": f"{BASE_URL}/platforms",
}

USER_AGENT = "whats-new-bot/1.0 (Claude Code feature discovery plugin)"


def fetch_page(url: str) -> str | None:
    """Fetch a documentation page. Returns HTML content or None on failure."""
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (URLError, TimeoutError) as e:
        print(f"  WARNING: Failed to fetch {url}: {e}", file=sys.stderr)
        return None


def strip_html(text: str) -> str:
    """Remove HTML tags and decode common entities."""
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&#39;", "'")
    text = text.replace("&quot;", '"')
    text = text.replace("&nbsp;", " ")
    return text.strip()


def extract_table_rows(html: str) -> list[dict]:
    """Extract rows from HTML tables as list of {header: value} dicts."""
    rows = []
    # Find all tables
    tables = re.findall(r"<table[^>]*>([\s\S]*?)</table>", html, re.IGNORECASE)
    for table in tables:
        # Extract headers
        header_match = re.findall(r"<th[^>]*>([\s\S]*?)</th>", table, re.IGNORECASE)
        headers = [strip_html(h).lower() for h in header_match]
        if not headers:
            continue

        # Extract body rows
        body_rows = re.findall(r"<tr[^>]*>([\s\S]*?)</tr>", table, re.IGNORECASE)
        for row_html in body_rows:
            cells = re.findall(r"<td[^>]*>([\s\S]*?)</td>", row_html, re.IGNORECASE)
            if len(cells) >= len(headers):
                row = {}
                for i, header in enumerate(headers):
                    row[header] = strip_html(cells[i])
                rows.append(row)
    return rows


def extract_headings_and_content(html: str) -> list[dict]:
    """Extract h2/h3 headings and their following paragraph content."""
    items = []
    # Match h2 or h3 followed by content up to next heading
    pattern = r"<h[23][^>]*>([\s\S]*?)</h[23]>([\s\S]*?)(?=<h[23]|$)"
    for match in re.finditer(pattern, html, re.IGNORECASE):
        heading = strip_html(match.group(1))
        content = strip_html(match.group(2))
        # Take first sentence or first 200 chars as description
        desc = content[:200].split(". ")[0] + "." if content else ""
        items.append({"name": heading, "description": desc})
    return items


def extract_code_references(html: str) -> list[str]:
    """Extract inline code references (commands, flags) from HTML."""
    codes = re.findall(r"<code[^>]*>([^<]+)</code>", html, re.IGNORECASE)
    return [strip_html(c) for c in codes if c.startswith(("/", "--", "claude "))]


def parse_commands_page(html: str) -> list[dict]:
    """Parse the /docs/commands page for slash commands."""
    features = []

    # Try table format first (most structured)
    rows = extract_table_rows(html)
    for row in rows:
        name = row.get("command", row.get("name", ""))
        desc = row.get("description", row.get("purpose", ""))
        if name:
            features.append({
                "name": name,
                "description": desc,
                "source_page": "commands",
                "type": "command",
            })

    # Also extract from code blocks in case some are listed outside tables
    if not features:
        codes = extract_code_references(html)
        for code in codes:
            if code.startswith("/"):
                features.append({
                    "name": code.split()[0],  # Just the command name
                    "description": "",
                    "source_page": "commands",
                    "type": "command",
                })

    return features


def parse_skills_page(html: str) -> list[dict]:
    """Parse the /docs/skills page for bundled skills."""
    features = []

    rows = extract_table_rows(html)
    for row in rows:
        name = row.get("skill", row.get("name", row.get("command", "")))
        desc = row.get("description", row.get("purpose", ""))
        if name:
            features.append({
                "name": name,
                "description": desc,
                "source_page": "skills",
                "type": "skill",
            })

    # Fallback: extract from headings
    if not features:
        headings = extract_headings_and_content(html)
        for item in headings:
            if item["name"].startswith("/") or "skill" in item["description"].lower():
                features.append({
                    "name": item["name"],
                    "description": item["description"],
                    "source_page": "skills",
                    "type": "skill",
                })

    return features


def parse_tools_page(html: str) -> list[dict]:
    """Parse the /docs/tools-reference page for internal tools."""
    features = []

    rows = extract_table_rows(html)
    for row in rows:
        name = row.get("tool", row.get("name", ""))
        desc = row.get("description", row.get("purpose", ""))
        if name:
            features.append({
                "name": name,
                "description": desc,
                "source_page": "tools_reference",
                "type": "tool",
            })

    if not features:
        headings = extract_headings_and_content(html)
        for item in headings:
            features.append({
                "name": item["name"],
                "description": item["description"],
                "source_page": "tools_reference",
                "type": "tool",
            })

    return features


def parse_cli_page(html: str) -> list[dict]:
    """Parse the /docs/cli-reference page for CLI flags and subcommands."""
    features = []

    rows = extract_table_rows(html)
    for row in rows:
        name = row.get("flag", row.get("option", row.get("command", row.get("name", ""))))
        desc = row.get("description", row.get("purpose", ""))
        if name:
            features.append({
                "name": name,
                "description": desc,
                "source_page": "cli_reference",
                "type": "cli_flag",
            })

    # Also extract --flag patterns from code blocks
    if not features:
        codes = extract_code_references(html)
        for code in codes:
            if code.startswith("--") or code.startswith("claude "):
                features.append({
                    "name": code,
                    "description": "",
                    "source_page": "cli_reference",
                    "type": "cli_flag",
                })

    return features


def parse_features_page(html: str) -> list[dict]:
    """Parse the /docs/features-overview page for high-level feature list."""
    features = []

    headings = extract_headings_and_content(html)
    for item in headings:
        if item["name"] and len(item["name"]) > 2:
            features.append({
                "name": item["name"],
                "description": item["description"],
                "source_page": "features_overview",
                "type": "feature",
            })

    return features


def parse_platforms_page(html: str) -> list[dict]:
    """Parse the /docs/platforms page for platform availability."""
    features = []

    headings = extract_headings_and_content(html)
    for item in headings:
        if item["name"] and len(item["name"]) > 2:
            features.append({
                "name": item["name"],
                "description": item["description"],
                "source_page": "platforms",
                "type": "platform",
            })

    return features


PARSERS = {
    "commands": parse_commands_page,
    "skills": parse_skills_page,
    "tools_reference": parse_tools_page,
    "cli_reference": parse_cli_page,
    "features_overview": parse_features_page,
    "platforms": parse_platforms_page,
}


def main():
    print("Scraping Claude Code documentation...")

    result = {
        "commands": [],
        "skills": [],
        "tools": [],
        "cli_flags": [],
        "features": [],
        "platforms": [],
        "scraped_at": date.today().isoformat(),
        "pages_fetched": 0,
        "pages_failed": [],
    }

    # Map source_page type to result key
    type_to_key = {
        "command": "commands",
        "skill": "skills",
        "tool": "tools",
        "cli_flag": "cli_flags",
        "feature": "features",
        "platform": "platforms",
    }

    for page_name, url in DOC_PAGES.items():
        print(f"  Fetching {page_name}: {url}")
        html = fetch_page(url)

        if html is None:
            result["pages_failed"].append(page_name)
            continue

        result["pages_fetched"] += 1

        # Cache raw HTML for debugging
        cache_path = f"/tmp/docs-page-{page_name}.html"
        with open(cache_path, "w") as f:
            f.write(html)

        # Parse with the appropriate parser
        parser = PARSERS.get(page_name)
        if parser:
            features = parser(html)
            for feat in features:
                key = type_to_key.get(feat.get("type", ""), "features")
                result[key].append(feat)
            print(f"    Found {len(features)} items")

    # Deduplicate by name within each category
    for key in type_to_key.values():
        seen = set()
        deduped = []
        for item in result[key]:
            norm = item["name"].lower().strip()
            if norm not in seen:
                seen.add(norm)
                deduped.append(item)
        result[key] = deduped

    total = sum(len(result[k]) for k in type_to_key.values())
    print(f"\nTotal unique items discovered: {total}")
    print(f"Pages fetched: {result['pages_fetched']}/{len(DOC_PAGES)}")

    if result["pages_failed"]:
        print(f"Pages failed: {', '.join(result['pages_failed'])}")

    # Write output
    output_path = "/tmp/docs-features.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Output written to {output_path}")


if __name__ == "__main__":
    main()
