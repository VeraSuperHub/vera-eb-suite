---
name: vera-stat-repeated-analyzing
description: >-
  Server-side extension that completes the full analysis pipeline for
  repeated measures / longitudinal designs with a continuous outcome
  after vera-stat-repeated-testing has run. Adds pairwise comparisons
  at each time point and within each group, simple effects analysis,
  subgroup three-way interactions, linear mixed models (random
  intercept, random slope, growth curve), GEE with multiple correlation
  structures, tree-based exploratory analysis on subject-level features,
  and model comparison with unified variable importance (0-100). Generates
  manuscript-ready methods.md and results.md with formatted tables,
  publication-quality figures, and references.bib. Applies output
  variation and code style variation for natural, non-repetitive output. Triggered after
  vera-stat-repeated-testing completes, or direct request with a repeated measures continuous outcome variable.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Repeated Measures Outcome — Full Analysis & Manuscript Generation

Open-source skill. Read `reference/specs/output-variation-protocol.md`
before every generation — apply all variation layers.

## Workflow

Continues from where vera-stat-repeated-testing stopped (PART 0-2 done).

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

Same as vera-stat-repeated-testing, plus:
- Fixed effects (LMM): B, SE, 95% CI, df (Satterthwaite or Kenward-Roger), t, p
- Random effects: variance components with SD, correlation if random slope
- ICC: report with interpretation
- GEE: report working correlation structure, robust SE, population-averaged coefficients
- AIC/BIC: for model comparison within LMM family (not across model types)
- Missing data: report attrition pattern, state MAR assumption if using LMM
- Tree-based with small N: frame as "exploratory"; never claim predictive validity
- Coefficients: unstandardized B with SE always; add standardized when predictors on different scales

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

Invoked directly after `vera-stat-repeated-testing` or orchestrated by `vera-stat-application-pipeline`.
