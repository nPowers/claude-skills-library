# Clinical NLP Entity Extractor

## Description
Extract structured clinical entities (problems, medications, procedures, labs, vitals) from free-text clinical notes and output machine-readable records (JSON or FHIR). Designed for programmatic extraction and integration into pipelines.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires code execution and access to text/data files)

## Instructions
1. Request the input: example clinical text, sample files, or a description of the note types and language; ask which schema is desired (custom JSON, FHIR R4, CSV) and which ontologies to map to (ICD-10, SNOMED CT, RxNorm).
2. Confirm extraction targets and attributes: entity type, span offsets, normalized code, negation status, certainty, onset/time, value/units, and confidence score.
3. Preprocess text (de-identification if needed), sentence-splitting, tokenization, and basic normalization (dates, units, abbreviations).
4. Run or outline an extraction pipeline: NER -> entity normalization -> relation extraction (e.g., med-dose, lab-value) -> negation and temporality detection -> output mapping to the requested schema.
5. Produce example output for the provided text: annotated JSON or FHIR resources containing entities with fields: text, span, type, normalized_code, negation, certainty, onset, value, and confidence.
6. Provide an evaluation summary (precision/recall heuristics), recommended training data or rules to improve coverage, and suggestions for validation/QA with human review.

## Example Usage
- "Extract problems, meds, and allergies from this discharge summary and return JSON with SNOMED codes."
- "Run a clinical NLP extraction pipeline producing FHIR Condition and MedicationStatement resources from these notes."
- "Show me example output for entity extraction from a cardiology consult note."

## Note
Handle protected health information (PHI) in secure environments and comply with applicable privacy rules. Outputs are probabilistic and require human validation before clinical use. This skill requires code execution and access to the text data.
