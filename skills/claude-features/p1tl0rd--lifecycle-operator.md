# Lifecycle Operator

## Description
An orchestration-focused skill that defines and executes lifecycle operator actions for systems and services. Use it to translate lifecycle plans into operator tasks, automation steps, and executable runbooks.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires execution context to run lifecycle operations and coordinate sub-agents)

## Instructions
1. Gather the target resource definitions, desired lifecycle goal, and any constraints (maintenance windows, dependencies).
2. Synthesize an ordered set of operator actions with preconditions, success criteria, and rollback procedures.
3. Emit executable artifacts suitable for automation (e.g., task list, operator manifests, or orchestration commands) and a human summary.
4. If running inside a Code execution environment, validate actions against the environment and optionally dispatch sub-agent tasks to carry out steps.
5. Report progress, handle failures by applying rollback logic, and produce a final status report.

## Example Usage
- "Create an operator runbook to migrate service A with zero downtime"
- "Translate this lifecycle plan into executable operator tasks"
- "Execute the lifecycle operator plan in the current orchestration environment"

## Note
This skill is designed for programmatic orchestration and requires a Code-capable environment to run tasks and coordinate sub-agents; it will not function in a Desktop-only context.