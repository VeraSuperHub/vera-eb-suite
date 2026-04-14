# Sentence Bank — Repeated Measures Outcome Results

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

## Trajectory Description (Spaghetti Plot)

TR1: "Individual trajectories revealed [substantial/modest] variability in [outcome] over time (Figure [X]). While most [subjects] showed [increasing/decreasing/stable] trends, [group] exhibited [steeper/flatter] growth on average."

TR2: "Visual inspection of individual growth curves (Figure [X]) indicated that [outcome] [increased/decreased] over the [N]-[unit] observation period, with [considerable/limited] between-subject variability in both level and rate of change."

TR3: "Spaghetti plots of individual trajectories (Figure [X]) suggested [diverging/parallel/converging] patterns across [groups], with [group] showing the [steepest/most gradual] average trajectory."

TR4: "Figure [X] displays individual [outcome] trajectories overlaid with group means. The [group] group showed a [distinct/similar] pattern compared to other groups, with [description of trajectory shape]."

---

## ICC (Intraclass Correlation)

ICC1: "The intraclass correlation coefficient was [val] (95% CI [[L], [U]]), indicating that [pct]% of the total variance in [outcome] was attributable to between-subject differences. This substantial clustering justified the use of mixed models."

ICC2: "An unconditional means model yielded an ICC of [val], suggesting that [outcome] was [highly/moderately/minimally] clustered within individuals. Approximately [pct]% of the variance was between subjects."

ICC3: "Between-subject differences accounted for [pct]% of the variance in [outcome] (ICC = [val]). The [high/moderate] ICC confirmed the need for analytic methods that account for the nested data structure."

ICC4: "The null model estimated an ICC of [val], partitioning variance into [pct]% between-subject and [pct]% within-subject components. This level of clustering [strongly supports/supports] the use of multilevel modeling."

---

## Sphericity

SP1: "Mauchly's test indicated that the assumption of sphericity was [violated/met] (*W* = [val], *p* [val]). [Greenhouse-Geisser corrected degrees of freedom were used (epsilon = [val]).|Uncorrected degrees of freedom are reported.]"

SP2: "The sphericity assumption was assessed using Mauchly's test (*W* = [val], *p* [val]). [Given the violation, the Greenhouse-Geisser correction was applied (epsilon = [val]), adjusting degrees of freedom for within-subjects effects.|The assumption was tenable, and uncorrected values are reported.]"

SP3: "Mauchly's *W* = [val] (*p* [val]) [indicated a departure from sphericity. Accordingly, Greenhouse-Geisser corrected results are reported (epsilon = [val]).|was not significant, supporting the sphericity assumption.]"

SP4: "[Sphericity was violated (*W* = [val], *p* [val]); Huynh-Feldt epsilon ([val]) and Greenhouse-Geisser epsilon ([val]) corrections were applied.|Mauchly's test was non-significant (*W* = [val], *p* [val]), and sphericity was assumed.]"

---

## Repeated Measures ANOVA

RM1: "A [one-way repeated measures/mixed] ANOVA revealed a significant [main effect of time/group x time interaction], *F*([df1], [df2]) = [val], *p* [val], partial eta-squared = [val]. [Outcome] [increased/decreased] significantly over the [N] measurement occasions."

RM2: "The [within-subjects/interaction] effect was statistically significant, *F*([df1], [df2]) = [val], *p* [val], partial eta-squared = [val], indicating that [outcome] trajectories [differed across groups/changed over time]."

RM3: "[Outcome] showed a significant [time/group x time] effect, *F*([df1], [df2]) = [val], *p* [val]. The effect was [small/medium/large] (partial eta-squared = [val]), [with/without] evidence of differential change across [groups]."

---

## Mixed ANOVA Interaction

MI1: "The time x [group] interaction was significant, *F*([df1], [df2]) = [val], *p* [val], partial eta-squared = [val], indicating that [outcome] trajectories differed across [group] levels. [Group_name] showed the [steepest/most gradual] change over time."

MI2: "A significant interaction between time and [group] emerged, *F*([df1], [df2]) = [val], *p* [val], partial eta-squared = [val]. This indicates that the rate of change in [outcome] was not uniform across [groups]."

