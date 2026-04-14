# Skill Routing Table

Maps confirmed outcome type to the appropriate testing and analyzing skill paths.

All paths are relative to the current StatResearch project root, discovered at runtime via REPO_ROOT (see step04-parallel.md for discovery logic).

## Routing Table

| Outcome Type | Testing Skill Directory | Analyzing Skill Directory | Analyzing SKILL.md Name | Key Methods |
|---|---|---|---|---|
| continuous | `vera-stat-continuous-testing/` | `vera-stat-analysis-engine/continuous/vera-stat-continuous-analyzing/` | vera-stat-continuous-analyzing | OLS, quantile regression, CART/RF/LightGBM |
| binary | `vera-stat-binary-testing/` | `vera-stat-analysis-engine/binary/vera-stat-binary-analyzing/` | vera-stat-binary-analyzing | Logistic regression, ROC, trees |
| ordinal | `vera-stat-ordinal-testing/` | `vera-stat-analysis-engine/ordinal/vera-stat-ordinal-analyzing/` | vera-stat-ordinal-analyzing | Proportional odds, adjacent-category, trees (dual-path) |
| nominal | `vera-stat-nominal-testing/` | `vera-stat-analysis-engine/nominal/vera-stat-nominal-analyzing/` | vera-stat-nominal-analyzing | Multinomial logistic, LDA, trees |
| count | `vera-stat-count-testing/` | `vera-stat-analysis-engine/count/vera-stat-count-analyzing/` | vera-stat-count-analyzing | Poisson, NB, ZIP, ZINB, hurdle |
| survival | `vera-stat-survival-testing/` | `vera-stat-analysis-engine/survival/vera-stat-survival-analyzing/` | vera-stat-survival-analyzing | Cox PH, AFT, random survival forest |
| repeated | `vera-stat-repeated-testing/` | `vera-stat-analysis-engine/repeated/vera-stat-repeated-analyzing/` | vera-stat-repeated-analyzing | Mixed models, GEE, growth curves |
| timeseries | `vera-stat-timeseries-testing/` | `vera-stat-analysis-engine/timeseries/vera-stat-timeseries-analyzing/` | vera-stat-timeseries-analyzing | ARIMA, SARIMA, GARCH, spectral, ML forecasting |
| multivariate | `vera-stat-multivariate-testing/` | `vera-stat-analysis-engine/multivariate/vera-stat-multivariate-analyzing/` | vera-stat-multivariate-analyzing | MANOVA, canonical correlation, PCA |
| doe | `vera-stat-doe-testing/` | `vera-stat-analysis-engine/doe/vera-stat-doe-analyzing/` | vera-stat-doe-analyzing | Factorial ANOVA, RSM, Taguchi, power analysis |
| meta | `vera-stat-meta-testing/` | `vera-stat-analysis-engine/meta/vera-stat-meta-analyzing/` | vera-stat-meta-analyzing | Fixed/random effects, meta-regression, forest plots |
| sem-cfa | `vera-sem-cfa-testing/` | `vera-stat-analysis-engine/sem-cfa/vera-sem-cfa-analyzing/` | vera-sem-cfa-analyzing | CFA, fit indices, modification indices |
| sem-full | `vera-sem-full-testing/` | `vera-stat-analysis-engine/sem-full/vera-sem-full-analyzing/` | vera-sem-full-analyzing | Full SEM, mediation, moderation, multi-group |
| sem-longchange | `vera-sem-longchange-testing/` | `vera-stat-analysis-engine/sem-longchange/vera-sem-longchange-analyzing/` | vera-sem-longchange-analyzing | Latent growth curves, longitudinal SEM |

## Workflow Files Available Per Skill

Each routed testing skill contains:
```
workflow/
├── 01-collect-inputs.md      ← Pre-populated by pipeline (skip interactive)
├── 02-check-distribution.md  ← Distribution diagnostics
├── 03-run-primary-test.md    ← Primary hypothesis tests
```

Each routed analyzing skill contains:
```
workflow/
├── 04-run-additional-tests.md ← Extended test battery
├── 05-analyze-subgroups.md   ← Stratified + interaction analysis
├── 06-fit-models.md          ← Regression + trees + alternatives
├── 07-compare-models.md      ← Cross-method synthesis
└── 08-generate-manuscript.md ← methods.md + results.md assembly
```

## Reference Files Available Per Skill

```
reference/
├── specs/
│   ├── output-variation-protocol.md    ← output quality variation
│   └── code-style-variation.md    ← 7-dimension code variation
├── rules/
│   └── reporting-standards.md ← Hard reporting rules
└── patterns/
    └── sentence-bank.md       ← 4-6 phrasings per result type
```

## How the Pipeline Uses This Table

1. Step 02 confirms the outcome type
2. Record BOTH the testing-skill path and the analyzing-skill path
3. Step 04 reads the routed testing skill for `T1_primary`
4. Step 04 reads the routed analyzing skill for downstream tracks (`T2+`)
5. Track outputs follow the analyzing skill's output format
6. Output Quality Variation references are read from the analyzing skill's `reference/` directory
