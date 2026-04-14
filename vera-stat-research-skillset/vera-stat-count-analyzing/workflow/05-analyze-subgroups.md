# 05 — Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no subgroup variable specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: Stratified Rate Ratios
For each level of the subgroup variable:
1. Subset data to that level
2. Fit Poisson or NB regression: outcome ~ predictor (+ offset if rate data)
3. Compute IRR + 95% CI per subgroup
4. If rate data: compute stratum-specific rates per [unit]
5. Skip subgroup levels with n < 5

### 5B: Interaction Test
1. Fit full: outcome ~ predictor * subgroup + covariates (+ offset if rate data)
2. Fit reduced: outcome ~ predictor + subgroup + covariates (+ offset if rate data)
3. Likelihood ratio test comparing models (chi-square, df, p)
4. Interpret: significant → "the rate ratio differs across subgroups"; non-significant → "the rate ratio is consistent across subgroups"

### 5C: Visualizations
1. **Forest plot**: subgroup IRRs + CIs + overall diamond
   - Diamond for overall IRR, circles for subgroup IRRs, size proportional to n
   - Dashed vertical line at IRR = 1 (null)
   → `plot_XX_subgroup_forest.png`

2. **Grouped bar chart**: mean counts (or rates) per predictor level, faceted by subgroup
   → `plot_XX_subgroup_bars.png`

### Quality: Apply structure variation
- Forest plot: alternate horizontal vs vertical orientation
- Bar chart: vary legend position (inside vs right margin)
- Interaction test: vary inline vs standalone reporting
- Non-significant interaction: rotate between "consistent across subgroups" /
  "did not differ meaningfully" / "was similar regardless of [subgroup]"

## Validation Checkpoint

- [ ] Stratified IRR computed for each subgroup level with n >= 5
- [ ] If rate data: stratum-specific rates reported
- [ ] IRR + CI reported per subgroup
- [ ] Interaction test LR chi-square, df, p reported
- [ ] Conclusion stated (differs vs consistent)
- [ ] Forest plot generated with IRR = 1 reference line
- [ ] Grouped bar chart generated
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
plots: [list of new plot filenames]
```
