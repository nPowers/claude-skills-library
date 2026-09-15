# Hooks System Manager

## Description
Manage and design hook systems (webhooks and internal event hooks). Use this skill to plan, secure, test, and produce handler code and deployment checklists for hook-based integrations.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask what kind of hooks the user needs (external webhooks, internal event hooks, or both) and what systems or services are involved.  
2. Identify required features: authentication, retry/backoff, idempotency, signing, rate limits, payload schema, and delivery guarantees.  
3. Propose a concise architecture: endpoints, event taxonomy, queueing, storage of events, monitoring/metrics, and optional broker (e.g., Kafka, SQS).  
4. Generate example handler implementations in requested language(s) (Node/Express, Python/Flask, Go, etc.), including validation, signature verification, and idempotency keys.  
5. Provide test cases and curl/postman examples to simulate deliveries, and suggest monitoring/logging instrumentation.  
6. Deliver a deployment and rollout checklist: secure TLS, rotated signing keys, retry policies, versioning, and backward compatibility steps.  
7. If asked, create a short troubleshooting guide for common delivery failures and recommended alerts.

## Example Usage
- "Design a secure webhook system for my e-commerce platform"
- "Generate Node.js webhook handler with HMAC signature verification"
- "Provide a testing plan and curl examples for webhook deliveries"

## Note
I cannot deploy or run code; I produce patterns, example code, and configuration you can apply and test in your environment.