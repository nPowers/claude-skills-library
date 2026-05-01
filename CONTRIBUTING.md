# Contributing to Claude Skills Library

Thank you for your interest in contributing. This library is maintained weekly via an automated pipeline, but human contributions are welcome.

## Skill Format

Every skill must follow this exact structure:

```markdown
# Skill Display Name

## Description
1–3 sentences describing what the skill does, when to use it, and its key capabilities.

## Platforms
- Claude Desktop: Supported / Not Supported
- Claude Code: Supported / Not Supported

## Instructions
1. Step one
2. Step two
3. Step three

## Example Usage
- "Example trigger phrase 1"
- "Example trigger phrase 2"
- "Example trigger phrase 3"

## Note
Any important caveats, limitations, or disclaimers.
```

## Platform Rules

- Skills requiring **file system access, Bash execution, or sub-agent spawning** → Claude Code only
- Skills requiring only **knowledge and conversation** → Both platforms
- Skills requiring an **MCP server** → Claude Desktop (if MCP server is installed)
- **Orchestrator agents** that coordinate sub-agents → Claude Code only

## Submitting a Skill

1. Fork the repository
2. Add your skill file to the appropriate `skills/` subfolder
3. Follow the format above exactly
4. Submit a PR with a brief description of what the skill does

## Review Criteria

Skills are accepted if they:
- Follow the format exactly
- Have a clear, specific use case
- Are not duplicates of existing skills
- Include accurate platform compatibility flags
- Are original writing (not copied verbatim from another source)
