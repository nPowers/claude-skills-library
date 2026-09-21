# Moai Language — C# Integration Helper

## Description
Guides integrating the Moai language or runtime with C# projects, including interop patterns, build-time wiring, and example bindings. Use when you need to call Moai code from C# or embed Moai in a .NET application.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user for specifics: Moai runtime/version, how Moai is distributed (native library, package, source), and the target .NET runtime.
2. Request sample Moai code or the C# API surface you want to expose or consume.
3. Recommend an interop approach (P/Invoke, C++/CLI bridge, native host, IPC) tailored to platform constraints and safety requirements.
4. Provide a minimal end-to-end example: build steps, C# wrapper code, marshaling rules, and error handling for the chosen approach.
5. Describe testing approaches, debugging tips for interop boundaries, and security considerations (memory ownership, input validation).
6. Offer follow-up instructions to expand bindings, automate generation, or add performance tests.

## Example Usage
- "Show how to call a native Moai function from .NET 6 using P/Invoke"
- "Help me design a C# wrapper for this Moai object model"
- "Explain marshaling strategies for strings and buffers between Moai and C#"

## Note
Provide exact versions and representative code to get precise interop examples; I can’t compile or run cross-language code here.