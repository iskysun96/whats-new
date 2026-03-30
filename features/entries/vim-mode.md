---
name: Vim Mode
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Full vim motions and text objects in the Claude Code input editor."
quick_start: "/vim"
detection:
  type: keyword
  patterns:
    - "vim.*mode"
    - "vim.*keybinding"
    - "hjkl"
    - "modal.*edit"
  tip: "Claude Code has built-in vim mode with full motions and text objects. Try /vim to enable it."
  signal: keyword
tags: [vim, keybindings, editor, motions, text-objects]
---

## What it does
Vim Mode brings real vim keybindings to Claude Code's input editor. Normal mode, insert mode, motions like `w`, `b`, `e`, `gg`, `G`, character motions like `f`/`F`/`t`/`T`, and text objects like `iw`, `i"`, `a(`. If your fingers think in vim, they'll feel right at home. No more fighting muscle memory just to type a prompt.

## When to use it
- You're a vim user and `hjkl` is how your hands navigate text
- You want to quickly edit long, multi-line prompts without reaching for arrow keys
- You need to yank and paste within your prompt efficiently
- You're composing complex prompts and want the full power of vim's text manipulation
- You keep accidentally hitting `Escape` and wish it did something useful

## How to use it
1. **Enable vim mode**: Run `/vim` to toggle vim mode on, or use `/config` to set it permanently. You can also set `editorMode` to `"vim"` in `~/.claude.json` directly.
2. **Start typing**: You begin in insert mode, just like vim.
3. **Press Escape**: Enter normal mode. Now `hjkl`, `w`, `b`, `dd`, `yy`, `p`, and all the usual suspects work.
4. **Character motions**: `f`/`F`/`t`/`T` with `;`/`,` repeat are supported for in-line navigation.
5. **Text objects**: In normal mode, commands like `ciw` (change inner word), `di"` (delete inside quotes), and `ya(` (yank around parens) all work as expected.

## Pro Tips
- Vim mode pairs beautifully with multi-line input — use `o` and `O` to open new lines, `dd` to delete lines, and `J` to join them
- If you're used to a specific vim leader key workflow, check out the keybindings customization to set up chord bindings that complement vim mode
- In vim normal mode, `Escape` switches to normal mode instead of triggering `chat:cancel` — vim mode and keybindings operate independently
- In normal mode, if the cursor is at the beginning or end of input and cannot move further, the arrow keys navigate command history instead

## Status history
- **2025-12-15 (v2.1.29)**: Released with normal and insert mode support including motions and text objects
