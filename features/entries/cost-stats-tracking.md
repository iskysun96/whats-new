---
name: Cost & Stats Tracking
category: Infrastructure
introduced_version: "1.0.85"
introduced_date: 2025-07-28
status: ga
ga_version: "1.0.85"
ga_date: 2025-07-28
one_liner: "Monitor token usage and API costs with /cost during your session."
quick_start: "/cost"
detection:
  type: keyword
  patterns:
    - "how.*much.*cost"
    - "session.*cost"
    - "token.*usage"
    - "spending"
    - "how.*expensive"
  tip: "Run /cost to see your current session costs and token usage."
  signal: keyword
tags: [cost, stats, usage, tokens, monitoring]
---

## What it does
Gives you full visibility into what Claude Code is actually costing you. The `/cost` command shows your current session's token usage and estimated API costs. Token counts are also shown in the status line at the bottom of every session, so you always have a sense of how much context you're consuming.

## When to use it
- You want to keep an eye on spend during a long coding session
- Your team lead asks "how much are we spending on Claude Code?" and you need actual numbers
- You're comparing costs between different models to find the right balance
- You need to justify the ROI of Claude Code with real usage data

## How to use it
1. Run `/cost` at any point during a session to see current token counts and estimated cost
2. Check the status bar at the bottom of your terminal for a running token count
3. Costs are estimated based on the model you're using — Opus costs more per token than Sonnet or Haiku

## Pro Tips
- Run `/cost` before and after a big refactoring task to see exactly what that operation cost you
- Token counts in the status bar update in real time, so you can watch context usage grow as you work

## Status history
- **2025-07-28 (v1.0.85)**: Released as GA with /cost command and status bar token tracking
