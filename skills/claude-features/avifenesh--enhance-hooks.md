# Enhance Hooks

## Description
A guidance skill that standardizes and enriches incoming hook payloads. Use it to validate, normalize, and produce structured JSON and human-readable summaries for webhook or hook-style inputs.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask the user for the raw hook payload or accept the payload provided in the activation context.
2. Validate required fields (timestamp, event type, id, payload) and list any missing or malformed entries.
3. Normalize field names and types (e.g., convert timestamps to ISO 8601, unify event name casing).
4. Extract key entities and values, then produce two outputs: a compact machine-friendly JSON object and a short human-readable summary.
5. Suggest next steps or follow-up actions (e.g., trigger a workflow, log the event, request more data) and include any recommended guardrails.

## Example Usage
- "Enhance this hook payload: {payload}"
- "Normalize and summarize webhook data for my monitoring pipeline"
- "Validate hook payload and return structured JSON"

## Note
Designed for conversational enrichment and formatting of hook data; it does not perform network calls or execute hooks against external systems.