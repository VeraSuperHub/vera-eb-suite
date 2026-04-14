# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subgroup)

## Generate code for PART 5: Modeling

## Design Principle

Models are analytic lenses, not contestants. Cox PH is the primary inferential
model for survival data. AFT provides an alternative lens when PH fails.
Tree-based models are exploratory tools for detecting nonlinear effects and
confirming variable importance. Never frame as "which model is best."

---

### Path A: Semi-Parametric and Parametric Survival Models

#### 6A-1: Cox Proportional Hazards (primary model)
1. Fit: Surv(time, status) ~ all predictors + covariates
2. Report per predictor: HR, 95% CI, Wald p
3. Global tests: likelihood ratio chi-sq, Wald chi-sq, Score (logrank) chi-sq
4. Concordance index (C-statistic) — note: in-sample
5. **Proportional hazards assumption test** (Schoenfeld residuals):
   - Global test (overall PH assumption)
   - Per-predictor test
   - If PH violated globally (p < ph_test_alpha): flag and note
   - If PH violated for specific predictor: recommend stratifying on it, or note time-varying effect
6. Coefficient forest plot: HRs with 95% CI → `plot_XX_cox_forest.png`

#### 6A-2: Accelerated Failure Time (AFT) Models
Alternative lens, especially when PH assumption is violated.
1. **Weibull AFT**: fit, report time ratio (TR) with 95% CI per predictor
   - TR interpretation: "TR = 1.5 means [group] survived 1.5 times longer"
2. **Log-normal AFT**: fit, report TR with 95% CI per predictor
3. **Log-logistic AFT**: fit, report TR with 95% CI per predictor
4. AIC comparison across AFT distributions:
   - Frame as "which distributional assumption fits the data" NOT "which model wins"
   - Report: Weibull AIC, Log-normal AIC, Log-logistic AIC
   - Note best-fitting distribution for interpretation

#### 6A-3: Cox Model with Time-Varying Covariates
When predictor values change over follow-up (e.g., treatment switches, lab values,
dose changes), a standard Cox model with baseline-only covariates is misspecified.
Use the counting-process (start/stop) formulation instead.

1. **When to use**: At least one covariate changes value during follow-up for some
   subjects. Common examples: medication changes, longitudinal biomarkers, time-
   dependent exposure status.
2. **Data format**: Convert person-level data to start-stop intervals per subject.
   Each row represents an interval `[tstart, tstop)` during which covariate values
   are constant. A subject contributes multiple rows.
3. **Data preparation**:
   - R: `survival::tmerge()` + `tdc()` to create counting-process dataset
   - Python: reshape to long format with `tstart`, `tstop`, `event`, `id` columns
4. **Model fitting**:
   - R: `coxph(Surv(tstart, tstop, event) ~ x_fixed + x_timevarying, data = long_df)`
   - Python: `lifelines.CoxTimeVaryingFitter().fit(long_df, id_col='id', event_col='event', start_col='tstart', stop_col='tstop')`
5. **Report per predictor**: HR, 95% CI, Wald p — same format as standard Cox
   but note "time-varying covariate" in interpretation for relevant predictors
6. **Diagnostics**: Standard Schoenfeld tests apply to time-fixed covariates in
   the model; the time-varying covariate itself addresses non-proportionality
   by construction
7. **Coefficient forest plot**: include time-varying predictors, annotated as "(TV)"
   → `plot_XX_cox_tv_forest.png`

#### 6A-4: Recurring (Recurrent) Event Models
When the same subject can experience the event multiple times (e.g., repeated
hospitalizations, recurrent infections, equipment failures), single-event
survival models are inadequate. Use recurrent event extensions of the Cox model.

1. **When to use**: The outcome event can occur more than once per subject.
   Examples: hospital readmissions, seizure episodes, mechanical breakdowns,
   disease relapses.
2. **Data format**: Start-stop counting-process format, similar to time-varying
   covariates. Each event interval is a row with `[tstart, tstop)`, event
   indicator, and subject ID. Subjects contribute multiple rows — one per gap
   or risk interval.

3. **Model options**:

   **a) Andersen-Gill (AG) model**
   - Treats each event occurrence as independent (conditional on covariates)
   - Extends Cox PH to recurrent events with robust (sandwich) SE for within-
     subject correlation
   - R: `coxph(Surv(tstart, tstop, event) ~ x1 + x2 + cluster(id), data = recur_df)`
   - Python: `lifelines` does not natively support recurrent events — note this
     limitation and recommend R for recurrent event analysis
   - Report: HR with robust SE, 95% CI, Wald p

   **b) Prentice-Williams-Peterson (PWP) model**
   - Stratifies by event number (1st event, 2nd event, etc.)
   - Two variants: PWP-GT (gap time: clock resets after each event) and
     PWP-TT (total time: clock keeps running)
   - R: `coxph(Surv(tstart, tstop, event) ~ x1 + x2 + strata(event_num) + cluster(id), data = recur_df)`
   - Report: HR with robust SE per stratum, 95% CI, Wald p; note which time
     scale (gap time vs total time) was used

   **c) Frailty model**
   - Adds a random effect (frailty) for each subject to capture unobserved
     heterogeneity in event rates
   - R: `coxph(Surv(tstart, tstop, event) ~ x1 + x2 + frailty(id, distribution = "gamma"), data = recur_df)`
   - Report: HR, 95% CI, Wald p for fixed effects; frailty variance (theta)
     with test of heterogeneity

