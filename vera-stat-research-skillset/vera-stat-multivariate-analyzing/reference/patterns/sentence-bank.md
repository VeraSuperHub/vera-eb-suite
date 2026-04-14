# Sentence Bank — Multivariate Outcome Results

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

## Multivariate Distribution Check

MD1: "Multivariate normality was assessed using Mardia's tests for skewness (*b*₁,p = [val], *p* = [val]) and kurtosis (*b*₂,p = [val], *p* = [val]). [Outcome]. Box's *M* test [indicated/did not indicate] significant heterogeneity of covariance matrices (*F* = [val], *p* = [val])."

MD2: "Prior to multivariate analysis, distributional assumptions were evaluated. The Henze-Zirkler test [supported/did not support] multivariate normality (HZ = [val], *p* = [val]). Equality of covariance matrices was [confirmed/not confirmed] by Box's *M* test (*M* = [val], *F* = [val], *p* = [val])."

MD3: "Mardia's test indicated that multivariate skewness ([val], *p* = [val]) and kurtosis ([val], *p* = [val]) were [within/outside] acceptable limits. Box's *M* = [val] (*p* = [val]) [suggested/did not suggest] equal covariance matrices across groups, supporting the use of [Pillai's Trace/Wilks' Lambda] as the primary test statistic."

MD4: "Multivariate distributional assumptions were evaluated prior to hypothesis testing. Mardia's skewness (*p* = [val]) and kurtosis (*p* = [val]) tests [were/were not] significant, and the Henze-Zirkler test (HZ = [val], *p* = [val]) [corroborated/qualified] this assessment."

---

## MANOVA (3+ groups)

M1: "A one-way MANOVA revealed a significant multivariate effect of [group variable] on the combined DVs, Pillai's *V* = [val], *F*([df1], [df2]) = [val], *p* [val]. Wilks' *Lambda* = [val], Hotelling-Lawley *T* = [val], and Roy's largest root *theta* = [val] were [all significant/consistent]."

M2: "The multivariate effect of [group variable] was statistically significant across all four test statistics: Pillai's *V* = [val] (*p* [val]), Wilks' *Lambda* = [val] (*p* [val]), Hotelling-Lawley *T* = [val] (*p* [val]), and Roy's largest root = [val] (*p* [val])."

M3: "[Group variable] significantly predicted the linear combination of [DV list], Pillai's *V* = [val], *F*([df1], [df2]) = [val], *p* [val]. Given [assumption status], [Pillai's Trace/Wilks' Lambda] was selected as the primary test statistic."

M4: "The omnibus MANOVA indicated that [group variable] had a significant multivariate effect, Wilks' *Lambda* = [val], *F*([df1], [df2]) = [val], *p* [val]. All four multivariate test statistics converged on this conclusion."

---

## Hotelling's T-squared (2 groups)

H1: "Hotelling's *T*² test indicated a significant multivariate difference between [Group1] and [Group2], *T*² = [val], *F*([df1], [df2]) = [val], *p* [val]. The two groups differed in their joint profile across the [k] outcome variables."

H2: "A two-sample Hotelling's *T*² was conducted to compare the multivariate means of [Group1] and [Group2]. The test was significant, *T*² = [val], *F*([df1], [df2]) = [val], *p* [val], indicating that the groups' centroids differed."

H3: "The multivariate mean vector of [Group1] differed significantly from that of [Group2], Hotelling's *T*² = [val], *F*([df1], [df2]) = [val], *p* [val]. Follow-up univariate tests identified which individual outcomes drove this difference."

---

## Follow-Up Univariate ANOVAs

U1: "Follow-up univariate ANOVAs (Bonferroni-adjusted *alpha* = [val]) indicated significant group differences for [DV1], *F*([df1], [df2]) = [val], *p* [val], partial *eta*² = [val], and [DV2], *F*([df1], [df2]) = [val], *p* [val], partial *eta*² = [val]."

U2: "Examining each DV separately, [DV1] showed the largest group effect (partial *eta*² = [val], *p* [val]), followed by [DV2] (partial *eta*² = [val], *p* [val]). [DV3] did not differ significantly across groups at the Bonferroni-adjusted threshold (*p* = [val])."

U3: "To identify which outcomes contributed to the multivariate effect, univariate ANOVAs were conducted for each DV using a Bonferroni-corrected *alpha* of [val]. Significant effects emerged for [DVs], with partial *eta*² ranging from [min] to [max]."

U4: "Univariate decomposition of the MANOVA revealed that [k of K] outcome variables showed significant group differences after Bonferroni correction. The strongest univariate effect was observed for [DV] (*F* = [val], partial *eta*² = [val])."

---

## Discriminant Analysis

DA1: "[N_functions] discriminant function(s) emerged, accounting for [val]% and [val]% of the between-group variance, respectively. The first function (canonical *r* = [val]) primarily reflected [DV loading interpretation]. Classification accuracy was [val]% overall."

