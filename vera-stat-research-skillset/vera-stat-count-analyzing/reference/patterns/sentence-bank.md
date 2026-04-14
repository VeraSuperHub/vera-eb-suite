# Sentence Bank — Count Outcome Results

## Purpose

Provide varied phrasings for each type of statistical result. The skill
selects from these contextually — never repeating patterns within a single
document. This is the core output quality variation mechanism for prose output.

## Rules

- Pick ONE variant per result instance
- Never repeat the same variant within a single results.md
- Adapt to actual data context (variable names, direction, IRR magnitude)
- These are structural templates — the actual text must feel natural and
  specific to the study, not templated

---

## Distribution Check (Count)

D1: "The distribution of [outcome] showed [overdispersion/equidispersion] (variance/mean ratio = [val]). The proportion of zeros was [val]%, [consistent with / exceeding] the Poisson expectation of [val]%."

D2: "Examination of the count distribution revealed a mean of [val] with variance [val], yielding an overdispersion ratio of [val]. [This suggested Poisson assumptions were tenable / This indicated overdispersion, favoring a negative binomial approach]."

D3: "[Outcome] counts ranged from [min] to [max] (*M* = [val], *SD* = [val]). The variance-to-mean ratio ([val]) [was close to 1, supporting equidispersion / substantially exceeded 1, indicating overdispersion]. Zero counts comprised [val]% of observations."

D4: "Prior to model fitting, the count distribution was assessed. The overdispersion ratio (variance/mean = [val]) [supported / contradicted] the Poisson equidispersion assumption. [Zero inflation was not a concern / Excess zeros were noted] ([val]% observed vs [val]% Poisson expected)."

---

## Group Comparison (IRR — 2 groups)

G1: "[Group1] had a significantly [higher/lower] rate of [outcome] compared to [Group2] (IRR = [val], 95% CI [[L], [U]], *p* [val]). The mean count was [val] (*SD* = [val]) in [Group1] versus [val] (*SD* = [val]) in [Group2]."

G2: "The incidence rate of [outcome] was [val] times [higher/lower] in [Group1] relative to [Group2] (IRR = [val], 95% CI [[L], [U]]). This difference was statistically significant (*p* [val]) and confirmed by Mann-Whitney *U* test (*p* [val])."

G3: "A [Poisson/negative binomial] regression indicated that [Group1] experienced [outcome] at [val] times the rate of [Group2] (IRR = [val], 95% CI [[L], [U]], *p* [val]). The nonparametric Mann-Whitney *U* test corroborated this finding (*p* [val])."

G4: "[Outcome] differed significantly between [Group1] and [Group2], with an incidence rate ratio of [val] (95% CI [[L], [U]], *p* [val]). In practical terms, [Group1] had approximately [X]% [more/fewer] [outcome events] than [Group2]."

---

## Group Comparison (IRR — 3+ groups)

A1: "[Outcome] differed significantly across [grouping variable] levels (LR χ²([df]) = [val], *p* [val]). Relative to [reference group], [group2] showed an IRR of [val] (95% CI [[L], [U]]) and [group3] an IRR of [val] (95% CI [[L], [U]])."

A2: "A [Poisson/negative binomial] regression with [grouping variable] as a factor revealed a significant overall group effect (LR χ²([df]) = [val], *p* [val]). The highest rate was observed in [group] (IRR = [val] vs reference), while [group] had the lowest."

A3: "Significant variation in [outcome] counts was observed across [grouping variable], LR χ²([df]) = [val], *p* [val]. Kruskal-Wallis nonparametric test confirmed this pattern (*H* = [val], *p* [val]). Pairwise IRRs indicated [details]."

---

## Overdispersion & Model Selection

O1: "The deviance/df ratio for the Poisson model was [val], indicating [substantial overdispersion / approximate equidispersion]. A likelihood ratio test comparing Poisson and negative binomial models was [significant/non-significant] (LR χ²(1) = [val], *p* [val]), [supporting / not supporting] the use of the negative binomial."

O2: "Comparison of the Poisson and negative binomial models via likelihood ratio test revealed [significant] improvement in fit (LR χ²(1) = [val], *p* [val]). The estimated dispersion parameter was θ = [val], confirming overdispersion."

O3: "Model selection was guided by distributional fit. The Poisson model showed a deviance/df ratio of [val]. The negative binomial [provided a significantly better fit / did not improve fit] (LR χ²(1) = [val], *p* [val]; AIC: Poisson = [val], NB = [val])."

