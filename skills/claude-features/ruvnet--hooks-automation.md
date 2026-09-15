# Hooks Automation Builder

## Description
Create automation workflows triggered by hooks or events. Use this skill to map events to actions, design retry and error policies, and produce integration/configuration snippets for automation platforms.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask for the source event(s), target actions, and preferred automation platform(s) (e.g., Zapier, n8n, Workflows, custom server).  
2. Clarify event payloads, authentication methods, and SLA requirements.  
3. Propose an automation flow diagram and describe each step (trigger, transformations, filters, actions, error handling).  
4. Generate concrete configuration snippets or recipes for the requested automation tool or provide generic webhook-to-service examples (HTTP calls, retries, exponential backoff).  
5. Recommend monitoring, alerting, and idempotency measures for reliable delivery.  
6. Provide tests and sample payloads to validate end-to-end behavior and a rollback plan for failed automations.

## Example Usage
- "Create an automation: when order.created -> post to Slack and update CRM"
- "Show an n8n workflow for converting webhook payloads to database inserts"
- "Generate retry/backoff policy and sample config for failed deliveries"

## Note
I generate configurations and code samples but cannot execute or deploy automations; credentials or live connections are not accessed.