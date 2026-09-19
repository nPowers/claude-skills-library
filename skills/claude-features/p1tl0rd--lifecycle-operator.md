# Lifecycle Operator Patterns & Guidance

## Description
Explains design patterns, common CRD/reconcile approaches, and best practices for building or operating a lifecycle operator (e.g., Kubernetes operator). Use it to design controllers, write CRDs, set RBAC, and debug reconcile loops.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask the user which platform and language they are targeting (Kubernetes, OpenShift; Go, Python, etc.).
2. Summarize the operator responsibilities and typical state machine for managed resources.
3. Provide example CRD schema outlines and a concise reconcile loop pseudocode showing idempotency and error handling.
4. List essential RBAC entries, common controller-runtime patterns, and testing strategies (unit, integration, e2e).
5. Offer debugging steps for common issues (event storms, infinite requeues, transient failures), plus monitoring and observability recommendations.

## Example Usage
- "Design a reconcile loop for a lifecycle operator managing backups"
- "Show a CRD sketch and RBAC needed for a lifecycle controller"
- "How do I test an operator's state transitions?"

## Note
Examples are illustrative pseudocode and patterns; adapt generated snippets to your operator SDK and cluster setup before deploying.