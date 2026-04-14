# 07 — Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md

## Design Principle

Models are analytic lenses, not contestants. Each model type makes different
assumptions and provides a different kind of insight. The comparison step
synthesizes what converges and what each uniquely reveals.
Never frame as "which model is best."

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Assumption Comparison Table

One row per model, focus on what each assumes and what it relaxes:

```
| Method                  | Sphericity | Balanced | Missing Data | Individual Trajectories | Distributional Assumptions |
|-------------------------|------------|----------|--------------|------------------------|---------------------------|
| RM-ANOVA / Mixed ANOVA  | Required   | Required | Complete cases | No                     | Normal residuals           |
| LMM random intercept    | Not needed | Relaxed  | MAR          | Intercepts differ       | Normal residuals + RE      |
| LMM random slope        | Not needed | Relaxed  | MAR          | Intercepts + slopes differ | Normal residuals + RE   |
| GEE                     | Not needed | Relaxed  | MCAR (or weighted) | No (population-averaged) | None (robust SE)       |
| Tree-based              | N/A        | N/A      | Subject-level only | Via engineered features | None                   |
```

Do NOT rank these. Present as "which assumptions does each make."

### 7B: LMM Model Comparison Table

Compare within the LMM family only (this is valid because same likelihood framework):

```
| Model              | AIC    | BIC    | LogLik  | n_params | Notes                          |
|--------------------|--------|--------|---------|----------|--------------------------------|
| Random intercept   | [val]  | [val]  | [val]   | [val]    | Baseline                       |
| Random slope       | [val]  | [val]  | [val]   | [val]    | LR test: chi2=[val], p=[val]   |
| Growth curve (quad)| [val]  | [val]  | [val]   | [val]    | Quadratic time                 |
```

Frame as "which random effect structure fits the data" — not "which wins."

### 7C: Unified Variable Importance Table

Normalize all importance measures to a 0-100 scale (max = 100):
- LMM: |standardized fixed effect coefficients| rescaled
- Random Forest: permutation importance rescaled (on subject-level features)
- LightGBM: feature_importance(importance_type='gain') rescaled (on subject-level features)

```
| Variable        | LMM (|std coef|) | RF Importance | LightGBM Importance | Rank Consensus |
|-----------------|-------------------|---------------|---------------------|----------------|
| time            | [val]             | [val]         | [val]               | [rank]         |
| group           | [val]             | [val]         | [val]               | [rank]         |
| time x group    | [val]             | [val]         | [val]               | [rank]         |
| ...             | ...               | ...           | ...                 | ...            |
```

Rank consensus = average rank across all methods.

Note: LMM importance is on observation-level predictors, tree importance is on
subject-level engineered features. Acknowledge this difference in interpretation.

### 7D: Key Insight — Do LMM Fixed Effects and Tree Importance Agree?

1. What converges: which variables are important across both parametric and nonparametric approaches?
2. What diverges: any variable ranked high by trees but not LMM (or vice versa)? Why?
3. What GEE adds: do population-averaged and subject-specific effects tell the same story?

### 7E: Narrative Synthesis

3-4 sentences covering:
1. What converges across methods (strongest predictor/effect agreement)
2. What LMM uniquely reveals (individual trajectory differences, random effects structure)
3. What GEE uniquely reveals (population-averaged interpretation, robustness)
4. What trees uniquely reveal (nonlinear patterns, variable ranking on subject summaries)
5. Overall: convergence strengthens confidence in key finding

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, unique LMM insight, GEE comparison, or tree confirmation.

## Validation Checkpoint

- [ ] Assumption comparison table with all model families
- [ ] LMM model comparison table with AIC/BIC/LogLik (within LMM family only)
- [ ] LR test result for random slope vs random intercept included
- [ ] Unified importance table with all predictors on 0-100 scale
- [ ] At least 3 methods represented in importance table
- [ ] Rank consensus column computed
- [ ] No R-squared horse-race comparison between model families
- [ ] No "best model" language — models are lenses
- [ ] Key insight narrative covers convergence + unique insights
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
assumption_table: [model x assumption matrix]
lmm_comparison_table: [AIC/BIC within LMM family]
unified_importance_table: [normalized 0-100 with rank consensus]
results_para_comparison: [synthesis paragraph prose]
```
