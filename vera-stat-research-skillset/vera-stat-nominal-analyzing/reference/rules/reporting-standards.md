# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

1. **p-values**: Never "p = 0.000" → use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no association" or "no effect" → "not statistically significant at alpha = [level]"
3. **Effect sizes**: Always alongside p-values. Cramer's V for Chi-square. Eta-squared for ANOVA. Standardized coefficients for multinomial logistic.
4. **95% CIs**: Always report. Adjust only if user specifies.
5. **Degrees of freedom**: Report with Chi-square, F, and LR test statistics.
6. **Sample size**: Report final analytic N (after exclusions), not original N. Report per-class n.
7. **RRR (Relative Risk Ratios)**: Report as "RRR = X.XX, 95% CI [X.XX, X.XX]" — always state reference category.
8. **Reference category**: State explicitly in both methods and results. Justify choice (most frequent, or substantively meaningful baseline).
9. **Confusion matrix**: Report overall accuracy + per-class precision and recall. Add in-sample caveat if N < 200 or no train/test split.
10. **LDA**: Report Wilks' lambda, approximate F, df, p. Report discriminant function loadings (structure matrix). Report canonical correlations.
11. **Chi-square**: Report chi-square statistic, df, p, Cramer's V. If any expected cell < 5, also report Fisher's exact. Note observed vs expected when informative.
12. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity.
13. **Decimal places**: 2 for RRR/coefficients/SEs, 3 for p-values, 2 for effect sizes (Cramer's V, eta-squared), 0 for frequencies, 1 for percentages.
14. **Class-specific reporting**: For multinomial logistic, report results for EACH non-reference class separately. Do not collapse across classes.
15. **Unified importance**: Normalize to 0-100 scale. Report rank consensus. Never frame as "which model is best."

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Bar chart (class distribution) | Always | Class balance assessment |
| Mosaic/grouped bar | Categorical predictor | Association visualization |
| Box plot by class | Continuous predictor | Distribution comparison |
| RRR coefficient plot | After multinomial | Class-specific effect summary |
| LDA score scatter | After LDA | Discriminant space visualization |
| Classification tree | After CART | Interpretable rules |
| Variable importance plot | After RF/LightGBM | Feature ranking |
| Confusion matrix heatmap | After each model | Classification quality |
| Unified importance plot | After comparison | Cross-method convergence |
| Subgroup proportions | Subgroup analysis | Stratified class distributions |
| Effect comparison plot | Subgroup analysis | Stratified effect sizes |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
