# Pre-Tool Use Validation Hook

## Description
Intercepts all tool invocation requests before execution to validate inputs, enforce safety policies, log actions, and prevent harmful operations. Built using Claude Code's lifecycle hooks.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires lifecycle hooks to intercept tool calls)

## Instructions
1. Enable the pre-tool use hook in Claude Code.
2. On each tool call, validate input parameters against safety rules.
3. Log the intended tool action for auditing.
4. Block or modify calls that violate safety policies or could cause damage.
5. Allow safe tool calls to proceed normally.

## Example Usage
- "Activate pre-tool use validation"
- "Intercept and validate tool calls before execution"
- "Enforce safety policies on tool usage"

## Note
This skill depends on Claude Code's hook system and cannot run on Claude Desktop.