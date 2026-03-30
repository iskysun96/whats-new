---
name: Session Management
category: Memory & Context
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Name, resume, fork, and rewind sessions so you never lose your place."
quick_start: "claude --resume"
detection:
  type: keyword
  first_prompt_only: true
  patterns:
    - "continue.*where.*left"
    - "pick.*up.*where"
    - "resume.*work"
    - "resume.*session"
    - "last.*session"
    - "where.*did.*I.*stop"
  tip: "You can pick up exactly where you left off with `claude --resume`. It restores the full conversation."
  signal: keyword
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
1. **Resume a session**: Run `claude --resume` to pick from recent sessions, or `claude --resume <session-id>` to jump to a specific one. You can also use `/resume` (or `/continue`) inside a session to switch to a different conversation.
2. **Name a session**: Use `/rename my-refactor` inside a session to give it a memorable name. Without a name argument, it auto-generates one from conversation history.
3. **Fork a session**: Use `/branch` (or `/fork`) inside a session to create a branch of the current conversation at that point.
4. **Rewind turns**: Use `/rewind` (or `/checkpoint`) to restore code and/or conversation to a previous point, or summarize from a selected message. You can also press `Esc` twice to trigger the rewind/summarize interface.

## Pro Tips
- Name your sessions by task (e.g., "auth-migration", "api-redesign") so `--resume` becomes a quick project switcher
- Use `/branch` (or `/fork`) before asking Claude to try a risky approach — you can always go back to the original branch
- Combine `/rewind` with a clarified prompt to steer Claude in a better direction without losing earlier context

## Status history
- **2025-05-01 (v1.0.0)**: Released with basic session resume and forking
- **2025-09-15 (v2.0.0)**: Added `/rewind` for stepping back through conversation turns
- **2025-12-01 (v2.1.29)**: Added `/rename` for naming sessions
