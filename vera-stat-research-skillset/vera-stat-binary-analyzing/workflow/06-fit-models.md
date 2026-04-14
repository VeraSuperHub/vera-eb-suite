# 06 --- Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Generate code for PART 5: Modeling

### 6A: Logistic Regression
1. Fit: outcome ~ all predictors + covariates (glm, family = binomial)
2. Report: OR with 95% CI for each predictor (exponentiated coefficients)
3. Supplementary table: raw B, SE, z-value, p per predictor
4. Hosmer-Lemeshow goodness-of-fit test (10 groups)
   - Report: chi-sq(df) = X.XX, p = .XXX
   - Non-significant p -> "adequate model fit"
5. Pseudo-R2: McFadden and Nagelkerke
   - Report both; say "the model accounted for" not "explained"
6. ROC curve + AUC
   - Plot ROC curve with AUC value annotated
   - Report: AUC = X.XX, 95% CI [X.XX, X.XX]
   - Note "in-sample" if no cross-validation
   - Save as `plot_05_roc.png`
7. Classification table at optimal threshold (Youden's index)
   - Report: sensitivity, specificity, accuracy, threshold used
   - Confusion matrix

### 6B: Coefficient Visualization
1. Forest plot of ORs with 95% CI (horizontal, OR = 1 reference line)
   - Save as `plot_06_or_forest.png`

### 6C: Tree-Based Models (Exploratory Classification)
1. CART (maxdepth=4) --- classification tree
2. Random Forest (500 trees, classification mode)
3. LightGBM (500 iterations, max_depth=3, learning_rate=0.01, num_leaves=31, objective='binary')
4. In-sample AUC for each (no train/test if N < 200)
5. Variable importance from RF (mean decrease in Gini or accuracy)
6. Variable importance plot -> `plot_07_importance.png`

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
- Logistic: lead with OR of strongest predictor, or Hosmer-Lemeshow result, or AUC, or research question
- ROC: discrimination framing, or clinical threshold framing, or comparison to chance
- Trees: variable importance, or logistic comparison, or sample size caveat

## Validation Checkpoint

- [ ] Logistic model fit with all predictors
- [ ] OR with 95% CI reported for every predictor
- [ ] Raw B, SE, z, p in supplementary table
- [ ] Hosmer-Lemeshow chi-sq, df, p reported
- [ ] McFadden and Nagelkerke pseudo-R2 reported
- [ ] ROC curve plotted with AUC + 95% CI
- [ ] Classification table at optimal threshold with sensitivity/specificity
- [ ] OR forest plot generated
- [ ] All 3 tree models fit with in-sample AUC
- [ ] Variable importance table and plot generated
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out -> 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_logistic: [prose]
methods_para_roc: [prose]
methods_para_trees: [prose]
results_para_logistic: [prose]
results_para_roc: [prose]
results_para_trees: [prose]
tables: [or_table, classification_table, importance_table]
plots: [roc, or_forest, importance]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
