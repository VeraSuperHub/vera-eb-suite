# 07 — Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md

## Design Principle

Models are analytic lenses, not contestants. Each model type provides a different
kind of insight. The comparison step synthesizes what converges and what each
uniquely reveals. Never frame as "which model is best."

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Unified Variable Importance Table

Normalize all importance measures to a 0-100 scale (max = 100):
- Best count model (from A6): |standardized coefficient| rescaled
  - Standardization: for each predictor, compute the change in log(expected count) per SD of predictor, then rescale to 0-100
- Random Forest: permutation importance rescaled
- LightGBM: feature_importance(importance_type='gain') rescaled

```
| Variable | Count Model (|std coef|) | RF Importance | LightGBM Importance | Rank Consensus |
|----------|--------------------------|---------------|---------------------|----------------|
| var1     | 100                      | 100           | 85                  | 1              |
| var2     | 67                       | 72            | 100                 | 2              |
| ...      | ...                      | ...           | ...                 | ...            |
```

Rank consensus = average rank across all three methods.

### 7B: Insight Synthesis Table

One row per model family, focus on *what it reveals*:

```
| Method              | Distributional Assumption        | Unique Insight                                    |
|---------------------|----------------------------------|---------------------------------------------------|
| Poisson             | Equidispersion (var = mean)      | [baseline IRRs, adequate if no overdispersion]    |
| Negative Binomial   | Overdispersion allowed           | [relaxed variance, theta estimate, LR test]       |
| ZIP/ZINB            | Excess zeros from two processes  | [which predictors drive zero-inflation]            |
| Hurdle              | Zeros separate from counts       | [what predicts any event vs event frequency]       |
| Tree-Based          | Non-parametric, no distribution  | [nonlinear patterns, interactions, importance]     |
```

Do NOT rank models by AIC as a horse-race. Present AIC only as evidence for distributional fit.

### 7C: Key Comparison
- Do the count model IRRs agree with tree-based importance rankings?
- Which predictors are consistently important across all methods?
- Where do methods diverge, and what does that reveal about the data?

### 7D: Narrative Synthesis

3-4 sentences covering:
1. What converges across methods (strongest predictor agreement)
2. What the distributional models reveal (Poisson assumes equidispersion, NB relaxes this, ZIP/ZINB handle excess zeros)
3. What trees uniquely reveal (nonlinear patterns, variable ranking confirmation or divergence)
4. Overall: convergence strengthens confidence in key finding

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, unique distributional insight, or tree confirmation.

## Validation Checkpoint

- [ ] Unified importance table with all predictors on 0-100 scale
- [ ] At least 3 methods represented in importance table (best count model + RF + LightGBM)
- [ ] Rank consensus column computed
- [ ] Insight synthesis table: one row per model family
- [ ] No AIC horse-race comparison between model families
- [ ] Key comparison: IRRs vs tree importance rankings addressed
- [ ] Narrative synthesis: 3-4 sentences covering convergence + unique insights
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
unified_importance_table: [normalized 0-100 with rank consensus]
insight_table: [model family x unique insight]
results_para_comparison: [synthesis paragraph prose]
```
