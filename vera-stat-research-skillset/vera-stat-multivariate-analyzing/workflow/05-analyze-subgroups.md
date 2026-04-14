# 05 — Analyze Subgroups

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip if no covariates AND no second factor AND no subgroup variable. Pass through to 06-fit-models.md.

## Generate code for PART 4: Subgroup Analysis

### 5A: MANCOVA (if covariates exist)
1. Fit MANCOVA: DVs ~ Group + Covariates
   - R: `manova(cbind(Y1, Y2, ...) ~ Group + Cov1 + Cov2, data = df)`
   - Python: statsmodels MANOVA with covariates
2. Report all four test statistics for the Group effect after adjusting for covariates:
   - Pillai's V, Wilks' Lambda, Hotelling-Lawley T, Roy's theta
   - F approximation, df, p for each
3. Compare to unadjusted MANOVA — did covariate adjustment change conclusions?
4. Report covariate effects (Pillai's Trace per covariate)
5. Adjusted group means per DV

### 5B: Two-Way MANOVA (if second factor exists)
1. Fit: DVs ~ Factor1 * Factor2
2. Report multivariate tests for:
   - Factor1 main effect (Pillai's V, F, p)
   - Factor2 main effect (Pillai's V, F, p)
   - Factor1 x Factor2 interaction (Pillai's V, F, p)
3. If interaction significant: simple effects analysis
4. Interaction profile plot → `plot_05_interaction.png`
   - DVs on x-axis, means on y-axis, separate lines per Factor1, panels per Factor2

### 5C: Profile Analysis (if DVs on same scale)
Skip if DVs are measured on different scales. Note this in output.

1. **Parallelism test** (Group x DV interaction in repeated-measures framework)
   - Tests whether profiles have the same shape across groups
   - R: restructure to long format, mixed model or `profileR::pbg()`
   - Python: restructure to long, mixed model
   - Report: F, df, p
   - If significant: "Profiles are not parallel — groups differ in their pattern across DVs"

2. **Equal levels test** (Group main effect)
   - Tests whether group means averaged across DVs are equal
   - Report: F, df, p
   - If significant: "Groups differ in their overall level across DVs"

3. **Flatness test** (DV main effect)
   - Tests whether the profile is flat (DVs have equal means averaged across groups)
   - Report: F, df, p
   - If significant: "The profile is not flat — DVs differ from each other"

4. Profile plot with error bars → `plot_06_profile.png`
   - DVs on x-axis, means on y-axis, lines per group, 95% CI error bars
   - 12x6, 300 DPI

### Quality: Apply structure variation
- Profile plot: alternate grouped bar chart vs line plot with error bars
- Interaction plot: vary legend position and facet arrangement
- MANCOVA: vary whether covariate-adjusted or unadjusted result is presented first
- Profile analysis: rotate between "parallel profiles" / "similar patterns" / "comparable shapes"

## Validation Checkpoint

- [ ] MANCOVA: all four statistics for group effect after covariate adjustment (if covariates)
- [ ] Two-way MANOVA: main effects and interaction reported (if second factor)
- [ ] Profile analysis: parallelism, equal levels, flatness tests reported (if same scale)
- [ ] Interaction and profile plots generated (as applicable)
- [ ] Comparison to unadjusted MANOVA stated
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_mancova: [methods paragraph prose]
methods_para_twoway: [methods paragraph prose]
methods_para_profile: [methods paragraph prose]
results_para_mancova: [results paragraph prose]
results_para_twoway: [results paragraph prose]
results_para_profile: [results paragraph prose]
plots: [plot_05_interaction.png, plot_06_profile.png]
tables: [mancova_table, twoway_table, profile_tests_table]
```
