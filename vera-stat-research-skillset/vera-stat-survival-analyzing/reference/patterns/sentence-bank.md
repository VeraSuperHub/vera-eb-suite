# Sentence Bank — Survival Outcome Results

## Purpose

Provide varied phrasings for each type of statistical result. The skill
selects from these contextually — never repeating patterns within a single
document. This is the core output quality variation mechanism for prose output.

## Rules

- Pick ONE variant per result instance
- Never repeat the same variant within a single results.md
- Adapt to actual data context (variable names, direction, HR magnitude)
- These are structural templates — the actual text must feel natural and
  specific to the study, not templated

---

## Follow-Up and Censoring Summary

F1: "Among [N] participants, [X] ([XX]%) experienced [event] during a median follow-up of [val] [units] (IQR: [Q1]-[Q3]). The remaining [Y] ([YY]%) were censored."

F2: "The median follow-up time was [val] [units] (range: [min]-[max]). A total of [X] events were observed, yielding a censoring rate of [YY]%."

F3: "Over the observation period (median: [val] [units]; IQR: [Q1]-[Q3]), [event] occurred in [X] of [N] participants ([XX]%), while [Y] ([YY]%) were censored prior to event occurrence."

F4: "Follow-up ranged from [min] to [max] [units] (median: [val]). Of [N] individuals, [X] experienced [event] and [Y] were right-censored at last contact."

---

## Kaplan-Meier and Log-Rank

K1: "Kaplan-Meier analysis revealed a significant difference in survival between [Group1] and [Group2] (log-rank chi-sq([df]) = [val], *p* [val]). Median survival was [val] [units] (95% CI [[L], [U]]) for [Group1] and [val] [units] (95% CI [[L], [U]]) for [Group2]."

K2: "The survival curves for [Group1] and [Group2] diverged significantly (log-rank *p* [val]). [Group1] had a median survival of [val] [units] compared to [val] [units] for [Group2], suggesting a [val]-[unit] difference in median time to [event]."

K3: "Survival differed significantly by [grouping variable] (log-rank chi-sq([df]) = [val], *p* [val]). The [X]-year survival rate was [val]% (95% CI [[L]%, [U]%]) in [Group1] versus [val]% (95% CI [[L]%, [U]%]) in [Group2]."

K4: "Log-rank testing indicated [significant/no significant] differences in survival across [grouping variable] levels (chi-sq([df]) = [val], *p* [val]). Median survival time for [Group1] was [val] [units] (95% CI [[L], [U]]) and for [Group2] was [val] [units] (95% CI [[L], [U]])."

---

## Hazard Ratio (Univariate Cox)

H1: "[Group1] had [val] times the hazard of [event] compared to [Group2] (HR = [val], 95% CI [[L], [U]], *p* [val]). The concordance index was [val], indicating [moderate/good] discriminative ability."

H2: "Univariate Cox regression indicated a [significant/non-significant] association between [predictor] and [event] (HR = [val], 95% CI [[L], [U]], *p* [val])."

H3: "Each unit increase in [predictor] was associated with a [val]% [increase/decrease] in the hazard of [event] (HR = [val], 95% CI [[L], [U]])."

H4: "The unadjusted hazard ratio for [predictor] was [val] (95% CI [[L], [U]], *p* [val]), suggesting that [predictor] [is/is not] significantly associated with time to [event]."

---

## Median Survival

M1: "Median survival was [val] [units] (95% CI [[L], [U]]) in [Group1] and [val] [units] (95% CI [[L], [U]]) in [Group2]."

M2: "The median time to [event] was [val] [units] for [Group1] (95% CI [[L], [U]]), compared with [val] [units] for [Group2] (95% CI [[L], [U]])."

M3: "[Group1] had a median survival of [val] [units] (95% CI [[L], [U]]); for [Group2], the median was [val] [units] (95% CI [[L], [U]]), corresponding to a [val]-[unit] difference."

M4: "Median survival was not reached in [Group1] (lower 95% CI bound: [val] [units]), while [Group2] had a median of [val] [units] (95% CI [[L], [U]])."

---

## Cox Proportional Hazards (Multivariable)

C1: "In the multivariable Cox model, [predictor] remained independently associated with [event] (HR = [val], 95% CI [[L], [U]], *p* [val]) after adjusting for [covariate list]. The model achieved a concordance index of [val]."

