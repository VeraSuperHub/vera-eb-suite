# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

## General Rules

1. **p-values**: Never "p = 0.000" → use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" → "not statistically significant at alpha = [level]"
3. **Effect sizes**: Always alongside p-values. Partial eta-squared for ANOVA effects. Cohen's d for paired comparisons.
4. **95% CIs**: Always report. Adjust only if user specifies.
5. **Degrees of freedom**: Report with F and t statistics.
6. **Sample size**: Report N subjects and total observations (after exclusions).
7. **Decimal places**: 2 for coefficients/SEs, 3 for p-values, 2 for effect sizes, 2 for M/SD.

## Repeated Measures Specific

8. **Fixed effects (LMM)**: B, SE, 95% CI, df (Satterthwaite or Kenward-Roger), t, p.
9. **Random effects**: Variance components with SD. If random slope, report correlation between random intercept and slope.
10. **ICC**: Report value with interpretation (e.g., "ICC = .72, indicating that 72% of the variance in [outcome] was between subjects").
11. **Sphericity**: Mauchly's W, p. If violated, report Greenhouse-Geisser epsilon and corrected p-values. Also report Huynh-Feldt epsilon for comparison.
12. **Partial eta-squared**: For each ANOVA effect (time, group, time x group). Use partial (not generalized).
13. **GEE**: Report working correlation structure chosen, estimated working correlations, robust SE. Note that coefficients are population-averaged.
14. **AIC/BIC**: For model comparison within LMM family only (not across model types like LMM vs GEE vs trees).
15. **Missing data**: Report attrition pattern (monotone vs intermittent), state MAR assumption explicitly if using LMM. Report N per time point.
16. **Pairwise comparisons**: Report both uncorrected and corrected p-values. State correction method (Bonferroni, Holm, or FDR).
17. **Growth curve**: Report linear and quadratic (or higher) time effects separately. Report group interactions with each polynomial term.
18. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity. Note that trees operate on subject-level features, not correlated observations.

## Coefficients

19. **Unstandardized B with SE**: Always. These are interpretable on the original scale.
20. **Standardized coefficients**: Add when predictors are on different scales (for LMM fixed effects).
21. **LMM vs GEE comparison**: When both reported, note that LMM gives subject-specific effects and GEE gives population-averaged effects. For linear models with identity link, these are often similar.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Spaghetti + mean ribbons | Always | Individual trajectories with group means |
| Interaction plot | Mixed ANOVA | Group x time means with error bars |
| Growth curve predicted | After growth model | Model-predicted trajectories per group |
| Residuals vs fitted | After LMM | Linearity assumption |
| Q-Q of residuals | After LMM | Normality of residuals |
| Random effects Q-Q | After LMM | Normality of random effects |
| Residuals vs time | After LMM | Heteroscedasticity over time |
| Coefficient forest plot | After LMM | Fixed effect summary |
| Variable importance | After tree-based | Feature ranking |
| Subgroup forest plot | Subgroup analysis | Stratified interaction effects |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
