---
name: Worktrees
category: Workflow & Automation
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Run agents in isolated git worktrees so they never block your main branch."
quick_start: "claude --worktree"
detection:
  type: many_files
  threshold: 8
  tip: "Claude just edited {files} different files ({file_list}). Worktrees let agents work in isolated git branches so changes don't interfere with your main work."
  signal: behavioral
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
1. **Launch with worktree**: Run `claude --worktree feature-auth` (or `claude -w feature-auth`) to start a session in a new isolated worktree. Omit the name and Claude generates a random one automatically.
2. **Subagent config**: Set `isolation: worktree` in a subagent's frontmatter for agents that should always use worktrees. Each subagent gets its own worktree that is automatically cleaned up if it makes no changes.
3. **Sparse checkout for monorepos**: Configure `worktree.sparsePaths` in settings to only check out the directories the agent needs — huge time saver in large repos.
4. **In-session**: You can also ask Claude to "work in a worktree" or "start a worktree" during a session, and it will create one automatically.
5. **Clean up**: When you exit, if there are no changes the worktree and branch are removed automatically. If changes or commits exist, Claude prompts you to keep or remove the worktree.

## Pro Tips
- Combine worktrees with background agents to run multiple isolated tasks simultaneously — each gets its own branch and working directory
- For monorepos, set `worktree.sparsePaths` in settings and use `worktree.symlinkDirectories` (e.g., `["node_modules"]`) to avoid duplicating large directories
- Worktree branches are named `worktree-<name>` and branch from `origin/HEAD`. They're real git branches, so you can inspect, merge, or cherry-pick from them
- Add `.claude/worktrees/` to your `.gitignore` to prevent worktree contents from appearing as untracked files
- Use a `.worktreeinclude` file in your project root to copy gitignored files like `.env` into new worktrees automatically

## Status history
- **2025-12-15 (v2.1.29)**: Released with worktree isolation, sparse checkout support, and subagent worktree integration