C2: "The Cox PH model was globally significant (likelihood ratio chi-sq([df]) = [val], *p* < .001). After adjustment, [predictor1] (HR = [val], 95% CI [[L], [U]]) and [predictor2] (HR = [val], 95% CI [[L], [U]]) were significant independent predictors of [event]."

C3: "After controlling for [covariates], [predictor] was associated with a [val]-fold [increase/decrease] in hazard (HR = [val], 95% CI [[L], [U]], *p* [val]). The overall model concordance was [val] (in-sample)."

C4: "Multivariable Cox regression identified [predictor] as the strongest predictor of [event] (HR = [val], *p* [val]). The global likelihood ratio test confirmed overall model significance (chi-sq([df]) = [val], *p* < .001)."

---

## Proportional Hazards Assumption

P1: "The global test of the proportional hazards assumption was [not] significant (chi-sq = [val], *p* = [val]), [supporting/suggesting violation of] the PH assumption. [Predictor] showed [evidence of/no evidence of] time-varying effects (rho = [val], *p* = [val])."

P2: "Schoenfeld residual analysis indicated that the PH assumption [held/was violated] globally (*p* = [val]). At the individual predictor level, [predictor] showed [significant/no significant] deviation from proportionality (*p* = [val])."

P3: "Assessment of the proportional hazards assumption via Schoenfeld residuals revealed [no evidence of/evidence of] non-proportional hazards (global *p* = [val]). [If violated: Given the PH violation for [predictor], AFT models provide a complementary perspective.]"

P4: "The proportionality of hazards was evaluated for each covariate and globally. [Predictor] exhibited a time-dependent effect (Schoenfeld *p* = [val]), indicating that its association with survival [strengthened/weakened] over time."

---

## AFT / Time Ratio

A1: "Under the Weibull AFT model, [predictor] was associated with a [val]-fold [increase/decrease] in expected survival time (TR = [val], 95% CI [[L], [U]], *p* [val])."

A2: "The AFT model with [distribution] distribution indicated that [group1] survived [val] times longer than [group2] (TR = [val], 95% CI [[L], [U]]). This distributional choice was supported by AIC comparison ([distribution] AIC = [val])."

A3: "Time ratios from the Weibull AFT provided an intuitive complement to hazard ratios. [Predictor] was associated with [val]% [longer/shorter] survival (TR = [val], 95% CI [[L], [U]]), consistent with the Cox finding of [increased/decreased] hazard."

A4: "Among the parametric AFT models, the [distribution] distribution provided the best fit (AIC = [val]). Under this model, each unit increase in [predictor] was associated with a [val]-fold change in expected survival time (TR = [val], 95% CI [[L], [U]])."

---

## Subgroup Analysis

S1: "Subgroup analysis examined whether the [predictor]-survival association differed by [subgroup]. The HR was [val] (95% CI [[L], [U]]) within [sub1] and [val] (95% CI [[L], [U]]) within [sub2]. The interaction test was [not] significant (LR chi-sq = [val], *p* = [val])."

S2: "To explore potential heterogeneity, the effect of [predictor] on survival was examined separately within each level of [subgroup]. Hazard ratios [varied/were similar] across subgroups (Figure [X]). The formal interaction test [did/did not] reach significance (*p* = [val])."

S3: "Stratified Cox analysis by [subgroup] revealed [consistent/divergent] associations between [predictor] and survival. Within [sub1] (*n* = [val]), [predictor] carried a hazard ratio of [val]; within [sub2] (*n* = [val]), the corresponding HR was [val]. The [predictor] x [subgroup] interaction was [not] statistically significant (*p* = [val])."

---

## Tree-Based (Exploratory)

E1: "Random survival forest analysis identified [var1] and [var2] as the most important predictors of survival (Figure [X]). The RSF concordance index was [val] (in-sample); given *N* = [val], these results should be interpreted as exploratory."

E2: "Tree-based models were fit as an exploratory complement. Variable importance rankings from the RSF were [consistent with / partially divergent from] the Cox results, with [var1] ranked first. The in-sample concordance ([val]) likely reflects optimistic estimation."

E3: "As an exploratory analysis, ensemble survival methods (RSF, gradient boosting) were applied. [Var1] emerged as the dominant predictor across all tree-based approaches. These findings corroborate the Cox PH results but cannot be interpreted as validated predictions given the sample size."

