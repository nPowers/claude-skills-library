# Python Runner (Execute Code)

## Description
Execute Python scripts or snippets in an isolated runtime and return stdout, stderr, exit codes, and captured artifacts. Use this skill when you need actual program output, test results, or live debugging information from running code.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires execution environment for running Python)

## Instructions
1. Ask the user for the exact code, entrypoint filename, or command to run and the target Python version/environment details.
2. Verify any external requirements (files, network access, environment variables) and request permission if filesystem or network access is needed.
3. Run the code in an isolated environment, capturing stdout, stderr, exit code, and any generated files; limit execution time and resource use.
4. Return a concise run report: exit code, first N lines of stdout/stderr, and links or listings for produced artifacts.
5. If execution fails, include the full traceback and suggest minimal reproducible fixes or test snippets to isolate the error.
6. For long-running jobs, provide progress updates or abort guidance and summarize results when finished.
7. If input is ambiguous, ask clarifying questions (e.g., required input files or expected behavior) before executing.

## Example Usage
- "Execute this script and show stdout and stderr"
- "Run the test suite and return failing tests with traces"
- "Run my snippet with Python 3.10 and show the output"

## Note
This skill requires a Code execution environment. Exercise caution with untrusted code—review for unsafe operations before running and obtain explicit consent for filesystem or network access.