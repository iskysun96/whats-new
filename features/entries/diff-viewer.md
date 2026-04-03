---
name: Diff Viewer
category: Developer Tools
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Interactive diff viewer showing uncommitted changes and per-turn diffs right in your session."
quick_start: "/diff"
detection:
  type: keyword
  patterns:
    - "show.*diff"
    - "what.*changed"
    - "see.*my.*changes"
    - "uncommitted.*changes"
    - "what.*did.*you.*change"
    - "review.*changes"
  tip: "Run /diff to see an interactive diff viewer showing all uncommitted changes and per-turn diffs."
  signal: keyword
tags: [diff, changes, git, review, comparison]
---

## What it does
The `/diff` command opens an interactive diff viewer right inside your Claude Code session. It shows you uncommitted changes in your working directory as well as per-turn diffs — what changed during each step of Claude's work. Instead of switching to another terminal to run `git diff`, you can review everything in context without breaking your flow.

## When to use it
- Claude just made a bunch of changes and you want to review them before committing
- You want to see exactly what changed during a specific turn of the conversation
- You're about to commit and want a final review of all pending changes
- You need to verify that Claude only changed what you asked it to change
- You want to compare the cumulative effect of multiple editing steps

## How to use it
1. Run `/diff` to open the interactive diff viewer
2. Browse through uncommitted changes — files are listed with their change status
3. Navigate between per-turn diffs to see what changed at each step of Claude's work
4. Use the viewer's navigation to jump between files and hunks

## Pro Tips
- Use `/diff` after each major step in a multi-step task to catch issues early, rather than reviewing a massive diff at the end
- Combine with `/rewind` — if `/diff` reveals unwanted changes, rewind to before they happened
- Per-turn diffs are especially useful when Claude made many changes across multiple files — they show the logical grouping of each edit step

## Status history
- **2025-12-15 (v2.1.29)**: Released as GA with uncommitted diff view and per-turn diff tracking
