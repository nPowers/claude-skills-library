# Python Code Generator

## Description
Generate, refactor, and document Python code snippets and modules. Use this skill when you need idiomatic, PEP 8–compliant code, explanations of design choices, or unit tests for Python functions and packages.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask the user for the goal, constraints (Python version, style, dependencies), and any existing code.
2. Produce concise, runnable Python code examples with clear filenames where appropriate (module.py, tests/test_module.py).
3. Follow PEP 8, include docstrings and type hints, and explain nontrivial choices in 1–3 sentences.
4. When refactoring, provide a before/after diff or clearly labeled code blocks for old and new versions.
5. Include unit tests (pytest/unittest) and example commands to run tests; list required pip packages and versions.
6. If the user requests performance or security considerations, add actionable suggestions and small code changes.
7. Always ask a clarifying question if the prompt is ambiguous before producing final code.

## Example Usage
- "Write a Python function that merges two sorted lists and include tests"
- "Refactor this class to use dataclasses and add type hints"
- "Show me a pytest suite for this module and list dependencies"

## Note
This skill generates code and guidance but cannot execute code or access the user filesystem; recommend running tests locally or in an execution-capable environment.