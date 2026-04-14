## Methods

### Search Strategy and Study Selection

The search strategy and study selection process followed PRISMA 2020 guidelines
(Page et al., 2021). Details of the systematic search are reported in the PRISMA
flow diagram; the present section focuses on the statistical analysis approach.

### Effect Size Calculation

Standardized mean differences were computed as Hedges' g to quantify the
magnitude of treatment effects on depression outcomes across studies. For each
study, the pooled standard deviation was used as the denominator, with the
small-sample correction factor J applied to yield unbiased estimates (Hedges &
Vevea, 1998). Negative values indicate lower depression scores in the treatment
group relative to control.

### Pooled Estimation

A random-effects model with restricted maximum likelihood (REML) estimation
served as the primary analytic approach, acknowledging that the included studies
likely sample from a distribution of true effects rather than sharing a single
common effect. The DerSimonian-Laird moment-based estimator (DerSimonian &
Laird, 1986) was computed for comparison given its prevalence in published
meta-analyses. A fixed-effects (inverse-variance) model was also fitted to
assess sensitivity of the pooled estimate to the modeling assumption.

### Heterogeneity Assessment

Between-study heterogeneity was evaluated using Cochran's Q statistic, the
I-squared index (Higgins & Thompson, 2002), tau-squared, and the H-squared
ratio. Thresholds of I-squared < 25%, 25-75%, and > 75% were used as benchmarks
for low, moderate, and high heterogeneity, respectively. A 95% prediction
interval was computed to characterize the expected range of effects in future
study settings.

### Publication Bias

Potential publication bias was assessed through visual inspection of a funnel
plot, Egger's regression test for funnel plot asymmetry (Egger et al., 1997),
and Begg's rank correlation test (Begg & Mazumdar, 1994). The trim-and-fill
method (Duval & Tweedie, 2000) was applied to estimate the number and impact of
potentially missing studies, and Rosenthal's fail-safe N was calculated.

### Sensitivity Analysis

Robustness of the pooled estimate was examined through leave-one-out analysis,
in which each study was removed in turn and the pooled effect re-estimated.
Influence diagnostics including Cook's distance and DFBETAS were computed to
identify studies exerting disproportionate influence on the overall result.
Studies with Cook's D exceeding 4/k were flagged. Cumulative meta-analysis,
with studies ordered by publication year, assessed temporal stability of the
pooled estimate.

### Moderator Analysis

Subgroup analyses tested whether the pooled effect differed across levels of
categorical moderators (intervention type, study quality) using the Q-between
statistic. Mixed-effects meta-regression examined mean participant age as a
continuous moderator, with the proportion of heterogeneity explained (R-squared
analog) reported for each predictor.

### Additional Models

To assess robustness to analytic assumptions, the Knapp-Hartung adjustment
(Knapp & Hartung, 2003; IntHout et al., 2014) was applied to provide
better-calibrated confidence intervals based on the t-distribution rather than
the normal approximation. An approximate Bayesian meta-analysis with a weakly
informative half-Cauchy(0, 0.5) prior on tau was conducted to provide a
complementary perspective on uncertainty. A three-level model was considered
but deemed inapplicable as each study contributed a single effect size.

### Software

All analyses were conducted in Python 3 using NumPy, SciPy, statsmodels, and
matplotlib. Effect sizes, pooled estimates, and heterogeneity statistics were
computed using custom implementations following established formulas
(Viechtbauer, 2010).
