# Sentence Bank — Nominal Outcome Results

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

## Class Distribution

CD1: "The outcome variable [outcome] comprised [k] classes: [list with n and %]. Class frequencies were [approximately balanced / moderately imbalanced / highly imbalanced]."

CD2: "Among the [N] observations, [outcome] was distributed as follows: [list]. [Largest class] was the most prevalent ([%]), while [smallest class] represented [%] of the sample."

CD3: "Examination of the [outcome] distribution revealed [k] categories with [balanced/unequal] representation. [Details about balance or rare classes]."

CD4: "[Outcome] had [k] levels. The modal category was [class] (*n* = [val], [%]%). [Comment on balance or rarity]."

---

## Chi-Square / Association Test

X1: "A Chi-square test of independence revealed a [significant/non-significant] association between [predictor] and [outcome], chi2([df]) = [val], *p* [val], Cramer's *V* = [val], indicating a [small/medium/large] effect."

X2: "The association between [predictor] and [outcome] was statistically [significant/non-significant], chi2([df]) = [val], *p* [val]. The strength of association was [magnitude] (Cramer's *V* = [val])."

X3: "[Predictor] was [significantly/not significantly] associated with [outcome] class membership, chi2([df]) = [val], *p* [val]. Cramer's *V* = [val] suggested a [small/medium/large] effect size."

X4: "Cross-tabulation of [predictor] and [outcome] yielded a [significant/non-significant] Chi-square statistic, chi2([df]) = [val], *p* [val], with a [magnitude] association (Cramer's *V* = [val])."

---

## ANOVA (Continuous Predictor by Outcome Class)

AN1: "[Predictor] differed significantly across [outcome] classes, *F*([df1], [df2]) = [val], *p* [val], eta2 = [val]. Post-hoc Tukey HSD tests revealed [which pairs differ]."

AN2: "A one-way ANOVA indicated significant between-class differences in [predictor], *F*([df1], [df2]) = [val], *p* [val], with [outcome] class accounting for [eta2*100]% of the variance in [predictor] (eta2 = [val])."

AN3: "Significant variation in [predictor] was observed across [outcome] classes, *F*([df1], [df2]) = [val], *p* [val]. The effect was [small/medium/large] (eta2 = [val]). Pairwise comparisons using Tukey HSD showed [details]."

AN4: "[Predictor] means varied by [outcome]: [class1] (*M* = [val], *SD* = [val]), [class2] (*M* = [val], *SD* = [val]), [class3] (*M* = [val], *SD* = [val]). This difference was statistically significant, *F*([df1], [df2]) = [val], *p* [val], eta2 = [val]."

---

## Multinomial Logistic Regression

M1: "Multinomial logistic regression with [reference] as the reference category indicated that [predictor] was a significant predictor of class membership. Compared to [reference], a one-unit increase in [predictor] was associated with [RRR] times the relative risk of being classified as [class] (RRR = [val], 95% CI [[L], [U]], *p* [val])."

M2: "The multinomial model (McFadden's pseudo-*R*2 = [val]) revealed that [predictor] significantly differentiated [class] from [reference] (RRR = [val], 95% CI [[L], [U]]). The likelihood ratio test for [predictor] was significant (chi2 = [val], *p* [val])."

M3: "Using [reference] as the baseline, the multinomial logistic model showed [key finding]. [Predictor] had the strongest association with class membership, with RRR = [val] for [class] vs [reference] (95% CI [[L], [U]])."

M4: "Relative to [reference], [predictor] was positively associated with membership in [class] (RRR = [val], 95% CI [[L], [U]], *p* [val]) but [negatively/not significantly] associated with [other class] (RRR = [val], 95% CI [[L], [U]], *p* [val])."

---

## Linear Discriminant Analysis

L1: "LDA identified [k-1] discriminant functions. The first function (Wilks' lambda = [val], *p* [val]) accounted for [%]% of the between-group variance. [Var1] and [var2] had the highest loadings on this function."

L2: "Linear discriminant analysis yielded [k-1] canonical discriminant functions. Wilks' lambda for the overall model was [val] (*p* [val]), indicating [significant/non-significant] discrimination. The structure matrix showed that [var1] (loading = [val]) was the strongest discriminator."

L3: "The LDA model achieved [accuracy]% in-sample classification accuracy. The first discriminant function, loaded most heavily by [var1] ([val]) and [var2] ([val]), separated [class1] from the other classes. The second function primarily distinguished [class2] from [class3]."

L4: "Discriminant analysis with [k] classes produced [k-1] discriminant functions (Wilks' lambda = [val], approximate *F* = [val], *p* [val]). Variable loadings on the first function were: [var1] = [val], [var2] = [val], [var3] = [val]."

---

## Tree-Based (Exploratory)

E1: "Random forest analysis identified [var1] and [var2] as the most important predictors of [outcome] class membership (Figure [X]). In-sample accuracy = [val]%; however, given *N* = [val], these results should be interpreted as exploratory."

E2: "Tree-based models were fit as an exploratory complement. Variable importance rankings from the random forest were [consistent with / partially divergent from] the multinomial logistic results, with [var1] ranked first. The high in-sample accuracy ([val]%) likely reflects overfitting."

E3: "As an exploratory analysis, ensemble tree methods (random forest, LightGBM) were applied to the multi-class classification. [Var1] emerged as the dominant predictor across all tree-based approaches. These findings corroborate the parametric results but cannot be interpreted as validated predictions given the sample size."

E4: "The classification tree identified [var1] as the primary splitting variable, followed by [var2]. This aligns with the multinomial logistic and LDA results, providing converging evidence for the importance of [var1] in distinguishing [outcome] classes."

---

## Subgroup Analysis

S1: "Subgroup analysis examined whether the [predictor]-[outcome] association differed by [subgroup]. The association was [significant/not significant] within [sub1] (Cramer's *V* = [val]) and [sub2] (Cramer's *V* = [val]). The interaction test was [not] significant (LR chi2 = [val], *p* = [val])."

S2: "To explore potential heterogeneity, the [predictor]-[outcome] association was examined separately within each level of [subgroup]. Effect sizes [varied/were similar] across subgroups (Figure [X]). The formal interaction test [did/did not] reach significance (LR chi2 = [val], *p* = [val])."

S3: "Stratified analysis by [subgroup] revealed [consistent/divergent] associations between [predictor] and [outcome] class membership. Within [sub1] (*n* = [val]), Cramer's *V* = [val]; within [sub2] (*n* = [val]), Cramer's *V* = [val]. The interaction was [not] statistically significant (*p* = [val])."

---

## Model Comparison Synthesis

C1: "Across all analytic approaches — multinomial logistic, LDA, and tree-based methods — [key finding]. The multinomial model provides the most interpretable class-specific results, while tree-based analyses confirm the variable importance hierarchy."

C2: "The convergence of parametric (multinomial logistic), discriminant (LDA), and machine learning methods strengthens confidence in [finding]. LDA additionally revealed [discriminant dimension insight]."

C3: "Taken together, [finding] was robust across multinomial logistic, LDA, and tree-based methods. The multinomial model is recommended for manuscript reporting due to its class-specific interpretability (RRR), supplemented by [specific insight] from the LDA and importance rankings from the ensemble methods."

C4: "[Var1] emerged as the top-ranked predictor across all four methods (unified importance: multinomial = [val], LDA = [val], RF = [val], LightGBM = [val]). This convergence provides strong evidence for its role in differentiating [outcome] classes."
