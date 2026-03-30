---
name: VS Code Extension
category: Editor Integration
introduced_version: "2.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "2.0.0"
ga_date: 2025-05-01
one_liner: "Full Claude Code experience inside VS Code with inline chat, session tabs, and sidebar management."
quick_start: "Install 'Claude Code' from VS Code marketplace"
tags: [vscode, ide, editor, inline]
---

## What it does
The VS Code extension brings Claude Code directly into your editor as a native graphical panel. You can review and edit Claude's plans before accepting them, auto-accept edits, @-mention files with specific line ranges, access conversation history, and open multiple conversations in separate tabs or windows. It also works with Cursor.

## When to use it
- You live in VS Code and don't want to context-switch to a terminal
- You want inline code suggestions right next to the lines you're editing
- You need to juggle multiple Claude sessions for different tasks and want them organized as tabs
- You prefer a visual sidebar for managing your conversation history
- You're pair-programming with Claude and want tight editor integration

## How to use it
1. Open the Extensions panel in VS Code (Cmd+Shift+X on Mac, Ctrl+Shift+X on Windows/Linux).
2. Search for "Claude Code" and install the official extension (also available for Cursor).
3. Once installed, the quickest way to open Claude is to click the Spark icon in the Editor Toolbar (top-right corner of the editor). You can also click the Spark icon in the Activity Bar (left sidebar), use the Command Palette (Cmd+Shift+P / Ctrl+Shift+P), or click the "Claude Code" entry in the Status Bar (bottom-right).
4. Start a new session or open multiple conversations in separate tabs using "Open in New Tab" from the Command Palette.
5. Manage sessions (rename, remove, switch) from the Past Conversations dropdown at the top of the panel.

## Pro Tips
- Use Cmd+Esc (Mac) / Ctrl+Esc (Windows/Linux) to toggle focus between the editor and the Claude panel. Use Cmd+Shift+Esc / Ctrl+Shift+Esc to open a new conversation tab.
- You can have multiple sessions open in separate editor tabs — great for working on different features simultaneously. A colored dot on the tab icon indicates status (blue for pending permission, orange for finished while hidden).
- Use Option+K (Mac) / Alt+K (Windows/Linux) to insert an @-mention reference with file path and line numbers from your current selection.

## Status history
- **2025-05-01 (v2.0.0)**: Released as generally available with inline chat, session tabs, and sidebar management.
