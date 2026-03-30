---
name: Claude in Chrome
category: Editor Integration
introduced_version: "2.1.29"
introduced_date: 2025-09-10
status: ga
ga_version: "2.1.29"
ga_date: 2025-09-10
one_liner: "Browser extension that lets Claude control and interact with web pages — navigate, click, fill forms, extract data."
tags: [chrome, browser, extension, web-automation]
---

## What it does
Claude in Chrome is a browser extension that gives Claude the ability to see and interact with web pages. It can navigate to URLs, click buttons, fill out forms, extract data from tables, and generally do anything you'd do manually in a browser. Think of it as giving Claude hands for the web — it reads what's on screen and takes action.

## When to use it
- You need Claude to check a deployed web app and verify something looks right
- You want to automate a repetitive browser task like filling out forms or extracting data
- You're debugging a frontend issue and want Claude to interact with the live page
- You need Claude to read documentation or reference material from a website
- You want Claude to test a web flow end-to-end (login, navigate, submit)

## How to use it
1. Install the "Claude in Chrome" extension from the Chrome Web Store.
2. Make sure you're logged into your Anthropic account.
3. When Claude needs to interact with a website, it will automatically use the extension via the Computer Use tool.
4. You can also explicitly ask Claude to "go to [URL] and check [something]" and it will use the browser.
5. Grant permissions when prompted — the extension needs access to the pages Claude will interact with.

## Pro tips
- This pairs naturally with Computer Use — Claude in Chrome is the mechanism that makes browser-based Computer Use work smoothly.
- For data extraction tasks, Claude can read complex pages (tables, nested elements) that simple HTTP fetches would miss because it sees the rendered page.
- If you're testing a web app, ask Claude to walk through user flows and report what it sees — it's like having a QA tester on demand.

## Status history
- **2025-09-10 (v2.1.29)**: Released as generally available with support for navigation, clicking, form filling, and data extraction.
