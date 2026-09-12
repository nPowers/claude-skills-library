# Autonomous Engineering: AI Agent Delivery Lifecycle

## Description
Implements an autonomous software delivery workflow tailored for AI agents. Use this skill to break the agent lifecycle into bounded, resumable phases with deterministic enforcement hooks and automated self-improvement loops.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (Code-only — executes repository operations, creates checkpoints, and runs lifecycle phases)

## Instructions
1. Identify the project repository, target agent, and desired high-level objective before activating the skill.
2. Initialize the delivery lifecycle: create a phase manifest that enumerates phases (design, implementation, test, validation, deploy) and required invariants for each phase.
3. Install deterministic enforcement hooks: register pre- and post-phase checks (linting, test coverage, security scans, performance gates) that must pass to proceed.
4. Create checkpointing points at phase boundaries: persist artifacts, metadata, and state so execution can be resumed deterministically from any checkpoint.
5. Execute phases sequentially or in parallel as defined by the manifest; record deterministic inputs, actions, and outputs to enable reproducible runs.
6. On failure, run the self-correction routine: analyze failed checks, synthesize targeted fixes (code edits, config changes, or test adjustments), apply the minimal change, and re-run the affected phase from the nearest checkpoint.
7. Maintain a learn/map loop: after each successful delivery, extract lessons (fix patterns, flaky tests, performance regressions), update the manifest, and refine enforcement hooks and heuristics for future runs.
8. Produce a summary report after each delivery with phase outcomes, checkpoint locations, remediation actions taken, and suggested improvements for the next cycle.
9. Integrate with CI/CD and version control: push checkpoints and artifacts to the repository or artifact store, and add reproducible run metadata to the commit history or pipeline logs.
10. When asked to resume or reproduce, locate the named checkpoint and replay the deterministic actions recorded for that checkpoint to reach the same outcome.

## Example Usage
- "Start autonomous delivery for repository <repo-url> with objective: deploy agent v1.2"
- "Initialize lifecycle manifest for agent 'dialog-manager' with phases: design, implement, test, validate, deploy"
- "Resume delivery from checkpoint 'phase-3-integration-test' and apply self-correction loop"

## Note
Requires Claude Code environment because it performs repository access, artifact checkpointing, and execution of lifecycle operations. Ensure proper repository permissions and security review before enabling automated code changes.