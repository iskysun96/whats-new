---
name: Doctor & Debug
category: Infrastructure
introduced_version: "1.0.86"
introduced_date: 2025-07-30
status: ga
ga_version: "1.0.86"
ga_date: 2025-07-30
one_liner: "Diagnose setup issues with `claude doctor` and enable verbose logging with `--verbose`."
quick_start: "claude doctor"
tags: [doctor, debug, diagnostics, troubleshooting, setup]
---

## What it does
Two tools that save you from tearing your hair out when something isn't working. `claude doctor` (run from the command line, not as an in-session slash command) runs a comprehensive check of your Claude Code setup — authentication, permissions, configuration files, network connectivity, the works. It tells you exactly what's wrong and often how to fix it. The `--verbose` flag enables verbose logging so you can see detailed information about API calls, tool invocations, and internal decisions Claude is making.

**Looking for mid-session debug logging?** See the **Debug Skill** entry — the `/debug` slash command lets you enable debug logging without restarting your session.

## When to use it
- Claude Code isn't connecting and you don't know why
- You just installed Claude Code and want to verify everything is configured correctly
- A tool call is failing silently and you need to see what's happening under the hood
- You're filing a bug report and need detailed logs to attach
- Your permissions seem off and you want to verify the full config chain

## How to use it
1. Run `claude doctor` from the command line to get a full system health check — it'll flag any issues with red/yellow indicators
2. Follow the suggested fixes that `claude doctor` provides for each issue
3. Start Claude Code with `claude --verbose` to enable verbose logging from the very beginning
4. Verbose logs include timestamps, so you can correlate issues with specific actions

## Pro Tips
- Run `claude doctor` first whenever something feels off — it catches 90% of common issues before you waste time guessing
- Verbose mode output can be overwhelming, so reproduce the specific issue right after enabling it
- Pair `claude doctor` with `--verbose` when troubleshooting: doctor tells you what's wrong, verbose logging shows you why

## Status history
- **2025-07-30 (v1.0.86)**: Released as GA with `claude doctor` CLI command and `--verbose` flag
- **2025-10-15 (v1.0.110)**: Added network connectivity checks to `claude doctor`
