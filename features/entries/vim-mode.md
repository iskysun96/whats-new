---
name: Vim Mode
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Full vim motions and text objects in the Claude Code input editor."
tags: [vim, keybindings, editor, motions, text-objects]
---

## What it does
Vim Mode brings real vim keybindings to Claude Code's input editor. Not a watered-down subset — actual normal mode, insert mode, visual mode, motions like `w`, `b`, `e`, `gg`, `G`, and text objects like `iw`, `i"`, `a(`. If your fingers think in vim, they'll feel right at home. No more fighting muscle memory just to type a prompt.

## When to use it
- You're a vim user and `hjkl` is how your hands navigate text
- You want to quickly edit long, multi-line prompts without reaching for arrow keys
- You need to yank and paste within your prompt efficiently
- You're composing complex prompts and want the full power of vim's text manipulation
- You keep accidentally hitting `Escape` and wish it did something useful

## How to use it
1. **Enable vim mode**: Run `/config` and set `vim_mode: true`, or toggle it in settings.
2. **Start typing**: You begin in insert mode, just like vim.
3. **Press Escape**: Enter normal mode. Now `hjkl`, `w`, `b`, `dd`, `yy`, `p`, and all the usual suspects work.
4. **Visual mode**: Press `v` in normal mode to select text, then yank or delete it.
5. **Text objects**: In normal mode, commands like `ciw` (change inner word), `di"` (delete inside quotes), and `ya(` (yank around parens) all work as expected.

## Pro tips
- Vim mode pairs beautifully with multi-line input — use `o` and `O` to open new lines, `dd` to delete lines, and `J` to join them
- If you're used to a specific vim leader key workflow, check out the keybindings customization to set up chord bindings that complement vim mode
- Remember that `Escape` now enters normal mode instead of doing nothing — your vim reflexes finally pay off

## Status history
- **2025-12-15 (v2.1.29)**: Released with full normal, insert, and visual mode support including motions and text objects
