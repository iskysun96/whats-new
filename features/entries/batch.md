---
name: Batch
category: Workflow & Automation
introduced_version: "2.1.81"
introduced_date: 2026-02-10
status: ga
ga_version: "2.1.81"
ga_date: 2026-02-10
one_liner: "Orchestrate large-scale parallel changes across your codebase — each unit in its own worktree with its own PR."
quick_start: "/batch"
detection:
  type: keyword
  patterns:
    - "change.*across.*all"
    - "update.*every.*file"
    - "bulk.*change"
    - "mass.*update"
    - "all.*files.*at.*once"
    - "apply.*to.*every"
    - "change.*in.*all.*components"
  tip: "Use /batch to orchestrate large-scale parallel changes. It splits work into independent units, each in its own worktree, each opening a separate PR."
  signal: keyword
tags: [batch, parallel, large-scale, worktree, automation]
---

## What it does
The `/batch` skill orchestrates large-scale parallel changes across your codebase. You describe what needs to change and it splits the work into 5–30 independent units, each running in its own isolated git worktree, each producing its own PR. Instead of one massive PR that's impossible to review, you get a set of focused, reviewable PRs that can be merged independently.

## When to use it
- You need to apply the same pattern change across dozens of files or modules
- You're migrating an API and every consumer needs to be updated
- You want to add consistent error handling, logging, or type annotations across a codebase
- You're upgrading a dependency and need to update its usage everywhere
- You need to rename a concept across the entire project (beyond what find-and-replace handles)

## How to use it
1. Run `/batch update all React class components to functional components`
2. The skill analyzes your codebase and identifies independent units of work
3. Each unit runs in its own worktree with its own agent — they execute in parallel
4. When complete, each unit has its own PR ready for review
5. Review and merge PRs independently — no single massive changeset to deal with

## Pro Tips
- Write clear, specific instructions — the quality of the batch operation depends on how well you describe the change
- Batch works best when changes are truly independent (e.g., updating each component file separately) — don't use it for changes with cross-file dependencies
- Review the first 2-3 PRs carefully to make sure the pattern is right before merging the rest
- Combine with `/simplify` after merging to catch any inconsistencies across the batched changes

## Status history
- **2026-02-10 (v2.1.81)**: Released as GA skill with worktree-based parallel execution and automatic PR creation
