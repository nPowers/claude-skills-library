# CodeStatus Menu

## Description
CodeStatus is a macOS menu bar utility that tracks active Claude Code and Codex sessions, displaying which coding agents are working, idle, or awaiting user input based on official lifecycle hooks rather than CPU activity. It is free and open source with no telemetry.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires local macOS menu bar integration and access to Claude Code lifecycle hooks)

## Instructions
1. Install the CodeStatus application on macOS and grant any required accessibility or network permissions per the installer instructions.
2. Connect CodeStatus to your local Claude Code or Codex session so it can subscribe to lifecycle hook events.
3. Configure which agent sessions to track and how notifications should be displayed in the menu bar.
4. Use the menu to inspect agent states, view recent lifecycle events, and jump to the corresponding project or session.
5. Adjust preferences for polling intervals, notification verbosity, and which lifecycle events trigger alerts.
6. For troubleshooting, open the CodeStatus logs and verify that lifecycle events are arriving from Claude Code as expected.

## Example Usage
- "Show me which agents are currently working on the repo in the menu bar"
- "Notify me when the review agent finishes or awaits input"
- "Open the session history for the last 24 hours"

## Note
CodeStatus is a macOS utility and requires local access to Claude Code lifecycle hooks. It does not collect telemetry but does require appropriate permissions to read lifecycle events and display UI elements in the menu bar.