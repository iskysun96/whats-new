---
name: Subagents
category: Multi-Agent
introduced_version: "1.0.60"
introduced_date: 2025-07-15
status: ga
ga_version: "1.0.60"
ga_date: 2025-07-15
one_liner: "Spawn specialized child agents that handle subtasks independently with their own context windows."
tags: [agents, parallel, delegation, multi-task]
---

## What it does
Subagents let Claude spin up child agents to handle specific subtasks without clogging up the main conversation's context window. Each subagent gets its own fresh context, works independently, and reports back when done. Think of it like delegating work to a focused colleague who only needs to know about their piece of the puzzle.

## When to use it
- You need to explore a large codebase and investigate multiple areas simultaneously
- A task naturally breaks down into independent pieces (e.g., "update the API, the tests, and the docs")
- You want Claude to plan a complex change before executing it, without burning main context
- You're working on a refactor that touches many files and want parallel exploration
- You need a deep-dive into a specific subsystem without losing your place in the main conversation

## How to use it
You don't invoke subagents directly -- Claude decides when to spawn them based on the complexity of your request. Under the hood, Claude uses the **Agent tool** to create them.

There are a few flavors:

1. **Explore agents** -- sent out to read files, search code, and gather information
2. **Plan agents** -- figure out the right approach before making changes
3. **General-purpose agents** -- execute specific subtasks end-to-end

When Claude spawns a subagent, you'll see it in the UI as an indented agent block. The subagent does its work, then its results flow back into the parent conversation.

```
You: "Refactor the auth module and update all related tests"

Claude spawns:
  -> Subagent 1: Explore the auth module structure
  -> Subagent 2: Find all test files related to auth
  -> Main agent: Coordinates and applies changes based on subagent findings
```

## Pro tips
- If Claude isn't spawning subagents when you think it should, you can nudge it: "Use subagents to explore X and Y in parallel"
- Subagents inherit your permission settings, so if you've approved file writes in the parent, subagents can write too
- Keep an eye on the subagent output -- sometimes they surface useful context that the main agent summarizes away

## Status history
- **2025-07-15 (v1.0.60)**: Released as GA -- subagents available via the Agent tool for task delegation and parallel exploration
