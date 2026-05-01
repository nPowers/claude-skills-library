# Post-Tool Use Auditor

## Description
Captures and logs the results of all tool executions to create detailed audit trails. Generates structured JSON logs per session to support debugging, compliance, and reporting requirements.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (uses lifecycle hooks for post-tool execution capture)

## Instructions
1. Activate the post-tool use auditor hook in Claude Code.
2. After each tool execution, capture the output and metadata.
3. Format the captured data into structured JSON audit logs.
4. Store or transmit logs for compliance and debugging.
5. Provide summaries or reports based on logged data as needed.

## Example Usage
- "Log tool results after execution"
- "Generate JSON audit trails for tool use"
- "Capture tool outputs for compliance"

## Note
This skill requires Claude Code environment due to its dependency on lifecycle hooks for capturing tool results.