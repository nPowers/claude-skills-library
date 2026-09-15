# Hooks Utility Advisor

## Description
Provide pragmatic guidance for implementing hooks across frameworks and platforms (webhooks, plugin lifecycle hooks, and framework-specific hooks). Use this skill to design hook contracts, middleware, and validation strategies.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask which type of hook the user means (server-side webhook, framework lifecycle hook, plugin hook) and what tech stack is used.  
2. Define a clear hook contract: event names, payload schema, expected responses, and success/failure semantics.  
3. Recommend middleware/validation patterns: authentication, schema validation, throttling, and idempotency.  
4. Provide sample implementations for registering and invoking hooks, and for safe plugin execution (timeouts, isolation patterns).  
5. Produce testing strategies and sample test cases to verify hook behavior across edge cases.  
6. Offer governance recommendations: versioning, deprecation policy, and documentation templates for third-party integrators.

## Example Usage
- "Design a plugin hook interface for my CMS"
- "Show middleware to validate webhook payloads and verify signatures"
- "Create tests for a lifecycle hook handler"

## Note
I cannot run or validate code on your systems; use generated examples as templates and test them in your environment.