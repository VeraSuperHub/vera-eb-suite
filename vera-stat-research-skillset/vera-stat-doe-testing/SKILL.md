---
name: vera-stat-doe-testing
description: >-
  Runs distribution diagnostics and primary analysis for designed experiments
  (DOE) with controlled factors. Produces cell descriptives, balance check,
  residual normality, Levene's test, full factorial ANOVA (Type III SS) with
  partial eta-squared, interaction plots, and Tukey HSD / simple effects
  post-hoc. Outputs .R and .py scripts with 2
  publication-quality plots. Triggered when user mentions "experimental
  design," "DOE," "factorial design," "treatment effects," "blocking,"
  "randomized experiment," "split-plot," "response surface," "2^k factorial,"
  "main effects and interactions," "Latin square," "fractional factorial,"
  "CRD," "RCBD," or describes manipulated factors. Does not handle
  observational studies, repeated measures, or SEM outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Design of Experiments — Diagnostics & Primary Analysis

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
1. CHECK DESIGN
   ├── Balanced (equal N per cell) → standard ANOVA
   └── Unbalanced → Type III SS mandatory

2. CHECK RESIDUALS
   ├── Normal residuals + equal variances → factorial ANOVA
   └── Non-normal / heteroscedastic → flag, proceed with caution + recommend transformations

3. FACTORIAL ANOVA
   ├── Significant main effects → Tukey HSD post-hoc
   └── Significant interactions → simple effects analysis
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Response (Y)** | Variable name, units, what it measures |
| **Factors** | Names, levels, type (fixed/random) |
| **Design type** | CRD, RCBD, factorial, fractional, split-plot, Latin square |
| **Blocking variable** | If RCBD or similar |
| **Replication info** | Replicates per cell, total N |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Design Diagnostics        → plot_01_interaction.png
PART 2: Factorial ANOVA + Post-hoc → plot_02_effects.png
PART 3: Recommendation Block       → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: partial eta-squared always alongside F-tests
3. SS Type III always for unbalanced designs
4. F(df1, df2) = X.XX, p, partial eta-squared
5. Effect estimates with SE
6. Degrees of freedom: always with F statistics
7. Sample size: final analytic N and cell sizes
8. Decimal places: 2 for M/SD, 3 for p and effect sizes
9. Non-significance: "not statistically significant at alpha = .05" -- never "no effect"
10. Design resolution for fractional factorial (in recommendation)

## Hypothesis Tests

| Scenario | Method |
|---|---|
| Main effects | F-test from factorial ANOVA |
| Interactions | F-test for each interaction term |
| Post-hoc (main effects) | Tukey HSD (all pairwise) |
| Post-hoc (interactions) | Simple effects (effect of A at each level of B) |
| Variance homogeneity | Levene's test |
| Residual normality | Shapiro-Wilk on residuals |

## Example Dataset

R built-in `npk`: 24 observations, N/P/K fertilizer treatments (2^3 factorial)
on pea yield, blocked by block. Classic agricultural DOE.
Python: `sm.datasets.get_rdataset("npk").data` (with offline fallback to bundled `examples/npk.csv`).

Alternative: `warpbreaks` -- wool x tension factorial on breaks.

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (interaction plot + effects plot)
└── recommendations → text block (additional analyses available)
```
