---
name: Auto Mode
category: Core Modes
introduced_version: "2.1.86"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.86"
ga_date: 2025-12-15
one_liner: "Claude automatically decides whether to think through a problem or jump straight into action."
tags: [auto, mode, beginner-friendly, productivity]
---

## What it does
Auto Mode lets Claude decide on the fly whether it should plan first or start executing right away. Instead of you manually toggling between thinking and acting, Claude reads the situation and picks the right approach. Simple rename? It just does it. Complex refactor touching 12 files? It'll think it through first, then act.

## When to use it
- You're working on a mix of small and large tasks and don't want to keep switching modes
- You're new to Claude Code and want a sensible default that handles most workflows
- You want Claude to spend brainpower on hard problems but move fast on easy ones
- You're pairing with Claude interactively and want it to match your pace naturally
- You're unsure whether a task needs planning or not and want Claude to figure it out

## How to use it
1. **Toggle in-session**: Type `/auto` in the Claude Code prompt to switch to Auto Mode.
2. **Start from CLI**: Launch with `claude --auto` to begin in Auto Mode immediately.
3. Once active, just give Claude your task normally. It will determine whether to plan or execute based on the complexity of your request.
4. You can switch out of Auto Mode at any time by toggling to `/plan` or another mode.

## Pro tips
- Auto Mode is arguably the best default for everyday work. Set it as your default mode if you find yourself using it most of the time.
- If Claude keeps jumping to execution on something you want it to think about first, just say "think about this before coding" in your prompt -- it respects intent signals even in Auto Mode.
- Combine with `/compact` periodically during long sessions so Claude's context stays sharp and its auto-decisions stay accurate.

## Status history
- **2025-12-15 (v2.1.86)**: Released as GA. Claude can autonomously choose between planning and execution based on task complexity.
