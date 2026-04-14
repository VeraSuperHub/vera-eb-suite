---
name: vera-stat-count-testing
description: >-
  Runs distribution diagnostics and primary hypothesis tests for count
  outcome variables (non-negative integers with no upper bound). Produces
  frequency table, overdispersion assessment, zero-inflation check, bar
  chart of count distribution with Poisson overlay, and one fully
  interpreted group comparison (Poisson/NB rate test for 2 groups or
  Poisson/NB regression with likelihood ratio test for 3+ groups) with
  incidence rate ratios and nonparametric confirmation. Detects whether
  data are raw event counts or event rates with exposure/offset. Ends
  with a recommendation block listing additional analyses available via
  the full analysis pipeline. Outputs .R and .py scripts with 2 publication-quality
  plots. Triggered when user has a count/frequency outcome and says
  "count outcome," "number of events," "frequency," "how many,"
  "Poisson," "incidents," "occurrences," "integer outcome floor at zero,"
  "rate," "per capita," "per 1000." Does not handle binary, continuous,
  survival, ordinal, repeated measures, or SEM outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Count Outcome — Distribution Diagnostics & Hypothesis Testing

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
1. CHECK COUNT TYPE
   ├── Exposure variable exists → rate model path (offset = log(exposure))
   └── No exposure variable → count model path

2. CHECK DISTRIBUTION
   ├── Variance ≈ Mean (ratio < 1.5) → Poisson
   ├── Variance >> Mean (ratio ≥ 1.5) → Negative Binomial
   └── Excess zeros (>20%) → flag for Zero-Inflated models

3. GROUP COMPARISON
   ├── 2 groups → Poisson/NB rate test + IRR + Mann-Whitney U
   └── 3+ groups → Poisson/NB regression with group factor + LR test + Kruskal-Wallis
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Outcome (Y)** | Variable name, what it counts, units |
| **Group variable** | What defines groups, how many levels |
| **Exposure/offset** | Time at risk, population, area — or none |
| **Predictors** | For recommendation block (not executed) |
| **Covariates** | For recommendation block (not executed) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Distribution Diagnostics → plot_01_count_distribution.png
PART 2: Primary Hypothesis Test  → plot_02_mean_counts_[var].png
PART 3: Recommendation Block     → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: incidence rate ratio (IRR) with 95% CI — always alongside p
3. Overdispersion: report variance/mean ratio with interpretation
4. Rate: "X.XX events per [unit] of exposure" when applicable
5. Degrees of freedom: always with chi-square and LR test statistics
6. Sample size: final analytic N
7. Decimal places: 2 for means/SDs, 3 for p and IRR, 2 for rate ratios
8. Non-significance: "not statistically significant at α = .05" — never "no effect"

## Hypothesis Tests

| Scenario | Equidispersed | Overdispersed |
|---|---|---|
| 2 independent groups | Poisson rate test | Negative binomial test |
| 3+ independent groups | Poisson regression + LR test | NB regression + LR test |

Nonparametric confirmation: Mann-Whitney U (2 groups) or Kruskal-Wallis (3+).

Paired/repeated designs → `vera-stat-repeated-testing`.

## Example Dataset

R built-in `warpbreaks`: outcome = breaks (count), predictors: wool (A/B), tension (L/M/H).
Python: `sm.datasets.get_rdataset("warpbreaks").data` (with offline fallback to bundled `examples/warpbreaks.csv`).

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (count distribution + mean counts bar chart)
└── recommendations → text block (additional analyses available)
```
