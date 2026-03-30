---
name: Keybindings
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Customize keyboard shortcuts and add chord bindings for full control over your input experience."
quick_start: "/keybindings"
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
1. **Open the config**: Run `/keybindings` to create or open your configuration file at `~/.claude/keybindings.json`.
2. **Edit bindings**: The file uses a `bindings` array, where each block specifies a context (e.g., `Chat`, `Global`, `Transcript`) and a map of keystrokes to actions.
3. **Rebind a key**: Add an entry mapping the key combination to the desired action using `namespace:action` format — e.g., `"ctrl+s": "chat:submit"` or `"ctrl+e": "chat:externalEditor"`.
4. **Chord bindings**: Define multi-key sequences separated by spaces — e.g., `"ctrl+k ctrl+s"` for a two-press chord binding.
5. **Unbind a key**: Set an action to `null` to remove a default binding — e.g., `"ctrl+u": null`.
6. **Auto-reload**: Changes are automatically detected and applied without restarting Claude Code.

## Pro tips
- The keybindings file is plain JSON with an optional `$schema` field for editor autocompletion, so you can check it into your dotfiles repo and sync across machines
- Chord bindings are especially powerful with vim mode enabled — build custom vim-style sequences that trigger Claude-specific actions
- Some shortcuts are reserved and cannot be rebound: `Ctrl+C` (interrupt), `Ctrl+D` (exit), and `Ctrl+M` (identical to Enter in terminals)
- Run `/doctor` to see any keybinding warnings, including parse errors, invalid contexts, reserved conflicts, and duplicate bindings

## Status history
- **2025-12-15 (v2.1.29)**: Released with full keybinding customization and chord binding support
