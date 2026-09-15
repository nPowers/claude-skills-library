# BenchFlow Git Hooks Manager

## Description
Tooling-focused skill to inspect, scaffold, install, and manage Git hooks inside a repository. Use it for adding pre-commit, pre-push, or custom hook scripts and for safely updating hook sets.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires filesystem and Git access to read/write hook files and set executables)

## Instructions
1. Ask the user to confirm the target repository path and whether they want a dry run or to perform changes.
2. Validate that the path is a Git repository; if not, inform the user and request a different path.
3. List existing hooks in .git/hooks and summarize their types and executability.
4. Offer actions: create scaffolded hook templates (pre-commit, commit-msg, pre-push), install a provided hook script, enable/disable a hook (by backing up or restoring files), or remove a hook.
5. Before making changes, present a clear plan and require explicit user confirmation.
6. When installing, create backups of replaced hooks, write new files, set executable bits, and report results (files changed, backups created, errors).
7. For testing, run safe, non-destructive checks (e.g., syntax checks) and, if requested, trigger a simulated commit/push step only after user agreement.
8. Always provide a rollback procedure and show exact commands or steps performed.

## Example Usage
- "Inspect hooks in /workspace/project and show me which are executable"
- "Install a provided pre-commit script at /repo with a backup and make it executable (confirm before writing)"
- "List existing hooks and scaffold a commit-msg hook template that validates conventional commits"

## Note
This skill performs filesystem and Git operations. It will not modify anything without explicit confirmation. Be cautious with repositories that have uncommitted changes.