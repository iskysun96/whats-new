---
name: Bash Tool & Background Tasks
category: Developer Tools
introduced_version: "1.0.0"
introduced_date: 2025-02-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-02-01
one_liner: "Execute shell commands with permission controls and run long-lived processes in the background."
tags: [bash, shell, terminal, commands, background]
---

## What it does
The Bash tool is how Claude runs shell commands on your machine. It can execute anything you'd type into a terminal — build commands, git operations, package installs, scripts, you name it. For long-running processes (like dev servers or test suites), it supports background execution so Claude doesn't block waiting for them to finish. Permission rules give you control over what Claude can and can't run.

## When to use it
- You need Claude to run your test suite and fix failing tests
- You want Claude to install dependencies, build your project, or run scripts
- You need a dev server running in the background while Claude works on other things
- You want Claude to execute git commands (commit, branch, push)
- You need Claude to run linters, formatters, or other CLI tools as part of a workflow

## How to use it
1. Just ask Claude to do something that requires a shell command — it will use the Bash tool automatically.
2. When Claude runs a command, you'll see it and can approve or deny execution.
3. For background tasks, Claude can run commands asynchronously. You can also press Ctrl+B to move a running command to the background (tmux users press Ctrl+B twice). Background task output is written to a file and can be retrieved with the Read tool.
4. Configure permission rules in your settings to allow or deny specific commands:
   - Allow-listed commands run without asking for approval.
   - Deny-listed commands are blocked entirely.
   - Everything else prompts you for confirmation.

## Pro tips
- Set up allow rules for common safe commands (like `npm test`, `git status`, `cargo build`) so Claude doesn't ask for permission every time.
- Background tasks are great for "start the dev server and then fix the CSS" workflows — Claude kicks off the server and moves on.
- Claude preserves the working directory between commands, but environment variables do not persist — an `export` in one command won't be available in the next. Use absolute paths when it matters.

## Status history
- **2025-02-01 (v1.0.0)**: Released as generally available with full shell access and permission controls.
