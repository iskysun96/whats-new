---
name: Permission System & Sandbox
category: Infrastructure
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Control what Claude can and can't do with granular permissions, approval workflows, and sandbox isolation."
quick_start: "Shift+Tab to cycle permission modes"
tags: [permissions, security, sandbox, safety, approval]
---

## What it does
A layered security system that lets you decide exactly what Claude Code is allowed to do on your machine. You set permission rules for file access, bash commands, and tool usage. The `allowedTools` configuration lets you auto-approve specific tool patterns (e.g., "allow all git commands"). Sandbox mode uses platform-specific isolation (macOS Seatbelt, Linux containers) so even if something goes sideways, your system stays clean. Hooks (including PreToolUse) let you add custom checks before any tool runs.

## When to use it
- You're working in a production environment and want to prevent accidental destructive commands
- You want Claude to have free rein on your project directory but nothing else
- You're setting up Claude Code for a team and need consistent safety guardrails
- You want to auto-approve common safe operations (like reading files) while requiring approval for writes
- You need an audit trail of what Claude has been allowed to do

## How to use it
1. Open your settings with `/config` or edit `.claude/settings.json` directly
2. Set your permission mode: use `plan` mode (read-only, no writes), default mode (asks for approval on risky actions), or `--dangerously-skip-permissions` (bypasses all prompts, use with extreme caution)
3. Add entries to `allowedTools` like `"Bash(git *)"` to auto-approve specific command patterns
4. Sandbox mode is enabled by default for Bash commands, using macOS Seatbelt or Linux containers for isolation
5. Add hooks (e.g., PreToolUse) in your `.claude/settings.json` to run custom validation before tool calls

## Pro Tips
- Start with the default permission mode for a new project, then add entries to `allowedTools` for the commands you keep approving — you'll build up a natural allowlist
- Wildcard patterns in `allowedTools` support glob matching: `"Bash(git *)"` approves all git subcommands automatically
- Hooks are powerful for enterprise setups — you can enforce policies like "never modify files in /config" programmatically via PreToolUse hooks

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA with core permission modes and approval workflows
- **2025-08-15 (v1.0.95)**: Added wildcard permission rules
- **2025-11-01 (v1.0.115)**: Added sandbox mode and PreToolUse hooks
