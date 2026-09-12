# Enterprise Agent Pack for Claude Code

## Description
A collection of production-ready subagents and orchestration templates tailored for enterprise software projects. Use it to provision persistent project memory, coordinate multi-agent workflows (for example: code review, testing, CI orchestration), and enforce orchestration rules across agents. Designed to run inside a Claude Code environment where agents can execute code, access project files, and maintain long‑lived state.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (Code-only: subagents require file system access, execution privileges, and persistent storage)

## Instructions
1. Clone or install the agent pack repository into your Claude Code workspace and inspect the examples and config templates.
2. Adapt the agent configuration: define agent roles, prompts, allowed actions, and memory backends for each subagent.
3. Provision persistent storage (local DB, vector store, or file-backed store) and record connection details in the config.
4. Register subagents with the orchestrator, mapping triggers, priorities, and permitted memory scopes.
5. Define orchestration rules: specify triggers (webhooks, schedules, or messages), escalation policies, concurrency limits, and conflict-resolution strategies.
6. Start the orchestrator and launch subagents inside the Claude Code runtime; monitor logs, heartbeats, and agent health.
7. Initialize a project session by sending structured context (repository path, project name, key files or summaries) to seed project memory and agent state.
8. Observe agent outputs and logs, then iterate on prompts, retention settings, and orchestration rules to refine behavior.
9. Secure credentials and access control: restrict memory access, rotate secrets, and enforce organizational policies for auditing and data governance.

## Example Usage
- "Initialize agent pack for repo https://github.com/example/project and start code-review and test-run subagents"
- "Create persistent memory for Project Alpha and register a deployment orchestrator with a daily schedule"
- "Run security-audit subagent across src/ and summarize findings into project memory"

## Note
This skill requires a Claude Code runtime with file system and execution access and is not usable on Claude Desktop. See the upstream repository for installation, examples, and license: https://github.com/chuckplayer/claude-agent-pack. Ensure you follow your organization’s security and data-handling policies when enabling persistent memory and external integrations.