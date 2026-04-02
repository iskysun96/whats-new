---
name: BTW (Side Questions)
category: Core Modes
introduced_version: "2.1.59"
introduced_date: 2025-12-01
status: ga
ga_version: "2.1.59"
ga_date: 2025-12-01
one_liner: "Ask a quick side question without adding it to your conversation history or derailing your main task."
quick_start: "/btw what does this error mean?"
detection:
  type: keyword
  patterns:
    - "quick.*question"
    - "side.*question"
    - "unrelated.*but"
    - "off.*topic.*but"
    - "btw.*can.*you"
    - "by.*the.*way"
  tip: "Use /btw to ask a quick side question without it being added to your conversation history. Your main task context stays clean."
  signal: keyword
tags: [btw, side-question, context, quick, modes]
---

## What it does
The `/btw` command lets you ask a quick side question without it being added to your conversation history. The question and answer happen in a temporary bubble — your main conversation context stays exactly as it was. This is perfect for those moments when you need to quickly look something up or ask an unrelated question without derailing the task Claude is helping you with.

## When to use it
- You're mid-refactor and want to quickly ask what a specific error message means
- You need a one-off syntax question but don't want it eating into your context window
- You want to ask about something unrelated to the current task without confusing Claude's focus
- You're curious about a concept you just encountered but don't want to sidetrack the conversation

## How to use it
1. Type `/btw` followed by your question: `/btw what does SIGTERM mean?`
2. Claude answers the question
3. The exchange is not added to your conversation history — your main context is preserved
4. Continue with your original task as if the side question never happened

## Pro Tips
- Use `/btw` liberally for quick lookups — it's free in terms of context window impact
- Great for "what does this flag do?" or "what's the syntax for X?" questions during a long session
- If the answer to your `/btw` question turns out to be important for your main task, just mention it in your next regular prompt

## Status history
- **2025-12-01 (v2.1.59)**: Released as GA with history-free side questions
