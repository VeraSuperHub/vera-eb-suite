# Sentence Bank — Continuous Outcome Results

## Purpose

Provide varied phrasings for each type of statistical result. The skill
selects from these contextually — never repeating patterns within a single
document. This is the core output quality variation mechanism for prose output.

## Rules

- Pick ONE variant per result instance
- Never repeat the same variant within a single results.md
- Adapt to actual data context (variable names, direction, magnitude)
- These are structural templates — the actual text must feel natural and
  specific to the study, not templated

---

## Distribution Check

D1: "[Outcome] was approximately normally distributed (Shapiro-Wilk *W* = [val], *p* = [val]; skewness = [val]). Parametric methods were selected as the primary analytic approach."

D2: "Visual inspection of the histogram and Q-Q plot, supplemented by the Shapiro-Wilk test (*W* = [val], *p* = [val]), indicated that [outcome] was approximately normally distributed (skewness = [val], kurtosis = [val])."

D3: "Distributional assessment revealed that [outcome] met the assumption of normality (*W* = [val], *p* = [val]), with skewness ([val]) and kurtosis ([val]) within acceptable ranges."

D4: "The distribution of [outcome] was examined prior to analysis. The Shapiro-Wilk test was non-significant (*W* = [val], *p* = [val]), and skewness ([val]) was within ±1, supporting the use of parametric methods."

---

## t-test (2 groups)

T1: "[Group1] (*M* = [val], *SD* = [val]) had significantly [higher/lower] [outcome] than [Group2] (*M* = [val], *SD* = [val]), *t*([df]) = [val], *p* [val], Cohen's *d* = [val]."

T2: "A Welch's *t*-test revealed a significant difference in [outcome] between [Group1] and [Group2], *t*([df]) = [val], *p* [val]. [Group1] scored [val] units [higher/lower] (95% CI [[L], [U]]), corresponding to a [small/medium/large] effect (Cohen's *d* = [val])."

T3: "The difference in [outcome] between [Group1] (*M* = [val], *SD* = [val]) and [Group2] (*M* = [val], *SD* = [val]) was statistically significant, *t*([df]) = [val], *p* [val], with a [magnitude] effect size (*d* = [val], 95% CI [[L], [U]])."

T4: "[Outcome] differed significantly by [grouping variable], *t*([df]) = [val], *p* [val]. [Group1] averaged [val] units [higher/lower] than [Group2] (Cohen's *d* = [val]), indicating a [magnitude] practical difference."

---

## ANOVA (3+ groups)

A1: "[Outcome] differed significantly across [grouping variable] levels, *F*([df1], [df2]) = [val], *p* [val], η² = [val]. Post-hoc Tukey HSD tests revealed [which pairs]."

A2: "A one-way ANOVA indicated significant between-group differences in [outcome], *F*([df1], [df2]) = [val], *p* [val], with [grouping variable] accounting for [η²*100]% of the variance (η² = [val])."

A3: "Significant variation in [outcome] was observed across [grouping variable], *F*([df1], [df2]) = [val], *p* [val]. The effect was [small/medium/large] (η² = [val]). Pairwise comparisons using Tukey HSD showed [details]."

---

## Subgroup Analysis

S1: "Subgroup analysis examined whether the [predictor]–[outcome] association differed by [subgroup]. The effect was [significant/not significant] within [sub1] (*B* = [val], 95% CI [[L], [U]]) and [sub2] (*B* = [val], 95% CI [[L], [U]]). The interaction test was [not] significant (*F* = [val], *p* = [val])."

S2: "To explore potential heterogeneity, the [predictor] effect on [outcome] was examined separately within each level of [subgroup]. Effect sizes [varied/were similar] across subgroups (Figure [X]). The formal interaction test [did/did not] reach significance (*F* = [val], *p* = [val])."

S3: "Stratified analysis by [subgroup] revealed [consistent/divergent] associations between [predictor] and [outcome]. Within [sub1] (*n* = [val]), [predictor] was associated with a [val]-unit [change] in [outcome]; within [sub2] (*n* = [val]), the corresponding estimate was [val]. The [predictor] × [subgroup] interaction was [not] statistically significant (*p* = [val])."

---

## OLS Regression

R1: "The OLS model was significant, *F*([df1], [df2]) = [val], *p* < .001, and accounted for [R²*100]% of the variance in [outcome] (adjusted *R*² = [val]). [Top predictor] was the strongest predictor (*B* = [val], *p* [val])."

R2: "A multiple linear regression predicting [outcome] from [predictor list] was statistically significant, *F*([df1], [df2]) = [val], *p* < .001, *R*² = [val]. After adjusting for covariates, [predictor] remained positively associated with [outcome] (*B* = [val], 95% CI [[L], [U]])."

R3: "The regression model accounted for [R²*100]% of the variance in [outcome] (adjusted *R*² = [val]). Among the predictors, [var1] (β = [val]) and [var2] (β = [val]) showed the strongest standardized associations."

R4: "[Outcome] was regressed on [predictor list]. The overall model was significant (*F* = [val], *p* < .001), accounting for [R²*100]% of variance. [Key finding about specific predictor with B, CI, p]."

---

## Quantile Regression

Q1: "Quantile regression revealed that the association between [predictor] and [outcome] [varied/was consistent] across the distribution. At the 25th percentile, *B* = [val]; at the median, *B* = [val]; at the 75th percentile, *B* = [val]."

Q2: "To assess distributional heterogeneity, quantile regression was estimated at τ = .25, .50, and .75. The effect of [predictor] was [strongest/weakest] at the [Xth] percentile (*B* = [val], 95% CI [[L], [U]]), suggesting [interpretation]."

Q3: "Beyond the conditional mean, quantile regression indicated that [predictor] effects on [outcome] [intensified/attenuated] at higher quantiles. This suggests that [predictor] has a [disproportionate/uniform] impact across the [outcome] distribution."

---

## Tree-Based (Exploratory)

E1: "Random forest analysis identified [var1] and [var2] as the most important predictors of [outcome] (Figure [X]). In-sample *R*² = [val]; however, given *N* = [val], these results should be interpreted as exploratory."

E2: "Tree-based models were fit as an exploratory complement. Variable importance rankings from the random forest were [consistent with / partially divergent from] the OLS results, with [var1] ranked first. The high in-sample *R*² ([val]) likely reflects overfitting."

E3: "As an exploratory analysis, ensemble tree methods (random forest, LightGBM) were applied. [Var1] emerged as the dominant predictor across all tree-based approaches. These findings corroborate the parametric results but cannot be interpreted as validated predictions given the sample size."

---

## Model Comparison Synthesis

C1: "Across all analytic approaches, [key finding]. The OLS model provides the most interpretable results, while tree-based analyses confirm the variable importance hierarchy."

C2: "The convergence of parametric, quantile, and machine learning methods strengthens confidence in [finding]. Quantile regression additionally revealed [distributional insight]."

C3: "Taken together, [finding] was robust across OLS, quantile regression, and tree-based methods. The primary analysis (OLS) is recommended for manuscript reporting, supplemented by [specific insight] from the quantile analysis."
