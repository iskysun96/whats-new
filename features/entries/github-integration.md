---
name: GitHub Integration
category: Workflow & Automation
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Full GitHub workflow support — PRs, issues, reviews, and CI, all from your terminal."
tags: [github, git, pr, issues, ci-cd]
---

## What it does
Claude Code has deep GitHub integration built in. It can create pull requests, respond to review comments, manage issues, trigger CI workflows, and understand your project's git context. It follows your repo's commit conventions automatically, tracks session URLs in commits for traceability, and can even respond to `@claude` mentions directly in PRs. It's like having a teammate who never forgets to link the issue.

## When to use it
- You want to create a well-structured PR with a proper description without leaving the terminal
- You need to respond to or address PR review comments
- You're triaging issues and want Claude to investigate, propose fixes, or close stale ones
- You want to check CI status or re-trigger a failed workflow run
- You're doing a code review and want Claude to summarize changes or flag potential issues

## How to use it
1. **Create a PR**: Just ask Claude to create a PR — it uses `gh pr create` under the hood and writes a meaningful description based on your changes.
2. **Review PR comments**: Use `/pr-comments` to pull in review feedback so Claude can address each comment.
3. **Manage issues**: Ask Claude to list, create, or investigate GitHub issues using `gh` CLI commands.
4. **Check CI**: Ask about CI status — Claude will check workflow runs and help debug failures.
5. **@claude in PRs**: Mention `@claude` in a PR comment on GitHub and Claude can respond with analysis or fixes.

## Pro tips
- Claude tracks session URLs in commits, so you can always trace back to the conversation that produced a change
- When creating PRs, Claude reads your recent commit history to match your team's commit message style — let it draft the PR title too
- Combine with worktrees to have Claude create PRs on separate branches without interrupting your current work

## Status history
- **2025-05-01 (v1.0.0)**: Released with full GitHub CLI integration, PR creation, and issue management
