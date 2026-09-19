# C# Async Patterns

## Description
Advises on designing and implementing asynchronous code in C#. Use it to review async/await usage, Task vs ValueTask decisions, cancellation, exception handling, synchronization contexts, and performance trade-offs.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Request the code snippet or describe the async scenario (library APIs, UI app, server-side service) and any performance or correctness goals.
2. Analyze the code for common async anti-patterns: async void, missing ConfigureAwait where relevant, blocking on Task.Result/Wait, and improper use of Task.Run.
3. Recommend concrete refactorings with short before/after snippets: proper async signatures, CancellationToken propagation, using ValueTask when appropriate, and safe parallelism via Task.WhenAll or Dataflow.
4. Explain exception handling strategies in async flows and guidance on top-level handling versus propagated exceptions.
5. Discuss synchronization context considerations (UI vs thread pool), avoiding deadlocks, and testing approaches for async methods (unit tests with Task-based assertions and timeouts).
6. When applicable, provide performance considerations and diagnostics (await diagnostics, thread starvation, and allocation reduction techniques).

## Example Usage
- "Review this async method and suggest improvements to avoid blocking calls."
- "When should I use ValueTask instead of Task in a high-throughput library?"
- "How do I propagate CancellationToken from controller to data-access layer?"

## Note
This skill provides design and refactoring guidance; it does not execute or profile code. For runtime profiling, run diagnostics in a proper environment.