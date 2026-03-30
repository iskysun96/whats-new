---
name: Grep & Glob Tools
category: Developer Tools
introduced_version: "1.0.0"
introduced_date: 2025-02-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-02-01
one_liner: "Fast codebase search — Grep searches file contents with regex, Glob finds files by name patterns."
tags: [search, grep, glob, regex, find]
---

## What it does
Two complementary search tools for navigating codebases of any size. **Grep** searches inside files using full regex syntax — find function definitions, track down error messages, locate usages of a variable. **Glob** finds files by name patterns — locate all TypeScript files, find config files, discover test files matching a pattern. Both are built on ripgrep and optimized to stay fast even on massive repositories.

## When to use it
- You need to find where a function is defined or called across the codebase
- You want to locate all files matching a pattern (e.g., all `*.test.ts` files)
- You're tracking down an error message and need to find where it originates
- You want to understand project structure by finding config files, entry points, etc.
- You need to search for a regex pattern like `TODO|FIXME|HACK` across the repo

## How to use it
1. Claude uses these tools automatically when searching your codebase.
2. **Grep** usage:
   - Provide a regex pattern to search for (e.g., `"function handleSubmit"`, `"import.*from 'react'"`)
   - Filter by file type (`type: "ts"`) or glob pattern (`glob: "*.tsx"`)
   - Choose output mode: `files_with_matches` (default), `content` (see matching lines), or `count`
   - Add context lines with `-A`, `-B`, or `-C` flags
3. **Glob** usage:
   - Provide a glob pattern like `"**/*.ts"`, `"src/**/*.test.js"`, or `"**/package.json"`
   - Results are sorted by modification time

## Pro tips
- Grep's `content` output mode with context lines (`-C 3`) is great for understanding how a function is used — you see the surrounding code, not just the matching line.
- Combine Grep and Glob: use Glob to find the files, then Grep to search within specific ones.
- For multiline patterns (like finding a struct definition that spans multiple lines), use `multiline: true` in Grep.

## Status history
- **2025-02-01 (v1.0.0)**: Released as generally available with ripgrep-based search and glob pattern matching.
