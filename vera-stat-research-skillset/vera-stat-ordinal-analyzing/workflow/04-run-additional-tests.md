# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-ordinal-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### If primary was Mann-Whitney and 3+ level variable exists:
1. Kruskal-Wallis on the 3+ level variable
2. Dunn's post-hoc (Bonferroni adjustment) — all pairwise
3. Cliff's delta for each significant pair
4. Stacked bar chart per group → `plot_03_stacked_bar_[var].png`

### If primary was Kruskal-Wallis and 2-level variable exists:
1. Mann-Whitney U on the 2-level variable
2. Rank-biserial r as effect size
3. Stacked bar chart → `plot_03_stacked_bar_[var].png`

### For continuous predictors:
1. Spearman rank correlation (rho) between each continuous predictor and the ordinal outcome (numeric-coded)
2. 95% CI for Spearman rho (Fisher z-transformation or bootstrap)
3. Scatter plot with jitter and trend line → `plot_03_spearman_[var].png`

### For ordinal × ordinal associations:
1. Goodman-Kruskal gamma for each ordinal predictor vs ordinal outcome
2. Report gamma with asymptotic SE and 95% CI
3. Interpret: gamma near 0 = no monotonic association; gamma near ±1 = strong monotonic association

### Always:
- Report ALL relevant associations with the ordinal outcome
- Each test: statistic, df (if applicable), p-value, effect size
- Follow `reference/rules/reporting-standards.md`

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether effect size or p-value leads the sentence
- Vary whether nonparametric detail is inline or separate sentence
- Vary descriptor vocabulary based on effect magnitude and discipline
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] All relevant group comparisons executed
- [ ] Effect sizes present for every test
- [ ] Spearman rho reported for continuous predictors (with CI)
- [ ] Goodman-Kruskal gamma reported for ordinal predictors
- [ ] p-value formatting follows rules
- [ ] Plot generated for each new comparison
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out → 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_tests: [methods paragraph prose]
results_para_tests: [results paragraph prose]
plots: [list of new plot filenames]
tables: [list of new table data]
```
