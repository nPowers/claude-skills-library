# C# Script Writer (Windmill Labs)

## Description
Generate concise, runnable C# scripts and small utilities for .NET runtimes. Use this when you need scaffolded script files, command-line utilities, or single-file examples with clear run instructions and minimal dependencies.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user for the script's purpose, target .NET/runtime (Core/Framework), and any input parameters or environment constraints.
2. Confirm required dependencies, target framework version, and whether the script must be single-file or may include multiple files/CSProj.
3. Produce a minimal working script with clear comments, a short README section at the top, and example input/output.
4. Provide both a concise version (as short as possible) and an expanded version with error handling and logging.
5. Include run and build commands for Windows, macOS, and Linux (dotnet CLI or appropriate runtime), and note any required SDK installation.
6. List external NuGet packages used and the command to add them, and explain why each package is needed.
7. Offer a simple test or example invocation and suggest one or two improvements or hardening steps (configuration, secrets handling).

## Example Usage
- "Write a C# script that reads a CSV and prints the top 10 most frequent values"
- "Create a single-file C# utility that downloads a URL and saves it with retries"
- "Generate a .NET 6 console script to POST JSON to a webhook and log responses"

## Note
This skill produces code for review — always validate and run generated scripts in a safe environment before using with sensitive data.