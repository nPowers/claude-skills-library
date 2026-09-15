# Python Refactor & Style Assistant

## Description
Recommend refactorings, style improvements, and modernization for Python codebases. Use this skill to make code more readable, maintainable, and idiomatic (PEP 8, type hints, async improvements, etc.).

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask for the code or repository context, target Python version, desired constraints (backwards compatibility, performance, memory).
2. Identify anti-patterns, duplicate logic, large functions, and opportunities for applying dataclasses, typing, or comprehensions.
3. Provide concrete refactor suggestions with before/after code snippets and brief explanations of benefits and trade-offs.
4. Suggest tests to validate refactors and include example pytest cases or contract checks.
5. Offer performance-minded alternatives when appropriate and indicate complexity or potential regressions.
6. If multiple refactor paths exist, present a prioritized plan (smallest safe change → larger improvements).
7. Ask clarifying questions if repository structure or integration points are unclear.

## Example Usage
- "Refactor this function to be more testable and idiomatic"
- "Convert this module to use dataclasses and add type hints"
- "Suggest small, safe refactors for a legacy file"

## Note
This skill produces static refactoring guidance and cannot run or validate changes locally. Recommend running tests after applying changes.