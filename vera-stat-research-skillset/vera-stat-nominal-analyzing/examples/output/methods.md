## Methods

### Statistical Analysis

The nominal outcome example used the iris dataset with three unordered species categories and four continuous floral measurements as predictors. Predictors were standardized before multinomial logistic regression so that relative risk ratios and coefficient magnitudes were comparable across features.

Multinomial logistic regression was fitted with setosa as the reference category. Relative risk ratios with 95% confidence intervals were obtained by exponentiating the model coefficients. Linear discriminant analysis (LDA) was used as a complementary projection-based method, with Wilks' lambda and discriminant loadings summarizing class separation.

As exploratory classification lenses, a classification tree, random forest, and LightGBM multiclass model were fit using the same predictor set. In-sample confusion matrices, overall accuracy, and per-class precision and recall were used to summarize classification performance. Variable importance from multinomial coefficients, LDA loadings, random forest permutation importance, and LightGBM gain were each rescaled to a common 0-100 scale for cross-method comparison.

Analyses were conducted in Python using statsmodels, scikit-learn, LightGBM, pandas, NumPy, SciPy, and matplotlib. Statistical significance was evaluated at alpha = .05, and all confidence intervals are at the 95% level.
