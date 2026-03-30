---
name: Plugin System
category: Extensibility
introduced_version: "2.0.12"
introduced_date: 2025-10-01
status: ga
ga_version: "2.0.12"
ga_date: 2025-10-01
one_liner: "Install community plugins that add skills, hooks, MCP servers, agents, and more."
tags: [plugins, marketplace, extensions, community]
---

## What it does
The Plugin System lets you extend Claude Code with community-built (or your own) plugins. Plugins can bundle skills, hooks, MCP servers, agents, and configuration into a single installable package. Browse the marketplace to find plugins for common workflows, or create your own and share them with your team or the community.

## When to use it
- You want to add a specialized workflow (e.g., a deploy plugin, a PR review plugin) without building it from scratch
- Your team has shared conventions and you want to distribute them as a single installable package
- You've built a useful set of skills and hooks and want to share them with the community
- You're evaluating third-party integrations and want a quick way to try them out
- You want to keep your Claude Code setup reproducible across machines

## How to use it
1. **Browse plugins**: Run `claude plugin list` to see available plugins, or browse the marketplace.
2. **Install a plugin**: Run `/plugin install <name>` to install a plugin from the registry.
3. **Local development**: Use `--plugin-dir <path>` to load a plugin from a local directory during development.
4. **Create your own**: Structure your plugin with a `plugin.json` manifest, then add skills, hooks, or MCP configs as needed.
5. **Uninstall**: Run `/plugin uninstall <name>` to remove a plugin you no longer need.

## Pro tips
- Pin plugin versions in your project config so your whole team uses the same version
- Use `--plugin-dir` during development to iterate quickly without publishing — changes are picked up on next session start
- Check a plugin's source before installing — plugins can run hooks and shell commands, so review what you're adding to your workflow

## Status history
- **2025-10-01 (v2.0.12)**: Released with plugin install, list, and local development support
