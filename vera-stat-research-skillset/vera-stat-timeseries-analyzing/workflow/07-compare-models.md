# 07 — Compare Models

## Executor: Main Agent (code generation)

## Data In: All model outputs from 06-fit-models.md

## Design Principle

Models are analytic lenses, not contestants. Each model type provides a different
kind of insight into the temporal dynamics. The comparison step synthesizes what
converges and what each uniquely reveals. Frame as "which assumptions fit the
data" — never "which model wins."

## Generate code for PART 6: Cross-Method Insight Synthesis

### 7A: Forecast Accuracy on Hold-Out Period

Split data: training = first 80% of observations, test = last 20%.

For each fitted model, compute on hold-out:
- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Square Error)
- **MAPE** (Mean Absolute Percentage Error)

```
| Model          | MAE    | RMSE   | MAPE (%) | AIC     | Assumptions                    |
|----------------|--------|--------|----------|---------|--------------------------------|
| ARIMA(p,d,q)   | [val]  | [val]  | [val]    | [val]   | Linear, stationary errors      |
| SARIMA         | [val]  | [val]  | [val]    | [val]   | Linear, seasonal stationarity  |
| ETS            | [val]  | [val]  | [val]    | [val]   | Exponential smoothing          |
| GARCH          | [val]  | [val]  | [val]    | [val]   | Conditional heteroscedasticity |
| VAR            | [val]  | [val]  | [val]    | [val]   | Cross-series linear dynamics   |
| Reg-ARIMA      | [val]  | [val]  | [val]    | [val]   | Exogenous + temporal errors    |
| RF (lagged)    | [val]  | [val]  | [val]    | —       | Nonlinear, no distributional   |
| LightGBM       | [val]  | [val]  | [val]    | —       | Nonlinear, no distributional   |
```

Only include rows for models that were actually fitted. Do NOT force-fit all.

### 7B: Forecast Comparison Plot

- All model forecasts on hold-out period overlaid
- Observed hold-out values as reference
- Different line styles/colors per model
- Legend identifying each model
  → `plot_13_forecast_comparison.png`

### 7C: Insight Synthesis Table

One row per model family, focus on *what it reveals*:

```
| Method              | Unique Insight                                          |
|---------------------|---------------------------------------------------------|
| ARIMA/SARIMA        | [linear temporal dynamics, seasonal pattern structure]  |
| ETS                 | [level/trend/seasonal decomposition perspective]        |
| GARCH               | [volatility clustering, risk periods]                   |
| VAR                 | [cross-series dynamics, Granger causality direction]    |
| Spectral            | [dominant cycles, hidden periodicities]                 |
| Reg-ARIMA           | [exogenous effect after controlling for temporal deps]  |
| Tree-Based (ML)     | [nonlinear lag importance, feature hierarchy]            |
```

Do NOT rank models by forecast accuracy. Do NOT declare a "winner."
Each row states what that modeling lens uniquely reveals about the data.

### 7D: Narrative Synthesis

3-4 sentences covering:
1. What converges across methods (e.g., "all models capture the upward trend and
   seasonal pattern, with MAPE ranging from X to Y%")
2. What classical models uniquely reveal (seasonal structure, volatility regimes,
   cross-series effects)
3. What ML models uniquely reveal (which lags dominate, nonlinear patterns)
4. Overall: "the ARIMA/SARIMA framework provides the most interpretable and
   theoretically grounded forecast, while tree-based methods confirm the
   importance of [specific lag structure]"

### Quality: Synthesis variation
Apply sentence bank from `reference/patterns/sentence-bank.md` (model comparison section).
Rotate lead-in: convergence finding, unique classical insight, or ML confirmation.

## Validation Checkpoint

- [ ] Hold-out accuracy computed for all fitted models (MAE, RMSE, MAPE)
- [ ] Forecast comparison plot with all models overlaid
- [ ] Insight synthesis table: one row per model family
- [ ] No "best model" declaration or horse-race framing
- [ ] Accuracy framed as "which assumptions fit" not "which wins"
- [ ] Narrative synthesis: 3-4 sentences covering convergence + unique insights
- [ ] Sentence bank applied (no repeated phrasing from prior steps)

## Data Out → 08-generate-manuscript.md

```
comparison_code_r: [PART 6 R code block]
comparison_code_py: [PART 6 Python code block]
accuracy_table: [MAE, RMSE, MAPE per model]
insight_table: [model family × unique insight]
forecast_comparison_plot: plot_13_forecast_comparison.png
results_para_comparison: [synthesis paragraph prose]
```
