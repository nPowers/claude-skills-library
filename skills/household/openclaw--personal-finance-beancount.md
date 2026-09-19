# Beancount Ledger Assistant

## Description
Helps create and maintain Beancount plain-text accounting ledgers: import CSV transactions, generate Beancount entries, reconcile accounts, and produce balance summaries. Use it when you keep your finances in a Beancount file and need import, cleanup, or query support.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires reading/writing ledger files and parsing uploaded CSVs)

## Instructions
1. Ask whether the user has an existing Beancount ledger file or is starting from scratch; request upload if available.
2. If importing transactions, request the CSV file and mapping for date, payee, amount, and account columns.
3. Propose an account hierarchy (Assets:Cash, Expenses:Groceries, Income:Salary, Liabilities:CreditCard) and confirm naming preferences.
4. Generate Beancount-formatted entries for each transaction, apply sensible splits where needed, and include metadata (payee, narration, tags).
5. Offer reconciliation assistance: match imported transactions to existing ledger entries and flag mismatches or duplicates.
6. Produce common queries (balances, income statement for a period, cash flow) and export an updated ledger file ready for local storage.

## Example Usage
- "Import this bank CSV and convert it to Beancount entries using Assets:Checking and Expenses categories."
- "I have a ledger; reconcile March transactions with the uploaded CSV and show unmatched items."
- "Create a minimal Beancount chart of accounts for personal finances and a sample ledger for the last three months."

## Note
This skill manipulates ledger files and requires uploads. Double-check sensitive details before sharing; generated entries should be reviewed before committing to your master ledger.