# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

## General Rules

1. **p-values**: Never "p = 0.000" -> use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" -> "not statistically significant at alpha = [level]"
3. **Sample size**: Report k (number of studies) and total N (participants) throughout. Never conflate.
4. **Decimal places**: 2 for effect sizes and CIs, 3 for p-values, 1 for I², 3 for τ².

## Meta-Analysis-Specific Rules

5. **Effect size with CI**: Always format: "[stat] = X.XX, 95% CI [X.XX, X.XX]". Include direction interpretation.
6. **Heterogeneity triple**: Always report Q, I², and τ² together. Format: "Q(df) = X.XX, p = .XXX; I² = XX.X%; τ² = X.XXX".
7. **I² interpretation**: Use Higgins thresholds (25% low, 50% moderate, 75% high). Never claim homogeneity when I² > 0 and Q is nonsignificant — note low power of Q test for small k.
8. **Prediction interval**: Report alongside pooled estimate when I² > 25%. Format: "95% prediction interval [X.XX, X.XX]".
9. **Model specification**: Always state fixed-effects vs. random-effects (and why). For random-effects, state τ² estimator (REML, DL, etc.).
10. **Forest plot**: Must include individual study weights (%), point estimates with CIs, and summary diamond. Studies labeled with author(year) format.
11. **Funnel plot**: Must include pseudo 95% CI lines. State whether visual asymmetry was observed.
12. **Publication bias tests**: Report at least two methods (Egger's + one other). State test statistic, df, and p-value.
13. **Trim-and-fill**: Report number of imputed studies and adjusted pooled estimate with CI. Interpret cautiously — note method limitations.
14. **Subgroup analysis**: Report Q_between with df and p-value. Report within-subgroup effects with CIs and k per subgroup.
15. **Meta-regression**: Report slope, SE, p-value, and R² (proportion of τ² explained). Note that R² can exceed 100% or be negative — explain if so.
16. **Leave-one-out**: Report range of pooled estimates and whether any single study shifts significance.
17. **Small k warning**: If k < 10, explicitly note: (a) low power for heterogeneity tests, (b) funnel plot unreliable, (c) meta-regression inadvisable. Do NOT suppress the analysis — run it but caveat interpretation.
18. **PRISMA compliance**: Manuscript sections should align with PRISMA 2020 reporting items where applicable.
19. **Effect size conversion**: When studies report different metrics, state conversion formula used (e.g., log OR to d via d = log(OR) × √3 / π).
20. **Study quality / risk of bias**: If quality scores are available, report as moderator. Never use quality as exclusion criterion without justification.
