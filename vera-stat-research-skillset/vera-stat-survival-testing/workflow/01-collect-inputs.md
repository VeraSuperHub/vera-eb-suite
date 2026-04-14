# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Time variable** — the survival/follow-up time
   - Name, units (days, months, years), must be continuous and ≥0
   - Confirm: what does time=0 represent? (enrollment, diagnosis, surgery, etc.)

3. **Event/status indicator** — the censoring variable
   - Name, coding scheme
   - Which value = event occurred (e.g., 1=death, 2=dead)
   - Which value = censored (e.g., 0=alive, 1=censored)
   - Confirm explicit mapping before proceeding

4. **Group variable** — for survival comparison
   - What defines groups (e.g., treatment vs control, sex, stage)
   - How many levels? (2 → single log-rank, 3+ → pairwise log-rank)

5. **Confirm right-censoring** — ask explicitly:
   - "Is this right-censored data? (Subjects are followed until event or end of observation, whichever comes first.)"
   - If left-censored, interval-censored, or competing risks → redirect, this skill does not handle those

## Optional (collect for recommendation quality)

6. **Primary predictor(s)** — for Cox regression recommendation
7. **Covariates/controls** — adjustment variables
8. **Subgroup variable** — for stratified analysis recommendation
9. **Sample size** — if not evident from data
10. **Clinical context** — what is the event? (death, relapse, failure, etc.)

## Validation Checkpoint

- [ ] Time variable is truly continuous and ≥0
- [ ] Event indicator coding is unambiguous (event value vs censored value confirmed)
- [ ] Right-censoring confirmed explicitly
- [ ] If left-censoring, interval-censoring, or competing risks detected → redirected
- [ ] If total events < 10, power limitation warning issued
- [ ] If N < 30, small sample warning issued
- [ ] Group variable levels identified (2 or 3+)
- [ ] At least time + event + group variable collected

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
time_var: {name, units, description}
event_var: {name, event_value, censored_value}
group_var: {name, levels, n_levels}
predictors: [{name, type}]  # for recommendation block
covariates: [{name, type}]  # for recommendation block
subgroup_var: {name} or null
sample_size: N or "unknown"
event_description: "death" | "relapse" | "failure" | etc.
data_source: {file_path | description | variable_list}
censoring_type: "right"
```
