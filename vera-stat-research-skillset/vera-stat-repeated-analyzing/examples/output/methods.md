## Methods

### Statistical Analysis

Chick weights were measured at 12 time points (days 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 21) across 50 chicks assigned to one of four diet conditions. Data were organized in long format with one row per measurement occasion, yielding 578 total observations. The between-subjects factor was Diet (4 levels), and the within-subjects factor was Time.

A mixed-design ANOVA was conducted with Time as the within-subjects factor and Diet as the between-subjects factor. Mauchly's test assessed the sphericity assumption for within-subjects effects. When sphericity was violated (p < .05), degrees of freedom were corrected using the Greenhouse-Geisser epsilon. Partial eta-squared quantified effect sizes for all ANOVA effects.

Pairwise comparisons examined group differences at each time point using independent-samples t-tests with Bonferroni correction for multiplicity. Simple effects tested the time effect separately within each diet group. Cohen's d quantified pairwise effect sizes.

A subgroup analysis examined whether the Time x Diet interaction varied by baseline weight (median split). Stratified mixed models were fit within each baseline weight subgroup, and heterogeneity was assessed using Cochran's Q.

Linear mixed models (LMMs) were fit using restricted maximum likelihood (REML) estimation. The random intercept model specified weight ~ Time * Diet + (1 | Chick), allowing between-subject differences in overall weight level. The random slope model added a random slope for Time, allowing individual growth rates to vary: weight ~ Time * Diet + (1 + Time | Chick). A likelihood ratio test compared the two specifications. Fixed-effect inference used the large-sample Wald z statistics reported by statsmodels MixedLM.

Generalized estimating equations (GEE) estimated population-averaged effects using the identity link function with exchangeable, first-order autoregressive (AR(1)), and independence working correlation structures. Robust (sandwich) standard errors ensured valid inference regardless of correlation misspecification.

Growth curve models extended the LMM framework with polynomial time terms. Quadratic (Time + Time^2) and cubic (Time + Time^2 + Time^3) growth models were fit with random intercepts and random slopes for Time, enabling curvilinear trajectory modeling. Model selection within the LMM family used AIC and BIC.

Subject-level features were engineered for exploratory tree-based analysis, including mean weight, individual OLS slope, within-subject variability, first and last observations, and maximum adjacent change. Random Forest (500 trees, permutation importance) and LightGBM (n_estimators=500, max_depth=3, learning_rate=0.1, num_leaves=15, min_child_samples=5) were fit on these features. Tree-based results are framed as exploratory given the modest sample size (N = 50).

Model comparison used an assumption comparison table detailing what each method assumes and what it relaxes, an AIC/BIC comparison within the LMM family, and a unified variable importance table rescaling importance measures from LMM (absolute Wald z statistics), Random Forest (permutation), and LightGBM (gain) to a common 0-100 scale. Models were treated as complementary analytic lenses rather than competitors.

Analyses were conducted in Python 3.9 using statsmodels (mixed models, GEE), scipy (hypothesis tests), scikit-learn (Random Forest, permutation importance), and LightGBM. Figures were generated with matplotlib at 300 DPI. The significance threshold was alpha = .05 for all tests. Multiple comparison corrections used the Bonferroni method unless otherwise noted.
