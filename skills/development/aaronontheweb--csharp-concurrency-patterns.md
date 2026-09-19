# C# Concurrency Patterns Guide

## Description
Specialized guidance on concurrency and parallelism in C#, covering async/await, Task-based patterns, threading, synchronization, and scalability trade-offs. Use it when designing concurrent systems or fixing race conditions.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask for the concurrency scenario: workload type (I/O-bound vs CPU-bound), expected throughput, and runtime target (ThreadPool behavior varies across runtimes).
2. Determine constraints: latency requirements, memory limits, cancellation and timeout behavior, and whether ordering must be preserved.
3. Recommend one or more concurrency strategies (async/await, Task.Run, Parallel.ForEach, TPL Dataflow, Channels) with rationale and trade-offs.
4. Provide concrete C# examples illustrating the recommended pattern, including correct use of CancellationToken, ConfigureAwait, and exception handling.
5. Highlight common pitfalls (deadlocks, thread starvation, synchronization overhead) and how to detect them.
6. Offer benchmarking and profiling suggestions, plus unit/integration test patterns for concurrent code.

## Example Usage
- "How should I implement a high-throughput producer/consumer in C#?"
- "Explain when to use Task.Run vs async IO"
- "Show an example using Channels to process messages with a bounded buffer"

## Note
Advice is conceptual and example-based; always validate concurrency changes with real workload tests because behavior depends on runtime, environment, and workload characteristics.
