---
name: configure
description: Set how aggressively whats-new suggests features. Choose introvert, coworker, or that-friend mode.
argument-hint: [introvert|coworker|that-friend]
allowed-tools: Bash
user-invocable: true
disable-model-invocation: true
---

# Configure whats-new Notification Mode

## Current Configuration

!`cat "${CLAUDE_PLUGIN_DATA}/config.json" 2>/dev/null || echo '{"mode": "coworker"}'`

## Plugin Data Directory: ${CLAUDE_PLUGIN_DATA}

## Instructions

The user wants to configure their notification mode to: $ARGUMENTS

### Available Modes

- **introvert** — You do your thing, it does its thing. No unsolicited advice. Use `/whats-new:discover`, `/whats-new:surprise`, or `/whats-new:list` whenever you want.
- **coworker** (default) — Drops a feature tip when you start your day. Friendly, not clingy.
- **that-friend** — "Oh you're doing THAT? Let me tell you about..." Can't help itself. **(beta)**

### Actions

If the user provided a valid mode argument (`introvert`, `coworker`, or `that-friend`), save the config by writing to the config file. The exact path is shown in "Plugin Data Directory" above — append `/config.json` to it:

```
echo '{"mode": "<MODE>"}' > <PLUGIN_DATA_DIR>/config.json
```

Then confirm the change with a friendly message explaining what they can expect in their next session.

If no argument was provided or the argument is invalid, show the current mode and explain all three options so the user can choose.

**Note**: Changes take effect on the next Claude Code session (restart required).
