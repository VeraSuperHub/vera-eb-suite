# Reporting Standards --- Hard Rules

Apply to ALL output. Never violate.

1. **p-values**: Never "p = 0.000" -> use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no association" or "no effect" -> "not statistically significant at alpha = [level]"
3. **Odds ratios**: Always with 95% CI. Format: "OR = X.XX, 95% CI [X.XX, X.XX]". Report direction in plain language.
4. **Chi-square**: Format: "chi-sq(df) = X.XX, p = .XXX, Cramer's V = .XXX". Always include df.
5. **Proportions**: Report as percentages with 1 decimal place (e.g., "38.2%").
6. **Logistic coefficients**: Report OR (not raw B) in results text. Raw B with SE in supplementary table only.
7. **Pseudo-R2**: Report McFadden and Nagelkerke. Say "accounted for" --- not "explained" unless true experiment.
8. **AUC**: Report with 95% CI. Note "in-sample" if no cross-validation. Format: "AUC = X.XX, 95% CI [X.XX, X.XX]".
9. **Classification**: Report sensitivity, specificity, accuracy, and threshold used.
10. **Hosmer-Lemeshow**: Format: "chi-sq(df) = X.XX, p = .XXX". Non-significant = adequate fit.
11. **Fisher's exact**: Report when any expected cell < 5. Format: "Fisher's exact p = .XXX".
12. **Sample size**: Report final analytic N (after exclusions), not original N. Report number of events.
13. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity.
14. **Decimal places**: 2 for OR/coefficients, 3 for p-values, 3 for effect sizes (Cramer's V), 1 for proportions, 2 for AUC.
15. **95% CIs**: Always report. Adjust only if user specifies different level.
16. **Degrees of freedom**: Report with chi-square, F, and t statistics.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Class balance bar chart | Always | Outcome distribution |
| Mosaic plot / grouped bar | Association test | Cell-level association |
| ROC curve | After logistic | Discrimination |
| OR forest plot | After logistic | Effect summary |
| Confusion matrix heatmap | After classification | Classification performance |
| Variable importance | After tree-based | Feature ranking |
| Subgroup forest plot | Subgroup analysis | Stratified ORs |
| Subgroup proportion chart | Subgroup analysis | Visual interaction |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
