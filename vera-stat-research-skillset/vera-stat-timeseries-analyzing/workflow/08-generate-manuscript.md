# 08 — Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Statistical Analysis

[Para 1: Data description — series length, frequency, time span, preprocessing]
[Para 2: Stationarity assessment — ADF, KPSS, differencing decision]
[Para 3: ARIMA/SARIMA — order selection method, diagnostic criteria]
[Para 4: Exponential smoothing — ETS framework, automatic selection]
[Para 5: GARCH — conditional on ARCH effects, specification]
[Para 6: VAR and Granger causality — if exogenous, lag selection, causality testing]
[Para 7: Spectral analysis — periodogram, smoothing kernel, frequency interpretation]
[Para 8: ML-based models — feature engineering, RF, LightGBM, exploratory framing]
[Para 9: Model comparison — hold-out strategy, accuracy metrics, lens framing]
[Para 10: Software — R version, Python version, key packages with versions]
```

### Rules
- Write as if a human analyst chose these methods for THIS specific study
- Never expose general decision rules or pipeline logic
- State what was done + why + key parameters
- No results in methods; no code in methods
- Cite methodological references where appropriate
- Follow `reference/rules/reporting-standards.md`

### Quality: Methods variation
Apply paragraph-level randomization per `reference/specs/output-variation-protocol.md`:
- Each paragraph selects one framing from 3 options (test-first, purpose-first, data-first)
- Vary passive vs active voice across paragraphs (not within)
- Vary whether CI level and alpha are stated explicitly or implied
- Vary whether Box-Jenkins or Hyndman-Athanasopoulos framework language is used

## Assemble results.md

### Section ordering logic

Choose ONE ordering based on research question emphasis:
- **Order A (forecast-driven):** ARIMA → SARIMA → ETS → GARCH → VAR → Spectral → ML → Comparison
- **Order B (dynamics-driven):** Stationarity → Spectral → ARIMA → GARCH → VAR → ETS → ML → Comparison
- **Order C (exploratory-driven):** Decomposition → Subseries → ML → ARIMA → ETS → VAR → Spectral → Comparison

Select: "what will happen next" → A. "what drives the dynamics" → B. "what patterns exist" → C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`

## Generate references.bib

Required references (include only those actually cited):
- Box, G. E. P., & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control*
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.)
- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. *Journal of Econometrics*
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*
- Dickey, D. A., & Fuller, W. A. (1979). Distribution of the estimators...
- Kwiatkowski, D., et al. (1992). Testing the null hypothesis of stationarity...
- Holt, C. C. (2004). Forecasting seasonals and trends by exponentially weighted moving averages
- Winters, P. R. (1960). Forecasting sales by exponentially weighted moving averages
- Ljung, G. M., & Box, G. E. P. (1978). On a measure of lack of fit...
- Granger, C. W. J. (1969). Investigating causal relations by econometric models...
- Breiman, L. (2001). Random forests. *Machine Learning*
- Software citations (R, Python, statsmodels, forecast, pmdarima, arch, etc.)

BibTeX format. Include ONLY references actually cited in methods.md or results.md.
Do NOT pad with uncited references.

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 8-10 paragraphs covering all analysis steps
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values — all numbers are computed
- [ ] All table/figure references in text match actual files
- [ ] Model notation always ARIMA(p,d,q)(P,D,Q)[s] for seasonal
- [ ] p-value formatting follows reporting-standards.md rules
- [ ] AIC/BIC reported for all fitted models
- [ ] Ljung-Box reported for all residual diagnostics
- [ ] Forecast accuracy framed as "which assumptions fit" not "which wins"
- [ ] references.bib includes all cited works and no uncited works
- [ ] Code style variation applied to final code.R and code.py
- [ ] No meta-commentary about pipeline structure in any output file
- [ ] Sentence bank applied with no repeated phrasing patterns

## Data Out → Final Deliverables

```
Deliverables:
├── {ts_var}_timeseries.R          (PARTS 0-6, style-varied)
├── {ts_var}_timeseries.py         (PARTS 0-6, style-varied)
├── methods.md                     (manuscript Methods section)
├── results.md                     (manuscript Results section)
├── references.bib                 (cited works only)
├── tables/
│   ├── model_comparison.csv       (MAE, RMSE, MAPE, AIC per model)
│   ├── arima_coefficients.csv
│   ├── var_coefficients.csv       (if applicable)
│   ├── garch_parameters.csv       (if applicable)
│   └── ml_importance.csv
└── figures/
    ├── plot_01_ts_diagnostics.png
    ├── plot_02_forecast.png
    ├── plot_03_cusum.png           (if structural break tested)
    ├── plot_04_subseries.png       (if periodic)
    ├── plot_05_rolling_stats.png
    ├── plot_06_rolling_coefs.png
    ├── plot_07_regimes.png         (if regime detection)
    ├── plot_08_arima_diagnostics.png
    ├── plot_09_garch_variance.png  (if GARCH fitted)
    ├── plot_10_irf.png             (if VAR fitted)
    ├── plot_11_spectral.png
    ├── plot_12_ml_importance.png
    └── plot_13_forecast_comparison.png
```
