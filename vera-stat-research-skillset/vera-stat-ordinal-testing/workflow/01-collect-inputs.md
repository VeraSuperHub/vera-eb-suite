# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Outcome variable** — the ordinal DV
   - Name, ordered levels (list from lowest to highest)
   - Confirm ordering with user: "You stated the levels are [X < Y < Z]. Is this the correct order from lowest to highest?"
   - What it measures (e.g., severity, satisfaction, improvement)

3. **Group variable** — for hypothesis testing
   - What defines groups (e.g., treatment vs placebo, male vs female)
   - How many levels? (2 → Mann-Whitney path, 3+ → Kruskal-Wallis path)
   - Is the group variable itself ordered? (if yes → Jonckheere-Terpstra trend test)

## Optional (collect for recommendation quality)

4. **Additional predictors** — for regression recommendation
5. **Covariates/controls** — adjustment variables
6. **Subgroup variable** — for subgroup analysis recommendation
7. **Sample size** — if not evident from data

## Validation Checkpoint

- [ ] Outcome is truly ordinal (not continuous, not nominal)
- [ ] If outcome looks continuous (many unique values), flagged and confirmed
- [ ] If outcome is binary (only 2 levels), flagged — consider binary logistic instead
- [ ] Ordering of levels explicitly confirmed by user
- [ ] If any level has < 5 observations, sparse level warning issued
- [ ] If N < 20, power limitation warning issued
- [ ] Group variable levels identified (2 or 3+)
- [ ] At least outcome + group variable collected

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
outcome_var: {name, levels: [ordered list], n_levels, description}
group_var: {name, levels, n_levels, is_ordered}
predictors: [{name, type}]  # for recommendation block
covariates: [{name, type}]  # for recommendation block
subgroup_var: {name} or null
sample_size: N or "unknown"
data_source: {file_path | description | variable_list}
```
