## Methods

### Statistical Analysis

Multivariate distribution assumptions were assessed prior to hypothesis testing.
Mardia's test evaluated multivariate skewness and kurtosis, supplemented by the
Henze-Zirkler test for multivariate normality. Box's M test examined homogeneity
of covariance matrices across species groups, using a conservative alpha of .001
given the test's sensitivity to departures from normality.

A one-way multivariate analysis of variance (MANOVA) tested whether the four
morphological measurements (sepal length, sepal width, petal length, petal width)
differed across three iris species (setosa, versicolor, virginica). All four
multivariate test statistics were computed: Pillai's Trace, Wilks' Lambda,
Hotelling-Lawley Trace, and Roy's Largest Root. The primary statistic was selected
based on diagnostic results.

Follow-up univariate ANOVAs examined each dependent variable individually, with
Bonferroni-corrected alpha (0.0125) controlling familywise error across
4 comparisons. Pairwise group comparisons used Welch's t-test with Cohen's d
as the effect size measure.

Linear discriminant analysis (LDA) identified the linear combinations of variables
that best separated the three species. Classification accuracy was evaluated using
both resubstitution and leave-one-out cross-validation. Structure coefficients
(correlations between original variables and discriminant functions) quantified
each variable's contribution to group separation.

Profile analysis tested three hypotheses: parallelism (whether group profiles
have the same shape across variables), equal levels (whether groups differ in
their overall mean across variables), and flatness (whether the profile is uniform
across variables). These results should be interpreted with caution given that
the four morphological measurements, while sharing the same unit (cm), differ
substantially in range and meaning.

Canonical correlation analysis (CCA) examined the multivariate association between
species membership (dummy-coded) and the set of morphological variables, reporting
canonical correlations with Wilks' lambda significance tests per dimension.

Principal component analysis (PCA) with standardized variables reduced the
dimensionality of the four morphological measurements. Component retention followed
the Kaiser criterion (eigenvalue >= 1). Component loadings >= |.40| were flagged
for interpretation.

Multivariate multiple regression tested the association between species membership
and each morphological variable simultaneously, with Pillai's Trace for the overall
multivariate effect and individual R-squared per dependent variable.

Random forest (500 trees) and LightGBM (500 iterations, max_depth = 3,
learning_rate = 0.1, num_leaves = 15, min_child_samples = 15)
provided exploratory, nonlinear importance estimates. These tree-based models
served as analytic lenses for pattern detection rather than prediction engines.
Cross-DV importance comparison identified which predictors matter for which
outcome variables.

All analyses were conducted using Python 3.9 with NumPy, SciPy,
pandas, scikit-learn, statsmodels, LightGBM, and matplotlib/seaborn.
