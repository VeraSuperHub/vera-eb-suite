---
name: vera-stat-timeseries-testing
description: >-
  Runs time series diagnostics and primary ARIMA modeling for temporal data.
  Produces time plot, ACF/PACF, seasonal decomposition, stationarity tests
  (ADF + KPSS), and one fully interpreted ARIMA model with forecast and
  prediction intervals. Ends with a recommendation block listing additional
  analyses available. Outputs .R and .py scripts with 2
  publication-quality plots. Triggered when user has temporal/time series
  data and says "time series," "temporal data," "forecast," "ARIMA,"
  "seasonal," "trend," "autocorrelation," "monthly data," "daily data,"
  "quarterly," "stationarity," or names a time-indexed variable like
  sales over time, temperature, stock price, monthly passengers. Does not
  handle panel/longitudinal data (redirect to vera-stat-repeated), cross-
  sectional data, or spatial time series.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Time Series — Diagnostics & Primary Modeling

Open-source skill.

## Workflow

Read each step file in `workflow/` before executing that step.

| Step | File | Executor | Output |
|---|---|---|---|
| Collect | `workflow/01-collect-inputs.md` | Main Agent | Structured input summary |
| Diagnose | `workflow/02-check-distribution.md` | Main Agent | PART 1 code block |
| Model | `workflow/03-run-primary-test.md` | Main Agent | PART 2-3 code blocks |

## Decision Tree

```
1. STATIONARITY CHECK
   ├── Stationary (ADF p < .05 AND KPSS p ≥ .05) → fit ARIMA(p,0,q)
   ├── Non-stationary → difference, retest, fit ARIMA(p,d,q)
   └── Seasonal pattern detected → recommend SARIMA

2. MODEL SELECTION
   ├── ACF/PACF inspection → candidate ARIMA(p,d,q) orders
   ├── Auto-ARIMA for automated selection (AIC minimization)
   └── Ljung-Box residual diagnostics → confirm adequacy
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Time series (Y)** | Variable name, units, what it measures |
| **Frequency** | Daily, weekly, monthly, quarterly, annual |
| **Date/time index** | Column name or implicit ordering |
| **Exogenous (optional)** | Any external predictors (for recommendation) |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Time Series Diagnostics   → plot_01_ts_diagnostics.png
PART 2: Primary ARIMA Model       → plot_02_forecast.png
PART 3: Recommendation Block      → text listing additional analyses available
```

## Reporting Standards

1. p-values: "< .001" not "0.000"; exact to 3 decimals otherwise
2. ADF test: report test statistic + p-value + number of lags used
3. KPSS test: report test statistic + p-value + bandwidth
4. Model notation: ARIMA(p,d,q) or ARIMA(p,d,q)(P,D,Q)[s]
5. Information criteria: AIC and BIC
6. Ljung-Box: Q statistic + lag + p-value
7. Forecast intervals: 80% and 95% prediction intervals
8. Accuracy metrics: RMSE, MAE, MAPE on training data
9. Decimal places: 2 for coefficients, 3 for p-values
10. Non-significance: "not statistically significant at alpha = .05" — never "no effect"

## Stationarity Tests

| Test | Null Hypothesis | Stationary if |
|---|---|---|
| ADF (Augmented Dickey-Fuller) | Unit root present (non-stationary) | p < .05 (reject null) |
| KPSS | Series is stationary | p >= .05 (fail to reject null) |

Conflicting results → note ambiguity, proceed with differencing as conservative choice.

## Example Dataset

R built-in `AirPassengers`: monthly airline passengers 1949-1960.
Python: `sm.datasets.get_rdataset("AirPassengers")` (with offline fallback to bundled `examples/airpassengers.csv`).

## Cross-Skill Interface

```
Output:
├── code_r      → .R script
├── code_python → .py script
├── figures/    → 2 PNGs (diagnostics + forecast)
└── recommendations → text block (additional analyses available)
```
