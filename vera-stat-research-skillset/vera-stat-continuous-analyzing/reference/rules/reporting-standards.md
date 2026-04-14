# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

1. **p-values**: Never "p = 0.000" → use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" → "not statistically significant at α = [level]"
3. **Effect sizes**: Always alongside p-values. Standardized β for OLS. Cohen's d for t-tests. η² for ANOVA.
4. **95% CIs**: Always report. Adjust only if user specifies.
5. **Degrees of freedom**: Report with F and t statistics.
6. **Sample size**: Report final analytic N (after exclusions), not original N.
7. **Coefficients**: Unstandardized B with SE always. Add standardized β when predictors on different scales.
8. **R²**: Say "accounted for X% of variance" — not "explained" unless true experiment.
9. **Quantile regression**: Report specific quantile(s) and SE method (bootstrap preferred).
10. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity.
11. **Decimal places**: 2 for coefficients/SEs, 3 for p-values, 2 for R²/effect sizes, 2 for M/SD.
12. **Transformations**: Report on both transformed and original scales. Back-transform for interpretation.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Histogram + density | Always | Distribution |
| Q-Q plot | Always | Normality |
| Residual vs fitted | After OLS | Linearity assumption |
| Scale-location | After OLS | Homoscedasticity |
| Coefficient forest plot | After regression | Effect summary |
| Quantile process plot | After QR | Distributional effects |
| Variable importance | After tree-based | Feature ranking |
| Partial dependence | After tree-based | Marginal effects |
| Box plot by group | Group comparison | Group differences |
| Subgroup forest plot | Subgroup analysis | Stratified effects |
| Subgroup scatter | Subgroup analysis | Visual interaction |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
