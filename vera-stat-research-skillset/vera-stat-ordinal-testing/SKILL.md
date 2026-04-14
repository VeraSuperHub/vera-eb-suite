---
name: vera-stat-ordinal-testing
description: >-
  Runs distribution diagnostics and primary hypothesis tests for ordinal
  outcome variables. Produces frequency tables, cumulative proportions,
  ordinal bar chart, and one fully interpreted nonparametric group
  comparison (Mann-Whitney U for 2 groups or Kruskal-Wallis for 3+
  groups) with effect sizes (rank-biserial r or Cliff's delta) and
  Jonckheere-Terpstra trend test. Ends with a recommendation block
  listing additional analyses available. Outputs .R and
  .py scripts with 2 publication-quality plots. Triggered when user has
  an ordinal outcome and says "ordinal outcome," "Likert scale," "ordered
  categories," "rating scale," "severity levels," "none/mild/moderate/
  severe," "low/medium/high," "improvement levels," "ranked outcome,"
  "ordered factor," or names an ordinal variable like satisfaction,
  severity, agreement, stage, grade, rating. Does not handle continuous,
  binary, count, survival, repeated measures, or SEM outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Ordinal Outcome — Distribution Diagnostics & Hypothesis Testing

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
   ├── Balanced levels (no cell < 5) → standard nonparametric tests
   └── Sparse levels (any cell < 5) → warn, consider collapsing levels

2. GROUP COMPARISON
   ├── 2 groups → Mann-Whitney U + rank-biserial r
   └── 3+ groups → Kruskal-Wallis + pairwise Dunn's + Cliff's delta

3. TREND TEST (if predictor is ordered)
   └── Jonckheere-Terpstra trend test
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Outcome (Y)** | Variable name, ordered levels (confirm ordering with user) |
| **Group variable** | What defines groups, how many levels |
| **Predictors** | For recommendation block (not executed) |
| **Covariates** | For recommendation block (not executed) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Distribution Diagnostics → plot_01_ordinal_distribution.png
PART 2: Primary Hypothesis Test  → plot_02_stacked_bar_[var].png
PART 3: Recommendation Block     → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: rank-biserial r (Mann-Whitney), Cliff's delta (2 groups), epsilon-squared (Kruskal-Wallis)
3. Always report medians and IQRs for ordinal data, not means/SDs
4. Mann-Whitney U: U = X, p = .XXX, rank-biserial r = .XXX
5. Kruskal-Wallis: H(df) = X.XX, p = .XXX
6. Proportions per level: report as percentages with 1 decimal
7. Non-significance: "not statistically significant at α = .05" — never "no effect"

## Hypothesis Tests

| Scenario | Test | Effect Size |
|---|---|---|
| 2 independent groups | Mann-Whitney U | Rank-biserial r |
| 3+ independent groups | Kruskal-Wallis + Dunn's | Cliff's delta (pairwise) |
| Ordered groups (trend) | Jonckheere-Terpstra | — |

Paired/repeated designs → `vera-stat-repeated-testing`.

## Example Dataset

R: `vcd::Arthritis` — Outcome = Improvement (None/Some/Marked), Predictors: Treatment, Sex, Age.
Python: reconstruct via `statsmodels.datasets` or manual construction from R dataset.

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (ordinal distribution + stacked bar)
└── recommendations → text block (additional analyses available)
```
