# 04 — Assess Publication Bias & Sensitivity

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-meta-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Publication Bias & Sensitivity Analysis

### 4A: Publication Bias Assessment

1. **Funnel plot**
   - x-axis: effect size, y-axis: standard error (inverted)
   - Pseudo-confidence region (expected triangle under no bias)
   - Points colored by study; asymmetry = potential bias
   - R: `metafor::funnel()`. Python: custom matplotlib.
   - Save as `plot_03_funnel.png` (8x8, 300 DPI)

2. **Egger's regression test**
   - Regression of standardized effect on precision (1/SE)
   - Report: intercept, SE, t-statistic, p-value
   - R: `metafor::regtest(model, model="lm")`
   - Significant intercept → evidence of funnel plot asymmetry

3. **Begg's rank correlation test**
   - Kendall's rank correlation between effect sizes and variances
   - Report: Kendall's tau, p-value
   - R: `metafor::ranktest(model)`

4. **Trim-and-fill analysis**
   - Estimate number of "missing" studies
   - Report: k imputed, adjusted pooled estimate, adjusted 95% CI
   - R: `metafor::trimfill(model)`
   - Funnel plot with imputed studies → `plot_03b_trimfill.png`

### 4B: Sensitivity Analysis

1. **Leave-one-out analysis**
   - Remove each study in turn, re-estimate pooled effect
   - Table: study removed, new pooled ES, 95% CI, p
   - Flag any study whose removal changes significance or shifts ES substantially
   - R: `metafor::leave1out(model)`

2. **Influence diagnostics**
   - Cook's distance per study
   - DFBETAS per study
   - Externally standardized residuals
   - R: `metafor::influence(model)`
   - Flag studies with Cook's D > 4/k or |DFBETAS| > 1

3. **Cumulative meta-analysis**
   - Pool studies cumulatively ordered by publication year
   - Forest plot showing how the estimate evolves over time
   - Does the estimate stabilize? When?
   - R: `metafor::cumul(model, order=year)`
   - Save as `plot_03c_cumulative.png` (10x8, 300 DPI)

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether Egger's or Begg's result leads the bias paragraph
- Vary whether trim-and-fill is framed as "adjustment" or "sensitivity check"
- Vary leave-one-out framing: "robust" vs "stable" vs "consistent"
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] Funnel plot generated (plot_03_funnel.png)
- [ ] Egger's test reported: intercept, SE, t, p
- [ ] Begg's test reported: tau, p
- [ ] Trim-and-fill: k imputed, adjusted ES, adjusted CI
- [ ] Trim-and-fill funnel plot generated (plot_03b_trimfill.png)
- [ ] Leave-one-out table complete (k rows)
- [ ] Influential studies flagged with Cook's D and DFBETAS
- [ ] Cumulative meta-analysis forest plot generated (plot_03c_cumulative.png)
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out → 05-analyze-subgroups.md

```
bias_code_r: [PART 3 R code block]
bias_code_py: [PART 3 Python code block]
methods_para_bias: [methods paragraph prose]
results_para_bias: [results paragraph prose]
results_para_sensitivity: [results paragraph prose]
plots: [plot_03_funnel.png, plot_03b_trimfill.png, plot_03c_cumulative.png]
tables: [leave1out_table, influence_table]
influential_studies: [list of flagged study IDs]
```
