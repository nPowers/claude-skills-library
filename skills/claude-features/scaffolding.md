# Scaffolding Orchestrator

## Description
Scaffolding is a spec-driven orchestration plugin for Claude Code that coordinates multiple agents across a project lifecycle. It supports per-phase model tiers, opt-in lifecycle hooks, optional cross-device semantic memory, and templates for complex multi-agent flows.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (multi-agent orchestration requires local agent execution)

## Instructions
1. Install the Scaffolding plugin into Claude Code and review the included agent templates and skills catalog.
2. Define project phases (spec, design, implementation, test, review) and assign agent roles to each phase using provided templates.
3. Configure model tiers and resource constraints for each agent, and decide which lifecycle hooks to opt into for automation.
4. If cross-device semantic memory is needed, connect a compatible memory provider and configure namespaces for shared context.
5. Start an orchestration run: provide the project spec, acceptance criteria, and any constraints; let Scaffolding allocate tasks to agents.
6. Monitor agents' outputs, review synthesized artifacts, and accept or request rework for specific agents or phases.
7. Iterate on the spec and orchestration parameters until the end-to-end workflow meets project goals.

## Example Usage
- "Create a multi-agent plan for building and testing the payments API using Scaffolding"
- "Run the implementation phase with medium-tier models and enable the review agent"
- "Export the phase artifacts and a summary of agent decisions"

## Note
Scaffolding is a sub-agent orchestrator and must run inside Claude Code. Orchestration can spawn many tasks and models; monitor resource usage and review agent outputs for correctness.