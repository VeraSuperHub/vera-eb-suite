# Sentence Bank — Meta-Analysis Results

## Purpose

Provide varied phrasings for each type of meta-analytic result. The skill
selects from these contextually — never repeating patterns within a single
document. This is the core output quality variation mechanism for prose output.

## Rules

- Pick ONE variant per result instance
- Never repeat the same variant within a single results.md
- Adapt to actual data context (k studies, effect sizes, heterogeneity)
- These are structural templates — the actual text must feel natural and
  specific to the study, not templated

---

## Overall Effect Size

E1: "Across [k] studies (total N = [N]), the pooled effect size was [stat] = [val] (95% CI [[lo], [hi]], p [= / <] [pval]), indicating a [small/medium/large] [direction] effect."

E2: "The [random/fixed]-effects meta-analysis yielded a summary [stat] of [val] (95% CI [[lo], [hi]]; p [= / <] [pval]; k = [k] studies), suggesting [interpretation]."

E3: "A [significant/nonsignificant] overall effect was observed ([stat] = [val], 95% CI [[lo], [hi]], p [= / <] [pval]) based on [k] independent samples comprising [N] participants."

E4: "Meta-analytic synthesis of [k] effect sizes produced a pooled estimate of [stat] = [val] (95% CI [[lo], [hi]]), which [was/was not] statistically significant (p [= / <] [pval])."

---

## Heterogeneity

H1: "Substantial heterogeneity was observed (Q([df]) = [val], p [= / <] [pval]; I² = [val]%, τ² = [val]), suggesting that [XX]% of the total variability reflects true between-study differences."

H2: "The Q statistic indicated [significant/nonsignificant] heterogeneity (Q([df]) = [val], p [= / <] [pval]). The I² index was [val]% ([low/moderate/high]), with τ² = [val]."

H3: "Between-study variance was [low/moderate/substantial] (τ² = [val]; I² = [val]%, 95% CI [[lo]%, [hi]%]), indicating that study-level differences accounted for [XX]% of total variation beyond sampling error."

H4: "Heterogeneity analysis revealed [level] inconsistency across studies (I² = [val]%; Q([df]) = [val], p [= / <] [pval]). The prediction interval ranged from [lo] to [hi], illustrating the expected effect in a new study setting."

---

## Publication Bias

B1: "Visual inspection of the funnel plot [revealed/did not reveal] asymmetry. Egger's regression test [was/was not] statistically significant (intercept = [val], p [= / <] [pval])."

B2: "Begg's rank correlation test yielded τ = [val] (p [= / <] [pval]), [suggesting/not suggesting] publication bias. The trim-and-fill method imputed [k] missing studies, adjusting the pooled estimate to [val] (95% CI [[lo], [hi]])."

B3: "The funnel plot appeared [symmetric/asymmetric]. Egger's test (t = [val], p [= / <] [pval]) and Begg's test (z = [val], p [= / <] [pval]) [provided converging evidence of/did not indicate] publication bias."

B4: "Rosenthal's fail-safe N was [val], indicating that [val] null studies would be needed to nullify the observed effect. The trim-and-fill analysis [imputed [k] studies / did not impute additional studies]."

---

## Subgroup / Moderator Analysis

M1: "The mixed-effects model indicated that [moderator] significantly moderated the overall effect (Q_M([df]) = [val], p [= / <] [pval]). The pooled [stat] was [val1] (95% CI [[lo1], [hi1]]) for [level1] versus [val2] (95% CI [[lo2], [hi2]]) for [level2]."

M2: "Subgroup analysis by [moderator] revealed [significant/nonsignificant] between-group differences (Q_between([df]) = [val], p [= / <] [pval]). Within [level1] (k = [k1]), the effect was [val1] (95% CI [[lo1], [hi1]]); within [level2] (k = [k2]), the effect was [val2] (95% CI [[lo2], [hi2]])."

M3: "Meta-regression with [moderator] as a continuous predictor yielded a slope of [val] (SE = [se], p [= / <] [pval]), explaining [R²]% of the between-study heterogeneity."

M4: "The omnibus test for moderation was [significant/nonsignificant] (Q_M([df]) = [val], p [= / <] [pval]). Residual heterogeneity remained [significant/nonsignificant] (Q_E([df]) = [val], p [= / <] [pval]; I²_residual = [val]%)."

---

## Forest Plot Description

P1: "Figure [X] presents the forest plot of individual study effects with 95% CIs and the pooled estimate (diamond). Studies are ordered by [effect size / year / weight]."

P2: "The forest plot (Figure [X]) displays point estimates and 95% CIs for each of the [k] included studies, along with the [random/fixed]-effects summary estimate."

P3: "Individual study effects ranged from [min] to [max], with the summary diamond centered at [val] (Figure [X]). Study weights ranged from [min_w]% to [max_w]%."

---

## Sensitivity Analysis

S1: "Leave-one-out analysis demonstrated that no single study disproportionately influenced the pooled estimate, which ranged from [min] to [max] upon sequential omission."

S2: "Sensitivity analysis confirmed the robustness of the overall effect. Excluding each study individually, the pooled [stat] varied between [min] (95% CI [[lo], [hi]]) and [max] (95% CI [[lo], [hi]])."

S3: "Influence diagnostics identified [study] as potentially influential (Cook's distance = [val]). Excluding this study [changed/did not change] the pooled estimate substantively ([stat] = [val_without] vs. [val_with])."