4. **Python limitation**: `lifelines` does not natively handle recurrent events.
   For recurrent event analysis, R is the recommended platform. Document this
   limitation in the methods section and provide R code only.

5. **Reporting conventions**:
   - AG model: HR with robust (sandwich) SE and 95% CI
   - PWP model: stratified HR per event number, robust SE
   - Frailty model: HR for fixed effects, frailty variance (theta), LR test
     for frailty significance
   - Always report total number of events and mean/median events per subject

#### 6A-5: Residual Diagnostics
1. **Cox-Snell residuals**: plot cumulative hazard of residuals vs residuals
   - Should follow 45-degree line if model fits well
   → `plot_XX_coxsnell.png`
2. **Deviance residuals** vs linear predictor:
   - Check for outliers (|deviance residual| > 2)
   → `plot_XX_deviance.png`
3. **Schoenfeld residuals** vs time (per predictor):
   - Visualize PH assumption — slope should be flat
   - Plot for predictors where PH test was borderline or violated
   → `plot_XX_schoenfeld.png`

---

### Path B: Tree-Based (Exploratory)

#### 6B-1: Survival CART
1. Recursive partitioning for survival (rpart with method="exp" in R, or survival tree)
2. Report: tree structure, split variables, terminal node survival curves
3. Max depth = 4

#### 6B-2: Random Survival Forest (RSF)
1. 500 trees
2. R: `randomForestSRC` package
3. Python: `scikit-survival` (sksurv.ensemble.RandomSurvivalForest)
4. Variable importance (permutation-based)
5. Variable importance plot → `plot_XX_rsf_importance.png`
6. Partial dependence plots for top 2 predictors → `plot_XX_pdp_[var].png`

#### 6B-3: Gradient Boosting Survival
1. Primary: `scikit-survival` GradientBoostingSurvivalAnalysis (handles censoring natively)
2. Alternative: LightGBM with objective='cox' (or xgboost with cox objective)
3. Settings: n_estimators=500, max_depth=3, learning_rate=0.1, min_samples_leaf=max(3, N//10)
4. Note: LightGBM does not natively handle censoring well — prefer scikit-survival for inference, use LightGBM for variable importance comparison only
5. Variable importance from gradient boosting
6. Concordance index from each tree-based model (in-sample)

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
- Cox: lead with global test, or strongest predictor, or concordance, or PH status
- AFT: distributional fit, or time ratio insight, or PH violation context
- RSF: variable importance, or Cox comparison, or sample size caveat

## Validation Checkpoint

- [ ] Cox PH model fit with all predictors
- [ ] HR with 95% CI reported per predictor
- [ ] Global tests (LR, Wald, Score) reported
- [ ] Concordance index reported
- [ ] Schoenfeld PH test reported (global + per predictor)
- [ ] PH violation flagged and addressed if detected
- [ ] Cox coefficient forest plot generated
- [ ] Time-varying Cox fit if time-varying covariates present
- [ ] Time-varying data prep code (tmerge/long format) included
- [ ] Time-varying HRs reported with "(TV)" annotation
- [ ] Recurring event model fit if recurrent outcome (AG, PWP, or frailty)
- [ ] Recurring event model type justified in methods prose
- [ ] Total events and events-per-subject summary reported
- [ ] Robust SE used for AG/PWP models
- [ ] Frailty variance reported if frailty model used
- [ ] Python limitation for recurrent events documented
- [ ] All 3 AFT models fit with TR and 95% CI
- [ ] AIC comparison table for AFT distributions
- [ ] Cox-Snell, deviance, and Schoenfeld residual plots generated
- [ ] Survival CART fit
- [ ] RSF fit with variable importance
- [ ] Gradient boosting fit with concordance
- [ ] Variable importance plot from RSF
- [ ] Partial dependence plots for top 2 predictors
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_cox: [prose]
methods_para_cox_tv: [prose, if time-varying covariates present]
methods_para_recurrent: [prose, if recurrent events]
methods_para_aft: [prose]
methods_para_trees: [prose]
results_para_cox: [prose]
results_para_cox_tv: [prose, if time-varying covariates present]
results_para_recurrent: [prose, if recurrent events]
results_para_aft: [prose]
results_para_trees: [prose]
tables: [cox_table, cox_tv_table, recurrent_table, aft_table, importance_table]
plots: [cox_forest, cox_tv_forest, coxsnell, deviance, schoenfeld, rsf_importance, pdp]
ph_status: {global_p, per_predictor: [{name, p, violated}]}
concordance: {cox, rsf, gbm}
recurrent_event_info: {model_type, total_events, mean_events_per_subject, frailty_variance}
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
