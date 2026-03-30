---
name: Transcript Mode
category: Workflow & Automation
introduced_version: "2.1.83"
introduced_date: 2026-03-05
status: ga
ga_version: "2.1.83"
ga_date: 2026-03-05
one_liner: "Scroll through and search your full conversation history with Claude."
tags: [transcript, history, search, review, conversation]
---

## What it does
Transcript Mode gives you a scrollable, searchable view of your entire conversation with Claude. Every message, every tool call, every response — all in one navigable view. Instead of scrolling endlessly through your terminal buffer trying to find that one thing Claude said 200 messages ago, you can jump into transcript mode, search for it, and get right back to work.

## When to use it
- You need to find a specific code snippet Claude generated earlier in a long session
- You want to review what tool calls Claude made and what results they returned
- You're debugging an issue and need to trace back through Claude's reasoning
- You want to copy a command or file path Claude mentioned a while back
- You're writing up notes and need to reference specific parts of your session

## How to use it
1. **Enter transcript mode**: Press `Ctrl+O` to open the transcript viewer.
2. **Navigate**: Use arrow keys (or j/k if you're a vim person) to scroll through the conversation.
3. **Search**: Press `/` to start a search, then type your query. Matches are highlighted as you type.
4. **Exit**: Press `Escape` or `q` to return to your normal session.

## Pro tips
- Use search with specific keywords like tool names (e.g., "Read", "Bash") to quickly find where Claude performed specific actions
- Transcript mode is read-only — you can't edit or re-run anything from there, but it's great for reviewing and copying

## Status history
- **2026-03-05 (v2.1.83)**: Released with full conversation transcript viewing and search
