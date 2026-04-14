# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Design Principle

Every model is an analytic lens, not a contestant. Path A (ignore ordering) and
Path B (respect ordering) provide complementary views of the same outcome. The
dual-path comparison itself is the key insight.

## Generate code for PART 5: Modeling

---

### Path A: Ignore Ordering (Multi-Class)

Treat the ordinal outcome as a nominal (unordered) factor. This reveals which
predictors separate classes regardless of ordering.

#### 6A-1: Multinomial Logistic Regression
1. Fit: outcome (unordered factor) ~ all predictors + covariates (`nnet::multinom` in R, `sklearn.linear_model.LogisticRegression(multi_class='multinomial')` or `statsmodels.MNLogit` in Python)
2. Reference category = lowest ordinal level
3. Report: class-specific OR per predictor (exponentiated coefficients), 95% CI, p per class contrast
4. Report: model-level log-likelihood, AIC, BIC
5. Interpretation: "Relative to [reference level], a one-unit increase in [predictor] was associated with [OR]-fold odds of being in [level k]"

#### 6A-2: CART (Classification Tree)
1. Fit classification tree: outcome (unordered factor) ~ all predictors (maxdepth=4)
2. Report: tree structure, in-sample accuracy, per-class accuracy
3. Note: ordering is not enforced — splits may not respect ordinal structure

#### 6A-3: Random Forest (Classification)
1. Fit: 500 trees, classification mode, outcome as unordered factor
2. Report: in-sample accuracy, per-class accuracy, OOB error
3. Extract variable importance (permutation importance)

#### 6A-4: LightGBM (Multi-Class)
1. Fit: objective='multiclass', n_estimators=500, max_depth=3, learning_rate=0.01, num_leaves=31
2. Outcome as unordered integer codes
3. Report: in-sample accuracy, per-class accuracy
4. Extract variable importance (gain-based)

#### 6A-5: Path A Variable Importance Summary
1. Compile variable importance from RF and LightGBM (Path A)
2. Normalize each to 0-100 scale
3. Also include multinomial |standardized coefficients| averaged across class contrasts, normalized to 0-100
4. Table: `path_a_importance_table`
5. Plot: `plot_06a_importance.png`

---

### Path B: Respect Ordering (Ordinal-Specific Models)

Exploit the ordered structure of the outcome. This reveals monotonic
relationships and level-transition dynamics.

#### 6B-1: Proportional Odds Model (Cumulative Logit)
1. Fit: ordinal outcome ~ all predictors + covariates (`MASS::polr` in R, `statsmodels.miscmodels.ordinal_model.OrderedModel` in Python)
2. Report: log-likelihood, AIC, BIC
3. Tidy coefficients: log-odds B, SE, cumulative OR, 95% CI for cumulative OR, p per predictor
4. Interpretation: "For each one-unit increase in [predictor], the cumulative odds of being in a higher category of [outcome] are multiplied by [OR]"

#### 6B-2: Brant Test for Proportional Odds Assumption
1. Run Brant test (`brant::brant` in R; manual Wald test or equivalent in Python)
2. Report: overall chi-squared(df), p; per-predictor chi-squared(df), p
3. Decision logic:
```
if Brant overall p >= 0.05:
    → "The proportional odds assumption was met."
    → Use polr results as primary ordinal model
else:
    → "The proportional odds assumption was violated."
    → Identify which predictors violate (per-predictor Brant p < .05)
    → Proceed to adjacent-category, continuation-ratio, and stereotype models
    → Flag the violating predictors in all subsequent reporting
```

#### 6B-3: Adjacent-Category Logit Model
1. Fit: compares each ordinal level to the next adjacent level (`VGAM::vglm` with `acat` family in R; custom or `mord` in Python)
2. Report: adjacent-category OR per predictor with 95% CI, p
3. Interpretation: "The odds of being in level [k+1] versus level [k] are multiplied by [OR] for each one-unit increase in [predictor]"
4. Unique insight: reveals which specific level transitions a predictor influences most

#### 6B-4: Continuation-Ratio Logit Model
1. Fit: probability of being in level k given that you reached level k (`VGAM::vglm` with `cratio` family in R; custom implementation in Python)
2. Report: continuation-ratio OR per predictor with 95% CI, p
3. Interpretation: "Among those who reached level [k], the odds of advancing to level [k] versus remaining at a lower level are multiplied by [OR]"
4. Unique insight: useful when ordinal levels represent progressive stages (e.g., disease severity, education attainment)

