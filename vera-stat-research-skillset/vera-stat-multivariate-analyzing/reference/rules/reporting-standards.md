# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

1. **p-values**: Never "p = 0.000" -> use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" -> "not statistically significant at alpha = [level]"
3. **Effect sizes**: Always alongside p-values. Partial eta-squared for ANOVAs/MANOVA follow-ups. Cohen's d for pairwise comparisons.
4. **95% CIs**: Always report. Adjust only if user specifies.
5. **Degrees of freedom**: Report with F, t, and chi-square statistics.
6. **Sample size**: Report final analytic N (after exclusions), not original N.
7. **MANOVA statistics**: Report all four (Pillai's V, Wilks' Lambda, Hotelling-Lawley T, Roy's theta) with F approximation and p. State which is primary and why.
8. **Box's M**: Report with F approximation and p. Use strict alpha (.001) for decision.
9. **Canonical correlations**: Report with Wilks' lambda significance test per dimension.
10. **Discriminant loadings**: Report structure coefficients. Bold loadings >= |.40|.
11. **Classification accuracy**: Overall and per-group hit rates. Report cross-validated accuracy.
12. **Profile analysis**: Report parallelism F, equal levels F, flatness F — each with df and p.
13. **PCA**: Eigenvalues, proportion of variance, cumulative proportion. Report loadings >= |.40|.
14. **Bonferroni correction**: State corrected alpha when multiple univariate follow-ups are conducted.
15. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity.
16. **Decimal places**: 2 for coefficients/SEs/means/SDs, 3 for p-values, 2 for R-squared/effect sizes, 3 for canonical correlations.
17. **Multivariate regression**: Pillai's Trace for overall test per predictor. Individual R-squared per DV.
18. **Importance normalization**: 0-100 scale (max = 100) for cross-method comparison tables.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Scatterplot matrix | Always | Bivariate relationships + correlation |
| Group means profile | Always | DV patterns across groups |
| Univariate box plots | Follow-up ANOVAs | Per-DV group differences |
| Discriminant scatter | After LDA | Group separation in discriminant space |
| Territorial map | After LDA (2+ functions) | Classification boundaries |
| Interaction plot | Two-way MANOVA | Factor interaction |
| Profile plot | Profile analysis | Parallelism / levels / flatness |
| CCA variate scatter | After CCA | Canonical variate relationships |
| Scree plot | After PCA | Component retention |
| Biplot | After PCA | Component loadings + scores |
| Importance heatmap | After tree-based | Cross-DV importance comparison |
| MV regression coefficients | After MV regression | Predictor effects across DVs |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
