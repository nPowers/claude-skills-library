# Lifecycle Hook Manager

## Description
Plan and generate lifecycle hooks for multi-step agent workflows. Use this skill to map lifecycle phases (init, validate, execute, finalize), produce hook stubs, and create a test plan for each phase.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user to list the workflow or agent flow and its major phases (e.g., start, pre-check, action, post-check, cleanup).
2. For each phase, define the intent of the hook, expected inputs/outputs, and success/failure handling.
3. Produce concise hook stubs (specification + example handler) for each lifecycle phase in pseudocode or the target hook format.
4. Provide a prioritized set of test scenarios and example inputs/outputs to validate each hook.
5. Recommend observability and rollback strategies (logging points, metrics to capture, safe failure behaviors).
6. Present a short integration plan describing where to attach hooks and any configuration or permission changes required.

## Example Usage
- "Help me add lifecycle hooks to validate inputs before my agent runs actions."
- "Create pre- and post-action hook stubs for a multi-step data pipeline."
- "Generate a test plan for lifecycle hooks in a customer support agent."

## Note
The skill creates specifications and examples only; executing or deploying hooks must be performed in your runtime environment.