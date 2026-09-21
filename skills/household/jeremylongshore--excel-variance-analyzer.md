# Excel Variance Analyzer

## Description
Process an Excel or CSV file to compute variances, highlight unexpected changes, and produce a concise variance report. Use this skill when you have time-series or comparative spreadsheet data and need anomaly identification and summarized insights.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires file processing to read XLSX/CSV and generate annotated output)

## Instructions
1. Prompt the user to upload the Excel (.xlsx) or CSV file and indicate which sheets or columns contain the baseline and comparison series (e.g., Actual vs Budget, Month N vs Month N-1).
2. Validate file structure and confirm column headers or let the user map columns to roles (date, category, baseline, comparison).
3. Compute absolute and percentage variances for the chosen comparisons and flag rows exceeding configurable thresholds (e.g., >10% change or absolute delta > X).
4. Summarize top positive and negative variances by magnitude and by category, and compute aggregated variances (totals, means, weighted changes).
5. Generate a short human-readable summary that explains major drivers of variance and any suspicious or missing data.
6. Offer an annotated output: a CSV/XLSX with added variance columns and flags, plus a plain-text executive summary. Provide guidance for next steps (drill-down queries to investigate anomalies).
7. If requested, produce visuals (simple charts) or generate pivot-style summaries if data has multiple categorical keys.

## Example Usage
- "Analyze variance between Actuals and Budget in this file and flag anything >15%"
- "Compare sales by month and show top 10 negative variances"
- "Upload a CSV of transactions and give me a variance summary by category"

## Note
This skill requires reading and writing files to examine spreadsheets; accuracy depends on correct column mapping and clean input data.