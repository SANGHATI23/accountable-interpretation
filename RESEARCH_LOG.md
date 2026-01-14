# Research Log — Accountable Interpretation of Genetic Variants

This log captures the research trail behind the project: what I tried, what changed, and why.

## Late 2025 — Framing the question
- Initial question: do some ClinVar interpretations that appear confident show signs of instability when examined more closely?
- Early assumption was that reclassification was rare; manual inspection of several ClinVar records suggested otherwise.
- Decided to focus on interpretation stability rather than pathogenicity prediction.

## Late 2025 — First analysis attempts
- Initial plan was to process the full ClinVar dataset end-to-end.
- This approach slowed iteration and made it harder to validate assumptions early.
- Adjusted workflow to test logic on smaller subsets before scaling analyses.

## Late 2025 — Data and schema issues
- Encountered missing or inconsistently structured metadata fields across exports.
- Added explicit mappings and checks rather than assuming a fixed schema.
- Performed spot checks to ensure signals behaved sensibly after each adjustment.

## Early 2026 — Methodological refinement
- Considered building a single composite risk score but found it obscured the sources of uncertainty.
- Chose to retain separable, interpretable signals so instability could be reasoned about transparently.
- Framed the work as an audit of interpretation reliability rather than a deployable tool.

## Early 2026 — Documentation and cleanup
- Consolidated notebooks and clarified analysis flow.
- Added README, design decisions, and limitations to make scope and intent explicit.
- Identified validation against historical reclassifications as a key next step.
