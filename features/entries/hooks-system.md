---
name: Hooks System
category: Extensibility
introduced_version: "1.0.62"
introduced_date: 2025-08-15
status: ga
ga_version: "1.0.62"
ga_date: 2025-08-15
one_liner: "Event-driven automation that triggers shell commands, HTTP calls, or AI prompts on Claude Code events."
tags: [hooks, automation, events, triggers, middleware]
---

## What it does
The Hooks System lets you wire up automated actions that fire in response to Claude Code events. When Claude starts a session, uses a tool, finishes a task, or hits any of 25 supported events, your hooks can run shell commands, make HTTP calls, or execute AI prompts. It's like middleware for your AI coding workflow — intercept, validate, transform, or extend anything Claude does.

## When to use it
- You want to auto-format code every time Claude writes a file
- You need to notify Slack or update a ticket tracker when Claude finishes a task
- You want to enforce project rules (e.g., block writes to certain directories) before tool execution
- You need to set up environment variables or run setup scripts at session start
- You want to log every tool invocation for auditing or debugging

## How to use it
1. **Configure hooks**: Add a `hooks` section to your `.claude/settings.json` (project-level), `~/.claude/settings.json` (user-level), or `.claude/settings.local.json` (local, gitignored).
2. **Choose an event**: Pick from events like `SessionStart`, `PreToolUse`, `PostToolUse`, `Stop`, `Notification`, `UserPromptSubmit`, `SubagentStart`, `ConfigChange`, `CwdChanged`, `FileChanged`, `SessionEnd`, and many more (25 events total).
3. **Define the action**: Each event takes an array of hook groups. Each group has a `matcher` (regex to filter when it fires) and a `hooks` array of actions. Each action specifies a `type` (`command`, `http`, `prompt`, or `agent`) and type-specific fields.
4. **Control flow**: Use `PreToolUse` hooks to block tool calls by exiting with code 2, or return structured JSON to deny/allow/ask.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Session started at $(date)' >> ~/.claude/session.log"
          }
        ]
      }
    ]
  }
}
```

## Pro tips
- Use `PreToolUse` hooks with exit code 2 to block tool calls — great for enforcing guardrails like "never delete production configs". Write a reason to stderr and Claude receives it as feedback
- Chain hooks with `matcher` regex patterns to target specific tools (e.g., `"Write|Edit"` to only run formatting on those tools, not `Bash`)
- Keep hook commands fast — they run synchronously by default (set `"async": true` on a hook to run it in the background), so slow hooks will make Claude feel sluggish. Default timeout is 10 minutes
- Use `/hooks` to browse all configured hooks grouped by event and verify your setup

## Status history
- **2025-08-15 (v1.0.62)**: Released with SessionStart, PreToolUse, PostToolUse, and Stop events
- **2025-09-15 (v2.0.0)**: Expanded to 25 events including UserPromptSubmit, SubagentStart, Notification, ConfigChange, CwdChanged, FileChanged, SessionEnd, and more
