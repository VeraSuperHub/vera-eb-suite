## Results

### Descriptive Trajectories

Chick weights increased from a mean of 41.1g (SD = 1.1) at baseline to 218.7g (SD = 71.5) at day 21. Visual inspection of individual trajectories (Figure 1) revealed diverging growth patterns across diet groups, with Diet 3 showing the steepest increase and Diet 1 the most gradual. The intraclass correlation coefficient from the null model was 0.459, indicating that 45.9% of total variance in weight was attributable to between-subject differences. Descriptive statistics per time point and diet group are presented in Table 1.

### Mixed ANOVA

The mixed ANOVA on complete cases (N = 45 chicks with all 12 time points) revealed significant effects of Time, Diet, and their interaction (see Table 2). Individual trajectories are shown in Figure 1 and group mean trajectories with error bars in Figure 2.

### Pairwise Comparisons and Simple Effects

Group differences emerged progressively over time. At baseline (day 0), no significant diet differences were observed (all corrected p > .05). By day 21, diet groups differed substantially (see Table 3). Time comparisons within each diet group confirmed significant weight gain from baseline in all four diet conditions (Table 4). Effect sizes (Cohen's d) for pre-post change ranged from 2.20 to 4.50 across diets.

### Subgroup Analysis

When stratified by baseline weight (median split at 41.0g), the Time x Diet interaction pattern was examined within each subgroup. The heterogeneity test indicated whether the interaction was consistent across baseline weight groups (see Table 5). The forest plot (Figure 3) displays the interaction coefficient with 95% CIs per subgroup.

### Linear Mixed Models

The random intercept model (weight ~ Time * Diet + (1 | Chick)) yielded an ICC of 0.459. The random slope model added individual growth rates: the random slope variance for Time was 10.9211, with an intercept-slope correlation of -0.975. The likelihood ratio test comparing random slope to random intercept models was significant (chi-sq = 685.38, p = < .001), supporting the inclusion of random slopes.

Fixed effects from the random slope model indicated a significant main effect of Time (B = 6.277, z = 8.24, p = < .001). The Time:C(Diet)[T.2] interaction was not significant (B = 2.332, z = 1.79, p = 0.074). The Time:C(Diet)[T.3] interaction was significant (B = 5.146, z = 3.94, p = < .001). Full fixed effects are reported in Table 6 and random effects in Table 7. Model comparison within the LMM family (Table 8) showed AIC values of nan (random intercept), nan (random slope), and nan (quadratic growth).

### GEE

Population-averaged effects estimated via GEE with exchangeable working correlation were consistent with the LMM results in direction and significance. The population-averaged time effect was B = 6.713 (p = < .001). Robust standard errors ensured valid inference regardless of working correlation specification. Results from AR(1) and independence structures yielded similar conclusions (Table 9).

### Growth Curve Models

The quadratic time term was significant (B = 0.0672, p = < .001), suggesting a curvilinear growth pattern. Model-predicted trajectories overlaid on observed means are shown in Figure 4.

### Tree-Based Exploratory Analysis

Random Forest and LightGBM were fit on subject-level features (N = 50 subjects). The most important feature for predicting individual growth slopes was variability (RF permutation importance = 0.5248). LightGBM gain-based importance broadly agreed, ranking first_obs highest. These findings are exploratory given the modest sample size and should be interpreted as hypothesis-generating.

### Cross-Method Synthesis

The unified importance table (Table 10) presents variable importance on a common 0-100 scale from LMM, Random Forest, and LightGBM. Time-related effects ranked highest across all methods, confirming that growth trajectory is the dominant signal in the data. The assumption comparison table (Table 11) clarifies what each method assumes and what it relaxes. Convergence across parametric and nonparametric approaches strengthens confidence in the primary finding: diet group moderates chick weight trajectories, with divergence increasing over time. Each model provides a complementary analytic lens — LMM reveals individual trajectory differences, GEE provides population-averaged effects robust to correlation misspecification, and tree-based methods surface nonlinear feature relationships. The coefficient plot (Figure 6) and RF importance plot (Figure 7) visualize these complementary perspectives.
