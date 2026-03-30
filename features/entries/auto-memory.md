---
name: Auto-Memory
category: Memory & Context
introduced_version: "2.1.59"
introduced_date: 2025-05-01
status: ga
ga_version: "2.1.59"
ga_date: 2025-05-01
one_liner: "Claude automatically remembers your preferences and project details across sessions."
quick_start: "/memory"
tags: [memory, persistence, context, preferences, learning]
---

## What it does
Auto-Memory lets Claude remember important things about you and your projects without you having to repeat yourself. When Claude notices patterns in your preferences, project conventions, or past feedback, it saves them as markdown files in `~/.claude/projects/<project>/memory/`. The memory directory contains a `MEMORY.md` entrypoint and optional topic files. Next time you start a session, the first 200 lines (or 25KB) of `MEMORY.md` is loaded automatically — no re-explaining needed.

## When to use it
- You've told Claude your coding style preferences and don't want to repeat them
- Your project has specific conventions (naming, architecture, testing patterns) that Claude should always follow
- You've corrected Claude on something and want it to stick
- You're onboarding onto a new codebase and want Claude to accumulate knowledge as you explore together
- You want a persistent knowledge base that grows with your project

## How to use it
1. **Just use Claude normally** — it detects and saves important context automatically. Claude doesn't save something every session; it decides what's worth remembering based on whether the information would be useful in a future conversation.
2. **View stored memories**: Run `/memory` to list all CLAUDE.md and rules files loaded in your session, toggle auto memory on or off, and browse auto memory entries.
3. **Edit memories**: Auto memory files are plain markdown you can edit or delete at any time. Use `/memory` to open the auto memory folder, then select any file to open it in your editor.
4. **Configure storage location**: Set the `autoMemoryDirectory` setting in your user or local settings to control where memory files are stored (defaults to `~/.claude/projects/<project>/memory/`). This setting is not accepted from project settings to prevent redirection to sensitive locations.

## Pro Tips
- Check `/memory` periodically to prune stale info — outdated memories can actually mislead Claude
- Memory files are plain markdown, so you can edit or delete them at any time. However, auto memory is machine-local and not shared across machines or cloud environments
- If Claude keeps making the same mistake, explicitly tell it to remember the correction — it'll save it for future sessions
- All worktrees and subdirectories within the same git repository share one auto memory directory
- To disable auto memory, toggle it via `/memory` or set `autoMemoryEnabled` to `false` in your project settings, or set the `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` environment variable

## Status history
- **2025-05-01 (v1.0.0)**: Released with automatic memory detection and persistence
