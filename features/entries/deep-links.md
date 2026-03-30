---
name: Deep Links
category: Workflow & Automation
introduced_version: "2.1.84"
introduced_date: 2026-03-10
status: ga
ga_version: "2.1.84"
ga_date: 2026-03-10
one_liner: "Launch Claude Code sessions from external apps and docs using claude-cli:// URIs."
quick_start: "claude-cli://open?q=your+prompt"
tags: [deep-links, uri, protocol, launch, integration]
---

## What it does
Deep Links register a `claude-cli://` URI protocol on your system so external apps, documentation pages, or scripts can launch Claude Code sessions directly. Click a link in your team's wiki and Claude Code opens with the right context already loaded. It bridges the gap between your browser, your docs, and your terminal — no copy-pasting instructions needed.

## When to use it
- Your team docs include runbooks and you want one-click "ask Claude to help with this" links
- You're building internal tooling and want buttons that launch Claude with specific prompts
- You want to share a reproducible Claude Code workflow with a teammate via a simple link
- You're writing onboarding docs and want new devs to jump straight into guided Claude sessions
- You have scripts that need to hand off to an interactive Claude session

## How to use it
1. **Use a deep link**: Click or open any `claude-cli://` URI — Claude Code will launch with the parameters encoded in the link. For example, `claude-cli://open?q=...` opens a session with a pre-filled prompt.
2. **Protocol registration**: Claude Code automatically registers the `claude-cli://` protocol handler with the operating system on startup.
3. **Embed in docs**: Add deep links to your team wiki, README, or internal documentation for common workflows.
4. **Disable if needed**: Set `disableDeepLinkRegistration` to `"disable"` in settings to prevent Claude Code from registering the protocol handler on startup.

## Pro tips
- Deep links are great for team playbooks — instead of writing "open Claude and paste this prompt," just give them a clickable link
- Combine with custom agents to create deep links that launch Claude with a specific agent persona and task already configured

## Status history
- **2026-03-10 (v2.1.84)**: Released with claude-cli:// URI protocol support for external app integration
