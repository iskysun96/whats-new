---
name: list
description: Browse and filter all Claude Code features by category, tag, or status. See what's available at a glance.
argument-hint: [category, tag, or status filter]
allowed-tools: Read, Bash
user-invocable: true
disable-model-invocation: true
---

# Browse Claude Code Features

You are presenting the user with a browsable catalog of Claude Code features.

## Feature Listing

!`bash "${CLAUDE_PLUGIN_ROOT}/scripts/list-features.sh" "$0"`

## Instructions

1. Present the feature listing above in a clean, well-formatted way.
2. If the user provided a filter argument, acknowledge what you filtered by.
3. If no filter was provided, you're showing all features grouped by category.
4. Each feature shows a status badge:
   - **[GA]** = Generally Available to all users
   - **[PUBLIC BETA]** = Available but still in beta
   - **[PRIVATE BETA]** = Limited availability
   - **[EXPERIMENTAL]** = Early stage, may change
   - **[DEPRECATED]** = Being phased out
5. After the listing, add helpful navigation tips:
   - "Filter by category: `/whats-new:list Multi-Agent`"
   - "Filter by tag: `/whats-new:list agents`"
   - "Filter by status: `/whats-new:list public-beta`"
   - "Deep dive into a feature: `/whats-new:discover [feature name]`"
   - "Random feature: `/whats-new:surprise-me`"
6. Keep formatting consistent and scannable.
