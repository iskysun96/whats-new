---
name: Image Support
category: Developer Tools
introduced_version: "2.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "2.0.0"
ga_date: 2025-05-01
one_liner: "Drag-and-drop or paste images into Claude Code — screenshots, diagrams, mockups, all understood."
tags: [images, multimodal, screenshots, visual, drag-drop]
---

## What it does
Claude Code is multimodal, which means it can see and understand images right in the terminal. Drag an image file into the terminal window, paste from your clipboard, or just point Claude at an image file path. It'll analyze screenshots, read diagrams, understand UI mockups, and use visual context to inform its work. No more describing what you see — just show it.

## When to use it
- You have a design mockup and want Claude to implement it in code
- You took a screenshot of a bug and want Claude to see exactly what's wrong
- You have an architecture diagram and want Claude to understand the system design
- You want Claude to compare your UI against a reference design
- You're debugging a visual issue and want Claude to see the rendered output

## How to use it
1. **Drag and drop**: Drag an image file directly into the terminal where Claude Code is running.
2. **Paste from clipboard**: Take a screenshot and paste it with Ctrl+V, Cmd+V (iTerm2), or Alt+V (Windows). An `[Image #N]` chip appears at the cursor so you can reference it in your prompt.
3. **File path**: Give Claude a path to an image file or use @-mention to reference it — Claude uses the Read tool to view it.
4. Claude will describe what it sees and incorporate the visual information into its work.

## Pro tips
- For UI implementation tasks, paste the mockup and say "implement this" — Claude will match colors, spacing, and layout from what it sees.
- When reporting bugs, a screenshot is worth a thousand words of description. Just paste it and say "fix this."
- Claude can read text in images (error messages in screenshots, labels in diagrams), so don't worry about transcribing them manually.

## Status history
- **2025-05-01 (v2.0.0)**: Released as generally available with drag-and-drop, clipboard paste, and file path support.
