# C# Concurrency Patterns Guide

## Description
Practical guidance for choosing and applying concurrency patterns in C# projects. Use this skill to diagnose concurrency problems, recommend patterns (async/await, TPL, dataflow, channels, locks), and produce focused example code and explanations.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user for context: application type (web, desktop, service), .NET/runtime version, and whether the workload is IO-bound or CPU-bound.
2. Request a minimal reproducible example or a short description of the concurrency problem (symptoms, performance metrics, exception traces, deadlocks).
3. Map the problem to candidate patterns (async/await, Task Parallel Library, Parallel LINQ, Channels/producer-consumer, TPL Dataflow, locks/Concurrent collections, immutability) and explain why each is appropriate or not.
4. Provide one clear, version-appropriate C# example implementing the recommended pattern, including cancellation, error handling, and resource cleanup.
5. Discuss trade-offs (scalability, latency, thread usage, complexity), common pitfalls (deadlocks, thread-affinity, synchronization contexts), and testing strategies.
6. Suggest concrete next steps: unit/integration tests, performance measurements, analyzers, and small refactor tasks. Offer follow-up refactoring or a code review cycle.

## Example Usage
- "Show me recommended concurrency patterns for a C# web API handling many concurrent requests"
- "Refactor this thread-and-lock based code to use async/await and channels"
- "Which concurrency model should I use for a CPU-bound background worker?"

## Note
I cannot execute code or access your filesystem; provide snippets and runtime details for the most accurate, runnable examples.