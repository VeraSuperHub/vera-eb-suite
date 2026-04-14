# 05 — Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no subgroup variable specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: Stratified Nonparametric Tests
For each level of the subgroup variable:
1. Subset data to that level
2. Run the primary nonparametric test (Mann-Whitney or Kruskal-Wallis) within the subset
3. Compute effect size (rank-biserial r or Cliff's delta) per subgroup
4. Skip subgroup levels with n < 5

### 5B: Interaction Test via Ordinal Logistic
1. Fit full: ordinal outcome ~ predictor * subgroup (proportional odds)
2. Fit reduced: ordinal outcome ~ predictor + subgroup
3. Likelihood ratio test comparing models
4. Interpret: significant → "the predictor effect on ordinal outcome differs across subgroups"; non-significant → "the predictor effect was consistent across subgroups"

### 5C: Visualizations
1. **Forest plot**: subgroup effects (Cliff's delta or proportional OR) + CIs + overall diamond
   - Diamond for overall, circles for subgroups, size proportional to n
   - Dashed line at null (0 for Cliff's delta, 1 for OR)
   → `plot_04_subgroup_forest.png`

2. **Stacked bar chart per subgroup**
   - Ordinal levels as stacked segments, faceted by subgroup
   - Row percentages within each subgroup × group combination
   → `plot_04_subgroup_stacked.png`

### Quality: Apply structure variation
- Forest plot: alternate horizontal vs vertical orientation
- Stacked bar: vary legend position (inside vs right margin)
- Interaction test: vary inline vs standalone reporting
- Non-significant interaction: rotate between "consistent across subgroups" /
  "did not differ meaningfully" / "was similar regardless of [subgroup]"

## Validation Checkpoint

- [ ] Stratified test run for each subgroup level with n >= 5
- [ ] Effect size reported per subgroup
- [ ] Interaction test LR chi-squared, df, p reported
- [ ] Conclusion stated (differs vs consistent)
- [ ] Forest plot generated
- [ ] Stacked bar per subgroup generated
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
plots: [list of new plot filenames]
```
