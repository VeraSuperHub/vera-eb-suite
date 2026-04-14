## Methods

Tooth length (`len`) was analyzed as a continuous outcome in the ToothGrowth dataset. Distributional properties were assessed using the Shapiro-Wilk test, skewness, kurtosis, a histogram with density overlay, and a Q-Q plot.

Welch's t-test compared orange juice (OJ) with ascorbic acid (VC) supplementation, with Cohen's d reported as an effect size. Mann-Whitney U served as a nonparametric confirmation. Dose groups were compared using one-way ANOVA with eta-squared, Tukey HSD, and Kruskal-Wallis follow-up.

Subgroup analyses fit dose-response regressions within each supplement group. A formal interaction test compared models with and without the dose-by-supplement term.

Primary modeling used OLS regression with dose, supplement type, and their interaction as predictors. Quantile regression at the 25th, 50th, and 75th percentiles evaluated distributional heterogeneity. CART, random forest (500 trees), and GBM were fit as exploratory models given the small sample size (N = 60).

