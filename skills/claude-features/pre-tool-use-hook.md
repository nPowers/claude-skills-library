# Pre-Tool Use Validation Hook

## Description
Intercepts all tool invocation requests before execution to validate inputs, enforce safety policies, log usage, and prevent harmful operations. Utilizes Claude Code's lifecycle hooks to ensure safe and compliant tool usage.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires lifecycle hooks available only in Claude Code)

## Instructions
1. Enable the pre-tool use hook in Claude Code.
2. On each tool call, intercept the input parameters.
3. Validate inputs against safety and policy rules.
4. Log the intended tool action for auditing.
5. Block or modify tool calls that violate safety constraints.
6. Allow safe tool calls to proceed.

## Example Usage
- "Validate tool inputs before execution"
- "Enforce safety policies on tool use"
- "Intercept and log tool calls pre-execution"

## Note
This skill is exclusive to Claude Code due to its reliance on lifecycle hooks for tool interception.