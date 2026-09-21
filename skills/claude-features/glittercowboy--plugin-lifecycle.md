# Plugin Lifecycle — Glittercowboy

## Description
Describes the typical lifecycle for plugins (install, initialize, activate, run, deactivate, uninstall), event hooks, and best practices for developing reliable, updatable plugins. Use this skill when authoring plugins or integrating third-party plugins into a host application.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user which host platform or plugin API they target (IDE, CMS, build tool, browser extension, etc.) and which runtime constraints apply.
2. Define a generic plugin lifecycle: installation → registration → initialization → activation → runtime interaction → deactivation → uninstallation, and list common responsibilities at each step.
3. Enumerate common hooks/events and recommended handler behaviors (idempotence, error handling, async initialization, resource cleanup on deactivate).
4. Provide guidance on state management, configuration storage, version compatibility, and migrations during upgrades.
5. Offer debugging and testing practices: sandboxed runs, mock host APIs, graceful degradation when dependencies are missing, and telemetry points.
6. If requested, produce a short checklist or template outlining manifest fields, required hooks, and a minimal compatibility contract for the host.
7. Close with tips for secure plugin practices (validate inputs, least privilege, avoid global side effects) and suggest release strategies.

## Example Usage
- "What are the lifecycle hooks I should implement for my IDE plugin?"
- "How should a plugin clean up resources when it is deactivated?"
- "Give me a compatibility checklist for plugin version upgrades"

## Note
I cannot inspect or run plugin binaries; include manifest snippets or API signatures for more precise templates or example code.