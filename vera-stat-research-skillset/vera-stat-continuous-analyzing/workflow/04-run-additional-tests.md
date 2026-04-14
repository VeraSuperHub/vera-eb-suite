# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-continuous-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### If primary was t-test and 3+ level variable exists:
1. One-way ANOVA on the 3+ level variable
2. η² for effect size
3. Tukey HSD post-hoc — all pairwise with adjusted p
4. Kruskal-Wallis nonparametric confirmation
5. Box plot per group → `plot_03_boxplot_[var].png`

### If primary was ANOVA and 2-level variable exists:
1. Welch's t on the 2-level variable
2. Cohen's d + 95% CI
3. Mann-Whitney U confirmation

### Always:
- Report ALL group comparisons relevant to the research question
- Each test: statistic, df, p-value, effect size, CI
- Follow `reference/rules/reporting-standards.md`

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether effect size or p-value leads the sentence
- Vary whether nonparametric confirmation is inline or separate sentence
- Vary descriptor vocabulary based on effect magnitude and discipline
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] All relevant group comparisons executed
- [ ] Effect sizes present for every test
- [ ] p-value formatting follows rules
- [ ] Nonparametric confirmations included
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