DA2: "Linear discriminant analysis yielded [N_functions] significant discriminant function(s). The first function (Wilks' *Lambda* = [val], *chi*²([df]) = [val], *p* [val]) was dominated by [DVs with highest structure coefficients]. Cross-validated classification accuracy was [val]%."

DA3: "Discriminant function analysis separated the [k] groups along [N_functions] dimension(s). [DV1] (structure coefficient = [val]) and [DV2] ([val]) loaded most heavily on the first function. The model correctly classified [val]% of cases ([val]% by leave-one-out cross-validation)."

DA4: "Group separation was examined through discriminant analysis. The first discriminant function, accounting for [val]% of between-group variance, was characterized by high loadings from [DVs]. Overall classification accuracy reached [val]%, with per-group rates ranging from [min]% to [max]%."

---

## Canonical Correlation Analysis

CC1: "Canonical correlation analysis revealed [N_sig] significant canonical variate pair(s). The first canonical correlation was [val] (Wilks' *Lambda* = [val], *F*([df1], [df2]) = [val], *p* [val]), indicating [interpretation of shared variance]."

CC2: "The first canonical correlation (*R*c = [val]) accounted for [val]% of the shared variance between the two variable sets. Redundancy analysis indicated that [val]% of the variance in the DV set was accounted for by the predictor canonical variate."

CC3: "[N_sig] of [N_total] canonical dimensions were statistically significant. The primary dimension (canonical *r* = [val]) linked [predictor-side loadings] with [DV-side loadings], suggesting [substantive interpretation]."

---

## Profile Analysis

PA1: "The parallelism test indicated that group profiles [were/were not] parallel, *F*([df1], [df2]) = [val], *p* [val]. The equal levels test [was/was not] significant (*F* = [val], *p* [val]), and the flatness test [was/was not] significant (*F* = [val], *p* [val])."

PA2: "Profile analysis revealed [non-parallel/parallel] profiles across groups (*F* = [val], *p* [val]). Groups [did/did not] differ in their overall level across DVs (*F* = [val], *p* [val]). The profile [was/was not] flat (*F* = [val], *p* [val])."

PA3: "The three profile analysis tests were conducted sequentially. Parallelism was [rejected/not rejected] (*F* = [val], *p* [val]), indicating that [interpretation]. The equal levels test (*F* = [val], *p* [val]) [supported/did not support] group differences in overall DV magnitude."

---

## PCA

P1: "Principal component analysis of the [k] outcome variables yielded [n] components with eigenvalues exceeding 1.0, accounting for [val]% of the total variance. The first component ([val]% variance) was characterized by high loadings from [DVs]."

P2: "PCA revealed that [n] principal component(s) explained [val]% of the variance in the outcome variables. [DV1] ([loading]) and [DV2] ([loading]) loaded most heavily on PC1, while [DV3] ([loading]) defined PC2."

P3: "Dimension reduction via PCA indicated that the [k] outcome variables could be represented by [n] component(s). The scree plot and Kaiser criterion converged on this solution. Component loadings suggested [interpretation of dimensions]."

---

## Tree-Based (Exploratory)

TE1: "Random forest importance rankings were [consistent with / partially divergent from] the MANOVA and discriminant results. [DV/predictor] emerged as the most important feature across all DVs. Given *N* = [val], these results are exploratory."

TE2: "Cross-DV importance analysis from random forest and LightGBM models revealed that [predictor] was consistently important for predicting [DVs], while [predictor] was primarily important for [specific DV]. These patterns corroborate the multivariate parametric results."

TE3: "As an exploratory complement, tree-based models (RF, LightGBM) were fit per DV. The importance heatmap (Figure [X]) shows [pattern]. The high in-sample *R*² values ([range]) likely reflect overfitting and should not be interpreted as predictive accuracy."

---

## Model Comparison Synthesis

MC1: "Across MANOVA, discriminant analysis, PCA, and tree-based methods, [DV1] and [DV2] consistently emerged as the primary sources of group differentiation. [N] methods converged on [key finding]."

MC2: "The convergence of multivariate parametric and exploratory approaches strengthens confidence in [finding]. Discriminant analysis additionally revealed [classification insight], while PCA [dimension reduction insight]."

MC3: "Taken together, the multivariate analyses paint a consistent picture: [finding]. MANOVA established the significance, discriminant analysis clarified the dimensions of separation, PCA revealed latent structure, and tree-based methods confirmed the variable importance hierarchy."

MC4: "The cross-method synthesis revealed strong agreement regarding [key variables]. All methods identified [DV] as the primary contributor to group differences. The dimensionality estimates converged — [PCA components, discriminant functions, CCA dimensions] all suggested [N] underlying dimension(s)."
