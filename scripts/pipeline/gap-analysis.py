#!/usr/bin/env python3
"""
Cross-reference discovered documentation features against existing entries.

Loads scraped docs from /tmp/docs-features.json, compares against the
feature index, and identifies gaps using fuzzy matching + optional
Haiku validation.

Output: /tmp/gap-report.json
"""

import json
import os
import re
import sys
from difflib import SequenceMatcher

import anthropic


def normalize(name: str) -> str:
    """Normalize a feature name for comparison."""
    name = name.lower().strip()
    # Strip leading / for commands
    name = name.lstrip("/")
    # Remove common prefixes
    name = re.sub(r"^(claude\s+|claude-code\s+)", "", name)
    # Remove punctuation except hyphens
    name = re.sub(r"[^a-z0-9\s-]", "", name)
    # Collapse whitespace
    name = re.sub(r"\s+", " ", name).strip()
    return name


def fuzzy_score(query: str, target: str) -> float:
    """Score how well query matches target (0-100)."""
    q = normalize(query)
    t = normalize(target)

    if not q or not t:
        return 0.0

    # Exact match
    if q == t:
        return 100.0

    # Substring match
    if q in t or t in q:
        return 85.0

    # Word overlap
    q_words = set(q.split())
    t_words = set(t.split())
    if q_words and t_words:
        overlap = len(q_words & t_words) / max(len(q_words), len(t_words))
        if overlap >= 0.5:
            return 60.0 + (overlap * 30.0)

    # Sequence similarity
    ratio = SequenceMatcher(None, q, t).ratio()
    return ratio * 80.0


def match_against_entries(
    doc_feature: dict, existing_features: list[dict]
) -> tuple[float, str | None]:
    """
    Find the best match for a doc feature against existing entries.

    Returns (score, matched_entry_name) or (0, None) if no match.
    """
    query = doc_feature.get("name", "")
    query_desc = doc_feature.get("description", "")
    best_score = 0.0
    best_match = None

    for entry in existing_features:
        # Check against entry name
        score = fuzzy_score(query, entry["name"])

        # Check against tags
        for tag in entry.get("tags", []):
            tag_score = fuzzy_score(query, tag)
            score = max(score, tag_score)

        # Check against one_liner (lower weight)
        if query_desc:
            liner_score = fuzzy_score(query_desc, entry.get("one_liner", ""))
            score = max(score, liner_score * 0.7)

        # Check query description against entry name
        if query_desc:
            desc_name_score = fuzzy_score(query_desc, entry["name"])
            score = max(score, desc_name_score * 0.8)

        if score > best_score:
            best_score = score
            best_match = entry["name"]

    return best_score, best_match


def validate_gaps_with_haiku(
    client: anthropic.Anthropic,
    candidates: list[dict],
    existing_names: list[str],
) -> list[dict]:
    """
    Use Claude Haiku to validate gap candidates and filter false positives.

    Some gaps are false positives (e.g., a tool listed in docs that's already
    covered by a broader feature entry). Haiku confirms which are real gaps.
    """
    if not candidates:
        return []

    candidates_text = "\n".join(
        f"- [{c['source']}] {c['name']}: {c.get('description', '(no description)')}"
        for c in candidates
    )
    existing_text = "\n".join(f"- {name}" for name in sorted(existing_names))

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f"""You are validating a gap analysis for a Claude Code feature teaching plugin.

Below are CANDIDATE GAPS — features found in documentation that may not be covered in
our existing feature entries. Some may be false positives (already covered by a broader
entry, too minor to teach, or internal implementation details).

EXISTING FEATURE ENTRIES (already in our database):
{existing_text}

CANDIDATE GAPS (features from docs not matched to existing entries):
{candidates_text}

For each candidate, decide:
- REAL_GAP: This is a genuine user-facing feature that users should learn about,
  and it is NOT adequately covered by any existing entry.
- FALSE_POSITIVE: This is already covered by an existing entry (name the entry),
  OR it's too minor/internal to warrant its own teaching entry.

Return valid JSON:
{{
  "validated": [
    {{"name": "feature name", "verdict": "REAL_GAP", "reason": "brief explanation", "suggested_name": "Entry Name", "suggested_category": "Category"}}
  ],
  "filtered": [
    {{"name": "feature name", "verdict": "FALSE_POSITIVE", "reason": "covered by 'Existing Entry Name'"}}
  ]
}}""",
            }
        ],
    )

    response_text = response.content[0].text
    json_match = re.search(r"\{[\s\S]*\}", response_text)
    if not json_match:
        print("WARNING: Could not parse Haiku validation response", file=sys.stderr)
        return candidates  # Return all candidates unfiltered

    try:
        result = json.loads(json_match.group())
    except json.JSONDecodeError:
        print("WARNING: Invalid JSON in Haiku validation response", file=sys.stderr)
        return candidates

    # Return only validated real gaps
    validated_names = {
        v["name"].lower()
        for v in result.get("validated", [])
        if v.get("verdict") == "REAL_GAP"
    }

    confirmed = []
    for candidate in candidates:
        if candidate["name"].lower() in validated_names:
            # Enrich with Haiku's suggestions
            for v in result.get("validated", []):
                if v["name"].lower() == candidate["name"].lower():
                    candidate["suggested_name"] = v.get("suggested_name", candidate["name"])
                    candidate["suggested_category"] = v.get("suggested_category", "Uncategorized")
                    break
            confirmed.append(candidate)

    filtered_count = len(candidates) - len(confirmed)
    print(f"  Haiku validation: {len(confirmed)} real gaps, {filtered_count} false positives filtered")

    return confirmed


