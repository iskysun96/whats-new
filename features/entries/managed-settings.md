---
name: Managed Settings (Enterprise)
category: Enterprise & Cloud
introduced_version: "2.1.83"
introduced_date: 2025-12-18
status: ga
ga_version: "2.1.83"
ga_date: 2025-12-18
one_liner: "Organization-wide policy configuration for controlling permissions, tools, models, and behaviors across all users."
tags: [enterprise, managed, policy, admin, organization]
---

## What it does
Gives admins a way to set and enforce policies across every Claude Code installation in their organization. You define rules in a `managed-settings.json` file — which models are allowed, what tools can be used, permission defaults, and behavioral constraints. There's also a `managed-settings.d/` directory for modular drop-in configs, so different teams can have different policies without one giant file. Server-managed settings let you push config changes centrally without touching individual machines.

## When to use it
- You're an admin rolling out Claude Code to a team and need consistent guardrails
- You want to restrict which models developers can use (e.g., only Sonnet for cost control)
- Your security team requires specific tools to be blocked or specific permission modes to be enforced
- You need different policies for different teams — frontend gets one config, backend gets another
- You want to push policy updates to all users without asking them to change anything locally

## How to use it
1. Create a `managed-settings.json` file in the managed settings directory (location depends on your OS and deployment)
2. Define your policies — allowed models, tool restrictions, permission defaults, etc.
3. For modular configs, create files in `managed-settings.d/` — they merge automatically
4. For centralized control, configure server-managed settings in your deployment infrastructure
5. Users will see managed policies reflected in their `/settings` view, marked as organization-managed and non-overridable
6. Test with a single user before rolling out to the whole org

## Pro tips
- The `managed-settings.d/` drop-in directory is great for layering: put security policies in one file, model restrictions in another, and team-specific overrides in a third
- Server-managed settings are the way to go for large orgs — you push once and every Claude Code instance picks it up on next restart
- Users can still set their own preferences for anything you haven't explicitly locked down, so you don't have to manage everything centrally

## Status history
- **2025-12-18 (v2.1.83)**: Released as GA with managed-settings.json and drop-in directory support
- **2026-01-15 (v2.1.90)**: Added server-managed settings for centralized policy distribution
