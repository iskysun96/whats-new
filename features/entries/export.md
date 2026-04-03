---
name: Export
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Export your conversation as plain text for documentation, sharing, or archiving."
quick_start: "/export"
detection:
  type: keyword
  patterns:
    - "save.*conversation"
    - "export.*chat"
    - "download.*transcript"
    - "share.*conversation"
    - "save.*session.*text"
  tip: "Use /export to save your conversation as a plain text file — great for documentation, sharing, or archiving."
  signal: keyword
tags: [export, save, text, documentation, sharing]
---

## What it does
The `/export` command saves your current conversation as a plain text file. It captures the full back-and-forth — your prompts, Claude's responses, tool calls and their results — in a readable format. Useful for documentation, sharing with teammates, or archiving important sessions.

## When to use it
- You had a productive session and want to save it for future reference
- You need to share a conversation with a teammate who wasn't there
- You're documenting a decision-making process and want the full reasoning trail
- You want to archive a debugging session that solved a tricky problem
- You need to include conversation context in a bug report or post-mortem

## How to use it
1. **Default**: Run `/export` to save the conversation to a file (auto-named based on session)
2. **Custom filename**: Run `/export my-refactor-session.txt` to specify the output filename
3. The exported file appears in your current working directory

## Pro Tips
- Export before running `/compact` if you want to preserve the full uncompressed conversation
- Combine with `/rename` to give your session a meaningful name before exporting — it makes exported files easier to find later
- Exported text is plain markdown, so it renders nicely in GitHub, Notion, or any markdown viewer

## Status history
- **2025-12-15 (v2.1.29)**: Released as GA with plain text conversation export
