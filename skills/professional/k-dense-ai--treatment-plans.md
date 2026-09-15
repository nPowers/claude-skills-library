# Treatment Plan Template Assistant

## Description
Create customizable treatment-plan templates and populate them from patient information. Use this when you need consistent, reproducible plans for specific conditions or care pathways (e.g., diabetes, COPD, postop care).

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask which condition or care pathway the user needs a template for and any local or institutional constraints (preferred meds, formulary, follow-up cadence).
2. Request patient-specific inputs to populate the template: demographics, diagnosis details, labs, allergies, current therapies, and care goals.
3. Generate a structured template with sections: summary, problem list, goals, ordered interventions (meds, doses, non-pharmacologic care), monitoring tasks, follow-up schedule, patient education points, and documentation checklist.
4. Provide variations (standard, conservative, aggressive) and explain when to choose each; include checkboxes or succinct action items suitable for EMR intake.
5. Offer outputs in common formats (plain text, bulleted list, table, or JSON schema) and optionally include ICD/SNOMED mappings for problems and medications.
6. Ask if the user wants local guideline citations or a printable patient-facing summary.

## Example Usage
- "Create a diabetes treatment-plan template for primary care with glycemic targets and follow-up schedule."
- "Populate a COPD exacerbation discharge template for a 74-year-old smoker on home oxygen."
- "Give me a conservative and an aggressive treatment plan template for chronic low back pain."

## Note
Templates are starting points and should be adapted to individual patients and institutional protocols. Clinician review and alignment with local guidelines are required before deployment.
