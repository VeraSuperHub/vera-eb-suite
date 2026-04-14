# 02 — Check Distribution (Time Series Diagnostics)

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Time Plot
- Plot the raw series over time (x = time index, y = series value)
- Include a LOESS/lowess smoother to visualize trend
- Note any obvious patterns: trend, seasonality, level shifts, outliers

### Descriptive Statistics
- Mean, SD, Min, Max, N (number of time points)
- First and last observation dates
- Number of missing values

### ACF and PACF Plots
- Autocorrelation function (ACF) up to lag = min(N/4, 40)
- Partial autocorrelation function (PACF) up to same max lag
- Note: significant spikes at seasonal lags (e.g., lag 12 for monthly) suggest seasonality

### Seasonal Decomposition
- If frequency is known (monthly=12, quarterly=4, etc.):
  - Classical decomposition or STL decomposition
  - Separate into: trend + seasonal + residual components
  - Plot all three components
- If frequency is 1 (annual) or unknown: skip decomposition, note in output

### Stationarity Tests
1. **Augmented Dickey-Fuller (ADF)**
   - Null: series has a unit root (non-stationary)
   - Report: test statistic, p-value, lags used
   - Stationary if p < .05

2. **KPSS (Kwiatkowski-Phillips-Schmidt-Shin)**
   - Null: series is stationary
   - Report: test statistic, p-value
   - Stationary if p >= .05

### Decision Logic (printed in console)

```
if ADF p < 0.05 AND KPSS p >= 0.05:
    → "Series is stationary. ARIMA(p,0,q) appropriate."
    → stationarity_flag = TRUE, d = 0
elif ADF p >= 0.05 AND KPSS p < 0.05:
    → "Series is non-stationary. Differencing required."
    → stationarity_flag = FALSE
    → Apply first difference, retest ADF/KPSS
    → If stationary after 1 diff: d = 1
    → If still non-stationary: d = 2, retest
elif ADF p < 0.05 AND KPSS p < 0.05:
    → "Conflicting results. Proceed with d=1 as conservative choice."
    → stationarity_flag = FALSE, d = 1
else:
    → "Both tests suggest stationarity. ARIMA(p,0,q) appropriate."
    → stationarity_flag = TRUE, d = 0
```

### If non-stationary: show differenced series
- Plot the differenced series
- Re-run ADF on differenced series to confirm stationarity
- Show ACF/PACF of differenced series (for model order selection)

### Plot Assembly
- Save as `plot_01_ts_diagnostics.png`
- Layout: 2x3 or 3x2 grid (time plot, ACF, PACF, decomposition trend, decomposition seasonal, decomposition residual)
- If no decomposition: 1x3 (time plot, ACF, PACF)
- 14x10 inches, 300 DPI

### Interpretation
Print 3-4 sentences: series characteristics (trend, seasonality, stationarity test results), differencing decision, and what the ACF/PACF patterns suggest for model order.

## Validation Checkpoint

- [ ] Time plot generated showing raw series
- [ ] Descriptive stats complete (M, SD, min, max, N)
- [ ] ACF plot generated with significance bands
- [ ] PACF plot generated with significance bands
- [ ] Seasonal decomposition performed (if frequency > 1)
- [ ] ADF test statistic and p reported
- [ ] KPSS test statistic and p reported
- [ ] stationarity_flag set (TRUE/FALSE)
- [ ] Differencing order d determined
- [ ] If differenced: differenced series ACF/PACF shown
- [ ] plot_01_ts_diagnostics.png generated
- [ ] Decision statement printed

## Data Out → 03-run-primary-test.md

```
stationarity_flag: TRUE | FALSE
d: 0 | 1 | 2
seasonal_detected: TRUE | FALSE
seasonal_period: {12 | 4 | 7 | ...} or null
descriptives: {mean, sd, min, max, n, start, end}
acf_significant_lags: [list]
pacf_significant_lags: [list]
diagnostics_code_r: [PART 1 R code block]
diagnostics_code_py: [PART 1 Python code block]
```
