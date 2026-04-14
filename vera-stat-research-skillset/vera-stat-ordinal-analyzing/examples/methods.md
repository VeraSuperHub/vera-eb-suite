## Methods

### Statistical Analysis

Frequency distributions and cumulative proportions were computed for the ordinal
outcome variable (arthritis improvement: None < Some < Marked). A sparse level
check confirmed that all ordinal categories contained at least five observations.

Group differences in improvement were assessed using the Wilcoxon rank-sum
(Mann-Whitney U) test, appropriate for comparing ordinal outcomes between two
independent groups. Rank-biserial correlation served as the effect size measure.
Spearman rank correlation quantified the monotonic association between age and
ordinal improvement.

Two complementary modeling paths were pursued. Path A (ignore ordering) treated
improvement as a nominal multi-class outcome and fit multinomial logistic
regression, CART (max depth = 4), random forest (500 trees), and LightGBM
(n_estimators = 500, max_depth = 3, learning_rate = 0.1, num_leaves = 15).
Path B (respect ordering) employed ordinal-specific models: proportional odds
(cumulative logit), adjacent-category logit, and continuation-ratio logit
models. The Brant test evaluated the proportional odds assumption. Variable
importance was extracted from each model family and normalized to a 0-100 scale
to construct a unified dual-path importance table.

Tree-based models were framed as exploratory pattern detection given the modest
sample size (N = 84). The stereotype model was noted as a limitation of the
Python implementation; the R VGAM package provides a full implementation.

All analyses were conducted in Python 3.x using statsmodels, scikit-learn,
LightGBM, and SciPy. Statistical significance was set at alpha = .05. Effect
sizes and 95% confidence intervals are reported throughout.
