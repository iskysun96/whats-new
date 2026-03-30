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
1. **Add a server**: Run `claude mcp add <name> -- <command>` to register a new MCP server.
2. **Configure in file**: Add server definitions to `.mcp.json` in your project root for shared team configs.
3. **Choose transport**: Use stdio for local tool servers or HTTP for remote/cloud-hosted servers.
4. **OAuth servers**: For authenticated services, Claude handles the OAuth flow — just add the server and follow the auth prompts.
5. **List servers**: Run `claude mcp list` to see all configured MCP servers and their status.

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
- Commit your `.mcp.json` to version control (minus secrets) so your whole team gets the same tool integrations
- Use environment variable references (`${VAR}`) in MCP configs to keep secrets out of your config files
- If an MCP server is slow to start, it won't block your session — Claude will use it once it's ready and fall back to built-in tools in the meantime

## Status history
- **2025-05-01 (v1.0.0)**: Released with stdio transport and basic MCP server support
- **2025-09-15 (v2.0.0)**: Added HTTP transport and OAuth support for authenticated servers
- **2025-12-01 (v2.1.0)**: Added `claude mcp add` CLI command for easier server registration
