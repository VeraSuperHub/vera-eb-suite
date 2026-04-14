## Methods

### Experimental Design

The experiment employed a 2^3 full factorial design with three two-level factors---nitrogen (N), phosphorus (P), and potassium (K)---arranged in a randomized complete block design (RCBD) with six blocks. Each treatment combination was replicated across all blocks, yielding a total of 24 observations. The response variable was pea crop yield measured in pounds per plot.

### Statistical Analysis

A full factorial analysis of variance (ANOVA) was conducted with Type III sums of squares to evaluate the main effects of N, P, and K and their two- and three-way interactions. Type III SS were chosen because they provide unbiased estimates regardless of cell frequency balance (Langsrud, 2003). Block was included as a fixed factor to account for spatial heterogeneity but was not crossed with treatment factors. Partial eta-squared (partial eta^2) was reported as the effect size measure for each F-test, with benchmarks of .01 (small), .06 (medium), and .14 (large) following Cohen (1988).

Post-hoc pairwise comparisons for significant main effects were conducted using Tukey's honestly significant difference (HSD) procedure. For significant interaction effects, simple effects analyses were performed to assess the effect of one factor at each level of the other. Planned contrasts comparing each nutrient present versus absent were adjusted using the Bonferroni correction.

Effect magnitudes were estimated using the Daniel half-normal probability plot and Lenth's method for pseudo standard error estimation (Lenth, 1989). Active effects were identified as those exceeding Lenth's margin of error on the Pareto chart.

Residual diagnostics included Shapiro-Wilk tests for normality and Levene's test for homogeneity of variance. Residuals-versus-fitted, normal Q-Q, and scale-location plots were inspected visually.

To demonstrate response surface methodology (RSM), a synthetic central composite design (CCD) with two continuous factors was generated. First-order and second-order (quadratic) models were fitted, with lack-of-fit tests against pure error. Canonical analysis was performed to classify the stationary point and identify the nature of the response surface (Myers, Montgomery, & Anderson-Cook, 2016).

As an exploratory complement, random forest (500 trees) and LightGBM (500 iterations, max depth = 3, learning rate = 0.1) models were fitted to corroborate the ANOVA factor importance rankings without parametric assumptions. Given the small sample size (N = 24), tree-based results are interpreted as exploratory confirmations rather than predictive models.

All analyses were performed using Python 3.9 with statsmodels, scipy, scikit-learn, and LightGBM. Figures were produced with matplotlib at 300 DPI.
