# 03 -- Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: normality_flag, homogeneity_flag, balanced, cell_descriptives, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Factorial ANOVA

### Full Factorial ANOVA

1. Fit full model: response ~ factor_A * factor_B * ... (all main effects + all interactions)
   - If RCBD: response ~ block + factor_A * factor_B * ...
   - Block is NOT interacted with treatment factors
2. Type III Sum of Squares (always, regardless of balance)
   - R: `car::Anova(model, type = "III")`
   - Python: `sm.stats.anova_lm(model, typ=3)`
3. Report for EACH effect (main effects and interactions):
   - SS, df, MS, F, p-value
   - Partial eta-squared: SS_effect / (SS_effect + SS_residual)

### Interaction Plots (PART 2)

For each significant interaction:
- Plot cell means with error bars (SE or 95% CI)
- One factor on x-axis, lines for the other factor
- Title: "Interaction: Factor_A x Factor_B"
- Save as `plot_02_effects.png` (300 DPI)

If no significant interactions, plot main effects means with error bars instead.

### Post-hoc Tests

**For significant main effects:**
1. Tukey HSD (all pairwise comparisons)
2. Report: difference, 95% CI, adjusted p-value
3. Letter grouping if 3+ levels

**For significant interactions:**
1. Simple effects: effect of Factor A at each level of Factor B
2. Report F-test for each simple effect
3. Tukey HSD within each level of the moderating factor

### Reporting rules (always follow):
- F(df1, df2) = X.XX, p = .XXX, partial eta-squared = .XXX
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Partial eta-squared for every F-test
- SS Type III always
- Effect estimates with SE for contrasts
- Degrees of freedom always with F statistics

### Interpretation

Print structured interpretation:
1. ANOVA table summary (which effects are significant)
2. Effect size interpretation (small: .01, medium: .06, large: .14 for partial eta-squared)
3. Post-hoc summary (which specific comparisons differ)
4. If blocked: whether block accounted for meaningful variation
5. Practical takeaway (which factor settings produce highest/lowest response)

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Simple effects analysis** -- always include if any interaction is significant
2. **Contrast analysis** -- always include (planned comparisons, e.g., control vs all treatments)
3. **Effect magnitude ranking** -- always include (which factors matter most)
4. **Response Surface Methodology** -- include if factors are continuous (or can be treated as continuous)
5. **Fractional factorial analysis** -- include if design is fractional (alias structure, resolution)
6. **Optimal factor settings** -- always include (which combination maximizes/minimizes response)
7. **Tree-based importance** -- always include (RF + LightGBM variable importance confirmation)
8. **Manuscript generation** -- always include (methods.md + results.md + references.bib)

### Template:

```
-- RECOMMENDED ADDITIONAL ANALYSES ---------------------------
Based on your experimental design and results:

  [numbered list, 4-6 items, each with 2-line rationale]

-> Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
--------------------------------------------------------------
```

## Validation Checkpoint

- [ ] Full factorial ANOVA table printed (SS, df, MS, F, p, partial eta-squared per effect)
- [ ] Type III SS used
- [ ] Block included in model (if RCBD) but not interacted
- [ ] Interaction plots generated for significant interactions (or main effect plots if none)
- [ ] Tukey HSD reported for significant main effects
- [ ] Simple effects reported for significant interactions
- [ ] Effect size interpretation included
- [ ] Practical takeaway stated
- [ ] plot_02_effects.png generated
- [ ] Recommendation block printed with 4-6 items
- [ ] AutoResearch API link included

## Data Out -> Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── {response}_doe_analysis.R
├── {response}_doe_analysis.py
├── plot_01_interaction.png
└── plot_02_effects.png
```
