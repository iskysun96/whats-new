---
name: Terminal Setup
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Optimized configurations for popular terminals so Claude Code looks and works its best."
tags: [terminal, setup, kitty, alacritty, warp, configuration]
---

## What it does
Terminal Setup provides ready-made, optimized configurations for popular terminal emulators — Kitty, Alacritty, Zed, Warp, iTerm2, and more. Instead of manually tweaking font settings, key handling, mouse support, and rendering options to get Claude Code working perfectly, you get a one-command setup that handles it all. Because life's too short to debug terminal escape sequences.

## When to use it
- You just installed Claude Code and your terminal isn't rendering things quite right
- You're switching to a new terminal emulator and want Claude Code to work perfectly from the start
- Code blocks or syntax highlighting look off and you suspect it's a terminal config issue
- Key combinations aren't being passed through correctly to Claude Code
- You want mouse support or better rendering performance in your terminal

## How to use it
1. **Run the setup**: Type `/terminal-setup` inside Claude Code.
2. **Select your terminal**: Choose your terminal emulator from the list.
3. **Review the config**: Claude shows you the recommended settings and where to apply them.
4. **Apply**: Follow the instructions to update your terminal's config file (or let Claude do it for you).
5. **Restart your terminal**: Some changes require a terminal restart to take effect.

## Pro tips
- Run `/terminal-setup` again after updating your terminal emulator — new versions sometimes change config formats or add new options
- If you're using a less common terminal, the general settings usually work fine — the terminal-specific configs are just optimizations
- Kitty and Alacritty users: make sure keyboard protocol settings are applied, otherwise some keybindings and chord sequences won't register correctly

## Status history
- **2025-12-15 (v2.1.29)**: Released with optimized configurations for Kitty, Alacritty, Zed, Warp, iTerm2, and other popular terminals
