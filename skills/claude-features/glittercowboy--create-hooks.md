# Create Hooks — General Hook Generator

## Description
Generate well-structured, documented hooks for chat agents, web apps, or automation tasks. Use this skill when you need a clear hook interface, example implementation, installation instructions, and optional test scaffolding.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user which runtime or framework the hook targets (e.g., Claude Hook API, Node.js, Python, browser extension, or custom webhook).
2. Clarify the hook's purpose, inputs, outputs, error conditions, and lifecycle events (init, handle, teardown, etc.).
3. Propose a concise hook interface and a filename/structure convention; get confirmation before generating code.
4. Produce the hook implementation with comments, example usage, and minimal dependencies.
5. Provide optional unit tests or simple test harness code and instructions to run them.
6. Give installation and integration steps (how to register the hook, environment variables, required permissions).
7. Offer iterative refinement based on user feedback (optimize API, add logging, change signatures).

## Example Usage
- "Create a Claude hook that forwards messages to a logging service and retries on failure."
- "Generate a Python webhook handler that verifies HMAC signatures and returns JSON responses."
- "Show me a minimal Node.js hook that injects a header into outgoing requests."

## Note
This skill generates code examples and integration guidance but does not execute or install code by itself. Validate generated code and secrets before deploying to production.