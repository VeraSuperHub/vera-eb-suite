# 07 — Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md

## Design Principle

Models are analytic lenses, not contestants. Each estimation method addresses a
different assumption about the data-generating process. The comparison step
synthesizes what converges and what each uniquely reveals about the pooled
effect and its uncertainty. Never frame as "which model is best."

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Model Comparison Table

Side-by-side comparison of all fitted models:

```
| Method          | Pooled ES | 95% CI       | Test Stat | p     | tau²  |
|-----------------|-----------|--------------|-----------|-------|-------|
| Fixed-effects   | X.XX      | [X.XX, X.XX] | z = X.XX  | .XXX  | --    |
| RE (DL)         | X.XX      | [X.XX, X.XX] | z = X.XX  | .XXX  | X.XX  |
| RE (REML)       | X.XX      | [X.XX, X.XX] | z = X.XX  | .XXX  | X.XX  |
| Knapp-Hartung   | X.XX      | [X.XX, X.XX] | t = X.XX  | .XXX  | X.XX  |
| Bayesian        | X.XX      | [X.XX, X.XX] | --        | --    | X.XX  |
```

Key comparisons:
- Do fixed and random estimates diverge? If yes → heterogeneity matters
- Do DL and REML tau² estimates differ? REML generally more accurate
- Is the Knapp-Hartung CI materially wider? If yes → standard z-based CI was overconfident
- Does Bayesian posterior differ from frequentist? If yes → prior influence or small-k instability

### 7B: Robustness Summary

One row per analytic decision, showing whether the main conclusion is sensitive:

```
| Decision               | Sensitivity                                    |
|------------------------|------------------------------------------------|
| FE vs RE               | [same direction/significance? or divergent?]   |
| DL vs REML estimator   | [tau² similar? CI similar?]                    |
| Standard vs Knapp-Hartung | [CI change clinically meaningful?]           |
| Frequentist vs Bayesian | [posterior consistent with REML?]              |
| Before vs after trim-fill | [adjusted ES materially different?]          |
| With vs without influential study | [if flagged in step 04]           |
```

### 7C: Narrative Synthesis

3-4 sentences covering:
1. Convergence: do all models point to the same direction and approximate magnitude?
2. Heterogeneity sensitivity: does the choice of tau² estimator matter?
3. Confidence interval sensitivity: Knapp-Hartung vs standard — is the conclusion robust?
4. Overall: is the pooled estimate robust across analytic choices?

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, CI sensitivity, or Bayesian comparison.

## Validation Checkpoint

- [ ] Model comparison table with all fitted models
- [ ] Fixed vs random divergence assessed
- [ ] DL vs REML tau² compared
- [ ] Knapp-Hartung CI width compared to standard
- [ ] Bayesian posterior compared to frequentist
- [ ] Robustness summary table completed
- [ ] Narrative synthesis: 3-4 sentences covering convergence + sensitivity
- [ ] No R² horse-race or "best model" framing
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
model_comparison_table: [all models side-by-side]
robustness_table: [decision × sensitivity]
results_para_comparison: [synthesis paragraph prose]
```
