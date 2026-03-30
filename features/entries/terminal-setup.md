---
name: Terminal Setup
category: Customization
introduced_version: "2.1.29"
introduced_date: 2025-12-15
status: ga
ga_version: "2.1.29"
ga_date: 2025-12-15
one_liner: "Optimized configurations for popular terminals so Claude Code looks and works its best."
tags: [terminal, setup, kitty, alacritty, warp, configuration]
---

## What it does
Terminal Setup configures terminal keybindings — particularly Shift+Enter for multiline input — in terminals that don't support it natively. Some terminals like iTerm2, WezTerm, Ghostty, and Kitty already support Shift+Enter out of the box, so this command is only visible in terminals that need manual configuration, like VS Code, Alacritty, Zed, and Warp.

## When to use it
- Shift+Enter isn't working for multiline input in your terminal
- You're using VS Code, Alacritty, Zed, or Warp and need keybinding configuration
- Key combinations like Option+T (toggle thinking) aren't being passed through correctly
- You need to configure Option as Meta key for macOS terminals

## How to use it
1. **Run the setup**: Type `/terminal-setup` inside Claude Code. This command is only visible in terminals that require manual configuration.
2. **Follow the instructions**: Claude configures Shift+Enter and other keybindings for your specific terminal.
3. **Restart your terminal**: Some changes require a terminal restart to take effect.
4. **For macOS Option key shortcuts**: Configure Option as Meta in your terminal settings — iTerm2: Settings > Profiles > Keys > set Left/Right Option key to "Esc+"; Terminal.app: Settings > Profiles > Keyboard > check "Use Option as Meta Key"; VS Code: set `terminal.integrated.macOptionIsMeta` to `true`.

## Pro tips
- If Shift+Enter already works in your terminal (iTerm2, WezTerm, Ghostty, Kitty), you won't see the `/terminal-setup` command — it's hidden when not needed
- You can also use `\` + Enter or `Ctrl+J` for multiline input in any terminal without configuration
- Run `/terminal-setup` again after updating your terminal emulator — new versions sometimes change config formats

## Status history
- **2025-12-15 (v2.1.29)**: Released with keybinding configuration for VS Code, Alacritty, Zed, Warp, and other terminals that need it
