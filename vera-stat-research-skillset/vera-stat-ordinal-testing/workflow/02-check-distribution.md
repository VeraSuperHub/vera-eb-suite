# 02 — Check Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Frequency Table
- Count per ordinal level
- Proportion per level (as percentage, 1 decimal)
- Cumulative proportion per level
- Print as formatted table

### Per-Group Frequency Table
- If group variable exists: cross-tabulation of outcome × group
- Row percentages (proportions within each group)
- Column totals

### Descriptive Statistics
- Median and IQR of outcome (numeric-coded)
- Mode (most frequent level)
- If groups exist: median and IQR per group

### Sparse Level Check
```
for each level:
    if count < 5:
        → WARNING: Level "[level]" has fewer than 5 observations.
          Consider collapsing adjacent levels before analysis.
    sparse_flag = TRUE if any level < 5, else FALSE
```

### Plots
- Bar chart of ordinal outcome (ordered levels on x-axis, count on y-axis)
- Overlay cumulative proportion line on secondary axis
- Save as `plot_01_ordinal_distribution.png` (12x5, 300 DPI)

### Interpretation
Print 2-3 sentences: distribution shape across levels (which level most common,
whether distribution is skewed toward low or high end), any sparse levels flagged.

## Validation Checkpoint

- [ ] Frequency table with counts, proportions, and cumulative proportions
- [ ] Cross-tabulation printed (if group variable exists)
- [ ] Median and IQR reported (overall and per group if applicable)
- [ ] Sparse level check completed with warning if any < 5
- [ ] plot_01_ordinal_distribution.png generated
- [ ] sparse_flag set (TRUE/FALSE)
- [ ] Interpretation printed (2-3 sentences)

## Data Out → 03-run-primary-test.md

```
sparse_flag: TRUE | FALSE
frequency_table: {level: count, proportion, cumulative}
cross_tab: {group × level matrix} or null
descriptives: {median, iqr, mode, n}
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
