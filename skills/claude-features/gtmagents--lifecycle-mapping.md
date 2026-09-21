# Lifecycle Mapping

## Description
Translate a sequence of lifecycle events into a clear, stage-based map. Use this to convert raw event logs or descriptions into structured stage transitions, timelines, and recommended triggers.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Request or ingest the list of lifecycle events, timestamps, and any available metadata.
2. Normalize event names and group them into logical stages (e.g., init, deploy, running, upgrade, retire).
3. Build a stage-transition map that shows allowed transitions, typical timing, and important invariants.
4. Output a machine-readable representation (JSON with stages, transitions, and sample triggers) and a concise human summary.
5. Provide suggested monitoring checks, alerts, and remediation steps for each stage.

## Example Usage
- "Map these lifecycle events into stages and transitions"
- "Create a lifecycle map for this application's event log"
- "Suggest monitoring rules for each lifecycle stage"

## Note
Produces analysis and recommendations only; it does not modify running systems or execute automated transitions.