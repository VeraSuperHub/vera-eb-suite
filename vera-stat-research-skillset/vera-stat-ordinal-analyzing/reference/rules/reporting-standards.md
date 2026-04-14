# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

1. **p-values**: Never "p = 0.000" → use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" → "not statistically significant at α = [level]"
3. **Effect sizes**: Always alongside p-values. Rank-biserial r for Mann-Whitney. Cliff's delta for pairwise. Epsilon-squared for Kruskal-Wallis.
4. **95% CIs**: Always report for cumulative ORs and effect sizes. Adjust only if user specifies.
5. **Medians and IQRs**: Always for ordinal data. Never report means/SDs for ordinal outcomes.
6. **Sample size**: Report final analytic N (after exclusions), not original N.
7. **Cumulative OR**: Format as "cumulative OR = X.XX, 95% CI [X.XX, X.XX]". Always with 95% CI.
8. **Proportional odds assumption**: Report Brant test as "χ²(df) = X.XX, p = .XXX". If violated, state which predictors.
9. **Proportions per level**: Report as percentages with 1 decimal (e.g., "42.3%").
10. **Mann-Whitney U**: Report as "U = X, p = .XXX, rank-biserial r = .XXX".
11. **Kruskal-Wallis**: Report as "H(df) = X.XX, p = .XXX".
12. **Spearman rho**: Report as "ρ = .XXX, p = .XXX" with 95% CI when available.
13. **Goodman-Kruskal gamma**: Report as "γ = .XXX, SE = .XXX, p = .XXX".
14. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity.
15. **Decimal places**: 2 for coefficients/SEs/ORs, 3 for p-values, 3 for effect sizes (r, delta, rho), 1 for proportions.
16. **Ordinal coding**: Always state how ordinal levels were coded numerically (e.g., "None = 1, Some = 2, Marked = 3").
17. **Multinomial logistic (class-specific OR)**: Format as "OR = X.XX, 95% CI [X.XX, X.XX], *p* = .XXX" per class contrast. Always state the reference category. Report for each non-reference level separately.
18. **Adjacent-category logit**: Format as "adjacent-category OR = X.XX, 95% CI [X.XX, X.XX], *p* = .XXX". Interpret as odds of level k+1 vs. level k. Specify which transition each OR refers to.
19. **Continuation-ratio logit**: Format as "continuation-ratio OR = X.XX, 95% CI [X.XX, X.XX], *p* = .XXX". Interpret as odds of advancing to level k among those who reached level k. State the conditioning set clearly.
20. **Stereotype model**: Report scaling parameters (phi) alongside coefficients. Format as "coefficient = X.XX, phi(k) = X.XX, *p* = .XXX". Explain that phi quantifies how the predictor effect varies across ordinal levels.
21. **LightGBM importance**: Report as gain-based importance normalized to 0-100 scale. Always report alongside RF importance for comparison. Label as "LightGBM importance (gain)" to distinguish from permutation importance.
22. **Dual-path framing**: Always present Path A (multi-class) and Path B (ordinal-specific) as complementary lenses. Never frame one path as superior. The convergence or divergence between paths is the finding.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Bar chart + cumulative line | Always | Ordinal distribution |
| Stacked bar chart | Group comparison | Group × outcome distribution |
| Diverging stacked bar | Group comparison (alt.) | Centered group comparison |
| Predicted probability plot | After proportional odds | Predicted P(Y ≤ j) across predictor |
| Variable importance | After tree-based | Feature ranking |
| Forest plot | Subgroup analysis | Stratified effects |
| Subgroup stacked bar | Subgroup analysis | Visual interaction |
| Spearman scatter | Continuous predictor | Monotonic association |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
