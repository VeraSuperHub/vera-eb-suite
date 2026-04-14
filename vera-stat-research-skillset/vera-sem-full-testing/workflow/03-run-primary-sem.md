# 03 — Run Primary SEM + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: estimator, structural specification, measurement model from 02-check-model-setup.md

## Generate code for PART 2: Primary SEM

1. Fit one theory-led SEM in R (`lavaan::sem`) and Python (`semopy`)
2. Extract and report global fit indices
3. Extract standardized structural path coefficients
4. Extract factor loadings (measurement model transparency)
5. Extract R-squared for endogenous latent variables
6. Produce path coefficient table (standardized beta, SE, p, 95% CI)
7. Produce SEM path diagram → `plot_02_sem_path.png`
8. 3-sentence interpretation of structural findings

### Reporting rules (always follow):
- Chi-square: chi-sq(df) = X.XX, p = .XXX
- CFI and TLI: report to 3 decimal places
- RMSEA: report with 90% CI
- SRMR: report to 3 decimal places
- Path coefficients: standardized beta to 3 decimals, with p-value
- R-squared: to 3 decimal places for each endogenous variable
- Fit interpretation: same thresholds as CFA (CFI >= .95, RMSEA <= .06, SRMR <= .08 = good)
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise

### Path interpretation template:
```
"[Predictor] had a [significant/non-significant] [positive/negative] effect
on [Outcome] (beta = .XXX, p = .XXX), controlling for [other predictors]."
```

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Indirect effects with bootstrap CIs** — always include if mediators present
2. **Multigroup SEM** — include if grouping variable collected
3. **Competing structural models** — always include (nested model comparison)
4. **Residual diagnostics / modification indices** — always include with guardrails
5. **Effect decomposition (total, direct, indirect)** — include if mediators present

### Template:

```
── RECOMMENDED ADDITIONAL ANALYSES ──────────────────────
Based on your SEM results:

  [numbered list, 3-5 items, each with 2-line rationale]

→ Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
──────────────────────────────────────────────────────────
```

## Validation Checkpoint

- [ ] SEM fitted without convergence errors or Heywood cases
- [ ] Global fit indices reported (chi-sq, CFI, TLI, RMSEA+CI, SRMR)
- [ ] Structural path table generated (beta, SE, p, CI)
- [ ] Factor loadings reported for measurement transparency
- [ ] R-squared reported for endogenous variables
- [ ] plot_02 generated (SEM path diagram)
- [ ] Interpretation includes fit verdict + key structural findings
- [ ] Recommendation block printed with 3-5 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── sem_analysis.R
├── sem_analysis.py
├── plot_01_measurement_check.png (from Step 02)
└── plot_02_sem_path.png
```
