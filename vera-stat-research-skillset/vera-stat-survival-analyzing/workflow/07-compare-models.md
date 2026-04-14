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
- Cox: |standardized coefficient| (log-HR × SD of predictor) rescaled
- RSF: permutation importance rescaled
- Gradient Boosting: feature importance rescaled

```
| Variable | Cox (|std coef|) | RSF Importance | GBM Importance | Rank Consensus |
|----------|------------------|----------------|----------------|----------------|
| var1     | 100              | 100            | 85             | 1              |
| var2     | 67               | 72             | 100            | 2              |
| ...      | ...              | ...            | ...            | ...            |
```

Rank consensus = average rank across all three methods.

### 7B: Insight Synthesis Table

One row per model family, focus on *what it reveals*:

```
| Method              | Unique Insight                                              |
|---------------------|-------------------------------------------------------------|
| Cox PH              | [adjusted HRs, independence, PH status]                     |
| AFT                 | [time ratios, distributional fit, intuitive interpretation] |
| RSF / Tree-Based    | [nonlinear effects, interactions, importance confirmation]  |
```

Do NOT include concordance comparison columns for ranking. Do NOT rank models by fit.

### 7C: Narrative Synthesis

3-4 sentences covering:
1. What converges: do Cox HRs and RSF importance rankings agree?
2. What AFT uniquely reveals: time ratios may be more intuitive for some audiences; distributional fit assessment
3. What trees uniquely reveal: nonlinear effects, interaction detection, importance confirmation
4. PH assumption status: if violated, how AFT and stratification provide robustness

### Key insight question: Do Cox HRs and RSF importance rankings agree?
- If yes → strong evidence for the identified risk factors
- If divergence → discuss which predictors differ and why (nonlinear effects, interactions)

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, unique AFT insight, tree confirmation, or PH discussion.

## Validation Checkpoint

- [ ] Unified importance table with all predictors on 0-100 scale
- [ ] At least 3 methods represented in importance table
- [ ] Rank consensus column computed
- [ ] Insight synthesis table: one row per model family
- [ ] No concordance horse-race comparison between model families
- [ ] Narrative synthesis: 3-4 sentences covering convergence + unique insights
- [ ] PH assumption status addressed in synthesis
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
unified_importance_table: [normalized 0-100 with rank consensus]
insight_table: [model family × unique insight]
results_para_comparison: [synthesis paragraph prose]
```