MI3: "The [group] x time interaction, *F*([df1], [df2]) = [val], *p* [val], partial eta-squared = [val], revealed that [groups] diverged in their [outcome] trajectories over the observation period."

MI4: "Trajectories of [outcome] differed significantly by [group], as evidenced by the time x [group] interaction, *F*([df1], [df2]) = [val], *p* [val]. [Group_name] gained [val] units more than [Group_name] over [duration] (partial eta-squared = [val])."

---

## Paired Comparisons

PC1: "[Outcome] [increased/decreased] significantly from [time1] (*M* = [val], *SD* = [val]) to [time2] (*M* = [val], *SD* = [val]), *t*([df]) = [val], *p* [val], Cohen's *d* = [val]."

PC2: "A paired *t*-test indicated a significant [increase/decrease] in [outcome] between [time1] and [time2], mean difference = [val] (95% CI [[L], [U]]), *t*([df]) = [val], *p* [val], *d* = [val]."

PC3: "The mean change in [outcome] from [time1] to [time2] was [val] units (95% CI [[L], [U]]), representing a [small/medium/large] effect (*d* = [val], *p* [val])."

PC4: "Between [time1] and [time2], [outcome] [rose/fell] by an average of [val] units (*t*([df]) = [val], *p* [val]). This change corresponded to a [magnitude] paired effect size (*d* = [val])."

---

## LMM Random Intercept

LRI1: "The random intercept model indicated significant fixed effects of time (*B* = [val], SE = [val], *t*([df]) = [val], *p* [val]) and [group] (*B* = [val], SE = [val], *t*([df]) = [val], *p* [val]). The random intercept variance was [val] (SD = [val]), confirming substantial between-subject variability in baseline [outcome]."

LRI2: "A linear mixed model with random intercepts revealed that [outcome] [increased/decreased] by [val] units per [time unit] (*B* = [val], 95% CI [[L], [U]]). Between-subject differences in intercepts (variance = [val]) accounted for a substantial portion of total variability (ICC = [val])."

LRI3: "Fixed effects from the random intercept model showed that both time (*B* = [val], *p* [val]) and [group] (*B* = [val], *p* [val]) significantly predicted [outcome]. The random intercept SD of [val] indicated [considerable/modest] individual differences in overall [outcome] levels."

LRI4: "In the random intercept LMM, the time x [group] interaction was [significant/not significant] (*B* = [val], SE = [val], *p* [val]), suggesting that [group] differences in [outcome] [did/did not] change over time when accounting for individual baseline differences."

---

## LMM Random Slope

LRS1: "Adding a random slope for time significantly improved model fit (LR chi-squared = [val], *p* [val]), indicating that individuals differed in their rate of [outcome] change. The random slope variance was [val] (SD = [val]), with a [correlation] between random intercepts and slopes (*r* = [val])."

LRS2: "The likelihood ratio test comparing random slope and random intercept models was significant (chi-squared([df]) = [val], *p* [val]), confirming substantial individual differences in trajectories. AIC [decreased/increased] from [val] to [val]."

LRS3: "Individual trajectories varied significantly (random slope SD = [val]), as confirmed by the LR test (chi-squared = [val], *p* [val]). The [negative/positive] correlation between intercepts and slopes (*r* = [val]) suggested that [subjects with higher/lower baseline outcome showed faster/slower change]."

LRS4: "The random slope model fit the data significantly better than the intercept-only model (delta AIC = [val]; LR *p* [val]). The estimated correlation between random intercepts and slopes was [val], indicating [interpretation]."

---

## Growth Curve

GC1: "[Outcome] followed a [linear/quadratic/nonlinear] trajectory over time. The linear time effect was [val] (*p* [val]) and the quadratic term was [val] (*p* [val]), indicating [accelerating/decelerating/inverted-U] change. [Group] moderated the [linear/quadratic] component (*B* = [val], *p* [val])."

GC2: "Growth curve modeling revealed a significant [quadratic] trend in [outcome] (Figure [X]). The positive linear slope (*B* = [val]) combined with the [negative/positive] quadratic term (*B* = [val]) indicated that growth [decelerated/accelerated] over time."

GC3: "Model-predicted trajectories (Figure [X]) showed that [group_name] exhibited [steeper/flatter] growth in [outcome] compared to [group_name]. The group x linear time interaction was [significant/not significant] (*B* = [val], *p* [val])."

