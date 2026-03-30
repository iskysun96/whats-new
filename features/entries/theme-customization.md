---
name: Theme & UI Customization
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Customize syntax highlighting, prompt bar color, and spinner tips to make Claude Code yours."
quick_start: "/theme"
detection:
  type: keyword
  patterns:
    - "change.*theme"
    - "syntax.*highlight"
    - "change.*color"
    - "dark.*mode"
  tip: "Run /theme to change syntax highlighting. Use /color to set prompt bar color. Customize spinner tips in settings."
  signal: keyword
tags: [theme, colors, ui, appearance, syntax-highlighting]
---

## What it does
Theme & UI Customization lets you control how Claude Code looks and feels. Change the syntax highlighting theme for code blocks, set your prompt bar to your favorite color, and even replace the default spinner tips with your own messages. It's a small thing, but when you're staring at a tool all day, it matters that it looks the way you want.

## When to use it
- The default syntax theme doesn't match your terminal's color scheme
- You want a visual distinction between different projects (color-coded prompt bars)
- The spinner tips are getting stale and you want to add your own jokes or reminders
- You prefer a minimal or high-contrast look
- You want Claude Code to match your overall terminal aesthetic

## How to use it
1. **Change color theme**: Run `/theme` and pick from available themes. Includes light and dark variants, colorblind-accessible (daltonized) themes, and ANSI themes that use your terminal's color palette. Press `Ctrl+T` inside the theme picker to toggle syntax highlighting on or off.
2. **Set prompt bar color**: Run `/color` and choose a color for your prompt bar. Available colors: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan`. Use `/color default` to reset.
3. **Toggle spinner tips**: Set `spinnerTipsEnabled` to `false` in your settings to hide tips shown while Claude is working (default: `true`).
4. **Custom spinner tips**: Set `spinnerTipsOverride` in settings as an object — e.g., `{ "excludeDefault": true, "tips": ["Your custom tip here"] }`. Set `excludeDefault` to `true` to show only your tips, or `false` to merge with built-in tips.
5. **Custom spinner verbs**: Set `spinnerVerbs` in settings to customize the action verbs shown in the spinner — e.g., `{ "mode": "append", "verbs": ["Pondering", "Crafting"] }`.

## Pro tips
- Use different prompt bar colors for different projects — it's a quick visual cue for which project you're in when you have multiple terminals open
- Custom spinner tips are a surprisingly fun way to keep yourself motivated or remind yourself of team conventions while waiting for responses
- The syntax theme applies to all code blocks in Claude's responses, so pick one that makes diffs and code snippets easy to read in your terminal

## Status history
- **2025-12-15 (v2.1.29)**: Released with syntax theme selection, prompt bar color, and customizable spinner tips
