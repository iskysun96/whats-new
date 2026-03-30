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
The Hooks System lets you wire up automated actions that fire in response to Claude Code events. When Claude starts a session, uses a tool, finishes a task, or hits any of 20+ supported events, your hooks can run shell commands, make HTTP calls, or even execute AI prompts. It's like middleware for your AI coding workflow — intercept, validate, transform, or extend anything Claude does.

## When to use it
- You want to auto-format code every time Claude writes a file
- You need to notify Slack or update a ticket tracker when Claude finishes a task
- You want to enforce project rules (e.g., block writes to certain directories) before tool execution
- You need to set up environment variables or run setup scripts at session start
- You want to log every tool invocation for auditing or debugging

## How to use it
1. **Configure hooks**: Add a `hooks` section to your `.claude/settings.json`.
2. **Choose an event**: Pick from events like `SessionStart`, `PreToolUse`, `PostToolUse`, `Stop`, `UserPromptSubmit`, and many more.
3. **Define the action**: Specify a shell command, HTTP endpoint, or AI prompt to run when the event fires.
4. **Control flow**: Use `PreToolUse` hooks to block or modify tool calls before they execute.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "match": "Write|Edit",
        "command": "prettier --write \"$CLAUDE_FILE_PATH\""
      }
    ],
    "SessionStart": [
      {
        "command": "echo 'Session started at $(date)' >> ~/.claude/session.log"
      }
    ]
  }
}
```

## Pro tips
- Use `PreToolUse` hooks with a non-zero exit code to block tool calls — great for enforcing guardrails like "never delete production configs"
- Chain hooks with `match` patterns to target specific tools (e.g., only run formatting on `Write` and `Edit`, not `Bash`)
- Keep hook commands fast — they run synchronously, so slow hooks will make Claude feel sluggish

## Status history
- **2025-08-15 (v1.0.62)**: Released with SessionStart, PreToolUse, PostToolUse, and Stop events
- **2025-09-15 (v2.0.0)**: Expanded to 20+ events including UserPromptSubmit, SubagentStart, and more
