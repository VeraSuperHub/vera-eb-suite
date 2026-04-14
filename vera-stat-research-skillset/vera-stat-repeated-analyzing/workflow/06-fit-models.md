# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Generate code for PART 5: Modeling (Dual-Path)

### Design Principle

Models are analytic lenses, not contestants. Each model provides a different
kind of insight into the longitudinal data. LMM gives subject-specific effects,
GEE gives population-averaged effects, trees detect nonlinear patterns.

---

## Path A: Mixed Models and GEE

### 6A-1: Linear Mixed Model — Random Intercept Only

1. Fit: outcome ~ time * group + covariates + (1 | subject)
2. Report fixed effects: B, SE, 95% CI, df (Satterthwaite), t, p
3. Report random effects: random intercept variance, residual variance
4. Compute ICC from this model
5. Report: AIC, BIC, log-likelihood
6. Interpretation: group differences in overall level, time trends

### 6A-2: Linear Mixed Model — Random Intercept + Random Slope

1. Fit: outcome ~ time * group + covariates + (1 + time | subject)
2. Report fixed effects: B, SE, 95% CI, df (Satterthwaite), t, p
3. Report random effects: random intercept variance, random slope variance, correlation between random intercept and slope
4. Likelihood ratio test: random slope model vs random intercept model
   - "Does allowing individual trajectories to differ improve fit?"
   - Report chi-squared, df, p
5. Report: AIC, BIC, log-likelihood
6. Interpretation: individual differences in rate of change

### 6A-3: Growth Curve Model

1. Fit: outcome ~ poly(time, 2) * group + (1 + time | subject) — quadratic growth
   - Or piecewise linear if theory supports it
2. Report: linear time effect, quadratic time effect, group interactions with both
3. Report random effects as in 6A-2
4. Predicted trajectory plot per group: model-predicted curves overlaid on observed means
   → `plot_04_growth_curves.png`
5. Interpretation: trajectory shape (linear, accelerating, decelerating), group differences in shape

### 6A-4: GEE (Generalized Estimating Equations)

1. Fit: outcome ~ time * group + covariates, id = subject
2. Try correlation structures: exchangeable, AR(1), unstructured
3. Select based on QIC (quasi-AIC) or theoretical justification
4. Report: population-averaged coefficients, robust SE, 95% CI, z, p
5. Report: working correlation structure chosen, estimated correlations
6. Compare with LMM results:
   - GEE gives population-averaged effects, LMM gives subject-specific effects
   - Note when they diverge and why (typically similar for linear models with identity link)
   - GEE more robust to correlation misspecification
   - LMM handles missing data (MAR) better than GEE (which assumes MCAR unless using weighted GEE)

### 6A-5: Residual Diagnostics for Best LMM

1. Residuals vs fitted → check linearity
2. Q-Q plot of residuals → check normality of residuals
3. Random effects Q-Q plot → are random intercepts/slopes normal?
4. Residuals vs time → check for heteroscedasticity over time
5. Save diagnostics panel → `plot_05_lmm_diagnostics.png`

### 6A-6: Coefficient Plot

1. Fixed effects from best LMM with 95% CIs
2. Include time, group, interaction, and covariate effects
3. Save → `plot_06_coef_forest.png`

---

## Path B: Tree-Based (Exploratory)

### Important Note
Standard tree models do not handle correlated observations natively. Two approaches:

### 6B-1: Feature Engineering — Subject-Level Summary Features

Create one row per subject with:
- Mean outcome across all time points
- Slope (linear trend from individual OLS fit)
- Variability (SD of individual's outcomes across time)
- First and last observation
- Max change between adjacent time points
- Group membership and any time-invariant covariates

### 6B-2: Random Forest on Subject-Level Features

1. Fit: outcome_slope ~ group + covariates (or outcome_mean ~ ...)
2. 500 trees, importance = TRUE
3. Report: variable importance (permutation-based)
4. Importance plot → `plot_07_rf_importance.png`

### 6B-3: LightGBM on Subject-Level Features

1. Settings: n_estimators=500, max_depth=3, learning_rate=0.1, num_leaves=15, min_child_samples=max(3, N_subjects//10)
2. Feature importance (gain-based)
3. Compare with RF importance ranking

### 6B-4: Compare Tree Importance with LMM Fixed Effects

1. Do the most important features from trees align with significant LMM fixed effects?
2. Note: tree importance operates on subject-level features, LMM on observation-level
3. Concordance and discrepancies inform different aspects of the data

---

### Quality: Code style variation
Apply per `reference/specs/code-style-variation.md`:
- Pick variable naming pattern (A-E) — adapted for LMM/GEE model objects
- Pick comment style (A-E)
- Pick ggplot theme (A-D)
- Pick color palette (A-E)
- Randomize import order (Python)
- Record style vector for consistency (never in output)

### Quality: Interpretation variation
For each model type, rotate lead-in pattern:
- LMM random intercept: lead with ICC, or fixed effects, or model fit, or random variance
- LMM random slope: lead with LR test, or individual differences, or slope variance
- Growth curve: lead with trajectory shape, or group differences in curvature, or predicted plot
- GEE: lead with population-averaged interpretation, or comparison to LMM, or robustness
- Trees: lead with variable importance, or LMM comparison, or sample size caveat

## Validation Checkpoint

- [ ] LMM random intercept: fixed effects with B, SE, CI, df, t, p
- [ ] LMM random intercept: variance components reported
- [ ] LMM random slope: fixed effects + variance components + correlation
- [ ] LR test comparing random slope vs random intercept reported
- [ ] Growth curve: polynomial time effects + group interactions reported
- [ ] Growth curve predicted trajectory plot generated
- [ ] GEE: coefficients with robust SE, working correlation reported
- [ ] GEE vs LMM comparison noted
- [ ] LMM residual diagnostics generated (4 panels)
- [ ] Coefficient plot generated
- [ ] Subject-level features engineered for tree models
- [ ] RF importance table and plot generated
- [ ] LightGBM importance computed
- [ ] Tree vs LMM comparison discussed
- [ ] Code style variation applied consistently
- [ ] AIC/BIC reported for LMM models
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_lmm: [prose]
methods_para_gee: [prose]
methods_para_growth: [prose]
methods_para_trees: [prose]
results_para_lmm_ri: [prose]
results_para_lmm_rs: [prose]
results_para_growth: [prose]
results_para_gee: [prose]
results_para_trees: [prose]
tables: [lmm_ri_fixed, lmm_rs_fixed, lmm_random, growth_fixed, gee_fixed, importance_table]
plots: [plot_04_growth_curves, plot_05_lmm_diagnostics, plot_06_coef_forest, plot_07_rf_importance]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
