# 02 — Check Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Frequency Table
- Tabulate count values (0, 1, 2, 3, ...) up to a reasonable truncation point
- Show observed frequency and percentage for each count value
- If max count > 20, bin into ranges for display

### Descriptive Statistics
- Mean, variance, SD, min, max, median, N (non-missing)
- If groups exist: descriptives per group
- If exposure variable exists: compute and display rate (count/exposure) distribution too

### Overdispersion Assessment
- Overdispersion ratio = variance / mean
- Interpretation:
  - Ratio < 1.5 → "Approximate equidispersion — Poisson assumptions likely met"
  - Ratio ≥ 1.5 → "Overdispersion detected — Negative Binomial preferred"
  - Ratio < 1.0 → "Underdispersion — rare; Poisson may still be conservative"

### Zero-Inflation Check
- Proportion of zeros in the outcome
- Expected proportion of zeros under Poisson (exp(-mean))
- If observed zeros > 20% AND observed >> Poisson expected → flag for zero-inflation
- Print: "Observed zeros: X% vs Poisson expected: Y%"

### Plots
- Bar chart of count frequencies (observed) + overlay Poisson expected frequencies (red dots/line)
- If exposure exists: additional histogram of rate distribution
- Save as `plot_01_count_distribution.png` (12x5, 300 DPI)

### Decision Logic (printed in console)

```
if overdispersion_ratio < 1.5 AND zero_proportion ≤ 0.20:
    → "Poisson distribution is appropriate."
    → distribution_flag = "poisson"
elif overdispersion_ratio ≥ 1.5 AND zero_proportion ≤ 0.20:
    → "Overdispersion detected. Negative Binomial is preferred."
    → distribution_flag = "negbin"
elif zero_proportion > 0.20:
    → "Excess zeros detected. Consider Zero-Inflated models (available in full analysis)."
    → distribution_flag = "zero_inflated"
    → If also overdispersed: note both issues
```

### Interpretation
Print 2-3 sentences: count distribution shape, overdispersion assessment, zero-inflation status, then decision and rationale.

## Validation Checkpoint

- [ ] Frequency table of count values generated
- [ ] Mean and variance reported
- [ ] Overdispersion ratio computed and interpreted
- [ ] Zero proportion computed and compared to Poisson expected
- [ ] plot_01_count_distribution.png generated
- [ ] If exposure variable: rate distribution also displayed
- [ ] distribution_flag set (poisson | negbin | zero_inflated)
- [ ] Decision statement printed

## Data Out → 03-run-primary-test.md

```
distribution_flag: "poisson" | "negbin" | "zero_inflated"
overdispersion_ratio: float
zero_proportion: float
count_subtype: "event_count" | "event_rate"
descriptives: {mean, variance, sd, min, max, median, n}
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
