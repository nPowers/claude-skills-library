# Enhance Hooks Builder

## Description
Create, refine, and test "enhance" hooks that modify or augment Claude responses. Use this skill when you want concise hook specifications, example code snippets, and integration checklists for response transformation, metadata enrichment, or conditional routing.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user to describe the desired transformation or enrichment (goal, input examples, expected output, performance constraints).
2. Determine which type of enhance hook fits the need (pre-processing, in-flight modification, post-processing, or metadata-only) and name the hook phase.
3. Produce a short hook specification: inputs, outputs, triggers, and failure modes (1–3 paragraphs).
4. Provide a minimal implementation example in clear pseudocode or the target platform's hook format (show sample input → transformed output).
5. Suggest test cases (3 examples) and a simple validation checklist to ensure correctness and safety.
6. Offer an integration checklist with steps to register the hook, required permissions, and monitoring/logging recommendations.

## Example Usage
- "Create an enhance hook to summarize customer emails into three bullet points."
- "Generate an enhance hook that rewrites responses to be more formal when the user is a business contact."
- "Show a hook that appends anonymized analytics metadata to every output."

## Note
This skill provides design guidance and example code snippets; actual deployment and runtime testing must be done in your environment.