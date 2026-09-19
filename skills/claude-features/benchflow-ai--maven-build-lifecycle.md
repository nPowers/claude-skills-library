# Maven Build Lifecycle Advisor

## Description
Explain and customize the Maven build lifecycle and recommend where to attach hooks, plugins, or automation. Use this skill to map goals to lifecycle phases, produce POM snippets, and propose pre/post-build checks and validations.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user for the project type (jar, war, multi-module), current POM layout, and desired customizations (checks, artifact signing, deployment steps).
2. Summarize the standard Maven lifecycle phases relevant to the project (validate, compile, test, package, verify, install, deploy) and common goals bound to each.
3. Recommend where to attach custom plugins or lifecycle hooks (pre-commit checks, test coverage gates, artifact signing) and provide short POM snippets illustrating plugin configuration.
4. Provide sample pre/post-build scripts or plugin configurations (pseudocode or XML snippets) and explain failure handling and idempotency considerations.
5. Offer a checklist for CI integration (cache strategy, parallel builds, artifact promotion, credentials handling) and test cases to validate the build lifecycle.
6. Advise on observability: build logs, artifact checksums, and rollback strategies for faulty releases.

## Example Usage
- "Show me where to bind a code-quality plugin into the Maven lifecycle for a multi-module project."
- "Create a POM snippet to run integration tests in the verify phase and sign artifacts in deploy."
- "Recommend CI best practices for Maven builds and artifact promotion."

## Note
This advisor provides configuration examples and best practices. Running builds or changing your CI/CD pipelines must be done in your build environment.