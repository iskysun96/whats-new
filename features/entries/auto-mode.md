---
name: Auto Mode
category: Core Modes
introduced_version: "2.1.86"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.86"
ga_date: 2025-12-15
one_liner: "Claude automatically decides whether to think through a problem or jump straight into action."
quick_start: "claude --permission-mode auto"
detection:
  type: keyword
  patterns:
    - "stop.*asking.*permission"
    - "tired.*of.*approving"
    - "auto.*approve"
    - "too.*many.*confirm"
    - "permission.*annoy"
    - "stop.*prompting.*me"
  tip: "Auto mode uses a background classifier to approve safe actions automatically, so you don't have to click allow on every tool use."
  signal: keyword
tags: [auto, mode, beginner-friendly, productivity]
---

## What it does
Auto Mode is a permission mode where a background classifier (Claude Sonnet) automatically approves or blocks actions without prompting you. Instead of clicking "allow" on every file edit or bash command, the classifier evaluates each action against safety rules and lets safe ones through. You stay in flow while Claude works autonomously.

## When to use it
- You're tired of approving every single tool use and want Claude to just work
- You trust Claude with local file operations but want guardrails against destructive actions
- You're running long tasks where constant permission prompts break your flow
- You want something between "approve everything manually" and "bypass all permissions"
- You're on a Team, Enterprise, or API plan with access to auto mode

## How to use it
1. **From CLI**: Start a session with auto mode:
```bash
claude --permission-mode auto
```
2. **During a session**: Press `Shift+Tab` to cycle through permission modes until you reach "auto".
3. **As your default**: Add to your settings.json:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```
4. Claude now works without prompting. The classifier auto-approves safe actions and blocks risky ones (force pushes, `curl | bash`, mass deletion, production deploys).

## Pro Tips
- Auto mode blocks dangerous patterns by default: code downloads + execution, sending sensitive data externally, force pushes to main, and mass cloud storage deletion. You can customize these rules.
- If the classifier blocks the same action 3+ times in a row, auto mode pauses and falls back to manual prompts until you explicitly approve — so you always stay in control.
- Requires Claude Sonnet 4.6 or Opus 4.6. Not available on Haiku or older models.

## Status history
- **2025-12-15 (v2.1.86)**: Released as GA. Background classifier for autonomous permission decisions.
