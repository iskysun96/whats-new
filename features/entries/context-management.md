---
name: Context Management
category: Memory & Context
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Monitor and optimize your context window usage with auto-compaction and usage insights."
tags: [context, compaction, optimization, tokens, window]
---

## What it does
Context Management gives you visibility into how much of Claude's context window you're using and helps you optimize it. When your conversation gets long, auto-compaction kicks in and intelligently summarizes older parts of the conversation so you can keep working without hitting limits. You can also manually compact at any time or check your usage to understand where your tokens are going.

## When to use it
- You're in a long session and Claude starts feeling "forgetful" about earlier context
- You want to understand how much context budget you have left before hitting limits
- You're working on a large codebase and reading lots of files is eating into your context
- You notice Claude's responses getting slower or less coherent as the conversation grows
- You want to proactively free up context space before a complex multi-step task

## How to use it
1. **Check usage**: Run `/context` to see a breakdown of your current context window usage with optimization suggestions.
2. **Manual compaction**: Run `/compact` to immediately summarize and compress older conversation history.
3. **Auto-compaction**: This happens automatically when you approach context limits — no action needed.
4. **Compact with focus**: Run `/compact focus on the database migration` to tell compaction what to prioritize retaining.

## Pro tips
- Use `/compact` with a focus phrase before starting a new sub-task — it keeps relevant context while freeing up space for the new work
- If you notice Claude "forgetting" something important after auto-compaction, mention it again — the compaction summary may have deprioritized it
- Long file reads are a common context hog; consider pointing Claude to specific line ranges instead of entire files

## Status history
- **2025-05-01 (v1.0.0)**: Released with `/context` usage display and `/compact` manual compaction
- **2025-07-10 (v1.0.30)**: Added auto-compaction with intelligent summarization
- **2025-09-15 (v2.0.0)**: Added focus-aware compaction with `/compact <topic>`
