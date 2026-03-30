---
name: Plugin System
category: Extensibility
introduced_version: "2.0.12"
introduced_date: 2025-10-01
status: ga
ga_version: "2.0.12"
ga_date: 2025-10-01
one_liner: "Install community plugins that add skills, hooks, MCP servers, agents, and more."
quick_start: "/plugin"
detection:
  type: keyword
  patterns:
    - "install.*tool"
    - "add.*integration"
    - "connect.*to.*(slack|jira|figma)"
    - "browse.*plugin"
  tip: "Browse and install community plugins with /plugin. Plugins add skills, hooks, MCP servers, and more."
  signal: keyword
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
1. **Browse plugins**: Run `/plugin` to open the plugin manager. It has four tabs: **Discover** (browse available plugins from your marketplaces), **Installed** (manage installed plugins), **Marketplaces** (add/remove marketplaces), and **Errors** (view loading errors).
2. **Install a plugin**: Run `/plugin install <name>@<marketplace-name>` to install a plugin from a marketplace. For example, `/plugin install github@claude-plugins-official`.
3. **Local development**: Use `--plugin-dir <path>` when launching Claude Code to load a plugin from a local directory during development. Run `/reload-plugins` to pick up changes without restarting.
4. **Create your own**: Structure your plugin with a `.claude-plugin/plugin.json` manifest, then add skills, hooks, agents, or MCP configs in directories at the plugin root.
5. **Uninstall**: Run `/plugin uninstall <name>@<marketplace-name>` to remove a plugin you no longer need.

## Pro tips
- Pin plugin versions in your project config so your whole team uses the same version
- Use `--plugin-dir` during development to iterate quickly without publishing — run `/reload-plugins` to pick up changes without restarting
- Check a plugin's source before installing — plugins can run hooks and shell commands, so review what you're adding to your workflow
- Plugin skills are namespaced (e.g., `/my-plugin:hello`) to prevent conflicts between plugins with the same skill names

## Status history
- **2025-10-01 (v2.0.12)**: Released with plugin install, list, and local development support
