---
name: Background Agents
category: Multi-Agent
introduced_version: "1.0.71"
introduced_date: 2025-08-12
status: ga
ga_version: "1.0.71"
ga_date: 2025-08-12
one_liner: "Kick off long-running tasks that keep working even after you close your terminal."
tags: [background, async, long-running, parallel-work]
---

## What it does
Background agents let you fire off a task and walk away. Close your terminal, grab coffee, work on something else -- the agent keeps running. When you come back, you can check on its progress or pick up the results. It's like having a teammate who works while you sleep.

## When to use it
- You have a large refactor or migration that'll take a while and you don't want to babysit it
- You want to run multiple independent tasks in parallel across different parts of your project
- You're kicking off a task at end of day and want to review results in the morning
- You need to run a long test suite or complex build and have Claude monitor it
- You want to keep your current terminal session free for interactive work

## How to use it
**Option 1: Background your current task**

If you're mid-conversation and realize a task is going to take a while:

```
Press Ctrl+B to send the current task to the background
```

Claude will continue working in the background. You get your terminal back immediately.

**Option 2: Ask Claude to run something in the background**

You can also prompt Claude to run a command in the background during a conversation. Claude runs the command asynchronously and immediately returns a background task ID.

**Checking on background tasks:**

Background task output is written to a file, and Claude can retrieve it using the Read tool. Background tasks have unique IDs for tracking and output retrieval. They are automatically cleaned up when Claude Code exits and automatically terminated if output exceeds 5GB.

To disable all background task functionality, set the `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to `1`.

## Pro tips
- Background tasks have the same permissions as your interactive session -- if you haven't pre-approved certain tools, a background subagent may auto-deny anything not pre-approved. Claude pre-prompts for permissions before launching a background subagent.
- You can run multiple background tasks simultaneously -- great for tackling independent workstreams in parallel.
- Common backgrounded commands include build tools (webpack, vite, make), package managers (npm, yarn, pnpm), test runners (jest, pytest), development servers, and long-running processes (docker, terraform).
- Use `Ctrl+X Ctrl+K` to kill all background agents (press twice within 3 seconds to confirm).

## Status history
- **2025-08-12 (v1.0.71)**: Released as GA -- background tasks available via `Ctrl+B` to background running tasks and subagents
