## Results

### Multivariate Distribution Assessment

Mardia's test and Henze-Zirkler test assessed multivariate normality of the
four morphological variables. Box's M test evaluated homogeneity of covariance
matrices across species groups (alpha = .001).

### MANOVA

The one-way MANOVA revealed a statistically significant multivariate effect of
species on the combined morphological variables. All four test statistics converged:

| Test Statistic     | Value  | F     | p       |
|--------------------|--------|-------|---------|
Follow-up univariate ANOVAs with Bonferroni correction (alpha = 0.0125) revealed:

- **sepal_length**: F(2, 147) = 119.26, p < .001, partial eta-squared = 0.619
- **sepal_width**: F(2, 147) = 49.16, p < .001, partial eta-squared = 0.401
- **petal_length**: F(2, 147) = 1180.16, p < .001, partial eta-squared = 0.941
- **petal_width**: F(2, 147) = 960.01, p < .001, partial eta-squared = 0.929

### Discriminant Function Analysis

Linear discriminant analysis identified 2 discriminant function(s).
Function 1 accounted for 99.1% of between-group variance (canonical r = 0.985). Function 2 accounted for 0.9% of between-group variance (canonical r = 0.471). 
Classification accuracy was 98.0% (resubstitution) and
98.0% (leave-one-out cross-validation). Structure coefficients
indicated that petal_length loaded most heavily on the first discriminant
function.

### Profile Analysis

Profile analysis tested parallelism, equal levels, and flatness. Note that
iris measurements, while sharing the same unit (cm), differ in range, so
these results should be interpreted cautiously.

### Canonical Correlation Analysis

CCA identified 2 canonical dimension(s). The first canonical correlation
was Rc = 0.985, indicating a strong multivariate association
between species membership and morphological characteristics.

### Principal Component Analysis

PCA retained 1 component(s) based on the Kaiser criterion,
accounting for 73.0% of total variance.
Component loadings indicated that petal measurements loaded strongly on
the first principal component, while sepal width showed a distinct loading
pattern on the second component.

### Tree-Based Exploratory Analysis

Random forest and LightGBM models served as exploratory tools for nonlinear
pattern detection. Cross-DV importance comparison confirmed that petal
measurements were consistently the most important features across all
outcome variable models, converging with parametric findings.

### Cross-Method Synthesis

Variable-level convergence analysis (Table 1) normalized importance measures
across MANOVA (partial eta-squared), discriminant analysis (structure
coefficients), PCA (component loadings), and random forest (feature importance)
to a common 0-100 scale. petal_length ranked first across all methods
(rank consensus = 1), followed by petal_width.

The convergence of parametric, classification-based, dimension-reduction, and
nonlinear methods provides robust evidence that petal morphology primarily
differentiates iris species, with sepal measurements providing supplementary
discriminatory information.
