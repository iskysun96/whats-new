---
name: Input Shortcuts
category: Customization
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Speed up your input with @ file mentions, ! bash mode, and multiline editing shortcuts."
quick_start: "Type @ to mention a file, ! to run a shell command"
tags: [input, shortcuts, mentions, bash-mode, multiline, productivity]
---

## What it does
Claude Code has several input shortcuts that speed up common interactions. **`@` file mentions** give you autocomplete for file and directory paths right in your prompt. **`!` bash mode** lets you run shell commands directly without Claude's involvement. **Multiline input** lets you write multi-line prompts using several different key combinations. These small shortcuts add up to a significantly faster workflow.

## When to use it
- You want to reference a specific file without typing the full path
- You need to quickly run a shell command without Claude interpreting it
- You're writing a complex, multi-line prompt or code snippet
- You want to paste content that spans multiple lines

## How to use it
1. **`@` file mentions**: Type `@` followed by a filename to get autocomplete suggestions. Select a file and it's referenced in your prompt with full path context. Works for files, directories, and even URLs.
2. **`!` bash mode**: Start your input with `!` followed by a command (e.g., `! git status`) to run it directly in your shell. The output appears in the conversation but Claude doesn't try to act on it.
3. **Multiline input**: Use any of these methods to write multi-line prompts:
   - `\` at the end of a line, then press Enter
   - `Option+Enter` (macOS) or `Alt+Enter` (Linux/Windows)
   - `Shift+Enter`
   - `Ctrl+J`

## Pro Tips
- `@` mentions are context-aware — they help Claude understand exactly which file you're talking about without ambiguity
- Chain `!` commands for quick checks: `! git log --oneline -5` to see recent commits without Claude offering to help
- Use multiline input when pasting error messages, code snippets, or writing detailed instructions — it's much cleaner than cramming everything onto one line
- `@` also works with MCP resource URIs if you have MCP servers configured

## Status history
- **2025-05-01 (v1.0.0)**: Released with `@` file mentions and `!` bash mode
- **2025-09-15 (v2.0.0)**: Added multiline input methods (Option+Enter, Shift+Enter, Ctrl+J)
