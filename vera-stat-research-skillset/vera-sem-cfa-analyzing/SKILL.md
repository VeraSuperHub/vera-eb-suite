---
name: vera-sem-cfa-analyzing
description: >-
  Full CFA skill for measurement-model evaluation. Extends the initial
  CFA fit with reliability, convergent/discriminant validity, alternative-model
  comparison, modification-index review, subgroup invariance testing, and
  manuscript-ready methods/results. Trigger after vera-sem-cfa-testing or by a
  direct request for confirmatory factor analysis or measurement
  validation.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# CFA Analyzing — Full Measurement Model & Manuscript

Open-source skill.

Read `reference/specs/output-variation-protocol.md` before every generation.

## Workflow

| Step | File | Executor | Output |
|---|---|---|---|
| Additional tests | `workflow/04-run-additional-tests.md` | Main Agent | Reliability + validity code/prose |
| Subgroup | `workflow/05-analyze-subgroups.md` | Main Agent | Measurement invariance code/prose |
| Modeling | `workflow/06-fit-models.md` | Main Agent | Alternative CFA models |
| Comparison | `workflow/07-compare-models.md` | Main Agent | Cross-model synthesis |
| Manuscript | `workflow/08-generate-manuscript.md` | Main Agent | methods.md + results.md |

## Additional Inputs

Collect if missing:
- target discipline / journal style
- whether theory allows correlated residuals or cross-loadings
- planned grouping variable for invariance
- whether ordinal indicators should force a categorical estimator

## Output Structure

```
output/
├── methods.md
├── results.md
├── tables/
├── figures/
├── references.bib
├── code.R
└── code.py
```

## Key References

| File | Purpose |
|---|---|
| `reference/specs/output-variation-protocol.md` | Output quality variation |
| `reference/specs/code-style-variation.md` | Code style diversity |
| `reference/patterns/sentence-bank.md` | SEM wording variants |
| `reference/rules/reporting-standards.md` | CFA reporting rules |
