# 04 — Run Additional Tests

## Executor: Main Agent (code generation)

## Data In: PART 0-2 code from vera-stat-timeseries-testing output

## Prerequisite: Testing workflow (PART 0-2) already executed.

## Generate code for PART 3: Additional Tests

### 4A: Seasonal ARIMA (SARIMA)
If seasonal pattern was detected (seasonal_detected == TRUE):
1. Fit SARIMA using auto.arima with `seasonal=TRUE`
   - R: `forecast::auto.arima(y, seasonal=TRUE, stepwise=FALSE)`
   - Python: `pmdarima.auto_arima(y, seasonal=True, m=frequency)`
2. Report full notation: ARIMA(p,d,q)(P,D,Q)[s]
3. Report AIC, BIC
4. Ljung-Box on residuals
5. Compare AIC with non-seasonal ARIMA from testing workflow

### 4B: Exponential Smoothing (ETS / Holt-Winters)
1. Fit ETS with automatic model selection
   - R: `forecast::ets(y)` — selects error, trend, seasonal components
   - Python: `statsmodels.tsa.holtwinters.ExponentialSmoothing` with optimized params
2. Report selected model: ETS(E,T,S) where E=error, T=trend, S=seasonal
3. Report AIC, BIC
4. Smoothing parameters (alpha, beta, gamma)
5. Ljung-Box on residuals

### 4C: Structural Break Tests
1. **CUSUM test** (cumulative sum of residuals)
   - R: `strucchange::efp()` + `sctest()`
   - Python: `statsmodels.stats.diagnostic.breaks_cusumolsresid()`
   - Report test statistic and p-value
   - Plot CUSUM with 5% critical bounds → `plot_03_cusum.png`
2. **Chow test** (if known break date provided)
   - Split series at break point, test for parameter stability
   - Report F statistic and p-value
3. Interpret: significant → "structural instability detected at [date/period]"

### 4D: Granger Causality (if exogenous variable present)
If exogenous variable(s) were provided:
1. Granger causality test: does X Granger-cause Y?
   - Test at lags 1 through min(12, N/10)
   - R: `lmtest::grangertest()`
   - Python: `statsmodels.tsa.stattools.grangercausalitytests()`
2. Report F statistic and p-value at optimal lag (AIC-selected)
3. Also test reverse: does Y Granger-cause X?
4. Interpret direction(s) of Granger causality

### Quality: Apply sentence bank from `reference/patterns/sentence-bank.md`
- Vary whether AIC comparison or diagnostic adequacy leads the SARIMA sentence
- Vary whether ETS components or smoothing parameters are emphasized
- Vary whether structural break is inline or standalone paragraph
- Include 0-1 methodological justifications per test (only when relevant)

## Validation Checkpoint

- [ ] SARIMA fitted with full notation reported (if seasonal)
- [ ] ETS fitted with model specification and smoothing parameters
- [ ] CUSUM test reported with statistic and p
- [ ] CUSUM plot generated (if applicable)
- [ ] Chow test reported (if break date provided)
- [ ] Granger causality reported (if exogenous variable present)
- [ ] AIC/BIC reported for all fitted models
- [ ] Ljung-Box on residuals for each model
- [ ] Sentence bank applied (no repeated phrasing patterns)

## Data Out → 05-analyze-subgroups.md

```
additional_tests_code_r: [PART 3 R code block]
additional_tests_code_py: [PART 3 Python code block]
methods_para_sarima: [methods paragraph prose]
methods_para_ets: [methods paragraph prose]
methods_para_breaks: [methods paragraph prose]
methods_para_granger: [methods paragraph prose]
results_para_additional: [results paragraph prose]
plots: [list of new plot filenames]
tables: [list of new table data]
```
