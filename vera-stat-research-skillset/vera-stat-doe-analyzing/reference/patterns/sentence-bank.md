# Sentence Bank -- DOE Results

## Purpose

Provide varied phrasings for each type of statistical result. The skill
selects from these contextually -- never repeating patterns within a single
document. This is the core output quality variation mechanism for prose output.

## Rules

- Pick ONE variant per result instance
- Never repeat the same variant within a single results.md
- Adapt to actual data context (factor names, response, direction, magnitude)
- These are structural templates -- the actual text must feel natural and
  specific to the experiment, not templated

---

## ANOVA Main Effect

M1: "[Factor] had a significant main effect on [response], *F*([df1], [df2]) = [val], *p* [val], partial eta^2 = [val]. [Highest level] produced the highest mean [response] (*M* = [val], *SD* = [val])."

M2: "A significant effect of [factor] on [response] was observed, *F*([df1], [df2]) = [val], *p* [val], accounting for [eta^2*100]% of variance (partial eta^2 = [val]). Post-hoc comparisons revealed [which levels differ]."

M3: "The main effect of [factor] was statistically significant, *F*([df1], [df2]) = [val], *p* [val], partial eta^2 = [val], indicating a [small/medium/large] effect. Tukey HSD showed that [pairwise result]."

M4: "[Response] varied significantly across levels of [factor], *F*([df1], [df2]) = [val], *p* [val]. The effect was [magnitude] (partial eta^2 = [val]), with [level] yielding the [highest/lowest] mean."

---

## ANOVA Interaction

I1: "A significant [Factor_A] x [Factor_B] interaction was detected, *F*([df1], [df2]) = [val], *p* [val], partial eta^2 = [val]. Simple effects analysis revealed that [Factor_A] was significant at [B = level1] but not at [B = level2]."

I2: "The interaction between [Factor_A] and [Factor_B] reached significance, *F*([df1], [df2]) = [val], *p* [val], partial eta^2 = [val], indicating that the effect of [Factor_A] on [response] depended on [Factor_B] level."

I3: "The [Factor_A] x [Factor_B] interaction was significant, *F*([df1], [df2]) = [val], *p* [val]. As shown in Figure [X], the effect of [Factor_A] was [stronger/reversed/absent] when [Factor_B] was at [level]."

I4: "There was a significant two-way interaction between [Factor_A] and [Factor_B], *F*([df1], [df2]) = [val], *p* [val], partial eta^2 = [val]. Decomposition through simple effects showed [specific pattern]."

---

## Non-Significant Effect

N1: "The main effect of [factor] was not statistically significant at alpha = .05, *F*([df1], [df2]) = [val], *p* = [val], partial eta^2 = [val]."

N2: "[Factor] did not significantly influence [response], *F*([df1], [df2]) = [val], *p* = [val], with a negligible effect size (partial eta^2 = [val])."

N3: "No significant effect of [factor] on [response] was detected, *F*([df1], [df2]) = [val], *p* = [val]. The partial eta^2 of [val] indicates a [negligible/small] practical effect."

---

## Simple Effects

SE1: "At [B = level1], [Factor_A] significantly affected [response], *F*([df1], [df2]) = [val], *p* [val], partial eta^2 = [val]. At [B = level2], this effect was not significant, *F*([df1], [df2]) = [val], *p* = [val]."

SE2: "Simple effects analysis showed that the impact of [Factor_A] was conditional on [Factor_B]. Specifically, when [Factor_B] = [level1], [Factor_A] had a [large/significant] effect (*F* = [val], *p* [val]), but this diminished at [Factor_B] = [level2] (*F* = [val], *p* = [val])."

SE3: "Decomposing the interaction, [Factor_A] produced significant differences in [response] at [B = level1] (*F* = [val], *p* [val]) with a [magnitude] effect (partial eta^2 = [val]). The effect was [not significant/attenuated] at [B = level2]."

---

## Contrast Analysis

CT1: "The planned contrast comparing [control] to the average of all treatment conditions was significant, *t*([df]) = [val], *p* [val], with a mean difference of [val] (95% CI [[L], [U]])."

CT2: "A priori contrasts revealed a significant [linear/quadratic] trend across levels of [factor], *t*([df]) = [val], *p* [val], suggesting a [dose-response/diminishing returns] relationship."

CT3: "The contrast between [group1] and [group2] yielded a difference of [val] units (SE = [val], 95% CI [[L], [U]]), *p* [val], after [Bonferroni/Scheffe] adjustment."

---

## RSM Results

RSM1: "The second-order response surface model explained [R^2*100]% of variance in [response] (adjusted *R*^2 = [val]). Canonical analysis identified a [maximum/minimum/saddle point] at [factor1] = [val], [factor2] = [val], with predicted [response] = [val]."

RSM2: "Response surface analysis revealed a [stationary point type] in [response]. The quadratic model was significant, *F*([df1], [df2]) = [val], *p* [val], *R*^2 = [val]. The stationary point ([coordinates]) corresponded to a predicted [response] of [val]."

RSM3: "The contour plot (Figure [X]) indicated that optimal [response] occurred near [factor1] = [val] and [factor2] = [val]. Canonical analysis confirmed a [maximum/minimum/saddle], with eigenvalues of [vals] along the principal axes."

RSM4: "Fitting a second-order model after the first-order lack-of-fit test was significant (*F* = [val], *p* = [val]), the response surface revealed [curvature description]. The predicted optimum ([val]) was [within/outside] the experimental region."

---

## Effect Screening (Half-Normal / Pareto)

HN1: "The half-normal plot identified [N] active effects out of [total]: [list]. The remaining effects fell along the reference line, consistent with normal noise."

HN2: "Effect screening via the [half-normal/Pareto] plot (Figure [X]) revealed that [Factor_A] and the [A x B] interaction were the dominant effects, substantially exceeding the noise line."

HN3: "Of the [total] estimable effects, [N] were identified as active by [Daniel's/Lenth's] method: [list], accounting for the majority of response variation."

---

## Tree-Based (Exploratory)

E1: "Random forest analysis identified [Factor_A] and [Factor_B] as the most important factors (Figure [X]). The importance ranking was [consistent with / partially divergent from] the ANOVA partial eta-squared ranking."

E2: "As an exploratory complement, tree-based methods (random forest, LightGBM) corroborated [Factor_A] as the dominant influence on [response]. Given *N* = [val], these results are interpreted as confirmatory rather than predictive."

E3: "Variable importance from ensemble tree methods confirmed the ANOVA findings: [Factor_A] dominated both RF (importance = [val]) and LightGBM (importance = [val]) rankings, consistent with its large partial eta^2 in the factorial model."

---

## Model Comparison Synthesis

C1: "Across all analytic approaches -- factorial ANOVA, response surface analysis, and tree-based methods -- [key finding]. The convergence across parametric and nonparametric methods strengthens confidence in this result."

C2: "The unified importance ranking showed [Factor_A] as the dominant factor across ANOVA (partial eta^2 = [val]), RF, and LightGBM. RSM additionally revealed that the response surface has a [type] at [coordinates]."

C3: "Taken together, the experimental evidence consistently identifies [factor(s)] as the primary driver(s) of [response]. The ANOVA provides the inferential basis, RSM maps the optimization landscape, and tree-based methods confirm the importance hierarchy without parametric assumptions."

C4: "The factorial analysis, response surface model, and machine learning methods converged on [finding]. [Factor_A] accounted for the largest share of variance, and RSM indicated that [response] can be [maximized/minimized] by setting [factor settings]."
