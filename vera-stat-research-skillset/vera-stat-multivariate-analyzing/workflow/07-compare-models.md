# 07 — Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md

## Design Principle

Models are analytic lenses, not contestants. Each method provides a different
kind of insight into multivariate structure. The comparison step synthesizes
what converges and what each uniquely reveals. Never frame as "which model
is best." No R-squared horse race.

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Variable-Level Convergence Table

Synthesize which DVs are most important for group separation across methods.
Normalize all measures to a 0-100 scale (max = 100):

- MANOVA follow-up: partial eta-squared per DV, rescaled
- Discriminant analysis: |structure coefficient| per DV, rescaled
- PCA: |loading on PC1| per DV, rescaled (or PC separating groups most)
- RF importance: mean per-DV importance averaged across DVs as outcomes, rescaled

```
| DV           | MANOVA (eta2) | Discriminant | PCA Loading | RF Importance | Rank Consensus |
|--------------|---------------|--------------|-------------|---------------|----------------|
| Petal.Length | 100           | 100          | 95          | 100           | 1              |
| Petal.Width  | 89            | 92           | 88          | 85            | 2              |
| Sepal.Length | 72            | 65           | 70          | 60            | 3              |
| Sepal.Width  | 30            | 25           | 35          | 40            | 4              |
```

Rank consensus = average rank across all methods.

### 7B: Method Insight Synthesis Table

One row per method family, focus on *what it reveals*:

```
| Method              | Unique Insight                                          |
|---------------------|---------------------------------------------------------|
| MANOVA              | [which DVs show significant group differences]          |
| Discriminant        | [which linear combinations separate groups best]        |
| CCA                 | [how DV set relates to predictor set, if applicable]    |
| Profile Analysis    | [parallelism/levels/flatness — pattern across DVs]      |
| PCA                 | [latent dimensions, which DVs cluster together]         |
| Tree-Based          | [nonlinear importance, which predictors matter per DV]  |
```

Do NOT include R-squared comparison columns. Do NOT rank models by fit.

### 7C: Dimension Summary

Synthesize how many "real" dimensions exist in the multivariate space:
- PCA: how many components above Kaiser criterion
- Discriminant: how many significant discriminant functions
- CCA: how many significant canonical dimensions
- Do these converge on the same dimensionality?

### 7D: Narrative Synthesis

4-6 sentences covering:
1. Which DVs consistently separate groups across all methods
2. What discriminant analysis uniquely reveals (linear combinations, classification)
3. What PCA uniquely reveals (latent structure, dimension reduction)
4. What CCA uniquely reveals (if applicable — cross-set relationships)
5. What trees uniquely reveal (nonlinear patterns, importance comparison across DVs)
6. Overall: convergence across methods strengthens confidence in key multivariate finding

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, dimensionality insight, or classification accuracy.

## Validation Checkpoint

- [ ] Variable-level convergence table with all DVs on 0-100 scale
- [ ] At least 3 methods represented in convergence table
- [ ] Rank consensus column computed
- [ ] Method insight synthesis table: one row per method family
- [ ] No R-squared horse-race comparison between model families
- [ ] Dimension summary: convergence of PCA, discriminant, CCA dimensionality
- [ ] Narrative synthesis: 4-6 sentences covering convergence + unique insights
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
convergence_table: [normalized 0-100 with rank consensus]
insight_table: [method family x unique insight]
dimension_summary: [convergence of dimensionality across methods]
results_para_comparison: [synthesis paragraph prose]
```
