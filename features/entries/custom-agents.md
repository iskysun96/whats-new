---
name: Custom Agent Definitions
category: Multi-Agent
introduced_version: "1.0.64"
introduced_date: 2025-07-29
status: ga
ga_version: "1.0.64"
ga_date: 2025-07-29
one_liner: "Define your own specialized agents with specific models, tools, system prompts, and constraints."
quick_start: "Create .claude/agents/my-agent.md"
tags: [agents, customization, definitions, reusable]
---

## What it does
Custom Agent Definitions let you create reusable agent archetypes tailored to your workflow. Instead of re-explaining what you want every time, you define an agent once -- its model, allowed tools, system prompt, constraints -- and invoke it by name. Think of it like creating specialized roles on your team: a "code-reviewer" agent, a "docs-writer" agent, a "security-auditor" agent, each preconfigured to do their job well.

## When to use it
- You have a recurring workflow (e.g., PR review, docs generation) and want a consistent agent personality for it
- You want to restrict an agent to specific tools for safety (e.g., a read-only explorer that can't write files)
- You're building agent teams and need to define the individual roles
- You want different agents to use different models (e.g., a fast model for exploration, a powerful model for complex reasoning)
- You're sharing agent configurations across a team via version control

## How to use it
Create a markdown file with YAML frontmatter in one of these locations:

**Project-level agents** (shared with your team via git):
```
.claude/agents/code-reviewer.md
```

**User-level agents** (personal, available across all projects):
```
~/.claude/agents/security-auditor.md
```

**Agent definition format:**

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer. Focus on:
- Logic errors and edge cases
- Security vulnerabilities
- Performance concerns
- Code clarity and maintainability

Be direct and specific. Reference line numbers. Suggest fixes, don't just point out problems.
```

Only `name` and `description` are required. Other supported frontmatter fields include: `tools`, `disallowedTools`, `model` (aliases like `sonnet`/`opus`/`haiku`, full model IDs, or `inherit`), `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, and `initialPrompt`.

**Using your custom agent:**

```bash
# Run a whole session as this agent
claude --agent code-reviewer

# Or reference in conversations
"Use the code-reviewer agent to check my latest changes"

# Or @-mention in the prompt to guarantee it runs
@"code-reviewer (agent)" look at the auth changes
```

You can also manage agents interactively with the `/agents` command, which lets you create, edit, and delete agents. To list all configured agents from the command line, run `claude agents`.

The body of the markdown file becomes the agent's system prompt. The YAML frontmatter configures its capabilities.

## Pro tips
- Use the `tools` field (or `disallowedTools` to deny specific tools) to enforce least-privilege -- a reviewer agent probably shouldn't need write access
- Store project-specific agents in `.claude/agents/` and commit them to your repo so the whole team benefits
- You can reference custom agents in agent team configurations, making them building blocks for more complex workflows

## Status history
- **2025-07-29 (v1.0.64)**: Released as GA -- custom agent definitions via markdown files with YAML frontmatter
