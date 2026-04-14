# 05 — Analyze Subgroups & Meta-Regression

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no moderator variables specified. Pass through to 06-fit-models.md.

## Generate code for PART 4: Moderator Analysis

### 5A: Subgroup Analysis (categorical moderators)

For each categorical moderator:
1. Pool effect sizes within each subgroup (random-effects)
2. Report per subgroup: k, pooled ES, 95% CI, I²
3. Test for subgroup differences: Q_between with df and p
4. Skip subgroup levels with k < 2 (need at least 2 studies to pool)
5. Subgroup forest plot → `plot_04_subgroup_[moderator].png`
   - Grouped by subgroup, diamond per subgroup, overall diamond
   - R: `metafor::forest()` with `rows` argument for grouping

### 5B: Meta-Regression (continuous moderators)

For each continuous moderator:
1. Fit mixed-effects meta-regression: yi ~ moderator, random-effects for residual heterogeneity
   - R: `metafor::rma(yi, vi, mods=~moderator, method="REML")`
2. Report: regression coefficient B, SE, z-test, p-value
3. R² analog: proportion of heterogeneity accounted for by moderator
   - R: `(model_base$tau2 - model_reg$tau2) / model_base$tau2`
4. Test of residual heterogeneity: QE statistic, df, p
5. **Bubble plot**: effect size (y) vs moderator (x), bubble size proportional to study precision (1/SE)
   - Regression line overlaid with 95% CI band
   - Save as `plot_04_bubble_[moderator].png` (8x6, 300 DPI)

### 5C: Multi-Moderator Regression (if k >= 10 and multiple moderators)

1. Fit model with all moderators simultaneously
2. Report: each coefficient B, SE, p
3. Compare R² to single-moderator models
4. Warn about overfitting if k/moderators < 10

### Quality: Apply structure variation
- Subgroup forest: vary study label positioning (left vs right)
- Bubble plot: vary point shape (circle vs diamond) and legend placement
- Vary whether subgroup results or meta-regression results come first
- Non-significant moderator: rotate between "did not significantly moderate" /
  "was not a significant source of heterogeneity" / "did not account for
  between-study variability"

## Validation Checkpoint

- [ ] Subgroup analysis run for each categorical moderator
- [ ] Per-subgroup: k, pooled ES, CI, I² reported
- [ ] Q_between reported with df and p for each moderator
- [ ] Meta-regression coefficient, SE, z, p reported for each continuous moderator
- [ ] R² analog reported for each meta-regression
- [ ] Subgroup forest plot generated for each categorical moderator
- [ ] Bubble plot generated for each continuous moderator
- [ ] Subgroup levels with k < 2 excluded with note
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_subgroup: [methods paragraph prose]
methods_para_metareg: [methods paragraph prose]
results_para_subgroup: [results paragraph prose]
results_para_metareg: [results paragraph prose]
plots: [list of new plot filenames]
tables: [subgroup_table, metareg_table]
```
