# Lifecycle Mapping Assistant

## Description
Translate application states and events into a clear lifecycle mapping that drives hooks and handlers. Use this to produce state→event→handler tables, prioritized actions per state, and sample code for the mapped handlers.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Request the list of application states, important events, and desired transitions (include edge cases and user roles).
2. Produce a state-machine mapping table listing: state, triggering events, resulting state, and recommended handler/hook action.
3. For each mapping row, provide a brief handler specification (inputs/outputs, validations, side effects).
4. Offer sample handler implementations or pseudocode illustrating how to attach the handler to the lifecycle event.
5. Suggest tests to validate transitions (happy path and failure cases) and monitoring signals to detect stuck states.
6. Summarize deployment recommendations (atomicity, idempotency, and error handling best practices).

## Example Usage
- "Map my document approval states to lifecycle events and handlers."
- "Create a state→event→hook table for an order processing system."
- "Show handler examples for transitions from pending→approved and pending→rejected."

## Note
This skill focuses on design and mapping; runtime enforcement and code execution must be handled in your systems.