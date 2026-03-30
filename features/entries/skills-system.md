---
name: Skills System
category: Extensibility
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Create custom slash commands with markdown files for reusable, shareable workflows."
tags: [skills, commands, slash-commands, customization]
---

## What it does
The Skills System lets you create your own slash commands by writing markdown files with YAML frontmatter. Each skill is a reusable prompt template that can inject dynamic context (like the output of shell commands), use specific tools, and be invoked by you or automatically by Claude when relevant. Think of them as programmable prompt shortcuts that live with your project.

## When to use it
- You have a repetitive workflow (code review, test writing, deployment) you want to standardize
- You want project-specific commands that capture institutional knowledge
- You need to inject live data (git status, test results, API responses) into a prompt
- Your team wants consistent workflows that everyone can use with a simple slash command
- You're building a plugin and want to bundle reusable commands

## How to use it
1. **Create a skill**: Make a `skills/<name>/SKILL.md` file in your `.claude/` directory.
2. **Add frontmatter**: Define metadata in YAML — name, description, whether it's model-invoked or user-invoked.
3. **Write the prompt**: The markdown body becomes the prompt template. Use `` !`command` `` syntax to inject dynamic context from shell commands.
4. **Invoke it**: Run `/<name>` in your session. If marked as model-invoked, Claude may also trigger it automatically when relevant.

```markdown
---
name: test-check
description: Run tests and analyze failures
invoke: user
tools: [Bash, Read]
---

Run the test suite and analyze any failures:

!`npm test 2>&1 | tail -50`

If there are failures, read the failing test files and suggest fixes.
```

## Pro tips
- Use `` !`command` `` for dynamic context — for example, `` !`git diff --cached` `` injects staged changes into the prompt at invocation time
- Mark frequently-needed skills as `invoke: model` so Claude uses them automatically without you having to remember the command
- Keep skills focused on one task — compose multiple skills together in a session rather than building one mega-skill

## Status history
- **2025-05-01 (v1.0.0)**: Released with user-invoked skills and dynamic context injection
- **2025-09-15 (v2.0.0)**: Added model-invoked skills and tool restrictions in frontmatter
