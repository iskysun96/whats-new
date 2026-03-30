---
name: Remote Control Sessions
category: Enterprise & Cloud
introduced_version: "2.1.79"
introduced_date: 2025-12-01
status: ga
ga_version: "2.1.79"
ga_date: 2025-12-01
one_liner: "Bridge terminal sessions to claude.ai/code for web-based session management with full bi-directional sync."
quick_start: "Sessions are automatically available at claude.ai/code"
tags: [remote, web, browser, sync, cloud]
---

## What it does
Connects your terminal-based Claude Code sessions to the web at claude.ai/code. You start a session in your terminal as usual, and it becomes accessible from your browser too. Changes flow both ways — type in the terminal or the web UI, and the other side stays in sync. Session URLs can be shared in commits and PRs so your team can see the context behind your changes. It's especially useful when you want a richer UI for reviewing Claude's output or sharing your session with a colleague.

## When to use it
- You started a session in the terminal but want to switch to a more visual interface for reviewing diffs
- You want to share a live session link with a teammate so they can see what you're working on
- You're adding session context to a pull request so reviewers understand the reasoning behind changes
- You want to continue a session from a different machine without losing context
- You need the web UI's rendering for large outputs that are hard to read in a terminal

## How to use it
1. Start a Claude Code session normally in your terminal
2. The session automatically gets a URL at claude.ai/code — look for it in the session header
3. Open the URL in your browser to access the web interface
4. Type in either the terminal or the web UI — both stay synced in real time
5. Copy the session URL and paste it into your commit messages or PR descriptions for team visibility
6. Access your session history at claude.ai/code to pick up where you left off

## Pro tips
- Drop the session URL into your PR description as a matter of habit — reviewers love being able to see the full conversation that led to the changes
- The web UI is better for reviewing multi-file diffs and long outputs, while the terminal is better for quick back-and-forth — use both
- Sessions persist even if you close your terminal, so you can always pick them back up from the web

## Status history
- **2025-12-01 (v2.1.79)**: Released as GA with bi-directional terminal-to-web sync
- **2026-01-10 (v2.1.88)**: Added session URL auto-insertion in git commits and PRs
