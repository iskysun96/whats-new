---
name: Edit Tool Enhancement
category: Developer Tools
introduced_version: "2.1.89"
introduced_date: 2026-04-02
status: ga
ga_version: "2.1.89"
ga_date: 2026-04-02
one_liner: "Edit files directly after viewing them with bash commands without needing a separate read operation"
tags: [edit-tool, file-editing, bash-integration, workflow-optimization]
---

## What it does
This enhancement allows Claude to edit files immediately after viewing them with bash commands like `sed -n` or `cat`, without requiring a separate `Read` call first. It streamlines the file editing workflow by maintaining context from bash file viewing operations and enabling direct modifications.

## When to use it
- When you want to quickly edit a file after inspecting it with `cat` or `sed -n`
- While debugging code and need to make immediate fixes after viewing file contents
- During file exploration workflows where you discover issues that need quick corrections
- When batch processing files where you view and edit in rapid succession
- For iterative development where you frequently switch between viewing and editing files

## How to use it
1. Use a bash command to view a file: `cat filename.txt` or `sed -n '10,20p' script.py`
2. After Claude shows the file contents, directly use the Edit tool on the same file
3. Make your desired changes using standard edit syntax
4. Claude will apply the edits without needing to read the file again first

## Pro tips
- Works seamlessly with partial file views using `sed -n` line ranges - you can still edit the entire file
- Combine with `grep -n` to locate specific lines, then edit immediately without losing context
- Particularly useful in debugging sessions where you're rapidly cycling through view-and-fix operations

## Status history
- **2026-04-02 (v2.1.89)**: Introduced as generally available
