# Sentence Bank — Time Series Results

## Purpose

Provide varied phrasings for each type of statistical result. The skill
selects from these contextually — never repeating patterns within a single
document. This is the core output quality variation mechanism for prose output.

## Rules

- Pick ONE variant per result instance
- Never repeat the same variant within a single results.md
- Adapt to actual data context (variable names, direction, magnitude)
- These are structural templates — the actual text must feel natural and
  specific to the study, not templated

---

## Stationarity Assessment

ST1: "The augmented Dickey-Fuller test indicated that [series] was [stationary/non-stationary] (ADF = [val], *p* = [val]). The KPSS test [confirmed/contradicted] this finding (KPSS = [val], *p* = [val]). [Differencing decision]."

ST2: "Prior to model fitting, stationarity was assessed using the ADF (*t* = [val], *p* = [val]) and KPSS (stat = [val], *p* = [val]) tests. [Series] [required/did not require] differencing to achieve stationarity."

ST3: "Formal stationarity testing revealed that [series] [contained/did not contain] a unit root (ADF *p* = [val]; KPSS *p* = [val]). [First differencing was applied to induce stationarity / The series was modeled in levels]."

ST4: "Both the ADF and KPSS tests were conducted to assess the stationarity of [series]. Results [consistently indicated / provided mixed evidence regarding] stationarity (ADF = [val], *p* = [val]; KPSS = [val], *p* = [val]). [Action taken]."

---

## ARIMA Model

AR1: "An ARIMA([p],[d],[q]) model was selected based on AIC minimization (AIC = [val]). The Ljung-Box test on residuals was not significant (*Q*([lag]) = [val], *p* = [val]), indicating adequate model fit."

AR2: "Automatic order selection identified ARIMA([p],[d],[q]) as the optimal specification (AIC = [val], BIC = [val]). Residual diagnostics confirmed white noise behavior (Ljung-Box *Q* = [val], *p* = [val])."

AR3: "The fitted ARIMA([p],[d],[q]) model (AIC = [val]) produced residuals consistent with white noise (*Q*([lag]) = [val], *p* = [val]). The [AR/MA] coefficient(s) were [val] (SE = [val])."

AR4: "Based on the ACF/PACF patterns of the [differenced/original] series, an ARIMA([p],[d],[q]) model was specified. Information criteria supported this choice (AIC = [val]). No significant residual autocorrelation was detected (Ljung-Box *p* = [val])."

---

## SARIMA Model

SA1: "The seasonal pattern evident at lag [s] motivated a SARIMA([p],[d],[q])([P],[D],[Q])[[s]] specification (AIC = [val]). The seasonal model improved fit over the non-seasonal ARIMA (deltaAIC = [val])."

SA2: "To capture the [s]-period seasonal cycle, a SARIMA model was fitted: ARIMA([p],[d],[q])([P],[D],[Q])[[s]] (AIC = [val]). Residual diagnostics were satisfactory (Ljung-Box *Q* = [val], *p* = [val])."

SA3: "Incorporating seasonal components yielded an ARIMA([p],[d],[q])([P],[D],[Q])[[s]] model. The AIC ([val]) was [lower/comparable to] the non-seasonal specification, and residuals showed no remaining autocorrelation (*p* = [val])."

SA4: "Given the clear [monthly/quarterly/weekly] seasonal structure, a seasonal ARIMA model was estimated. The selected ARIMA([p],[d],[q])([P],[D],[Q])[[s]] achieved AIC = [val] with adequate residual behavior."

---

## Exponential Smoothing (ETS)

ET1: "Automatic ETS selection identified an ETS([E],[T],[S]) model (AIC = [val]). Smoothing parameters were alpha = [val], [beta = [val],] [gamma = [val]]."

ET2: "The Holt-Winters framework selected an ETS([E],[T],[S]) specification with [additive/multiplicative] [trend/seasonality]. The level smoothing parameter (alpha = [val]) indicated [fast/slow] adaptation to recent observations."

ET3: "Exponential smoothing via the ETS framework yielded an [E],[T],[S] model. The estimated smoothing parameters (alpha = [val], beta = [val], gamma = [val]) suggest [interpretation about adaptation speed]."

ET4: "An ETS([E],[T],[S]) model was fitted as a complementary forecasting approach (AIC = [val]). The [damped/undamped] trend component and [additive/multiplicative] seasonal component [captured/reflected] [pattern description]."

---

## GARCH

