# Quick Question Game-Dev Agent Controller

## Description
Manage and coordinate game development agents across Unity, Godot, Unreal, and S&box. Provides lifecycle-aware routing, verified compile and test cycles, and cross-model review using HTTP and MCP protocols. Designed primarily for Claude Code with extensive slash command support.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires HTTP and MCP integration for agent coordination)

## Instructions
1. Activate the skill in Claude Code environment.
2. Use lifecycle-aware routing commands to initiate compile, test, and review cycles.
3. Employ slash commands prefixed with /qq: to interact with agents.
4. Monitor agent responses and close the loop with verified outputs.

## Example Usage
- "/qq:go compile the latest build"
- "/qq:test run unit tests on Godot project"
- "/qq:review cross-check Unreal asset integration"

## Note
This skill requires Claude Code due to its reliance on agent orchestration via HTTP and MCP protocols and is not available on Claude Desktop.