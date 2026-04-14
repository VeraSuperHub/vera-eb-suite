# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Outcome variable** — the continuous DV measured repeatedly
   - Name, units, what it measures
   - If outcome is binary, count, or ordinal: redirect to the respective outcome skill with a note about clustering/repeated structure

3. **Time / occasion variable** — when measurements were taken
   - What are the measurement points? (e.g., 0, 2, 4, ... 21 days; baseline, 6mo, 12mo)
   - How many time points?
   - Equally spaced or unequal intervals?

4. **Subject / ID variable** — what identifies the same individual across time
   - Unique ID per subject

5. **Between-subjects grouping variable** — for group comparisons
   - Treatment, condition, diet, etc.
   - How many levels? (0 → pure within-subjects, 2+ → mixed design)

6. **Data format** — LONG or WIDE?
   - Long: one row per observation (subject × time)
   - Wide: one row per subject, time points as separate columns
   - If wide: note that conversion to long is needed before analysis

## Optional (collect for recommendation quality)

7. **Covariates** — time-varying or time-invariant?
   - Time-varying: changes at each measurement (e.g., daily stress)
   - Time-invariant: constant across time (e.g., sex, baseline age)
8. **Number of subjects** — if not evident from data
9. **Attrition / missing data** — any dropout? monotone or intermittent?
10. **Research question** — "does the outcome change over time?" vs "does group moderate the trajectory?"

## Validation Checkpoint

- [ ] Outcome is truly continuous (not ordinal, not count, not binary)
- [ ] If outcome looks like count data (integers, floor at 0), flagged and confirmed
- [ ] Time variable identified with specific measurement occasions listed
- [ ] Subject/ID variable identified
- [ ] Between-subjects factor identified (or confirmed as none)
- [ ] Data format confirmed (long or wide)
- [ ] If wide format, reshape plan noted
- [ ] Number of time points known (2 vs 3+; determines test path)
- [ ] If N < 20 subjects, power limitation warning issued
- [ ] If attrition > 20%, flagged for mixed model recommendation

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
outcome_var: {name, units, description}
time_var: {name, time_points, n_timepoints, equal_spacing}
subject_var: {name}
group_var: {name, levels, n_levels} or null
covariates: [{name, type: "time_varying" | "time_invariant"}]
data_format: "long" | "wide"
n_subjects: N or "unknown"
attrition_flag: true | false | "unknown"
data_source: {file_path | description | variable_list}
design: "paired" | "rm_anova" | "mixed_anova"
```
