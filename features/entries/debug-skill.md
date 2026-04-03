---
name: Debug Skill
category: Developer Tools
introduced_version: "2.1.70"
introduced_date: 2026-01-15
status: ga
ga_version: "2.1.70"
ga_date: 2026-01-15
one_liner: "Enable debug logging mid-session and troubleshoot issues by reading the debug log."
quick_start: "/debug"
detection:
  type: keyword
  patterns:
    - "debug.*log"
    - "enable.*debug"
    - "troubleshoot.*issue"
    - "verbose.*log"
    - "debug.*mode"
    - "something.*not.*working"
  tip: "Run /debug to enable debug logging for this session and troubleshoot issues. You can also describe the issue: /debug MCP server not connecting."
  signal: keyword
tags: [debug, logging, troubleshooting, diagnostics, skill]
---

## What it does
The `/debug` skill enables debug logging for your current session and helps you troubleshoot issues by reading the session debug log. Unlike starting Claude with `--debug` from the command line, `/debug` can be activated mid-session — it starts capturing logs from that point forward. You can optionally describe the issue you're experiencing to focus the analysis on relevant log entries.

**Note**: This is different from `claude doctor` (which checks your installation health) and `--verbose` (which shows verbose output from the start). See the "Doctor & Debug" entry for those tools.

## When to use it
- An MCP server isn't connecting and you need to see the handshake logs
- A tool call is failing and you want to see exactly what's happening under the hood
- Hooks aren't firing when you expect them to and you need to trace the event flow
- You're mid-session and realize you should have started with `--debug` but don't want to restart
- You need to attach debug logs to a bug report

## How to use it
1. **Basic**: Run `/debug` to start capturing debug logs for the remainder of your session
2. **Focused**: Run `/debug MCP server not connecting` to enable logging and focus the analysis on MCP-related entries
3. **Review**: After reproducing the issue, the skill reads the debug log and highlights relevant entries
4. **CLI alternative**: Start a new session with `claude --debug` for full session debug logging, or `claude --debug "api,hooks"` to filter by category

## Pro Tips
- Use `/debug` right before reproducing an issue — the less noise in the log, the easier it is to find the problem
- The category filter (`claude --debug "api,hooks"`) is invaluable when you know which subsystem is broken
- Combine with `claude --debug-file /tmp/debug.log` to write logs to a specific file for sharing or later analysis
- If `/debug` shows the issue is with your setup (not a bug), follow up with `claude doctor` for guided fixes

## Status history
- **2026-01-15 (v2.1.70)**: Released as GA skill with mid-session activation and focused analysis
