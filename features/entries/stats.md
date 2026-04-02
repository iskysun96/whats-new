---
name: Stats
category: Customization
introduced_version: "2.1.59"
introduced_date: 2025-12-01
status: ga
ga_version: "2.1.59"
ga_date: 2025-12-01
one_liner: "Visualize your daily usage, session history, streaks, and model preferences."
quick_start: "/stats"
tags: [stats, usage, visualization, streaks, history]
---

## What it does
The `/stats` command gives you a visual overview of how you've been using Claude Code over time. It shows daily usage patterns, session history, usage streaks, and which models you've been using most. Unlike `/cost` (which focuses on tokens and spend for the current session), `/stats` is about your long-term usage picture.

**Note**: For current session token counts and cost estimates, see the **Cost & Stats Tracking** entry (`/cost`).

## When to use it
- You're curious how much you've been using Claude Code day-to-day
- You want to see your usage streak (how many consecutive days you've used it)
- You're interested in which models you gravitate toward most
- You want a quick overview of your recent session history
- You're tracking your own productivity habits with Claude Code

## How to use it
1. Run `/stats` to see your usage dashboard
2. Review daily usage patterns — see which days you use Claude Code most
3. Check your streak — how many consecutive days you've used it
4. See model preference breakdown — which models you use and how often

## Pro Tips
- Use `/stats` alongside `/insights` for a complete picture — stats shows quantitative usage, insights shows qualitative patterns
- Your streak resets if you miss a day, so check `/stats` to keep it going if you're competitive about it
- Model preference data can help you decide if you should default to a different model

## Status history
- **2025-12-01 (v2.1.59)**: Released as GA with daily usage visualization, streaks, and model preference tracking
