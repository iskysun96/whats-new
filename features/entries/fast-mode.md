---
name: Fast Mode
category: Core Modes
introduced_version: "2.1.81"
introduced_date: 2026-02-10
status: ga
ga_version: "2.1.81"
ga_date: 2026-02-10
one_liner: "Get 2.5x faster output from the same Opus 4.6 model — toggle with /fast."
quick_start: "/fast"
detection:
  type: keyword
  patterns:
    - "too.*slow"
    - "speed.*up"
    - "faster.*response"
    - "taking.*long"
    - "slow.*output"
    - "respond.*faster"
  tip: "Try /fast to toggle fast mode — same Opus 4.6 model but 2.5x faster output. Useful when speed matters more than cost."
  signal: keyword
tags: [fast, speed, performance, mode, output]
---

## What it does
Fast mode gives you 2.5x faster output from the same Claude Opus 4.6 model. It doesn't switch to a smaller or less capable model — it's the exact same Opus, just with faster token generation at a higher cost per token. Toggle it on when speed matters, toggle it off when you want to optimize for cost.

## When to use it
- You're iterating rapidly and waiting for Claude's responses feels like it's slowing you down
- You're in a live demo or pairing session where speed matters
- The task is straightforward and you don't need to think about cost optimization
- You're running quick one-off questions where latency is more annoying than cost

## How to use it
1. **Toggle on**: Run `/fast` or `/fast on` to enable fast mode
2. **Toggle off**: Run `/fast off` to return to normal speed
3. The mode persists for the rest of your session
4. Your current model is shown in the status bar — fast mode adds an indicator

## Pro Tips
- Fast mode is most noticeable on longer responses — short answers already feel instant
- For cost-sensitive work, keep fast mode off and only toggle it on for interactive back-and-forth moments
- Fast mode works with the same model, so quality and capabilities are identical — the only difference is speed and cost

## Status history
- **2026-02-10 (v2.1.81)**: Released as GA with 2.5x speed improvement on Opus 4.6
