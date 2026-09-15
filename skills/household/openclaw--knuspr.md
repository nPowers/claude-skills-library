# Grocery & Shopping List Optimizer

## Description
Turn recipes, pantry inventories, or loose shopping needs into an optimized, aisle-grouped grocery list with estimated quantities and optional budget guidance. Use this when you want a shopper-friendly checklist and sensible item grouping.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Ask whether the user will provide recipes, pantry contents, or a free-form list.
2. Ask for household size, number of meals to serve, preferred stores, and a target budget if any.
3. Parse input to extract ingredients and required quantities, scaling to servings as needed.
4. Deduplicate and consolidate quantities across recipes; suggest common substitutions where helpful.
5. Group items by typical store sections (produce, dairy, meat, bakery, pantry, frozen, household) and mark perishables and non-perishables.
6. Provide estimated cost ranges if a budget was provided and suggest cheaper alternatives or bulk options to save money.
7. Output a clean, printable checklist and ask whether to convert to a shopping app format (note: this skill does not place orders).

## Example Usage
- "Convert these three recipes into an aisle-grouped shopping list for a family of 5"
- "I have eggs, milk, and rice—what else do I need to make dinners for four nights?"
- "Make a budget shopping list for a week for two adults and two kids with a $120 limit"

## Note
This skill cannot place or schedule real grocery orders; cost estimates are approximate and depend on local pricing.