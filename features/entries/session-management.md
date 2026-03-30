---
name: Session Management
category: Memory & Context
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Name, resume, fork, and rewind sessions so you never lose your place."
tags: [sessions, resume, fork, rewind, history]
---

## What it does
Session Management lets you pick up conversations exactly where you left off, even after closing your terminal. You can name sessions for easy recall, fork them to explore alternative approaches without losing your original thread, and rewind to undo recent turns when things go sideways.

## When to use it
- You're mid-refactor, need to close your laptop, and want to continue tomorrow
- You want to try two different approaches to the same problem without starting over
- Claude went down a wrong path and you want to roll back a few turns
- You're juggling multiple tasks and want named sessions to keep them organized
- You need to revisit a past session to recall what decisions were made

## How to use it
1. **Resume a session**: Run `claude --resume` to pick from recent sessions, or `claude --resume <session-id>` to jump to a specific one.
2. **Name a session**: Use `/rename my-refactor` inside a session to give it a memorable name.
3. **Fork a session**: Use `--fork-session` when launching to branch off from the current conversation state.
4. **Rewind turns**: Use `/rewind` to step back through recent turns and undo mistakes.

## Pro tips
- Name your sessions by task (e.g., "auth-migration", "api-redesign") so `--resume` becomes a quick project switcher
- Fork before asking Claude to try a risky approach — you can always go back to the original branch
- Combine `/rewind` with a clarified prompt to steer Claude in a better direction without losing earlier context

## Status history
- **2025-05-01 (v1.0.0)**: Released with basic session resume and forking
- **2025-09-15 (v2.0.0)**: Added `/rewind` for stepping back through conversation turns
- **2025-12-01 (v2.1.29)**: Added `/rename` for naming sessions
