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
- Multinomial logistic: |standardized coefficients| averaged across all non-reference classes, rescaled
- LDA: |discriminant function loadings| (from structure matrix), rescaled
- Random Forest: mean decrease in Gini/accuracy, rescaled
- LightGBM: feature_importance(importance_type='gain'), rescaled

```
| Variable | Multinomial (|avg std coef|) | LDA (|loadings|) | RF Importance | LightGBM Importance | Rank Consensus |
|----------|----------------------------|-------------------|---------------|---------------------|----------------|
| var1     | 100                        | 85                | 100           | 92                  | 1              |
| var2     | 67                         | 100               | 72            | 78                  | 2              |
| ...      | ...                        | ...               | ...           | ...                 | ...            |
```

Rank consensus = average rank across all four methods.

### 7B: Insight Synthesis Table

One row per model family, focus on *what it reveals*:

```
| Method                  | Unique Insight                                              |
|-------------------------|-------------------------------------------------------------|
| Multinomial Logistic    | [which predictors differentiate which classes, RRR direction]|
| LDA                     | [discriminant dimensions, separation quality]               |
| CART                    | [primary splits, interpretable rules]                       |
| Random Forest / LightGBM| [importance ranking, nonlinear patterns]                    |
```

Do NOT include accuracy comparison columns as the primary comparison. Do NOT rank models by fit.

### 7C: Classification Agreement Table (Optional)
- Cross-tabulate predictions from multinomial logistic vs RF
- Identify cases where models disagree — these are the ambiguous cases
- Note which classes have highest agreement/disagreement

### 7D: Narrative Synthesis

3-4 sentences covering:
1. What converges across methods (strongest predictor agreement across all 4)
2. What multinomial logistic uniquely reveals (class-specific direction via RRR)
3. What LDA uniquely reveals (discriminant dimensions, separation quality)
4. What trees uniquely reveal (nonlinear patterns, interaction-like splits, importance confirmation)
5. Overall: convergence strengthens confidence in key predictors

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, unique multinomial insight, LDA dimension, or tree confirmation.

## Validation Checkpoint

- [ ] Unified importance table with all predictors on 0-100 scale
- [ ] At least 4 methods represented in importance table (multinomial, LDA, RF, LightGBM)
- [ ] Rank consensus column computed
- [ ] Insight synthesis table: one row per model family
- [ ] No accuracy horse-race comparison between model families
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
