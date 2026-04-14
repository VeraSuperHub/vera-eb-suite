# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Outcome variable** — the nominal DV
   - Name, what categories represent
   - Confirm categories have NO natural ordering
   - List all category levels

3. **Number of levels** — confirm 3+ unordered categories
   - If only 2 levels → redirect to `vera-stat-binary-testing`
   - If levels are ordered → redirect to `vera-stat-ordinal-testing`

4. **Primary predictor** — for the association test
   - Name, type (categorical or continuous)
   - If categorical: how many levels

## Optional (collect for recommendation quality)

5. **Additional predictors** — for multinomial regression recommendation
6. **Covariates/controls** — adjustment variables
7. **Subgroup variable** — for subgroup analysis recommendation
8. **Sample size** — if not evident from data
9. **Research question** — helps tailor recommendations

## Validation Checkpoint

- [ ] Outcome is truly nominal (unordered categories)
- [ ] If only 2 levels, redirected to binary skill
- [ ] If levels are ordered (Likert, severity, education), redirected to ordinal skill
- [ ] 3+ category levels confirmed and listed
- [ ] Primary predictor identified with type (categorical/continuous)
- [ ] If any class has very few observations, noted for rare-class warning
- [ ] At least outcome + primary predictor collected

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
outcome_var: {name, levels, n_levels, description}
outcome_ordering: "none — nominal"
primary_predictor: {name, type, levels_if_categorical}
predictors: [{name, type}]  # for recommendation block
covariates: [{name, type}]  # for recommendation block
subgroup_var: {name} or null
sample_size: N or "unknown"
data_source: {file_path | description | variable_list}
```
