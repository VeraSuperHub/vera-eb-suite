---
name: vera-stat-multivariate-testing
description: >-
  Multivariate diagnostics and primary hypothesis tests for multiple continuous
  outcomes analyzed simultaneously. Produces multivariate normality (Mardia,
  Henze-Zirkler), Box's M test, scatterplot matrix, correlation matrix, and one
  multivariate group comparison (Hotelling's T-squared for 2 groups or one-way
  MANOVA with all four test statistics for 3+ groups) with partial eta-squared
  per DV and univariate follow-up ANOVAs. Ends with a recommendation block.
  Outputs .R and .py scripts with publication-quality plots. Trigger when user
  has multiple continuous outcomes and says "multiple outcomes," "multivariate,"
  "MANOVA," "multiple dependent variables," "Hotelling," "canonical correlation,"
  "profile analysis," or names 2+ continuous variables as outcomes. Does not
  handle single DV, repeated measures, or SEM outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Multivariate Outcome — Distribution Diagnostics & Hypothesis Testing

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
1. CHECK MULTIVARIATE DISTRIBUTION
   ├── Mardia skewness p >= .05 AND Mardia kurtosis p >= .05 → multivariate normal
   └── Either p < .05 → note violation, Pillai's Trace is robust

2. CHECK COVARIANCE EQUALITY
   ├── Box's M p >= .001 (strict alpha) → covariance matrices equal
   └── Box's M p < .001 → note violation, Pillai's Trace is robust

3. GROUP COMPARISON
   ├── 2 groups → Hotelling's T² + F approximation + individual ANOVAs
   └── 3+ groups → One-way MANOVA (all 4 statistics) + discriminant follow-up
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Outcomes (Y₁..Yₖ)** | 2+ continuous variable names, what they measure |
| **Group variable** | What defines groups, how many levels |
| **Predictors** | For recommendation block (not executed) |
| **Covariates** | For recommendation block (not executed) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Multivariate Distribution Diagnostics → plot_01_scattermatrix.png
PART 2: Primary Multivariate Test             → plot_02_groupmeans.png
PART 3: Recommendation Block                  → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: partial eta-squared per DV in follow-up ANOVAs
3. 95% CIs: always for mean differences in univariate follow-ups
4. Degrees of freedom: always with F statistics
5. Sample size: final analytic N
6. Decimal places: 2 for M/SD, 3 for p and effect sizes
7. Non-significance: "not statistically significant at alpha = .05" — never "no effect"
8. MANOVA statistics: report all four (Pillai's V, Wilks' Lambda, Hotelling-Lawley T, Roy's theta) with F approximation and p
9. Box's M: report with F approximation and p, use strict alpha (.001)

## Hypothesis Tests

| Scenario | Test | Follow-Up |
|---|---|---|
| 2 independent groups | Hotelling's T² | Individual Welch's t per DV |
| 3+ independent groups | One-way MANOVA | Individual ANOVAs per DV |

Paired/repeated multivariate → `vera-stat-repeated-testing`.
Single DV → `vera-stat-continuous-testing`.

## Example Dataset

R built-in `iris`: outcomes = Sepal.Length, Sepal.Width, Petal.Length, Petal.Width; group = Species.
Python: `from sklearn.datasets import load_iris`.

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (scattermatrix + group means)
└── recommendations → text block (additional analyses available)
```
