---
name: WebFetch Tool
category: Developer Tools
introduced_version: "1.0.0"
introduced_date: 2025-02-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-02-01
one_liner: "Fetch and analyze web content — documentation, API responses, GitHub issues, and more."
tags: [web, fetch, http, documentation, api]
---

## What it does
WebFetch lets Claude reach out to the internet and pull in web content. It can read documentation pages, check API responses, fetch GitHub issues and pull requests, and grab any publicly accessible URL. Instead of you copy-pasting docs or error messages into the chat, Claude can just go read them directly. It's like giving Claude a browser for text content.

## When to use it
- You want Claude to read a library's documentation before using it in your code
- You need Claude to check a GitHub issue or PR for context on a bug
- You want Claude to fetch an API response to understand a data format
- You're working with a third-party service and need Claude to read their API docs
- You want Claude to pull in a Stack Overflow answer or blog post as reference

## How to use it
1. Just share a URL with Claude or ask it to look something up — it uses WebFetch automatically.
2. Say things like "read the docs at [URL]" or "check this GitHub issue [URL]".
3. Claude fetches the page content and uses it as context for your conversation.
4. Works with any publicly accessible URL — documentation sites, GitHub, APIs returning JSON, etc.

## Pro tips
- This is especially powerful for "use this library I've never used before" tasks — Claude can read the official docs and write correct code on the first try.
- For GitHub issues and PRs, Claude can fetch comments and discussion threads, giving it the full context of a conversation.
- If a page requires authentication or JavaScript rendering, WebFetch might not be able to access it — use Claude in Chrome for those cases instead.

## Status history
- **2025-02-01 (v1.0.0)**: Released as generally available with support for fetching and parsing web content.
