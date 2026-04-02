---
name: Auto Mode Permission Management UI
category: Auto Mode
introduced_version: "2.1.89"
introduced_date: 2026-04-02
status: ga
ga_version: "2.1.89"
ga_date: 2026-04-02
one_liner: "Get visual feedback when Auto Mode commands are denied and easily retry them from a dedicated permissions interface"
tags: [auto-mode, permissions, notifications, retry, ui-management]
---

## What it does
When Claude's Auto Mode encounters a command that requires permission, you'll now see a clear notification explaining what was blocked. All denied commands are automatically logged in a new "Recent" tab under `/permissions`, where you can review what happened and retry any command with a simple `r` keystroke.

## When to use it
- When Auto Mode hits permission boundaries and you want to understand what was blocked
- To review recent permission denials and decide which ones to approve
- When you want to quickly retry a command that was previously denied
- To audit Auto Mode's permission requests over time
- When debugging why certain automated workflows aren't completing

## How to use it
1. Run Auto Mode and let it work until you see a permission denial notification
2. Type `/permissions` to open the permissions interface
3. Navigate to the "Recent" tab to see all recently denied commands
4. Review the command details and context
5. Press `r` next to any command to retry it with permission granted

## Pro tips
- Check the Recent tab periodically to catch commands you might have missed approving
- Use the notification details to understand why certain commands need permission before retrying

## Status history
- **2026-04-02 (v2.1.89)**: Introduced as generally available
