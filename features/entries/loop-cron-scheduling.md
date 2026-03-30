---
name: Loop & Cron Scheduling
category: Workflow & Automation
introduced_version: "2.1.75"
introduced_date: 2026-02-10
status: ga
ga_version: "2.1.75"
ga_date: 2026-02-10
one_liner: "Run prompts or commands on recurring intervals — set it and forget it."
quick_start: "/loop 5m run the tests"
detection:
  type: repeated_command
  threshold: 3
  no_edits_between: true
  tip: "You've run `{command}` {count} times without changes in between. Loop can automate this — try `/loop 5m {command}`."
  signal: behavioral
tags: [loop, cron, scheduling, recurring, automation]
---

## What it does
Loop & Cron Scheduling lets you run any prompt or slash command on a repeating interval, right from inside Claude Code. `/loop 5m check if the deployment finished` runs that check every 5 minutes. Under the hood, `/loop` converts intervals to cron expressions and schedules jobs using the CronCreate tool. All scheduled tasks are session-scoped — they live in the current Claude Code process and are gone when you exit. For durable scheduling that survives restarts, use Cloud scheduled tasks, Desktop scheduled tasks, or GitHub Actions.

## When to use it
- You're fixing flaky tests and want to run the suite every few minutes to see if your fix holds
- You need to poll a deployment status or health check endpoint repeatedly
- You want Claude to periodically review a log file or build output while you focus on something else
- You're running a long migration and want periodic progress checks
- You want a one-time reminder to check on something later in your session

## How to use it
1. **Quick loop**: Type `/loop 5m check the build logs for errors` to run that prompt every 5 minutes. The default interval is 10 minutes if you omit the time.
2. **Loop over a command**: `/loop 20m /review-pr 1234` runs that skill every 20 minutes. You can also put the interval at the end: `/loop check the build every 2 hours`.
3. **One-time reminders**: Describe what you want in natural language — e.g., `remind me at 3pm to push the release branch` — and Claude schedules a single-fire task.
4. **List active schedules**: Ask Claude "what scheduled tasks do I have?" or reference the CronList tool directly.
5. **Cancel a schedule**: Ask Claude to cancel a task by description, or use CronDelete with the task's 8-character ID.

## Pro Tips
- Loops are great for "watch mode" workflows — pair them with `/compact` if the conversation gets long
- All session-scoped tasks automatically expire after 3 days. For durable scheduling, use Cloud or Desktop scheduled tasks instead
- You can nest slash commands inside loops — `/loop 15m /doctor` is a nice way to keep tabs on project health
- Supported interval units are `s` (seconds, rounded up to nearest minute), `m` (minutes), `h` (hours), and `d` (days)

## Status history
- **2026-02-10 (v2.1.75)**: Released with loop intervals and cron-based scheduling support
