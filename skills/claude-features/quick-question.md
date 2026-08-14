# Quick Question Game-Dev Agent Control Plane

## Description
Quick Question is a control plane designed for game development agents. It closes the loop with verified compile, test, and cross-model review across popular engines like Unity, Godot, Unreal, and S&box. It features lifecycle-aware routing via /qq:go, 26 slash commands under /qq:*, and supports Claude Code-first workflows with agent-agnostic integration through HTTP and MCP.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires code execution and multi-agent integration)

## Instructions
1. Deploy Quick Question in your Claude Code environment.
2. Use /qq:go for lifecycle-aware routing of game-dev tasks.
3. Utilize the 26 /qq:* slash commands to manage compile, test, and review processes.
4. Integrate with game engines via HTTP or MCP protocols.
5. Coordinate cross-model reviews and verification loops.

## Example Usage
- "/qq:go start build verification"
- "Run cross-model review with Quick Question"
- "Compile and test Unity project using /qq commands"

## Note
Quick Question requires Claude Code due to its reliance on code execution, HTTP integrations, and multi-agent orchestration. It is not supported on Claude Desktop.
