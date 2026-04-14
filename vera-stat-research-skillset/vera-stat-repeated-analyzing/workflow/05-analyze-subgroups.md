# 05 — Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no subgroup variable specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: Three-Way Interaction (time x group x subgroup)

1. Fit mixed ANOVA: outcome ~ time * group * subgroup + Error(subject/time)
2. Report three-way interaction: F, df, p, partial eta-squared
3. Interpret: significant → "the time x group pattern differs by [subgroup]"
4. If three-way not significant: "the time x group interaction was consistent across [subgroup] levels"

### 5B: Stratified Analyses Per Subgroup Level

For each level of the subgroup variable:
1. Subset data to that subgroup level
2. Run the mixed ANOVA (time x group) within the subset
3. Report time x group interaction: F, df, p, partial eta-squared
4. Skip subgroup levels with n < 5 subjects

### 5C: Forest Plot of Time x Group Interaction Per Subgroup

1. Extract interaction effect sizes per subgroup
2. Forest plot: subgroup interaction effects + CIs + overall diamond
   - Diamond for overall, circles for subgroups, size proportional to n
   - Dashed line at zero
   → `plot_03_subgroup_forest.png`

### 5D: Test for Heterogeneity

1. Formally test whether the time x group interaction differs across subgroups
2. Report heterogeneity statistic and p-value
3. Interpretation: homogeneous vs heterogeneous effects

### Quality: Apply structure variation
- Forest plot: alternate horizontal vs vertical orientation
- Vary legend position (inside vs right margin)
- Three-way interaction: vary inline vs standalone reporting
- Non-significant three-way: rotate between "consistent across subgroups" /
  "did not differ meaningfully by [subgroup]" / "was similar regardless of [subgroup]"

## Validation Checkpoint

- [ ] Three-way interaction tested and reported (if applicable)
- [ ] Stratified time x group analyses run for each subgroup level with n >= 5
- [ ] Interaction effect size + CI reported per subgroup
- [ ] Forest plot generated
- [ ] Heterogeneity test reported
- [ ] Conclusion stated (heterogeneous vs consistent)
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
plots: [plot_03_subgroup_forest.png]
```
