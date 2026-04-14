# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Generate code for PART 5: Modeling

### 6A: Multinomial Logistic Regression (Primary Model)
1. Fit baseline-category logit: outcome ~ all predictors + covariates
   - State reference category explicitly (most frequent class, or user-specified)
2. Report for EACH non-reference class vs reference:
   - Log-odds coefficients (B) with SE
   - Relative Risk Ratios (RRR = exp(B)) with 95% CI
   - p-value per coefficient
3. Likelihood ratio test for each predictor (drop-one LR test)
4. Overall model: log-likelihood, AIC, BIC, McFadden's pseudo-R-squared
5. Coefficient plot: RRR with 95% CI, faceted by outcome class
6. Interpretation: "Compared to [reference], a one-unit increase in [predictor]
   is associated with [RRR] times the relative risk of being in [class] vs [reference]"

### 6B: Linear Discriminant Analysis (LDA)
1. Fit LDA: outcome ~ all continuous predictors
2. Report: Wilks' lambda, approximate F, df, p
3. Report canonical discriminant functions (up to k-1 functions)
4. Discriminant function loadings (structure matrix) — used for variable importance
5. Classification accuracy (in-sample)
6. Scatter plot of first two discriminant scores, colored by outcome class
   → `plot_XX_lda_scores.png`

### 6C: CART (Classification Tree)
1. Fit classification tree (maxdepth = 4)
2. Print tree rules
3. Variable importance from tree
4. In-sample accuracy + confusion matrix
5. Tree visualization → `plot_XX_cart_tree.png`

### 6D: Random Forest
1. Fit: 500 trees, classification mode
2. In-sample accuracy + confusion matrix
3. Variable importance (mean decrease in Gini / accuracy)
4. Variable importance plot → `plot_XX_rf_importance.png`

### 6E: LightGBM
1. Fit: multi-class objective (softmax or OVR)
   - n_estimators = 500
   - max_depth = 3
   - learning_rate = 0.1
   - num_leaves = 15
   - min_child_samples = max(3, N // 10)
2. In-sample accuracy + confusion matrix
3. Variable importance (gain-based)
4. Variable importance plot → `plot_XX_lgbm_importance.png`

### 6F: Confusion Matrices (All Models)
For each of the 5 models:
1. In-sample confusion matrix
2. Overall accuracy
3. Per-class precision (PPV) and recall (sensitivity)
4. If N < 200: explicit caveat "In-sample metrics; no train/test split due to sample size"
5. Summary table: model x accuracy x per-class precision/recall

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
- Multinomial: lead with overall fit, or strongest predictor, or reference category framing
- LDA: lead with Wilks' lambda, or classification accuracy, or discriminant loadings
- Trees: variable importance, or classification accuracy, or comparison to multinomial
- RF/LightGBM: top variable, or agreement with parametric results, or sample size caveat

## Validation Checkpoint

- [ ] Multinomial logistic fit with RRR, 95% CI, p for all predictors x all classes
- [ ] Reference category explicitly stated
- [ ] LR test for each predictor reported
- [ ] LDA fit with Wilks' lambda, loadings, and discriminant scores plot
- [ ] CART with tree visualization and variable importance
- [ ] Random Forest with 500 trees, confusion matrix, importance plot
- [ ] LightGBM with correct hyperparameters, confusion matrix, importance plot
- [ ] Confusion matrix for each model with accuracy + per-class precision/recall
- [ ] In-sample caveat if N < 200
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_multinomial: [prose]
methods_para_lda: [prose]
methods_para_trees: [prose]
results_para_multinomial: [prose]
results_para_lda: [prose]
results_para_trees: [prose]
tables: [multinomial_coef_table, lda_loadings_table, confusion_matrices, importance_table]
plots: [coef_plot, lda_scores, cart_tree, rf_importance, lgbm_importance]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
