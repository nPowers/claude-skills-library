# Cortex Memory MCP

## Description
Cortex is a local-first, persistent memory store and MCP implementation designed for Claude, Codex, and other local LLM hosts. It provides hybrid retrieval, decay-based consolidation, and reproducible benchmarks to support long-lived agent context and retrieval-augmented workflows.

## Platforms
- Claude Desktop: Supported (if a Cortex MCP server is installed and configured)
- Claude Code: Supported

## Instructions
1. Install and start the Cortex server (SQLite/Postgres backend) on your machine or host following the repository instructions.
2. Configure the MCP endpoint and credentials in your Claude or local LLM client so the assistant can query and store memory.
3. Decide on memory policies: retention windows, decay rates, consolidation schedules, and which namespaces to persist.
4. Enable optional lifecycle hooks in Claude to automatically store summaries, task state, or important artifacts after sessions.
5. Use the hybrid retrieval settings to combine vector search and metadata filters; test retrieval quality with representative queries.
6. Run provided benchmarks to establish baseline recall and consolidation behavior; adjust decay and consolidation parameters as needed.
7. When requesting assistance from Claude, indicate whether to read from Cortex, write new episodic memories, or consolidate existing entries.

## Example Usage
- "Connect this session to my Cortex MCP and store a summary of the project plan"
- "Retrieve the last three design decisions about the payments module from Cortex"
- "Run Cortex benchmarks and suggest consolidation settings for weekly meetings"

## Note
Requires a running Cortex MCP server and network or local socket access. Data persistence and retention are controlled by your Cortex configuration; secure storage is the user's responsibility.