GC4: "The growth curve model captured [linear and quadratic/piecewise] change in [outcome]. Groups differed in trajectory shape: [group_name] showed [description], while [group_name] showed [description] (Figure [X])."

---

## GEE

GEE1: "Population-averaged estimates from GEE (working correlation: [structure]) indicated that [outcome] [increased/decreased] by [val] units per [time unit] (robust SE = [val], *p* [val]). The time x [group] interaction coefficient was [val] (*p* [val])."

GEE2: "GEE with [exchangeable/AR(1)/unstructured] working correlation revealed a significant [group] effect on [outcome] trajectories (*B* = [val], robust SE = [val], 95% CI [[L], [U]]). These population-averaged estimates were [similar to/somewhat different from] the subject-specific LMM results."

GEE3: "Using generalized estimating equations with robust standard errors, the population-averaged effect of time on [outcome] was [val] (*p* [val]). The [exchangeable/AR(1)] correlation structure yielded an estimated working correlation of [val]."

GEE4: "The GEE model, using [structure] working correlation, confirmed the [LMM/ANOVA] findings: [group] significantly moderated [outcome] trajectories (*B* = [val], robust SE = [val], *p* [val]). Population-averaged and subject-specific estimates were [concordant/discordant], consistent with the [linear/nonlinear] modeling framework."

---

## Attrition / Missing Data

AT1: "Attrition was [minimal/moderate/substantial], with [pct]% of subjects completing all [N] waves. The missing data pattern was [monotone/intermittent]. Linear mixed models, which accommodate missing data under the MAR assumption, were used as the primary analytic approach."

AT2: "By the final time point, [pct]% of the original sample remained. [Outcome] at baseline did not differ significantly between completers and non-completers (*p* = [val]), supporting the plausibility of the MAR assumption."

AT3: "Sample retention was [val]% at [time point]. Given the [monotone/intermittent] missingness pattern, LMM was preferred over RM-ANOVA, as it uses all available data under MAR rather than requiring complete cases."

AT4: "[N] subjects ([pct]%) had incomplete data. Missing data were assumed to be missing at random (MAR), and LMM was used to leverage all available observations without listwise deletion."

---

## Tree-Based on Longitudinal Data

TE1: "As an exploratory complement, tree-based models were applied to subject-level summary features (individual mean, slope, and variability). Random forest identified [var1] and [var2] as the most important predictors of individual [outcome] trajectories (Figure [X])."

TE2: "Subject-level features — including individual growth rates, mean [outcome], and within-person variability — were derived and used as inputs for random forest and LightGBM models. Variable importance rankings were [consistent with/partially divergent from] the LMM fixed effects."

TE3: "Tree-based exploratory analysis on subject-level summaries revealed [var1] as the dominant predictor of individual trajectories. Given the sample size (*N* = [val] subjects), these results should be interpreted as pattern detection rather than validated prediction."

TE4: "Random forest and LightGBM were applied to engineered subject-level features to assess variable importance from a nonparametric perspective. [Var1] emerged as most important across both methods, corroborating the LMM finding of a significant [var1] effect on [outcome] trajectories."

---

## Model Comparison Synthesis

MC1: "Across all analytic approaches — RM-ANOVA, LMM, GEE, and tree-based models — [key finding] emerged as the central result. The LMM additionally revealed [individual difference insight], while GEE confirmed the finding at the population level."

MC2: "The convergence of traditional (RM-ANOVA), mixed model (LMM/GEE), and machine learning methods strengthens confidence in [finding]. LMM uniquely captured [random effects insight], and tree-based importance confirmed [variable ranking]."

MC3: "Taken together, [finding] was robust across repeated measures ANOVA, linear mixed models, GEE, and tree-based approaches. The primary analysis (LMM with random slopes) is recommended for manuscript reporting, as it handles [missing data/unbalanced design] and captures individual differences in trajectories."

MC4: "The time x [group] interaction was consistent across RM-ANOVA (partial eta-squared = [val]), LMM (B = [val]), and GEE (B = [val]). Tree-based models on subject-level features confirmed [group] as a key predictor of individual trajectory characteristics. This multi-method convergence supports [conclusion]."
