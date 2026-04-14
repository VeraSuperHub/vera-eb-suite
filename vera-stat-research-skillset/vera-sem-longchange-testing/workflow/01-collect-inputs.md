# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Repeated variable(s)** — what is measured at each wave
   - Variable name(s) and what they measure
   - If latent constructs repeat (e.g., depression at each wave), list indicators per wave

2. **Number of waves** — minimum 3 for growth modeling
   - Exact wave labels (t1, t2, t3, ... or time points)
   - Time intervals: equal or unequal spacing

3. **Subject identifier** — column name for individual ID

4. **Data shape** — wide (one row per person) or long (one row per observation)

5. **Sample size** — total N (individuals, not observations)

## Optional (collect for recommendation quality)

6. **Grouping variable** — if trajectory comparisons across groups needed
7. **Time-varying covariates** — variables that change with each wave
8. **Time-invariant predictors** — baseline variables predicting trajectory
9. **Model preference** — latent growth curve vs latent change score
10. **Missing data pattern** — attrition rate, assumed mechanism

## Validation Checkpoint

- [ ] At least 3 waves identified (2 waves → redirect to paired/repeated testing)
- [ ] Time spacing documented (equal or unequal with specific values)
- [ ] Data shape confirmed (wide preferred for lavaan growth models)
- [ ] Subject ID column identified
- [ ] Repeated measure is continuous (ordinal → may need threshold model)
- [ ] Sample size collected (minimum ~100 for stable growth estimates)
- [ ] If N < 50, power warning issued

## Data Out → 02-check-longitudinal-setup.md

Structured input summary containing:
```
construct: {name, description}
waves: [t1, t2, t3, ...]
n_waves: int
time_spacing: equal | unequal
time_values: [0, 1, 2] or [0, 6, 12, 24] (months)
data_shape: wide | long
subject_id: {column_name}
sample_size: N
grouping_var: {name} or null
model_candidate: linear_growth | latent_change_score
data_source: {file_path | description}
```
