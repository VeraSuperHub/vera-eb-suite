# Sentence Bank — Ordinal Outcome Results

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

## Distribution Check (Ordinal)

D1: "The distribution of [outcome] was [right-skewed/left-skewed/approximately symmetric], with [level] being the most frequent category ([X]%). Cumulative proportions indicated that [X]% of participants fell at or below [level]."

D2: "Across the sample, [outcome] levels were distributed as follows: [level1] ([X]%), [level2] ([X]%), [level3] ([X]%). No ordinal level contained fewer than [threshold] observations."

D3: "[Outcome] showed a [concentration/spread] toward the [lower/upper] end of the scale. The modal category was [level] (*n* = [val], [X]%), while [level] was least frequent (*n* = [val], [X]%)."

D4: "Examination of the ordinal distribution revealed that [X]% of responses fell in the [level] category. The cumulative distribution showed that [X]% of participants were at or below [level], indicating [interpretation]."

---

## Mann-Whitney U (2 groups)

M1: "[Group1] (Mdn = [val], IQR = [val]) had significantly [higher/lower] [outcome] than [Group2] (Mdn = [val], IQR = [val]), *U* = [val], *p* [val], rank-biserial *r* = [val]."

M2: "A Mann-Whitney *U* test indicated a significant difference in [outcome] between [Group1] and [Group2], *U* = [val], *p* [val]. The rank-biserial correlation (*r* = [val]) indicated a [small/medium/large] effect, with [Group1] tending toward [higher/lower] ordinal levels."

M3: "The distribution of [outcome] differed significantly between [Group1] (Mdn = [val]) and [Group2] (Mdn = [val]), *U* = [val], *p* [val]. The magnitude of this difference was [small/medium/large] (rank-biserial *r* = [val])."

M4: "[Outcome] ranks were significantly [higher/lower] in [Group1] compared to [Group2], *U* = [val], *p* [val], with a [magnitude] effect (rank-biserial *r* = [val]). In [Group1], [X]% were classified as [highest level] versus [X]% in [Group2]."

---

## Kruskal-Wallis (3+ groups)

K1: "[Outcome] differed significantly across [grouping variable] levels, *H*([df]) = [val], *p* [val]. Post-hoc Dunn's tests with Bonferroni correction revealed [which pairs differed]."

K2: "A Kruskal-Wallis test indicated significant between-group differences in [outcome], *H*([df]) = [val], *p* [val]. Pairwise comparisons using Dunn's test showed that [pair1] differed significantly (*p* = [val], Cliff's δ = [val]), while [pair2] did not (*p* = [val])."

K3: "Significant variation in [outcome] was observed across [grouping variable], *H*([df]) = [val], *p* [val]. [Group] had the highest median ([val]), while [group] had the lowest ([val]). Pairwise Cliff's delta values ranged from [min] to [max]."

K4: "The ordinal distribution of [outcome] varied significantly by [grouping variable], *H*([df]) = [val], *p* [val]. Dunn's post-hoc tests identified [number] significant pairwise differences after Bonferroni adjustment."

---

## Jonckheere-Terpstra Trend Test

J1: "The Jonckheere-Terpstra test confirmed a significant [increasing/decreasing] trend in [outcome] across ordered levels of [grouping variable], *JT* = [val], *p* [val]."

J2: "A monotonic trend in [outcome] was assessed using the Jonckheere-Terpstra test. The result was [significant/non-significant], *JT* = [val], *p* [val], [supporting/not supporting] a [direction] trend across [grouping variable] levels."

J3: "Ordered group analysis via the Jonckheere-Terpstra test indicated that [outcome] [increased/decreased] systematically across [grouping variable] levels (*JT* = [val], *p* [val])."

---

## Spearman Correlation

SP1: "[Predictor] was [positively/negatively] correlated with [outcome], ρ = [val], *p* [val], 95% CI [[L], [U]], indicating a [weak/moderate/strong] monotonic association."

SP2: "Spearman rank correlation between [predictor] and [outcome] was [significant/non-significant], ρ = [val], *p* [val]. The [direction] association suggests that [interpretation]."

SP3: "A [weak/moderate/strong] [positive/negative] monotonic relationship was observed between [predictor] and [outcome] (ρ = [val], 95% CI [[L], [U]], *p* [val])."

---

## Goodman-Kruskal Gamma

G1: "The association between [predictor] and [outcome] was assessed using Goodman-Kruskal gamma. The association was [significant/non-significant], γ = [val], SE = [val], *p* [val], indicating [no/a weak/a moderate/a strong] monotonic relationship."

G2: "Goodman-Kruskal gamma for the ordinal association between [predictor] and [outcome] was γ = [val] (*p* [val]), suggesting [interpretation of concordance/discordance]."

