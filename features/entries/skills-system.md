---
name: Skills System
category: Extensibility
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Create custom slash commands with markdown files for reusable, shareable workflows."
quick_start: "Create .claude/skills/my-skill/SKILL.md"
detection:
  type: keyword
  patterns:
    - "custom.*slash.*command"
    - "create.*my.*own.*command"
    - "add.*command"
    - "make.*a.*slash.*command"
  tip: "You can create custom slash commands by adding SKILL.md files in .claude/skills/. Each skill gets its own /command."
  signal: keyword
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
1. **Create a skill**: Make a `.claude/skills/<name>/SKILL.md` file in your project, or `~/.claude/skills/<name>/SKILL.md` for personal skills available across all projects.
2. **Add frontmatter**: Define metadata in YAML — `name`, `description`, `disable-model-invocation`, `allowed-tools`, and more.
3. **Write the prompt**: The markdown body becomes the prompt template. Use `` !`command` `` syntax to inject dynamic context from shell commands.
4. **Invoke it**: Run `/<name>` in your session. By default, Claude may also trigger skills automatically when relevant. Set `disable-model-invocation: true` to require manual invocation.

```markdown
---
name: test-check
description: Run tests and analyze failures
disable-model-invocation: true
allowed-tools: Bash, Read
---

Run the test suite and analyze any failures:

!`npm test 2>&1 | tail -50`

If there are failures, read the failing test files and suggest fixes.
```

## Pro tips
- Use `` !`command` `` for dynamic context — for example, `` !`git diff --cached` `` injects staged changes into the prompt at invocation time
- Leave `disable-model-invocation` at its default (`false`) for frequently-needed skills so Claude uses them automatically without you having to remember the command. Set `disable-model-invocation: true` for workflows with side effects like deploy or commit
- Set `user-invocable: false` for background knowledge skills that Claude should use automatically but users shouldn't invoke directly
- Keep skills focused on one task — compose multiple skills together in a session rather than building one mega-skill
- Use `context: fork` in frontmatter to run a skill in an isolated subagent context

## Status history
- **2025-05-01 (v1.0.0)**: Released with user-invoked skills and dynamic context injection
- **2025-09-15 (v2.0.0)**: Added model-invoked skills and tool restrictions in frontmatter
