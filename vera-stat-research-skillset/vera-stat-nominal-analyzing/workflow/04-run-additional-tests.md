# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-nominal-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### 4A: Remaining Categorical Predictors
For each categorical predictor not yet tested:
1. Cross-tabulation: outcome x predictor (observed + expected)
2. Chi-square test of independence
   - If any expected cell count < 5: also run Fisher's exact test
3. Cramer's V as effect size
4. Grouped bar chart or mosaic plot
5. 2-sentence interpretation per predictor

### 4B: Remaining Continuous Predictors
For each continuous predictor not yet tested:
1. Descriptive statistics of predictor within each outcome class (n, M, SD)
2. One-way ANOVA: predictor ~ outcome (outcome as factor)
   - F statistic, df, p-value, eta-squared
3. If ANOVA significant: Tukey HSD pairwise comparisons
4. Kruskal-Wallis as nonparametric confirmation
5. Box plot of predictor by outcome class
6. 2-sentence interpretation per predictor

### 4C: Pairwise Class Comparisons
For the primary predictor(s):
1. All pairwise combinations of outcome classes (e.g., setosa vs versicolor, setosa vs virginica, versicolor vs virginica)
2. For categorical predictors: pairwise Chi-square (subset to 2 classes at a time)
3. For continuous predictors: pairwise t-tests or Wilcoxon with Bonferroni correction
4. Summary table of all pairwise comparisons with adjusted p-values

### Always:
- Report ALL predictor-outcome associations relevant to the research question
- Each test: statistic, df, p-value, effect size
- Follow `reference/rules/reporting-standards.md`

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether effect size or p-value leads the sentence
- Vary whether nonparametric confirmation is inline or separate sentence
- Vary descriptor vocabulary based on effect magnitude and discipline
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] All remaining categorical predictors tested (Chi-square + Cramer's V)
- [ ] All remaining continuous predictors tested (ANOVA + eta-squared)
- [ ] Fisher's exact reported where expected cell counts < 5
- [ ] Pairwise class comparisons completed with adjusted p-values
- [ ] Effect sizes present for every test
- [ ] p-value formatting follows rules
- [ ] Nonparametric confirmations included
- [ ] Plot generated for each new predictor
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out → 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_tests: [methods paragraph prose]
results_para_tests: [results paragraph prose]
plots: [list of new plot filenames]
tables: [list of new table data]
pairwise_comparisons: [summary table]
```
