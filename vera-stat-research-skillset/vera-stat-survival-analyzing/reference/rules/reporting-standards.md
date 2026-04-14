# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

## General Rules

1. **p-values**: Never "p = 0.000" -> use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" -> "not statistically significant at alpha = [level]"
3. **Sample size**: Report final analytic N (after exclusions), not original N.
4. **Decimal places**: 2 for HR/TR/coefficients, 3 for p-values, 2 for concordance/effect sizes, 1 for median survival time.

## Survival-Specific Rules

5. **Hazard ratio (HR)**: Always with 95% CI. Format: "HR = X.XX, 95% CI [X.XX, X.XX]". Include direction: HR > 1 = increased hazard; HR < 1 = decreased hazard.
6. **Time ratio (AFT)**: Always with 95% CI. Format: "TR = X.XX, 95% CI [X.XX, X.XX]". Include direction interpretation: "TR = 1.50 indicates [group] survived 1.50 times longer than [reference]."
7. **Median survival**: Always with 95% CI. Format: "median = X.X [units], 95% CI [X.X, X.X]". If not reached: "median survival was not reached (lower bound: X.X [units])."
8. **Survival rates at landmarks**: Always with 95% CI. Format: "1-year survival rate: XX.X% (95% CI [XX.X%, XX.X%])."
9. **Censoring**: Always report % censored overall and by group. Format: "Of N patients, X (XX.X%) experienced the event and Y (YY.Y%) were censored."
10. **Log-rank test**: Format: "chi-sq(df) = X.XX, p = .XXX". For pairwise: note Bonferroni adjustment.
11. **Cox global tests**: Report all three: "Likelihood ratio test: chi-sq(df) = X.XX, p = .XXX; Wald test: chi-sq(df) = X.XX, p = .XXX; Score (logrank) test: chi-sq(df) = X.XX, p = .XXX."
12. **Concordance index**: Format: "C = X.XX". Always note "(in-sample)" if no external validation performed.
13. **PH assumption (Schoenfeld test)**: Report per predictor and globally. Format: "The global test of proportional hazards was [not] significant (chi-sq = X.XX, p = .XXX). [Predictor] showed evidence of non-proportionality (rho = X.XX, chi-sq = X.XX, p = .XXX)."
14. **Degrees of freedom**: Report with chi-sq statistics.
15. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity.
16. **AIC comparison**: Report as distributional fit assessment, not model ranking. "Among AFT distributions, the [distribution] provided the best fit (AIC = X.X) compared to [others]."
17. **Time-varying Cox HR**: Same format as standard HR — "HR = X.XX, 95% CI [X.XX, X.XX]" — but explicitly note "(time-varying covariate)" in interpretation. State that the predictor was modeled using the counting-process (start/stop) formulation to account for changes during follow-up.
18. **Time-varying data format**: Report that data were restructured into start-stop intervals using `tmerge()` (R) or equivalent long-format reshaping (Python). State the total number of intervals and mean intervals per subject.
19. **Recurring events — event burden**: Always report total number of events, number of subjects with at least one event, and mean/median events per subject.
20. **Recurring events — AG model**: Report HR with robust (sandwich) standard errors and 95% CI. Format: "HR = X.XX, 95% CI [X.XX, X.XX] (robust SE)". Note the independence assumption and that robust variance accounts for within-subject correlation.
21. **Recurring events — PWP model**: Report stratified HR per event number with robust SE. State time scale used (gap time or total time). Format: "For the [Nth] event, HR = X.XX, 95% CI [X.XX, X.XX] (robust SE)."
22. **Recurring events — frailty model**: Report fixed-effect HR with 95% CI plus frailty variance (theta). Format: "HR = X.XX, 95% CI [X.XX, X.XX]; frailty variance theta = X.XX (LR test *p* = .XXX)." Theta significantly > 0 indicates unobserved heterogeneity.
23. **Python limitation for recurrent events**: When recurrent event analysis is performed, note in the methods section that R was used because `lifelines` does not natively support recurrent event models.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| KM overall | Always | Overall survival curve |
| KM per group | Group comparison | Survival by group |
| Number-at-risk table | With every KM plot | Sample size over time |
| KM per predictor level | Categorical predictors | Univariate screening |
| Martingale residuals vs predictor | Continuous predictors | Linearity check |
| Cox coefficient forest plot | After Cox PH | Effect summary (HRs) |
| Cox-Snell residuals | After Cox PH | Overall model fit |
| Deviance residuals | After Cox PH | Outlier detection |
| Schoenfeld residuals vs time | After Cox PH | PH assumption per predictor |
| RSF variable importance | After RSF | Feature ranking |
| Partial dependence plots | After RSF | Marginal effects on survival |
| Subgroup forest plot | Subgroup analysis | Stratified HRs |
| Stratified KM curves | Subgroup analysis | Visual subgroup comparison |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
