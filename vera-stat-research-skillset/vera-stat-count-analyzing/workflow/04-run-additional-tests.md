# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-count-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### If primary was 2-group and 3+ level variable exists:
1. Poisson or NB regression: outcome ~ categorical_var (+ offset if rate data)
2. Likelihood ratio test for overall group effect
3. IRR for each level vs reference with 95% CI
4. Kruskal-Wallis nonparametric confirmation
5. Bar chart of mean counts per group → `plot_03_mean_counts_[var].png`

### If primary was 3+ group and 2-level variable exists:
1. Poisson or NB regression: outcome ~ binary_var (+ offset if rate data)
2. IRR with 95% CI
3. Mann-Whitney U confirmation

### For continuous predictors:
1. Spearman correlation with count outcome
2. Scatter plot of predictor vs count (jittered) with Poisson/NB regression curve
3. Report: rho, p-value
4. Plot → `plot_03_scatter_[var].png`

### If rate data:
- Compare rates across groups with person-time denominators
- Report: events, person-time, rate per [unit], rate ratio with 95% CI

### Always:
- Report ALL group comparisons relevant to the research question
- Each test: IRR or rate ratio, CI, p-value
- Follow `reference/rules/reporting-standards.md`

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether IRR or p-value leads the sentence
- Vary whether nonparametric confirmation is inline or separate sentence
- Vary descriptor vocabulary based on IRR magnitude and discipline
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] All relevant group comparisons executed
- [ ] IRR with 95% CI present for every group comparison
- [ ] If rate data: rates reported with person-time denominators
- [ ] p-value formatting follows rules
- [ ] Nonparametric confirmations included
- [ ] Continuous predictor correlations (Spearman) reported if applicable
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
