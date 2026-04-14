# 05 --- Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no subgroup variable specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: Stratified Odds Ratios
For each level of the subgroup variable:
1. Subset data to that level
2. Compute 2x2 contingency table (outcome x primary group) within subset
3. Compute odds ratio + 95% CI per subgroup
4. Skip subgroup levels with n < 5

### 5B: Breslow-Day Test for Homogeneity of ORs
1. Test whether odds ratios are homogeneous across subgroup strata
2. Report: Breslow-Day chi-sq(df) = X.XX, p = .XXX
3. Interpret: significant -> "ORs differ across strata (effect modification detected)";
   non-significant -> "ORs are homogeneous across strata (no evidence of effect modification)"
4. Compute Mantel-Haenszel common OR with 95% CI as pooled estimate

### 5C: Visualizations
1. **Forest plot of subgroup ORs**
   - Diamond for overall (Mantel-Haenszel) OR, circles for subgroup ORs
   - Size proportional to stratum N
   - Dashed vertical line at OR = 1 (null)
   - 95% CI whiskers for each point
   -> `plot_04_subgroup_forest.png`

2. **Grouped bar chart of proportions by subgroup**
   - Outcome proportion within each subgroup x group combination
   - Percentage labels on bars
   -> `plot_04_subgroup_proportions.png`

### Quality: Apply structure variation
- Forest plot: alternate horizontal vs vertical orientation
- Bar chart: vary stacked vs grouped, legend position
- Breslow-Day: vary inline vs standalone reporting
- Non-significant homogeneity: rotate between "consistent across subgroups" /
  "did not vary meaningfully" / "was similar regardless of [subgroup]"

## Validation Checkpoint

- [ ] Stratified OR computed for each subgroup level with n >= 5
- [ ] OR + 95% CI reported per subgroup
- [ ] Breslow-Day chi-sq, df, p reported
- [ ] Mantel-Haenszel common OR with 95% CI reported
- [ ] Conclusion stated (homogeneous vs heterogeneous)
- [ ] Forest plot generated with OR = 1 reference line
- [ ] Subgroup proportion chart generated
- [ ] No repeated phrasing patterns from sentence bank

## Data Out -> 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
plots: [list of new plot filenames]
```
