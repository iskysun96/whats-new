---
name: Bedrock Integration
category: Enterprise & Cloud
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Run Claude Code through AWS Bedrock using your organization's AWS credentials and billing."
tags: [aws, bedrock, enterprise, cloud, deployment]
---

## What it does
Lets you route all Claude Code API calls through AWS Bedrock instead of hitting the Anthropic API directly. This means usage goes through your organization's AWS account, billing, and compliance infrastructure. You get full feature parity — everything that works with the direct API works through Bedrock. It also supports cross-region inference, so you can hit whichever AWS region gives you the best latency.

## When to use it
- Your organization requires all AI API calls to go through AWS for compliance or billing reasons
- You already have AWS Bedrock set up and want to consolidate usage under one billing umbrella
- You need to use Claude Code in an environment that can't reach the Anthropic API directly
- Your IT policy requires traffic to stay within AWS infrastructure
- You want to leverage existing AWS IAM roles and policies for access control

## How to use it
1. Ensure you have AWS credentials configured (`aws configure` or environment variables)
2. Set `CLAUDE_CODE_USE_BEDROCK=1` in your environment
3. Set `ANTHROPIC_MODEL` to the Bedrock model ID you want to use (e.g., `us.anthropic.claude-sonnet-4-20250514-v1:0`)
4. Optionally set `AWS_REGION` for your preferred region
5. Start Claude Code normally — it will automatically route through Bedrock
6. Verify with `claude doctor` that the Bedrock connection is healthy

## Pro tips
- Cross-region inference prefixes (like `us.` in the model ID) let you use models that might not be available in your default region
- If you're getting throttled, check your Bedrock service quotas in the AWS console — the defaults can be conservative
- You can set the environment variables in your shell profile so Bedrock mode is always on, then override with `CLAUDE_CODE_USE_BEDROCK=0` when you want direct API access

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA with Bedrock routing support
- **2025-08-20 (v1.0.97)**: Added cross-region inference support
