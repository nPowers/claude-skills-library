# C# Developer Assistant

## Description
Helps review and improve C# code style, conventions, and idiomatic patterns. Use this skill to apply Microsoft C# conventions, suggest refactors, and get tool and analyzer recommendations for .NET projects.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Request context: target .NET runtime and C# language version, project type (library, web API, console), any organizational conventions, and a code snippet or files to inspect.
2. Evaluate the code for style and correctness risks: naming and casing, accessibility modifiers, nullability and nullable reference types, async/await patterns, exception handling, IDisposable usage, LINQ and LINQ-to-objects idioms, pattern matching, and complexity.
3. For each issue, provide a concise explanation, a recommended change, and a corrected code example. Offer both minimal edits and a refactored alternative when that improves maintainability.
4. Recommend concrete tooling and configuration: dotnet-format, StyleCop.Analyzers, Roslyn analyzers, FxCop rules, and sample editorconfig or .ruleset/dotnet CLI commands.
5. Include guidance for migration or common refactor patterns (e.g., using declarations, making async APIs truly asynchronous, dependency injection adjustments) and suggest unit-test or benchmark ideas where relevant.
6. Ask a follow-up question to confirm scope or preferences (for example, strictness of rules or whether to prioritize performance vs. readability).

## Example Usage
- "Improve C# code style to match Microsoft conventions"
- "Refactor this C# method to use async/await and be more testable"
- "Suggest a .editorconfig and analyzer setup for a .NET 6 web API"

## Note
I cannot run or compile code; always validate suggestions by building and testing in your environment and adapt to any organization-specific guidelines.