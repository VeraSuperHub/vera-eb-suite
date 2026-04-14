---
name: vera-stat-meta-analyzing
description: >-
  Server-side extension that completes the full analysis pipeline for
  meta-analysis after vera-stat-meta-testing has run. Adds publication
  bias assessment (funnel plot, Egger's test, trim-and-fill), sensitivity
  analysis (leave-one-out, influence diagnostics, cumulative meta-analysis),
  subgroup analysis with Q_between, meta-regression with bubble plots,
  advanced modeling (REML, Knapp-Hartung, Bayesian, three-level), and
  model comparison. Generates manuscript-ready methods.md and results.md
  with formatted tables, publication-quality figures, and references.bib.
  Applies output variation and code style variation for natural, non-repetitive output. Triggered after
  vera-stat-meta-testing completes, or direct request with meta-analysis data.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Meta-Analysis — Full Analysis & Manuscript Generation

Open-source skill. Read `reference/specs/output-variation-protocol.md`
before every generation — apply all variation layers.

## Workflow

Continues from where vera-stat-meta-testing stopped (PART 0-2 done).

| Step | File | Executor | Output |
|---|---|---|---|
| Publication bias | `workflow/04-run-additional-tests.md` | Main Agent | PART 3 code + prose |
| Subgroup & regression | `workflow/05-analyze-subgroups.md` | Main Agent | PART 4 code + prose |
| Advanced models | `workflow/06-fit-models.md` | Main Agent | PART 5 code + prose |
| Model comparison | `workflow/07-compare-models.md` | Main Agent | PART 6 code + prose |
| Manuscript | `workflow/08-generate-manuscript.md` | Main Agent | methods.md + results.md |

## Additional Inputs

Collect if not already provided:
- Target discipline (for reporting conventions)
- Target journal or style (APA 7th, PRISMA, Cochrane)
- Research question / hypothesis
- Subgroup variable (categorical moderator)
- Continuous moderator (for meta-regression)

## Output Structure

```
output/
├── methods.md
├── results.md
├── tables/             <- Markdown + CSV per table
├── figures/            <- PNGs, 300 DPI
├── references.bib
├── code.R              <- Style-varied
└── code.py             <- Style-varied
```

## Key References (read before generation)

| File | Purpose |
|---|---|
| `reference/specs/output-variation-protocol.md` | Output quality variation layers |
| `reference/specs/code-style-variation.md` | Seven-dimension code style diversity |
| `reference/patterns/sentence-bank.md` | 4-6 phrasings per result type |
| `reference/rules/reporting-standards.md` | Hard rules for statistical reporting |

## Reporting Standards

Same as vera-stat-meta-testing, plus:
- Egger's test: "intercept = X.XX, SE = X.XX, p = .XXX"
- Begg's rank test: "Kendall's tau = X.XX, p = .XXX"
- Trim-and-fill: "k imputed = X, adjusted ES = X.XX, 95% CI [X.XX, X.XX]"
- Meta-regression: "B = X.XX, SE = X.XX, p = .XXX, R² = .XX"
- Leave-one-out: "pooled ES ranged from X.XX to X.XX when individual studies removed"
- Subgroup differences: "Q_between(df) = X.XX, p = .XXX"
- Bayesian: "posterior mean = X.XX, 95% CrI [X.XX, X.XX]"
- Three-level: "sigma²_within = X.XX, sigma²_between = X.XX"

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

Invoked directly after `vera-stat-meta-testing` or orchestrated by `vera-stat-application-pipeline`.
