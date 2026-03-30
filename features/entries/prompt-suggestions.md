---
name: Prompt Suggestions
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Auto-complete suggestions for commands, file paths, and common prompts as you type."
tags: [autocomplete, suggestions, prompts, productivity]
---

## What it does
Prompt Suggestions gives you context-aware auto-complete as you type in Claude Code. Start typing a slash command and it suggests completions. Reference a file path and it fills in the rest. It even suggests common prompts and patterns based on what you're working on. It's like tab completion in your shell, but for talking to Claude.

## When to use it
- You can't remember the exact name of a slash command
- You're referencing a file path and don't want to type the whole thing
- You want to discover available commands without reading docs
- You're new to Claude Code and want to explore what's possible
- You keep typing the same prompts and want faster input

## How to use it
1. **Just start typing**: Suggestions appear automatically as you type.
2. **Accept a suggestion**: Press `Tab` to accept the current suggestion.
3. **Cycle through options**: If multiple suggestions appear, use arrow keys or keep typing to narrow them down.
4. **Slash commands**: Type `/` to see all available slash commands with descriptions.
5. **Configure**: Adjust suggestion behavior in your settings if you want to tweak or disable it.

## Pro tips
- Typing `/` and pausing for a beat is a great way to discover commands you didn't know existed
- File path suggestions are project-aware, so they'll suggest paths relative to your current project root
- If suggestions feel too aggressive, you can configure the delay or disable specific suggestion types in settings

## Status history
- **2025-12-15 (v2.1.29)**: Released with auto-complete for slash commands, file paths, and contextual prompt suggestions
