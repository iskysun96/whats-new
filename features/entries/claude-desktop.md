---
name: Claude Desktop App
category: Editor Integration
introduced_version: "2.1.76"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.76"
ga_date: 2025-12-15
one_liner: "The Code tab in the Claude Desktop app for Mac and Windows — full GUI with visual diff review, live app preview, computer use, and parallel sessions."
quick_start: "Download from claude.ai → Code tab"
tags: [desktop, native, gui, app, standalone]
---

## What it does
The Code tab within the Claude Desktop app lets you use Claude Code through a graphical interface instead of the terminal. It's available for macOS and Windows (Linux is not currently supported). On top of the standard Claude Code experience, Desktop adds visual diff review with inline comments, live app preview with dev servers, computer use (macOS only), GitHub PR monitoring with auto-fix and auto-merge, parallel sessions with automatic Git worktree isolation, Dispatch integration, scheduled tasks, and connectors for GitHub, Slack, Linear, and more. You can also run long-running tasks remotely and monitor them from claude.ai/code.

## When to use it
- You want Claude Code but aren't comfortable with terminal workflows
- You're on a machine where you prefer a native app over a CLI tool
- You want a dedicated window for Claude that doesn't compete with your terminal tabs
- You're doing code review or exploration and want a more visual experience
- You need quick access to Claude Code without any IDE or terminal setup

## How to use it
1. Download the Claude Desktop app from [claude.ai](https://claude.ai) (macOS universal build or Windows x64/ARM64). Linux is not currently supported.
2. Install and open the application.
3. Sign in with your Anthropic account (requires a Pro, Max, Teams, or Enterprise subscription).
4. Click the **Code** tab at the top center of the app.
5. Select your environment (Local, Remote, or SSH), choose a project folder, pick a model, and set a permission mode, then start working.

## Pro Tips
- The desktop app is great for non-engineers (designers, PMs) who want to interact with codebases without learning terminal commands.
- You can run it alongside your IDE — use your editor for writing code and the desktop app for asking Claude questions about the codebase.
- Use parallel sessions from the sidebar to work on multiple tasks at once — each session gets its own isolated Git worktree so changes don't interfere with each other.
- You can send long-running tasks to the cloud by selecting "Remote" instead of "Local" — they continue even if you close the app.

## Status history
- **2025-12-15 (v2.1.76)**: Released as generally available for Mac and Windows.
