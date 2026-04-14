---
name: vera-stat-repeated-testing
description: >-
  Trajectory diagnostics and primary hypothesis tests for repeated measures /
  longitudinal designs with a continuous outcome. Produces spaghetti plots with
  group mean ribbons, ICC, descriptives per time point, attrition check, and
  one interpreted test: paired t-test for 2 time points, repeated measures
  ANOVA for 3+ time points in one group, or mixed ANOVA (time x group) for 3+
  time points with 2+ groups, including Mauchly sphericity and Greenhouse-Geisser
  correction. Ends with a recommendation block. Outputs .R and .py scripts with
  publication-quality plots. Trigger when user has a continuous outcome measured
  on the same subjects over time and says "repeated measures," "longitudinal,"
  "within-subjects," "pre-post," "paired," "panel data," "growth curve,"
  "multilevel," "mixed model," or "correlated observations." Does not handle
  binary, count, survival, ordinal, or cross-sectional outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Repeated Measures Outcome — Trajectory Diagnostics & Hypothesis Testing

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
1. DATA FORMAT CHECK
   ├── Wide → reshape to long before proceeding
   └── Long → continue

2. TIME POINTS
   ├── Exactly 2 → paired comparisons path
   └── 3+ → repeated measures ANOVA / mixed ANOVA path

3. GROUP STRUCTURE
   ├── No between-subjects factor → one-way RM-ANOVA (within-subjects only)
   └── Between-subjects factor → mixed ANOVA (time × group)

4. SPHERICITY (if 3+ time points)
   ├── Mauchly p ≥ .05 → uncorrected F
   └── Mauchly p < .05 → Greenhouse-Geisser / Huynh-Feldt correction
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Outcome (Y)** | Variable name, units, what it measures (continuous) |
| **Time variable** | Measurement occasions, how many, equally spaced? |
| **Subject/ID variable** | What identifies the same individual across time |
| **Group variable** | Between-subjects factor (treatment, condition, etc.) |
| **Covariates** | Time-varying? Time-invariant? |
| **Data format** | Long (one row per obs) or wide (one row per subject) |

## Code Structure

```
PART 0: Setup & Data Loading (+ reshape if wide)
PART 1: Trajectory Diagnostics → plot_01_trajectories.png
PART 2: Primary Hypothesis Test → plot_02_interaction.png
PART 3: Recommendation Block   → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Effect sizes: Cohen's d (paired t-test), partial eta-squared (RM-ANOVA/mixed ANOVA)
3. 95% CIs: always for mean differences
4. Degrees of freedom: always with t and F statistics
5. Sphericity: Mauchly's W, p; if violated, GG epsilon and corrected p
6. ICC: report value with interpretation
7. Sample size: final analytic N (subjects) and total observations
8. Decimal places: 2 for M/SD, 3 for p and effect sizes
9. Non-significance: "not statistically significant at alpha = .05" — never "no effect"

## Hypothesis Tests

| Scenario | Normal | Non-Normal |
|---|---|---|
| 2 time points (paired) | Paired t-test | Wilcoxon signed-rank |
| 3+ time points, 1 group | One-way RM-ANOVA + sphericity | Friedman test |
| 3+ time points, 2+ groups | Mixed ANOVA (time x group) | — |

Cross-sectional group comparisons → `vera-stat-continuous-testing`.

## Example Dataset

R built-in `ChickWeight`: outcome = weight, time = Time (0, 2, 4, ..., 21 days),
subject = Chick, group = Diet (1, 2, 3, 4).
Python: `sm.datasets.get_rdataset("ChickWeight").data` (with offline fallback to bundled `examples/chickweight.csv`).

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (trajectories + interaction)
└── recommendations → text block (additional analyses available)
```
