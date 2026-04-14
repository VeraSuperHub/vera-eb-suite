# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Outcome variable** — the count DV
   - Name, what it counts, units
   - Confirm: non-negative integers with no fixed upper bound

3. **Group variable** — for hypothesis testing
   - What defines groups (e.g., treatment vs control, wool type, region)
   - How many levels? (2 → rate test path, 3+ → regression LR test path)

4. **Exposure/offset variable** — CRITICAL for count sub-type detection
   - Ask: "Is there an exposure variable such as time at risk, population size, area, or observation period?"
   - If YES → rate model path (offset = log(exposure))
   - If NO → raw count model path
   - If unsure → help user decide based on study design

## Optional (collect for recommendation quality)

5. **Primary predictor(s)** — for regression recommendation
6. **Covariates/controls** — adjustment variables
7. **Subgroup variable** — for subgroup analysis recommendation
8. **Sample size** — if not evident from data

## Validation Checkpoint

- [ ] Outcome is truly count data (non-negative integers, no upper bound)
- [ ] If outcome looks continuous (decimals), flagged and redirected to continuous skill
- [ ] If outcome is binary (only 0/1), flagged and redirected to binary skill
- [ ] If outcome has a fixed upper bound (0-10 Likert), flagged and redirected to ordinal skill
- [ ] Exposure/offset status determined (present or absent)
- [ ] If exposure present: units recorded (person-days, population, area, etc.)
- [ ] If N < 20, power limitation warning issued
- [ ] Group variable levels identified (2 or 3+)
- [ ] At least outcome + group variable collected

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
outcome_var: {name, description, what_it_counts}
group_var: {name, levels, n_levels}
exposure_var: {name, units} or null
count_subtype: "event_count" | "event_rate"
predictors: [{name, type}]  # for recommendation block
covariates: [{name, type}]  # for recommendation block
subgroup_var: {name} or null
sample_size: N or "unknown"
data_source: {file_path | description | variable_list}
```
