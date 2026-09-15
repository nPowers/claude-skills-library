# Smart Grocery List Planner

## Description
Create organized, shareable grocery lists from recipes, meal plans, or quick inputs. Use it to categorize items by aisle, deduplicate quantities, scale lists for serving size, and produce checklists for shopping.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user whether they want to build a list from scratch, from recipes, or from a weekly meal plan.
2. When given items or recipes, parse ingredients, normalize names (e.g., "bell pepper" vs "peppers"), and combine duplicate ingredients into summed quantities.
3. Classify each item into logical shopping categories (produce, dairy, bakery, pantry, frozen, household, other). If the user provided a preferred store or aisles, use those mappings.
4. If asked, scale ingredient quantities according to target servings and convert units to user-preferred units (metric or imperial).
5. Produce a final checklist formatted with categories and quantities. Offer options to remove items, mark items as already in the pantry, or split the list by shopper.
6. Ask follow-up questions if any ingredient amounts, substitutions, or dietary constraints are unclear.

## Example Usage
- "Make a grocery list for this week's dinners: spaghetti bolognese, chicken tacos, and stir-fry."
- "Add: 2 cartons of milk, eggs, and flour, and categorize by aisle."
- "Scale the recipe list to serve 6 people and convert to metric."

## Note
Does not persist lists between sessions unless the user copies or exports them; clarify exports (text, CSV) when requested.