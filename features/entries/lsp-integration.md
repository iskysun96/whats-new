---
name: LSP Integration
category: Developer Tools
introduced_version: "2.1.29"
introduced_date: 2025-09-10
status: ga
ga_version: "2.1.29"
ga_date: 2025-09-10
one_liner: "Language Server Protocol support for go-to-definition, find-references, hover docs, and smarter code navigation."
quick_start: "/plugin install typescript@anthropic"
tags: [lsp, language-server, code-navigation, go-to-definition, references]
---

## What it does
LSP Integration connects Claude to Language Server Protocol servers via code intelligence plugins, giving it the same code intelligence your editor has. After every file edit, the language server automatically reports errors and warnings back to Claude, so it catches type errors, missing imports, and syntax issues without running a compiler. Claude can also jump to definitions, find all references to a symbol, get type info, list symbols, find implementations, and trace call hierarchies — all programmatically with more precision than grep-based search.

## When to use it
- You want Claude to find all callers of a function before refactoring it
- You need Claude to understand the type signature of a method in a large codebase
- You want Claude to follow the chain of definitions across multiple files accurately
- You're working in a strongly-typed language and want Claude to leverage type information
- You need Claude to understand complex inheritance hierarchies or interface implementations

## How to use it
1. Install a code intelligence plugin from the official Anthropic marketplace using `/plugin install <name>@claude-plugins-official` (e.g., `/plugin install typescript-lsp@claude-plugins-official`). Available plugins include:
   - Go: `gopls-lsp` (requires `gopls`)
   - TypeScript: `typescript-lsp` (requires `typescript-language-server`)
   - Python: `pyright-lsp` (requires `pyright-langserver`)
   - Rust: `rust-analyzer-lsp` (requires `rust-analyzer`)
   - C/C++: `clangd-lsp`, C#: `csharp-lsp`, Java: `jdtls-lsp`, Kotlin: `kotlin-lsp`, Lua: `lua-lsp`, PHP: `php-lsp`, Swift: `swift-lsp`
2. Ensure the required language server binary is installed on your system and available in your `$PATH`.
3. Run `/reload-plugins` to activate the plugin. Claude will automatically use the configured LSP server for diagnostics after edits and for code navigation.
4. No changes needed to how you interact with Claude — it transparently uses LSP for smarter results.

## Pro Tips
- LSP makes Claude significantly more accurate in large codebases where grep-based search would return too many false positives. If Claude is struggling to find the right definition, install the appropriate code intelligence plugin.
- The automatic diagnostics feature is especially valuable — Claude sees type errors immediately after making an edit and can fix them in the same turn, without needing to run a compiler.
- You don't need LSP for every project. For small projects, Grep and Glob work fine. LSP shines in large, complex codebases with deep type hierarchies. You can also create your own LSP plugin for languages not in the official marketplace.

## Status history
- **2025-09-10 (v2.1.29)**: Released as generally available with support for Go (gopls), TypeScript, Python, Rust, and other LSP-compatible language servers.
