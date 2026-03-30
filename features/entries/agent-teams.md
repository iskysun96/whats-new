---
name: Agent Teams
category: Multi-Agent
introduced_version: "2.1.0"
introduced_date: 2026-01-20
status: experimental
one_liner: "Multiple agents collaborating on a shared task, each with different roles and specializations."
quick_start: "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude"
tags: [teams, collaboration, multi-agent, coordination]
---

## What it does
Agent Teams takes multi-agent beyond simple delegation. Instead of one main agent spawning helpers, you get a coordinated group of agents that each bring a specific role to the table -- think architect, implementer, reviewer, tester -- all working together on a shared objective. They communicate, hand off work, and keep each other honest. It's the closest thing to having a small engineering team inside your terminal.

## When to use it
- You're tackling a complex project that benefits from multiple perspectives (design, implementation, review)
- You want built-in code review as part of your development workflow -- one agent writes, another reviews
- You need to coordinate changes across multiple services or packages in a monorepo
- You're doing a large-scale migration where planning, execution, and validation should happen in concert
- You want to simulate a team workflow for solo projects (architect proposes, implementer builds, reviewer checks)

## How to use it
> **Note:** Agent Teams is currently **experimental and disabled by default**. Enable by setting `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to `1` in your environment or in `settings.json`. Requires Claude Code v2.1.32 or later.

**Enable agent teams:**

```json
// settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

**Start a team by describing the task in natural language:**

Tell Claude to create an agent team and describe the task and team structure you want. Claude creates the team, spawns teammates, and coordinates work based on your prompt.

```
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.
```

Claude won't create a team without your approval. You can specify the number of teammates and their models explicitly.

**Display modes:**
- `in-process` -- all teammates run inside your main terminal. Use `Shift+Down` to cycle through teammates. Works in any terminal.
- Split panes (tmux/iTerm2) -- each teammate gets its own pane. Requires tmux or iTerm2.

Set the mode with `--teammate-mode in-process` or configure `teammateMode` in `~/.claude.json`.

## Pro tips
- Start with research and review tasks to get a feel for how teams work before tackling parallel implementation.
- Agent teams use significantly more tokens than a single session -- each teammate has its own context window. Start with 3-5 teammates for most workflows.
- Avoid having two teammates edit the same file -- break the work so each teammate owns a different set of files.
- You can require teammates to plan before implementing by saying "Require plan approval before they make any changes." The lead reviews and approves or rejects plans.
- Tell the lead to wait for teammates to finish: "Wait for your teammates to complete their tasks before proceeding."

## Status history
- **2026-01-20 (v2.1.0)**: Released as experimental (disabled by default) -- agent teams available via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` environment variable, coordinated through natural language with shared task lists and inter-agent messaging
