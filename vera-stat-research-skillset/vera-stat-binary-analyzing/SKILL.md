---
name: vera-stat-binary-analyzing
description: >-
  Server-side extension that completes the full analysis pipeline for
  binary outcome variables after vera-stat-binary-testing has run. Adds
  remaining association tests (chi-square/Fisher's for additional
  predictors, point-biserial for continuous predictors), stratified odds
  ratio analysis with Breslow-Day test and forest plot, full modeling
  (logistic regression with OR and 95% CI, Hosmer-Lemeshow GOF, pseudo-R2,
  ROC curve with AUC, classification table, tree-based classification with
  CART/RF/GBM), and cross-method variable importance comparison on a 0-100
  unified scale. Generates manuscript-ready methods.md and results.md with
  formatted tables, publication-quality figures, and references.bib.
  Applies output variation and code style variation for natural, non-repetitive output. Triggered after
  vera-stat-binary-testing completes, or direct request with a binary outcome variable.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Binary Outcome --- Full Analysis & Manuscript Generation

Open-source skill. Read `reference/specs/output-variation-protocol.md`
before every generation --- apply all variation layers.

## Workflow

Continues from where vera-stat-binary-testing stopped (PART 0-2 done).

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

Same as vera-stat-binary-testing, plus:
- Logistic coefficients: report OR (not raw B) in results text; raw B with SE in supplementary table
- Pseudo-R2: report McFadden and Nagelkerke; say "the model accounted for" --- never "explained"
- AUC: report with 95% CI; note "in-sample" if no cross-validation performed
- Classification: report sensitivity, specificity, and threshold used
- Tree-based with small N: frame as "exploratory"; never claim predictive validity
- Hosmer-Lemeshow: report chi-sq, df, p; non-significant = adequate fit

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

Invoked directly after `vera-stat-binary-testing` or orchestrated by `vera-stat-application-pipeline`.
