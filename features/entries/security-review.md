---
name: Security Review
category: Developer Tools
introduced_version: "2.1.81"
introduced_date: 2026-02-10
status: ga
ga_version: "2.1.81"
ga_date: 2026-02-10
one_liner: "Analyze pending code changes for security vulnerabilities before you commit."
quick_start: "/security-review"
detection:
  type: keyword
  patterns:
    - "security.*check"
    - "vulnerabilit"
    - "owasp"
    - "xss"
    - "injection"
    - "security.*review"
    - "secure.*code"
  tip: "Run /security-review to analyze your pending changes for security vulnerabilities like XSS, injection, and other OWASP risks."
  signal: keyword
tags: [security, vulnerability, owasp, review, safety]
---

## What it does
The `/security-review` command analyzes your pending code changes for security vulnerabilities. It scans uncommitted changes looking for common security issues — SQL injection, XSS, command injection, insecure authentication patterns, hardcoded secrets, and other OWASP Top 10 risks. Think of it as a security-focused code review that runs before you commit.

## When to use it
- You just wrote code that handles user input and want to check for injection risks
- You're about to commit authentication or authorization changes
- You've added new API endpoints and want to verify they're secure
- You're working with sensitive data (credentials, tokens, PII) and want to catch leaks
- You want a security sanity check before opening a PR

## How to use it
1. Make your code changes as usual
2. Run `/security-review` before committing
3. Review the findings — each issue includes the file, line, risk level, and a suggested fix
4. Address any high or critical findings before committing

## Pro Tips
- Run `/security-review` as a habit before every commit that touches user input, auth, or data handling
- Pair with hooks to automate: set up a `PreToolUse` hook that reminds you to run `/security-review` before `git commit`
- The review is most effective on focused changesets — review after each logical change rather than once after a massive refactor

## Status history
- **2026-02-10 (v2.1.81)**: Released as GA with OWASP Top 10 vulnerability detection for pending changes
