# 03 — Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: mv_normal_flag, box_m_flag, descriptives, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Multivariate Test

### If 2 groups (n_levels == 2):
1. Group descriptives per outcome (n, M, SD per group per DV)
2. **Hotelling's T²** (two-sample)
   - R: `DescTools::HotellingsT2Test()` or `ICSNP::HotellingsT2()`
   - Python: manual computation or `pingouin` equivalent
3. Report: T² statistic, F approximation, df1 (= k DVs), df2, p-value
4. **Individual follow-up tests**: Welch's t per DV with Bonferroni correction
   - Report: t, df, p (unadjusted and Bonferroni-adjusted), Cohen's d per DV
5. **Partial eta-squared** per DV
6. Group means profile plot → `plot_02_groupmeans.png`
   - Line/point plot with DVs on x-axis, mean on y-axis, lines per group
   - Error bars = 95% CI
   - 12x6, 300 DPI
7. 3-4 sentence interpretation: overall multivariate effect, which DVs drive it, effect magnitudes

### If 3+ groups (n_levels >= 3):
1. Group descriptives per outcome (n, M, SD per group per DV)
2. **One-way MANOVA** — report ALL four test statistics:
   - Pillai's Trace (V) + F approximation + df1 + df2 + p
   - Wilks' Lambda (Λ) + F approximation + df1 + df2 + p
   - Hotelling-Lawley Trace (T) + F approximation + df1 + df2 + p
   - Roy's Largest Root (θ) + F approximation + df1 + df2 + p
   - R: `summary(manova(...), test = c("Pillai","Wilks","Hotelling-Lawley","Roy"))`
   - Python: `statsmodels` MANOVA or manual computation
3. **Recommend primary statistic** based on diagnostics:
   - If mv_normal_flag AND box_m_flag → Wilks' Lambda (most powerful when assumptions met)
   - If NOT mv_normal_flag OR NOT box_m_flag → Pillai's Trace (most robust)
4. **Follow-up univariate ANOVAs** per DV
   - F, df1, df2, p, partial eta-squared per DV
   - Bonferroni-corrected alpha for k DVs
5. **Discriminant analysis summary** (brief)
   - How many significant discriminant functions
   - Which DVs load most heavily (standardized discriminant function coefficients)
6. Group means profile plot → `plot_02_groupmeans.png`
   - Line/point plot with DVs on x-axis, mean on y-axis, lines per group
   - Error bars = 95% CI
   - 12x6, 300 DPI
7. 4-5 sentence interpretation: overall multivariate effect, recommended statistic and why, which DVs separate groups, discriminant function summary

### Reporting rules (always follow):
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Effect sizes: partial eta-squared per DV in follow-ups
- 95% CIs: for group mean differences in follow-ups
- Degrees of freedom: always with F and t statistics
- MANOVA: report all four test statistics even if one is primary
- Box's M decision uses alpha = .001

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Canonical Correlation Analysis (CCA)** — always include if predictors exist (two variable sets)
2. **Profile Analysis** — include if DVs measured on same scale (parallelism, equal levels, flatness)
3. **MANCOVA** — include if covariates collected
4. **Discriminant Function Analysis** — always include (full version with classification accuracy)
5. **Two-way MANOVA** — include if second factor exists
6. **PCA / Dimension Reduction** — always include if k >= 4 DVs
7. **Multivariate regression** — include if predictors exist

### Template:

```
── RECOMMENDED ADDITIONAL ANALYSES ──────────────────────
Based on your multivariate data and research question:

  [numbered list, 4-7 items, each with 2-line rationale]

→ Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
──────────────────────────────────────────────────────────
```

## Validation Checkpoint

- [ ] Group descriptives printed per outcome per group (n, M, SD)
- [ ] Primary multivariate test executed (Hotelling's T² or MANOVA)
- [ ] If MANOVA: all four test statistics reported (Pillai, Wilks, Hotelling-Lawley, Roy)
- [ ] Recommended primary statistic stated with rationale
- [ ] Follow-up univariate tests per DV with Bonferroni correction
- [ ] Partial eta-squared per DV reported
- [ ] plot_02 generated (group means profile)
- [ ] Interpretation printed (3-5 sentences)
- [ ] Recommendation block printed with 4-7 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── multivariate_analysis.R
├── multivariate_analysis.py
├── plot_01_scattermatrix.png
└── plot_02_groupmeans.png
```
