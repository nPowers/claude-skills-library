# C# Code Authoring (Foundry-style)

## Description
Focused on producing production-ready C# code with clear structure, consistent naming, and maintainable patterns. Use it when you need feature implementations, API endpoints, or library components written to professional standards.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Collect requirements: clarify feature goals, input/output, performance targets, and security or compliance constraints.
2. Ask which architecture or patterns to prefer (e.g., layered, hexagonal, clean architecture) and which dependency injection/container to use.
3. Provide a high-level design and list of public interfaces or endpoints for the user to approve.
4. Generate the requested C# files (controllers, services, models, interfaces) with comments and XML documentation where appropriate.
5. Include configuration snippets (appsettings.json), DI registration, and minimal startup wiring for the chosen .NET runtime.
6. Add unit/integration test examples, and include sample requests (HTTP curl/Postman) if applicable.
7. Highlight potential breaking changes and migration notes if the code touches public APIs.

## Example Usage
- "Implement an ASP.NET Core POST endpoint that accepts order DTOs and validates them"
- "Generate a repository and service layer for product data using Dapper"
- "Create DTOs and AutoMapper profiles for these domain models"

## Note
The skill generates ready-to-review code but does not run builds or tests. Confirm runtime version and dependencies before integrating into a live project.
