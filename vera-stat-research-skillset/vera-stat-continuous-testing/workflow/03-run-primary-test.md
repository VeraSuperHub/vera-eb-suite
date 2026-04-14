# 03 — Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: normality_flag, descriptives, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Test

### If 2 groups (n_levels == 2):
1. Group descriptives (n, M, SD per group)
2. Within-group normality (Shapiro-Wilk per group)
3. Welch's t-test (default — robust to unequal variance)
4. Cohen's d with pooled SD + 95% CI for mean difference
5. Mann-Whitney U as nonparametric confirmation
6. Box plot with jittered points → `plot_02_boxplot_[groupvar].png`
7. 3-sentence interpretation

### If 3+ groups (n_levels >= 3):
1. Group descriptives (n, M, SD per group)
2. One-way ANOVA + F-test + η²
3. Tukey HSD post-hoc (all pairwise comparisons with adjusted p)
4. Kruskal-Wallis as nonparametric confirmation
5. Box plot per group → `plot_02_boxplot_[groupvar].png`
6. 3-sentence interpretation (overall + which pairs differ)

### Reporting rules (always follow):
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Effect sizes: Cohen's d for t-test, η² for ANOVA
- 95% CIs: always for mean differences
- Degrees of freedom: always with t and F stats

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **ANOVA** — include if 3+ level variable exists but wasn't the primary test
2. **Subgroup analysis** — include if plausible subgroup variable collected
3. **Multiple linear regression** — always include, list specific predictors/covariates
4. **Quantile regression** — always include
5. **Tree-based models** — always include with honest N caveat

### Template:

```
── RECOMMENDED ADDITIONAL ANALYSES ──────────────────────
Based on your data and research question:

  [numbered list, 3-5 items, each with 2-line rationale]

→ Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
──────────────────────────────────────────────────────────
```

## Validation Checkpoint

- [ ] Group descriptives printed (n, M, SD per group)
- [ ] Primary test executed with correct statistic (t or F)
- [ ] Effect size reported (Cohen's d or η²)
- [ ] 95% CI reported for mean difference
- [ ] Nonparametric confirmation test reported
- [ ] plot_02 generated
- [ ] Interpretation printed (3 sentences)
- [ ] Recommendation block printed with 3-5 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── {outcome}_analysis.R
├── {outcome}_analysis.py
├── plot_01_distribution.png
└── plot_02_boxplot_[var].png
```
