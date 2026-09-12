# Groundwork — Claude Code Harness Starter

## Description
Groundwork is a batteries-included starter harness for Claude Code projects that emphasizes safe-by-default behavior: guardrails, a wiki-grounded quality loop, and an integrated memory lifecycle to help teams scaffold reliable agent workflows quickly.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires local install to scaffold harness, guardrails, and memory lifecycle)

## Instructions
1. Clone the Groundwork repository and read the quickstart to understand the harness components (guardrails, wiki grounding, memory lifecycle).
2. Install and initialize a new project scaffold using Groundwork's setup commands or templates.
3. Configure guardrail policies, the wiki grounding source (local documentation), and memory lifecycle parameters to match your project needs.
4. Integrate Groundwork into your Claude Code lifecycle so the harness enforces guardrails during run, records outputs to the wiki-grounded quality loop, and maintains memory decay.
5. Run a sample job to validate that guardrails trigger correctly and that the wiki-grounded loop collects quality signals.
6. Iterate on policies and memory settings as your workflow matures.

## Example Usage
- "Scaffold a new Claude Code project using Groundwork with default guardrails"
- "Enable wiki-grounding and point Groundwork at the local project docs"
- "Run the quality loop and review guardrail-triggered items"

## Note
Groundwork is intended as a local harness starter and requires filesystem and runtime access to install and enforce guardrails. It provides a secure default posture but should be customized for project-specific safety and privacy requirements.