# 01 --- Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** --- one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Outcome variable** --- the binary DV
   - Name, what 0 and 1 represent (e.g., Survived: 0 = No, 1 = Yes)
   - Confirm truly binary (not ordinal, not multi-class)

3. **Primary group variable** --- for association testing
   - What defines groups (e.g., Sex, Treatment, Class)
   - How many levels? (2 → 2x2 table, 3+ → 2xK table)

## Optional (collect for recommendation quality)

4. **Additional predictors** --- for logistic regression recommendation
5. **Covariates/controls** --- adjustment variables
6. **Subgroup variable** --- for stratified analysis recommendation
7. **Sample size** --- if not evident from data

## Validation Checkpoint

- [ ] Outcome is truly binary (0/1, yes/no, two categories only)
- [ ] If outcome has more than 2 levels, flagged and confirmed or reclassified
- [ ] If outcome is survival time (not just event), redirected to survival analysis
- [ ] If N < 20, power limitation warning issued
- [ ] Primary group variable levels identified (2 or 3+)
- [ ] At least outcome + primary group variable collected

## Data Out -> 02-check-distribution.md

Structured input summary containing:
```
outcome_var: {name, level_0_label, level_1_label}
group_var: {name, levels, n_levels}
predictors: [{name, type}]  # for recommendation block
covariates: [{name, type}]  # for recommendation block
subgroup_var: {name} or null
sample_size: N or "unknown"
data_source: {file_path | description | variable_list}
```
