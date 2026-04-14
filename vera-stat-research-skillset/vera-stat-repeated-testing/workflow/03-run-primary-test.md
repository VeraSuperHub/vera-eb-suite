# 03 — Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: test_path, icc_value, attrition_flag, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Test

### If test_path == "paired" (exactly 2 time points):

1. Descriptives per time point (N, M, SD) and per group if applicable
2. Paired t-test: mean difference, t, df, p, 95% CI for mean difference
3. Cohen's d for paired data (using SD of differences)
4. Wilcoxon signed-rank test as nonparametric confirmation
5. If groups exist: run paired t-test within each group separately
6. Plot: paired line plot or box plot of difference scores → `plot_02_interaction.png`
7. 3-sentence interpretation

### If test_path == "rm_anova" (3+ time points, one group):

1. One-way repeated measures ANOVA
2. Mauchly's test for sphericity (W, p)
3. If sphericity violated (p < .05): report Greenhouse-Geisser epsilon and corrected F, df, p
4. If sphericity holds: report uncorrected F, df, p
5. Partial eta-squared for time effect
6. Post-hoc: pairwise paired t-tests with Bonferroni correction
7. Plot: mean trajectory with error bars → `plot_02_interaction.png`
8. 3-sentence interpretation

### If test_path == "mixed_anova" (3+ time points, 2+ groups — the ChickWeight case):

1. Mixed ANOVA with:
   - Within-subjects factor: time
   - Between-subjects factor: group
   - Interaction: time x group
2. Mauchly's test for sphericity on the within-subjects effect
3. If sphericity violated: Greenhouse-Geisser correction applied to within-subjects and interaction effects
4. Report for each effect:
   - Time (within): F, df, p, partial eta-squared
   - Group (between): F, df, p, partial eta-squared
   - Time x Group (interaction): F, df, p, partial eta-squared
5. If interaction significant: "Trajectories differ by group" — primary finding
6. If interaction not significant but main effects significant: interpret main effects
7. Interaction plot: group means over time with error bars → `plot_02_interaction.png`
8. 3-sentence interpretation covering interaction, time, and group effects

### Reporting rules (always follow):
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Effect sizes: Cohen's d (paired), partial eta-squared (ANOVA effects)
- 95% CIs: always for mean differences
- Degrees of freedom: always with t and F stats
- Sphericity: Mauchly's W, p; if violated, GG epsilon and corrected values

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Linear mixed models** — always include: "Random intercept and random slope models handle missing data (MAR), unequal spacing, and individual trajectory differences"
2. **GEE** — always include: "Population-averaged effects with robust standard errors"
3. **Growth curve modeling** — include if 4+ time points: "Polynomial or piecewise trajectories with individual differences in change"
4. **Pairwise comparisons** — always include: "Group differences at each time point and time differences within each group with multiplicity correction"
5. **Tree-based exploratory** — always include: "Variable importance from subject-level features using Random Forest and LightGBM"

### Template:

```
── RECOMMENDED ADDITIONAL ANALYSES ──────────────────────
Based on your repeated measures data:

  [numbered list, 3-5 items, each with 2-line rationale]

→ Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
──────────────────────────────────────────────────────────
```

## Validation Checkpoint

- [ ] Correct test path executed (paired / rm_anova / mixed_anova)
- [ ] Mauchly's test reported (if 3+ time points)
- [ ] GG correction applied if sphericity violated
- [ ] All effects reported with F or t, df, p, effect size
- [ ] Interaction effect reported (mixed ANOVA path)
- [ ] 95% CI reported for mean differences
- [ ] Nonparametric confirmation reported (paired path)
- [ ] plot_02_interaction.png generated
- [ ] Interpretation printed (3 sentences)
- [ ] Recommendation block printed with 3-5 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── {outcome}_repeated_analysis.R
├── {outcome}_repeated_analysis.py
├── plot_01_trajectories.png
└── plot_02_interaction.png
```
