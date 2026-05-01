# Session Memory Manager

## Description
Manage and preserve important contextual information across Claude Code sessions by using structured memory files. This skill enables tracking of entities, logging decisions, and summarizing context to maintain continuity in complex workflows.

## Platforms
- Claude Desktop: Not Supported (requires file system access)
- Claude Code: Supported

## Instructions
1. When activated, identify key entities and decisions within the current session.
2. Store this information in structured memory files for persistence.
3. Summarize the session context periodically to maintain a concise overview.
4. On session restart, recall stored memory files to restore context.
5. Use the recalled context to inform ongoing tasks and decisions.

## Example Usage
- "Save current session context"
- "Recall previous session memory"
- "Summarize important entities and decisions"

## Note
This skill requires file system access to read and write memory files and thus is only available in Claude Code.