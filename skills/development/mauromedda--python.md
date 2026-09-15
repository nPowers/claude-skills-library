# Python Libraries & Integration Helper

## Description
Help integrate third-party Python libraries, provide minimal reproducible examples, and outline installation and compatibility steps. Use this skill when you need correct usage patterns, dependency guidance, or migration advice between libraries.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask the user for the target library, desired functionality, Python version, and any constraints (offline installs, license requirements).
2. Provide a minimal, copy-pastable example demonstrating the common usage pattern, including required imports and simple error handling.
3. List installation commands (pip/poetry) and recommend exact package versions or constraints for compatibility.
4. Call out common pitfalls, platform-specific issues, and security or performance caveats.
5. If the user requests integration with other libraries or frameworks, provide glue code and explain lifecycle concerns (e.g., async vs sync, threads, event loops).
6. Offer migration steps and code snippets when proposing alternative libraries or upgrades.
7. Ask clarifying questions about deployment or runtime environment before giving final recommendations.

## Example Usage
- "Show me a minimal example of using requests to post JSON and handle errors"
- "How do I integrate SQLAlchemy with asyncio in Python 3.11?"
- "Recommend a lightweight HTTP client for downloads and show usage"

## Note
This skill cannot install or execute code; examples must be run in the user's environment. Verify compatibility and test examples locally.