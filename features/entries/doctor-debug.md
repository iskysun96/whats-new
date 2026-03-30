---
name: Doctor & Debug
category: Infrastructure
introduced_version: "1.0.86"
introduced_date: 2025-07-30
status: ga
ga_version: "1.0.86"
ga_date: 2025-07-30
one_liner: "Diagnose setup issues with /doctor and enable verbose logging with /debug."
tags: [doctor, debug, diagnostics, troubleshooting, setup]
---

## What it does
Two tools that save you from tearing your hair out when something isn't working. `/doctor` runs a comprehensive check of your Claude Code setup — authentication, permissions, configuration files, network connectivity, the works. It tells you exactly what's wrong and often how to fix it. `/debug` flips on verbose logging so you can see every API call, tool invocation, and internal decision Claude is making.

## When to use it
- Claude Code isn't connecting and you don't know why
- You just installed Claude Code and want to verify everything is configured correctly
- A tool call is failing silently and you need to see what's happening under the hood
- You're filing a bug report and need detailed logs to attach
- Your permissions seem off and you want to verify the full config chain

## How to use it
1. Run `/doctor` to get a full system health check — it'll flag any issues with red/yellow indicators
2. Follow the suggested fixes that `/doctor` provides for each issue
3. Run `/debug` during a session to enable verbose logging for the rest of that session
4. From the command line, start with `claude --debug` to get verbose output from the very beginning
5. Debug logs include timestamps, so you can correlate issues with specific actions

## Pro tips
- Run `/doctor` first whenever something feels off — it catches 90% of common issues before you waste time guessing
- Debug mode output can be overwhelming, so reproduce the specific issue right after enabling it, then turn it off
- Pair `/doctor` with `/debug` when troubleshooting: doctor tells you what's wrong, debug shows you why

## Status history
- **2025-07-30 (v1.0.86)**: Released as GA with /doctor and /debug commands
- **2025-10-15 (v1.0.110)**: Added network connectivity checks to /doctor
