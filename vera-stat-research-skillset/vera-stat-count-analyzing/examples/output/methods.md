## Methods

### Statistical Analysis

Count outcomes from the `warpbreaks` dataset were analyzed using a two-part workflow. First, raw break counts per loom were evaluated as count-number outcomes. Distributional diagnostics included the mean-variance relationship, observed versus Poisson-expected zeros, and the Cameron-Trivedi overdispersion test.

Primary group comparisons across tension levels used the Kruskal-Wallis test because the outcome is discrete and overdispersed. Count regression models then included Poisson and negative binomial generalized linear models, with zero-inflated and hurdle models evaluated when warranted by the observed zero structure. Model adequacy within the count-model family was summarized with deviance and Akaike's Information Criterion (AIC).

As exploratory complements, a regression tree, random forest, and LightGBM model were fit to the same predictors. Variable importance from the best-fitting count model, random forest permutation importance, and LightGBM gain were rescaled to a common 0-100 scale for cross-method comparison.

Second, a count-rate workflow demonstrated how offsets change interpretation when exposure varies. Synthetic loom-hours were introduced for illustration, and Poisson and negative binomial rate models were fit with offset = log(exposure). These models estimated incidence rate ratios rather than raw count ratios.

Analyses were conducted in Python using statsmodels, SciPy, scikit-learn, LightGBM, pandas, NumPy, and matplotlib. Statistical significance was evaluated at alpha = .05, and all confidence intervals are at the 95% level.
