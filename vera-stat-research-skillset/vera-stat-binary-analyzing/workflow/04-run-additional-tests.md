# 04 --- Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-binary-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### For each additional categorical predictor (not already tested as primary):
1. Contingency table with outcome (observed counts + percentages)
2. Expected cell count check
3. Chi-square test of independence with Cramer's V
4. Fisher's exact test if any expected cell < 5
5. Odds ratio with 95% CI (per level vs reference)
6. Grouped bar chart of outcome proportions -> `plot_03_assoc_[var].png`

### For each continuous predictor:
1. Point-biserial correlation with outcome
2. Report r_pb, p-value
3. Descriptives by outcome level (M, SD, N for each outcome group)
4. Welch's t-test comparing continuous predictor across outcome levels
5. Cohen's d + 95% CI
6. Box plot of continuous predictor by outcome -> `plot_03_boxplot_[var].png`

### Always:
- Report ALL association tests relevant to the research question
- Each test: statistic, df (if applicable), p-value, effect size, CI
- Follow `reference/rules/reporting-standards.md`

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether effect size or p-value leads the sentence
- Vary whether Fisher's exact confirmation is inline or separate sentence
- Vary descriptor vocabulary based on effect magnitude and discipline
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] All relevant association tests executed (chi-square/Fisher's for categorical, point-biserial for continuous)
- [ ] Effect sizes present for every test (Cramer's V, OR, r_pb, Cohen's d)
- [ ] p-value formatting follows rules
- [ ] Fisher's exact included when expected cells < 5
- [ ] OR with 95% CI reported for each categorical comparison
- [ ] Plot generated for each new comparison
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out -> 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_tests: [methods paragraph prose]
results_para_tests: [results paragraph prose]
plots: [list of new plot filenames]
tables: [list of new table data]
```
