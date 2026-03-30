---
name: Cost & Stats Tracking
category: Infrastructure
introduced_version: "1.0.85"
introduced_date: 2025-07-28
status: ga
ga_version: "1.0.85"
ga_date: 2025-07-28
one_liner: "Monitor token usage, API costs, and session stats with /cost and /stats."
tags: [cost, stats, usage, tokens, monitoring]
---

## What it does
Gives you full visibility into what Claude Code is actually costing you. The `/cost` command shows your current session's token usage and estimated API costs. The `/stats` command goes deeper with historical data, session duration tracking, and date-range filtering so you can see trends over time. Token counts are also shown in the status line at the bottom of every session.

## When to use it
- You want to keep an eye on spend during a long coding session
- Your team lead asks "how much are we spending on Claude Code?" and you need actual numbers
- You're comparing costs between different models to find the right balance
- You want to see how your usage patterns have changed over the past week or month
- You need to justify the ROI of Claude Code with real usage data

## How to use it
1. Run `/cost` at any point during a session to see current token counts and estimated cost
2. Run `/stats` for a broader overview of your usage history
3. Use `/stats --from 2026-03-01 --to 2026-03-29` to filter by date range
4. Check the status bar at the bottom of your terminal for a running token count
5. Costs are estimated based on the model you're using — Opus costs more per token than Sonnet or Haiku

## Pro tips
- Run `/cost` before and after a big refactoring task to see exactly what that operation cost you
- The `/stats` date filtering is great for weekly standups — pull last week's stats to share with the team
- Token counts in the status bar update in real time, so you can watch context usage grow as you work

## Status history
- **2025-07-28 (v1.0.85)**: Released as GA with /cost and /stats commands
- **2025-09-10 (v1.0.102)**: Added date-range filtering to /stats
