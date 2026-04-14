# 02 — Check Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Tests
- Shapiro-Wilk normality test on outcome
- Skewness (scipy.stats.skew / moments::skewness)
- Kurtosis (excess kurtosis in Python, regular in R — note the difference)

### Descriptive statistics
- Mean, SD, Min, Max, N (non-missing)
- If groups exist: descriptives per group

### Plots
- Histogram with kernel density overlay
- Q-Q plot against normal distribution
- Save as `plot_01_distribution.png` (side-by-side, 12x5, 300 DPI)

### Decision logic (printed in console)

```
if Shapiro-Wilk p >= 0.05 AND |skewness| < 1:
    → "Distribution is approximately normal. OLS is appropriate."
    → normality_flag = TRUE
else:
    → "Distribution deviates from normal. Consider transformation or nonparametric."
    → normality_flag = FALSE
```

### Interpretation
Print 2 sentences: distribution shape + test results, then decision and rationale.

## Validation Checkpoint

- [ ] Shapiro-Wilk W and p reported
- [ ] Skewness and kurtosis reported
- [ ] Descriptive stats complete (M, SD, min, max, N)
- [ ] plot_01_distribution.png generated
- [ ] normality_flag set (TRUE/FALSE)
- [ ] Decision statement printed

## Data Out → 03-run-primary-test.md

```
normality_flag: TRUE | FALSE
descriptives: {mean, sd, min, max, n}
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
