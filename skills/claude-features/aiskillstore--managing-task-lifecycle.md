# Managing Task Lifecycle (Workflows & Automation)

## Description
Guidance for designing and operating task lifecycles in teams or automation systems: define states, triggers, transitions, and observability. Use it to create clear workflows, reduce bottlenecks, and map tasks to tooling or automation rules.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask what type of tasks or system the user means (engineering tickets, CI jobs, background workers, etc.).
2. Propose a concise state model (e.g., New -> In Progress -> Blocked -> Review -> Done -> Archived) tailored to the scenario.
3. Recommend triggers, guards, and transition rules; include who/what can trigger each transition.
4. Map the model to practical tools (issue trackers, workflow engines, automation scripts) and give example automation rules or webhooks.
5. Provide monitoring and KPIs to track lifecycle health (cycle time, queue length, failure rate) and troubleshooting tips for common failure modes.

## Example Usage
- "Design a task lifecycle for an engineering team"
- "Map task states to Jira automation rules"
- "Recommend KPIs to monitor workflow health"

## Note
Suggested models are templates; refine state names and transitions to match your organisation's policies and tooling.