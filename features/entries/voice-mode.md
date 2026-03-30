---
name: Voice Mode
category: Core Modes
introduced_version: "1.0.0"
introduced_date: 2025-06-20
status: ga
ga_version: "1.0.0"
ga_date: 2025-06-20
one_liner: "Talk to Claude Code with your voice -- hold a key, speak, release to send."
tags: [voice, accessibility, speech-to-text, hands-free]
---

## What it does
Voice Mode adds speech-to-text input to Claude Code. Hold down the push-to-talk key, say what you want, and release to send it as a prompt. It supports 20 languages and works with your system's speech recognition. It's especially handy when you're thinking out loud about a problem or want to give instructions without context-switching to typing.

## When to use it
- You're brainstorming or thinking through an approach and want to talk it out rather than type
- You have an accessibility need that makes extended typing difficult
- You're reviewing code on a second monitor and want to send instructions hands-free
- You're dictating longer descriptions or requirements that would be tedious to type
- You want to quickly ask a follow-up question without breaking your reading flow

## How to use it
1. **Check your setup**: Ensure your terminal and OS allow microphone access.
2. **Configure the push-to-talk key**: Go to Claude Code settings and set your preferred key. The default varies by terminal emulator.
3. **Set your language**: If you're not using English, configure your preferred language in settings. 20 languages are supported.
4. **Use it**: Hold the push-to-talk key, speak your prompt clearly, and release the key. Your speech is transcribed and sent to Claude as text.
5. You can mix voice and typed input freely within the same session.

## Pro tips
- Voice Mode transcribes to text, so Claude sees exactly what you'd type. You can say things like "use plan mode" or "slash compact" and it works as expected.
- Speak in short, clear sentences for the best transcription accuracy. Pausing briefly between thoughts helps the recognizer segment properly.
- If you work in a noisy environment, consider a directional microphone or headset -- it makes a significant difference in transcription quality.

## Status history
- **2025-06-20 (v1.0.0)**: Released as GA. Push-to-talk voice input with multi-language support.
