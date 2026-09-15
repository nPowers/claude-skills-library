# Python REPL Runner

## Description
Execute Python snippets interactively and return live output, stdout/stderr, and exit status. Use this skill when you want immediate execution results, iterative experimentation, or to validate small scripts.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires runtime to execute code and capture output)

## Instructions
1. Prompt the user for the Python code to run and ask about desired Python version and any required packages.
2. Validate the snippet for obvious issues (syntax errors, infinite loops) and ask for confirmation to run if necessary.
3. Execute the code in an isolated REPL environment and capture stdout, stderr, return value, and execution time.
4. Return the exact output and any traceback, then provide a concise diagnosis and suggestions for fixes if exceptions occurred.
5. If output is large, provide a short summary and offer to display full output or save it to a file (when file access is available in the environment).
6. Support iterative edits: accept user changes, rerun, and diff outputs or explain behavioral differences.
7. Respect resource limits and timeouts; warn the user about long-running or resource-intensive code.

## Example Usage
- "Run this Python snippet and show the output"
- "Execute a quick REPL to test this algorithm with sample input"
- "Run my pytest function and return the test output"

## Note
This skill requires execution privileges and is therefore Code-only. It cannot access external networks or persistent host files unless the execution environment provides them.