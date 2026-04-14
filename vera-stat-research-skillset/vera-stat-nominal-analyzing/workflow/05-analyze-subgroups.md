# 05 — Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no subgroup variable specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: Stratified Association Tests
For each level of the subgroup variable:
1. Subset data to that level
2. Run the primary association test within the subset
   - Categorical predictor: Chi-square + Cramer's V (or Fisher's if sparse)
   - Continuous predictor: ANOVA + eta-squared (or Kruskal-Wallis)
3. Compute effect size per subgroup
4. Skip subgroup levels with n < 5
5. Compare class distributions across subgroup levels

### 5B: Interaction Test
1. Fit multinomial logistic: outcome ~ predictor * subgroup
2. Fit reduced: outcome ~ predictor + subgroup
3. Likelihood ratio test comparing models
4. Interpret: significant → "association differs across subgroups"; non-significant → "association is consistent"

### 5C: Visualizations
1. **Grouped bar chart**: class proportions per subgroup level
   - Faceted or side-by-side, colored by outcome class
   → `plot_XX_subgroup_proportions.png`

2. **Effect size comparison plot**: Cramer's V or eta-squared per subgroup
   - Points with CIs if available, dashed line at overall effect
   → `plot_XX_subgroup_effects.png`

### Quality: Apply structure variation
- Bar chart: alternate faceted vs side-by-side layout
- Effect plot: vary legend position (inside vs right margin)
- Interaction test: vary inline vs standalone reporting
- Non-significant interaction: rotate between "consistent across subgroups" /
  "did not differ meaningfully" / "was similar regardless of [subgroup]"

## Validation Checkpoint

- [ ] Stratified test run for each subgroup level with n >= 5
- [ ] Effect size reported per subgroup
- [ ] Interaction test (LR chi-square, df, p) reported
- [ ] Conclusion stated (differs vs consistent)
- [ ] Grouped bar chart generated
- [ ] Effect comparison plot generated
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
plots: [list of new plot filenames]
```
