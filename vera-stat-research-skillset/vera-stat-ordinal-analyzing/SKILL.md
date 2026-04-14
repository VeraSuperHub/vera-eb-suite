---
name: vera-stat-ordinal-analyzing
description: >-
  Server-side extension that completes the full analysis pipeline for
  ordinal outcome variables after vera-stat-ordinal-testing has run.
  Adds nonparametric tests, subgroup analysis, and dual-path modeling:
  Path A ignores ordering (multinomial logistic, CART, RF, LightGBM) while
  Path B respects ordering (proportional odds with Brant test,
  adjacent-category logit, continuation-ratio logit, stereotype model,
  ordinal-aware trees and LightGBM). Cross-path synthesis compares
  variable importance rankings across both paths. Generates manuscript-ready
  methods.md and results.md with formatted tables, publication-quality
  figures, and references.bib. Applies output variation, code
  and code style variation for natural, non-repetitive output. Triggered after
  vera-stat-ordinal-testing completes, or direct request with
  an ordinal outcome variable.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Ordinal Outcome — Full Analysis & Manuscript Generation

Open-source skill. Read `reference/specs/output-variation-protocol.md`
before every generation — apply all variation layers.

## Workflow

Continues from where vera-stat-ordinal-testing stopped (PART 0-2 done).

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

Same as vera-stat-ordinal-testing, plus:
- Cumulative odds ratios: always with 95% CI, "cumulative OR = X.XX, 95% CI [X.XX, X.XX]"
- Proportional odds assumption: Brant test chi-squared(df) = X.XX, p = .XXX; if violated, state which predictors
- Coefficients: log-odds with SE always; report cumulative OR for interpretation
- If proportional odds violated: report adjacent-category, continuation-ratio, and stereotype models
- Multinomial logistic (Path A): class-specific OR with 95% CI per class contrast
- Adjacent-category logit: adjacent-category OR with 95% CI
- Continuation-ratio logit: continuation-ratio OR with 95% CI
- Stereotype model: scaling parameters with coefficients, 95% CI
- LightGBM importance: gain-based, normalized to 0-100
- Tree-based with small N: frame as "exploratory"; never claim predictive validity
- Spearman rho: report with 95% CI when available

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

Invoked directly after `vera-stat-ordinal-testing` or orchestrated by `vera-stat-application-pipeline`.
