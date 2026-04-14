# 03 — Run Primary Association Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: class_balance_flag, class_frequencies, cross_tabs, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Association Test

### If primary predictor is CATEGORICAL:
1. Cross-tabulation: outcome x predictor (observed counts)
2. Expected counts table
3. Chi-square test of independence
   - Report: chi2 statistic, df, p-value
   - If any expected cell count < 5: also run Fisher's exact test
4. Cramer's V as effect size
   - Small: V ~ 0.1, Medium: V ~ 0.3, Large: V ~ 0.5
5. Mosaic plot or stacked/grouped bar chart → `plot_02_association_[var].png`
6. 3-sentence interpretation: association present/absent, strength, which cells drive it

### If primary predictor is CONTINUOUS:
1. Descriptive statistics: n, M, SD of predictor within each outcome class
2. One-way ANOVA: predictor ~ outcome (outcome as factor)
   - Report: F statistic, df1, df2, p-value
   - eta-squared as effect size
3. If ANOVA significant: Tukey HSD pairwise comparisons
4. Kruskal-Wallis as nonparametric confirmation
   - Report: H statistic, df, p-value
5. Box plot of predictor by outcome class → `plot_02_association_[var].png`
6. 3-sentence interpretation: differences present/absent, which classes differ, effect magnitude

### Reporting rules (always follow):
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Effect sizes: Cramer's V for Chi-square, eta-squared for ANOVA
- Degrees of freedom: always with chi2 and F stats
- State which outcome class is most/least associated with predictor levels
- If Chi-square assumptions violated (expected < 5): note and report Fisher's

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Remaining predictor tests** — include if additional predictors exist beyond primary
2. **Multinomial logistic regression** — always include, note baseline-category logit and RRR
3. **Linear Discriminant Analysis** — always include for classification + variable importance
4. **Tree-based models** — always include (CART, Random Forest, LightGBM multi-class)
5. **Subgroup analysis** — include if plausible subgroup variable collected
6. **Confusion matrix evaluation** — always include (per-class precision/recall)

### Template:

```
── RECOMMENDED ADDITIONAL ANALYSES ──────────────────────
Based on your data and research question:

  [numbered list, 4-6 items, each with 2-line rationale]

→ Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
──────────────────────────────────────────────────────────
```

## Validation Checkpoint

- [ ] Correct test selected based on predictor type (Chi-square or ANOVA)
- [ ] Test statistic, df, p-value reported
- [ ] Effect size reported (Cramer's V or eta-squared)
- [ ] If Chi-square with expected < 5: Fisher's exact also reported
- [ ] If ANOVA significant: Tukey HSD pairwise comparisons reported
- [ ] Nonparametric confirmation (Fisher's exact or Kruskal-Wallis) reported
- [ ] plot_02 generated
- [ ] Interpretation printed (3 sentences)
- [ ] Recommendation block printed with 4-6 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── {outcome}_analysis.R
├── {outcome}_analysis.py
├── plot_01_class_distribution.png
└── plot_02_association_[var].png
```
