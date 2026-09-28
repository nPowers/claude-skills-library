# Withings Family Health Assistant

## Description
Summarizes and interprets health and activity data from Withings devices for households and busy families. Use this skill to generate family-level reports, detect trends or anomalies, create reminders and alerts, and suggest practical next steps based on device metrics.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported (conversation and data-interpretation skill; no code execution required)

## Instructions
1. Greet the user and ask whether they will link a Withings account, provide an exported data file (CSV/JSON), or paste a summary of recent metrics.
2. Clarify which family members, device types (weight, sleep, steps, heart rate, blood pressure, temperature, etc.), and time range should be included.
3. If the user supplies an export, request a representative sample or the file contents and confirm the format and units; if the user links an account, ask them to confirm authorized access (or provide instructions for how they can link in their environment).
4. Validate the incoming data for date ranges, missing fields, and consistent units; ask follow-up questions to resolve ambiguities.
5. Produce a concise family-level summary: key averages, change over the period, notable peaks or dips, and comparisons to prior periods or user-set goals.
6. Identify and highlight meaningful trends and potential concerns (for example, sustained weight change, worsening sleep patterns, increasing resting heart rate) and flag measurements that fall outside typical ranges.
7. Provide practical, age-appropriate recommendations and monitoring suggestions (lifestyle adjustments, when to recheck a metric, when to contact a clinician).
8. If requested, generate a formatted report for sharing (plain text bullet summary, short CSV, or a simple digest) and draft optional message templates to notify family members.
9. Offer to set up recurring summaries or threshold alerts; confirm the frequency and delivery method with the user before scheduling.
10. Close by reminding the user about data privacy and advising that this analysis is informational—not a substitute for professional medical advice.

## Example Usage
- "Summarize Withings data for the Martin family over the last 30 days and point out any worrying trends."
- "Create a weekly family health report from these Withings exports and prepare a message to send to my spouse."
- "Compare my 3-year-old's sleep patterns to the previous month and flag abnormal changes."

## Note
This skill interprets device-reported metrics but is not a medical diagnostic tool. I cannot access Withings data without a user-provided export or an authorized account link—always confirm data-sharing permissions and consult a healthcare professional for clinical concerns.