# CC Commander — Claude Code Orchestrator

## Description
CC Commander is an orchestration framework that shapes Claude Code behavior using an enforceable, gate-based methodology, a large library of plugin skills, and many specialist agents. Use it to standardize and control multi-agent Claude Code workflows and lifecycle hooks.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (sub-agent orchestration and local plugin management require code execution and CLI installation)

## Instructions
1. Review the Commander repository and documentation to understand the plugin model and the gate-based enforcement approach.
2. Clone the repository and install Commander per the project instructions (CLI install or local setup).
3. Register or enable desired plugins and specialist agents from the available plugin catalog, and configure any plugin-specific settings.
4. Define a Commander workflow: select the sequence of gates or enforcement checks to apply for each task, and attach the relevant lifecycle hooks for start, progress, and completion events.
5. Run workflows under Commander and observe agent outputs; iterate on gate settings and plugin selection to shape outputs into the desired Fable-style results.
6. Add Commander to your Claude Code runtime hooks so it intercepts and enforces policies across sessions.

## Example Usage
- "Run CC Commander to apply the standard 12-gate workflow to this Claude Code task"
- "Enable the 'review' and 'safety' plugins in Commander before launching the agent chain"
- "Add Commander as a lifecycle hook to validate outputs at the end of each job"

## Note
Commander is an orchestration tool that runs locally and controls sub-agents; installation and plugin configuration require access to the local system and the repository's setup instructions.