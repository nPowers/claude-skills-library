# React Hooks Refactor Assistant

## Description
Specialized assistant for migrating components to React hooks and extracting reusable hook logic. Use this skill to analyze components, propose modular hooks, and generate a safe migration plan with tests.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Request the component code or a representative sample and note the React version and project constraints.  
2. Analyze stateful logic and side effects to identify candidates for extraction into hooks.  
3. Propose one or more custom hooks with clear APIs and a step-by-step migration plan that minimizes breaking changes.  
4. Provide the hook implementations and updated component examples demonstrating integration.  
5. Add unit and integration tests for the hook and the refactored component, plus a rollback strategy.  
6. List potential pitfalls (stale closures, dependency arrays, render performance) and mitigation techniques.

## Example Usage
- "Help migrate this class component to hooks"
- "Extract a useForm hook from my form component"
- "Create tests for the new hook and the updated component"

## Note
I produce refactor recommendations and code snippets; you must run, test, and integrate the changes in your repository.