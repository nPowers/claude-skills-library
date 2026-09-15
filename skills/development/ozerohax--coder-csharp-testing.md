# C# Testing & QA Coder

## Description
Create unit, integration, and end-to-end tests for C# projects and advise on testability, mocking, and CI integration. Use this skill to build reliable test suites and reduce flakiness in automated pipelines.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask which test framework to use (xUnit, NUnit, MSTest), the mocking library preference (Moq, NSubstitute), and CI system in use.
2. Request project structure or the specific code under test; ask for interfaces to mock and external dependencies to isolate.
3. Produce example unit tests covering normal cases, edge cases, and error conditions; include setup and teardown code as needed.
4. Provide integration test patterns for services, databases, and HTTP endpoints, showing how to use in-memory stores or containers for isolation.
5. Offer strategies to reduce flakiness: deterministic data, time control (clock abstractions), retry decorators, and parallel test settings.
6. Include examples of test doubles, fixtures, parameterized tests, and how to measure coverage and interpret results.
7. Add CI snippets (GitHub Actions, Azure DevOps) to run tests, collect coverage, and publish results.

## Example Usage
- "Write xUnit tests for this service method that calls an external API"
- "Show how to integration test EF Core with an in-memory provider and Docker SQL"
- "Create a GitHub Actions workflow to run tests and publish code coverage"

## Note
Tests are most effective when run in an environment close to production; prefer integration testing with ephemeral infrastructure for end-to-end confidence.