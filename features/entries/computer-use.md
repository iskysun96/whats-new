---
name: Computer Use
category: Developer Tools
introduced_version: "1.0.0"
introduced_date: 2025-02-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-02-01
one_liner: "macOS screen control — Claude can open apps, click, type, scroll, and take screenshots to interact with native GUI applications."
tags: [computer-use, browser, gui, automation, desktop]
---

## What it does
Computer Use gives Claude the ability to interact with graphical interfaces on macOS. It can take screenshots to see what's on screen, click buttons, type into fields, scroll, and control apps. This is a research preview available only on macOS with a Pro or Max plan (not available on Team or Enterprise plans). Computer Use is specifically for native GUI tasks that can't be handled by other tools — Claude prefers MCP servers, Bash, or Chrome integration when those are available, and falls back to Computer Use only when nothing else can reach the task.

## When to use it
- You need Claude to build and validate a native macOS app by compiling, launching, and clicking through it
- You need to automate a GUI-based workflow that doesn't have a CLI or API
- You want Claude to debug visual or layout issues by resizing windows and taking screenshots
- You need Claude to drive GUI-only tools like the iOS Simulator, hardware control panels, or proprietary apps
- You want Claude to test a desktop application's UI end-to-end

## How to use it
1. Computer Use is off by default. Enable it by running `/mcp` in an interactive session, finding the `computer-use` server, and selecting Enable.
2. Grant macOS permissions when prompted: Accessibility (for clicking, typing, scrolling) and Screen Recording (for seeing your screen). You may need to restart Claude Code after granting Screen Recording.
3. The first time Claude needs a specific app in a session, you'll be prompted to approve access for that app. Approvals last for the current session.
4. Ask Claude to do GUI tasks, e.g., "build the app, launch it, and click through each tab to check for crashes."
5. Press Esc anywhere to abort Computer Use immediately. Claude releases control and restores your hidden apps.

## Pro tips
- Computer Use and Claude in Chrome are separate tools. For browser tasks, use Chrome integration — it's faster and more precise. Computer Use is for native apps and GUIs that nothing else can reach.
- While Claude is working, other visible apps are hidden so it only interacts with approved apps. Your terminal stays visible and is excluded from screenshots.
- Only one Claude Code session can use Computer Use at a time (it holds a machine-wide lock). Apps with broad reach (terminals, Finder, System Settings) show extra warnings before you approve them.

## Status history
- **2025-02-01 (v1.0.0)**: Released as generally available with support for browser and desktop GUI interaction.
