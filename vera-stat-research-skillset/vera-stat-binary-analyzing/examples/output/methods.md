## Methods

### Statistical Analysis

Class balance of the outcome variable (survival) was assessed prior to analysis.
The proportion of the minority class was evaluated against a 10% threshold to
determine whether standard inferential methods were appropriate or whether
rare-event corrections would be needed.

Association between categorical predictors and survival was tested using
Pearson's chi-square test of independence. When any expected cell count fell
below 5, Fisher's exact test was used as the primary test. Effect sizes were
quantified using Cramer's V for overall association and odds ratios (OR) with
95% confidence intervals for pairwise comparisons.

To examine whether the sex-survival association was consistent across passenger
classes, stratified odds ratios were computed for each class level. The
Breslow-Day test assessed homogeneity of odds ratios across strata, and the
Mantel-Haenszel common odds ratio provided a pooled estimate adjusting for class.

A logistic regression model was fitted with survival as the binary outcome and
sex, passenger class, and age group as predictors. Odds ratios with 95%
confidence intervals were computed by exponentiating the regression coefficients.
Model specification used dummy coding with Crew as the reference category for
class.

Model adequacy was evaluated using the Hosmer-Lemeshow goodness-of-fit test with
10 groups. Discrimination was assessed via the area under the receiver operating
characteristic curve (AUC) with 95% bootstrap confidence intervals (1,000
replicates). McFadden's and Nagelkerke's pseudo-R-squared values were reported.
Classification performance was evaluated at the optimal probability threshold
identified by Youden's index.

Three tree-based classifiers were fitted as exploratory analytic lenses: a
classification and regression tree (CART; max depth = 4), a random forest (500
trees), and a LightGBM gradient boosting model (500 iterations, max depth = 3,
learning rate = 0.1, 15 leaves). These models were used to examine variable
importance patterns and nonlinear relationships, not as competing alternatives
to logistic regression.

All analyses were conducted in Python 3 using pandas, NumPy, SciPy, statsmodels,
scikit-learn, and LightGBM. Statistical significance was set at alpha = .05.
All confidence intervals are at the 95% level.
