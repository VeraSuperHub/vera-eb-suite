# 05 -- Analyze Subgroups (Blocking / Nesting / Split-Plot)

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Skip conditions:
- Skip 5A if no additional blocking/nesting structure beyond what was already modeled.
- Skip 5B if design is NOT split-plot.
- If both skipped, pass through to 06-fit-models.md.

## Generate code for PART 4: Stratified / Nested Analysis

### 5A: Stratified Analysis by Block or Nesting Factor

If additional blocking or nesting structure exists beyond the primary model:
1. Fit separate ANOVA within each block (or nesting level)
2. Report effect sizes per stratum
3. Check whether treatment effects are consistent across blocks
4. Block x Treatment interaction test: F, df, p
5. Forest plot of treatment effects per block -> `plot_04_block_forest.png`

### 5B: Split-Plot Analysis

If design is split-plot:
1. Identify whole-plot factor(s) and subplot factor(s)
2. Fit split-plot model with appropriate error terms:
   - Whole-plot effects tested against whole-plot error (block x whole-plot interaction)
   - Subplot effects and interactions tested against subplot error (residual)
3. ANOVA table with TWO error terms clearly labeled
4. Report F-tests with correct denominator for each effect
5. Interpretation: distinguish whole-plot precision from subplot precision

Split-plot model structure:
```
R: aov(response ~ whole_plot * subplot + Error(block/whole_plot), data)
Python: mixedlm or manual SS decomposition
```

### Quality: Apply structure variation
- Forest plot: alternate horizontal vs vertical orientation
- Vary whether block effects are discussed as nuisance or as scientifically interesting
- Non-significant block x treatment interaction: rotate between "treatment effects were
  consistent across blocks" / "blocking did not modify treatment effects" /
  "the experimental blocking was effective at reducing error without interacting with treatments"

## Validation Checkpoint

- [ ] Stratified analysis run within each block/nesting level (if applicable)
- [ ] Block x Treatment interaction test reported (if applicable)
- [ ] Forest plot generated (if applicable)
- [ ] Split-plot ANOVA with two error terms (if split-plot)
- [ ] Each effect tested against correct error term
- [ ] No repeated phrasing patterns from sentence bank

## Data Out -> 06-fit-models.md

```
subgroup_code_r: [PART 4 R code block]
subgroup_code_py: [PART 4 Python code block]
methods_para_blocking: [methods paragraph prose]
methods_para_split_plot: [methods paragraph prose]  # if applicable
results_para_blocking: [results paragraph prose]
results_para_split_plot: [results paragraph prose]  # if applicable
plots: [plot_04_block_forest.png]  # if applicable
```
