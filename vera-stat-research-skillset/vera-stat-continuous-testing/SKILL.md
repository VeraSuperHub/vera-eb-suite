---
name: vera-stat-continuous-testing
description: >-
  Runs distribution diagnostics and primary hypothesis tests for continuous
  outcome variables. Produces Shapiro-Wilk normality check, skewness,
  kurtosis, Q-Q plot, and one fully interpreted group comparison (Welch's t
  for 2 groups or ANOVA with Tukey HSD for 3+ groups) with effect sizes and
  nonparametric confirmation. Ends with a recommendation block listing
  Outputs .R and .py scripts
  with 2 publication-quality plots. Triggered when user has a
  continuous/numeric outcome and says "analyze continuous outcome," "my DV is
  numeric," "compare group means," or names a continuous variable like
  weight, score, income, time, cost, mpg, blood pressure. Does not handle
  binary, count, survival, ordinal, repeated measures, or SEM outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Continuous Outcome — Distribution Diagnostics & Hypothesis Testing

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
1. CHECK DISTRIBUTION
   ├── Normal (Shapiro-Wilk p ≥ .05, |skewness| < 1) → parametric primary
   └── Non-normal → nonparametric primary + recommend QR/trees

2. GROUP COMPARISON
   ├── 2 groups → Welch's t + Cohen's d + Mann-Whitney U
   └── 3+ groups → ANOVA + η² + Tukey HSD + Kruskal-Wallis
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Outcome (Y)** | Variable name, units, what it measures |
| **Group variable** | What defines groups, how many levels |
| **Predictors** | For recommendation block (not executed) |
| **Covariates** | For recommendation block (not executed) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Distribution Diagnostics → plot_01_distribution.png
PART 2: Primary Hypothesis Test  → plot_02_boxplot_[var].png
PART 3: Recommendation Block     → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: Cohen's d (t-test), η² (ANOVA) — always alongside p
3. 95% CIs: always for mean differences
4. Degrees of freedom: always with t and F statistics
5. Sample size: final analytic N
6. Decimal places: 2 for M/SD, 3 for p and effect sizes
7. Non-significance: "not statistically significant at α = .05" — never "no effect"

## Hypothesis Tests

| Scenario | Normal | Non-Normal |
|---|---|---|
| 2 independent groups | Welch's t | Mann-Whitney U |
| 3+ independent groups | ANOVA + Tukey HSD | Kruskal-Wallis + Dunn's |

Paired/repeated designs → `vera-stat-repeated-testing`.

## Example Dataset

R built-in `mtcars`: outcome = mpg, 2-group = am, 3+ group = cyl.
Python: `sm.datasets.get_rdataset("mtcars").data` (with offline fallback to bundled `examples/mtcars.csv`).

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (distribution + boxplot)
└── recommendations → text block (additional analyses available)
```
