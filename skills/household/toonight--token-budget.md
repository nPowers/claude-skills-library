# Token Budget Planner

## Description
Estimates token usage and cost for LLM prompts and deployments, helps plan monthly token budgets, and suggests prompt optimizations to reduce cost. Use this when you need to forecast cost for a model, optimize prompt length, or compare model token pricing.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask which model(s) the user plans to use (name and pricing if known) and whether they want input, output, or both counted.
2. Request a sample prompt or an estimate of average prompt and expected response length (in words or characters), plus expected calls per day/week/month.
3. Calculate tokens per call using conservative token-per-word or known tokenizer rates; multiply by call volume to produce monthly token totals and cost estimates.
4. Provide a breakdown: tokens per call (input/output), monthly tokens, estimated monthly cost, and cost per 1k tokens.
5. Suggest concrete token-reduction tactics: prompt templates, instruction compression, caching, fewer model calls, or using a smaller model for some tasks.
6. Offer alternate scenarios (e.g., high/medium/low usage) and a short plan to stay within a given token budget.

## Example Usage
- "Estimate monthly token cost for 10,000 calls/month using Claude-2 with ~300 tokens input and 200 tokens output."
- "How can I reduce token usage for a chat assistant that currently sends 1,000 characters per turn?"
- "Compare cost and token use between model A and model B for a monthly budget of $100."

## Note
Estimates use heuristic token conversions and public pricing. For precise billing, cross-check with your provider's token accounting and pricing sheets.