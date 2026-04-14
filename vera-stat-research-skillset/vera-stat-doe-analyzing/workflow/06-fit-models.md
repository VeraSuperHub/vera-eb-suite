# 06 -- Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Generate code for PART 5: Modeling

### 6A: Full Factorial Model (Comprehensive)

1. Fit: response ~ all main effects + all interactions (+ block if RCBD)
2. Full ANOVA table: SS, df, MS, F, p, partial eta-squared for every term
3. R-squared and adjusted R-squared for the full model
4. Effect estimates (least-squares means / marginal means) with SE for each factor level
5. Formatted coefficient table

### 6B: Effect Estimation -- Half-Normal / Pareto Chart

For 2^k or fractional factorial designs:
1. Calculate effect estimates for all main effects and interactions
2. Half-normal plot of absolute effects (unreplicated) or Pareto chart (replicated)
3. Identify "active" effects (those that stand out from the noise line)
4. Daniel's method or Lenth's method for unreplicated designs
-> `plot_05_halfnormal.png`

For designs with replication:
1. Pareto chart of |t-values| or F-values for each effect
2. Reference line at critical value
-> `plot_05_pareto_effects.png`

### 6C: Fractional Factorial Analysis (if design is fractional)

1. Determine defining relation (generators)
2. Compute design resolution (III, IV, V)
3. Print alias structure: which effects are confounded
4. Identify clear effects vs. aliased effects
5. Interpretation: what can and cannot be estimated independently

If not fractional, skip this section entirely.

### 6D: Response Surface Methodology (if factors are continuous)

**First-order model:**
1. Fit: response ~ x1 + x2 + ... (linear in all factors)
2. Lack-of-fit test against pure error (if replicates exist)
3. If lack-of-fit significant -> proceed to second-order

**Second-order (quadratic) model:**
1. Fit: response ~ x1 + x2 + x1^2 + x2^2 + x1*x2 + ...
2. Full ANOVA for quadratic model
3. R-squared, adjusted R-squared, lack-of-fit test
4. Contour plot (2 factors at a time, others at center) -> `plot_06_contour.png`
5. Surface plot (3D, 2 factors at a time) -> `plot_07_surface.png`

**Canonical analysis:**
1. Compute stationary point (solve dY/dx = 0)
2. Eigenvalue decomposition of the B matrix (quadratic coefficients)
3. Classify: maximum (all eigenvalues negative), minimum (all positive),
   saddle point (mixed signs), ridge (near-zero eigenvalue)
4. Report stationary point coordinates and predicted response at stationary point

If factors are purely categorical (not continuous), skip RSM entirely.

### 6E: Residual Diagnostics

1. Residuals vs. fitted values plot
2. Residuals vs. each factor (box plots of residuals by factor level)
3. Normal Q-Q plot of residuals
4. Scale-location plot (sqrt|residuals| vs. fitted)
-> `plot_08_residual_diagnostics.png` (2x2 panel)

### 6F: Optimal Factor Settings

1. From ANOVA: which factor-level combination produces best (max or min) response
2. Marginal means table with CIs for each factor
3. If RSM: predicted optimum from canonical analysis
4. If multiple responses (future): desirability function framework mentioned

### 6G: Tree-Based Variable Importance (Exploratory)

1. Random Forest on factors -> variable importance (permutation importance)
   - 500 trees, importance = TRUE
   - Report importance ranking
2. LightGBM on factors -> variable importance (gain-based)
   - 500 iterations, max_depth = 3, learning_rate = 0.1, num_leaves = 15
   - min_child_samples = max(3, N // 10)
   - Report importance ranking
3. Variable importance plot (RF + LightGBM side-by-side) -> `plot_09_importance.png`
4. Frame as exploratory: "Tree-based methods were applied to corroborate the ANOVA findings."
5. If N < 200: explicit caveat about overfitting

### Quality: Code style variation

Apply per `reference/specs/code-style-variation.md`:
- Pick variable naming pattern (A-E)
- Pick comment style (A-E)
- Pick ggplot theme (A-D)
- Pick color palette (A-E)
- Randomize import order (Python)
- Record style vector for consistency (never in output)

### Quality: Interpretation variation

For each model type, rotate lead-in pattern:
- ANOVA: lead with strongest effect, or overall model significance, or practical implication
- Half-normal: lead with number of active effects, or which effect is largest, or noise estimate
- RSM: lead with stationary point type, or R-squared, or contour shape description
- Trees: variable importance ranking, or ANOVA comparison, or sample size caveat

## Validation Checkpoint

- [ ] Full ANOVA table with SS, df, MS, F, p, partial eta-squared for every term
- [ ] Effect estimates with SE reported
- [ ] Half-normal or Pareto chart generated
- [ ] Fractional factorial alias structure printed (if fractional)
- [ ] RSM models fit (if continuous factors): first-order, second-order, canonical analysis
- [ ] Contour and surface plots generated (if RSM)
- [ ] Stationary point classified (max/min/saddle/ridge)
- [ ] Residual diagnostic panel generated (4 plots)
- [ ] Optimal factor settings identified
- [ ] RF and LightGBM importance computed and plotted
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out -> 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_anova: [prose]
methods_para_rsm: [prose]  # if applicable
methods_para_trees: [prose]
results_para_anova: [prose]
results_para_effects: [prose]
results_para_rsm: [prose]  # if applicable
results_para_trees: [prose]
tables: [anova_table, effect_estimates, contrast_table, importance_table]
plots: [plot_05 through plot_09 as applicable]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
