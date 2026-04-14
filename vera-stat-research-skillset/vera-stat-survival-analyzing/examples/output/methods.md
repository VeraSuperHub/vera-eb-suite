## Methods

### Statistical Analysis

Complete-case data from the NCCTG lung cancer dataset were analyzed after excluding observations with missing values on the prespecified covariates. Survival time was measured in days, and the event indicator represented death versus right censoring.

Kaplan-Meier estimators were used to summarize overall survival and survival stratified by sex. Group differences in survival curves were evaluated with the log-rank test. Median survival times and landmark survival probabilities were reported descriptively.

Predictor screening used univariate Cox proportional hazards models for sex, age, ECOG performance status, Karnofsky scores, meal calories, and weight loss. A multivariable Cox proportional hazards model then estimated adjusted hazard ratios (HRs) with 95% confidence intervals. The proportional hazards assumption was assessed with Schoenfeld residual tests.

Accelerated failure time (AFT) models with Weibull, log-normal, and log-logistic distributions were fitted as complementary lenses that provide time-ratio interpretations and relax the proportional hazards assumption. Distributional fit within the AFT family was compared using Akaike's Information Criterion (AIC).

As an exploratory nonparametric complement, a random survival forest with 500 trees was fitted and permutation importance was used to summarize variable importance. Cox absolute log-hazard ratios and random survival forest permutation scores were rescaled to a common 0-100 scale for cross-method comparison.

Analyses were conducted in Python using lifelines, scikit-survival, pandas, NumPy, and matplotlib. Statistical significance was evaluated at alpha = .05, and all confidence intervals are at the 95% level.
