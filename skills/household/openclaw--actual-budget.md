# Actual Budget Reconciliation

## Description
A conversational assistant that helps reconcile planned budgets with actual spending. Use it to summarize expenses by category, compute variances against targets, and generate adjustments or next-step recommendations for household finances.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask the user which budget period and currency to analyze (e.g., "March 2026", "monthly").
2. Request the user's budgeted categories and amounts, either typed in, pasted, or uploaded as plain text or CSV data.
3. Ask the user to provide actual transactions for the same period (pasted list, CSV export, or typed entries) and clarify how transactions map to categories if needed.
4. Parse the provided transactions, total spending per category and overall, and compute variance versus each budgeted amount.
5. Present a clear summary: totals, over/under per category, percent differences, and a short plain-language explanation of the biggest variances.
6. Offer actionable recommendations (e.g., reallocate budget, cut a category, or increase savings target) and propose a simple revised budget.
7. If the user requests, prepare a concise exportable summary they can copy or paste into a spreadsheet.

## Example Usage
- "Compare my actual spending to my budget for April 2026"
- "Reconcile these transactions with my monthly budget"
- "Which categories went over budget last month?"

## Note
I cannot access bank accounts automatically—please paste or upload your transaction data. This provides guidance only and is not professional financial advice.