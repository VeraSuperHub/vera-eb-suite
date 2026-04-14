# 02 -- Check Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Cell Descriptives

For every factor combination (cell):
- N per cell
- Mean
- SD
- Min, Max

Print as formatted table.

### Balance Check

1. Count N per cell (every treatment combination)
2. If all cells equal: "Design is balanced. Type I = Type II = Type III SS."
3. If unequal: "Design is unbalanced. Type III SS will be used (invariant to cell frequencies)."
4. Flag any empty cells: "WARNING: Empty cell(s) detected — some effects are not estimable."

### Interaction Plot

For each pair of factors:
- Plot cell means with one factor on x-axis, lines for the other factor
- Non-parallel lines suggest interaction
- Save as `plot_01_interaction.png` (grid layout if multiple pairs, 300 DPI)

### Residual Assessment

1. Fit the full factorial model (all main effects + all interactions, include block if RCBD)
2. Extract residuals
3. Shapiro-Wilk test on residuals
4. Levene's test for homogeneity of variance across treatment groups

### Decision Logic (printed in console)

```
RESIDUAL NORMALITY:
if Shapiro-Wilk on residuals p >= 0.05:
    -> "Residuals are approximately normal. ANOVA assumptions met."
    -> normality_flag = TRUE
else:
    -> "Residuals deviate from normality. Results should be interpreted with caution."
    -> normality_flag = FALSE

VARIANCE HOMOGENEITY:
if Levene's p >= 0.05:
    -> "Equal variances assumption satisfied."
    -> homogeneity_flag = TRUE
else:
    -> "Unequal variances detected. Consider Welch or transformation."
    -> homogeneity_flag = FALSE
```

### Interpretation

Print 3 sentences: (1) balance status, (2) residual normality result, (3) variance homogeneity result + recommendation.

## Validation Checkpoint

- [ ] Cell descriptives printed (N, M, SD per factor combination)
- [ ] Balance check reported (balanced/unbalanced, any empty cells)
- [ ] Interaction plot generated (plot_01_interaction.png)
- [ ] Shapiro-Wilk on residuals: W and p reported
- [ ] Levene's test: F, df, p reported
- [ ] normality_flag set (TRUE/FALSE)
- [ ] homogeneity_flag set (TRUE/FALSE)
- [ ] Decision statements printed

## Data Out -> 03-run-primary-test.md

```
normality_flag: TRUE | FALSE
homogeneity_flag: TRUE | FALSE
balanced: TRUE | FALSE
cell_descriptives: [{cell, n, mean, sd}]
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