GA1: "The ARCH-LM test on ARIMA residuals was significant (*p* = [val]), indicating volatility clustering. A GARCH(1,1) model was fitted, with persistence (alpha + beta) = [val], suggesting [high/moderate/low] volatility persistence."

GA2: "Evidence of conditional heteroscedasticity was detected (ARCH-LM *p* = [val]). The fitted GARCH(1,1) (omega = [val], alpha = [val], beta = [val]) indicated that volatility shocks [persist/decay] [quickly/slowly]."

GA3: "Residual variance was non-constant (ARCH-LM *p* = [val]). The GARCH(1,1) specification captured volatility dynamics, with a persistence parameter of [val] indicating [near-integrated/transient] volatility."

GA4: "Volatility clustering in the ARIMA residuals (ARCH-LM *p* = [val]) motivated a GARCH(1,1) extension. The conditional variance equation revealed [interpretation about risk periods or volatility regimes]."

---

## VAR and Granger Causality

VA1: "A VAR([p]) model was fitted based on [AIC/BIC] lag selection. Granger causality tests indicated that [X] [did/did not] Granger-cause [Y] (*F* = [val], *p* = [val])."

VA2: "Vector autoregression at lag [p] (selected by [criterion]) captured the joint dynamics of [Y] and [X]. [X] provided significant predictive information for [Y] (Granger *F* = [val], *p* = [val]), [but the reverse was not significant / and vice versa]."

VA3: "The multivariate dynamics were modeled via a VAR([p]) specification. Impulse response analysis showed that a one-unit shock to [X] [increased/decreased] [Y] by [val] units after [k] periods. Granger causality was [significant/not significant] (*p* = [val])."

VA4: "Cross-series relationships were examined using a VAR([p]) model. Forecast error variance decomposition indicated that [X] accounted for [val]% of the variation in [Y] at a [k]-period horizon."

---

## Spectral Analysis

SP1: "Spectral analysis identified a dominant cycle at frequency [val] (period = [val] [units]), consistent with the [monthly/quarterly/annual] seasonal pattern."

SP2: "The periodogram revealed peak spectral density at a period of [val] [units], confirming the [seasonal/cyclical] structure identified in the time domain analysis."

SP3: "Frequency domain analysis via the smoothed periodogram indicated a dominant periodicity of [val] [units]. [Secondary peaks / No additional significant cycles] were detected."

SP4: "Spectral decomposition of [series] showed concentrated power at a period of [val] [units], corroborating the seasonal decomposition results. The spectral density at this frequency was [val]."

---

## ML-Based (Exploratory)

ML1: "Random forest and LightGBM models on lagged features identified [lag_k] and [feature] as the most important predictors. The dominance of recent lags is consistent with the ARIMA structure, while [calendar/rolling] features captured [additional pattern]."

ML2: "Tree-based models were fitted as an exploratory complement. Variable importance from the random forest ranked [lag_1] highest, followed by [seasonal_lag]. These results should be interpreted cautiously given the sample size (*T* = [val])."

ML3: "As exploratory analysis, ensemble methods (RF, LightGBM) were applied to engineered lag features. The importance hierarchy ([top features]) was [consistent with / partially divergent from] the frequency domain and ARIMA findings."

ML4: "Machine learning models on lagged and calendar features provided a complementary perspective. [Feature] emerged as the dominant predictor across both RF and LightGBM, corroborating the [ARIMA/spectral] results while revealing [nonlinear pattern]."

---

## Model Comparison Synthesis

MC1: "Across all forecasting approaches, [key finding about convergence]. Hold-out MAPE ranged from [val]% to [val]%, with [model family] providing the most accurate point forecasts under its [assumption set]."

MC2: "The convergence of classical time series models, exponential smoothing, and machine learning methods strengthens confidence in the [seasonal/trend/cyclical] pattern. Each approach illuminated different aspects: ARIMA captured [X], GARCH revealed [Y], and tree-based models highlighted [Z]."

MC3: "Taken together, the multi-method analysis revealed robust [finding]. The ARIMA/SARIMA framework is recommended for manuscript reporting given its interpretability and theoretical grounding, supplemented by [specific insight] from the [complementary method]."

MC4: "No single model dominated across all accuracy metrics, reflecting the complementary assumptions each brings. [Model A] excelled at [short-horizon/seasonal] forecasts while [Model B] better captured [volatility/nonlinear] dynamics. The unified view suggests [synthesis finding]."
