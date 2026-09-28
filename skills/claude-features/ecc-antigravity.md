# ECC Antigravity — Claude Code Runtime & Lifecycle Hooks

## Description
A Claude Code runtime package that delivers the Antigravity ECC suite: a large collection of specialized agents and reusable skills plus automated safety and quality lifecycle hooks driven by Gemini 3.8. Use this skill to install, inspect, test, and orchestrate ECC agents and to configure CI-style safety and quality checks before deployment.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires filesystem and runtime execution; this skill performs repository operations and runs tests)

## Instructions
1. Confirm the user's objective and environment details (install, inspect agents, run tests, deploy, or configure lifecycle hooks; OS, runtime versions, network access).
2. If installation is requested, provide the exact commands to clone the repository, install dependencies, and initialize the runtime. Explain expected outputs and common failure signals.
3. If inspection is requested, enumerate available agents and skills (counts, names, short descriptions), and provide a concise capability summary for each major component.
4. If testing or validation is requested, run the automated safety and quality lifecycle hooks, collect logs, and summarize pass/fail status with key findings and severity levels.
5. If deployment or orchestration is requested, produce a step-by-step rollout plan including required resources, configuration files to adjust, commands to execute, and post-deploy verification checks.
6. For any detected issues, supply targeted remediation steps, minimal code or config snippets to apply fixes, and recommended safety mitigations.
7. Before executing any system-changing commands, present the commands to the user for review and request explicit confirmation.

## Example Usage
- Set up the ECC Antigravity runtime and run the safety hooks
- List all Antigravity agents and summarize their purposes
- Run the automated quality checks and return failures with remediation steps

## Note
This skill requires Claude Code with repository access, network connectivity, and permission to run code on the host. Review and approve any commands before execution. The implementation is based on the cloudblower/ECC-Antigravity project on GitHub; ensure you trust the source and inspect scripts prior to running them.