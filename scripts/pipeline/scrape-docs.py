#!/usr/bin/env python3
"""
Scrape Claude Code documentation to extract feature names and descriptions.

Primary discovery: Parse sitemap.xml to find ALL doc pages, then fetch
each page to extract titles and descriptions.

Secondary: Also parse specific structured pages (commands, skills, etc.)
for richer extraction of individual items within those pages.

Output: /tmp/docs-features.json
"""

import json
import re
import sys
from datetime import date
from urllib.error import URLError
from urllib.request import Request, urlopen
from xml.etree import ElementTree

SITEMAP_URL = "https://code.claude.com/sitemap.xml"
BASE_URL = "https://code.claude.com/docs"

# Structured pages with table/list formats for detailed extraction
STRUCTURED_PAGES = {
    "commands": f"{BASE_URL}/en/commands",
    "skills": f"{BASE_URL}/en/skills",
    "tools_reference": f"{BASE_URL}/en/tools-reference",
    "cli_reference": f"{BASE_URL}/en/cli-reference",
    "features_overview": f"{BASE_URL}/en/features-overview",
    "platforms": f"{BASE_URL}/en/platforms",
}

# Pages that are informational/meta and not features themselves
NON_FEATURE_SLUGS = {
    "overview", "quickstart", "setup", "common-workflows", "best-practices",
    "interactive-mode", "how-claude-code-works", "changelog",
    "data-usage", "legal-and-compliance", "zero-data-retention", "analytics",
    "monitoring-usage", "network-config", "security", "troubleshooting",
    "costs", "env-vars", "settings", "discover-plugins", "plugin-marketplaces",
    "plugins-reference", "channels-reference", "hooks-guide",
    "claude-directory", "features-overview",
}

USER_AGENT = "whats-new-bot/1.0 (Claude Code feature discovery plugin)"


