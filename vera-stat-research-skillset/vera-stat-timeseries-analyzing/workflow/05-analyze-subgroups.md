# 05 — Analyze Subseries & Rolling Windows

## Executor: Main Agent (code generation)

## Data In: Code + prose from 04-run-additional-tests.md

## Generate code for PART 4: Subseries & Stability Analysis

### 5A: Subseries Analysis
For periodic data (monthly, quarterly, etc.):
1. **Subseries plots** (one mini-series per period)
   - Monthly: 12 subseries (all Januaries, all Februaries, etc.)
   - Quarterly: 4 subseries
   - Show mean per period as horizontal line
   - R: `forecast::monthplot()` or custom ggplot
   - Python: `statsmodels.graphics.tsaplots.month_plot()` or custom
   → `plot_04_subseries.png`

2. **Subseries statistics**
   - Mean, SD, trend slope per subseries period
   - Identify which periods show strongest/weakest values
   - Identify which periods show most/least variability

3. **Seasonal strength metric**
   - Variance of seasonal component / variance of (seasonal + residual)
   - 0 = no seasonality, 1 = pure seasonality
   - Report as percentage

### 5B: Rolling Window Analysis (Parameter Stability)
1. **Rolling mean and variance**
   - Window size = max(frequency, N/10)
   - Plot rolling mean and rolling SD over time
   - Detect level shifts or variance changes
   → `plot_05_rolling_stats.png`

2. **Rolling ARIMA coefficients**
   - Fit ARIMA(p,d,q) in rolling windows (same order as primary model)
   - Window size = max(2*frequency, 30)
   - Step = 1 or frequency
   - Plot AR and MA coefficients over time
   - Stable → parameters do not drift; Unstable → time-varying dynamics
   → `plot_06_rolling_coefs.png`

3. **Rolling forecast accuracy**
   - 1-step-ahead rolling forecast (expanding or fixed window)
   - Compute rolling RMSE over time
   - Detect periods where model fits poorly

### 5C: Regime Detection
1. **Visual regime identification**
   - Based on rolling statistics: are there distinct "eras"?
   - If rolling mean or variance shows clear shifts → identify approximate break dates
2. **Markov switching (if N > 100)**
   - Fit 2-regime Markov switching model
   - R: `MSwM::msmFit()` or `fMarkovSwitching`
   - Python: `statsmodels.tsa.regime_switching.markov_regression`
   - Report regime probabilities and transition matrix
   - Plot smoothed regime probabilities over time
   → `plot_07_regimes.png` (if applicable)

### Quality: Apply structure variation
- Subseries plot: alternate grid vs single-panel layout
- Rolling plots: vary line color scheme, window annotations
- Regime plot: vary between probability shading vs line plot
- Rotate between "parameter stability" / "temporal robustness" / "dynamic consistency" framing

## Validation Checkpoint

- [ ] Subseries plot generated (if periodic data)
- [ ] Subseries statistics reported (mean, SD, trend per period)
- [ ] Seasonal strength metric reported
- [ ] Rolling mean and variance plotted
- [ ] Rolling ARIMA coefficients plotted
- [ ] Rolling forecast accuracy computed
- [ ] Regime detection attempted (if N > 100)
- [ ] No repeated phrasing patterns from sentence bank

## Data Out → 06-fit-models.md

```
subseries_code_r: [PART 4 R code block]
subseries_code_py: [PART 4 Python code block]
methods_para_subseries: [methods paragraph prose]
methods_para_rolling: [methods paragraph prose]
methods_para_regime: [methods paragraph prose]
results_para_subseries: [results paragraph prose]
plots: [list of new plot filenames]
```