#### 6B-5: Stereotype Model
1. Fit: relaxes proportional odds but preserves ordinal structure via scaling parameter (`VGAM::vglm` with `multinomial` family and constraints, or `ordinal::clm` with scale in R; custom in Python)
2. Report: scaling parameters (phi) per level, coefficients with 95% CI, p
3. Interpretation: "The stereotype model estimates scaling parameters that quantify how much each predictor's effect varies across ordinal levels while maintaining ordinal structure"
4. Unique insight: good middle ground when proportional odds fails — reveals where the proportional odds assumption breaks down

#### 6B-6: CART (Ordinal-Aware)
1. Fit: same classification tree (maxdepth=4), outcome as ordered factor
2. Report: tree structure, in-sample accuracy
3. Key comparison: do the split points respect the ordinal ordering? Note any splits where ordinal structure is preserved vs. violated

#### 6B-7: Random Forest (Path B)
1. Fit: same 500-tree RF, classification mode
2. Note: trees do not inherently distinguish ordering — the comparison of RF importance between Path A and Path B is the insight
3. Extract variable importance (permutation importance)

#### 6B-8: LightGBM (Ordinal-Aware)
1. If LightGBM ordinal regression mode available: use it
2. Otherwise: objective='regression', treat ordinal levels as numeric (1, 2, 3, ...)
3. n_estimators=500, max_depth=3, learning_rate=0.01, num_leaves=31
4. Extract variable importance (gain-based)
5. Note difference in objective from Path A (regression vs. multi-class)

#### 6B-9: Predicted Probability Plot
1. From the proportional odds model: plot predicted P(Y <= j) across values of the primary predictor for each cumulative threshold
2. Overlay all threshold curves on one plot
3. Save as `plot_06b_predicted_probs.png`

#### 6B-10: Path B Variable Importance Summary
1. Compile variable importance from RF and LightGBM (Path B)
2. Normalize each to 0-100 scale
3. Also include proportional odds |standardized coefficients|, normalized to 0-100
4. Table: `path_b_importance_table`
5. Plot: `plot_06b_importance.png`
6. If N < 200: frame all tree/LightGBM results as "exploratory pattern detection"

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
- Multinomial logistic: lead with class-specific OR, or reference category rationale, or strongest predictor, or model fit
- Proportional odds: lead with cumulative OR, or Brant test result, or strongest predictor, or research question
- Adjacent-category / continuation-ratio: lead with transition-specific insight, or comparison to proportional odds, or stage-specific finding
- Stereotype model: lead with where proportional odds failed, or scaling parameter interpretation, or comparison to other ordinal models
- Trees/LightGBM: variable importance, or path comparison insight, or sample size caveat

## Validation Checkpoint

- [ ] **Path A** multinomial logistic fit with class-specific ORs, CIs, p per class contrast
- [ ] **Path A** CART, RF, LightGBM fit with in-sample accuracy
- [ ] **Path A** variable importance table and plot (RF + LightGBM + multinomial |std coef|)
- [ ] **Path B** proportional odds model fit (log-likelihood, AIC, BIC)
- [ ] **Path B** all predictor coefficients with log-odds B, SE, cumulative OR, CI, p
- [ ] **Path B** Brant test overall and per-predictor reported
- [ ] **Path B** adjacent-category logit fit with adjacent-category ORs, CIs, p
- [ ] **Path B** continuation-ratio logit fit with continuation-ratio ORs, CIs, p
- [ ] **Path B** stereotype model fit with scaling parameters
- [ ] **Path B** CART with ordinal alignment notes
- [ ] **Path B** RF and LightGBM fit with importance
- [ ] **Path B** predicted probability plot generated
- [ ] **Path B** variable importance table and plot (RF + LightGBM + prop. odds |std coef|)
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_multinomial: [prose]
methods_para_polr: [prose]
methods_para_brant: [prose]
methods_para_adjacent_category: [prose]
methods_para_continuation_ratio: [prose]
methods_para_stereotype: [prose]
methods_para_trees_lightgbm: [prose]
results_para_multinomial: [prose]
results_para_polr: [prose]
results_para_brant: [prose]
results_para_adjacent_category: [prose]
results_para_continuation_ratio: [prose]
results_para_stereotype: [prose]
results_para_trees_lightgbm: [prose]
tables: [multinomial_table, polr_table, brant_table, adjacent_cat_table, cont_ratio_table, stereotype_table, path_a_importance_table, path_b_importance_table]
plots: [path_a_importance, path_b_importance, predicted_probs]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
