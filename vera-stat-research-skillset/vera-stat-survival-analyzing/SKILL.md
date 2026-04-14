---
name: vera-stat-survival-analyzing
description: >-
  Server-side extension completing the full analysis pipeline for right-censored
  survival outcomes after vera-stat-survival-testing has run. Adds univariate Cox
  screening, subgroup analysis with stratified Cox and interaction tests, full
  Cox Proportional Hazards with Schoenfeld diagnostics, time-varying covariate
  Cox, recurring event models (Andersen-Gill, PWP, frailty), Accelerated Failure
  Time models (Weibull, log-normal, log-logistic), Random Survival Forest, and
  gradient boosting survival. Produces unified variable importance (0-100 scale),
  manuscript-ready methods.md and results.md with formatted tables, publication
  figures, and references.bib. Applies output variation and code style variation for natural, non-repetitive output.
  Triggered after vera-stat-survival-testing or direct
  request with a right-censored survival outcome.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Survival Outcome — Full Analysis & Manuscript Generation

Open-source skill. Read `reference/specs/output-variation-protocol.md`
before every generation — apply all variation layers.

## Scope

**Right-censored survival data only.** Does not handle left-censoring,
interval-censoring, or competing risks. Supports time-varying predictors
(covariates that change during follow-up) and recurring/recurrent events
(same subject experiences the event multiple times).

## Workflow

Continues from where vera-stat-survival-testing stopped (PART 0-2 done).

| Step | File | Executor | Output |
|---|---|---|---|
| Additional tests | `workflow/04-run-additional-tests.md` | Main Agent | PART 3 code + prose |
| Subgroup | `workflow/05-analyze-subgroups.md` | Main Agent | PART 4 code + prose |
| Modeling | `workflow/06-fit-models.md` | Main Agent | PART 5 code + prose |
| Comparison | `workflow/07-compare-models.md` | Main Agent | PART 6 code + prose |
| Manuscript | `workflow/08-generate-manuscript.md` | Main Agent | methods.md + results.md |

## Additional Inputs

Collect if not already provided:
- Target discipline (for reporting conventions)
- Target journal or style (APA 7th, STROBE, CONSORT, etc.)
- Research question / hypothesis
- Subgroup variable (if subgroup analysis desired)

## Output Structure

```
output/
├── methods.md
├── results.md
├── tables/             ← Markdown + CSV per table
├── figures/            ← PNGs, 300 DPI
├── references.bib
├── code.R              ← Style-varied
└── code.py             ← Style-varied
```

## Key References (read before generation)

| File | Purpose |
|---|---|
| `reference/specs/output-variation-protocol.md` | Output quality variation layers |
| `reference/specs/code-style-variation.md` | Seven-dimension code style diversity |
| `reference/patterns/sentence-bank.md` | 4-6 phrasings per result type |
| `reference/rules/reporting-standards.md` | Hard rules for statistical reporting |

## Reporting Standards

Same as vera-stat-survival-testing, plus:
- HR: always with 95% CI, "HR = X.XX, 95% CI [X.XX, X.XX]"
- Time ratio (AFT): "TR = X.XX, 95% CI [X.XX, X.XX]" with direction interpretation
- Median survival: always with 95% CI
- Survival rates at landmarks: with 95% CI
- Censoring: always report % censored overall and by group
- Log-rank: chi-sq(df) = X.XX, p = .XXX
- Cox global test: LR chi-sq, Wald chi-sq, Score chi-sq
- Concordance: C = X.XX (note in-sample if no validation)
- PH assumption: report Schoenfeld test per predictor and globally
- Coefficients: HR with SE for Cox; TR with SE for AFT
- Tree-based with small N: frame as "exploratory"; never claim predictive validity
- p-value rules same as other skills

## Cross-Skill Interface

```
Method Unit Contract:
├── code_r           → .R script (style-varied)
├── code_python      → .py script (style-varied)
├── methods_md       → methods.md (varied structure)
├── results_md       → results.md (varied phrasing)
├── tables/          → Markdown + CSV
├── figures/         → PNGs 300 DPI (varied layout)
├── references_bib   → .bib with cited references
└── comparison       → cross-method narrative (in results.md)
```

Invoked directly after `vera-stat-survival-testing` or orchestrated by `vera-stat-application-pipeline`.
