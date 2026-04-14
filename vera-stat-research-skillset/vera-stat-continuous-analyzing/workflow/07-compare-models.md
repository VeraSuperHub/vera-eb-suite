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
- OLS: |standardized β| rescaled
- Random Forest: permutation importance rescaled
- LightGBM: feature_importance(importance_type='gain') rescaled

```
| Variable | OLS (|β|) | RF Importance | LightGBM Importance | Rank Consensus |
|----------|-----------|---------------|---------------------|----------------|
| var1     | 100       | 100           | 85                  | 1              |
| var2     | 67        | 72            | 100                 | 2              |
| ...      | ...       | ...           | ...                 | ...            |
```

Rank consensus = average rank across all three methods.

### 7B: Insight Synthesis Table

One row per model family, focus on *what it reveals*:

```
| Method              | Unique Insight                                    |
|---------------------|---------------------------------------------------|
| OLS                 | [which predictors significant, direction, CIs]    |
| Quantile Regression | [where effects differ across distribution]        |
| Tree-Based          | [nonlinear patterns, interactions, importance]     |
```

Do NOT include R² comparison columns. Do NOT rank models by fit.

### 7C: Narrative Synthesis

3-4 sentences covering:
1. What converges across methods (strongest predictor agreement)
2. What quantile regression uniquely reveals (distributional heterogeneity)
3. What trees uniquely reveal (nonlinear patterns, variable ranking confirmation)
4. Overall: convergence strengthens confidence in key finding

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, unique QR insight, or tree confirmation.

## Validation Checkpoint

- [ ] Unified importance table with all predictors on 0-100 scale
- [ ] At least 3 methods represented in importance table
- [ ] Rank consensus column computed
- [ ] Insight synthesis table: one row per model family
- [ ] No R² horse-race comparison between model families
- [ ] Narrative synthesis: 3-4 sentences covering convergence + unique insights
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
unified_importance_table: [normalized 0-100 with rank consensus]
insight_table: [model family × unique insight]
results_para_comparison: [synthesis paragraph prose]
```
