---
name: Permission System & Sandbox
category: Infrastructure
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Control what Claude can and can't do with granular permissions, approval workflows, and sandbox isolation."
tags: [permissions, security, sandbox, safety, approval]
---

## What it does
A layered security system that lets you decide exactly what Claude Code is allowed to do on your machine. You set permission rules for file access, bash commands, and tool usage. Wildcard rules let you allow or deny patterns (e.g., "allow all git commands but block rm -rf"). Sandbox mode runs everything in an isolated environment so even if something goes sideways, your system stays clean. And PreToolUse hooks let you add custom checks before any tool runs.

## When to use it
- You're working in a production environment and want to prevent accidental destructive commands
- You want Claude to have free rein on your project directory but nothing else
- You're setting up Claude Code for a team and need consistent safety guardrails
- You want to auto-approve common safe operations (like reading files) while requiring approval for writes
- You need an audit trail of what Claude has been allowed to do

## How to use it
1. Open your settings with `/settings` and navigate to the permissions section
2. Set your base permission mode: `ask` (approve each action), `auto` (allow known-safe), or `manual` (strict control)
3. Add wildcard rules like `allow:bash(git *)` to auto-approve specific command patterns
4. Enable sandbox mode in settings for fully isolated execution
5. Add PreToolUse hooks in your `.claude/settings.json` to run custom validation before tool calls

## Pro tips
- Start with `ask` mode for a new project, then add allow rules for the commands you keep approving — you'll build up a natural allowlist
- Wildcard rules support negation: `deny:bash(rm -rf *)` is a nice safety net even in permissive modes
- PreToolUse hooks are powerful for enterprise setups — you can enforce policies like "never modify files in /config" programmatically

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA with core permission modes and approval workflows
- **2025-08-15 (v1.0.95)**: Added wildcard permission rules
- **2025-11-01 (v1.0.115)**: Added sandbox mode and PreToolUse hooks
