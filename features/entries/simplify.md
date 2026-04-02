---
name: Simplify
category: Developer Tools
introduced_version: "2.1.81"
introduced_date: 2026-02-10
status: ga
ga_version: "2.1.81"
ga_date: 2026-02-10
one_liner: "Review changed code for reuse, quality, and efficiency with three parallel review agents."
quick_start: "/simplify"
detection:
  type: keyword
  patterns:
    - "code.*quality"
    - "simplify.*code"
    - "code.*smell"
    - "clean.*up.*code"
    - "refactor.*suggest"
    - "improve.*code.*quality"
  tip: "Run /simplify to review your recent changes for code reuse, quality, and efficiency improvements using three parallel agents."
  signal: keyword
tags: [simplify, quality, refactoring, review, efficiency]
---

## What it does
The `/simplify` skill reviews your recently changed code for opportunities to improve reuse, quality, and efficiency. It spawns three parallel review agents — each focused on a different quality dimension — then consolidates their findings into actionable suggestions. It's like having three experienced reviewers look at your code simultaneously, each bringing a different lens.

## When to use it
- You've just finished a feature and want to clean it up before opening a PR
- You suspect there's duplicated logic that could be consolidated
- You want a second opinion on whether your implementation is overcomplicated
- You've written code under time pressure and want to spot obvious quality issues
- You want to find performance improvements in recently changed files

## How to use it
1. **Basic**: Run `/simplify` to review all recently changed files
2. **Focused**: Run `/simplify focus on the auth module` to narrow the review to specific areas
3. Review the consolidated findings from the three review agents
4. Apply the suggestions that make sense — not every suggestion needs to be followed

## Pro Tips
- Run `/simplify` after completing a feature but before opening a PR — it catches things you'll otherwise hear about in code review
- The three agents check for: code reuse (DRY violations), code quality (clarity, naming, structure), and efficiency (unnecessary allocations, redundant operations)
- Don't blindly apply every suggestion — use your judgment about whether a simplification actually improves readability in your codebase's context

## Status history
- **2026-02-10 (v2.1.81)**: Released as GA skill with three-agent parallel review system
