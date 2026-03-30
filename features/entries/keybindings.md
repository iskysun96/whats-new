---
name: Keybindings
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Customize keyboard shortcuts and add chord bindings for full control over your input experience."
tags: [keybindings, keyboard, shortcuts, customization]
---

## What it does
Keybindings let you remap any keyboard shortcut in Claude Code and create multi-key chord sequences for custom actions. Want `Ctrl+S` to submit instead of `Enter`? Done. Want a two-key chord like `g g` to jump to the top of your input? You got it. Your keystrokes, your rules. The config lives in a simple JSON file you can version-control and share.

## When to use it
- The default submit key doesn't feel right and you want to change it
- You want chord bindings (multi-key sequences) for advanced navigation or actions
- You're coming from another tool and want to replicate its keybinding scheme
- You need to rebind keys that conflict with your terminal emulator
- You want to share a keybinding config with your team for consistency

## How to use it
1. **View current bindings**: Run `/keybindings` to see all active keyboard shortcuts.
2. **Edit bindings**: Open `~/.claude/keybindings.json` in your editor, or use `/keybindings` to get started.
3. **Rebind a key**: Add an entry mapping the key combination to the desired action (e.g., submit, cancel, voice, newline).
4. **Chord bindings**: Define multi-key sequences by specifying an array of keys — e.g., `["g", "g"]` for a two-press binding.
5. **Reload**: Changes take effect on the next Claude Code session, or restart to apply immediately.

## Pro tips
- The keybindings file is plain JSON, so you can check it into your dotfiles repo and sync across machines
- Chord bindings are especially powerful with vim mode enabled — build custom vim-style sequences that trigger Claude-specific actions
- If a keybinding conflicts with your terminal (e.g., `Ctrl+C`), rebind the Claude action to something else rather than fighting with your terminal emulator

## Status history
- **2025-12-15 (v2.1.29)**: Released with full keybinding customization and chord binding support
