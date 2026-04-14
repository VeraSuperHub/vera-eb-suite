# 05 — Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no subgroup variable specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: Stratified Tests
For each level of the subgroup variable:
1. Subset data to that level
2. Run the primary test within the subset
3. Compute effect size + 95% CI per subgroup
4. Skip subgroup levels with n < 5

### 5B: Interaction Test
1. Fit full: outcome ~ predictor * subgroup + covariates
2. Fit reduced: outcome ~ predictor + subgroup + covariates
3. F-test comparing models
4. Interpret: significant → "effect differs"; non-significant → "consistent"

### 5C: Visualizations
1. **Forest plot**: subgroup effects + CIs + overall diamond
   - Diamond for overall, circles for subgroups, size ∝ n
   - Dashed line at zero
   → `plot_XX_subgroup_forest.png`

2. **Scatter with regression lines per subgroup**
   - Colors per subgroup, regression line + SE band
   → `plot_XX_subgroup_scatter.png`

### Quality: Apply structure variation
- Forest plot: alternate horizontal vs vertical orientation
- Scatter: vary legend position (inside vs right margin)
- Interaction test: vary inline vs standalone reporting
- Non-significant interaction: rotate between "consistent across subgroups" /
  "did not differ meaningfully" / "was similar regardless of [subgroup]"

## Validation Checkpoint

- [ ] Stratified test run for each subgroup level with n ≥ 5
- [ ] Effect size + CI reported per subgroup
- [ ] Interaction test F, df, p reported
- [ ] Conclusion stated (differs vs consistent)
- [ ] Forest plot generated
- [ ] Scatter plot generated
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
plots: [list of new plot filenames]
```
