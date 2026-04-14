# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Outcome variables (2+)** — the continuous DVs
   - Names, units, what each measures
   - Confirm they are conceptually related (measured on same construct, same domain, or same measurement occasion)
   - If only 1 DV → redirect to `vera-stat-continuous-testing`

3. **Group variable** — for multivariate hypothesis testing
   - What defines groups (e.g., species, treatment condition, diagnosis)
   - How many levels? (2 → Hotelling's T² path, 3+ → MANOVA path)

## Optional (collect for recommendation quality)

4. **Primary predictor(s)** — for CCA / multivariate regression recommendation
5. **Covariates/controls** — for MANCOVA recommendation
6. **Second factor** — for two-way MANOVA recommendation
7. **Sample size** — if not evident from data

## Validation Checkpoint

- [ ] At least 2 outcome variables collected (all continuous)
- [ ] Outcomes are conceptually related (not arbitrary grouping)
- [ ] If outcomes look like count data (integers, floor at 0), flagged and confirmed
- [ ] If outcomes are on different scales, noted for profile analysis caveat
- [ ] If N < 20 per group, power limitation warning issued
- [ ] Group variable levels identified (2 or 3+)
- [ ] At least outcomes + group variable collected
- [ ] If only 1 DV, redirected to continuous skill

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
outcome_vars: [{name, units, description}, ...]   # 2+ entries
n_outcomes: k
group_var: {name, levels, n_levels}
predictors: [{name, type}]  # for recommendation block
covariates: [{name, type}]  # for recommendation block
second_factor: {name} or null
sample_size: N or "unknown"
data_source: {file_path | description | variable_list}
same_scale: TRUE | FALSE   # for profile analysis feasibility
```
