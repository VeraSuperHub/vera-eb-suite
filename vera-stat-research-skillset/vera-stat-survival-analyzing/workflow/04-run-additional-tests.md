# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-survival-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Univariate Cox Screening

### For each predictor separately:
1. Univariate Cox: Surv(time, status) ~ predictor
2. Report: HR, 95% CI, Wald p, concordance index
3. For continuous predictors:
   - Check linearity assumption via Martingale residual plot
   - Plot Martingale residuals (from null model) vs predictor
   - If nonlinear pattern visible → note for potential transformation or spline
4. For categorical predictors:
   - KM curves per level + log-rank test
   - Median survival per level with 95% CI
   → `plot_03_km_[varname].png` for each

### Summary table of all univariate results:
```
| Predictor | HR | 95% CI | Wald p | C-index | Linearity |
|-----------|-----|--------|--------|---------|-----------|
| age       | 1.02 | [0.99, 1.04] | .120 | 0.54 | OK |
| sex       | 0.59 | [0.42, 0.82] | .002 | 0.58 | N/A (categorical) |
| ...       | ... | ... | ... | ... | ... |
```

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether HR or p-value leads the sentence
- Vary whether concordance is inline or separate sentence
- Vary descriptor vocabulary based on HR magnitude
- Include 0-1 methodological justifications per predictor (only when relevant)

## Validation Checkpoint

- [ ] Univariate Cox run for each predictor
- [ ] HR with 95% CI reported for every predictor
- [ ] Wald p reported for every predictor
- [ ] Concordance index reported for every predictor
- [ ] Martingale residual plot generated for continuous predictors
- [ ] KM curves generated for categorical predictors
- [ ] Summary table of all univariate HRs complete
- [ ] Linearity assessment noted for each continuous predictor
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out → 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_univariate: [methods paragraph prose]
results_para_univariate: [results paragraph prose]
univariate_table: [summary of all univariate HRs]
plots: [list of new plot filenames]
significant_predictors: [list of predictors with p < alpha]
```
