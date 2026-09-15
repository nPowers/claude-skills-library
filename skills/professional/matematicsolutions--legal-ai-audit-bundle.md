# Legal AI Audit Bundle

## Description
A compact suite of audit checks for AI systems focused on legal and compliance concerns: model governance, data use, privacy, contracts, and regulatory risk. Use it to produce a structured audit report and prioritized remediation plan.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported

## Instructions
1. Request high-level context: the AI system type, intended use cases, data sources, deployment model, and applicable jurisdictions.
2. Ask for available artifacts: data inventories, model documentation, contracts, privacy notices, and incident logs.
3. Run the following checklist for each audit area and record findings:
   a. Governance: roles, documented policies, approval workflows, and version control for models.
   b. Data: consent, provenance, retention, sensitive categories, and anonymization techniques.
   c. Privacy & Security: DPIA status, access controls, encryption, breach history.
   d. Contractual: vendor obligations, license terms, indemnities, liability caps.
   e. Regulatory: sector-specific obligations, consumer protection, AI-specific rules (if applicable).
4. For each finding, assign a risk rating (High/Medium/Low), explain the legal or business implication, and reference the relevant document or gap.
5. Produce a concise executive summary (1–3 paragraphs) and a detailed section-by-section audit report.
6. Provide prioritized remediation recommendations with estimated effort and suggested owners (legal, engineering, product).
7. Offer follow-up templates: discovery questions for vendors, audit evidence request lists, and policy change proposals.
8. Ask whether the user wants the report formatted for internal stakeholders, regulators, or external auditors.

## Example Usage
- "Run an AI governance audit for our recommendation engine"
- "Produce a privacy risk summary for a model trained on customer support chats"
- "What contractual clauses should we add for third-party model providers?"

## Note
Results depend on the quality and completeness of supplied artifacts. This assistant provides analysis and recommendations, not binding legal advice. For regulatory compliance, consult qualified counsel.