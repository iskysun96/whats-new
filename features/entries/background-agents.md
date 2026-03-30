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

**Option 2: Start a background task from scratch**

```bash
claude --background "Migrate all API endpoints from v2 to v3 format"
```

**Checking on background tasks:**

```bash
# List all background tasks
claude --background-status

# Resume or check a specific background task
claude --resume <task-id>
```

When a background task finishes, you'll see a notification (if your terminal supports it).

## Pro tips
- Background agents have the same permissions as your interactive session -- if you haven't pre-approved certain tools, the agent may pause waiting for approval, so consider your permission settings before backgrounding
- You can run multiple background agents simultaneously -- great for tackling independent workstreams in parallel
- Combine with `--allowedTools` to give background agents exactly the permissions they need without over-granting

## Status history
- **2025-08-12 (v1.0.71)**: Released as GA -- background agents available via `Ctrl+B` and `--background` flag
