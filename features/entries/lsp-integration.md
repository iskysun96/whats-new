---
name: LSP Integration
category: Developer Tools
introduced_version: "2.1.29"
introduced_date: 2025-09-10
status: ga
ga_version: "2.1.29"
ga_date: 2025-09-10
one_liner: "Language Server Protocol support for go-to-definition, find-references, hover docs, and smarter code navigation."
tags: [lsp, language-server, code-navigation, go-to-definition, references]
---

## What it does
LSP Integration connects Claude to Language Server Protocol servers, giving it the same code intelligence your editor has. Claude can jump to definitions, find all references to a symbol, read hover documentation, and understand type information — all programmatically. Instead of grepping for function names (which can produce false positives), Claude uses real semantic understanding of your code to navigate precisely.

## When to use it
- You want Claude to find all callers of a function before refactoring it
- You need Claude to understand the type signature of a method in a large codebase
- You want Claude to follow the chain of definitions across multiple files accurately
- You're working in a strongly-typed language and want Claude to leverage type information
- You need Claude to understand complex inheritance hierarchies or interface implementations

## How to use it
1. Create a `.lsp.json` file in your project root to configure language servers.
2. Specify which language servers to use — for example:
   - Go: `gopls`
   - TypeScript: `typescript-language-server`
   - Python: `pyright` or `pylsp`
   - Rust: `rust-analyzer`
3. Claude will automatically use the configured LSP servers when navigating your code.
4. No changes needed to how you interact with Claude — it transparently uses LSP for smarter results.

## Pro tips
- LSP makes Claude significantly more accurate in large codebases where grep-based search would return too many false positives. If Claude is struggling to find the right definition, set up LSP.
- The go-to-definition and find-references capabilities are especially powerful for refactoring — Claude can confidently find every usage of a symbol.
- You don't need LSP for every project. For small projects, Grep and Glob work fine. LSP shines in large, complex codebases with deep type hierarchies.

## Status history
- **2025-09-10 (v2.1.29)**: Released as generally available with support for Go (gopls), TypeScript, Python, Rust, and other LSP-compatible language servers.
