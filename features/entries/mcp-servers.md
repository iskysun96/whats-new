---
name: MCP Servers
category: Extensibility
introduced_version: "1.0.0"
introduced_date: 2025-05-01
status: ga
ga_version: "1.0.0"
ga_date: 2025-05-01
one_liner: "Connect Claude to external tools and data sources via the Model Context Protocol."
tags: [mcp, integrations, tools, protocol, external]
---

## What it does
MCP Servers let you plug Claude into external tools, APIs, and data sources using the Model Context Protocol. Want Claude to query your database, interact with GitHub, call internal APIs, or use any custom tool? Add an MCP server and Claude gets new capabilities instantly. Servers can run locally via stdio or remotely over HTTP, and OAuth support means you can connect to authenticated services securely.

## When to use it
- You want Claude to interact with GitHub (create PRs, review issues, manage repos) directly
- You need Claude to query a database or internal API during your session
- You're building a custom tool integration that doesn't exist as a built-in
- You want to connect Claude to third-party services (Jira, Linear, Sentry, etc.)
- You need Claude to access private data sources that require authentication

## How to use it
1. **Add a stdio server**: Run `claude mcp add --transport stdio <name> -- <command> [args...]` for local tool servers. All options (`--transport`, `--env`, `--scope`) must come before the server name.
2. **Add an HTTP server**: Run `claude mcp add --transport http <name> <url>` for remote/cloud-hosted servers (recommended for remote MCP).
3. **Add an SSE server**: Run `claude mcp add --transport sse <name> <url>` for SSE-based remote servers (deprecated in favor of HTTP).
4. **Configure in file**: Add server definitions to `.mcp.json` in your project root (with `--scope project`) for shared team configs.
5. **OAuth servers**: For authenticated services, use `/mcp` inside a session to authenticate with servers that require OAuth 2.0.
6. **List servers**: Run `claude mcp list` to see all configured MCP servers, or use `/mcp` inside a session to check status.

```json
// .mcp.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```

## Pro tips
- Commit your `.mcp.json` to version control (minus secrets) so your whole team gets the same tool integrations. Use `--scope project` when adding servers to write to `.mcp.json`
- Use environment variable references (`${VAR}`) in MCP configs to keep secrets out of your config files. Pass env vars with `--env KEY=value` when adding servers via CLI
- Use the `--scope` flag to control where configs are stored: `local` (default, private to you in current project), `project` (shared via `.mcp.json`), or `user` (available across all projects)
- Configure MCP server startup timeout using the `MCP_TIMEOUT` environment variable (e.g., `MCP_TIMEOUT=10000 claude` for 10 seconds)

## Status history
- **2025-05-01 (v1.0.0)**: Released with stdio transport and basic MCP server support
- **2025-09-15 (v2.0.0)**: Added HTTP transport and OAuth support for authenticated servers
- **2025-12-01 (v2.1.0)**: Added `claude mcp add` CLI command for easier server registration
