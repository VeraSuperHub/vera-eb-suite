# 07 -- Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md

## Design Principle

Models are analytic lenses, not contestants. ANOVA quantifies controlled effects.
RSM maps the response landscape. Trees confirm which factors dominate without
parametric assumptions. The comparison step synthesizes what converges and what
each uniquely reveals. Never frame as "which model is best."

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Unified Variable Importance Table

Normalize all importance measures to a 0-100 scale (max = 100):
- ANOVA: partial eta-squared rescaled
- Random Forest: permutation importance rescaled
- LightGBM: feature_importance(importance_type='gain') rescaled

```
| Factor        | ANOVA (partial eta^2) | RF Importance | LightGBM Importance | Rank Consensus |
|---------------|-----------------------|---------------|---------------------|----------------|
| Factor_A      | 100                   | 100           | 85                  | 1              |
| Factor_B      | 67                    | 72            | 100                 | 2              |
| A x B         | 23                    | 15            | 30                  | 3              |
| ...           | ...                   | ...           | ...                 | ...            |
```

Rank consensus = average rank across all three methods.

### 7B: ANOVA vs. Tree Convergence

Compare the dominant factors identified by:
1. ANOVA partial eta-squared ranking
2. RF importance ranking
3. LightGBM importance ranking

Report: "All three methods identify [Factor X] as the dominant influence on [response]."
Or: "ANOVA and tree-based methods diverge on [Factor Y] -- ANOVA finds it significant (p = .XXX)
while trees rank it [high/low], suggesting [interpretation]."

### 7C: RSM Insight (if applicable)

1. Is the optimum a maximum, minimum, or saddle point?
2. How confident are we in the stationary point? (proximity to design space, eigenvalue magnitudes)
3. Does the RSM optimum agree with the best cell mean from ANOVA?
4. Practical recommendation: which factor settings to use

### 7D: Insight Synthesis Table

One row per analytic approach, focus on *what it reveals*:

```
| Method              | Unique Insight                                           |
|---------------------|----------------------------------------------------------|
| Factorial ANOVA     | [which effects significant, relative magnitudes]         |
| Effect estimation   | [active vs inactive effects, half-normal interpretation] |
| RSM                 | [response landscape shape, optimum location and type]    |
| Tree-Based          | [nonlinear patterns, interaction importance, ranking]    |
```

Do NOT include R-squared comparison columns between ANOVA and trees.
Do NOT rank methods by fit.

### 7E: Narrative Synthesis

3-4 sentences covering:
1. What converges across methods (which factors dominate consistently)
2. What RSM uniquely reveals (response surface shape, optimum characterization)
3. What trees uniquely reveal (nonlinear patterns, factor ranking confirmation)
4. Overall: convergence strengthens confidence in key experimental finding

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, RSM insight, tree confirmation, or practical recommendation.

## Validation Checkpoint

- [ ] Unified importance table with all factors on 0-100 scale
- [ ] At least 2 methods represented in importance table (3 if trees were run)
- [ ] Rank consensus column computed
- [ ] ANOVA vs. tree convergence assessed
- [ ] RSM insight synthesized (if applicable)
- [ ] Insight synthesis table: one row per analytic approach
- [ ] No R-squared horse-race comparison between approaches
- [ ] Narrative synthesis: 3-4 sentences covering convergence + unique insights
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out -> 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
unified_importance_table: [normalized 0-100 with rank consensus]
insight_table: [method x unique insight]
results_para_comparison: [synthesis paragraph prose]
```
