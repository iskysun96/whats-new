---
name: Bare Mode
category: Core Modes
introduced_version: "2.1.81"
introduced_date: 2025-11-28
status: ga
ga_version: "2.1.81"
ga_date: 2025-11-28
one_liner: "Stripped-down execution mode that skips hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md for maximum speed."
quick_start: "claude --bare -p 'your prompt'"
tags: [scripting, automation, lightweight, ci-cd, headless]
---

## What it does
Bare Mode launches Claude Code without loading hooks, skills, plugins, MCP servers, auto memory, or CLAUDE.md. It's the lightest-weight way to run Claude programmatically. Startup is near-instant because there's nothing extra to initialize. You get Claude Code with Bash, file read, and file edit tools, but none of the surrounding ecosystem. It also skips OAuth and keychain reads -- Anthropic authentication must come from `ANTHROPIC_API_KEY` or an `apiKeyHelper` in settings passed via `--settings`. It's built for scripts, CI pipelines, and automation where you want predictable, fast execution.

## When to use it
- You're calling Claude Code from a shell script or CI/CD pipeline and need fast startup
- You want deterministic behavior without hooks or plugins potentially altering output
- You're running batch operations across many files or repos and every second of startup matters
- You need headless execution in environments where MCP servers aren't available or relevant
- You're building tooling on top of Claude Code and want a clean, minimal interface

## How to use it
1. **Basic usage**: Run `claude --bare -p "your prompt"` to execute a single prompt with minimal overhead.
2. **In scripts**: Pipe input or use heredocs for multi-line prompts:
   ```bash
   claude --bare -p "Summarize the changes in this diff" < changes.diff
   ```
3. **In CI/CD**: Add to your pipeline steps. Bare Mode won't try to load local hooks or connect to MCP servers that aren't present in the CI environment.
4. The `-p` flag (print mode) is almost always paired with `--bare` for scripted usage, since it outputs the result and exits.

## Pro tips
- If your automation scripts are mysteriously slow, check whether you're running without `--bare`. Loading hooks, skills, plugins, MCP servers, and CLAUDE.md on every invocation in a loop adds up fast.
- Bare Mode skips CLAUDE.md, hooks, skills, plugins, MCP servers, and auto memory. Only flags you pass explicitly take effect. If you need system prompt additions, use `--append-system-prompt` or `--append-system-prompt-file`. If you need MCP servers, use `--mcp-config`. If you need settings, use `--settings`.
- Combine with `--output-format json` for machine-readable output that's easy to parse downstream in your pipeline.

## Status history
- **2025-11-28 (v2.1.81)**: Released as GA. Lightweight execution mode for scripting and automation without hooks, skills, plugins, MCP servers, auto memory, or CLAUDE.md.