def fetch_page(url: str) -> str | None:
    """Fetch a page. Returns content or None on failure."""
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
    for entity, char in [("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                         ("&#39;", "'"), ("&quot;", '"'), ("&nbsp;", " ")]:
        text = text.replace(entity, char)
    return text.strip()


# ──────────────────────────────────────────────────
# Sitemap-based discovery (primary)
# ──────────────────────────────────────────────────

def parse_sitemap(xml_content: str) -> list[dict]:
    """Parse sitemap.xml and return English doc page entries."""
    pages = []
    try:
        root = ElementTree.fromstring(xml_content)
    except ElementTree.ParseError as e:
        print(f"  WARNING: Failed to parse sitemap XML: {e}", file=sys.stderr)
        return pages

    # Handle XML namespaces (sitemaps use xmlns)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    for url_elem in root.findall(".//sm:url", ns):
        loc = url_elem.findtext("sm:loc", default="", namespaces=ns)
        lastmod = url_elem.findtext("sm:lastmod", default="", namespaces=ns)

        # Filter to English doc pages only
        if "/docs/en/" not in loc:
            continue

        # Extract slug from URL
        slug = loc.rstrip("/").split("/")[-1]

        pages.append({
            "url": loc,
            "slug": slug,
            "lastmod": lastmod,
        })

    return pages


def extract_page_title(html: str) -> str:
    """Extract the page title from HTML."""
    # Try <title> tag
    match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if match:
        title = strip_html(match.group(1))
        # Remove site suffix like " | Claude Code" or " - Claude Code"
        title = re.split(r"\s*[|–—-]\s*Claude", title)[0].strip()
        return title

    # Try first <h1>
    match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
    if match:
        return strip_html(match.group(1))

    return ""


def extract_page_description(html: str) -> str:
    """Extract the first meaningful paragraph as description."""
    # Try meta description
    match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html, re.IGNORECASE)
    if match:
        return match.group(1).strip()

    # Try first <p> after the first heading
    match = re.search(r"<h[12][^>]*>.*?</h[12]>\s*<p[^>]*>(.*?)</p>", html, re.IGNORECASE | re.DOTALL)
    if match:
        desc = strip_html(match.group(1))
        if len(desc) > 20:
            return desc[:200].rsplit(". ", 1)[0] + "." if ". " in desc[:200] else desc[:200]

    return ""


def discover_from_sitemap() -> list[dict]:
    """Fetch sitemap and discover all doc pages."""
    print("Fetching sitemap...")
    xml = fetch_page(SITEMAP_URL)
    if not xml:
        print("  WARNING: Could not fetch sitemap, falling back to structured pages only", file=sys.stderr)
        return []

    pages = parse_sitemap(xml)
    print(f"  Found {len(pages)} English doc pages in sitemap")

    # Filter out non-feature pages
    feature_pages = [p for p in pages if p["slug"] not in NON_FEATURE_SLUGS]
    print(f"  {len(feature_pages)} potential feature pages after filtering")

    # Fetch each feature page to extract title and description
    discovered = []
    for page in feature_pages:
        print(f"  Fetching {page['slug']}...")
        html = fetch_page(page["url"])
        if not html:
            continue

        title = extract_page_title(html)
        description = extract_page_description(html)

        if title:
            discovered.append({
                "name": title,
                "description": description,
                "source_page": "sitemap",
                "type": "doc_page",
                "slug": page["slug"],
                "lastmod": page.get("lastmod", ""),
                "url": page["url"],
            })

    print(f"  Extracted {len(discovered)} features from sitemap pages")
    return discovered


# ──────────────────────────────────────────────────
# Structured page parsing (secondary, for detail)
# ──────────────────────────────────────────────────

def extract_table_rows(html: str) -> list[dict]:
    """Extract rows from HTML tables as list of {header: value} dicts."""
    rows = []
    tables = re.findall(r"<table[^>]*>([\s\S]*?)</table>", html, re.IGNORECASE)
    for table in tables:
        header_match = re.findall(r"<th[^>]*>([\s\S]*?)</th>", table, re.IGNORECASE)
        headers = [strip_html(h).lower() for h in header_match]
        if not headers:
            continue
        body_rows = re.findall(r"<tr[^>]*>([\s\S]*?)</tr>", table, re.IGNORECASE)
        for row_html in body_rows:
            cells = re.findall(r"<td[^>]*>([\s\S]*?)</td>", row_html, re.IGNORECASE)
            if len(cells) >= len(headers):
                row = {headers[i]: strip_html(cells[i]) for i in range(len(headers))}
                rows.append(row)
    return rows


def extract_headings_and_content(html: str) -> list[dict]:
    """Extract h2/h3 headings and their following paragraph content."""
    items = []
    pattern = r"<h[23][^>]*>([\s\S]*?)</h[23]>([\s\S]*?)(?=<h[23]|$)"
    for match in re.finditer(pattern, html, re.IGNORECASE):
        heading = strip_html(match.group(1))
        content = strip_html(match.group(2))
        desc = content[:200].split(". ")[0] + "." if content else ""
        items.append({"name": heading, "description": desc})
    return items


def parse_commands_page(html: str) -> list[dict]:
    """Parse the /docs/commands page for slash commands."""
    features = []
    rows = extract_table_rows(html)
    for row in rows:
        name = row.get("command", row.get("name", ""))
        desc = row.get("description", row.get("purpose", ""))
        if name:
            features.append({
                "name": name, "description": desc,
                "source_page": "commands", "type": "command",
            })
    if not features:
        codes = re.findall(r"<code[^>]*>(/[^<]+)</code>", html, re.IGNORECASE)
        for code in codes:
            features.append({
                "name": code.split()[0], "description": "",
                "source_page": "commands", "type": "command",
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
                "name": name, "description": desc,
                "source_page": "skills", "type": "skill",
            })
    if not features:
        for item in extract_headings_and_content(html):
            if item["name"].startswith("/") or "skill" in item["description"].lower():
                features.append({
                    "name": item["name"], "description": item["description"],
                    "source_page": "skills", "type": "skill",
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
                "name": name, "description": desc,
                "source_page": "tools_reference", "type": "tool",
            })
    if not features:
        for item in extract_headings_and_content(html):
            features.append({
                "name": item["name"], "description": item["description"],
                "source_page": "tools_reference", "type": "tool",
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
                "name": name, "description": desc,
                "source_page": "cli_reference", "type": "cli_flag",
            })
    return features


def parse_generic_page(html: str) -> list[dict]:
    """Generic fallback parser for features-overview and platforms."""
    features = []
    for item in extract_headings_and_content(html):
        if item["name"] and len(item["name"]) > 2:
            features.append({
                "name": item["name"], "description": item["description"],
                "source_page": "generic", "type": "feature",
            })
    return features


PARSERS = {
    "commands": parse_commands_page,
    "skills": parse_skills_page,
    "tools_reference": parse_tools_page,
    "cli_reference": parse_cli_page,
    "features_overview": parse_generic_page,
    "platforms": parse_generic_page,
}


def scrape_structured_pages() -> dict[str, list[dict]]:
    """Scrape specific structured pages for detailed item extraction."""
    type_to_key = {
        "command": "commands", "skill": "skills", "tool": "tools",
        "cli_flag": "cli_flags", "feature": "features", "platform": "platforms",
    }
    result = {k: [] for k in type_to_key.values()}
    pages_fetched = 0

    for page_name, url in STRUCTURED_PAGES.items():
        print(f"  Fetching structured page: {page_name}")
        html = fetch_page(url)
        if not html:
            continue
        pages_fetched += 1
        parser = PARSERS.get(page_name, parse_generic_page)
        features = parser(html)
        for feat in features:
            feat["source_page"] = page_name
            key = type_to_key.get(feat.get("type", ""), "features")
            result[key].append(feat)
        print(f"    Found {len(features)} items")

    return result, pages_fetched


# ──────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────

def main():
    print("Scraping Claude Code documentation...")

    # Primary: sitemap-based discovery
    sitemap_features = discover_from_sitemap()

    # Secondary: structured page parsing
    structured, structured_pages_fetched = scrape_structured_pages()

    # Build result
    result = {
        "doc_pages": sitemap_features,
        "commands": structured.get("commands", []),
        "skills": structured.get("skills", []),
        "tools": structured.get("tools", []),
        "cli_flags": structured.get("cli_flags", []),
        "features": structured.get("features", []),
        "platforms": structured.get("platforms", []),
        "scraped_at": date.today().isoformat(),
        "sitemap_pages_found": len(sitemap_features),
        "structured_pages_fetched": structured_pages_fetched,
        "pages_failed": [],
    }

    # Deduplicate within each category
    for key in ["doc_pages", "commands", "skills", "tools", "cli_flags", "features", "platforms"]:
        seen = set()
        deduped = []
        for item in result[key]:
            norm = item["name"].lower().strip()
            if norm not in seen:
                seen.add(norm)
                deduped.append(item)
        result[key] = deduped

    total = sum(len(result[k]) for k in ["doc_pages", "commands", "skills", "tools", "cli_flags", "features", "platforms"])
    print(f"\nTotal unique items discovered: {total}")
    print(f"  Sitemap doc pages: {len(result['doc_pages'])}")
    print(f"  Structured pages fetched: {structured_pages_fetched}")

    # Write output
    output_path = "/tmp/docs-features.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Output written to {output_path}")


if __name__ == "__main__":
    main()