G3: "The ordinal-by-ordinal association between [predictor] and [outcome] was [strong/moderate/weak/negligible] (γ = [val], SE = [val], *p* [val]). More concordant than discordant pairs indicated [direction of association]."

---

## Subgroup Analysis

S1: "Subgroup analysis examined whether the [predictor]–[outcome] association differed by [subgroup]. The effect was [significant/not significant] within [sub1] (Cliff's δ = [val]) and [sub2] (Cliff's δ = [val]). The interaction test was [not] significant (LR χ² = [val], *p* = [val])."

S2: "To explore potential heterogeneity, the [predictor] effect on [outcome] was examined separately within each level of [subgroup]. Effect sizes [varied/were similar] across subgroups (Figure [X]). The formal interaction test [did/did not] reach significance (LR χ² = [val], *p* = [val])."

S3: "Stratified analysis by [subgroup] revealed [consistent/divergent] associations between [predictor] and [outcome]. Within [sub1] (*n* = [val]), the rank-biserial *r* was [val]; within [sub2] (*n* = [val]), *r* was [val]. The [predictor] × [subgroup] interaction in the ordinal logistic model was [not] statistically significant (*p* = [val])."

---

## Proportional Odds Regression

P1: "The proportional odds model was significant, LR χ²([df]) = [val], *p* < .001. [Top predictor] had the largest effect: cumulative OR = [val], 95% CI [[L], [U]], indicating that [interpretation of odds of higher category]."

P2: "An ordinal logistic regression predicting [outcome] from [predictor list] was statistically significant, LR χ²([df]) = [val], *p* < .001, AIC = [val]. After adjusting for covariates, [predictor] was significantly associated with higher [outcome] levels (cumulative OR = [val], 95% CI [[L], [U]])."

P3: "The cumulative logit model indicated that [predictor] significantly predicted [outcome] category membership. For each one-unit increase in [predictor], the cumulative odds of being in a higher category were multiplied by [OR] (95% CI [[L], [U]])."

P4: "[Outcome] was regressed on [predictor list] using proportional odds logistic regression. The overall model was significant (LR χ² = [val], *p* < .001). [Key finding about specific predictor with cumulative OR, CI, p]."

---

## Brant Test / Proportional Odds Assumption

B1: "The proportional odds assumption was assessed using the Brant test. The overall test was [not] significant, χ²([df]) = [val], *p* = [val], [supporting/questioning] the assumption of parallel slopes across cut-points."

B2: "The Brant test for the proportional odds assumption yielded χ²([df]) = [val], *p* = [val]. [All predictors satisfied / [predictor(s)] violated] the assumption. [Action taken: model retained / partial proportional odds fitted / multinomial sensitivity analysis conducted]."

B3: "Assessment of the proportional odds assumption via the Brant test indicated that [the assumption held / the assumption was violated for [predictors]]. The overall test statistic was χ²([df]) = [val], *p* = [val]."

---

## Tree-Based (Exploratory)

E1: "Random forest classification identified [var1] and [var2] as the most important predictors of [outcome] category (Figure [X]). In-sample accuracy was [val]%; however, given *N* = [val], these results should be interpreted as exploratory."

E2: "Tree-based models were fit as an exploratory complement. Variable importance rankings from the random forest were [consistent with / partially divergent from] the proportional odds results, with [var1] ranked first. The modest sample size precludes predictive validation."

E3: "As an exploratory analysis, random forest classification was applied to the ordinal outcome. [Var1] emerged as the dominant predictor across tree-based approaches. These findings corroborate the ordinal regression results but cannot be interpreted as validated predictions given the sample size."

---

## Multinomial Logistic Regression (Path A)

MN1: "The multinomial logistic model with [reference level] as the reference category revealed class-specific associations. Relative to [reference], [predictor] was significantly associated with [level k] membership (OR = [val], 95% CI [[L], [U]], *p* [val])."

MN2: "Treating the ordinal outcome as nominal, multinomial logistic regression identified [predictor] as a significant differentiator of [level k] versus [reference level] (OR = [val], 95% CI [[L], [U]]). Associations [varied/were consistent] across class contrasts."

MN3: "Class-specific odds ratios from the multinomial model indicated that [predictor] primarily distinguished [level k] from [reference level] (OR = [val], *p* [val]), while its effect on [other level] was [weaker/non-significant] (OR = [val], *p* [val])."

MN4: "Without imposing ordinal structure, the multinomial logistic model showed that [predictor] had [heterogeneous/homogeneous] effects across outcome levels. The strongest contrast was [level] versus [reference] (OR = [val], 95% CI [[L], [U]])."

