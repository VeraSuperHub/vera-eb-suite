# Sentence Bank --- Binary Outcome Results

## Purpose

Provide varied phrasings for each type of statistical result. The skill
selects from these contextually --- never repeating patterns within a single
document. This is the core output quality variation mechanism for prose output.

## Rules

- Pick ONE variant per result instance
- Never repeat the same variant within a single results.md
- Adapt to actual data context (variable names, direction, magnitude)
- These are structural templates --- the actual text must feel natural and
  specific to the study, not templated

---

## Class Balance

B1: "The outcome [outcome] was observed in [n] of [N] cases ([pct]%). The minority class ([label]) comprised [pct]% of the sample, indicating [adequate/imbalanced] class representation."

B2: "Of the [N] participants, [n] ([pct]%) experienced [outcome]. The event rate of [pct]% was [sufficient for / below the threshold for] standard logistic modeling without correction."

B3: "Class distribution analysis revealed that [pct]% of cases were classified as [level_1] and [pct]% as [level_0]. This [balanced/imbalanced] distribution [supports standard methods / warrants caution regarding model stability]."

B4: "[Outcome] was [present/absent] in [n] cases ([pct]%), with the remaining [n] ([pct]%) classified as [level_0]. The class balance was [adequate/marginal/poor] for the planned analyses."

---

## Chi-Square / Fisher's Exact

X1: "A significant association was observed between [group_var] and [outcome], chi-sq([df]) = [val], *p* [val], Cramer's *V* = [val], indicating a [small/medium/large] effect."

X2: "Chi-square analysis revealed that [outcome] was significantly associated with [group_var], chi-sq([df]) = [val], *p* [val]. The strength of association was [small/medium/large] (Cramer's *V* = [val])."

X3: "[Group_var] and [outcome] were significantly related, chi-sq([df]) = [val], *p* [val]. Fisher's exact test confirmed this association (*p* [val]). The effect was [magnitude] (Cramer's *V* = [val])."

X4: "The relationship between [group_var] and [outcome] was statistically significant, chi-sq([df]) = [val], *p* [val], with Cramer's *V* = [val] suggesting a [magnitude] association."

X5: "There was [no] statistically significant association between [group_var] and [outcome], chi-sq([df]) = [val], *p* [val], Cramer's *V* = [val]. The pattern of proportions [description]."

---

## Odds Ratio

O1: "[Group1] had [val] times the odds of [outcome] compared to [Group2] (OR = [val], 95% CI [[L], [U]]). This [significant/non-significant] elevation in odds corresponds to a [pct]% [increase/decrease] in the likelihood of [outcome]."

O2: "The odds of [outcome] were [val] times [higher/lower] among [Group1] relative to [Group2] (OR = [val], 95% CI [[L], [U]], *p* [val])."

O3: "Compared to [reference], [group] exhibited [significantly/non-significantly] [elevated/reduced] odds of [outcome] (OR = [val], 95% CI [[L], [U]]). The confidence interval [includes/excludes] 1.0, [consistent with / suggesting] [conclusion]."

O4: "[Outcome] was associated with [group_var]: OR = [val], 95% CI [[L], [U]]. [Group1] were [interpretation] as likely to [outcome verb] relative to [Group2]."

---

## Logistic Regression

L1: "The logistic regression model was significant (chi-sq([df]) = [val], *p* < .001) and accounted for [McFadden R2]% of the variance (McFadden *R*2 = [val], Nagelkerke *R*2 = [val]). [Strongest predictor] was the strongest predictor (OR = [val], 95% CI [[L], [U]])."

L2: "A multivariable logistic regression predicting [outcome] from [predictor list] was statistically significant. After adjusting for covariates, [predictor] remained independently associated with [outcome] (OR = [val], 95% CI [[L], [U]], *p* [val])."

