# 04 -- Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-doe-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### 4A: Simple Effects Analysis

For each significant interaction (e.g., A x B):
1. Effect of A at each level of B (and vice versa)
2. F-test for each simple effect with df, p, partial eta-squared
3. Tukey HSD within each slice if the simple effect is significant
4. Simple effects interaction plot with error bars per slice

Report pattern: "The effect of [A] was significant at [B = level1], F(df1, df2) = X.XX, p = .XXX, partial eta-squared = .XXX, but not at [B = level2], F(df1, df2) = X.XX, p = .XXX."

### 4B: Contrast Analysis (Planned Comparisons)

1. Define meaningful contrasts based on research question:
   - Control vs. all treatments (if control exists)
   - Linear/quadratic trends (if factor levels are ordered/quantitative)
   - Specific a priori comparisons from the research question
2. Estimate each contrast: difference, SE, t-statistic, p-value, 95% CI
3. Bonferroni or Scheffe adjustment for multiple contrasts

### 4C: Effect Magnitude Ranking

1. Rank all effects (main effects + interactions) by partial eta-squared
2. Formatted table: Effect | SS | df | F | p | Partial eta-squared | Rank
3. Pareto chart or bar chart of effect sizes -> `plot_03_effect_ranking.png`
4. Identify which factors and interactions dominate the response

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether effect size or p-value leads the sentence
- Vary whether simple effects are reported factor-by-factor or in a unified paragraph
- Vary descriptor vocabulary based on effect magnitude
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] Simple effects computed for every significant interaction
- [ ] Contrast analysis with adjusted p-values
- [ ] Effect magnitude ranking table generated
- [ ] Pareto chart / bar chart of effects generated
- [ ] All F-tests include df, p, partial eta-squared
- [ ] p-value formatting follows rules
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out -> 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_simple_effects: [methods paragraph prose]
methods_para_contrasts: [methods paragraph prose]
results_para_simple_effects: [results paragraph prose]
results_para_contrasts: [results paragraph prose]
results_para_ranking: [results paragraph prose]
plots: [plot_03_effect_ranking.png]
tables: [effect_ranking_table, contrast_table]
```
