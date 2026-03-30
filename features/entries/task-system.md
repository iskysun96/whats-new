---
name: Task System
category: Multi-Agent
introduced_version: "2.1.29"
introduced_date: 2026-03-10
status: ga
ga_version: "2.1.29"
ga_date: 2026-03-10
one_liner: "Create, track, and manage tasks with dependencies so you can see exactly where complex work stands."
quick_start: "Ctrl+T to toggle task list"
tags: [tasks, tracking, progress, project-management, dependencies]
---

## What it does
The Task System gives Claude a structured way to break down complex work into tracked subtasks, each with status updates and dependency awareness. Instead of Claude just plowing through a big request and hoping you trust it's making progress, you get real-time visibility into what's done, what's in flight, and what's blocked. It's project management baked directly into the agent loop.

## When to use it
- You've asked Claude to do something complex with many steps and want to see progress as it happens
- You're running a background agent and want to check in on how far along it is
- A task has natural dependencies (e.g., "set up the database schema before writing the migration scripts")
- You want to pause a multi-step task and resume later without losing track of where things stand
- You need to coordinate work across subagents and want a single view of overall progress

## How to use it
The Task System is mostly automatic -- when Claude takes on complex work, it creates and manages tasks behind the scenes using built-in tools.

**What Claude uses under the hood:**

- **TaskCreate** -- creates a new task in the task list
- **TaskUpdate** -- updates task status, dependencies, details, or deletes tasks
- **TaskList** -- lists all tasks with their current status
- **TaskGet** -- retrieves full details for a specific task
- **TaskStop** -- kills a running background task by ID

**What you see in the UI:**

Press `Ctrl+T` to toggle the task list view. The display shows up to 10 tasks at a time with status indicators:

```
[done]        Set up project structure
[done]        Create database schema
[in-progress] Write migration scripts
  [done]      Users table migration
  [in-progress] Orders table migration
  [pending]   Products table migration
[blocked]     Write integration tests (waiting on migrations)
[pending]     Update API documentation
```

To see all tasks or clear them, ask Claude directly: "show me all tasks" or "clear all tasks".

**Nudging Claude to use tasks:**

If Claude isn't breaking work into tasks automatically, you can ask:

```
"Break this into tracked tasks with dependencies, then work through them"
```

Or be more specific:

```
"Create a task plan for migrating from Express to Fastify, then execute it step by step"
```

## Pro Tips
- Tasks persist across context compactions, helping Claude stay organized on larger projects. To share a task list across sessions, set `CLAUDE_CODE_TASK_LIST_ID` to use a named directory in `~/.claude/tasks/`.
- You can ask Claude to re-prioritize or skip specific tasks mid-flight: "Skip the documentation task for now and focus on tests"
- The task tree is especially valuable with background agents -- check in anytime to see exactly where things stand without reading through the full conversation

## Status history
- **2026-03-10 (v2.1.29)**: Released as GA -- full task system with TaskCreate, TaskUpdate, TaskList, TaskGet, TaskStop, and dependency tracking
