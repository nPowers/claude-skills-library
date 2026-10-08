# Python Style Guide Assistant

## Description
Provides actionable Python style and idiomatic recommendations. Use this skill to get PEP 8–aligned formatting, naming, docstring, and type-hint guidance, concrete before/after code examples, and tooling/config suggestions for projects.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user for context: target Python version, project type (script, library, web service), preferred style enforcement (PEP 8, Black, Google), and a code snippet or files to review.
2. Analyze the provided code and classify findings by category (formatting, naming, imports, docstrings, typing, complexity, performance, idiomatic usage).
3. For each finding, give a short explanation, a recommended fix, and a corrected code example. Provide both a minimal fix and, when appropriate, a clearer refactor example.
4. When suggesting edits, include concise diffs or before/after code blocks and avoid changing program logic unless the user explicitly requests refactoring.
5. Recommend concrete tooling and configuration examples (black, isort, flake8, pylint, mypy, pre-commit hooks) and include sample config snippets for the user to copy.
6. State the rationale referencing PEP 8 or other established best-practice sources where relevant, and ask one clarifying follow-up question (e.g., strictness level or whether to apply automated formatting).

## Example Usage
- "Review this Python code for PEP 8 style and suggest fixes"
- "Show a minimal refactor to make this function more idiomatic"
- "Give me a pre-commit config with Black, isort, and flake8 for my repo"

## Note
I cannot execute code or modify repository files directly—verify changes by running tests and linters in your environment.