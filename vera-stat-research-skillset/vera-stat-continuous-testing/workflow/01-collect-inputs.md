# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Outcome variable** — the continuous DV
   - Name, units, what it measures

3. **Group variable** — for hypothesis testing
   - What defines groups (e.g., treatment vs control, gender, categories)
   - How many levels? (2 → t-test path, 3+ → ANOVA path)

## Optional (collect for recommendation quality)

4. **Primary predictor(s)** — for regression recommendation
5. **Covariates/controls** — adjustment variables
6. **Subgroup variable** — for subgroup analysis recommendation
7. **Sample size** — if not evident from data

## Validation Checkpoint

- [ ] Outcome is truly continuous (not ordinal, not count)
- [ ] If outcome looks like count data (integers, floor at 0), flagged and confirmed
- [ ] If outcome is bounded (0-100 scale), noted for distribution check
- [ ] If N < 20, power limitation warning issued
- [ ] Group variable levels identified (2 or 3+)
- [ ] At least outcome + group variable collected

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
outcome_var: {name, units, description}
group_var: {name, levels, n_levels}
predictors: [{name, type}]  # for recommendation block
covariates: [{name, type}]  # for recommendation block
subgroup_var: {name} or null
sample_size: N or "unknown"
data_source: {file_path | description | variable_list}
```
