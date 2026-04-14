# 02 --- Check Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Class Balance Check
- Frequency table of outcome (count and proportion for each level)
- Proportion of minority class
- If minority class < 10%: print rare-event warning with implications
  (separation risk, unstable estimates, consider exact methods or penalized likelihood)

### Descriptives by Outcome Level
- For each predictor/group variable:
  - If categorical: cross-tabulation with outcome, row/column percentages
  - If continuous: mean, SD, min, max, N by outcome level
- Overall N, number of events (outcome = 1), event rate

### Plots
- Grouped bar chart of outcome proportions by primary group variable
  (stacked or side-by-side, with percentage labels)
- Save as `plot_01_class_balance.png` (12x5, 300 DPI)

### Decision logic (printed in console)

```
if minority_proportion >= 0.10:
    → "Class balance is adequate (minority = X.X%). Standard methods apply."
    → balance_flag = TRUE
else:
    → "WARNING: Class imbalance detected (minority = X.X%). Consider exact
       methods, penalized regression, or resampling strategies."
    → balance_flag = FALSE
```

### Interpretation
Print 2 sentences: class balance assessment + implications for analysis approach.

## Validation Checkpoint

- [ ] Frequency table of outcome printed (counts + proportions)
- [ ] Minority class proportion reported
- [ ] If minority < 10%, rare-event warning issued
- [ ] Descriptives by outcome level complete
- [ ] plot_01_class_balance.png generated
- [ ] balance_flag set (TRUE/FALSE)
- [ ] Decision statement printed

## Data Out -> 03-run-primary-test.md

```
balance_flag: TRUE | FALSE
minority_proportion: value
outcome_frequencies: {level_0_n, level_1_n, level_0_pct, level_1_pct}
descriptives_by_outcome: {per-group cross-tabs or summaries}
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
