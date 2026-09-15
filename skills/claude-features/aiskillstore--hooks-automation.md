# Hooks Automation — Generation & Test Workflows

## Description
Automate creation, testing, and CI integration for hooks: scaffold projects, generate tests, run linters, and produce CI job snippets. Use this skill when you want repeatable, scriptable hook pipelines.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires file scaffolding, test execution, or CI script generation)

## Instructions
1. Ask which language, test framework, and CI system the project uses (e.g., GitHub Actions, GitLab CI, CircleCI).
2. Confirm repository layout, preferred package manager, and any required secrets or environment variables.
3. Generate scaffolding scripts or templates (project structure, example hooks, test files, linter config).
4. Provide CI job definitions that run unit tests, linters, and optional integration tests for hooks.
5. Produce automation scripts for local development: test runners, pre-commit hooks, and codegen commands.
6. Explain how to wire secrets and environment variables into CI securely and how to run the pipeline locally.
7. Offer iterative improvements: parallelization, caching strategies, and test flakiness mitigation.

## Example Usage
- "Create a GitHub Action that runs tests and linters for my hook library."
- "Scaffold a repository with a hook template, Jest tests, and husky pre-commit hooks."
- "Generate a CI job that runs integration tests against a staging webhook endpoint using stored secrets."

## Note
This skill generates automation code and CI configurations and is designed for environments where file operations and test execution are permitted; it does not itself run commands unless executed in a code-capable environment.