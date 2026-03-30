---
name: Copy Picker
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Select and copy specific code blocks from Claude's responses without manual highlighting."
quick_start: "/copy"
tags: [copy, clipboard, code-blocks, productivity]
---

## What it does
Copy Picker lets you grab any code block from Claude's responses with precision. Instead of squinting at your terminal trying to highlight exactly the right text (and inevitably grabbing a line number or some surrounding prose), you open the picker, select the block you want, and it lands cleanly in your clipboard. It knows where every code block starts and ends, so you don't have to.

## When to use it
- Claude generated a code snippet you want to paste into your editor
- There are multiple code blocks in a response and you need a specific one
- You're collecting code snippets from a long conversation
- Manual text selection in your terminal is fighting you (as it does)
- You want to quickly grab a shell command Claude suggested without the surrounding explanation

## How to use it
1. **Copy the last response**: Type `/copy` to copy Claude's most recent response to the clipboard.
2. **Copy an older response**: Pass a number — `/copy 2` copies the second-to-last response, `/copy 3` the third-to-last, etc.
3. **Pick a code block**: When code blocks are present in the response, an interactive picker appears so you can select individual blocks or the full response.
4. **Write to file**: Press `w` in the picker to write the selection to a file instead of the clipboard — useful when working over SSH where clipboard access isn't available.

## Pro tips
- Use `/copy` without arguments for the most common case — grabbing the last thing Claude said
- The `w` key in the picker is a lifesaver when you're SSH'd into a remote machine and can't use clipboard
- This works especially well after asking Claude to generate multiple file contents — pick exactly the file you need without scrolling back

## Status history
- **2025-12-15 (v2.1.29)**: Released with code block selection and automatic clipboard copying
