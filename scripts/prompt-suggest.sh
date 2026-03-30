#!/usr/bin/env bash
set -euo pipefail

# Capture stdin immediately before anything else consumes it
INPUT=$(cat)

DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"

# Need plugin data dir
if [[ -z "$DATA_DIR" ]]; then
  exit 0
fi

# Only run in bold mode
CONFIG_FILE="${DATA_DIR}/config.json"
MODE="medium"
if [[ -f "$CONFIG_FILE" ]]; then
  MODE=$(python3 -c "
import json
with open('$CONFIG_FILE') as f:
    print(json.load(f).get('mode', 'medium'))
" 2>/dev/null || echo "medium")
fi

if [[ "$MODE" != "bold" ]]; then
  exit 0
fi

# Throttle: only suggest every 4th prompt
COUNTER_FILE="${DATA_DIR}/suggest-counter.txt"
COUNTER=0
if [[ -f "$COUNTER_FILE" ]]; then
  COUNTER=$(cat "$COUNTER_FILE" 2>/dev/null || echo "0")
fi
COUNTER=$((COUNTER + 1))
echo "$COUNTER" > "$COUNTER_FILE"

if (( COUNTER % 4 != 0 )); then
  exit 0
fi

# Python handles keyword matching and JSON output
export WHATS_NEW_INPUT="$INPUT"
python3 << 'PYEOF'
import json, sys, re, os

try:
    data = json.loads(os.environ.get("WHATS_NEW_INPUT", "{}"))
    prompt = data.get("prompt", "").lower()
except Exception:
    sys.exit(0)

if not prompt or prompt.startswith("/whats-new:"):
    sys.exit(0)

rules = [
    (r"refactor|rename.*across|change.*all.*files|update.*every|bulk.*edit|find.*replace.*all",
     "Subagents & Worktrees", "claude --worktree",
     "Subagents can parallelize multi-file work, and worktrees let agents run in isolated branches"),

    (r"every.*minutes?|keep.*running|repeat|watch.*for|monitor|poll|recurring|periodically|run.*again",
     "Loop & Cron Scheduling", "/loop 5m your-task-here",
     "Loop runs a prompt on a recurring interval -- set it and forget it"),

    (r"run.*test|test.*pass|test.*fail|check.*test|testing|jest|pytest|mocha|spec",
     "Loop & Cron Scheduling", "/loop 5m run the tests",
     "Loop can re-run your tests automatically on an interval while you keep working"),

    (r"approve|permission|allow|keep.*asking|stop.*asking|annoying.*prompt|too.*many.*confirm",
     "Auto Mode", "claude --permission-mode auto",
     "Auto mode uses a background classifier to approve safe actions automatically"),

    (r"pull.*request|create.*pr|merge|commit|push|git.*workflow|code.*review",
     "GitHub Integration", "Ask Claude to create a PR",
     "Claude can create PRs, review comments, manage issues, and trigger CI"),

    (r"background|close.*laptop|long.*running|leave.*running|overnight|takes.*long|walk.*away",
     "Background Agents", "Ctrl+B",
     "Ctrl+B backgrounds the current task -- it keeps running even after you move on"),

    (r"custom.*command|slash.*command|add.*command|create.*/\w+|my.*own.*command",
     "Skills System", "Create .claude/skills/my-skill/SKILL.md",
     "Skills let you create custom slash commands with markdown files"),

    (r"always.*follow|convention|rule|standard|guideline|enforce|style.*guide|never.*do|claude.*md",
     "Rules (CLAUDE.md)", "/init",
     "CLAUDE.md files let you set persistent instructions Claude follows in every session"),

    (r"trigger|automat|before.*commit|after.*edit|pre.*commit|post.*save|lint.*auto|format.*auto",
     "Hooks System", "/hooks",
     "Hooks run shell commands or AI prompts in response to Claude Code events"),

    (r"search.*code|find.*in.*files|grep|where.*is|look.*for.*string|find.*function|find.*class",
     "Grep & Glob Tools", "Claude uses these automatically",
     "Grep searches file contents with regex, Glob finds files by name patterns"),

    (r"fetch.*url|read.*page|documentation|web.*page|api.*docs|check.*website|scrape",
     "WebFetch Tool", "Ask Claude to fetch any URL",
     "Claude can fetch and analyze any web page -- docs, API responses, GitHub issues"),

    (r"screenshot|image|picture|diagram|mockup|design|visual|ui.*bug|what.*look",
     "Image Support", "Drag an image into the terminal or Ctrl+V",
     "Claude can see and analyze images -- just drag, paste, or provide a file path"),

    (r"parallel|simultaneous|at.*same.*time|multiple.*agent|split.*work|divide",
     "Subagents", "Claude spawns these automatically for complex tasks",
     "Subagents let Claude delegate subtasks to child agents that work in parallel"),

    (r"too.*slow|faster|speed.*up|cheaper|different.*model|switch.*model|opus|sonnet|haiku",
     "Model Selection & Effort Control", "/model",
     "Switch between Opus, Sonnet, and Haiku on the fly"),

    (r"remember|forget|context.*window|too.*long|running.*out.*context|compact|token",
     "Context Management", "/context",
     "/context shows your usage and /compact summarizes old context to free up space"),

    (r"plugin|extension|marketplace|install.*tool|add.*integration",
     "Plugin System", "/plugin",
     "Browse and install community plugins that add skills, hooks, and more"),

    (r"mcp|external.*tool|connect.*api|database.*tool|third.*party",
     "MCP Servers", "claude mcp add my-server -- npx server-package",
     "MCP servers connect Claude to external tools and data sources"),

    (r"vim|hjkl|modal.*edit|emacs",
     "Vim Mode", "/vim",
     "Full vim motions in the input editor -- hjkl, text objects, normal/insert mode"),

    (r"cost|spending|usage|expensive|how.*much|bill|token.*count|budget",
     "Cost & Stats Tracking", "/cost",
     "/cost shows your current session costs and token usage"),

    (r"resume|pick.*up|continue.*where|last.*session|come.*back|save.*session",
     "Session Management", "claude --resume",
     "claude --resume picks up your last session exactly where you left off"),

    (r"voice|speak|talk|hands.*free|dictate|speech",
     "Voice Mode", "/voice",
     "Hold Space to talk, release to send -- supports 20 languages"),
]

for pattern, feature, quick_start, tip in rules:
    if re.search(pattern, prompt):
        output = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": (
                    f"whats-new tip: The user might benefit from **{feature}**. "
                    f"{tip}. Quick start: {quick_start}. "
                    f"Mention this naturally in your response, prefixed with 'whats-new tip:' so the user knows it comes from the plugin. "
                    f"Keep it to 1-2 sentences. Don't force it if it doesn't fit. "
                    f"For more: /whats-new:learn-more {feature}"
                )
            }
        }
        json.dump(output, sys.stdout)
        break
PYEOF
