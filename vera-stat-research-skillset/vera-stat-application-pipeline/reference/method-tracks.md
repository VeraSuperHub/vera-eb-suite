# Method Track Definitions

Defines the parallel and sequential analysis tracks for each outcome type.
Each track maps to specific workflow steps from the routed skill layer.

Important ownership rule:
- `T1_primary` always runs against the routed **testing** skill (`01-03`)
- `T2+` tracks run against the routed **analyzing** skill (`04-08`)
- Post-track convergence and manuscript assembly use the analyzing skill outputs

## Track Architecture

```
Independent Tracks (parallel):
  T1: Distribution & Primary Tests    ← testing workflow steps 01-03
  T2: Regression Modeling              ← analyzing workflow step 06 (regression portion)
  T3: Tree-Based Exploratory           ← analyzing workflow step 06 (tree portion)
  T4: Alternative Methods              ← analyzing workflow step 06 (alternative portion)

Dependent Tracks (sequential):
  T5: Subgroup Analysis                ← analyzing workflow steps 04-05 (needs T1 results)

Post-Track (always sequential, after all tracks):
  Convergence: Model Comparison        ← workflow step 07
  Assembly: Manuscript Fragments       ← workflow step 08
```

---

## Continuous Outcome

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Distribution & Primary Tests | T1_primary | Shapiro-Wilk, Q-Q plot, t-test/ANOVA, effect sizes (d/η²), Mann-Whitney/Kruskal-Wallis | testing 01, 02, 03 | — |
| OLS Regression | T2_regression | OLS + diagnostics (residual plots, VIF), coefficient CIs, standardized β, R² | 06 (regression) | — |
| Tree-Based Exploratory | T3_trees | CART (maxdepth=4), Random Forest (500 trees), LightGBM (500 iter), variable importance | 06 (trees) | — |
| Quantile Regression | T4_qr | QR at τ=0.25,0.50,0.75, bootstrap SEs, OLS vs QR comparison | 06 (QR) | — |
| Subgroup Analysis | T5_subgroup | Stratified tests per subgroup, interaction test (predictor×subgroup), forest plot | 04, 05 | T1 |

## Binary Outcome

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Distribution & Primary Tests | T1_primary | Frequency table, Chi-square/Fisher's exact, odds ratios, risk difference | testing 01, 02, 03 | — |
| Logistic Regression | T2_regression | Binary logistic, ORs + CIs, Hosmer-Lemeshow, ROC/AUC, calibration plot | 06 (regression) | — |
| Tree-Based Exploratory | T3_trees | CART, RF, LightGBM (objective='binary'), importance, partial dependence | 06 (trees) | — |
| Penalized Regression | T4_penalized | LASSO logistic, Ridge logistic (if p > 10 predictors); else skip | 06 (penalized) | — |
| Subgroup Analysis | T5_subgroup | Stratified ORs, interaction terms in logistic model, forest plot | 04, 05 | T1 |

## Ordinal Outcome

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Distribution & Primary Tests | T1_primary | Frequency table, Mann-Whitney U/Kruskal-Wallis, Jonckheere-Terpstra trend | testing 01, 02, 03 | — |
| Proportional Odds (Path B) | T2_po | Proportional odds logistic, Brant test; if violated → adjacent-category/continuation-ratio/stereotype | 06 (Path B) | — |
| Tree-Based Exploratory | T3_trees | CART (ordered), RF, LightGBM (objective='regression' on numeric codes) | 06 (trees) | — |
| Multinomial (Path A) | T4_multinomial | Multinomial logistic (ignoring order), LDA, cross-path importance comparison | 06 (Path A) | — |
| Subgroup Analysis | T5_subgroup | Stratified nonparametric tests, ordinal interaction models | 04, 05 | T1 |

## Nominal (Multi-class) Outcome

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Distribution & Primary Tests | T1_primary | Class frequencies, Chi-square (categorical), ANOVA/KW (continuous predictors) | testing 01, 02, 03 | — |
| Multinomial Logistic | T2_regression | Multinomial logistic, RRR, LDA | 06 (regression) | — |
| Tree-Based Exploratory | T3_trees | CART (multiclass), RF, LightGBM (objective='multiclass'), confusion matrices | 06 (trees) | — |
| — | T4 | Not applicable (skip) | — | — |
| Subgroup Analysis | T5_subgroup | Stratified classification, subgroup-specific distributions | 04, 05 | T1 |

