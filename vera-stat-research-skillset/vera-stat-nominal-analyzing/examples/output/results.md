## Results

### Class Distribution

The analysis included 150 flowers, with 50 setosa, 50 versicolor, and 50 virginica observations.

### Multinomial Logistic Regression

Multinomial logistic regression yielded McFadden pseudo-R-squared = 0.964. The strongest standardized coefficient was for Petal_Length in the virginica vs setosa contrast (RRR = 4228938782503395131392.00, 95% CI [0.00, inf], p = 1.000).

### Linear Discriminant Analysis

LDA produced 2 discriminant functions, with LD1 accounting for 99.1% of between-class variance. Wilks' lambda was 0.0234, with approximate F(8, 288) = 199.15, p < .001. This indicates strong multivariate separation among species.

### Classification Performance

The highest in-sample accuracy was achieved by Random Forest (100.0%). Across models, petal measurements dominated the classification boundary, while sepal measurements contributed more modestly.

### Cross-Method Synthesis

The unified importance table ranked Petal_Length as the most influential predictor across multinomial logistic regression, LDA, random forest, and LightGBM. Agreement across these parametric, projection-based, and tree-based approaches strengthens confidence that the main species differences are concentrated in that measurement axis.
