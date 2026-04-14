# 06 — Fit Advanced Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no moderators)

## Design Principle

Models are analytic lenses, not contestants. Each estimation method provides a
different perspective on the pooled effect and heterogeneity. No hyperparameter
tuning. No tree-based models (not applicable to meta-analysis).

## Generate code for PART 5: Advanced Modeling

### 6A: Fixed-Effects Model (Inverse-Variance)
1. Assumes a common true effect across all studies
2. R: `metafor::rma(yi, vi, method="FE")`
3. Report: pooled ES, 95% CI, z, p
4. Note: weights driven entirely by study precision; heterogeneity ignored

### 6B: Random-Effects Model (DerSimonian-Laird)
1. Most commonly reported estimator in published meta-analyses
2. R: `metafor::rma(yi, vi, method="DL")`
3. Report: pooled ES, 95% CI, z, p, tau²
4. Note: moment-based estimator, can underestimate tau² with few studies

### 6C: Random-Effects Model (REML)
1. Restricted maximum likelihood — generally preferred estimator
2. R: `metafor::rma(yi, vi, method="REML")`
3. Report: pooled ES, 95% CI, z, p, tau²
4. Note: better statistical properties than DL, especially with small k

### 6D: Knapp-Hartung Adjustment
1. More accurate CIs and test statistics for random-effects, especially with few studies
2. R: `metafor::rma(yi, vi, method="REML", test="knha")`
3. Report: pooled ES, 95% CI (wider than standard), t-statistic (not z), df, p
4. Note: uses t-distribution instead of z; CIs better calibrated when k < 20

### 6E: Bayesian Meta-Analysis
1. Useful when k is small (< 10) or informative priors are justified
2. Place weakly informative prior on tau (half-Cauchy or half-normal)
3. R: `brms::brm()` or `bayesmeta::bayesmeta()`
4. Report: posterior mean, 95% credible interval, posterior median of tau
5. Compare posterior to frequentist estimate
6. Note: if brms/bayesmeta not available, describe approach in methods and report frequentist

### 6F: Three-Level Meta-Analysis
1. When studies report multiple effect sizes (dependent effects)
2. Accounts for within-study correlation and between-study variance
3. R: `metafor::rma.mv(yi, vi, random = ~ 1 | study/effect_id)`
4. Report: pooled ES, 95% CI, sigma²_within, sigma²_between
5. Skip if each study contributes only one effect size
6. Note: mention as available capability; fit only if data structure warrants it

### Network Meta-Analysis
- Mention as future capability in recommendation block
- Do NOT implement in this version

### Quality: Code style variation
Apply per `reference/specs/code-style-variation.md`:
- Pick variable naming pattern (A-E) for model objects
- Pick comment style (A-E)
- Pick plot theme (A-D)
- Pick color palette (A-E)
- Randomize import order
- Record style vector for consistency (never in output)

### Quality: Interpretation variation
For each model, rotate lead-in pattern:
- Fixed-effects: lead with assumption, or estimate, or comparison to random
- DL: lead with prevalence in literature, or estimate, or tau² magnitude
- REML: lead with statistical properties, or estimate, or tau² comparison
- Knapp-Hartung: lead with CI width comparison, or small-k rationale
- Bayesian: lead with prior specification, or posterior, or credible interval width

## Validation Checkpoint

- [ ] Fixed-effects model fit and reported (ES, CI, z, p)
- [ ] DerSimonian-Laird model fit and reported (ES, CI, z, p, tau²)
- [ ] REML model fit and reported (ES, CI, z, p, tau²)
- [ ] Knapp-Hartung adjustment applied and reported (ES, CI, t, df, p)
- [ ] Bayesian model fit or approach described (posterior mean, CrI, tau)
- [ ] Three-level model fit if applicable, or noted as not applicable
- [ ] All models produce identical point direction (sanity check)
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_fe: [prose]
methods_para_dl: [prose]
methods_para_reml: [prose]
methods_para_knha: [prose]
methods_para_bayes: [prose]
methods_para_threelevel: [prose] or null
results_para_models: [prose for each model]
tables: [model_comparison_table]
style_vector: [e.g., "B-A-C-D-E-2-1"]
```
