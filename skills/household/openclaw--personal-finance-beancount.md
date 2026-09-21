# Beancount Ledger Assistant

## Description
Parse a Beancount ledger file to produce summaries (income/expense breakdowns, cashflow, net worth) and help find syntax or balancing issues. Use this skill to reconcile Beancount data, generate reports, and get suggestions for cleaning ledger entries.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires reading and analyzing Beancount files)

## Instructions
1. Ask the user to upload their Beancount file(s) (.beancount) or paste relevant ledger snippets.
2. Parse entries to validate transaction syntax, detect unbalanced transactions, missing metadata, and common formatting errors.
3. Produce summary reports: income vs expense by account, cash balance timeline, net worth snapshot, and account-level summaries for a given date range.
4. Flag suspicious transactions (e.g., large outliers, uncategorized postings) and suggest corrective actions or journal entry fixes.
5. Offer exportable reports (CSV or simple tables) and, if requested, a cleaned or annotated version of the ledger with comments on lines that need attention.
6. Provide guidance on Beancount best practices (naming conventions, account hierarchies, and metadata tips) to keep the ledger maintainable.

## Example Usage
- "Check my ledger.beancount file for unbalanced transactions and give a net worth summary"
- "Show income and expenses by account for Jan–Jun 2026"
- "Help me find why my cash account balance differs from the bank statement"

## Note
This skill requires access to ledger files to parse and validate entries. It can suggest fixes but does not replace formal accounting or audit processes.