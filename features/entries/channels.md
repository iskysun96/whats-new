---
name: Channels (Mobile & Slack)
category: Enterprise & Cloud
introduced_version: "2.1.81"
introduced_date: 2025-12-10
status: public-beta
ga_version: null
ga_date: null
one_liner: "Access Claude Code from mobile devices, Slack, and other messaging platforms via channel servers."
quick_start: "Configure channel servers in settings"
tags: [channels, mobile, slack, remote, messaging]
---

## What it does
Breaks Claude Code out of the terminal and into the places where you already communicate. Channel servers act as a bridge — they relay your messages and Claude's responses between your messaging platform and a running Claude Code instance. You can send a task from your phone via Telegram, approve a permission request in Slack, or monitor progress from anywhere. The permission system carries over, so you still get approval workflows even when you're not at your desk.

## When to use it
- You kicked off a long-running task and want to monitor it from your phone while grabbing coffee
- Your team uses Slack and wants Claude Code integrated into their development channel
- You need to approve or deny a permission request while away from your terminal
- You want to quickly ask Claude a question about your codebase without opening a terminal
- You're on call and need to investigate a production issue from your mobile device

## How to use it
1. Configure a channel server in your Claude Code settings under the `channels` section
2. For Slack, set up the Claude Code Slack app and link it to your channel server
3. For Telegram, configure the Telegram bot token in your channel settings
4. Start a Claude Code session with channel support enabled
5. Send messages from your configured platform — they'll be relayed to the active session
6. Permission requests show up in your channel, and you can approve/deny with a reply

## Pro Tips
- Set up Slack channels per-project so your team can follow along with what Claude is doing in each repo
- The permission relaying is the killer feature — you can kick off a big task, walk away, and approve file writes from your phone as they come in
- Custom channel servers are supported if you want to integrate with something beyond the built-in options — the protocol is straightforward

## Status history
- **2025-12-10 (v2.1.81)**: Released as public beta with Slack and Telegram support
- **2026-02-01 (v2.1.95)**: Added custom channel server protocol documentation
