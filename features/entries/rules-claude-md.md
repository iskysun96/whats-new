---
name: Rules (CLAUDE.md)
category: Extensibility
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Customize Claude's behavior with markdown instruction files loaded into every session."
quick_start: "/init"
tags: [rules, instructions, claude-md, configuration, team]
---

## What it does
Rules let you shape how Claude behaves in your project by writing plain markdown instruction files. You can set project-level rules (shared with your team), user-level rules (your personal preferences), and directory-level rules (different conventions for different parts of the codebase). These files are automatically loaded into every session, so Claude always knows the ground rules without you having to repeat them.

## When to use it
- Your project has coding conventions (naming, architecture, testing) that Claude should follow
- You want consistent Claude behavior across your whole team
- Different parts of your monorepo follow different conventions
- You have personal preferences (response style, tool usage) you want applied everywhere
- You're onboarding new team members and want Claude to guide them according to project norms

## How to use it
1. **Project rules**: Create `CLAUDE.md` or `.claude/CLAUDE.md` in your project root. These rules are shared with everyone on the project via version control.
2. **Personal rules**: Create `~/.claude/CLAUDE.md` for preferences that follow you across all projects.
3. **Directory rules**: Place `CLAUDE.md` files in subdirectories — they load on demand when Claude reads files in those directories. Claude Code also walks up the directory tree from your working directory, loading CLAUDE.md files at each level.
4. **Modular rules**: Use `.claude/rules/*.md` to split rules into focused, topic-specific files. Files without a `paths` frontmatter field are loaded unconditionally at launch. Add `paths` frontmatter with glob patterns to scope rules to specific file types (e.g., `paths: ["src/api/**/*.ts"]`).
5. **Personal modular rules**: Use `~/.claude/rules/*.md` for personal rules that apply across all projects.

```markdown
# Project Rules

## Code Style
- Use TypeScript for all new files
- Prefer named exports over default exports
- Write tests for all public functions

## Architecture
- Follow the repository pattern for data access
- Keep business logic out of route handlers
- Use dependency injection for external services

## Communication
- Explain trade-offs when suggesting architectural changes
- Ask before deleting or significantly refactoring existing code
```

## Pro tips
- Use `.claude/rules/*.md` for modular rules — one file per concern (e.g., `testing.md`, `architecture.md`, `style.md`) keeps things maintainable. Rules files are discovered recursively, so you can organize them into subdirectories
- Commit your project-level `CLAUDE.md` to version control so the whole team benefits and rules evolve with code review
- Be specific and actionable in your rules — "use descriptive variable names" is vague, "use camelCase for variables, PascalCase for types" is something Claude can actually follow
- Target under 200 lines per CLAUDE.md file — longer files consume more context and reduce adherence. Use `@path/to/import` syntax to import additional files
- Run `/init` to auto-generate a starting CLAUDE.md. Use `/memory` to see which CLAUDE.md and rules files are loaded in your session

## Status history
- **2025-05-01 (v1.0.0)**: Released with project-level and user-level CLAUDE.md support
- **2025-09-15 (v2.0.0)**: Added `.claude/rules/` directory for modular rule files
