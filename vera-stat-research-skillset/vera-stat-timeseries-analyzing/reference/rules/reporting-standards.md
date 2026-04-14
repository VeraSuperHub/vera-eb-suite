# Reporting Standards — Hard Rules

Apply to ALL output. Never violate.

1. **p-values**: Never "p = 0.000" → use "p < .001". Exact to 3 decimals otherwise.
2. **Non-significance**: Never "no effect" → "not statistically significant at alpha = [level]"
3. **ADF test**: Always report test statistic, p-value, and number of lags used.
4. **KPSS test**: Always report test statistic, p-value, and bandwidth.
5. **Model notation**: Always ARIMA(p,d,q) for non-seasonal, ARIMA(p,d,q)(P,D,Q)[s] for seasonal.
6. **Information criteria**: Report AIC and BIC for every fitted model.
7. **Ljung-Box**: Report Q statistic, lag tested, and p-value for every model's residuals.
8. **Coefficients**: Report with standard errors always. Include 95% CI when space permits.
9. **Forecast intervals**: Report both 80% and 95% prediction intervals.
10. **Accuracy metrics**: Report MAE, RMSE, and MAPE. State whether on training or hold-out.
11. **GARCH**: Report ARCH-LM test before fitting. Report omega, alpha, beta, and persistence.
12. **VAR**: Report lag selection criteria used (AIC/BIC/HQ). Report Granger causality p-values.
13. **Spectral**: Report dominant frequency, corresponding period in original time units, and spectral power.
14. **Sample size**: Report number of time points (T), frequency, and time span.
15. **Decimal places**: 2 for coefficients/SEs, 3 for p-values, 2 for AIC/BIC (or integer), 2 for accuracy metrics.
16. **Differencing**: State order of differencing and justification (ADF/KPSS results).
17. **Tree-based**: Frame as "exploratory" or "complementary." Never claim superiority over statistical models for time series.
18. **Hold-out**: State the split ratio and number of observations in training vs test.

## Visualization Standards

| Plot | When | Purpose |
|---|---|---|
| Time plot | Always | Raw series visualization |
| ACF/PACF | Always | Temporal dependency structure |
| Seasonal decomposition | If frequency > 1 | Trend/seasonal/residual |
| Forecast + intervals | After model fit | Prediction visualization |
| CUSUM | If structural breaks tested | Parameter stability |
| Subseries | If periodic data | Within-period patterns |
| Rolling statistics | Analysis workflow | Temporal stability |
| Rolling coefficients | Analysis workflow | Parameter stability |
| ARIMA residual diagnostics | After ARIMA fit | Model adequacy |
| Conditional variance | After GARCH fit | Volatility visualization |
| Impulse response | After VAR fit | Dynamic cross-effects |
| Spectral density | Analysis workflow | Frequency domain |
| ML variable importance | After tree models | Feature hierarchy |
| Forecast comparison | After all models | Cross-method overlay |

All plots: 300 DPI, clean labels, no gridlines clutter.
Vary theme/palette per generation (see code-style-variation.md).
