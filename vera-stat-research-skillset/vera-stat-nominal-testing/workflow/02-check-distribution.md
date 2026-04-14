# 02 — Check Class Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Class Frequency Table
- Frequency count per class
- Proportion per class (as percentage)
- Cumulative frequency (optional)

### Rare-Class Detection
```
for each class level:
    if proportion < 5%:
        → WARNING: "[class] has < 5% of observations (n = [val], [pct]%).
           This may cause instability in multinomial models."
    if count < 10:
        → WARNING: "[class] has fewer than 10 observations.
           Consider merging with a related category if substantively justified."
```

### Descriptive Cross-Tabulations
For each key predictor (up to 3):
- If predictor is categorical: cross-tabulation table (outcome x predictor), row/column percentages
- If predictor is continuous: summary stats (n, M, SD) of predictor within each outcome class

### Plots
- Bar chart of class distribution (counts + proportions labeled)
  - Bars colored by class, proportion labels on top
  - Save as `plot_01_class_distribution.png` (8x6, 300 DPI)

### Summary Statement
Print 2-3 sentences:
- How many classes, total N, whether classes are balanced or imbalanced
- Flag any rare classes
- Note if any class dominates (>60% of observations)

## Validation Checkpoint

- [ ] Frequency table with counts and proportions for all classes
- [ ] Rare-class warnings issued if any class < 5%
- [ ] Cross-tabulation or summary stats for key predictors by outcome class
- [ ] plot_01_class_distribution.png generated
- [ ] Summary statement printed (balance assessment)
- [ ] class_balance_flag set (balanced | imbalanced | rare_class_present)

## Data Out → 03-run-primary-test.md

```
class_frequencies: {level: count, ...}
class_proportions: {level: pct, ...}
class_balance_flag: balanced | imbalanced | rare_class_present
cross_tabs: [{predictor, table_data}]
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