L3: "The logistic model accounted for [Nagelkerke]% of the variance in [outcome] (Nagelkerke *R*2 = [val]). Among the predictors, [var1] (OR = [val]) and [var2] (OR = [val]) showed the strongest independent associations."

L4: "[Outcome] was regressed on [predictor list] using logistic regression. The overall model was significant (*p* < .001), with Hosmer-Lemeshow goodness-of-fit indicating adequate calibration (chi-sq([df]) = [val], *p* = [val]). [Key finding about specific predictor with OR, CI, p]."

---

## ROC / AUC

A1: "The logistic model demonstrated [excellent/good/fair/poor] discrimination, AUC = [val], 95% CI [[L], [U]]. At the optimal threshold ([val], Youden's index), sensitivity was [val]% and specificity was [val]%."

A2: "Receiver operating characteristic analysis yielded an AUC of [val] (95% CI [[L], [U]]), indicating [discrimination level]. The model correctly classified [val]% of cases at the optimal cutpoint of [val]."

A3: "The area under the ROC curve was [val] (95% CI [[L], [U]]), suggesting [discrimination quality]. Using Youden's index to determine the optimal threshold ([val]), the model achieved a sensitivity of [val]% and specificity of [val]%."

A4: "Model discrimination was assessed via ROC analysis. The in-sample AUC was [val] (95% CI [[L], [U]]), [which should be interpreted cautiously absent external validation / indicating adequate discriminative ability]."

---

## Subgroup Analysis (Stratified ORs)

S1: "Subgroup analysis examined whether the [group_var]--[outcome] association differed by [subgroup]. The OR was [val] (95% CI [[L], [U]]) within [sub1] and [val] (95% CI [[L], [U]]) within [sub2]. The Breslow-Day test was [not] significant (chi-sq([df]) = [val], *p* = [val])."

S2: "To explore potential effect modification, odds ratios were computed within each stratum of [subgroup]. ORs [varied/were similar] across strata (Figure [X]). The Breslow-Day test [did/did not] indicate heterogeneity of odds ratios (*p* = [val])."

S3: "Stratified analysis by [subgroup] revealed [consistent/divergent] associations between [group_var] and [outcome]. Within [sub1] (*n* = [val]), OR = [val]; within [sub2] (*n* = [val]), OR = [val]. The Mantel-Haenszel common OR was [val] (95% CI [[L], [U]]). The [group_var] x [subgroup] interaction was [not] statistically significant (*p* = [val])."

---

## Tree-Based (Exploratory Classification)

E1: "Random forest analysis identified [var1] and [var2] as the most important predictors of [outcome] (Figure [X]). In-sample AUC = [val]; however, given *N* = [val], these results should be interpreted as exploratory."

E2: "Tree-based models were fit as an exploratory complement. Variable importance rankings from the random forest were [consistent with / partially divergent from] the logistic results, with [var1] ranked first. The high in-sample AUC ([val]) likely reflects overfitting."

E3: "As an exploratory analysis, ensemble classification methods (random forest, LightGBM) were applied. [Var1] emerged as the dominant predictor across all tree-based approaches. These findings corroborate the logistic regression results but cannot be interpreted as validated predictions given the sample size."

---

## Model Comparison Synthesis

C1: "Across all analytic approaches, [key finding]. The logistic model provides the most interpretable results through adjusted odds ratios, while tree-based analyses confirm the variable importance hierarchy."

C2: "The convergence of logistic regression, chi-square, and machine learning methods strengthens confidence in [finding]. Logistic regression additionally provided adjusted ORs controlling for [covariates]."

C3: "Taken together, [finding] was robust across logistic, bivariate, and tree-based methods. The logistic regression model is recommended for manuscript reporting, supplemented by [specific insight] from the exploratory tree analysis."

C4: "Variable importance rankings were [largely consistent / partially divergent] across logistic regression and tree-based methods. [Var1] ranked first across all approaches, supporting its role as the primary predictor of [outcome]. The unified importance table (Table [X]) summarizes these convergent findings."
