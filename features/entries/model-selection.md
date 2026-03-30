---
name: Model Selection & Effort Control
category: Infrastructure
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Switch between Claude models and dial in effort levels to balance depth vs speed."
quick_start: "/model"
detection:
  type: keyword
  patterns:
    - "switch.*model"
    - "use.*haiku"
    - "use.*sonnet"
    - "too.*slow"
    - "faster.*model"
    - "cheaper.*model"
  tip: "You can switch models on the fly with /model — choose between Opus, Sonnet, and Haiku for different speed/quality tradeoffs."
  signal: keyword
tags: [model, effort, opus, sonnet, haiku, context-window]
---

## What it does
Lets you swap between Claude Opus, Sonnet, and Haiku mid-session without restarting anything. You can also set effort levels (low, medium, high) to control how deeply Claude thinks through a problem versus how fast it responds. Opus 4.6 supports extended context windows up to 1M tokens, so you can feed it entire codebases without chunking.

## When to use it
- You're doing quick edits and want Haiku's speed instead of burning Opus tokens on trivial changes
- You need deep architectural reasoning and want to bump up to Opus with high effort
- You're working with a massive codebase and need the full 1M token context window
- You want to keep costs down during exploration, then switch to a beefier model for the actual implementation
- You're comparing how different models handle the same task

## How to use it
1. Use `/model` in a session to see available models and switch between them
2. Set the thinking effort level using the `--effort` flag when launching Claude (e.g., `claude --effort low`), or use the `/model` command within a session to change it
3. Effort levels are `low`, `medium` (auto), and `high` (max) — controlling how deeply Claude reasons before responding
4. For 1M context, select Opus 4.6 (1M context) from the model list
5. You can also set your default model in `settings.json` under `model`
6. The current model and effort level are shown in the status bar at the bottom of your terminal

## Pro tips
- Start with Sonnet + medium effort for most tasks, escalate to Opus only when you hit something genuinely complex — your wallet will thank you
- Low effort (via `--effort low` or `/model`) on Haiku is perfect for quick "does this file exist" or "what's the type of X" questions
- The 1M context window on Opus 4.6 is real — you can load entire monorepos, but be mindful that more context means higher costs per request

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA with model switching and effort control
- **2025-12-15 (v2.0.0)**: Added 1M context window support for Opus 4.6
