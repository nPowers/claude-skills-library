# Post-Tool Use Auditor

## Description
Captures and logs results of all tool executions after completion to create audit trails, assist debugging, and support compliance reporting. Produces structured JSON audit logs per session.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires post-execution hook and logging capabilities)

## Instructions
1. Install the post-tool use auditor hook in Claude Code.
2. Capture tool results immediately after execution.
3. Generate structured JSON logs detailing tool usage and outcomes.
4. Store logs for auditing, debugging, and compliance purposes.

## Example Usage
- "Log all tool results after use."
- "Generate JSON audit trails for tool sessions."
- "Review tool execution logs for compliance."

## Note
Requires lifecycle hooks and logging infrastructure, so it is only available in Claude Code.