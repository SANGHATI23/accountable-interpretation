# Accountable Interpretation of Genetic Variants: Studying Stability and Reclassification Risk

**Timeline:** Exploratory analysis began in **late 2025**; refactored and documented in **early 2026** after iterative testing and scope refinement.


## Why I worked on this

Genetic test results and clinical AI outputs are often treated as definitive once they are labeled or deployed. While working with public genomic databases, I noticed that many variant interpretations appear confident even though the underlying evidence is incomplete, outdated or disputed.

Initially, I assumed this instability was rare. However, after manually examining multiple ClinVar records, it became clear that reclassification is not an exception but a recurring pattern.

This project began as an attempt to understand when genetic interpretations should be treated cautiously, rather than accepted at face value.

---

## The problem I am studying

Public databases such as ClinVar provide categorical labels for genetic variants (e.g., pathogenic, benign, uncertain). These labels are frequently used in downstream clinical and research settings.

However, the evidence supporting these labels evolves over time as new studies emerge, expert opinions change, and additional submissions are made. Despite this, the labels themselves often appear static and equally trustworthy.

The central problem addressed in this project is:

**How can we identify variant interpretations that look confident but are actually unstable or at high risk of reclassification?**

---

## What I did (in plain terms)

Rather than predicting pathogenicity or building a diagnostic model, I focused on auditing the reliability of existing interpretations.

Using publicly available ClinVar metadata, I examined signals such as:
- number of submitters  
- agreement versus disagreement among submissions  
- review status  
- age of supporting evidence  

I combined these interpretable signals to characterize how stable or fragile a given variant interpretation may be. The goal was not to assign a new label, but to flag cases where confidence may be misleading.

## What changed during development (and why)

- **Scope adjustment:** My initial approach was to run the full workflow end-to-end immediately. This proved too slow for meaningful iteration, so I shifted to validating assumptions and logic on smaller subsets before scaling.
- **Schema surprises:** Some ClinVar fields I expected to be consistently populated were missing or structured differently across exports. Rather than assuming a stable schema, I added explicit mappings and defensive checks.
- **Method simplification:** I originally considered using more complex modeling approaches, but practical constraints and interpretability concerns led me to favor simpler, transparent analyses that could be inspected and reasoned about directly.
- These changes helped keep the analysis reproducible and aligned with the goal of auditing interpretation stability rather than maximizing predictive performance.

---

## What this project is not

This project is not a prediction system and does not attempt to determine whether a variant is pathogenic or benign.

It is also not intended to replace expert review or clinical judgment. Instead, it is designed to support prioritization and caution, highlighting cases where interpretations may warrant closer scrutiny.

---

## Why this matters

Genetic interpretations are increasingly integrated into clinical decision-making and automated pipelines. When unstable interpretations are treated as definitive, there is a risk of over-trust and inappropriate downstream decisions.

By surfacing instability and uncertainty, this work aims to support safer use of genetic data and contribute to broader discussions around accountability and trust in biomedical decision-support systems.

---

## How to read this repository

If you are reviewing this repository:
1. Read the sections **Why I worked on this** and **What I did** above  
2. Review the main analysis notebook(s) to understand how instability signals were derived  
3. Refer to the documentation files for limitations and design decisions  

---

## Current limitations and future directions

This work has several limitations, including reliance on public metadata and lack of longitudinal clinical outcomes. These are discussed in more detail in the accompanying documentation.

Future work would involve validating instability signals against known historical reclassifications and exploring how such signals could be integrated into real-world review workflows.

---

## Project status

This is an exploratory research project intended to study reliability and reclassification risk in genetic interpretation. The work is ongoing and meant to evolve with further validation and feedback.
