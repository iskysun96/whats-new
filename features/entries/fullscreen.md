---
name: Fullscreen Rendering
category: Customization
introduced_version: "2.1.89"
introduced_date: 2026-04-02
status: public-beta
one_liner: "Flicker-free alternate screen rendering with mouse support and constant memory usage."
quick_start: "CLAUDE_CODE_NO_FLICKER=1 claude"
detection:
  type: keyword
  patterns:
    - "flicker"
    - "screen.*flash"
    - "scroll.*jump"
    - "fullscreen"
    - "alternate.*screen"
    - "mouse.*click"
  tip: "Try fullscreen rendering for a flicker-free experience: CLAUDE_CODE_NO_FLICKER=1 claude. It also adds mouse support for clicking URLs, files, and tool results."
  signal: keyword
tags: [fullscreen, rendering, flicker-free, mouse, terminal, ui]
---

## What it does
Fullscreen rendering is an alternate display mode that draws on the terminal's alternate screen buffer — like `vim` or `htop` — instead of the normal scrollback. This eliminates screen flicker and scroll-jump issues that some terminals experience (especially VS Code's integrated terminal, tmux, and iTerm2). It also adds mouse support: click to position your cursor, click to expand/collapse tool results, click URLs and file paths to open them, and click-and-drag to select text.

## When to use it
- Your terminal flickers or flashes during Claude's output (common in VS Code integrated terminal)
- You're in a long session and notice increasing memory usage or scroll jitter
- You want mouse interaction — clicking file paths, URLs, or expanding tool results
- You use tmux and want a rendering mode that plays nicely with `set -g mouse on`
- You prefer a full-screen TUI experience over traditional scrolling output

## How to use it
1. **Enable**: Start Claude with `CLAUDE_CODE_NO_FLICKER=1 claude`
2. **Scroll**: Use PgUp/PgDn or mouse wheel to scroll through the conversation
3. **Transcript mode**: Press `Ctrl+o` for a less-style full transcript with `/` search, `n`/`N` for next/prev match
4. **Open files/URLs**: Click on file paths or URLs in Claude's output to open them
5. **Expand/collapse**: Click on tool result headers to expand or collapse them
6. **Adjust scroll speed**: Set `CLAUDE_CODE_SCROLL_SPEED=1` through `20` (default varies)
7. **Disable mouse only**: Set `CLAUDE_CODE_DISABLE_MOUSE=1` to keep flicker-free rendering but restore native terminal text selection

## Pro Tips
- If you like it, add `export CLAUDE_CODE_NO_FLICKER=1` to your shell profile so it's always on
- Press `[` in transcript mode (`Ctrl+o`) to dump the conversation to your native scrollback — useful for copying large sections
- Press `v` in transcript mode to open the full conversation in your `$EDITOR`
- Incompatible with iTerm2's `tmux -CC` integration mode — use regular tmux instead

## Status history
- **2026-04-02 (v2.1.89)**: Released as research preview (public beta) with alternate screen rendering, mouse support, and transcript mode
