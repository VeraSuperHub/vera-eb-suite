# 03 --- Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: balance_flag, outcome_frequencies, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Association Test

### For outcome x primary group variable:

1. **Contingency table** (observed counts, row percentages, column percentages)

2. **Expected cell count check**
   - Compute expected frequencies
   - Flag any cell with expected count < 5

3. **Chi-square test of independence**
   - Report: chi-sq(df) = X.XX, p = .XXX
   - Cramer's V effect size with interpretation (small/medium/large per Cohen)

4. **Fisher's exact test**
   - Always run if any expected cell < 5
   - Also run as confirmation when all cells >= 5
   - Report: p = .XXX (two-sided)

5. **Odds ratio with 95% CI**
   - For 2x2 tables: compute directly from contingency table
   - Report: OR = X.XX, 95% CI [X.XX, X.XX]
   - Interpret direction: "X had Y.YY times the odds of [outcome] compared to Z"
   - For 2xK tables (3+ group levels): report OR for each level vs reference

6. **Mosaic plot or grouped bar chart**
   - Mosaic plot preferred for 2x2 (shading by residual)
   - Grouped bar chart for 2xK (proportions with error bars)
   - Save as `plot_02_mosaic_[groupvar].png` (12x5, 300 DPI)

7. **3-sentence interpretation**
   - Sentence 1: overall association (significant or not, effect size)
   - Sentence 2: direction of effect (OR interpretation)
   - Sentence 3: nonparametric/exact confirmation consistency

### Reporting rules (always follow):
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Odds ratios: "OR = X.XX, 95% CI [X.XX, X.XX]"
- Chi-square: "chi-sq(df) = X.XX, p = .XXX, Cramer's V = .XXX"
- Proportions: percentages with 1 decimal place
- Degrees of freedom: always with chi-square statistic

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Logistic regression** --- always include, list specific predictors/covariates
2. **Subgroup analysis** --- include if plausible subgroup variable collected
3. **Additional chi-square/Fisher's** --- include if other categorical predictors exist
4. **Tree-based classification** --- always include with honest N caveat
5. **ROC analysis** --- always include for model discrimination assessment

### Template:

```
-- RECOMMENDED ADDITIONAL ANALYSES ----------------------------------------
Based on your data and research question:

  [numbered list, 3-5 items, each with 2-line rationale]

-> Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
---------------------------------------------------------------------------
```

## Validation Checkpoint

- [ ] Contingency table printed (observed counts + percentages)
- [ ] Expected cell counts checked, flag reported
- [ ] Chi-square test executed with chi-sq, df, p, Cramer's V
- [ ] Fisher's exact test executed when applicable
- [ ] Odds ratio reported with 95% CI
- [ ] OR direction interpreted in plain language
- [ ] plot_02 generated (mosaic or grouped bar)
- [ ] Interpretation printed (3 sentences)
- [ ] Recommendation block printed with 3-5 items
- [ ] AutoResearch API link included

## Data Out -> Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── {outcome}_analysis.R
├── {outcome}_analysis.py
├── plot_01_class_balance.png
└── plot_02_mosaic_[var].png
```
