# whats-new

A Claude Code plugin that helps you keep up with the latest features. Discover what's available, get feature-of-the-day tips, and find the right feature for your workflow — all without leaving your terminal.

## The Problem

Claude Code ships features fast. Too fast to keep up with. You end up using the same basic features while powerful capabilities go unnoticed. Features get announced on X from various team members, some are in private beta, some are GA — it's hard to track.

## The Solution

**whats-new** lives inside Claude Code and teaches you about features in-context, right when you need them.

## Installation

```bash
# From the official marketplace
claude plugin install whats-new

# Or add the self-hosted marketplace and install
claude plugin marketplace add iskysun96/whats-new
claude plugin install whats-new

# Or install directly from GitHub
claude plugin install github:iskysun96/whats-new

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
