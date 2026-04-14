# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Measurement model** — latent factors and their indicators
   - Factor names and indicator variable names
   - Syntax: `factor =~ y1 + y2 + y3`
   - At least 2 latent factors for a structural model to be meaningful

2. **Structural paths** — regressions among latent/observed variables
   - Syntax: `eta2 ~ eta1 + x1` (outcome ~ predictors)
   - Identify which paths represent mediation, direct effects, or control variables

3. **Indicator type** — continuous, ordinal, or binary

4. **Sample size** — total analytic N

5. **Data source** — CSV/data file, covariance matrix, or variable description

## Optional (collect for recommendation quality)

6. **Mediator variables** — label which latent variables serve as mediators
7. **Grouping variable** — if multigroup SEM may follow
8. **Covariates/controls** — observed exogenous variables in the structural part
9. **Goal** — explanation, prediction, or manuscript-ready inference
10. **Missing data pattern** — proportion and assumed mechanism (MCAR/MAR)

## Validation Checkpoint

- [ ] At least 2 latent factors defined with indicators
- [ ] At least 1 structural path specified
- [ ] Indicator measurement level identified
- [ ] Mediators clearly labeled (if any)
- [ ] Sample size collected or derivable from data
- [ ] Model is not just a CFA (has structural paths beyond factor correlations)

## Data Out → 02-check-model-setup.md

Structured input summary containing:
```
measurement_model:
  - factor_1 =~ y1 + y2 + y3
  - factor_2 =~ y4 + y5 + y6
structural_paths:
  - factor_2 ~ factor_1 + x1
  - outcome ~ factor_2
mediators: [factor_2] or []
indicator_type: continuous | ordinal | binary
sample_size: N
estimator_candidate: ML | MLR | WLSMV
grouping_var: {name} or null
goal: explanation | prediction | inference
data_source: {file_path | cov_matrix | variable_list}
```
