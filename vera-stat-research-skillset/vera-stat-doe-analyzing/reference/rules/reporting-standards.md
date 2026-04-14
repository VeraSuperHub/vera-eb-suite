# Reporting Standards -- Hard Rules

Apply to ALL output. Never violate.

1. **p-values**: Never "p = 0.000" -> use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" -> "not statistically significant at alpha = [level]"
3. **Effect sizes**: Always alongside F-tests. Partial eta-squared for ANOVA effects.
4. **95% CIs**: Always report for effect estimates and contrasts. Adjust only if user specifies.
5. **Degrees of freedom**: Report with ALL F statistics: F(df1, df2) = X.XX.
6. **Sample size**: Report total N and cell sizes (N per treatment combination).
7. **SS Type III**: Always use Type III SS. State explicitly in methods.
8. **Effect estimates**: Report with SE for all contrasts and marginal means.
9. **R-squared for RSM**: Say "explained X% of variance" -- this IS a designed experiment, so causal language is appropriate.
10. **Tree-based with small N**: Frame as "exploratory" or "corroborative." Never claim predictive validity.
11. **Decimal places**: 2 for means/SDs/effect estimates, 3 for p-values, 3 for partial eta-squared, 2 for R-squared.
12. **Fractional factorial**: Always report design resolution (III, IV, V) and alias structure.
13. **Split-plot**: Report which error term was used for each effect.
14. **RSM canonical analysis**: Report stationary point coordinates, eigenvalues, and classification (max/min/saddle/ridge).
15. **Post-hoc**: Report adjustment method (Tukey, Bonferroni, Scheffe) and adjusted p-values.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Interaction plot | Always | Factor interactions |
| Main effects plot | Always | Marginal means |
| Pareto / half-normal | 2^k or fractional | Active effect identification |
| Contour plot | RSM (continuous factors) | Response landscape |
| Surface plot (3D) | RSM (continuous factors) | Response landscape |
| Residuals vs fitted | Always | Model adequacy |
| Residuals vs factors | Always | Per-factor variance check |
| Normal Q-Q of residuals | Always | Normality assumption |
| Scale-location | Always | Homoscedasticity |
| Effect ranking bar chart | Always | Factor importance |
| Variable importance | After tree-based | Factor ranking confirmation |
| Forest plot by block | If stratified | Block consistency |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
