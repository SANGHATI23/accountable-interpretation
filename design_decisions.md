# Design Decisions

This document describes key design choices made during the development of this project and the reasoning behind them. The goal is to clarify why certain approaches were taken and why others were intentionally avoided.

## Why I focused on interpretation stability rather than prediction

I initially considered building a model to predict whether a variant would be reclassified in the future. However, reclassification depends on future evidence that is not observable at decision time, such as new experiments or expert consensus changes.

Instead of attempting to predict unknown future events, I chose to study signals of instability present at the time an interpretation is made. This framing better aligns with the goal of supporting cautious interpretation rather than producing speculative predictions.

## Why I relied on interpretable metadata signals

The project prioritizes signals that are transparent and easily interpretable, such as submission counts, disagreement among submitters, review status and evidence age.

These features were chosen because they can be understood and debated by clinicians and researchers. More complex representations may offer higher predictive performance but would reduce interpretability and trust, which are central concerns in clinical and biomedical contexts.

## Why I did not use patient-level or outcome data

This work is intentionally limited to publicly available data. Incorporating patient-level outcomes would introduce additional ethical, privacy and access considerations and would shift the project toward clinical effectiveness rather than interpretability and reliability.

By restricting the scope to metadata-level signals, the project remains focused on auditing interpretation processes rather than clinical decision outcomes.

## Why I avoided building a single composite risk score

I considered summarizing instability into a single numerical score. However, doing so would obscure which specific factors contributed to uncertainty.

Instead, I retained separable signals so that users can inspect and reason about different sources of instability independently. This supports transparency and avoids over-simplifying complex evidence structures.

## Why this is framed as an audit rather than a tool

The intent of this work is not to deploy a decision-support system but to analyze how existing systems behave under evolving evidence.

Framing the project as an audit emphasizes accountability and reflection rather than automation. This perspective is more appropriate for early-stage research into reliability and trust.

## Decisions intentionally deferred

Several potential extensions were deliberately deferred, including:
- prospective validation against future ClinVar releases
- disease- or gene-specific analyses
- integration with clinical workflows

These directions were postponed to keep the current work focused and interpretable, and to avoid making claims that would require additional validation.
