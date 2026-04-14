# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

## General Rules

1. **p-values**: Never "p = 0.000" → use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" → "not statistically significant at α = [level]"
3. **Sample size**: Report final analytic N (after exclusions), not original N.
4. **Decimal places**: 2 for coefficients/SEs, 3 for p-values, 2 for IRR/effect sizes, 2 for M/SD.

## Count-Specific Rules

5. **IRR**: Always report as "IRR = X.XX, 95% CI [X.XX, X.XX]" — never raw log-scale coefficients alone.
6. **Rate**: "X.XX events per [unit] of exposure" — always specify the denominator unit.
7. **Overdispersion**: Report deviance/df ratio. State whether Poisson or NB is preferred and why.
8. **Poisson vs NB**: Likelihood ratio test as "LR χ²(1) = X.XX, p [val]".
9. **ZIP/ZINB**: Vuong test as "Vuong statistic = X.XX, p [val]".
10. **Hurdle model**: Report both components separately (zero/non-zero logistic + truncated count).
11. **Count means**: Report with SD (not SE unless explicitly comparing means).
12. **Log-scale coefficients**: Report B (log IRR) with SE for technical audience; always accompany with exponentiated IRR.
13. **Offset**: When exposure/offset is used, explicitly state "with log([exposure]) as offset" in methods.
14. **Degrees of freedom**: Report with chi-square, LR test, and Wald test statistics.
15. **95% CIs**: Always report for IRR. Adjust CI level only if user specifies.

## Model Comparison Rules

16. **AIC**: Report for all fitted count models. Frame as "distributional fit" not "model competition."
17. **Model selection**: "The [model] provided the best fit to the observed count distribution (AIC = X.XX)" — never "the [model] won."
18. **Tree-based with small N**: Frame as "exploratory" or "pattern detection." Never claim predictive validity.
19. **Variable importance**: Report on unified 0-100 scale. State which methods contributed to the ranking.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Count frequency bar chart | Always | Count distribution |
| Poisson overlay | Always | Expected vs observed frequencies |
| Mean counts bar chart | Group comparison | Group differences |
| IRR forest plot | After count regression | Effect summary |
| Residual vs fitted | After Poisson/NB | Model adequacy |
| Rootogram | After count models | Distributional fit |
| Variable importance | After tree-based | Feature ranking |
| Subgroup forest plot | Subgroup analysis | Stratified IRRs |
| Grouped bar chart | Subgroup analysis | Visual interaction |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
