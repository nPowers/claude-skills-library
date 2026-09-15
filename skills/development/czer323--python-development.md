# Practical Python Development — czer323

## Description
Guidance for real-world Python development tasks: project layout, packaging, testing, CI, dependency management, linting, and debugging. Use when building or improving Python projects and CI workflows.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Clarify the project type (library, CLI, web service), target Python versions, and deployment/packaging needs.
2. Recommend a project structure and show example files (pyproject.toml or setup.py, package layout, tests directory).
3. Provide example packaging config (pyproject.toml + poetry or setuptools) and explain relevant fields.
4. Supply sample unit tests (pytest) and basic test commands; recommend coverage and test practices.
5. Show a sample CI configuration (e.g., GitHub Actions) to run tests, linters, and publish artifacts.
6. Recommend developer tooling: linters (flake8/ruff), formatter (black/isort), type checker (mypy), and dependency management strategies.
7. Offer debugging tips and recommended logging/monitoring practices for production services.

## Example Usage
- "Create a pyproject.toml for a small library with pytest and mypy"
- "Set up GitHub Actions to run tests on push and PRs"
- "Recommend dev dependencies and a project layout for a Flask app"

## Note
I cannot access repositories or execute packaging/CI steps. Provide configs and commands that users can run in their environment.