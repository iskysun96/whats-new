---
name: Deferred Tool Permission Evaluation
category: Extensibility
introduced_version: "2.1.89"
introduced_date: 2026-04-02
status: ga
ga_version: "2.1.89"
ga_date: 2026-04-02
one_liner: "PreToolUse hooks can now defer permission decisions, letting you pause headless sessions at tool calls and resume later with fresh evaluation"
tags: [hooks, tool-use, defer, headless, resume, pretooluse]
---

## What it does
When Claude wants to use a tool in a headless session, your PreToolUse hook can now return `"defer"` instead of just allowing or blocking the tool call. This pauses the session right at that moment, letting you resume later with `-p --resume` where the hook will re-evaluate the tool permission with fresh context or updated logic.

## When to use it
- You want human approval for certain tool calls but don't want to block the entire workflow
- Your permission logic depends on external systems that might be temporarily unavailable
- You need to gather additional context or credentials before allowing a tool to execute
- You're building approval workflows where different people might resume sessions
- You want to pause automated processes for manual review at critical decision points

## How to use it
1. In your PreToolUse hook, return `"defer"` when you want to pause: `return "defer"`
2. Claude will pause the headless session and save its state
3. Later, resume the session with: `claude -p --resume`
4. Your PreToolUse hook will be called again with the same tool request
5. This time, return `"allow"` or `"block"` to proceed

## Pro tips
- Use defer strategically for high-impact tools while allowing routine ones to proceed normally
- Your hook's re-evaluation on resume can use completely different logic or check updated external state
- Consider logging deferred decisions so you know what sessions are waiting for approval

## Status history
- **2026-04-02 (v2.1.89)**: Introduced as generally available
