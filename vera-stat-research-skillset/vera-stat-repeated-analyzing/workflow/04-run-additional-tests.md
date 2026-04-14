# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-repeated-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Pairwise Comparisons & Simple Effects

### 4A: Pairwise Comparisons at Each Time Point (group differences per wave)

For each time point:
1. Subset data to that time point
2. Compare groups (t-test or ANOVA depending on number of groups)
3. Effect size (Cohen's d for 2 groups, partial eta-squared for 3+)
4. 95% CI for each group difference
5. Apply multiple comparison correction (Bonferroni across time points)

Output: Table with Time | Comparison | Statistic | p (uncorrected) | p (corrected) | Effect Size | 95% CI

### 4B: Pairwise Comparisons Within Each Group (time differences per group)

For each group:
1. Subset data to that group
2. All pairwise time point comparisons (paired t-tests)
3. Cohen's d for paired data
4. Apply Bonferroni correction across pairwise comparisons

Output: Table with Group | Time1 vs Time2 | Mean Diff | t | df | p (corrected) | d

### 4C: Simple Effects Analysis

Time effect within each group separately:
1. For each group: one-way RM-ANOVA on time
2. Report: F, df, p, partial eta-squared per group
3. Interpretation: which groups show significant change over time?

### 4D: Effect Size Summary

Compile all pairwise effect sizes into a summary table:
- Pre-post effect sizes per group (first to last time point)
- Adjacent time point effect sizes per group
- Cross-group effect sizes at each time point

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether effect size or p-value leads the sentence
- Vary whether correction method is stated inline or in a footnote
- Rotate between "significant at the corrected threshold" / "survived correction" / "remained significant after adjustment"
- Include 0-1 methodological justifications per comparison set

## Validation Checkpoint

- [ ] Group comparisons at each time point executed with effect sizes
- [ ] Time comparisons within each group executed with effect sizes
- [ ] Simple effects (time within group) reported with F, df, p, eta-squared
- [ ] Multiple comparison correction applied and method stated
- [ ] Both corrected and uncorrected p-values reported
- [ ] Effect size summary table generated
- [ ] p-value formatting follows rules
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out → 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_pairwise: [methods paragraph prose]
results_para_pairwise: [results paragraph prose]
tables: [pairwise_by_time, pairwise_by_group, simple_effects, effect_summary]
```
