---
name: Computer Use
category: Developer Tools
introduced_version: "1.0.0"
introduced_date: 2025-02-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-02-01
one_liner: "Direct browser and desktop control — Claude can navigate websites, click buttons, fill forms, and interact with GUI applications."
tags: [computer-use, browser, gui, automation, desktop]
---

## What it does
Computer Use gives Claude the ability to interact with graphical interfaces just like a human would. It can take screenshots to see what's on screen, move the mouse, click buttons, type into fields, and navigate between windows. This means Claude can test web apps, automate GUI workflows, fill out forms, and interact with any application that has a visual interface — not just the terminal.

## When to use it
- You want Claude to test a web application by actually clicking through it
- You need to automate a GUI-based workflow that doesn't have a CLI or API
- You want Claude to fill out forms or configure settings in a web interface
- You need Claude to verify that a UI change looks correct after deployment
- You want Claude to interact with a desktop application (Figma, Slack, etc.)

## How to use it
1. Claude uses Computer Use automatically when it needs to interact with graphical interfaces.
2. Ask Claude to "open [URL] and click the submit button" or "check if the login page works."
3. Claude takes screenshots to see the current state, then performs actions (click, type, scroll).
4. For browser tasks, the Claude in Chrome extension provides the smoothest experience.
5. You'll see Claude's actions in real time and can intervene if needed.

## Pro tips
- Computer Use works best when paired with the Claude in Chrome extension — it gives Claude more reliable browser control.
- For repetitive GUI tasks, describe the full workflow once and Claude will execute all the steps in sequence.
- Claude can take screenshots at each step, so if something goes wrong, you can see exactly where the flow broke down.

## Status history
- **2025-02-01 (v1.0.0)**: Released as generally available with support for browser and desktop GUI interaction.