E4: "Partial dependence plots from the RSF revealed [a nonlinear/a linear] relationship between [predictor] and predicted survival probability, [consistent with/suggesting additional complexity beyond] what the Cox model captured."

---

## Concordance

N1: "The concordance index for the Cox model was [val] (in-sample), indicating [poor/moderate/good/excellent] discriminative ability."

N2: "Discriminative accuracy, as measured by Harrell's concordance index, was [val] for the Cox model, [val] for the RSF, and [val] for gradient boosting (all in-sample estimates)."

N3: "The Cox model achieved a C-statistic of [val], suggesting that it correctly ordered survival times for [val]% of comparable pairs."

---

## Time-Varying Cox

TV1: "Because [predictor] changed during follow-up, it was modeled as a time-varying covariate using the counting-process formulation. Each unit increase in the current value of [predictor] was associated with a [val]-fold [increase/decrease] in hazard (HR = [val], 95% CI [[L], [U]], *p* [val])."

TV2: "To account for changes in [predictor] over the observation period, a Cox model with time-varying covariates was fit using start-stop intervals. The time-varying [predictor] was [significantly/not significantly] associated with [event] (HR = [val], 95% CI [[L], [U]], *p* [val])."

TV3: "Data were restructured into [N_intervals] person-intervals (mean: [val] per subject) to accommodate time-varying [predictor]. After adjusting for baseline covariates, the current value of [predictor] carried a hazard ratio of [val] (95% CI [[L], [U]], *p* [val])."

TV4: "Using the extended Cox model with time-dependent [predictor], the updated covariate value was associated with [event] (HR = [val], 95% CI [[L], [U]]). This time-varying specification is preferred because [predictor] values changed meaningfully during follow-up for [val]% of subjects."

---

## Recurring (Recurrent) Events

RE1: "A total of [N_events] events were observed among [N_subjects] subjects (mean: [val] events per subject; range: [min]-[max]). Using the Andersen-Gill extension of the Cox model with robust standard errors, [predictor] was associated with the rate of recurrent [event] (HR = [val], 95% CI [[L], [U]], robust *p* [val])."

RE2: "Recurrent [event] was analyzed using the Prentice-Williams-Peterson model stratified by event number ([gap/total] time scale). For the first event, the hazard ratio for [predictor] was [val] (95% CI [[L], [U]]); for subsequent events, HRs [remained stable/varied], suggesting [consistency/heterogeneity] in the predictor effect across recurrences."

RE3: "To account for within-subject correlation in recurrent [event] data, a shared frailty model was fit with a [gamma/Gaussian] random effect. The frailty variance was [val] (LR test *p* = [val]), indicating [substantial/minimal] unobserved heterogeneity. After accounting for this heterogeneity, [predictor] remained associated with recurrent [event] (HR = [val], 95% CI [[L], [U]])."

RE4: "Given that subjects experienced [event] multiple times (median: [val]; IQR: [Q1]-[Q3]), an Andersen-Gill model was used to estimate the overall effect of [predictor] on the recurrence rate. The robust hazard ratio was [val] (95% CI [[L], [U]], *p* [val]), with sandwich variance estimation to account for within-subject dependence."

RE5: "The frailty model identified [significant/no significant] subject-level heterogeneity in event rates (theta = [val], *p* = [val]). Adjusted for this random effect, [predictor] was associated with a [val]-fold [increase/decrease] in the rate of [event] (HR = [val], 95% CI [[L], [U]])."

---

## Model Comparison Synthesis

X1: "Across all analytic approaches, [key finding]. The Cox PH model provides the most interpretable adjusted hazard ratios, while RSF confirms the variable importance hierarchy."

X2: "The convergence of semi-parametric (Cox), parametric (AFT), and machine learning (RSF) methods strengthens confidence in [finding]. The AFT model additionally provided intuitive time-ratio interpretations."

X3: "Taken together, [finding] was robust across Cox PH, AFT, and tree-based methods. The Cox model is recommended for primary manuscript reporting, supplemented by [specific insight] from the AFT analysis."

X4: "Variable importance rankings from the Cox model (|standardized coefficients|) and RSF (permutation importance) showed [strong/moderate] agreement, with [var1] and [var2] consistently identified as the strongest predictors of survival."
