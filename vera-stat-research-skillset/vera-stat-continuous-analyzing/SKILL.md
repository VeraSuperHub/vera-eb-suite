---
name: vera-stat-continuous-analyzing
description: >-
  Server-side extension that completes the full analysis pipeline for
  continuous outcome variables after vera-stat-continuous-testing has run.
  Adds remaining hypothesis tests (ANOVA, post-hoc, nonparametric),
  subgroup analysis with interaction tests and forest plots, full modeling
  (OLS with diagnostics, quantile regression, tree-based exploratory), and
  model comparison. Generates manuscript-ready methods.md and results.md
  with formatted tables, publication-quality figures, and references.bib.
  Applies output variation and code style variation for natural, non-repetitive output. Triggered after
  vera-stat-continuous-testing completes, or direct request with a continuous/numeric outcome variable.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Continuous Outcome — Full Analysis & Manuscript Generation

Open-source skill. Read `reference/specs/output-variation-protocol.md`
before every generation — apply all variation layers.

## Workflow

Continues from where vera-stat-continuous-testing stopped (PART 0-2 done).

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
- Target journal or style (APA 7th, STROBE, etc.)
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

Same as vera-stat-continuous-testing, plus:
- Coefficients: unstandardized B with SE always; add β when predictors on different scales
- R²: "accounted for X% of variance" — never "explained" unless true experiment
- Quantile regression: report specific quantile(s) and SE method (bootstrap preferred)
- Tree-based with small N: frame as "exploratory"; never claim predictive validity
- Transformations: report on both transformed and original scales

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

Invoked directly after `vera-stat-continuous-testing` or orchestrated by `vera-stat-application-pipeline`.
