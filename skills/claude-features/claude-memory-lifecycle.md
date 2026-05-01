# Connection-Based Memory Lifecycle

## Description
This skill manages memory entries in Claude Code by tracking their connections. Entries linked to other knowledge persist, while isolated entries gradually fade. It is implemented entirely using lifecycle hooks to maintain relevant memory efficiently.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (relies on lifecycle hooks exclusive to Claude Code)

## Instructions
1. Activate the memory lifecycle hooks within Claude Code.
2. Monitor memory entries for connections to other knowledge.
3. Retain entries that have active connections.
4. Gradually remove or fade isolated entries without connections.
5. Continuously update memory state based on connection changes.

## Example Usage
- "Manage memory lifecycle for connected knowledge"
- "Retain linked memory entries and fade isolated ones"
- "Apply connection-based memory pruning"

## Note
This skill requires Claude Code environment due to its dependence on lifecycle hooks and is not available on Claude Desktop.