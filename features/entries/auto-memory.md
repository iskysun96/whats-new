---
name: Auto-Memory
category: Memory & Context
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Claude automatically remembers your preferences and project details across sessions."
tags: [memory, persistence, context, preferences, learning]
---

## What it does
Auto-Memory lets Claude remember important things about you and your projects without you having to repeat yourself. When Claude notices patterns in your preferences, project conventions, or past feedback, it saves them as markdown files in `.claude/`. Next time you start a session, that knowledge is already there — no re-explaining needed.

## When to use it
- You've told Claude your coding style preferences and don't want to repeat them
- Your project has specific conventions (naming, architecture, testing patterns) that Claude should always follow
- You've corrected Claude on something and want it to stick
- You're onboarding onto a new codebase and want Claude to accumulate knowledge as you explore together
- You want a persistent knowledge base that grows with your project

## How to use it
1. **Just use Claude normally** — it detects and saves important context automatically.
2. **View stored memories**: Run `/memory` to see what Claude has remembered.
3. **Edit memories**: Use `/memory` and modify or delete entries that are outdated or incorrect.
4. **Configure storage location**: Set the `autoMemoryDirectory` setting to control where memory files are stored (defaults to `.claude/`).

## Pro tips
- Check `/memory` periodically to prune stale info — outdated memories can actually mislead Claude
- Memory files are plain markdown, so you can version-control them with your project or share them with teammates
- If Claude keeps making the same mistake, explicitly tell it to remember the correction — it'll save it for future sessions

## Status history
- **2025-05-01 (v1.0.0)**: Released with automatic memory detection and persistence