## Count Outcome

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Distribution & Primary Tests | T1_primary | Poisson check, overdispersion test, mean-variance relationship | testing 01, 02, 03 | — |
| GLM Count Models | T2_regression | Poisson, quasi-Poisson, negative binomial, IRRs + CIs, offset handling | 06 (regression) | — |
| Tree-Based Exploratory | T3_trees | CART, RF, LightGBM (objective='regression'), importance | 06 (trees) | — |
| Zero-Inflated / Hurdle | T4_zeroinfl | ZIP, ZINB, hurdle models (if excess zeros detected); else skip | 06 (zero-inflation) | — |
| Subgroup Analysis | T5_subgroup | Stratified rate comparisons, interaction in count models | 04, 05 | T1 |

## Survival Outcome

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| KM & Log-Rank | T1_primary | Kaplan-Meier curves, log-rank test, median survival + CI | testing 01, 02, 03 | — |
| Cox Regression | T2_regression | Cox PH model, HRs + CIs, PH assumption check (Schoenfeld), concordance | 06 (Cox) | — |
| Random Survival Forest | T3_trees | RSF, variable importance, partial dependence | 06 (trees) | — |
| AFT Models | T4_aft | Accelerated failure time (if PH violated): Weibull, log-normal, log-logistic | 06 (AFT) | T2 (needs PH check) |
| Subgroup Analysis | T5_subgroup | Stratified KM, interaction terms in Cox, forest plot of subgroup HRs | 04, 05 | T1, T2 |

**Note**: For survival, T4 depends on T2 (needs PH assumption check result). T5 depends on both T1 and T2.

## Repeated Measures / Longitudinal

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Paired/Repeated Tests | T1_primary | Sphericity (Mauchly), paired t/Wilcoxon, Friedman, basic mixed model | testing 01, 02, 03 | — |
| Linear Mixed Models | T2_regression | Random intercept/slope, REML, ICC, likelihood ratio tests, marginal vs conditional | 06 (LMM) | — |
| Tree-Based Exploratory | T3_trees | RF on flattened features, time-varying importance | 06 (trees) | — |
| GEE | T4_gee | GEE with exchangeable/AR1 correlation, comparison with LMM | 06 (GEE) | — |
| Subgroup Analysis | T5_subgroup | Subgroup×time interaction in mixed models, stratified trajectories | 04, 05 | T1 |

## Time Series

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Diagnostics & Basic Model | T1_primary | ACF/PACF, stationarity (ADF, KPSS), basic ARIMA with forecast | testing 01, 02, 03 | — |
| SARIMA & ETS | T2_sarima | SARIMA, exponential smoothing (ETS), structural breaks | 06 (SARIMA) | — |
| ML Forecasting | T3_trees | RF + LightGBM on lagged features, feature importance | 06 (ML) | — |
| Advanced TS | T4_advanced | GARCH (if volatility), VAR (if multivariate), Granger causality, spectral | 06 (advanced) | T1 (needs stationarity) |
| — | T5 | Subgroup not typical for time series (skip unless panel data) | — | — |

## Multivariate Outcome

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Multivariate Tests | T1_primary | Multivariate normality, MANOVA, Box's M | testing 01, 02, 03 | — |
| Canonical Correlation | T2_cca | CCA, canonical weights, redundancy analysis | 06 (CCA) | — |
| PCA / Dimension Reduction | T3_pca | PCA, scree plot, loading matrix, variance explained | 06 (PCA) | — |
| Discriminant Analysis | T4_da | LDA, QDA, classification accuracy | 06 (DA) | — |
| — | T5 | Per-outcome subgroup analysis if requested | 04, 05 | T1 |

