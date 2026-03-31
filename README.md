# whats-new

The Claude Code team ships features *literally every day*. That's amazing — but also kind of overwhelming.

You hear about a cool new feature on X. You bookmark it. You tell yourself you'll try it later. You forget. A week later you're doing something the hard way and someone mentions, "Oh, you know there's a command for that, right?" Sound familiar?

The problem isn't that the features don't exist — it's the context switching. You're deep in your workflow, focused on your code, and the last thing you want to do is stop everything, open the docs, dig through changelogs, figure out what a feature does, and then try to remember to use it when you're back in your terminal.

**whats-new** fixes this by bringing feature discovery *into* your session. No more context switching. No more digging through docs or hunting down posts. While you're working, you can ask about a feature, get a random recommendation that makes you go "wait, *that* exists?", or let the plugin notice what you're doing and suggest something relevant. The information comes to you — right where you need it, right when you can actually use it.

It's like having a colleague who's read every changelog sitting next to you, ready to tap you on the shoulder at just the right moment.

## Installation

```bash
# From the marketplace
claude plugin install whats-new

# Or from GitHub
claude plugin install github:your-org/whats-new

# Or for local development
claude --plugin-dir ./whats-new
```

## Commands

### `/whats-new:discover [topic]`
Find features relevant to what you're working on.

```
/whats-new:discover refactoring large codebases
/whats-new:discover running tests automatically
/whats-new:discover git workflow
```

### `/whats-new:surprise`
Get a random feature explained in a fun, conversational way. Great for learning something new every day.

### `/whats-new:list [filter]`
Browse all features, optionally filtered by category, tag, or status.

```
/whats-new:list                    # All features
/whats-new:list Multi-Agent        # Filter by category
/whats-new:list agents             # Filter by tag
/whats-new:list public-beta        # Filter by status
```

### `/whats-new:configure [mode]`
Set how aggressively the plugin suggests features.

```
/whats-new:configure passive   # No proactive suggestions
/whats-new:configure medium    # Feature of the day at session start (default)
/whats-new:configure bold      # Proactive suggestions during your session
```

## Notification Modes

| Mode | Session Start | During Session | Manual Commands |
|------|--------------|----------------|-----------------|
| **passive** | Nothing | Nothing | Available |
| **medium** | Feature of the day | Nothing | Available |
| **bold** | Feature of the day | Claude suggests features when relevant | Available |

## Feature Status Tracking

Every feature entry tracks its lifecycle:

- **[GA]** — Generally Available to all users
- **[PUBLIC BETA]** — Available but still in beta
- **[PRIVATE BETA]** — Limited availability
- **[EXPERIMENTAL]** — Early stage, may change
- **[DEPRECATED]** — Being phased out

## Auto-Update Pipeline

A daily GitHub Action keeps the knowledge base current:

1. Fetches the latest CHANGELOG.md from `anthropics/claude-code`
2. Diffs against the last known version
3. Uses Claude Haiku to classify entries as major/minor (~$0.01/run)
4. Generates feature entries for major items using Claude Sonnet
5. Opens a PR for human review

To enable: set the `ANTHROPIC_API_KEY` secret in your fork's GitHub settings.

## Knowledge Base

The plugin ships with 50 curated feature entries across 10 categories:

- **Core Modes** — Auto, Plan, Voice, Bare
- **Multi-Agent** — Subagents, Background Agents, Agent Teams, Custom Agents, Task System
- **Memory & Context** — Sessions, Auto-Memory, Context Management, Extended Thinking
- **Extensibility** — Plugins, Skills, Hooks, Rules, MCP Servers
- **Editor Integration** — VS Code, JetBrains, Desktop, Chrome
- **Developer Tools** — Bash, File Tools, Search, WebFetch, Images, Computer Use, LSP
- **Workflow & Automation** — Loop/Cron, Worktrees, GitHub, Transcripts, Deep Links
- **Customization** — Vim Mode, Themes, Keybindings, Terminal Setup, Prompts, Copy Picker
- **Infrastructure** — Models, Cost Tracking, Diagnostics, Permissions, Auth
- **Enterprise & Cloud** — Bedrock, Vertex AI, Managed Settings, Channels, Remote Control

## Development

```bash
# Test locally
claude --plugin-dir ./whats-new

# Rebuild the feature index after adding/editing entries
bash scripts/build-index.sh

# Validate the plugin
bash scripts/validate.sh
```

## Contributing

1. Fork the repo
2. Add or update feature entries in `features/entries/`
3. Run `bash scripts/build-index.sh` to rebuild the index
4. Run `bash scripts/validate.sh` to check for issues
5. Submit a PR

## License

MIT
