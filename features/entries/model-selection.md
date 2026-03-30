---
name: Model Selection & Effort Control
category: Infrastructure
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Switch between Claude models and dial in effort levels to balance depth vs speed."
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
2. Use `/effort` to set the effort level — `low` for quick responses, `medium` for balanced, `high` for deep reasoning
3. For 1M context, select Opus 4.6 (1M context) from the model list
4. You can also set your default model in `settings.json` under `preferredModel`
5. The current model and effort level are shown in the status bar at the bottom of your terminal

## Pro tips
- Start with Sonnet + medium effort for most tasks, escalate to Opus only when you hit something genuinely complex — your wallet will thank you
- Low effort on Haiku is perfect for quick "does this file exist" or "what's the type of X" questions
- The 1M context window on Opus 4.6 is real — you can load entire monorepos, but be mindful that more context means higher costs per request

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA with model switching and effort control
- **2025-12-15 (v2.0.0)**: Added 1M context window support for Opus 4.6
