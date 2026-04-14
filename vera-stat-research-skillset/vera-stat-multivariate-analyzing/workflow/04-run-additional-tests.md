# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-multivariate-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### 4A: Univariate Follow-Up ANOVAs
For each DV:
1. One-way ANOVA: F, df1, df2, p, partial eta-squared
2. If significant: Tukey HSD pairwise comparisons
3. If non-normal DV: Kruskal-Wallis + Dunn's post-hoc as confirmation
4. Bonferroni-corrected alpha = 0.05 / k (where k = number of DVs)
5. Box plots per group per DV → `plot_03_univariate_[dv_name].png`

### 4B: Discriminant Function Analysis
1. Fit LDA: `MASS::lda()` in R, `sklearn.discriminant_analysis.LinearDiscriminantAnalysis` in Python
2. Report number of discriminant functions (min(k, g-1) where g = number of groups)
3. For each discriminant function:
   - Eigenvalue and proportion of between-group variance
   - Canonical correlation
   - Wilks' lambda test of significance (chi-square approximation, df, p)
4. **Standardized discriminant function coefficients** — which DVs contribute most to group separation
5. **Structure coefficients** (discriminant loadings) — correlations between DVs and discriminant functions
6. **Classification accuracy**: confusion matrix, overall hit rate, per-group hit rate
7. Territorial map / scatter of discriminant scores by group → `plot_04_discriminant.png`
   - If 2 functions: 2D scatter colored by group
   - If 1 function: histogram of scores by group

### 4C: Bonferroni-Corrected Pairwise Comparisons
For each DV where ANOVA was significant:
1. All pairwise group comparisons (Tukey HSD or Games-Howell if variances unequal)
2. Mean difference, 95% CI, adjusted p per pair
3. Cohen's d per pair per DV
4. Summary table: DV x Pair x difference x CI x p x d

### Reporting rules:
- Apply Bonferroni correction across DVs for follow-up ANOVAs
- Within each DV, use Tukey HSD for pairwise (already controls familywise error)
- Report both unadjusted and Bonferroni-adjusted significance for univariate follow-ups
- Effect sizes: partial eta-squared per DV for ANOVAs, Cohen's d per pair

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether multivariate result or strongest univariate DV leads the narrative
- Vary whether discriminant function description uses "separated" vs "differentiated" vs "distinguished"
- Vary classification accuracy framing: "correctly classified X%" vs "X% accuracy" vs "hit rate of X%"
- Include 0-1 methodological justifications per test

## Validation Checkpoint

- [ ] Univariate ANOVA per DV with F, df, p, partial eta-squared
- [ ] Bonferroni-corrected alpha stated and applied
- [ ] Tukey HSD pairwise comparisons for significant DVs
- [ ] LDA fit with discriminant function eigenvalues and canonical correlations
- [ ] Wilks' lambda test per discriminant function
- [ ] Standardized coefficients and structure coefficients reported
- [ ] Classification accuracy (confusion matrix + hit rates)
- [ ] plot_03 and plot_04 generated
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out → 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_followup: [methods paragraph prose]
methods_para_discriminant: [methods paragraph prose]
results_para_followup: [results paragraph prose]
results_para_discriminant: [results paragraph prose]
plots: [plot_03_univariate_*.png, plot_04_discriminant.png]
tables: [univariate_anova_table, pairwise_table, discriminant_table, confusion_matrix]
```