---

## Zero-Inflation

Z1: "Excess zeros were present ([val]% observed vs [val]% Poisson expected). The Vuong test comparing the zero-inflated Poisson to the standard Poisson was significant (Vuong = [val], *p* [val]), indicating a superior fit for the zero-inflated model."

Z2: "The proportion of zeros ([val]%) exceeded the Poisson prediction ([val]%), suggesting a two-component data-generating process. The zero-inflated [Poisson/negative binomial] model improved fit over the standard model (Vuong = [val], *p* [val]; AIC: standard = [val], ZI = [val])."

Z3: "Zero-inflation analysis indicated that [val]% of observations were zeros, substantially above the [val]% expected under Poisson. The [ZIP/ZINB] model captured this pattern, with the logistic component identifying [predictor(s)] as significant predictors of structural zeros."

Z4: "A two-process framework was warranted given the excess zeros. The Vuong test favored the zero-inflated specification (Vuong = [val], *p* [val]). In the zero-inflation component, [predictor] was associated with [increased/decreased] probability of a structural zero (OR = [val], *p* [val])."

---

## Hurdle Model

H1: "The hurdle model separated the zero/non-zero decision from the positive count process. In the logistic component, [predictor] significantly predicted the occurrence of any [outcome] (OR = [val], *p* [val]). Among non-zero observations, [predictor] was associated with [higher/lower] counts (IRR = [val], *p* [val])."

H2: "A hurdle specification treated the zero counts as a separate process. The probability of observing at least one [outcome] was significantly associated with [predictor] (OR = [val], 95% CI [[L], [U]]). Conditional on non-zero counts, the truncated [Poisson/NB] component identified [finding]."

---

## Subgroup Analysis

S1: "Subgroup analysis examined whether the [predictor]–[outcome] rate ratio differed by [subgroup]. The IRR was [val] (95% CI [[L], [U]]) within [sub1] and [val] (95% CI [[L], [U]]) within [sub2]. The interaction test was [not] significant (LR χ²([df]) = [val], *p* = [val])."

S2: "To explore potential heterogeneity, the [predictor] effect on [outcome] counts was examined separately within each level of [subgroup]. Rate ratios [varied/were similar] across subgroups (Figure [X]). The formal interaction test [did/did not] reach significance (LR χ²([df]) = [val], *p* = [val])."

S3: "Stratified analysis by [subgroup] revealed [consistent/divergent] rate ratios between [predictor] and [outcome]. Within [sub1] (*n* = [val]), IRR = [val]; within [sub2] (*n* = [val]), IRR = [val]. The [predictor] × [subgroup] interaction was [not] statistically significant (*p* = [val])."

---

## Tree-Based (Exploratory)

E1: "Random forest analysis identified [var1] and [var2] as the most important predictors of [outcome] counts (Figure [X]). In-sample *R*² = [val]; however, given *N* = [val], these results should be interpreted as exploratory."

E2: "Tree-based models were fit as an exploratory complement to the count regression. Variable importance rankings from the random forest were [consistent with / partially divergent from] the count model IRRs, with [var1] ranked first."

E3: "As an exploratory analysis, ensemble tree methods (random forest, LightGBM) were applied to the count outcome. [Var1] emerged as the dominant predictor across all tree-based approaches. These findings corroborate the parametric count model results but cannot be interpreted as validated predictions given the sample size."

---

## Model Comparison Synthesis

C1: "Across all analytic approaches — [Poisson/NB] regression, [ZIP/ZINB if applicable], and tree-based methods — [key finding]. The count regression models provide the most interpretable results via IRRs, while tree-based analyses confirm the variable importance hierarchy."

C2: "The convergence of parametric count models and machine learning methods strengthens confidence in [finding]. The distributional analysis additionally revealed [overdispersion/zero-inflation insight], which informed model selection."

C3: "Taken together, [finding] was robust across [Poisson/NB], [zero-inflated models if applicable], and tree-based methods. The [best-fitting count model] is recommended for manuscript reporting, supplemented by [specific insight] from the exploratory tree analysis."

C4: "Multiple analytic lenses converged on [key variable] as the strongest predictor of [outcome] counts. Poisson regression provided the baseline, negative binomial relaxed the equidispersion assumption, [and zero-inflated models addressed excess zeros]. Tree-based methods confirmed this ranking without distributional assumptions."
