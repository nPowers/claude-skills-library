# S3 Lifecycle Configuration Generator

## Description
Generate Amazon S3 lifecycle configurations (XML and JSON) to transition, expire, or manage object versions. Use this skill to produce ready-to-apply lifecycle rules, validate rule interactions, and get example aws CLI commands and best-practice checks.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask the user for the target bucket name(s), object prefixes or tags, and whether versioning is enabled.
2. Clarify desired lifecycle actions and timing (e.g., transition to STANDARD_IA after X days, move to Glacier after Y days, expire after Z days, delete noncurrent versions after N days, abort multipart uploads after M days).
3. Produce both a JSON and an XML representation of the lifecycle configuration, including rule Ids, filters, status, actions, and noncurrent version rules where applicable.
4. Provide a sample aws CLI command to apply the configuration (aws s3api put-bucket-lifecycle-configuration ...) with placeholders for bucket name and file path, and explain required IAM permissions.
5. Call out common validation checks and pitfalls (overlapping rules, unintended deletions, versioning implications, rule ordering) and recommend a test plan such as applying to a staging bucket and monitoring object transitions.

## Example Usage
- "Create an S3 lifecycle policy to move logs to Glacier after 30 days and delete them after 365 days"
- "Show me an S3 lifecycle XML for a versioned bucket that expires old versions after 180 days"
- "What aws CLI command applies a lifecycle config to bucket 'my-app-logs'?"

## Note
This skill generates configuration and commands but does not execute changes. Always validate in a non-production environment and ensure appropriate IAM permissions before applying.
