# Pre-Tool Use Validation Hook

## Description
Intercepts all tool invocation calls before execution to validate inputs, enforce safety policies, log actions, and block potentially destructive operations. Built using Claude Code's lifecycle hooks.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires hook interception and validation logic)

## Instructions
1. Install the pre-tool use hook in your Claude Code environment.
2. Define validation rules and safety policies for tool inputs.
3. Intercept tool calls and apply validation before execution.
4. Log all intercepted calls and block unsafe operations.

## Example Usage
- "Validate tool inputs before execution."
- "Prevent destructive tool actions automatically."
- "Log all tool use attempts for review."

## Note
This skill depends on lifecycle hooks and code interception, so it is only supported in Claude Code.