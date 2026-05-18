# Post-Tool Use Auditor

## Description
Captures and logs the results of all tool executions after completion. Generates structured JSON audit logs per session to support debugging, compliance, and traceability.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (uses lifecycle hooks for post-tool execution logging)

## Instructions
1. Enable the post-tool use auditor hook in Claude Code.
2. After each tool completes, capture its output and metadata.
3. Format the captured data into structured JSON audit logs.
4. Store or transmit logs for compliance and debugging purposes.
5. Review logs to monitor tool usage and results.

## Example Usage
- "Start post-tool use auditing"
- "Log all tool results after execution"
- "Generate JSON audit trails for tool sessions"

## Note
Requires Claude Code environment due to dependency on lifecycle hooks.