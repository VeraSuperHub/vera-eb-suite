---
name: vera-stat-meta-testing
description: >-
  Runs study-level diagnostics and primary pooled estimation for
  meta-analysis of summary statistics across multiple studies. Produces
  forest plot, heterogeneity assessment (Q, I-squared, tau-squared),
  pooled estimates under both fixed-effects and random-effects models,
  and prediction interval. Ends with a recommendation block listing
  Outputs .R and .py
  scripts with 1 publication-quality forest plot. Triggered when user
  says "meta-analysis," "systematic review," "pooled estimate," "combine
  studies," "forest plot," "heterogeneity," "I-squared," "effect size
  synthesis," or "aggregate results across studies." Does not handle
  network meta-analysis or individual participant data.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Meta-Analysis — Diagnostics & Primary Pooled Estimation

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
1. EFFECT SIZE TYPE
   ├── Continuous (SMD, MD) → escalc(measure="SMD") or "MD"
   ├── Binary (OR, RR, RD) → escalc(measure="OR") or "RR"/"RD"
   └── Correlation (r) → escalc(measure="ZCOR") Fisher z transform

2. HETEROGENEITY ASSESSMENT
   ├── I² < 25% → low heterogeneity (fixed-effects may suffice)
   ├── 25% ≤ I² ≤ 75% → moderate (random-effects preferred)
   └── I² > 75% → high (random-effects + moderator analysis needed)
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Study data** | Study ID, effect size, SE (or CI, or N per group + means/SDs) |
| **Effect type** | SMD, MD, OR, RR, RD, or r |
| **Moderators** | Study-level variables (year, quality, setting) — for recommendation |
| **Model preference** | Fixed vs random (or let data decide) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Study Table + Forest Plot + Heterogeneity → plot_01_forest.png
PART 2: Pooled Estimates (fixed + random) + Prediction Interval
PART 3: Recommendation Block → text listing additional analyses available
```

## Reporting Standards

1. Pooled effect: "pooled ES = X.XX, 95% CI [X.XX, X.XX], z = X.XX, p"
2. Heterogeneity: "Q(df) = X.XX, p = .XXX; I² = XX.X%; tau² = X.XX"
3. Prediction interval: always alongside CI
4. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
5. Weights: report study weights in forest plot
6. Degrees of freedom: always with test statistics
7. Sample size: report total N across studies and k (number of studies)
8. Decimal places: 2 for effect sizes, 3 for p-values, 1 for I²

## Example Dataset

Constructed example: 10 studies comparing treatment vs control on a
continuous outcome (standardized mean difference). NOT a built-in R
dataset — create a data frame with study_id, n_treatment, n_control,
mean_treatment, mean_control, sd_treatment, sd_control.

R: `metafor` package. Python: `statsmodels` or custom inverse-variance.

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 1 PNG (forest plot)
└── recommendations → text block (additional analyses available)
```
