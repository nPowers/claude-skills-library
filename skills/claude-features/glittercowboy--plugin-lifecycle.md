# Plugin Lifecycle Manager

## Description
A concise guide and assistant for managing a plugin's lifecycle: install, enable, configure, run, update, deactivate, and uninstall. Use this when designing plugin hooks, writing handlers, or diagnosing lifecycle-related problems.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Clarify context: ask the user what kind of plugin (UI component, background worker, integration, etc.), the target environment (development, staging, production), and the platform/runtime.
2. Present the canonical lifecycle phases: install, enable (or activate), configure, run/operate, update/migrate, deactivate/disable, uninstall, and error/recovery.
3. For each phase, provide a short description, the typical triggers/events, recommended hook names, expected handler signatures, and an example event payload.
4. Offer concrete examples: produce a manifest snippet and a short pseudo-code or code example (specify language when requested) showing hook registration and the handler logic for one or two phases.
5. Recommend versioning and migration practices: semantic versioning rules, compatibility checks, and safe update steps (backup, feature flags, migration scripts, rollbacks).
6. Create a checklist artifact on request: pre-install checks, post-install verification steps, update checklist, and uninstall cleanup tasks.
7. Provide common troubleshooting steps for lifecycle failures (missing permissions, dependency mismatches, failed migrations) and suggested remediation for each.
8. Ask whether the user wants a tailored manifest, language-specific code examples, or a test plan for automated lifecycle testing.

## Example Usage
- "Help me design the lifecycle hooks for a background data-sync plugin"
- "Show me example install and update handlers and payloads for a browser extension plugin"
- "Create a checklist and manifest snippet for safely upgrading my analytics plugin from v1.2 to v2.0"

## Note
This skill provides design guidance and example code only; it does not perform file or system changes. Validate any generated snippets in your environment and run tests before applying to production.