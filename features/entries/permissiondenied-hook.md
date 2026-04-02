---
name: PermissionDenied Hook
category: Extensibility
introduced_version: "2.1.89"
introduced_date: 2026-04-02
status: ga
ga_version: "2.1.89"
ga_date: 2026-04-02
one_liner: "Intercept auto mode classifier denials and programmatically decide whether the model should retry the operation"
tags: [permission-denied, hooks, auto-mode, classifier, retry, extensibility]
---

## What it does
The PermissionDenied hook fires whenever Claude's auto mode classifier denies an operation, giving you a chance to intervene before the model gives up. You can inspect the denial reason and return `{retry: true}` to tell Claude to try again, or let the denial stand by returning nothing or `{retry: false}`.

## When to use it
- Override overly cautious auto mode restrictions for trusted workflows
- Log permission denials for compliance or debugging purposes
- Implement custom authorization logic that's more context-aware than the default classifier
- Provide user prompts to confirm sensitive operations before retrying
- Build approval workflows where humans can review and approve denied operations

## How to use it
1. Register your hook function in your Claude configuration
2. Implement the handler: `function onPermissionDenied(context) { /* your logic */ }`
3. Access the denial details via `context.operation`, `context.reason`, and `context.resource`
4. Return `{retry: true}` to retry the operation, or return nothing to maintain the denial
5. Optionally include `{retry: true, message: "Custom reason"}` to provide context for the retry

## Pro tips
- Use sparingly — the auto mode classifier exists for good security reasons
- Log all permission overrides for audit trails, especially in production environments
- Consider implementing rate limiting to prevent infinite retry loops if your logic is faulty

## Status history
- **2026-04-02 (v2.1.89)**: Introduced as generally available