## DOE / Factorial

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Design Validation & Main Effects | T1_primary | Balance check, main effects ANOVA, effect sizes | testing 01, 02, 03 | — |
| Factorial ANOVA | T2_regression | Full factorial ANOVA, interactions, contrast analysis | 06 (ANOVA) | — |
| Response Surface | T3_rsm | RSM (if continuous factors), optimization, contour plots | 06 (RSM) | — |
| Robust / Nonparametric | T4_robust | Aligned rank transform ANOVA (if non-normal), Taguchi methods | 06 (robust) | — |
| — | T5 | Blocking analysis if blocking factor exists | 04, 05 | T1 |

## Meta-Analysis

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Heterogeneity & Basic Pooling | T1_primary | I², Q-test, fixed-effects pooled estimate, forest plot | testing 01, 02, 03 | — |
| Random Effects | T2_regression | Random-effects model (REML), prediction interval, funnel plot | 06 (RE) | — |
| Meta-Regression | T3_metareg | Meta-regression with moderators, bubble plot | 06 (metareg) | — |
| Sensitivity & Bias | T4_sensitivity | Leave-one-out, trim-and-fill, Egger's test, p-curve | 06 (sensitivity) | — |
| Subgroup Meta | T5_subgroup | Subgroup pooled estimates, between-subgroup Q-test | 04, 05 | T1 |

## SEM-CFA

For CFA, tracks are sequential and stay within the measurement-model family.

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Primary CFA | T1_primary | Identification checks, estimator choice, initial CFA fit, standardized loadings | testing 01, 02, 03 | — |
| Reliability & Validity | T2_validity | Reliability, convergent/discriminant validity, modification-index review | 04 | T1_primary |
| Invariance | T3_invariance | Measurement invariance (configural, metric, scalar) | 05 | T1_primary |
| Alternative CFA Models | T4_models | Alternative CFA specifications, residual/cross-loading review under theory constraints | 06 | T2_validity |
| Cross-Model Synthesis | T5_compare | Model comparison, fit synthesis, manuscript-ready interpretation | 07 | T4_models |

## SEM-Full

For full SEM, tracks are sequential and stay within the structural-model family.

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Primary SEM | T1_primary | Model setup, identification, global fit, key direct paths | testing 01, 02, 03 | — |
| Indirect Effects & Residual Review | T2_indirect | Indirect effects, residual diagnostics, local misfit checks | 04 | T1_primary |
| Multi-Group SEM | T3_multigroup | Group comparisons, moderated structure, subgroup SEM | 05 | T1_primary |
| Alternative Structural Models | T4_models | Alternative path structures, mediation/moderation variants | 06 | T2_indirect |
| Cross-Model Synthesis | T5_compare | Nested comparison, fit synthesis, manuscript-ready interpretation | 07 | T4_models |

## SEM-Longitudinal Change

For longitudinal SEM, tracks are sequential and stay within the growth/change family.

| Track | ID | Methods | Workflow Steps | Depends On |
|-------|----|---------|----------------|------------|
| Primary Growth / Change Model | T1_primary | Initial latent growth / change setup, estimator choice, baseline trajectory fit | testing 01, 02, 03 | — |
| Change Diagnostics | T2_change | Nonlinear trajectory checks, latent-basis/change-score diagnostics | 04 | T1_primary |
| Multi-Group Growth / Change | T3_multigroup | Group comparisons for change trajectories | 05 | T1_primary |
| Alternative Growth Models | T4_models | Alternative growth or change specifications, parallel-process variants when justified | 06 | T2_change |
| Cross-Trajectory Synthesis | T5_compare | Model comparison and manuscript-ready growth/change interpretation | 07 | T4_models |

---

## Track Output Contract

Each track produces files in its directory `output/track_outputs/{track_id}/`:

```
{track_id}/
├── methods.md        ← Methods fragment for this track
├── results.md        ← Results fragment with statistics
├── code.R            ← R code for this track
├── code.py           ← Python code for this track
├── figures/          ← Track-specific figures (PNG, 300 DPI)
├── tables/           ← Track-specific tables (Markdown + CSV)
└── references.bib    ← Methodological references for this track
```

## Dependency Notation

- `—` = no dependencies, can run immediately
- `T1` = depends on T1 completing first
- `T1, T2` = depends on both T1 and T2 completing
- SEM-family tracks are sequential within their routed family (CFA, full SEM, or longitudinal change)
