# 02 — Assess Heterogeneity

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Study Summary Table
- Table of included studies: study ID, N (or n_treatment + n_control), effect size, 95% CI, weight (inverse-variance)
- Print to console and store as data frame
- Sort by effect size or study ID (user preference)

### Forest Plot
- Standard forest plot showing:
  - Each study as square (size proportional to weight) + 95% CI line
  - Summary diamond at bottom (random-effects pooled estimate)
  - Dashed vertical line at null (0 for SMD/MD, 1 for OR/RR)
  - Study labels on left, effect size + CI on right
- Save as `plot_01_forest.png` (10x8, 300 DPI)
- R: `metafor::forest()`. Python: custom matplotlib or forestplot package.

### Heterogeneity Assessment
- Cochran's Q statistic with df and p-value
- I² (percentage of variability due to true heterogeneity)
- tau² (between-study variance estimate)
- H² (total variability / within-study variability)

### Decision logic (printed in console)

```
if I² < 25%:
    → "Low heterogeneity (I² = [val]%). Fixed-effects model may be appropriate."
    → heterogeneity_level = "low"
elif I² <= 75%:
    → "Moderate heterogeneity (I² = [val]%). Random-effects model recommended."
    → heterogeneity_level = "moderate"
else:
    → "High heterogeneity (I² = [val]%). Random-effects model required; moderator analysis strongly recommended."
    → heterogeneity_level = "high"
```

### Interpretation
Print 2-3 sentences: number of studies synthesized, heterogeneity level with statistics, and implication for model choice.

## Validation Checkpoint

- [ ] Study summary table complete (ID, N, ES, CI, weight)
- [ ] plot_01_forest.png generated with proper formatting
- [ ] Cochran's Q reported with df and p
- [ ] I² reported as percentage
- [ ] tau² reported
- [ ] H² reported
- [ ] heterogeneity_level set (low/moderate/high)
- [ ] Decision statement printed

## Data Out → 03-run-primary-test.md

```
heterogeneity_level: "low" | "moderate" | "high"
Q_stat: {Q, df, p}
I_squared: value
tau_squared: value
study_table: data frame
forest_code_r: [PART 1 R code block]
forest_code_py: [PART 1 Python code block]
```
