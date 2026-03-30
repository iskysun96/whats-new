---
name: Transcript Mode
category: Workflow & Automation
introduced_version: "2.1.83"
introduced_date: 2026-03-05
status: ga
ga_version: "2.1.83"
ga_date: 2026-03-05
one_liner: "Scroll through and search your full conversation history with Claude."
quick_start: "Ctrl+O"
tags: [transcript, history, search, review, conversation]
---

## What it does
Transcript Mode toggles verbose output so you can see detailed tool usage and execution in your conversation with Claude. When enabled, it expands tool calls that normally collapse to a single summary line (like "Queried slack") and shows the full details of MCP read and search calls. It gives you visibility into what Claude is actually doing under the hood.

## When to use it
- You want to see the full details of tool calls Claude made and what results they returned
- You're debugging an issue and want to see Claude's extended thinking (shown as gray italic text)
- You want to see expanded MCP tool call results instead of collapsed summaries
- You need to verify exactly what commands Claude ran and what output they produced

## How to use it
1. **Toggle verbose output**: Press `Ctrl+O` to toggle the transcript/verbose mode on or off.
2. **View details**: When enabled, tool calls and MCP results are shown in full detail instead of collapsed summaries.
3. **Toggle show all content**: Press `Ctrl+E` while the transcript viewer is open to toggle showing all content.
4. **Exit transcript view**: Press `q`, `Ctrl+C`, or `Escape` to exit the transcript view.

## Pro tips
- Verbose mode is especially useful for seeing Claude's extended thinking process, which appears as gray italic text
- The `Ctrl+E` shortcut within the transcript view can be rebound via the `transcript:toggleShowAll` keybinding
- The exit shortcuts `Ctrl+C` and `Escape` can be rebound via `transcript:exit`, but `q` is not rebindable

## Status history
- **2026-03-05 (v2.1.83)**: Released with verbose output toggle and transcript viewing
