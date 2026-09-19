# Document Lifecycle Planner

## Description
Design document lifecycle policies, metadata schemas, and automation hooks for content from draft to archive. Use this skill to define states, transitions, review rules, and sample automation for publishing workflows.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask what types of documents and stakeholders are involved (e.g., blog posts, policies, reviewers, approvers).
2. Define lifecycle states (draft, review, approved, published, archived) and list allowed transitions and triggers.
3. Propose a metadata schema for each state (required fields, timestamps, reviewer IDs, versioning info).
4. Provide example automation rules and corresponding hook handlers (e.g., notify reviewer on state change, auto-archive after N days).
5. Supply short sample implementations or pseudocode for each automation rule and a small testing checklist.
6. Recommend governance controls: access rules, retention policies, audit logging, and rollback procedures.

## Example Usage
- "Help me design a review workflow and metadata schema for marketing articles."
- "Create automation that notifies a reviewer when a draft is ready."
- "Suggest retention and archive rules for internal policy documents."

## Note
Outputs are design artifacts and sample code; actual enforcement and storage integration require implementation in your environment.