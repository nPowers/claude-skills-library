# Hook Templates & Patterns Library

## Description
Provide a curated set of hook templates and design patterns for common tasks (authentication, caching, retries, observability). Use when you want a starting point or consistent approach across projects.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask what category of hook the user needs (e.g., auth, persistence, HTTP retry, telemetry).
2. Present 2–3 patterns with trade-offs and recommended contexts for each pattern.
3. Upon selection, generate a complete template with code, comments, configuration options, and integration notes.
4. Include example tests, CI suggestions, and monitoring hooks (metrics/logging) where applicable.
5. Offer conversion guidance between frameworks or languages if requested (e.g., JS -> TS, Node -> serverless).

## Example Usage
- "Show me templates for caching hooks for API requests."
- "I need a retryable HTTP hook with exponential backoff."
- "Provide an authentication hook pattern that works with OAuth2 refresh tokens."

## Note
Templates aim to standardize common solutions but may require customization for your application's security and performance requirements.