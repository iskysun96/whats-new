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
Prompt Suggestions shows grayed-out example prompts in the input area based on your project context. When you first open a session, the suggestion is drawn from your project's git history so it reflects files you've been working on recently. After Claude responds, suggestions continue to appear based on your conversation history — like a follow-up step from a multi-part request or a natural continuation of your workflow.

## When to use it
- You've just opened a session and want a quick starting point based on your recent work
- Claude just finished a task and you want a natural next step suggested for you
- You're in a multi-step workflow and want Claude to suggest the logical follow-up

## How to use it
1. **See the suggestion**: A grayed-out suggestion appears automatically in the prompt input.
2. **Accept a suggestion**: Press `Tab` to accept the suggestion text, or press `Enter` to accept and submit it immediately.
3. **Dismiss**: Start typing your own prompt to dismiss the suggestion.
4. **Disable**: Set the environment variable `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false`, or toggle it off in `/config`.

## Pro tips
- Suggestions reuse the parent conversation's prompt cache, so the additional cost is minimal
- Suggestions are automatically skipped after the first turn, in non-interactive mode, and in plan mode
- Suggestion generation is also skipped when the cache is cold to avoid unnecessary cost
- For slash command discovery, type `/` to see all available slash commands with descriptions — that's separate from prompt suggestions

## Status history
- **2025-12-15 (v2.1.29)**: Released with context-aware prompt suggestions based on git history and conversation context
