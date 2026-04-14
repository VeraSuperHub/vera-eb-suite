---
name: vera-stat-nominal-testing
description: >-
  Runs class distribution diagnostics and primary association tests for
  nominal (unordered multi-class) outcome variables. Produces class frequency
  table, proportions, rare-class warnings, bar chart of class distribution,
  and one fully interpreted association test (Chi-square/Cramer's V for
  categorical predictors, or ANOVA/Kruskal-Wallis for continuous predictors)
  with effect sizes. Ends with a recommendation block listing additional
  analyses available. Outputs .R and .py scripts with
  2 publication-quality plots. Triggered when user has a nominal/unordered
  categorical outcome with 3+ levels and says "nominal outcome,"
  "multi-class," "categorical outcome no order," "unordered categories,"
  "species," "type classification," "which category," "multinomial," or
  names an unordered categorical variable like species, diagnosis type,
  transportation mode, region, product category. Does NOT handle binary
  (2-level), ordinal (ordered), continuous, count, survival, or SEM outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Nominal Outcome — Class Distribution Diagnostics & Primary Association Test

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
1. VALIDATE OUTCOME TYPE
   ├── Only 2 levels → redirect to vera-stat-binary-testing
   ├── Ordered levels → redirect to vera-stat-ordinal-testing
   └── 3+ unordered levels → proceed

2. PRIMARY ASSOCIATION TEST
   ├── Primary predictor is categorical → Chi-square + Cramér's V
   └── Primary predictor is continuous → One-way ANOVA (predictor ~ outcome) or Kruskal-Wallis
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Outcome (Y)** | Variable name, what categories represent, confirm NO ordering |
| **Number of levels** | Confirm 3+ unordered categories |
| **Primary predictor** | Variable name, type (categorical or continuous) |
| **Predictors** | For recommendation block (not executed) |
| **Covariates** | For recommendation block (not executed) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Class Distribution Diagnostics → plot_01_class_distribution.png
PART 2: Primary Association Test       → plot_02_association_[var].png
PART 3: Recommendation Block           → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: Cramer's V (Chi-square), eta-squared (ANOVA) — always alongside p
3. 95% CIs: always for effect sizes when available
4. Degrees of freedom: always with Chi-square and F statistics
5. Sample size: final analytic N
6. Decimal places: 2 for frequencies/proportions, 3 for p and effect sizes
7. Non-significance: "not statistically significant at alpha = .05" — never "no association"
8. Chi-square: report observed vs expected when informative
9. Always state which category is the reference (for later multinomial modeling)

## Association Tests

| Predictor Type | Primary Test | Confirmation |
|---|---|---|
| Categorical predictor | Chi-square + Cramer's V | Fisher's exact (if any cell < 5) |
| Continuous predictor | One-way ANOVA (predictor ~ outcome as factor) | Kruskal-Wallis |

## Example Dataset

R built-in `iris`: outcome = Species (setosa/versicolor/virginica, 3 unordered classes).
Predictors: Sepal.Length, Sepal.Width, Petal.Length, Petal.Width.
Python: `from sklearn.datasets import load_iris` (preferred — fully offline) or `sm.datasets.get_rdataset("iris")`.

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (class distribution + association plot)
└── recommendations → text block (additional analyses available)
```
