# React Hooks Assistant

## Description
Help design, implement, and refactor React hooks. Use this skill to create custom hooks, explain hook rules, optimize performance, and produce testable examples.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask whether the user wants a new custom hook, a refactor of a component, or an explanation of hook behavior.  
2. Request the relevant component code or a clear description of the desired behavior and state transitions.  
3. Propose a hook signature (name, inputs, outputs) and explain the rationale for its API.  
4. Provide a full implementation using best practices (useEffect dependency handling, useCallback/useMemo where appropriate, cleanup, error handling).  
5. Supply usage examples showing how to integrate the hook in function components.  
6. Add unit tests or testing guidance (React Testing Library, Jest), and list common performance pitfalls and optimization tips.  
7. Offer migration steps if converting class components or duplicated logic into reusable hooks.

## Example Usage
- "Write a useFetch hook that supports cancellation and caching"
- "Refactor this component to use custom hooks"
- "Explain useEffect dependencies for this effect"

## Note
I produce code and tests for copy-and-paste; run and validate returned code in your environment before deploying.