def main():
    # Load scraped docs
    docs_path = "/tmp/docs-features.json"
    if not os.path.exists(docs_path):
        print("ERROR: /tmp/docs-features.json not found. Run scrape-docs.py first.", file=sys.stderr)
        sys.exit(1)

    with open(docs_path) as f:
        docs = json.load(f)

    # Load existing features
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plugin_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    index_path = os.path.join(plugin_root, "features", "index.json")

    if not os.path.exists(index_path):
        print("ERROR: features/index.json not found", file=sys.stderr)
        sys.exit(1)

    with open(index_path) as f:
        index = json.load(f)

    existing_features = index.get("features", [])
    existing_names = [f["name"] for f in existing_features]

    print(f"Existing features: {len(existing_features)}")

    # Collect all doc-discovered features
    all_doc_features = []
    for key in ("commands", "skills", "tools", "cli_flags", "features", "platforms"):
        items = docs.get(key, [])
        for item in items:
            item["source"] = key
        all_doc_features.extend(items)

    print(f"Doc-discovered features: {len(all_doc_features)}")

    # Match each doc feature against existing entries
    match_threshold = 60.0
    covered = []
    gap_candidates = []

    for doc_feat in all_doc_features:
        score, matched = match_against_entries(doc_feat, existing_features)
        if score >= match_threshold:
            covered.append({
                "doc_feature": doc_feat["name"],
                "matched_entry": matched,
                "confidence": round(score, 1),
                "source": doc_feat.get("source", ""),
            })
        else:
            gap_candidates.append({
                "name": doc_feat["name"],
                "description": doc_feat.get("description", ""),
                "source": doc_feat.get("source", ""),
                "type": doc_feat.get("type", ""),
                "best_score": round(score, 1),
                "closest_match": matched,
            })

    print(f"Covered: {len(covered)}, Gap candidates: {len(gap_candidates)}")

    # Validate gaps with Haiku (if API key available and there are candidates)
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    confirmed_gaps = gap_candidates  # Default: keep all candidates
    false_positives_filtered = 0

    if api_key and gap_candidates:
        print("Validating gap candidates with Haiku...")
        client = anthropic.Anthropic(api_key=api_key)
        confirmed_gaps = validate_gaps_with_haiku(client, gap_candidates, existing_names)
        false_positives_filtered = len(gap_candidates) - len(confirmed_gaps)
    elif not api_key:
        print("WARNING: ANTHROPIC_API_KEY not set, skipping Haiku validation", file=sys.stderr)

    # Calculate coverage
    total_doc = len(all_doc_features)
    coverage_pct = (len(covered) / total_doc * 100) if total_doc > 0 else 100.0

    # Per-source coverage
    source_coverage = {}
    for key in ("commands", "skills", "tools", "cli_flags", "features", "platforms"):
        source_total = len(docs.get(key, []))
        source_covered = sum(1 for c in covered if c["source"] == key)
        if source_total > 0:
            source_coverage[key] = {
                "total": source_total,
                "covered": source_covered,
                "pct": round(source_covered / source_total * 100, 1),
            }

    # Build report
    report = {
        "covered": covered,
        "gaps": confirmed_gaps,
        "false_positives_filtered": false_positives_filtered,
        "coverage_pct": round(coverage_pct, 1),
        "source_coverage": source_coverage,
        "existing_feature_count": len(existing_features),
        "doc_feature_count": total_doc,
    }

    output_path = "/tmp/gap-report.json"
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

    # Print summary
    print(f"\n=== Gap Analysis Report ===")
    print(f"Existing entries: {len(existing_features)}")
    print(f"Doc-discovered: {total_doc}")
    print(f"Covered: {len(covered)} ({coverage_pct:.1f}%)")
    print(f"Gaps: {len(confirmed_gaps)}")
    print(f"False positives filtered: {false_positives_filtered}")
    print(f"\nPer-source coverage:")
    for source, stats in source_coverage.items():
        print(f"  {source}: {stats['covered']}/{stats['total']} ({stats['pct']}%)")

    if confirmed_gaps:
        print(f"\nGap details:")
        for gap in confirmed_gaps:
            print(f"  - [{gap['source']}] {gap['name']}: {gap.get('description', '')[:80]}")

    print(f"\nReport written to {output_path}")


if __name__ == "__main__":
    main()
