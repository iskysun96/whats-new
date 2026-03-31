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

!`cat "${CLAUDE_PLUGIN_DATA}/config.json" 2>/dev/null || echo '{"mode": "medium"}'`

## Plugin Data Directory: ${CLAUDE_PLUGIN_DATA}

## Instructions

The user wants to configure their notification mode to: $ARGUMENTS

### Available Modes

- **passive** — No proactive suggestions. You're in full control. Use `/whats-new:discover`, `/whats-new:surprise-me`, or `/whats-new:list` whenever you want.
- **medium** (default) — Feature of the day shown when you start a Claude Code session. A gentle nudge to explore something new.
- **bold** — Feature of the day at session start, plus Claude will proactively suggest relevant features during your session when it notices you could benefit from one.

### Actions

If the user provided a valid mode argument (`passive`, `medium`, or `bold`), save the config by writing to the config file. The exact path is shown in "Plugin Data Directory" above — append `/config.json` to it:

```
echo '{"mode": "<MODE>"}' > <PLUGIN_DATA_DIR>/config.json
```

Then confirm the change with a friendly message explaining what they can expect in their next session.

If no argument was provided or the argument is invalid, show the current mode and explain all three options so the user can choose.

**Note**: Changes take effect on the next Claude Code session (restart required).
