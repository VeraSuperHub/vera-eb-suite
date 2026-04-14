## Results

### Class Balance

Of 2201 individuals in the dataset, 711 survived (32.3%)
and 1490 did not survive (67.7%). The minority
class (survivors) comprised 32.3% of observations, exceeding the
10% threshold for adequate class balance. Standard inferential methods were
therefore applied without rare-event corrections.

### Association Tests

Sex was significantly associated with survival, chi-sq(1) = 456.87,
p < .001,
Cramer's V = 0.456.
Passenger class was also significantly associated with survival. Age group
(child vs. adult) showed a significant but smaller association.

### Subgroup Analysis

Stratified analysis revealed that the sex-survival odds ratio varied across
passenger classes. The Breslow-Day test indicated heterogeneous ORs
across strata (chi-sq(3) = 60.23, p < .001). The
Mantel-Haenszel common OR was 0.09 (95% CI [0.07, 0.12]),
indicating that males had substantially higher odds of not surviving compared to
females after adjusting for passenger class.

### Logistic Regression

Sex (Female) emerged as the strongest predictor in the logistic model
(OR = 11.25,
95% CI [8.54, 14.81],
p < .001). The model accounted
for a McFadden pseudo-R-squared of 0.202 and Nagelkerke
pseudo-R-squared of 0.314. The Hosmer-Lemeshow test
indicated potential lack of fit
(chi-sq(3) = 16.73, p < .001). In-sample AUC was
0.76 (95% CI [0.74, 0.78]).

### Variable Importance Across Methods

All three modeling approaches converged on Sex (Female) as the most important
predictor (rank consensus = 1). Table 1 presents the unified importance scores
rescaled to 0-100 for each method. This convergence across parametric (logistic
regression) and nonparametric (random forest, LightGBM) approaches strengthens
confidence in the centrality of sex as a determinant of survival.

See Table 1 (importance_table.csv), Figure 5 (plot_05_roc.png), Figure 6
(plot_06_or_forest.png), and Figure 7 (plot_07_importance.png).
