# 07 --- Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md

## Design Principle

Models are analytic lenses, not contestants. Each model type provides a different
kind of insight. The comparison step synthesizes what converges and what each
uniquely reveals. Never frame as "which model is best." No AUC horse race.

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Unified Variable Importance Table

Normalize all importance measures to a 0-100 scale (max = 100):
- Logistic regression: |standardized coefficients| rescaled
  (standardize continuous predictors, use absolute value of z-score-scaled B)
- Random Forest: mean decrease in Gini (or accuracy) rescaled
- LightGBM: feature_importance(importance_type='gain') rescaled

```
| Variable | Logistic (|std B|) | RF Importance | LightGBM Importance | Rank Consensus |
|----------|--------------------|---------------|---------------------|----------------|
| var1     | 100                | 100           | 85                  | 1              |
| var2     | 67                 | 72            | 100                 | 2              |
| ...      | ...                | ...           | ...                 | ...            |
```

Rank consensus = average rank across all three methods.

### 7B: Insight Synthesis Table

One row per model family, focus on *what it reveals*:

```
| Method              | Unique Insight                                         |
|---------------------|--------------------------------------------------------|
| Logistic Regression | [which predictors significant, OR direction, CIs]      |
| Tree-Based          | [nonlinear patterns, interactions, importance ranking]  |
| Chi-square/Fisher   | [bivariable associations, cell-level patterns]          |
```

Do NOT include AUC comparison columns. Do NOT rank models by discrimination.

### 7C: Narrative Synthesis

3-4 sentences covering:
1. What converges across methods (strongest predictor agreement)
2. What logistic regression uniquely reveals (adjusted ORs, independent effects)
3. What trees uniquely reveal (nonlinear patterns, variable ranking confirmation)
4. Overall: convergence strengthens confidence in key finding

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, unique logistic insight, or tree confirmation.

## Validation Checkpoint

- [ ] Unified importance table with all predictors on 0-100 scale
- [ ] At least 3 methods represented in importance table
- [ ] Rank consensus column computed
- [ ] Insight synthesis table: one row per model family
- [ ] No AUC horse-race comparison between model families
- [ ] Narrative synthesis: 3-4 sentences covering convergence + unique insights
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out -> 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
unified_importance_table: [normalized 0-100 with rank consensus]
insight_table: [model family x unique insight]
results_para_comparison: [synthesis paragraph prose]
```
