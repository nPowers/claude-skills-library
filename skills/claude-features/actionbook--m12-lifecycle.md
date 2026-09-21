# M12 / Component Lifecycle — Actionbook

## Description
Explains component lifecycle concepts used in component development environments (mount, update, unmount, rendering phases) and how to apply them in an Actionbook-like workflow. Use when building, testing, or documenting UI components and their lifecycle behaviors.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask which UI framework and environment the user is using (React/Preact/solid, Actionbook or similar, component library versions).
2. Describe the core lifecycle stages relevant to the framework (initialization/mount, prop/state updates, re-rendering, cleanup/unmount) and typical side effects at each stage.
3. Explain how to represent lifecycle states in a component playground: stories/fixtures for initial state, interaction-driven updates, and teardown scenarios.
4. Provide concrete testing and debugging strategies: snapshot tests, interaction tests, story-driven visual checks, and how to simulate lifecycle transitions.
5. Suggest documentation patterns: annotate stories with lifecycle notes, include usage scenarios and expected events (e.g., data fetching on mount), and list props that affect lifecycle.
6. Offer performance guidance (memoization, effect dependency lists, avoiding expensive operations on render) and migration notes if updating framework versions.
7. Conclude with example triggers to create stories or tests and references to framework lifecycle docs.

## Example Usage
- "Show lifecycle stages for a React component in Actionbook"
- "How do I test a component's cleanup logic when it unmounts?"
- "Create a story plan that demonstrates mount, update, and error states"

## Note
I cannot run the component playground or execute tests here; include code or story snippets for targeted suggestions.