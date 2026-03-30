---
name: JetBrains Extension
category: Editor Integration
introduced_version: "2.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "2.0.0"
ga_date: 2025-05-01
one_liner: "Claude Code integrated into IntelliJ, PyCharm, WebStorm, and all other JetBrains IDEs."
quick_start: "Install 'Claude Code' from JetBrains marketplace"
tags: [jetbrains, intellij, pycharm, webstorm, ide]
---

## What it does
This plugin brings Claude Code into the JetBrains ecosystem. Whether you're using IntelliJ IDEA, PyCharm, WebStorm, GoLand, Android Studio, PhpStorm, or other JetBrains IDEs, you get Claude Code integrated into your development environment. It provides interactive diff viewing in the IDE's diff viewer, automatic selection context sharing, file reference shortcuts, and diagnostic sharing. Claude Code runs in the IDE's integrated terminal with these extra IDE integration features active.

## When to use it
- You develop in a JetBrains IDE and want Claude Code without switching to a terminal
- You're working on a Java/Kotlin project in IntelliJ and want AI-assisted refactoring
- You need Claude's help in PyCharm while debugging Python code
- You want to keep your existing JetBrains workflow and key bindings while using Claude
- You're on a team that standardizes on JetBrains tools

## How to use it
1. Open your JetBrains IDE (IntelliJ, PyCharm, WebStorm, etc.).
2. Install the Claude Code plugin from the JetBrains Marketplace (find it at plugins.jetbrains.com or search in Settings > Plugins > Marketplace).
3. Restart the IDE when prompted (you may need to restart completely, sometimes multiple times).
4. Run `claude` from the IDE's integrated terminal — all integration features (diff viewing, selection context, diagnostics) will be active automatically.
5. Alternatively, use Cmd+Esc (Mac) / Ctrl+Esc (Windows/Linux) to launch Claude Code directly, or click the Claude Code button in the UI.

## Pro tips
- The plugin works across all JetBrains IDEs, so if you switch between IntelliJ and PyCharm, you get the same experience everywhere.
- Use Cmd+Option+K (Mac) / Alt+Ctrl+K (Windows/Linux) to insert file references (e.g., @File#L1-99) into your prompt.
- For external terminals, use the `/ide` command inside Claude Code to connect it to your JetBrains IDE and activate all integration features.

## Status history
- **2025-05-01 (v2.0.0)**: Released as generally available with support for all JetBrains IDEs.
