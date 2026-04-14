# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Generate code for PART 5: Modeling

### 6A: Multiple Linear Regression (OLS)
1. Fit: outcome ~ all predictors + covariates
2. Report: R², adjusted R², F-test, AIC, BIC
3. Tidy coefficients: B, SE, 95% CI, p per predictor
4. Standardized β (z-score all continuous vars, refit)
5. Residual diagnostics: residuals vs fitted, Q-Q of residuals, scale-location
6. Coefficient forest plot

### 6B: Quantile Regression
1. Fit at τ = 0.25, 0.50, 0.75
2. Bootstrap SEs
3. Comparison table: OLS vs Q25 vs Q50 vs Q75
4. Interpret: do effects vary across the distribution?

### 6C: Tree-Based Models (Exploratory)
1. CART (maxdepth=4)
2. Random Forest (500 trees, importance=TRUE)
3. LightGBM (500 iterations, max_depth=3, learning_rate=0.01, num_leaves=31)
4. In-sample R² for each (no train/test if N < 200)
5. Variable importance from RF
6. Variable importance plot

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
- OLS: lead with R², or F-test, or strongest predictor, or research question
- QR: distributional insight, or robustness check, or specific predictor variation
- Trees: variable importance, or OLS comparison, or sample size caveat

## Validation Checkpoint

- [ ] OLS model fit reported (R², adj R², F, p)
- [ ] All predictor coefficients with B, SE, CI, p
- [ ] Standardized β reported
- [ ] Residual diagnostic plots generated
- [ ] Coefficient forest plot generated
- [ ] Quantile regression at 3 quantiles with bootstrap SE
- [ ] Comparison table (OLS vs quantiles) generated
- [ ] All 3 tree models fit with in-sample R²
- [ ] Variable importance table and plot generated
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_ols: [prose]
methods_para_qr: [prose]
methods_para_trees: [prose]
results_para_ols: [prose]
results_para_qr: [prose]
results_para_trees: [prose]
tables: [regression_table, quantile_table, importance_table]
plots: [residual, coef_forest, importance]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
