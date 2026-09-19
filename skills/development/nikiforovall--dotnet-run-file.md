# Run a .NET File (dotnet-run-file)

## Description
A helper skill that runs a single .NET source file or small program using the dotnet toolchain. Use it when you want the agent to execute a C#/.NET file, capture output, and return runtime logs or errors.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires executing dotnet CLI and access to the filesystem to compile/run code)

## Instructions
1. Confirm the file path, required runtime (SDK) version, and any command-line arguments or environment variables the program needs.
2. Verify the execution environment: check dotnet SDK availability and report the version. If missing, report that execution cannot proceed.
3. If the file is a single-script-compatible C# file, run it using an appropriate command (e.g., a temporary project or dotnet-script if available). For full projects, run dotnet run in the project directory.
4. Capture stdout and stderr, the exit code, and any compilation errors. If compilation fails, return the relevant compiler messages and suggest fixes.
5. If requested, run with provided arguments, timeout limits, or input redirection; otherwise use safe defaults.
6. Return a concise execution report: success/failure, exit code, truncated logs (flag large outputs), and suggested next steps for errors.

## Example Usage
- "Run this Program.cs with arguments 'input.txt' and return the output."
- "Compile and run the project in ./MyApp and show any compile errors."
- "Execute the single-file script and capture stderr and exit code."

## Note
Executing code can be unsafe. Confirm user intent before running untrusted code and enforce timeouts and resource limits. This skill requires a Code-enabled agent with access to the dotnet SDK and the filesystem.