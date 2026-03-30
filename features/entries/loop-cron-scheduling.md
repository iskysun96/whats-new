---
name: Loop & Cron Scheduling
category: Workflow & Automation
introduced_version: "2.1.75"
introduced_date: 2026-02-10
status: ga
ga_version: "2.1.75"
ga_date: 2026-02-10
one_liner: "Run prompts or commands on recurring intervals — set it and forget it."
tags: [loop, cron, scheduling, recurring, automation]
---

## What it does
Loop & Cron Scheduling lets you run any prompt or slash command on a repeating interval, right from inside Claude Code. `/loop 5m /test` runs your test suite every 5 minutes. For longer-lived or persistent schedules, cron-based scheduling lets you set up tasks that survive session restarts. Think of it as your personal CI that lives in your terminal.

## When to use it
- You're fixing flaky tests and want to run the suite every few minutes to see if your fix holds
- You need to poll a deployment status or health check endpoint repeatedly
- You want Claude to periodically review a log file or build output while you focus on something else
- You're running a long migration and want periodic progress checks
- You need a persistent scheduled task that runs even across sessions

## How to use it
1. **Quick loop**: Type `/loop 5m /test` to run `/test` every 5 minutes. The default interval is 10 minutes if you omit the time.
2. **Loop with a prompt**: `/loop 10m check the build logs for errors` runs that prompt on repeat.
3. **Cron scheduling**: Use the CronCreate tool to set up persistent scheduled tasks with cron expressions.
4. **List active schedules**: CronList shows all your active scheduled tasks.
5. **Stop a schedule**: CronDelete removes a scheduled task by ID.
6. **Stop a loop**: Press `Ctrl+C` or type `/stop` to cancel an active loop.

## Pro tips
- Loops are great for "watch mode" workflows — pair them with `/compact` if the conversation gets long
- Cron schedules persist across sessions, so use them for things like daily code review reminders or periodic dependency checks
- You can nest slash commands inside loops — `/loop 15m /doctor` is a nice way to keep tabs on project health

## Status history
- **2026-02-10 (v2.1.75)**: Released with loop intervals and cron-based scheduling support
