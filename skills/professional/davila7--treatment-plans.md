# Clinical Treatment Plan Generator

## Description
Generate structured, evidence-aware treatment plans for clinical cases. Use when you need a concise problem list, goals, recommended interventions (medications, procedures, therapy), monitoring, follow-up, and contingency planning tailored to patient context.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Prompt the user to provide patient context: age, sex, chief complaint, diagnoses, allergies, current medications, labs/imaging, comorbidities, functional status, and treatment goals.
2. Ask about constraints and preferences: frailty, renal/hepatic function, pregnancy, resource limits, care setting, and desired output format (text, bulleted, ICD/SNOMED codes, FHIR JSON).
3. Perform a succinct problem-based synthesis: a brief summary and prioritized problem list with severity and acuity.
4. For each primary problem produce: goals (short- and long-term), recommended interventions (drug name, dose, route, frequency, duration, monitoring requirements), non-pharmacologic interventions, referrals, and required diagnostics.
5. Include monitoring plan, follow-up timeline, and explicit contingency plans for common complications or treatment failures.
6. Provide a short rationale with guideline citations or standard references when available, and highlight uncertainty or need for specialist input.
7. Offer the output in the requested format (bulleted plan, checklist, or FHIR-compliant structure) and add an editable template version if asked.

## Example Usage
- "Create a treatment plan for a 67-year-old with newly diagnosed heart failure and CKD stage 3."
- "Draft a discharge treatment plan for a patient with community-acquired pneumonia; include medication doses and follow-up."
- "Generate a problem-oriented treatment plan and export as a checklist for nursing staff."

## Note
This tool provides clinical decision support, not a substitute for clinician judgment. Verify recommendations against local protocols and patient-specific data; cite local guidelines where required.
