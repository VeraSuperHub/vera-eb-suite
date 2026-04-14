# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Generate code for PART 5: Modeling

### Design Principle

Models are analytic lenses, not contestants. Each distributional assumption
reveals different aspects of the count-generating process. Model selection is
framed as "which distributional assumption fits the data" — never "which model wins."

---

### Path A: Standard Count Models

All models include offset = log(exposure) if rate data.

#### A1: Poisson Regression
1. Fit: outcome ~ all predictors + covariates (+ offset if rate data)
2. Report: IRR with 95% CI for each predictor (exponentiated coefficients)
3. Report: deviance, residual df, AIC
4. Check overdispersion: deviance / residual df ratio
   - If ratio > 1.5 → flag: "Poisson overdispersed; NB results preferred"
5. Tidy coefficient table: B (log scale), SE, z, p, IRR, IRR 95% CI

#### A2: Negative Binomial Regression
1. Fit: outcome ~ all predictors + covariates (+ offset if rate data)
2. Report: IRR with 95% CI for each predictor
3. Report: theta (dispersion parameter), AIC
4. Likelihood ratio test: Poisson vs NB
   - LR chi-sq(1) with p-value
   - If significant → NB provides significantly better fit
5. Tidy coefficient table: B (log scale), SE, z, p, IRR, IRR 95% CI

#### A3: Zero-Inflated Poisson (ZIP)
Skip if zero_proportion ≤ 0.10 (not enough zeros to warrant).
1. Two-part model:
   - Logistic component: P(structural zero) ~ predictors
   - Count component: Poisson(count | non-structural) ~ predictors (+ offset)
2. Report both sets of coefficients
3. Vuong test: ZIP vs standard Poisson
   - If significant → ZIP is preferred over Poisson
4. AIC comparison

#### A4: Zero-Inflated Negative Binomial (ZINB)
Skip if zero_proportion ≤ 0.10 OR overdispersion_ratio < 1.5.
1. Two-part model:
   - Logistic component: P(structural zero) ~ predictors
   - Count component: NB(count | non-structural) ~ predictors (+ offset)
2. Report both sets of coefficients
3. Vuong test: ZINB vs standard NB
4. AIC comparison

#### A5: Hurdle Model
Alternative to zero-inflation — conceptually different framing.
1. Two-part model:
   - Part 1: Logistic regression for zero vs non-zero
   - Part 2: Truncated Poisson or truncated NB for positive counts (+ offset)
2. Report coefficients for both parts
3. AIC comparison with standard and zero-inflated models

#### A6: Model Selection Summary
1. AIC comparison table across all fitted count models
2. Frame as: "Poisson assumes equidispersion, NB relaxes this, ZIP/ZINB handle excess zeros, Hurdle separates the zero-generating process"
3. Identify best-fitting distributional assumption (lowest AIC) for use in variable importance
4. Do NOT frame as horse-race — each model answers a different question about the data

---

### Path B: Tree-Based Models (Exploratory)

Regression mode (predicting count, not classification).

#### B1: CART (maxdepth=4)
1. Fit: outcome ~ all predictors + covariates
2. Report: in-sample R² (or deviance explained)
3. Tree plot → `plot_XX_cart_tree.png`

#### B2: Random Forest (500 trees)
1. Fit: regression mode on count outcome
2. Report: in-sample R² (no train/test split if N < 200)
3. Variable importance (permutation-based)
4. Variable importance plot → `plot_XX_rf_importance.png`

#### B3: LightGBM (500 iterations, regression)
1. Settings: n_estimators=500, max_depth=3, learning_rate=0.1, num_leaves=15, min_child_samples=max(3, N//10)
2. Fit: regression mode on count outcome
3. Report: in-sample R²
4. Variable importance (gain-based)

---

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
- Poisson: lead with deviance, or IRR of strongest predictor, or overdispersion check
- NB: lead with theta, or LR test vs Poisson, or strongest IRR
- ZIP/ZINB: lead with Vuong test, or zero-inflation insight, or count component finding
- Hurdle: lead with conceptual framing, or zero-generating process insight
- Trees: variable importance, or count model agreement, or sample size caveat

## Validation Checkpoint

- [ ] Poisson regression fit with IRR, CI, deviance, AIC
- [ ] Overdispersion check via deviance/df ratio
- [ ] Negative Binomial fit with IRR, CI, theta, AIC
- [ ] LR test Poisson vs NB reported (chi-sq, df, p)
- [ ] ZIP fit if zero_proportion > 0.10 (Vuong test, AIC)
- [ ] ZINB fit if overdispersed AND excess zeros (Vuong test, AIC)
- [ ] Hurdle model fit with both components reported
- [ ] AIC comparison table across all count models
- [ ] Model selection framed as distributional assumption, not horse-race
- [ ] If rate data: offset included in ALL count models
- [ ] CART, RF, LightGBM fit with in-sample R²
- [ ] Variable importance table and plot generated
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_poisson: [prose]
methods_para_nb: [prose]
methods_para_zi: [prose]
methods_para_hurdle: [prose]
methods_para_trees: [prose]
results_para_poisson: [prose]
results_para_nb: [prose]
results_para_zi: [prose]
results_para_hurdle: [prose]
results_para_trees: [prose]
tables: [poisson_table, nb_table, zip_table, zinb_table, hurdle_table, aic_table, importance_table]
plots: [cart_tree, rf_importance, ...]
style_vector: [e.g., "B-A-C-D-E-2-1"]
best_count_model: "poisson" | "negbin" | "zip" | "zinb" | "hurdle"
```
