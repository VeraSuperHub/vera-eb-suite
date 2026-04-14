---
name: vera-stat-binary-testing
description: >-
  Runs class balance diagnostics and primary association tests for binary
  outcome variables (0/1, yes/no, survived/died, pass/fail). Produces
  proportion tables, class balance check with rare-event warning,
  descriptives by outcome level, chi-square test of independence with
  Cramer's V, Fisher's exact test when cell counts are small, odds ratio
  with 95% CI, and a mosaic or grouped bar chart. Outputs .R and .py scripts with 2 publication-quality plots.
  Triggered when user has a binary/dichotomous outcome and says "binary
  outcome," "logistic," "survived or died," "yes or no," "pass or fail,"
  "0/1," "classification," "binary DV," or names a binary variable like
  survived, admitted, defaulted, churned, diagnosed. Does not handle
  continuous, count, survival time, ordinal, repeated measures, or SEM.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Binary Outcome --- Class Balance Diagnostics & Association Testing

Open-source skill.

## Workflow

Read each step file in `workflow/` before executing that step.

| Step | File | Executor | Output |
|---|---|---|---|
| Collect | `workflow/01-collect-inputs.md` | Main Agent | Structured input summary |
| Diagnose | `workflow/02-check-distribution.md` | Main Agent | PART 1 code block |
| Test | `workflow/03-run-primary-test.md` | Main Agent | PART 2-3 code blocks |

## Decision Tree

```
1. CHECK CLASS BALANCE
   ├── Balanced (minority ≥ 10%) → standard tests
   └── Imbalanced (minority < 10%) → rare event warning, note power limits

2. PRIMARY ASSOCIATION TEST
   ├── All cells ≥ 5 → Chi-square + Cramer's V + OR
   └── Any cell < 5 → Fisher's exact + OR
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Outcome (Y)** | Variable name, what 0/1 represents |
| **Primary group variable** | What defines groups, how many levels |
| **Predictors** | For recommendation block (not executed) |
| **Covariates** | For recommendation block (not executed) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Class Balance Diagnostics  → plot_01_class_balance.png
PART 2: Primary Association Test   → plot_02_mosaic_[var].png
PART 3: Recommendation Block       → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: Cramer's V (chi-square), odds ratio with 95% CI
3. Odds ratios: always as "OR = X.XX, 95% CI [X.XX, X.XX]"
4. Proportions: report as percentages with 1 decimal
5. Chi-square: chi-sq(df) = X.XX, p = .XXX, Cramer's V = .XXX
6. Degrees of freedom: always with chi-square statistic
7. Sample size: final analytic N
8. Decimal places: 1 for proportions, 2 for OR, 3 for p and effect sizes
9. Non-significance: "not statistically significant at alpha = .05" --- never "no association"

## Association Tests

| Scenario | Expected cells all >= 5 | Any expected cell < 5 |
|---|---|---|
| 2x2 or 2xK | Chi-square + Cramer's V | Fisher's exact test |

Paired/matched binary designs -> `vera-stat-repeated-testing` (handles within-subject comparisons including paired binary data via McNemar's test).

## Example Dataset

R built-in `Titanic` (convert to data frame): outcome = Survived (0/1), predictors = Class, Sex, Age.
Python: `sm.datasets.get_rdataset("Titanic").data` or reconstruct from counts (offline fallback uses base R `Titanic` dataset).

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (class balance + mosaic/grouped bar)
└── recommendations → text block (additional analyses available)
```
