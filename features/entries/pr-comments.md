---
name: PR Comments
category: Workflow & Automation
introduced_version: "2.1.59"
introduced_date: 2025-12-01
status: ga
ga_version: "2.1.59"
ga_date: 2025-12-01
one_liner: "Fetch and display GitHub PR comments so you can address review feedback without leaving your session."
quick_start: "/pr-comments"
detection:
  type: keyword
  patterns:
    - "pr.*comment"
    - "review.*comment"
    - "pull.*request.*feedback"
    - "pr.*review"
    - "address.*review"
  tip: "Use /pr-comments to fetch GitHub PR comments and address review feedback right from your session."
  signal: keyword
tags: [pr, comments, review, github, feedback]
---

## What it does
The `/pr-comments` command fetches comments from a GitHub pull request and displays them in your session. Instead of switching between your terminal and GitHub's web UI to read review feedback, you can pull all the comments into Claude Code, read them in context, and immediately start addressing them.

## When to use it
- A reviewer left comments on your PR and you want to work through them
- You want Claude to help you address specific review feedback
- You're on a branch and want to see what feedback your PR has received
- You prefer working in the terminal over the GitHub web UI for code reviews

## How to use it
1. **Current branch PR**: Run `/pr-comments` to fetch comments for the PR associated with your current branch
2. **Specific PR**: Run `/pr-comments 123` to fetch comments from PR #123
3. Review the comments displayed in your session
4. Ask Claude to help address specific feedback — the comments are now in context

## Pro Tips
- After addressing comments, use `/diff` to review your changes before pushing
- Combine with `claude --from-pr 123` to resume a session that's already linked to a specific PR
- The colored PR link in the footer of your session shows the PR review status at a glance

## Status history
- **2025-12-01 (v2.1.59)**: Released as GA with PR comment fetching and display
