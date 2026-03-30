---
name: Claude in Chrome
category: Editor Integration
introduced_version: "2.1.29"
introduced_date: 2025-09-10
status: ga
ga_version: "2.1.29"
ga_date: 2025-09-10
one_liner: "Browser extension that lets Claude control and interact with web pages — navigate, click, fill forms, extract data."
quick_start: "/chrome or claude --chrome"
tags: [chrome, browser, extension, web-automation]
---

## What it does
Claude in Chrome is a browser extension (available for Google Chrome and Microsoft Edge) that gives Claude browser automation capabilities. It can navigate to URLs, click buttons, fill out forms, extract data, read console logs, and automate multi-site workflows. Claude opens new tabs for browser tasks and shares your browser's login state, so it can access any site you're already signed into. Browser actions run in a visible window in real time. Chrome integration is currently in beta.

## When to use it
- You need Claude to check a deployed web app and verify something looks right
- You want to automate a repetitive browser task like filling out forms or extracting data
- You're debugging a frontend issue and want Claude to interact with the live page
- You need Claude to read documentation or reference material from a website
- You want Claude to test a web flow end-to-end (login, navigate, submit)

## How to use it
1. Install the "Claude in Chrome" extension (version 1.0.36 or higher) from the Chrome Web Store (works in both Chrome and Edge).
2. In the CLI, start Claude Code with the `--chrome` flag (`claude --chrome`), or run `/chrome` within an existing session to enable it. In the VS Code extension, Chrome is available automatically when the extension is installed.
3. Ask Claude to interact with a website, e.g., "go to localhost:3000 and check the console for errors."
4. Claude uses its own browser tools (not the Computer Use tool) to navigate, click, type, read console logs, and more.
5. Site-level permissions are managed through the Chrome extension settings. When Claude encounters a login page or CAPTCHA, it pauses and asks you to handle it manually.

## Pro Tips
- Claude in Chrome and Computer Use are separate tools. Chrome integration is for browser-based tasks (web apps, debugging, data extraction), while Computer Use is for native desktop GUI control. Claude prefers Chrome over Computer Use for browser work when both are available.
- For data extraction tasks, Claude can read complex pages (tables, nested elements) that simple HTTP fetches would miss because it sees the rendered page.
- Claude can record browser interactions as GIFs to document or share what happened. Ask it to "record a GIF showing the checkout flow."
- To enable Chrome by default without passing `--chrome` each time, run `/chrome` and select "Enabled by default."

## Status history
- **2025-09-10 (v2.1.29)**: Released as generally available with support for navigation, clicking, form filling, and data extraction.
