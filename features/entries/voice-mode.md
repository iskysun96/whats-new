---
name: Voice Mode
category: Core Modes
introduced_version: "2.1.69"
introduced_date: 2025-06-20
status: ga
ga_version: "2.1.69"
ga_date: 2025-06-20
one_liner: "Talk to Claude Code with your voice -- hold a key, speak, release to send."
quick_start: "/voice"
detection:
  type: keyword
  patterns:
    - "voice.*input"
    - "speak.*to.*claude"
    - "dictate"
    - "hands.*free"
    - "speech.*to.*text"
  tip: "You can speak to Claude instead of typing. Try /voice — hold Space to talk, release to send."
  signal: keyword
tags: [voice, accessibility, speech-to-text, hands-free]
---

## What it does
Voice Mode adds speech-to-text input to Claude Code. Hold down the push-to-talk key (default: `Space`), say what you want, and release to finalize the transcription. It supports 20 languages and streams your recorded audio to Anthropic's servers for transcription (audio is not processed locally). It requires a Claude.ai account and is not available with direct API keys, Bedrock, Vertex, or Foundry. It's especially handy when you're thinking out loud about a problem or want to give instructions without context-switching to typing.

## When to use it
- You're brainstorming or thinking through an approach and want to talk it out rather than type
- You have an accessibility need that makes extended typing difficult
- You're reviewing code on a second monitor and want to send instructions hands-free
- You're dictating longer descriptions or requirements that would be tedious to type
- You want to quickly ask a follow-up question without breaking your reading flow

## How to use it
1. **Enable voice dictation**: Run `/voice` in Claude Code to toggle it on. The first time, it runs a microphone check and may trigger an OS permission prompt.
2. **Use it**: Hold `Space` (the default push-to-talk key) to start recording. There is a brief warmup while hold detection triggers -- the footer shows `keep holding...` then switches to a live waveform. Release to finalize the transcription. Your speech is inserted at the cursor position as text.
3. **Set your language**: If you're not using English, set your language via `/config` or the `language` setting in your settings file (e.g., `"language": "japanese"`). 20 languages are supported. If unset, dictation defaults to English.
4. **Rebind the key**: To skip the warmup, rebind the push-to-talk key to a modifier combination like `meta+k` in `~/.claude/keybindings.json` (bind `voice:pushToTalk` in the `Chat` context). Modifier combos start recording on the first keypress.
5. You can mix voice and typed input freely within the same session -- the transcript is inserted at your cursor position.

## Pro Tips
- Voice Mode transcribes to text, so Claude sees exactly what you'd type. You can say things like "use plan mode" or "slash compact" and it works as expected.
- Speak in short, clear sentences for the best transcription accuracy. Pausing briefly between thoughts helps the recognizer segment properly.
- If you work in a noisy environment, consider a directional microphone or headset -- it makes a significant difference in transcription quality.

## Status history
- **2025-06-20 (v2.1.69)**: Released as GA. Push-to-talk voice input with multi-language support.
