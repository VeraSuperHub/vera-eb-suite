# 07 — Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md (Path A + Path B)

## Design Principle

Models are analytic lenses, not contestants. Path A (ignore ordering) and Path B
(respect ordering) each provide a different kind of insight. The comparison step
synthesizes what converges and what each path uniquely reveals. The dual-path
comparison itself is the key insight. Never frame as "which model is best."

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Unified Variable Importance Table (Dual-Path)

Normalize all importance measures to a 0-100 scale (max = 100):

**Path A columns** (ignore ordering):
- Multinomial logistic: |standardized coefficients| averaged across class contrasts, rescaled
- Random Forest: permutation importance rescaled
- LightGBM: gain-based importance rescaled

**Path B columns** (respect ordering):
- Proportional odds: |standardized coefficients| rescaled
- Random Forest: permutation importance rescaled (same RF, but comparison is the point)
- LightGBM: gain-based importance rescaled

```
| Variable | A: Multinom |std| | A: RF Imp | A: LGBM Imp | B: Prop Odds |std| | B: RF Imp | B: LGBM Imp | Path A Avg Rank | Path B Avg Rank | Overall Rank |
|----------|---------------------|-----------|-------------|----------------------|-----------|-------------|-----------------|-----------------|--------------|
| var1     | 100                 | 95        | 88          | 100                  | 92        | 85          | 1               | 1               | 1            |
| var2     | 67                  | 72        | 70          | 55                   | 68        | 74          | 2               | 2               | 2            |
| ...      | ...                 | ...       | ...         | ...                  | ...       | ...         | ...             | ...             | ...          |
```

- Path A Avg Rank = average rank across the three Path A columns
- Path B Avg Rank = average rank across the three Path B columns
- Overall Rank = average of Path A Avg Rank and Path B Avg Rank

### 7B: Dual-Path Convergence Analysis

Key questions to answer:

1. **Do Path A and Path B agree on variable importance rankings?**
   - Compute Spearman rank correlation between Path A Avg Rank and Path B Avg Rank
   - High correlation → ordering does not change the importance story
   - Low correlation → ordering reveals different predictor dynamics

2. **What does proportional odds uniquely reveal?**
   - Cumulative OR interpretation: effect on movement across all thresholds
   - Direction and magnitude of ordinal shift per predictor

3. **What do adjacent-category and continuation-ratio add?**
   - Adjacent-category: which specific level transitions does the predictor influence most?
   - Continuation-ratio: for sequential/progressive outcomes, which stage transitions matter?
   - Compare: does the predictor matter equally across all transitions, or concentrated at specific jumps?

4. **When proportional odds assumption fails, what does the stereotype model show?**
   - Which predictors have non-proportional effects?
   - Do scaling parameters reveal where the ordinal structure is violated?
   - Does the stereotype model recover ordinal structure that proportional odds misses?

5. **What do trees/LightGBM confirm nonparametrically?**
   - Consistency of importance ranking without distributional assumptions
   - LightGBM Path A (multi-class) vs. Path B (regression/ordinal): does the objective change importance?
   - Any nonlinear patterns from CART that parametric models miss?

### 7C: Insight Synthesis Table

One row per model family, focus on *what it reveals*:

```
| Path | Method                    | Unique Insight                                                  |
|------|---------------------------|-----------------------------------------------------------------|
| A    | Multinomial Logistic      | [class-specific ORs: which predictors separate specific levels] |
| A    | RF / LightGBM (multi)     | [importance ranking when ordering ignored]                      |
| B    | Proportional Odds         | [cumulative ORs, monotonic effect across all thresholds]        |
| B    | Adjacent-Category         | [which level transitions the predictor influences most]         |
| B    | Continuation-Ratio        | [stage-specific progression dynamics]                           |
| B    | Stereotype                | [where proportional odds breaks, scaled ordinal effects]        |
| B    | RF / LightGBM (ordinal)   | [importance ranking when ordering respected]                    |
| A+B  | Convergence               | [what both paths agree on — strongest finding]                  |
```

Do NOT include accuracy comparison columns. Do NOT rank models by fit.

### 7D: Narrative Synthesis

4-6 sentences covering:
1. What converges across both paths (strongest predictor agreement, rank correlation)
2. What the proportional odds model uniquely reveals (cumulative OR interpretation, assumption status)
3. What adjacent-category and continuation-ratio uniquely add (transition-specific insights)
4. When proportional odds fails: what the stereotype model shows
5. What trees/LightGBM confirm nonparametrically (importance hierarchy, nonlinear patterns)
6. Overall: dual-path convergence strengthens confidence in key finding

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison and dual-path sections).
Rotate lead-in: convergence finding, unique proportional odds insight, transition-specific finding, or tree confirmation.

## Validation Checkpoint

- [ ] Unified importance table with all predictors on 0-100 scale, both Path A and Path B columns
- [ ] At least 6 importance columns (3 per path) represented
- [ ] Path A Avg Rank, Path B Avg Rank, and Overall Rank computed
- [ ] Spearman rank correlation between Path A and Path B reported
- [ ] Adjacent-category and continuation-ratio insights synthesized
- [ ] Stereotype model insight included (especially if Brant test violated)
- [ ] Insight synthesis table: one row per model family, Path column included
- [ ] No accuracy horse-race comparison between model families
- [ ] Narrative synthesis: 4-6 sentences covering convergence + unique insights from both paths
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
unified_importance_table: [normalized 0-100 with dual-path ranks]
insight_table: [path × model family × unique insight]
convergence_analysis: [Path A vs Path B rank correlation and interpretation]
results_para_comparison: [dual-path synthesis paragraph prose]
```
