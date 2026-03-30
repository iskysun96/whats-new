---
name: Vertex AI Integration
category: Enterprise & Cloud
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Run Claude Code through Google Cloud Vertex AI with your GCP project billing and credentials."
tags: [gcp, vertex, enterprise, cloud, google]
---

## What it does
Routes all Claude Code API calls through Google Cloud's Vertex AI platform. Your usage gets billed to your GCP project, runs through your organization's GCP security and compliance stack, and uses Application Default Credentials — so if you're already authenticated with `gcloud`, you're basically good to go. Full feature parity with the direct Anthropic API, just running through Google's infrastructure.

## When to use it
- Your organization is a GCP shop and wants all AI usage under Google Cloud billing
- You need Claude Code traffic to flow through your GCP VPC and security controls
- You already have Vertex AI set up for other ML workloads and want to consolidate
- Your compliance team requires all AI API calls to go through a cloud provider's managed service
- You're in a region where Vertex AI has better availability or latency than direct API

## How to use it
1. Authenticate with GCP: run `gcloud auth application-default login`
2. Set `CLAUDE_CODE_USE_VERTEX=1` in your environment
3. Set `CLOUD_ML_REGION` to your preferred region (e.g., `us-east5`)
4. Set `ANTHROPIC_VERTEX_PROJECT_ID` to your GCP project ID
5. Optionally set `ANTHROPIC_MODEL` to a specific model version
6. Start Claude Code normally — all requests route through Vertex AI

## Pro tips
- If you've already run `gcloud auth application-default login`, you don't need any extra credential setup — Vertex integration picks up ADC automatically
- Set the three environment variables in your `.zshrc` or `.bashrc` so you don't have to remember them every time
- Use `/doctor` after setup to verify your Vertex AI connection — it'll catch common issues like wrong project IDs or missing permissions

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA with Vertex AI routing support
- **2025-09-05 (v1.0.101)**: Improved region selection and error messages for quota issues
