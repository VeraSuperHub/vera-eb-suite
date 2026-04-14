## Results

### Assumption Checks

Residual normality was assessed via the Shapiro-Wilk test, and variance homogeneity was evaluated using Levene's test. Visual inspection of the residuals-versus-fitted, Q-Q, and scale-location plots revealed no systematic departures from ANOVA assumptions (Figure 8).

### Factorial ANOVA

The full factorial ANOVA (Type III SS) with block as a covariate revealed the following effects on pea yield (Table 1):

- **block**: SS = 343.29, df = 5, F = 4.45, p = 0.016, partial eta^2 = 0.649
- **N**: SS = 194.05, df = 1, F = 12.57, p = 0.004, partial eta^2 = 0.512
- **N:K**: SS = 33.13, df = 1, F = 2.15, p = 0.169, partial eta^2 = 0.152
- **N:P**: SS = 21.28, df = 1, F = 1.38, p = 0.263, partial eta^2 = 0.103
- **K**: SS = 7.35, df = 1, F = 0.48, p = 0.503, partial eta^2 = 0.038
- **P:K**: SS = 0.48, df = 1, F = 0.03, p = 0.863, partial eta^2 = 0.003
- **P**: SS = 0.35, df = 1, F = 0.02, p = 0.883, partial eta^2 = 0.002

The effect magnitude ranking (Figure 3) shows the relative contribution of each factor and interaction to yield variation.

### Post-Hoc Comparisons

Tukey HSD comparisons and planned contrasts with Bonferroni adjustment indicated:

- Nitrogen (N present vs. absent): difference = 5.62, SE = 2.28, 95% CI [1.14, 10.09], p = 0.022
- Potassium (K present vs. absent): difference = -3.98, SE = 2.43, 95% CI [-8.75, 0.78], p = 0.116
- Phosphorus (P present vs. absent): difference = -1.18, SE = 2.56, 95% CI [-6.21, 3.84], p = 0.649

### Effect Estimation

The half-normal plot and Pareto chart (Figure 5) identified active effects using Lenth's pseudo standard error method. Effects exceeding the margin of error are considered active contributors to yield variation.

### Block Analysis

Treatment effects were examined within each block (Figure 4). No significant block x treatment interactions were detected, indicating that treatment effects were consistent across experimental blocks.

### Response Surface Methodology (Synthetic CCD Demonstration)

A second-order RSM model fitted to the synthetic CCD data achieved R^2 = 0.9928. Canonical analysis classified the stationary point at x1 = 0.514, x2 = -0.472 as a maximum (all eigenvalues negative), with a predicted response of 51.925 (Figures 6-7).

### Optimal Factor Settings

The factor combination producing the highest mean yield was N = 1, P = 0, K = 0 (M = 63.77), while the lowest was N = 0, P = 1, K = 1 (M = 50.50).

### Tree-Based Variable Importance

Random forest and LightGBM models were applied as exploratory complements (Figure 9). Given the small sample size (N = 24), these results serve to corroborate rather than replace the ANOVA findings.

### Cross-Method Synthesis

| Factor | ANOVA (eta^2) | RF Importance | LightGBM Importance | Consensus Rank |
|--------|---------------|---------------|---------------------|----------------|
| N | 100.0 | 100.0 | 65.5 | 1 |
| K | 7.5 | 76.7 | 80.3 | 2 |
| P | 0.4 | 33.2 | 100.0 | 3 |

ANOVA identifies N as dominant, while tree-based methods show partial divergence, reflecting potential nonlinear patterns. This convergence across parametric and non-parametric approaches strengthens confidence in the primary experimental finding. Models serve as complementary analytic lenses---ANOVA quantifies controlled effects, RSM maps the response landscape, and tree-based methods confirm factor rankings without distributional assumptions.
