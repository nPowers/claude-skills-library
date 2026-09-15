# Conductor Workflow Manager

## Description
Assist with designing, reviewing, and generating Netflix Conductor workflow and task definitions. Use this skill to produce workflow JSON, task definitions, sample API calls for registration, and troubleshooting tips for common validation errors.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask for the Conductor API endpoint, Conductor version (if known), and whether the user wants a new workflow or modifications to an existing one.
2. Gather workflow details: name, version, owner, description, input/output parameters, task sequence (simple tasks, fork/join, decision tasks, sub-workflows), error handling, and retry strategies.
3. Produce a complete workflow definition in JSON, including tasks array, input/output mappings, defaultRetryParameters, and any required task definitions. Use clear, descriptive task names and include comments/explanations inline (as plain text near the JSON) if helpful.
4. Provide sample curl or HTTP requests to register or update the workflow via the Conductor REST API (e.g., POST /metadata/workflow) and to start an execution, with placeholders for endpoint, auth headers, and payload.
5. List common validation issues (missing task definitions, incorrect input mapping, circular dependencies) and offer localized testing suggestions such as registering in a staging Conductor instance and using the UI or API to run sample executions.

## Example Usage
- "Draft a Conductor workflow JSON that runs ETL_task, then a parallel set of analysis tasks, and finally aggregates results"
- "Give me curl commands to register a workflow definition and start an execution"
- "Validate this workflow JSON and point out potential mapping errors"

## Note
This skill generates definitions and example API calls; it does not call the Conductor API or modify server state. The user must supply the endpoint and credentials to perform registration or execution.
