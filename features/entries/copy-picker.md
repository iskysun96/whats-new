---
name: Copy Picker
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Select and copy specific code blocks from Claude's responses without manual highlighting."
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
1. **Open the picker**: Type `/copy` to launch the copy picker.
2. **Browse blocks**: See a numbered list of all code blocks from Claude's recent responses.
3. **Select a block**: Choose the one you want by number or arrow keys.
4. **Copied**: The selected code block is automatically copied to your clipboard, ready to paste.

## Pro tips
- The picker shows code blocks in order of appearance, so the most recent ones are at the bottom — if you want the last thing Claude wrote, jump to the end
- This works especially well after asking Claude to generate multiple file contents — pick exactly the file you need without scrolling back
- Pair with transcript mode if you need to find and copy a code block from much earlier in the conversation

## Status history
- **2025-12-15 (v2.1.29)**: Released with code block selection and automatic clipboard copying