---

## Adjacent-Category Logit

AC1: "The adjacent-category logit model revealed that [predictor] most strongly influenced the transition from [level k] to [level k+1] (adjacent-category OR = [val], 95% CI [[L], [U]], *p* [val]), while the [other transition] was [weaker/non-significant]."

AC2: "Examining level-to-level transitions, [predictor] significantly predicted the odds of being in [level k+1] versus [level k] (adjacent-category OR = [val], *p* [val]). The effect was [consistent/variable] across adjacent transitions."

AC3: "Adjacent-category analysis identified the [level k] to [level k+1] transition as the critical jump associated with [predictor]. The adjacent-category OR of [val] (95% CI [[L], [U]]) indicates that [interpretation]."

---

## Continuation-Ratio Logit

CR1: "The continuation-ratio model indicated that among those who reached [level k], [predictor] significantly predicted advancement to [level k] (continuation-ratio OR = [val], 95% CI [[L], [U]], *p* [val])."

CR2: "Stage-specific analysis via the continuation-ratio model showed that [predictor] mattered most at the [level k] threshold: among participants at or beyond this level, each unit increase in [predictor] was associated with [val]-fold odds of advancing further."

CR3: "The continuation-ratio logit revealed a [stage-dependent/stage-consistent] effect of [predictor]. The odds of progressing beyond [level k], conditional on reaching it, were multiplied by [OR] per unit increase in [predictor] (*p* [val])."

---

## Stereotype Model

ST1: "The stereotype model relaxed the proportional odds assumption while preserving ordinal structure. Scaling parameters indicated that [predictor]'s effect was [strongest/weakest] at the [level] transition (phi = [val])."

ST2: "When proportional odds was relaxed via the stereotype model, [predictor] retained its significance (coefficient = [val], *p* [val]). The scaling parameters (phi) confirmed that the effect was [not strictly proportional / approximately proportional] across ordinal levels."

ST3: "The stereotype model provided a middle ground between the strict proportional odds and fully unconstrained multinomial models. For [predictor], the scaling parameters suggested that the ordinal effect was [concentrated at specific levels / distributed across levels]."

---

## Dual-Path Comparison

DP1: "The dual-path analysis — treating the outcome as both unordered (Path A) and ordered (Path B) — [converged/diverged] on variable importance rankings. The Spearman rank correlation between paths was [val], indicating that [interpretation]."

DP2: "Comparing multi-class (Path A) and ordinal-specific (Path B) analyses, [predictor] emerged as the top-ranked variable in both paths. The consistency across paradigms strengthens confidence in this finding regardless of assumptions about level ordering."

DP3: "Path A (ignoring ordering) and Path B (respecting ordering) provided complementary insights. While both identified [predictor] as important, Path B additionally revealed [specific ordinal insight — cumulative OR, transition pattern, or proportional odds finding]."

DP4: "The convergence between multi-class and ordinal-specific approaches confirmed that [key finding]. Path B uniquely contributed the cumulative OR of [val] (proportional odds) and identified the [level k] to [level k+1] transition as the critical threshold (adjacent-category model)."

---

## Model Comparison Synthesis

C1: "Across both multi-class and ordinal-specific analytic paths, [key finding]. The proportional odds model provides cumulative ORs, the adjacent-category model pinpoints transition-specific effects, and tree-based analyses confirm the variable importance hierarchy nonparametrically."

C2: "The convergence of Path A (multi-class) and Path B (ordinal-specific) methods strengthens confidence in [finding]. The proportional odds model revealed a cumulative OR of [val], while the adjacent-category model showed that the effect concentrated at the [level] transition."

C3: "Taken together, [finding] was robust across multinomial logistic, proportional odds, adjacent-category, continuation-ratio, and tree-based/LightGBM methods. The dual-path framework confirmed that [predictor]'s importance does not depend on whether ordinal structure is assumed."

C4: "Both Path A and Path B converged on [variable] as the strongest predictor (rank correlation = [val]). The cumulative OR of [val] from the proportional odds model aligns with [variable]'s top ranking in both RF and LightGBM importance, reinforcing this conclusion across methodological perspectives."

C5: "The dual-path analysis revealed that [predictor] was the dominant variable regardless of whether ordering was imposed. Ordinal-specific models uniquely added that the effect was [proportional across thresholds / concentrated at the [level] transition / stage-dependent], an insight invisible to the multi-class path."

C6: "Where paths diverged, [variable] ranked higher under Path B, suggesting its effect operates through the ordinal structure itself. The stereotype model confirmed that this predictor's effect was [proportional / non-proportional], with scaling parameters indicating [interpretation]."
