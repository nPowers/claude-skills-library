# Quick Question Game-Dev Control Plane

## Description
Quick Question is a control plane for game development agents that closes the loop with verified compile, testing, and cross-model review across Unity, Godot, Unreal, and S&box. It features lifecycle-aware /qq:go routing and 26 /qq:* slash commands. Designed primarily for Claude Code, it supports agent-agnostic operation via HTTP and MCP.

## Platforms
- Claude Desktop: Not Supported (requires lifecycle routing and agent orchestration features)
- Claude Code: Supported

## Instructions
1. Activate Quick Question within Claude Code.
2. Use /qq:go routing to manage lifecycle-aware task flows.
3. Employ the 26 /qq:* slash commands for various game-dev operations.
4. Integrate with Unity, Godot, Unreal, and S&box pipelines.
5. Utilize HTTP and MCP protocols for agent-agnostic communication.
6. Verify compile and test results to close the development loop.

## Example Usage
- "/qq:go start compile and test cycle"
- "/qq:review cross-model game assets"
- "/qq:deploy to Unreal environment"

## Note
Quick Question requires Claude Code due to its reliance on lifecycle routing and multi-agent orchestration. It is not supported on Claude Desktop.
