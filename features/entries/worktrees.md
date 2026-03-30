---
name: Worktrees
category: Workflow & Automation
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Run agents in isolated git worktrees so they never block your main branch."
tags: [worktrees, git, isolation, parallel, branches]
---

## What it does
Worktrees let you spin up Claude agents in their own isolated git worktrees — separate working directories on separate branches. This means an agent can make changes, commit, and even push without touching your main checkout. It's perfect for running multiple agents in parallel on different tasks without any of them stepping on each other's toes.

## When to use it
- You want to kick off a refactoring agent while you keep coding on your main branch
- You're running parallel agents on different features and need full git isolation
- You have a monorepo and want an agent to work on a specific package without checking out the whole thing
- You need an agent to experiment freely without risking your working directory
- You're doing code review and want Claude to try a fix on a separate branch

## How to use it
1. **Launch with worktree**: Run `claude --worktree` to start a session in a new isolated worktree.
2. **Agent config**: Set `isolation: "worktree"` in your agent configuration for agents that should always use worktrees.
3. **Sparse checkout for monorepos**: Configure `worktree.sparsePaths` to only check out the directories the agent needs — huge time saver in large repos.
4. **In-session tools**: Use EnterWorktree and ExitWorktree tools to move between worktrees during a session.
5. **Clean up**: Worktrees are cleaned up automatically when the session ends, or you can manage them with standard `git worktree` commands.

## Pro tips
- Combine worktrees with background agents to run multiple isolated tasks simultaneously — each gets its own branch and working directory
- For monorepos, always set `worktree.sparsePaths` to avoid checking out hundreds of packages your agent doesn't need
- Worktree branches are real git branches, so you can inspect, merge, or cherry-pick from them just like any other branch

## Status history
- **2025-12-15 (v2.1.29)**: Released with worktree isolation, sparse checkout support, and EnterWorktree/ExitWorktree tools
