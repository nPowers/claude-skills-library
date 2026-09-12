# Claude Night Market

## Description
A collection of Claude Code plugins and agent integrations that add test-driven development hooks, git and PR workflows, spec-driven development, automated code review, lifecycle and maintenance automation, context optimization, and multi-LLM delegation. Use it to add structured developer workflows and automated enforcement across projects.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires local plugin/agent execution and access to project repository)

## Instructions
1. Confirm Claude Code is running and you have repository access. Install the Night Market plugin bundle into your Claude Code environment.
2. Describe the repository, language, and preferred workflows (TDD, PR gating, spec-driven tests). Let the skill infer relevant hooks.
3. Choose which modules to enable (TDD enforcement, git/PR workflows, spec generation, code review, maintenance automation, multi-LLM delegation).
4. Request a run: ask the skill to generate and apply config files (CI hooks, pre-commit, test harnesses) or to produce a step-by-step plan for manual integration.
5. For automated runs, provide commit range or branch; instruct the plugin to execute test suites, produce failing tests, or propose fixes using the fix-from-error flow.
6. Use the code-review module to get a synthesized review and suggested PR comments; accept or iterate on suggested patches.
7. Ask for ongoing maintenance automation: schedule periodic dependency checks, refactor suggestions, or context trimming rules for future sessions.
8. If multi-LLM delegation is desired, specify roles and constraints for each model; validate outputs and adjust delegation policy.

## Example Usage
- "Enable Night Market TDD enforcement and generate CI hooks for this repo"
- "Run the PR workflow on branch feature/login and produce a review summary and suggested fixes"
- "Set up spec-driven development: create a spec, tests, and an initial implementation for the auth module"

## Note
Requires Claude Code and local repository access. Installation, repository hooks, and automated actions will modify files and run tests; review generated changes before merging.