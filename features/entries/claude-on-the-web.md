---
name: Claude Code on the Web
category: Editor Integration
introduced_version: "2.1.70"
introduced_date: 2026-01-15
status: ga
ga_version: "2.1.70"
ga_date: 2026-01-15
one_liner: "Run Claude Code in your browser at claude.ai/code — no local setup needed."
quick_start: "Visit claude.ai/code"
tags: [web, browser, cloud, no-setup, platform]
---

## What it does
Claude Code on the Web lets you run Claude Code directly in your browser at claude.ai/code, with no local installation required. You get the same agentic coding experience — file editing, terminal commands, web search — but running on Anthropic's infrastructure. Sessions can also be scheduled to run on a recurring basis from the web interface, and you can teleport web sessions to your local terminal with `claude --teleport`.

## When to use it
- You're on a machine where you can't install Claude Code locally (work laptop restrictions, Chromebook, etc.)
- You want to try Claude Code without committing to a local install
- You need to run scheduled tasks on cloud infrastructure instead of your local machine
- You're pairing with someone remotely and want to share a session via URL
- You want to kick off work from your phone or tablet

## How to use it
1. Visit **claude.ai/code** in your browser and sign in
2. Start a new session — you get a full terminal environment in the browser
3. Work as you normally would: edit files, run commands, ask Claude for help
4. **Teleport to local**: Run `claude --teleport` in your local terminal to continue a web session locally
5. **Schedule tasks**: Use the web UI to create recurring scheduled tasks that run on Anthropic infrastructure

## Pro Tips
- Web sessions are great for experimenting — spin one up, try something, and close it without touching your local environment
- Use `claude --teleport` when you start work on the web (e.g., from your phone) and want to continue with your full local tooling
- Scheduled tasks on the web run even when your machine is off — useful for nightly builds, daily reports, or periodic code checks
- The `/desktop` command moves a local session to the desktop app, while `--teleport` moves a web session to your local terminal — they're complementary

## Status history
- **2026-01-15 (v2.1.70)**: Released as GA at claude.ai/code with browser-based sessions, scheduling, and teleport support
