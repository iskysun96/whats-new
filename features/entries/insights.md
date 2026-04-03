---
name: Insights
category: Developer Tools
introduced_version: "2.1.59"
introduced_date: 2025-12-01
status: ga
ga_version: "2.1.59"
ga_date: 2025-12-01
one_liner: "Generate a report analyzing your Claude Code sessions — project areas, interaction patterns, and friction points."
quick_start: "/insights"
detection:
  type: keyword
  patterns:
    - "how.*am.*I.*using"
    - "session.*analysis"
    - "usage.*pattern"
    - "interaction.*pattern"
    - "analyze.*my.*session"
    - "how.*do.*I.*use.*claude"
  tip: "Run /insights to generate a report analyzing your Claude Code sessions — it shows project areas, interaction patterns, and friction points."
  signal: keyword
tags: [insights, analytics, sessions, patterns, reflection]
---

## What it does
The `/insights` command generates a comprehensive report analyzing your Claude Code sessions. It looks at what project areas you've been working on, how you interact with Claude (what tools you use, how you prompt, what modes you prefer), and where friction points occur — places where you get stuck, where Claude struggles, or where workflows break down.

## When to use it
- You want to understand your own Claude Code usage habits and improve your workflow
- You're curious which parts of your codebase you've been spending the most time on
- You want to identify recurring friction points so you can address them
- Your team is evaluating Claude Code adoption and wants data on usage patterns
- You feel like sessions could be more productive but aren't sure what to change

## How to use it
1. Run `/insights` during any session to generate an analysis of your recent Claude Code sessions
2. Review the report — it covers project areas, interaction patterns, and friction points
3. Use the friction points section to identify workflows you could optimize (e.g., if you're frequently re-explaining context, consider improving your CLAUDE.md)

## Pro Tips
- Run `/insights` periodically (e.g., weekly) to track how your usage evolves as you learn new features
- Pay attention to the friction points — they often reveal features you aren't using yet that could help
- Share insights with your team to identify common patterns and best practices

## Status history
- **2025-12-01 (v2.1.59)**: Released as GA with session analysis covering project areas, interaction patterns, and friction points
