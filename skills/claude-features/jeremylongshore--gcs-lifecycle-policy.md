# GCS Lifecycle Policy Generator

## Description
Create Google Cloud Storage lifecycle policies in JSON to transition storage classes, delete objects, or manage noncurrent versions. Use this skill to produce policy JSON, example gcloud commands, and guidance on filters and lifecycle conditions.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask which bucket(s), object name prefixes, and labels/tags the policy should target, and whether object versioning (Object Versioning) is enabled.
2. Confirm desired lifecycle actions (changeStorageClass, delete, setStorageClass) and timing or conditions (age, createdBefore, isLive, matchesStorageClass, numberOfNewerVersions).
3. Generate a complete GCS lifecycle policy JSON document that includes rule names, conditions, and actions; include at least one example with multiple rules and a brief explanation of each field.
4. Provide an example gcloud command to set the lifecycle policy (e.g., gsutil lifecycle set or gcloud alpha storage buckets update) and note required IAM roles.
5. Describe typical validation steps and pitfalls (conflicting rules, versioning interactions, retention policies) and recommend testing in a staging bucket.

## Example Usage
- "Produce a GCS lifecycle policy that moves objects to Nearline after 60 days and deletes after 730 days"
- "Show me a JSON lifecycle policy for a bucket with versioning enabled that deletes noncurrent versions after 90 days"
- "How do I apply a lifecycle policy to bucket 'my-data-bucket' using gsutil?"

## Note
This skill provides configuration and commands only; it does not perform changes. Verify IAM roles and test policies in non-production buckets first.
