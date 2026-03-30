---
name: Authentication & OAuth
category: Infrastructure
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Flexible authentication with OAuth, API keys, dynamic key refresh, and keychain integration."
tags: [auth, oauth, api-key, login, security]
---

## What it does
Handles how you authenticate with the Anthropic API, and it's more flexible than you'd expect. You can do browser-based OAuth for the smoothest experience, set an API key via environment variable for headless setups, or use a helper script that dynamically refreshes your key. Credentials are stored securely in your system keychain, not in plain text config files.

## When to use it
- You're setting up Claude Code for the first time and need to authenticate
- You're running Claude Code in CI/CD and can't do browser-based login
- Your organization rotates API keys and you need automatic refresh
- You're switching between personal and work Anthropic accounts
- You want to verify your auth is working correctly after a credential change

## How to use it
1. Run `claude` for the first time and follow the interactive OAuth flow — it opens your default browser and handles authentication
2. Set `ANTHROPIC_API_KEY` environment variable for direct API key auth (useful for CI/CD and headless environments)
3. For dynamic key refresh, set `apiKeyHelper` in settings to a command that outputs a fresh key — Claude Code calls it to refresh credentials automatically
4. Run `claude logout` to clear stored credentials
5. Use `/login` within a session to re-authenticate if needed

## Pro tips
- The `apiKeyHelper` approach is clutch for enterprise setups where keys rotate — point it to a script that fetches from your secrets manager and Claude Code handles the rest
- Keychain integration means your credentials survive terminal restarts without re-authenticating
- If you're hitting auth issues, run `claude doctor` first — it checks your auth configuration as part of its system health check

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA with OAuth and API key authentication
- **2025-09-01 (v1.0.100)**: Added dynamic key refresh with apiKeyHelper
- **2025-10-20 (v1.0.112)**: Added keychain integration for secure credential storage
