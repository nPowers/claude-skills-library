# Python Explainer & Debugger

## Description
Explain Python code, diagnose errors from traces, and suggest precise fixes and tests. Use this skill to understand unfamiliar code, find logic bugs, and get step-by-step remediation when you cannot or do not want to run the code.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Request the code snippet, error trace, and the expected vs actual behavior from the user.
2. Recreate a minimal mental model of the problem and list likely root causes in order of probability.
3. Provide a targeted fix: show the minimal changed code block and explain each change in 1–2 lines.
4. Offer unit tests or small example invocations that would demonstrate the fix; include sample inputs and expected outputs.
5. When appropriate, provide alternative approaches (simple/robust/performant) and trade-offs.
6. Encourage iterative verification: ask the user to run the suggested tests and report results or paste updated traces.
7. Always ask clarifying questions if the provided information is insufficient to produce a reliable fix.

## Example Usage
- "I get a TypeError in this function — help me fix it"
- "Explain what this class does and point out potential bugs"
- "Give me a minimal test that reproduces this failure"

## Note
This skill cannot execute code; recommendations are based on static analysis and the information provided. Always run suggested fixes in your environment.