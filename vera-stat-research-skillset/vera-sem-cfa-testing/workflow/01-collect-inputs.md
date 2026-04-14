# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Factor structure** — which indicators belong to each latent factor
   - Factor names and indicator variable names
   - Syntax: `factor_1 =~ y1 + y2 + y3`
   - Minimum 3 indicators per factor preferred

2. **Indicator type** — determines estimator choice
   - Continuous (interval-scaled)
   - Ordinal (Likert or ordered categorical)
   - Binary (dichotomous)

3. **Sample size** — total analytic N after listwise/FIML

4. **Data source** — one of:
   - CSV/data file uploaded
   - Covariance matrix + N
   - Dataset description with variable names

## Optional (collect for recommendation quality)

5. **Grouping variable** — if measurement invariance testing may follow
6. **Correlated errors** — any theoretically justified error covariances
7. **Higher-order factors** — if hierarchical CFA is intended
8. **Missing data pattern** — MCAR/MAR assumption, proportion missing

## Validation Checkpoint

- [ ] At least one latent factor defined with 2+ indicators
- [ ] Indicator measurement level identified (continuous/ordinal/binary)
- [ ] Sample size collected or derivable from data
- [ ] If any factor has only 2 indicators, flagged for identification constraint
- [ ] If only 1 factor with 3 indicators, noted as just-identified (df = 0)
- [ ] Data source confirmed (file, matrix, or variable list)

## Data Out → 02-check-measurement-setup.md

Structured input summary containing:
```
factors:
  - factor_1 =~ y1 + y2 + y3
  - factor_2 =~ y4 + y5 + y6
indicator_type: ordinal | continuous | binary
sample_size: N
estimator_candidate: ML | MLR | WLSMV | DWLS
grouping_var: {name} or null
correlated_errors: [] or [{e1 ~~ e2}]
data_source: {file_path | cov_matrix | variable_list}
```
