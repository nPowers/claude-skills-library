# Token Budget Calculator

## Description
Estimate token consumption and cost for prompts and conversations. Use this skill to plan prompt length, set per-session or monthly token budgets, and get suggestions to reduce token usage.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask the user which model (or tokenization rules) and pricing they want to use, or provide default values (e.g., tokens per 1k and per-token cost).
2. Request the prompt(s) or typical messages to analyze; accept pasted text or short examples.
3. Estimate input and output token counts using a simple heuristic (words → tokens or known model ratios) and explain assumptions.
4. Calculate per-message and per-conversation costs, then extrapolate to daily/weekly/monthly totals based on user-specified frequency.
5. Present a clear budget summary: tokens per message, total tokens, cost, and recommended monthly cap.
6. Offer optimization tips to reduce tokens (shortening instructions, using system messages, batching messages) and show how each tip changes the estimate.
7. If the user asks, provide a compact template they can reuse to calculate budgets for other prompts.

## Example Usage
- "Estimate the token budget for a 500-word prompt and 3 responses per day"
- "How much will my monthly usage cost if I send 100 prompts a week with 300 tokens each?"
- "Suggest ways to cut tokens for this prompt: [paste prompt]"

## Note
Estimates use heuristics and model assumptions; send actual samples and model details for more accurate calculations.