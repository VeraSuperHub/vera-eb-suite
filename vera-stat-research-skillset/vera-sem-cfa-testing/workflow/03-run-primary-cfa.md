# 03 — Run Primary CFA + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: identification_status, estimator, scaling, factor structure from 02-check-measurement-setup.md

## Generate code for PART 2: Primary CFA Model

1. Fit the specified CFA in R (`lavaan::cfa`) and Python (`semopy`)
2. Extract and report global fit indices
3. Extract standardized factor loadings
4. Extract factor correlations (if multi-factor)
5. Produce loading table (sorted by factor, descending loading)
6. Produce path diagram or loading forest plot → `plot_02_cfa_loadings.png`
7. 3-sentence interpretation of model fit and loadings

### Reporting rules (always follow):
- Chi-square: chi-sq(df) = X.XX, p = .XXX
- CFI and TLI: report to 3 decimal places (e.g., CFI = .952)
- RMSEA: report with 90% CI, e.g., RMSEA = .062, 90% CI [.045, .079]
- SRMR: report to 3 decimal places
- Standardized loadings: report to 3 decimal places
- Fit interpretation thresholds: CFI/TLI >= .95 good, >= .90 acceptable; RMSEA <= .06 good, <= .08 acceptable; SRMR <= .08 good
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise

### Fit verdict logic:
```
if CFI >= .95 and RMSEA <= .06 and SRMR <= .08:
    verdict = "good fit"
elif CFI >= .90 and RMSEA <= .08 and SRMR <= .10:
    verdict = "acceptable fit"
else:
    verdict = "poor fit — consider model revisions"
```

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Reliability (omega, composite reliability, AVE)** — always include
2. **Discriminant validity (HTMT or Fornell-Larcker)** — include if multi-factor
3. **Modification indices** — always include with guardrails ("only free paths with theoretical justification")
4. **Measurement invariance** — include if grouping variable collected
5. **Alternative-factor models** — include if > 2 factors or if fit is poor

### Template:

```
── RECOMMENDED ADDITIONAL ANALYSES ──────────────────────
Based on your CFA results:

  [numbered list, 3-5 items, each with 2-line rationale]

→ Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
──────────────────────────────────────────────────────────
```

## Validation Checkpoint

- [ ] CFA model fitted without convergence errors
- [ ] Global fit indices reported (chi-sq, CFI, TLI, RMSEA+CI, SRMR)
- [ ] Standardized loadings table generated (all factors, sorted)
- [ ] Factor correlations reported (if multi-factor)
- [ ] plot_02 generated (path diagram or loading forest plot)
- [ ] Fit verdict stated in interpretation
- [ ] Recommendation block printed with 3-5 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── cfa_analysis.R
├── cfa_analysis.py
├── plot_01_correlation_heatmap.png (from Step 02 diagnostics)
└── plot_02_cfa_loadings.png
```
