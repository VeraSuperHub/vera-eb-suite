# 06 — Fit Models

## Executor: Main Agent (code generation)

## Data In: Code + prose from 05-analyze-subgroups.md (or 04 if no subseries)

## Generate code for PART 5: Modeling

## Design Principle

Models are analytic lenses, not contestants. Each model captures different
dynamics: ARIMA captures linear temporal dependencies, GARCH captures
volatility clustering, VAR captures cross-series relationships, trees capture
nonlinear patterns. The goal is insight from multiple perspectives.

### Dual-Path Architecture

---

## Path A: Classical Time Series Models

### 6A-1: ARIMA/SARIMA — Full Specification
1. Fit ARIMA(p,d,q) with AIC-selected order (from testing workflow or step 04)
2. If seasonal: fit SARIMA(p,d,q)(P,D,Q)[s]
3. Report: coefficients, SE, AIC, BIC, log-likelihood
4. Ljung-Box on residuals at multiple lags (5, 10, 15)
5. Residual diagnostics plot: residual time plot, ACF, histogram, Q-Q
   → `plot_08_arima_diagnostics.png`

### 6A-2: ETS (Exponential Smoothing State Space)
1. Automatic model selection: ETS(E,T,S)
   - R: `forecast::ets()`
   - Python: `statsmodels.tsa.holtwinters.ExponentialSmoothing`
2. Report: selected model, smoothing parameters (alpha, beta, gamma), AIC
3. In-sample fitted values + residuals
4. Ljung-Box on residuals

### 6A-3: GARCH (if volatility clustering detected)
Condition: fit only if residuals from ARIMA show ARCH effects.
1. **ARCH-LM test** on ARIMA residuals
   - R: `FinTS::ArchTest()` or `tseries::jarque.bera.test()` on squared residuals
   - Python: `arch.unitroot.engle_granger` or `statsmodels` het_arch
   - If p < .05 → proceed with GARCH
2. Fit GARCH(1,1) on ARIMA residuals
   - R: `rugarch::ugarchfit()`
   - Python: `arch.arch_model()`
3. Report: omega, alpha1, beta1, persistence (alpha1+beta1)
4. Plot conditional variance over time
   → `plot_09_garch_variance.png` (if applicable)

### 6A-4: VAR (if multiple related series / exogenous)
Condition: fit only if exogenous variable(s) provided.
1. **Lag selection**: AIC, BIC, HQ criteria
   - R: `vars::VARselect()`
   - Python: `statsmodels.tsa.vector_ar.var_model.VAR`
2. Fit VAR(p) at selected lag
3. Report: coefficients for each equation
4. Granger causality within VAR framework
5. Impulse response functions (IRF)
   - Plot IRF for each variable pair
   → `plot_10_irf.png` (if applicable)
6. Forecast error variance decomposition (FEVD)

### 6A-5: Spectral Analysis
1. **Periodogram**: raw spectral density
2. **Smoothed spectrum**: Daniell or Parzen kernel
3. Report: dominant frequency, corresponding period, spectral power
4. Interpret: "dominant cycle of [X] periods" or "no clear cyclical pattern"
   → `plot_11_spectral.png`

### 6A-6: Regression with ARIMA Errors
Condition: fit only if exogenous predictor(s) exist.
1. Fit: Y ~ X with ARIMA(p,d,q) errors
   - R: `forecast::auto.arima(y, xreg=X)`
   - Python: `statsmodels.tsa.arima.model.ARIMA(y, exog=X)`
2. Report: regression coefficients for X + ARIMA order for errors
3. Compare AIC with pure ARIMA (no exogenous)
4. Interpret: "after accounting for temporal dynamics, [X] is [significant/not]"

---

## Path B: ML-Based (Exploratory)

### 6B-1: Feature Engineering
Create lagged features from the time series:
1. **Lag features**: y_{t-1}, y_{t-2}, ..., y_{t-p} where p = max(frequency, 12)
2. **Rolling statistics**: rolling mean and SD (window = frequency)
3. **Calendar features**: month, quarter, day-of-week (if applicable)
4. **Differenced features**: first difference of y
5. **Seasonal lag**: y_{t-s} where s = frequency

### 6B-2: Random Forest on Lagged Features
1. Fit RF (n_estimators=500, random_state=42)
2. In-sample R² (no train/test split if N < 200)
3. Variable importance (permutation importance)

### 6B-3: LightGBM on Lagged Features
1. Fit LightGBM with fixed hyperparameters:
   - n_estimators=500, max_depth=3, learning_rate=0.1
   - num_leaves=15, min_child_samples=max(3, N//10)
2. In-sample R²
3. Variable importance (gain-based)

### 6B-4: Variable Importance Comparison
- Which lags matter most? (recent vs seasonal lags)
- Which features matter? (raw lags vs rolling stats vs calendar)
- Variable importance plot combining RF and LightGBM
  → `plot_12_ml_importance.png`

### Quality: Code style variation
Apply per `reference/specs/code-style-variation.md`:
- Pick variable naming pattern (A-E)
- Pick comment style (A-E)
- Pick ggplot theme (A-D)
- Pick color palette (A-E)
- Randomize import order (Python)
- Record style vector for consistency (never in output)

### Quality: Interpretation variation
For each model type, rotate lead-in pattern:
- ARIMA: lead with model order, or AIC comparison, or diagnostic adequacy
- ETS: lead with selected components, or smoothing parameters, or comparison to ARIMA
- GARCH: lead with ARCH-LM evidence, or persistence, or practical interpretation
- VAR: lead with lag selection, or Granger causality, or impulse response insight
- Trees: lead with variable importance, or lag structure insight, or sample size caveat

## Validation Checkpoint

- [ ] ARIMA/SARIMA fully specified with diagnostics
- [ ] ETS fitted with automatic selection reported
- [ ] GARCH fitted (if ARCH effects detected) with persistence reported
- [ ] VAR fitted (if exogenous) with lag selection and Granger causality
- [ ] Spectral analysis with dominant frequency reported
- [ ] Regression with ARIMA errors (if exogenous) with coefficient comparison
- [ ] RF and LightGBM fitted on lagged features
- [ ] Variable importance from both ML models
- [ ] All diagnostic plots generated
- [ ] Code style variation applied consistently
- [ ] No repeated interpretation patterns within document

## Data Out → 07-compare-models.md

```
modeling_code_r: [PART 5 R code block]
modeling_code_py: [PART 5 Python code block]
methods_para_arima: [prose]
methods_para_ets: [prose]
methods_para_garch: [prose]
methods_para_var: [prose]
methods_para_spectral: [prose]
methods_para_regarima: [prose]
methods_para_ml: [prose]
results_para_classical: [prose]
results_para_ml: [prose]
tables: [model_comparison, importance_table, var_coefficients]
plots: [diagnostics, garch_variance, irf, spectral, ml_importance]
style_vector: [e.g., "C-B-A-D-E-1-2"]
```
