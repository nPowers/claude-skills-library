# Maven Build Lifecycle Guide

## Description
A compact reference to the Maven build lifecycle: phases, where plugins bind, how to customize or extend lifecycle behavior, and debugging tips for build failures. Use it when configuring builds, writing plugins, or diagnosing multi-module issues.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask whether the user needs a conceptual overview, plugin configuration examples, custom lifecycle instructions, or debugging help.
2. Summarize the standard lifecycle phases (validate, compile, test, package, verify, install, deploy) and explain typical responsibilities for each.
3. Show how to bind a plugin to a specific phase with a short pom.xml snippet and explain common plugin configuration options.
4. Describe how to create and register a custom lifecycle or profile and when to use profiles vs. custom lifecycle bindings.
5. Provide troubleshooting steps for common issues (dependency resolution, plugin version conflicts, reactor build ordering) and tips for diagnosing with -X and -D flags.

## Example Usage
- "Explain Maven's default build phases"
- "Show a pom snippet binding a plugin to the package phase"
- "How do I debug multi-module build order problems?"

## Note
Advice is geared to standard Maven usage; for specialized build systems or CI integrations, adapt commands and settings to your environment.