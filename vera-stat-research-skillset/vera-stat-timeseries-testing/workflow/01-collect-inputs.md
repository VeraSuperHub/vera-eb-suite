# 01 — Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** — one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Time series variable** — the outcome to model/forecast
   - Name, units, what it measures
   - Is it a single series or multiple? If panel/longitudinal → redirect to `vera-stat-repeated-testing`

3. **Frequency** — temporal granularity
   - Daily, weekly, monthly, quarterly, annual
   - If irregular spacing → flag and confirm

4. **Date/time index** — how time is represented
   - Column name (e.g., "date", "month", "year")
   - Or implicit ordering (row 1 = first observation)
   - Start date if known

## Optional (collect for recommendation quality)

5. **Exogenous variable(s)** — external predictors (e.g., temperature, price, policy change)
6. **Forecast horizon** — how many periods ahead to forecast
7. **Known structural breaks** — regime changes, interventions, policy shifts
8. **Sample size** — number of time points (if not evident from data)

## Validation Checkpoint

- [ ] Time series variable identified (continuous, measured over time)
- [ ] If data looks cross-sectional (no time ordering), flagged and redirected
- [ ] If data is panel/longitudinal (multiple subjects over time), redirected to repeated
- [ ] Frequency confirmed (daily/weekly/monthly/quarterly/annual)
- [ ] Date/time index identified or implicit ordering confirmed
- [ ] If N < 30 time points, power limitation warning issued
- [ ] If irregular spacing detected, noted for interpolation consideration
- [ ] At least time series variable + frequency collected

## Data Out → 02-check-distribution.md

Structured input summary containing:
```
ts_var: {name, units, description}
frequency: {daily | weekly | monthly | quarterly | annual}
date_index: {column_name | "implicit"}
start_date: {date | "unknown"}
exogenous: [{name, type}] or null
forecast_horizon: N or "default"
structural_breaks: [{date, description}] or null
sample_size: N or "unknown"
data_source: {file_path | description | variable_list}
```
