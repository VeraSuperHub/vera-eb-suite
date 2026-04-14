# 02 — Check Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Multivariate Descriptives
- Mean, SD, Min, Max, N (non-missing) per outcome variable
- If groups exist: descriptives per group per outcome
- Correlation matrix among all outcome variables
- Print correlation matrix with significance stars

### Plots
- Scatterplot matrix (pairs plot) with:
  - Lower triangle: scatter with loess/lowess smoother
  - Diagonal: density per group (colored)
  - Upper triangle: correlation coefficients
  - Color by group variable
  - Save as `plot_01_scattermatrix.png` (square, 10x10, 300 DPI)

### Multivariate Normality
- **Mardia's test** for multivariate skewness and kurtosis
  - R: `MVN::mvn(method = "mardia")`
  - Python: `pingouin.multivariate_normality(method='hz')` or manual Mardia implementation
- **Henze-Zirkler test** as secondary check
  - R: `MVN::mvn(method = "hz")`
  - Python: `pingouin.multivariate_normality()`
- Report: test statistic, p-value, conclusion

### Box's M Test
- Test equality of covariance matrices across groups
  - R: `heplots::boxM()` or `biotools::boxM()`
  - Python: manual implementation or `pingouin` equivalent
- Report: M statistic, F approximation, df1, df2, p-value
- Use strict alpha (.001) for decision — Box's M is sensitive to non-normality

### Univariate Normality Per DV
- Shapiro-Wilk test per outcome variable (overall and per group)
- Skewness and kurtosis per outcome

### Decision Logic (printed in console)

```
Multivariate normality:
  if Mardia skewness p >= 0.05 AND Mardia kurtosis p >= 0.05:
    → "Multivariate normality assumption is tenable."
    → mv_normal_flag = TRUE
  else:
    → "Multivariate normality assumption is violated. Pillai's Trace is recommended (most robust)."
    → mv_normal_flag = FALSE

Covariance equality:
  if Box's M p >= 0.001:
    → "Covariance matrices are approximately equal across groups."
    → box_m_flag = TRUE
  else:
    → "Covariance matrices differ across groups. Pillai's Trace is recommended (most robust)."
    → box_m_flag = FALSE
```

### Interpretation
Print 3-4 sentences: multivariate distribution assessment, Box's M result, which MANOVA statistic to prioritize, and any caveats.

## Validation Checkpoint

- [ ] Descriptive stats complete per outcome (M, SD, min, max, N)
- [ ] Correlation matrix printed with significance
- [ ] plot_01_scattermatrix.png generated
- [ ] Mardia's test reported (skewness + kurtosis statistics and p-values)
- [ ] Henze-Zirkler test reported (statistic and p-value)
- [ ] Box's M test reported (M, F, df, p)
- [ ] Univariate Shapiro-Wilk per DV reported
- [ ] mv_normal_flag set (TRUE/FALSE)
- [ ] box_m_flag set (TRUE/FALSE)
- [ ] Decision statement printed

## Data Out → 03-run-primary-test.md

```
mv_normal_flag: TRUE | FALSE
box_m_flag: TRUE | FALSE
descriptives: [{var, mean, sd, min, max, n}, ...]
correlation_matrix: [k x k matrix]
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
