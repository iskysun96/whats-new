---
name: Extended Thinking
category: Memory & Context
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Claude thinks deeper before responding, showing its reasoning process in real-time."
quick_start: "Option+T (macOS) or Alt+T (Linux/Windows)"
tags: [thinking, reasoning, deep-thought, ultrathinking]
---

## What it does
Extended Thinking lets Claude spend more time reasoning through complex problems before giving you an answer. Instead of rushing to respond, Claude works through the problem step by step, and you can watch the thought process unfold in real-time with interleaved thinking display. For the hardest problems, "ultrathinking" mode gives Claude even more room to reason.

## When to use it
- You're debugging a tricky issue that requires analyzing multiple interacting systems
- You need Claude to plan a complex refactor before making changes
- You're asking Claude to reason about architecture trade-offs
- A straightforward prompt gave you a wrong answer and you want Claude to think more carefully
- You want to understand why Claude is making a particular recommendation

## How to use it
1. **Thinking is on by default** — Claude automatically uses extended thinking for complex prompts.
2. **Toggle thinking**: Press `Option+T` (macOS) or `Alt+T` (Windows/Linux) to toggle extended thinking mode on or off. You may need to run `/terminal-setup` first to enable this shortcut.
3. **Watch in real-time**: When thinking is displayed, you'll see Claude's reasoning process inline as it works through the problem.
4. **Ultrathinking in skills**: To enable deeper reasoning in a custom skill, include the word "ultrathink" anywhere in your skill content. Claude scales thinking to match problem difficulty.

## Pro tips
- If Claude gives a shallow answer, try rephrasing your question to be more specific — this often triggers deeper thinking automatically
- Reading the thinking output is a great way to catch when Claude is heading in the wrong direction early, before it writes code
- Turn off thinking display with `Option+T` (macOS) or `Alt+T` (Windows/Linux) when you're doing rapid-fire simple tasks and don't need to see the reasoning

## Status history
- **2025-05-01 (v1.0.0)**: Released with extended thinking and `Option+T`/`Alt+T` keyboard toggle
- **2025-09-15 (v2.0.0)**: Added interleaved thinking display for real-time reasoning visibility
- **2025-12-01 (v2.1.0)**: Introduced ultrathinking for deeper reasoning on complex problems
