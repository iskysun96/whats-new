---
name: configure
description: Set how aggressively whats-new suggests features. Choose passive, medium, or bold mode.
argument-hint: [passive|medium|bold]
allowed-tools: Bash
user-invocable: true
disable-model-invocation: true
---

# Configure whats-new Notification Mode

## Current Configuration

!`bash "${CLAUDE_PLUGIN_ROOT}/scripts/read-config.sh"`

## Instructions

The user wants to configure their notification mode to: $ARGUMENTS

### Available Modes

- **passive** — No proactive suggestions. You're in full control. Use `/whats-new:discover`, `/whats-new:surprise`, or `/whats-new:list` whenever you want.
- **medium** (default) — Feature of the day shown when you start a Claude Code session. A gentle nudge to explore something new.
- **bold** — Feature of the day at session start, plus Claude will proactively suggest relevant features during your session when it notices you could benefit from one.

### Actions

If the user provided a valid mode argument (`passive`, `medium`, or `bold`), run this command to save it:

```
bash "${CLAUDE_PLUGIN_ROOT}/scripts/set-config.sh" <mode>
```

Then confirm the change with a friendly message explaining what they can expect in their next session.

If no argument was provided or the argument is invalid, show the current mode and explain all three options so the user can choose.

**Note**: Changes take effect on the next Claude Code session (restart required).
