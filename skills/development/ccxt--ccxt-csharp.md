# CCXT C# Integration Helper

## Description
Guide integration of cryptocurrency exchange APIs in C# (patterns similar to CCXT). Use this for authentication, market data retrieval, order placement, error handling, and rate-limit strategies tailored to .NET applications.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask which exchange(s) the user targets, whether a CCXT-compatible wrapper is available, and the target .NET version and runtime environment.
2. Request whether the integration is for production or sandbox/testing and if API keys or a simulator will be used.
3. Provide a secure authentication example (storing and loading API keys safely) and sample code for initializing the client.
4. Produce well-documented asynchronous examples for common tasks: fetch markets, get balances, place/cancel orders, and subscribe to websockets if required.
5. Add retry/backoff, rate-limiting, and error classification (retryable vs fatal) patterns with code snippets.
6. Suggest unit and integration test approaches, including mocking HTTP clients or using recorded responses.
7. Explain best practices for symbol mapping, timezones, precision handling, and concurrency concerns.

## Example Usage
- "Show me how to fetch balances from Binance using a C# CCXT-style client"
- "Create an async C# method to place a limit order and handle rate-limit errors"
- "Help build integration tests for exchange API calls without hitting live endpoints"

## Note
Exchange APIs differ: always confirm the exchange's specific endpoints and test in a sandbox before running live orders.