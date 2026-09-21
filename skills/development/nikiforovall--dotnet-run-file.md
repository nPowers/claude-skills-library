# Run .NET File

## Description
Run a single .NET/C# source file or project using the dotnet CLI and return execution output. Use this skill when you need to build and execute code, capture stdout/stderr, or test a small .NET program directly.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (Code-only: requires file system access and the dotnet CLI to build and execute files)

## Instructions
1. Ask the user for the path to the C# file or project, the target framework (if relevant), and any command-line arguments.
2. Confirm that the requested file or project exists and that they consent to executing it (warn about running untrusted code).
3. Detect whether the input is a standalone .cs file, a csproj-based project, or a script; choose the appropriate command (e.g., `dotnet run` for projects, `dotnet script` or `dotnet run` with a temporary project for single files).
4. Execute the selected dotnet command, capturing stdout, stderr, exit code, and execution time.
5. Return the captured output and any errors to the user. If compilation errors occur, present the compiler messages and suggest likely fixes.
6. If requested, produce a reproducible command snippet and instructions to run the same file locally (including required SDK version and environment variables).

## Example Usage
- 'Run Program.cs with input "hello"'
- 'Execute the project at ./src/MyApp.csproj'
- 'Compile and run this C# script file'

## Note
This skill executes code on the host environment; ensure the user understands security risks and that the runtime (dotnet SDK) is available on the machine running the command.