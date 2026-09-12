# MDKB — Local Memory + Code Search

## Description
MDKB provides a local, privacy-first memory and search layer for coding assistants: hybrid BM25 + semantic retrieval, tree-sitter–based code intelligence for many languages, and a persistent memory store with confidence decay. It integrates via CLI, lifecycle hooks, and MCP to augment Claude Code and Codex without cloud APIs.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires local indexing, database files, and CLI/MCP integration)

## Instructions
1. Clone the MDKB repository and follow the README to install dependencies and start the local indexing service.
2. Prepare a corpus (codebase, notes, docs) and run MDKB's indexing pipeline to populate the BM25 + semantic store and language-aware code indexes.
3. Configure the persistence and confidence-decay parameters to suit your retention needs.
4. Integrate MDKB with Claude Code or Codex via the provided CLI hooks or MCP connector so queries can be routed to the local memory/search layer.
5. Use the MDKB query API to surface relevant memories, code snippets, and references during agent runs; use tree-sitter results for language-aware code lookups.
6. Periodically re-index or tune decay settings as your codebase and knowledge evolve.

## Example Usage
- "Index my repository with MDKB and connect it to Claude Code via the MCP connector"
- "Query MDKB for prior fixes related to 'memory leak' in Python modules"
- "Enable MDKB as a lifecycle pre-check to suggest relevant code examples before generation"

## Note
MDKB is designed for fully local operation and requires filesystem access to index and store data. No cloud API calls are required by default; follow the repo docs for configuration and language support.