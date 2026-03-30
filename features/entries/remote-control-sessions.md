---
name: Remote Control Sessions
category: Enterprise & Cloud
introduced_version: "2.1.51"
introduced_date: 2026-02-24
status: ga
ga_version: "2.1.51"
ga_date: 2026-02-24
one_liner: "Continue local Claude Code sessions from any device via claude.ai/code or the Claude mobile app, with your full local environment still running."
quick_start: "Run `claude remote-control` or use `/remote-control` inside a session to make it available at claude.ai/code"
tags: [remote, web, browser, mobile, cloud]
---

## What it does
Connects a locally running Claude Code session to claude.ai/code or the Claude mobile app (iOS/Android) so you can drive it from another device. Claude keeps running on your machine the entire time — your filesystem, MCP servers, tools, and project configuration all stay available. The web and mobile interfaces are just a window into that local session, not a separate cloud environment. You can send messages from your terminal, browser, and phone interchangeably, and the conversation stays in sync across all connected devices. If your laptop sleeps or the network drops, the session reconnects automatically when your machine comes back online.

## When to use it
- You started a session at your desk and want to keep steering it from your phone or a different computer
- You want a richer web UI for reviewing diffs and long outputs that are hard to read in a terminal
- You want to share a live session link with a teammate so they can see what you're working on
- You need your full local environment (filesystem, MCP servers, tools) available while working from another device
- You want to continue working from a browser without setting up a separate cloud environment

## How to use it
There are three ways to start a Remote Control session:

**Server mode** — run `claude remote-control` in your project directory. This starts a dedicated server that waits for remote connections. Press spacebar to show a QR code for quick phone access. Supports `--name`, `--spawn`, `--capacity`, `--verbose`, and `--sandbox` flags.

**Interactive session** — run `claude --remote-control` (or `claude --rc`) to start a normal interactive session with Remote Control enabled. You can type locally while the session is also available remotely.

**From an existing session** — type `/remote-control` (or `/rc`) inside a running Claude Code session. This makes your current session available remotely, carrying over your conversation history.

Once active:
1. Open the session URL displayed in the terminal, or scan the QR code with your phone
2. Alternatively, find the session by name at claude.ai/code or in the Claude mobile app — online sessions show a green status dot
3. Send messages from any connected device — terminal, browser, or phone

To enable Remote Control for every session automatically, run `/config` and set "Enable Remote Control for all sessions" to `true`.

## Pro tips
- Use server mode (`claude remote-control --spawn worktree`) to run multiple concurrent sessions, each in its own git worktree
- Use `/mobile` inside Claude Code to get a QR code for downloading the Claude app on iOS or Android
- Unlike Claude Code on the web, Remote Control runs on your machine — use it when you need your local MCP servers and tools; use web sessions when you want cloud infrastructure
- The session title can be set with `--name`, `--remote-control "name"`, `/remote-control name`, or `/rename`
- Remote Control requires a claude.ai subscription (Pro, Max, Team, or Enterprise) — API keys are not supported. On Team and Enterprise plans, an admin must enable the Remote Control toggle in admin settings first

## Status history
- **2026-02-24 (v2.1.51)**: Added `claude remote-control` subcommand, enabling local environment serving
- **2026-02-25 (v2.1.58)**: Expanded Remote Control availability to more users
- **2026-03-18 (v2.1.79)**: Added `/remote-control` slash command for VS Code, session bridging to claude.ai/code from browser or phone
