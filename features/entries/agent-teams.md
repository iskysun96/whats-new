---
name: Agent Teams
category: Multi-Agent
introduced_version: "2.1.0"
introduced_date: 2026-01-20
status: public-beta
one_liner: "Multiple agents collaborating on a shared task, each with different roles and specializations."
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
> **Note:** Agent Teams is currently in **public beta** (research preview). The API and configuration format may change.

**Quick start with built-in team presets:**

```bash
claude --team "dev-review"
```

This spins up a development team with an implementer and a reviewer agent.

**Configure custom teams in your settings:**

Add a team definition to `.claude/settings.json` or your project's Claude config:

```json
{
  "agentTeams": {
    "my-team": {
      "agents": [
        { "role": "architect", "agent": "planner" },
        { "role": "implementer", "agent": "coder" },
        { "role": "reviewer", "agent": "code-reviewer" }
      ],
      "coordination": "sequential"
    }
  }
}
```

You can also define teams using custom agent definition files (see the Custom Agent Definitions feature).

**Coordination modes:**
- `sequential` -- agents take turns in order (plan -> implement -> review)
- `parallel` -- agents work simultaneously and sync at checkpoints
- `adaptive` -- Claude decides the best coordination strategy based on the task

## Pro tips
- Start with the built-in presets to get a feel for how teams work before building custom configurations
- The reviewer role is surprisingly useful even for small changes -- it catches things a single agent misses
- Teams work best when each agent has a clearly scoped role; avoid overlapping responsibilities

## Status history
- **2026-01-20 (v2.1.0)**: Released as public beta (research preview) -- agent teams available with built-in presets and custom configuration
