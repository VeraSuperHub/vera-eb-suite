# 03 — Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: sparse_flag, frequency_table, descriptives, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Test

### If 2 groups (n_levels == 2):
1. Group descriptives (n, median, IQR per group)
2. Frequency table per group (counts and row percentages per ordinal level)
3. Mann-Whitney U test
4. Rank-biserial correlation as effect size
5. If group variable is ordered → Jonckheere-Terpstra trend test
6. Stacked bar chart or diverging stacked bar → `plot_02_stacked_bar_[groupvar].png`
7. 3-sentence interpretation

### If 3+ groups (n_levels >= 3):
1. Group descriptives (n, median, IQR per group)
2. Frequency table per group (counts and row percentages per ordinal level)
3. Kruskal-Wallis test
4. Epsilon-squared (omnibus effect size for Kruskal-Wallis)
5. Dunn's post-hoc test (all pairwise with Bonferroni adjustment)
6. Cliff's delta for each significant pair
6. If group variable is ordered → Jonckheere-Terpstra trend test
7. Stacked bar chart per group → `plot_02_stacked_bar_[groupvar].png`
8. 3-sentence interpretation (overall + which pairs differ)

### Reporting rules (always follow):
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Mann-Whitney U: U = X, p = .XXX, rank-biserial r = .XXX
- Kruskal-Wallis: H(df) = X.XX, p = .XXX
- Always report medians and IQRs, not means/SDs
- Proportions as percentages with 1 decimal place

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Ordinal logistic regression (proportional odds)** — always include, mention cumulative OR interpretation
2. **Proportional odds assumption test** — always include, mention Brant test
3. **Subgroup analysis** — include if plausible subgroup variable collected
4. **Spearman correlations** — include if continuous predictors present
5. **Tree-based classification** — always include with honest N caveat

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

- [ ] Group descriptives printed (n, median, IQR per group)
- [ ] Frequency table per group printed
- [ ] Primary test executed with correct statistic (U or H)
- [ ] Effect size reported (rank-biserial r, or epsilon-squared + Cliff's delta)
- [ ] Jonckheere-Terpstra reported if ordered groups
- [ ] plot_02 generated (stacked bar chart)
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
├── plot_01_ordinal_distribution.png
└── plot_02_stacked_bar_[var].png
```
