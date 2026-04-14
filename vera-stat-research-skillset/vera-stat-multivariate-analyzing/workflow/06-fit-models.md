# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Design Principle

Models are analytic lenses, not contestants. No hyperparameter tuning.
ML models are analytic tools for pattern detection, not prediction engines.

## Generate code for PART 5: Modeling

### 6A: Canonical Correlation Analysis (CCA)
When predictors exist (two sets of variables: DVs and predictors/covariates):
1. Fit CCA
   - R: `CCA::cc()` or `cancor()`
   - Python: `sklearn.cross_decomposition.CCA` or manual via eigendecomposition
2. Report canonical correlations (Rc1, Rc2, ...) for each dimension
3. Wilks' lambda significance test for each canonical dimension
   - Lambda, F approximation, df1, df2, p per dimension
4. **Canonical loadings** (structure coefficients): correlations between original variables and canonical variates
5. **Canonical weights** (standardized coefficients): contribution of each variable to canonical variate
6. **Redundancy analysis**: proportion of variance in each set accounted for by the other set's canonical variate
7. Canonical variate scatter plot → `plot_07_cca.png`
   - First pair of canonical variates, colored by group
   - 10x8, 300 DPI

### 6B: Profile Analysis (full version)
If DVs are on the same scale and not already done in step 05:
1. Parallelism test (Group x DV interaction)
2. Equal levels test (Group main effect)
3. Flatness test (DV main effect)
4. Report all three F tests with df and p
5. Profile plot → `plot_08_profile_full.png`

If already done in step 05, skip and reference prior results.

### 6C: PCA — Dimension Reduction
1. Fit PCA on all outcome variables (centered and scaled)
   - R: `prcomp(scale. = TRUE)` or `psych::principal()`
   - Python: `sklearn.decomposition.PCA`
2. **Scree plot** with Kaiser criterion line (eigenvalue = 1) → `plot_09_scree.png`
3. Report per component:
   - Eigenvalue, proportion of variance, cumulative proportion
4. **Component loadings** (correlation between original DV and component)
   - Bold/flag loadings >= |.40|
5. **Biplot** of first two components colored by group → `plot_10_biplot.png`
6. Interpret: which DVs cluster, how dimensions relate to group separation

### 6D: Discriminant Analysis (Full)
Extends brief LDA from step 04 with:
1. Full discriminant function coefficients (raw and standardized)
2. Group centroids in discriminant space
3. Prior and posterior classification probabilities
4. Cross-validated classification accuracy (leave-one-out)
5. Territorial map → `plot_11_territorial.png` (if 2+ discriminant functions)

### 6E: Multivariate Multiple Regression
If predictors exist:
1. Fit multivariate regression: cbind(Y1, Y2, ...) ~ X1 + X2 + ...
   - R: `lm(cbind(Y1, Y2, ...) ~ X1 + X2, data = df)` then `car::Manova()`
   - Python: separate OLS per DV + Pillai's Trace for overall test
2. Overall multivariate test: Pillai's Trace for each predictor
3. Individual R-squared per DV
4. Coefficient table per DV: B, SE, t, p
5. Coefficient comparison plot across DVs → `plot_12_mv_regression.png`

### 6F: Tree-Based Importance Comparison
1. Fit Random Forest per DV separately (500 trees, default hyperparameters)
2. Fit LightGBM per DV separately (500 iterations, max_depth=3, learning_rate=0.1, num_leaves=15, min_child_samples=max(3, N//10))
3. Extract variable importance from RF and LightGBM per DV
4. **Cross-DV importance comparison**: which predictors matter for which DVs?
5. Heatmap of importance across DVs → `plot_13_importance_heatmap.png`
   - Rows = predictors, columns = DVs, cell color = normalized importance (0-100)
6. In-sample R-squared per model per DV (no train/test if N < 200)
7. Frame as exploratory: "pattern detection" not "prediction"

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
- CCA: lead with strongest canonical correlation, or dimensionality, or redundancy
- PCA: lead with variance accounted for, or number of components, or loading pattern
- Discriminant: lead with classification accuracy, or group separation, or function loadings
- Trees: importance comparison across DVs, or convergence with parametric, or sample size caveat

## Validation Checkpoint

- [ ] CCA: canonical correlations with significance tests (if predictors exist)
- [ ] CCA: loadings, weights, redundancy analysis reported
- [ ] Profile analysis: three tests reported (if same scale, not done in 05)
- [ ] PCA: scree plot, eigenvalues, loadings, biplot generated
- [ ] PCA: only loadings >= |.40| highlighted
- [ ] Discriminant: full coefficients, cross-validated accuracy
- [ ] Multivariate regression: Pillai's Trace per predictor (if predictors exist)
- [ ] RF and LightGBM per DV with importance extraction
- [ ] Cross-DV importance heatmap generated
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_cca: [prose]
methods_para_profile: [prose]
methods_para_pca: [prose]
methods_para_discriminant: [prose]
methods_para_mvreg: [prose]
methods_para_trees: [prose]
results_para_cca: [prose]
results_para_pca: [prose]
results_para_discriminant: [prose]
results_para_mvreg: [prose]
results_para_trees: [prose]
tables: [cca_table, pca_table, discriminant_table, mvreg_table, importance_table]
plots: [plot_07 through plot_13]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
