---
name: vera-stat-survival-testing
description: >-
  Runs survival diagnostics and primary hypothesis tests for right-censored
  time-to-event outcome variables. Produces follow-up time summary, censoring
  rate assessment, Kaplan-Meier survival curves with number-at-risk tables,
  log-rank test for group comparison with median survival times and landmark
  survival rates, and hazard ratio preview from univariate Cox regression.
  Ends with a recommendation block listing additional analyses available via
  the full analysis pipeline. Outputs .R and .py scripts with publication-quality plots.
  Triggered when user has a survival or time-to-event outcome and says
  "survival outcome," "time to event," "right-censored," "censored,"
  "Kaplan-Meier," "hazard," "death," "failure," "duration," "event time,"
  "follow-up," or names a survival variable like time, status, event,
  survival, OS, PFS, DFS. Handles right-censored survival data only. Does
  not handle left-censoring, interval-censoring, or competing risks. Does
  not handle binary, count, continuous, ordinal, repeated measures, or SEM
  outcomes.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Survival Outcome — Diagnostics & Hypothesis Testing

Open-source skill.

## Scope

**Right-censored survival data only.** This skill handles the standard
scenario where observation ends before the event occurs (censored) or
the event is observed (event). It does not handle left-censoring,
interval-censoring, or competing risks.

## Workflow

Read each step file in `workflow/` before executing that step.

| Step | File | Executor | Output |
|---|---|---|---|
| Collect | `workflow/01-collect-inputs.md` | Main Agent | Structured input summary |
| Diagnose | `workflow/02-check-distribution.md` | Main Agent | PART 1 code block |
| Test | `workflow/03-run-primary-test.md` | Main Agent | PART 2-3 code blocks |

## Decision Tree

```
1. CHECK FOLLOW-UP & CENSORING
   ├── Censoring rate > 80% → Warning: limited events, wide CIs expected
   ├── Censoring rate < 5% → Note: standard regression may suffice
   └── Otherwise → proceed normally

2. GROUP COMPARISON
   ├── 2 groups → Log-rank test + HR from univariate Cox
   └── 3+ groups → Log-rank test + pairwise log-rank (Bonferroni)
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Time variable** | Continuous, ≥0, follow-up/survival time |
| **Event indicator** | Which value = event occurred, which = censored |
| **Group variable** | What defines groups, how many levels |
| **Predictors** | For recommendation block (not executed) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Follow-Up & Censoring Diagnostics → plot_01_km_overall.png, plot_01b_event_histogram.png
PART 2: Primary Hypothesis Test           → plot_02_km_groups.png
PART 3: Recommendation Block              → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. Hazard ratio: HR with 95% CI, "HR = X.XX, 95% CI [X.XX, X.XX]"
3. Median survival: always with 95% CI
4. Survival rates at landmarks: with 95% CI
5. Censoring: always report % censored overall and by group
6. Log-rank: chi-sq(df) = X.XX, p = .XXX
7. Decimal places: 2 for median survival, 3 for p and HR
8. Non-significance: "not statistically significant at alpha = .05" — never "no effect"

## Hypothesis Tests

| Scenario | Test |
|---|---|
| 2 independent groups | Log-rank + univariate Cox HR |
| 3+ independent groups | Log-rank + pairwise log-rank (Bonferroni) |

Paired/clustered designs are out of scope for this version.

## Example Dataset

R built-in `survival::lung`: outcome = time (survival time), status (1=censored, 2=dead).
Predictors: age, sex, ph.ecog, ph.karno, pat.karno, meal.cal, wt.loss.
Python: `from lifelines.datasets import load_lung` or reconstruct from R.

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (KM overall + KM groups)
└── recommendations → text block (additional analyses available)
```
