# Excel Variance Analyzer

## Description
Analyzes differences between two Excel sources (files or sheets) to identify and summarize variances (for example: budget vs. actual). Use it when you want a clear table of changed rows, percent and absolute variance, and suggested causes or remediation steps.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires file parsing and temporary file access to read and compare Excel workbooks)

## Instructions
1. Ask the user to upload one or two Excel files, or specify the workbook and sheet names to compare.
2. Request which column(s) serve as the row identifier (key) and which numeric columns to compare (e.g., Budget vs Actual).
3. Ask for any thresholds or filters (e.g., show only variances > 5% or > $500).
4. Parse the sheets, align rows by the key(s), compute absolute and percent variance for each matched row.
5. Produce a clear summary: total variance by category, top N variances (by absolute and percent), and a short narrative of likely causes.
6. Offer remedial suggestions (reclassify, investigate vendor, timing differences) and optionally export a CSV/Excel with annotated results.
7. If needed, produce visual aids (simple charts) or a compact human-readable report summarizing findings and next steps.

## Example Usage
- "Analyze variance between Budget.xlsx (sheet 'Jan') and Actuals.xlsx (sheet 'Jan') and show items >5% change."
- "Compare the 'Forecast' and 'Actual' columns in my spreadsheet and list the top 20 differences."
- "I uploaded two sheets — find rows where the amount changed by more than $200 and explain possible reasons."

## Note
This skill requires reading uploaded spreadsheet files and is intended for transient, session-level processing; do not upload sensitive data you cannot share. Results are as good as the provided key columns and data alignment.