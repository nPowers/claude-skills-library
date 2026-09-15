# React Hooks Generator & Reviewer

## Description
Create and review custom React hooks (useX) with type-safe signatures, tests, and usage examples. Use this for building reusable stateful logic, optimizing renders, or migrating logic into hooks.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask which React version and whether the project uses TypeScript or JavaScript.
2. Ask for the hook's responsibilities, required inputs, and expected outputs (state, callbacks, returned values).
3. Propose the hook API (name, params, return shape) and list any external dependencies (context, service calls).
4. Generate the hook implementation with React best practices: proper dependency arrays, memoization, and cleanup.
5. Provide example usage in a component, plus unit tests (Jest/React Testing Library) or TypeScript types.
6. Offer performance tweaks (useMemo, useCallback) and migration hints if converting from classes or HOCs.

## Example Usage
- "Create a useAuth hook that fetches a token and exposes user info and a refresh method."
- "Review my useDebouncedValue hook — it's causing stale values in components."
- "Generate TypeScript tests for a usePagination hook."

## Note
Generated hooks are templates — run and test them in your environment. Pay attention to dependency arrays and side effects when integrating into large apps.