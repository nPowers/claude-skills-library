# Maven Build Lifecycle — The Bushido Collective

## Description
Provides a compact, actionable explanation of Maven's build lifecycle and pragmatic advice for mapping lifecycle phases to build goals, plugins, and commands. Use this skill for troubleshooting build failures or designing build pipelines.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user for the specific Maven goal, POM excerpts, or error output they want help with.
2. Give a succinct breakdown of the standard lifecycle phases (validate, compile, test, package, verify, install, deploy) and the typical outcomes of running each phase.
3. For the user's goal, identify which plugins are usually invoked and what configuration elements in the POM affect behavior (plugin executions, profiles, properties).
4. Provide example CLI invocations appropriate to the situation and explain commonly used flags and environment variables.
5. Recommend debugging steps (mvn -X, mvn -DskipTests, mvn help:effective-pom) and specific POM checks (dependency versions, parent POM overrides, pluginManagement).
6. Suggest strategies for CI integration, caching, and incremental builds to improve reliability and performance.
7. Finish with a brief list of useful references and how to provide precise inputs (POM snippets, logs) for deeper help.

## Example Usage
- "What does mvn verify do and when should I run it?"
- "My deploy step fails with a permission error — what should I check?"
- "How do I see the effective plugin configuration for my project?"

## Note
I can't execute Maven or view your files here; paste key POM sections or errors for tailored advice.