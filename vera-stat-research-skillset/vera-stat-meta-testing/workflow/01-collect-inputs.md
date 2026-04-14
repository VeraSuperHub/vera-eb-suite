# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Study-level data** — one of:
   - CSV/data file with one row per study
   - Table pasted with study-level summary statistics
   - Individual study results described in text

2. **Per-study fields** — must have or be derivable:
   - Study ID (author/year or label)
   - Effect size (d, g, OR, RR, RD, r, MD) OR raw data to compute it
   - Standard error OR 95% CI OR sample sizes per group + means/SDs

3. **Effect size type** — confirm which metric:
   - Continuous outcomes: SMD (standardized mean difference) or MD (mean difference)
   - Binary outcomes: OR (odds ratio), RR (risk ratio), RD (risk difference)
   - Correlation: r (Pearson correlation)

4. **If raw means/SDs/Ns provided** — will compute effect sizes automatically:
   - n_treatment, mean_treatment, sd_treatment
   - n_control, mean_control, sd_control

## Optional (collect for recommendation quality)

5. **Model preference** — fixed-effects, random-effects, or "let data decide"
6. **Moderator variables** — study-level: year, quality score, setting, sample type, country, design
7. **Subgroup variable** — categorical moderator for subgroup analysis recommendation
8. **Continuous moderator** — for meta-regression recommendation
9. **Research question / hypothesis** — for framing

## Validation Checkpoint

- [ ] At least k = 3 studies provided (warn if fewer)
- [ ] Effect size type identified (SMD, MD, OR, RR, RD, or r)
- [ ] Each study has effect size + SE (or enough info to compute both)
- [ ] If raw data provided, confirm computation approach with user
- [ ] If k < 10, power limitation warning issued for moderator analyses
- [ ] If mix of adjusted and unadjusted effects, flagged and confirmed
- [ ] Study IDs are unique

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
studies: [{study_id, yi, sei, ni_t, ni_c, ...}]
effect_type: "SMD" | "MD" | "OR" | "RR" | "RD" | "ZCOR"
k: number_of_studies
total_n: sum of all study Ns
moderators: [{name, type: "categorical" | "continuous"}] or null
subgroup_var: {name} or null
model_preference: "fixed" | "random" | "both"
data_source: {file_path | table | description}
```
