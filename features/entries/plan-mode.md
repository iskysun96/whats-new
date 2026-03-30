---
name: Plan Mode
category: Core Modes
introduced_version: "1.0.77"
introduced_date: 2025-09-10
status: ga
ga_version: "1.0.77"
ga_date: 2025-08-10
one_liner: "Claude explores your codebase and builds a strategic implementation plan before writing a single line of code."
quick_start: "Shift+Tab to cycle to plan mode"
tags: [planning, architecture, approval, workflow]
---

## What it does
Plan Mode puts Claude into a "look but don't touch" mindset. It reads your code, traces dependencies, maps out the architecture, and produces a concrete implementation plan -- all without modifying any files. Once the plan is ready, Claude presents it for your approval. Nothing gets written until you say go. Think of it as a design review with a very fast colleague.

## When to use it
- You're about to refactor a large module and want to see the blast radius before committing
- You need to understand an unfamiliar codebase before making changes
- You want to validate an architectural approach before Claude starts generating code
- You're working on a sensitive area (auth, payments, data migrations) where "move fast and break things" is a bad idea
- You want to share a plan with your team before execution begins

## How to use it
1. **Toggle in-session**: Type `/plan` to enter Plan Mode directly (optionally with a task description, e.g., `/plan fix the auth bug`), or press `shift+tab` to cycle through permission modes (`default` -> `acceptEdits` -> `plan`). You can also start a session in Plan Mode with `claude --permission-mode plan`.
2. Describe what you want to accomplish. Claude will explore relevant files, trace call paths, and draft a step-by-step implementation plan. Claude uses `AskUserQuestion` to gather requirements and clarify your goals.
3. Review the plan. Ask follow-up questions, request changes, or narrow the scope.
4. When the plan is ready, Claude presents it and asks how to proceed. You can: approve and start in auto mode, approve and accept edits, approve and manually review each edit, or keep planning with additional feedback.
5. To cancel, just switch modes or give a new instruction.

## Pro Tips
- Use Plan Mode as a learning tool. Ask Claude to plan a change in an unfamiliar repo, and you'll get a guided tour of the architecture for free.
- You can partially approve a plan. Say "do steps 1-3 first, then pause" to execute incrementally.
- Plan Mode pairs well with git branching. Have Claude plan on main, then create a branch and execute -- you get a clean diff that matches the plan.

## Status history
- **2025-08-10 (v1.0.77)**: Released as GA. Strategic planning with approval gates before code execution.
