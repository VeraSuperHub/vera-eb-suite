# 05 — Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no subgroup variable specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: Stratified KM Curves
For each level of the subgroup variable:
1. Subset data to that level
2. KM curves per group within the subgroup level
3. Median survival per group within each subgroup level with 95% CI
4. Skip subgroup levels with n < 5

### 5B: Stratified Cox
For each level of the subgroup variable:
1. Univariate Cox: Surv(time, status) ~ predictor (within subgroup level)
2. HR with 95% CI per subgroup level
3. Concordance per subgroup level

### 5C: Interaction Test
1. Fit full: Surv(time, status) ~ predictor * subgroup + covariates
2. Fit reduced: Surv(time, status) ~ predictor + subgroup + covariates
3. Likelihood ratio test comparing models
4. Interpret: significant → "the effect of [predictor] on survival differed by [subgroup]"; non-significant → "the effect was consistent across subgroups"

### 5D: Visualizations
1. **Forest plot**: subgroup-specific HRs + CIs + overall diamond
   - Diamond for overall HR, circles for subgroup HRs, size proportional to n
   - Dashed vertical line at HR=1 (null)
   - Include p-value for interaction
   → `plot_XX_subgroup_forest.png`

2. **Stratified KM curves**
   - Faceted or overlaid KM curves per subgroup level
   → `plot_XX_subgroup_km.png`

### Quality: Apply structure variation
- Forest plot: alternate horizontal vs vertical orientation
- KM facets: vary facet wrap vs facet grid layout
- Interaction test: vary inline vs standalone reporting
- Non-significant interaction: rotate between "consistent across subgroups" /
  "did not differ meaningfully by [subgroup]" / "was similar regardless of [subgroup]"

## Validation Checkpoint

- [ ] Stratified KM run for each subgroup level with n >= 5
- [ ] HR + CI reported per subgroup level
- [ ] Interaction test LR chi-sq, df, p reported
- [ ] Conclusion stated (differs vs consistent)
- [ ] Forest plot generated with HR=1 reference line
- [ ] Stratified KM plot generated
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
interaction_p: float
subgroup_hrs: [{subgroup_level, hr, ci_lower, ci_upper, n}]
plots: [list of new plot filenames]
```
