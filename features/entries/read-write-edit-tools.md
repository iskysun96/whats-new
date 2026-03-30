---
name: Read/Write/Edit Tools
category: Developer Tools
introduced_version: "1.0.0"
introduced_date: 2025-02-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-02-01
one_liner: "Core file manipulation — read files with line numbers, write new files, and make surgical edits with exact string replacement."
tags: [files, edit, read, write, core]
---

## What it does
These are the bread-and-butter tools Claude uses to work with your files. **Read** views file contents with line numbers (and handles images, PDFs, and Jupyter notebooks too). **Write** creates new files or completely rewrites existing ones. **Edit** makes precise, surgical changes using exact string matching — you specify the old text and the new text, and Claude swaps them. Together, they give Claude full file manipulation capabilities with a bias toward minimal, targeted changes.

## When to use it
- You want Claude to fix a bug — it reads the file, finds the issue, and edits just the affected lines
- You need a new file created (a component, test, config file, etc.)
- You want Claude to review a file and understand its structure before making changes
- You need Claude to read a screenshot, PDF, or Jupyter notebook to understand context
- You want Claude to refactor code by making precise replacements across a file

## How to use it
1. Claude uses these tools automatically whenever it needs to interact with files.
2. **Read**: Claude reads a file (or specific line ranges for large files). Supports images, PDFs (with page ranges), and `.ipynb` notebooks.
3. **Write**: Claude creates a new file or does a complete rewrite. It must read a file first before overwriting it.
4. **Edit**: Claude specifies an `old_string` and `new_string` for exact replacement. The old string must be unique in the file, or Claude provides more context to disambiguate.

## Pro tips
- Edit is preferred over Write for modifications because it only sends the diff — faster and less error-prone than rewriting entire files.
- For large files, Claude can read specific line ranges (using `offset` and `limit`) instead of loading the whole thing.
- The `replace_all` flag on Edit lets Claude rename variables or update strings across an entire file in one shot.

## Status history
- **2025-02-01 (v1.0.0)**: Released as generally available as the core file manipulation toolset.
