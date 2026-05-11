# Harness Mem Session Log Analyzer

## Description
A command-line tool that analyzes AI agent session logs to generate concise, human-readable summaries. Integrates with Claude Code's session lifecycle to automatically capture and brief users on session activities upon return.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires CLI access and session lifecycle hooks)

## Instructions
1. Install and configure the Harness Mem tool within Claude Code.
2. Allow it to hook into session lifecycle events to capture logs.
3. Upon returning to a session, request a summary of previous activities.
4. Review the generated briefings to quickly get up to speed.

## Example Usage
- "Summarize last session's key points"
- "Generate briefing for recent interactions"
- "Provide overview of agent decisions"

## Note
This tool is designed exclusively for Claude Code environments due to its reliance on CLI integration and session lifecycle hooks.