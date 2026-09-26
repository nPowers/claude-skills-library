# ECC - Antigravity

## Description
A Claude Code runtime bundle for "Google Antigravity" projects that packages 68+ specialized agents, 280+ skills, and built-in safety and quality lifecycle hooks. Use this skill to provision a ready ECC runtime, orchestrate agents, and apply automated governance checks during development and deployment.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires the Claude Code runtime; provides ECC agents, runtime components, and lifecycle hooks)

## Instructions
1. Clone the repository to your Claude Code workspace: git clone https://github.com/cloudblower/ECC-Antigravity.git
2. Install any listed prerequisites (runtime libs, Python/Node versions, container runtime) according to the repo README.
3. Start the ECC runtime or agent orchestrator following the included startup script (e.g., launch the provided supervisor or docker-compose) so agents are registered.
4. List available agents and skills exposed by the runtime to confirm successful startup.
5. Invoke a specific agent with a clear task payload (task description, input files, and desired outputs) through the runtime's CLI or API gateway.
6. Enable the automated safety and quality hooks before running deployment workflows to enforce checks and logging.
7. Monitor agent execution logs, capture outputs, and iterate on agent prompts or skill parameters as needed.
8. When customizing, edit agent configurations or skill definitions in the workspace and redeploy the runtime to apply changes.

## Example Usage
- "Initialize ECC-Antigravity runtime and list available agents"
- "Run the antigravity-deploy agent with this deployment manifest"
- "Enable safety hooks and run a full integration test suite"

## Note
Requires a Claude Code environment and access to the local filesystem/containers. Review the repository README for hardware and dependency requirements before use.