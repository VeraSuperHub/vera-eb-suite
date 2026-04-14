# Code Style Variation Specification

## Purpose

Every code generation produces naturally varied surface patterns --- different variable names, comments, colors, and import orders --- so outputs look hand-written rather than templated, while preserving identical analytical logic.

## Style Dimensions

### 1. Variable Naming Pattern (pick ONE per generation)

| Pattern | ARIMA | SARIMA | ETS | GARCH | VAR | RF | LightGBM |
|---|---|---|---|---|---|---|---|
| A | `model_arima` | `model_sarima` | `model_ets` | `model_garch` | `model_var` | `model_rf` | `model_lgbm` |
| B | `fit_arima` | `fit_sarima` | `fit_ets` | `fit_garch` | `fit_var` | `fit_forest` | `fit_lgbm` |
| C | `arima_result` | `sarima_result` | `ets_result` | `garch_result` | `var_result` | `rf_result` | `lgbm_result` |
| D | `mod_arima` | `mod_sarima` | `mod_ets` | `mod_garch` | `mod_var` | `mod_rf` | `mod_lgbm` |
| E | `arima_fit` | `sarima_fit` | `ets_fit` | `garch_fit` | `var_fit` | `rforest` | `lgbm_fit` |

Forecast output follows the same pattern:
- A: `forecast_arima`, `forecast_ets`
- B: `pred_arima`, `pred_ets`
- C: `arima_forecast`, `ets_forecast`
- D: `fc_arima`, `fc_ets`
- E: `arima_pred`, `ets_pred`

### 2. Comment Style (pick ONE per generation)

```
Style A: # ── Section Name ──────────────────────
Style B: # --- Section Name ---
Style C: # == Section Name ==
Style D: # Section Name
Style E: # ▸ Section Name
```

### 3. Section Separator (pick ONE per generation)

```
Sep A: cat("=" |> strrep(60), "\n")          / print("=" * 60)
Sep B: cat("-" |> strrep(60), "\n")          / print("-" * 60)
Sep C: cat("#" |> strrep(60), "\n")          / print("#" * 60)
Sep D: cat("\n---\n")                         / print("\n---\n")
```

### 4. ggplot Theme (pick ONE, maintain within script)

| Theme | R | Python equivalent |
|---|---|---|
| A | `theme_minimal(base_size = 12)` | `plt.style.use('seaborn-v0_8-whitegrid')` |
| B | `theme_bw(base_size = 12)` | `plt.style.use('seaborn-v0_8-white')` |
| C | `theme_classic(base_size = 12)` | `plt.style.use('classic')` with grid off |
| D | `theme_light(base_size = 12)` | `plt.style.use('seaborn-v0_8-ticks')` |

### 5. Color Palette (pick ONE per generation)

| Palette | Primary | Secondary | Accent | Forecast | CI_band |
|---|---|---|---|---|---|
| A | `#4A90D9` | `#D94A4A` | `#D9A04A` | `#2E86AB` | `#A8D0E6` |
| B | `#2C7BB6` | `#D7191C` | `#FDAE61` | `#1A5276` | `#AED6F1` |
| C | `#1B9E77` | `#D95F02` | `#7570B3` | `#117A65` | `#A9DFBF` |
| D | `#E41A1C` | `#377EB8` | `#4DAF4A` | `#1F618D` | `#85C1E9` |
| E | `#66C2A5` | `#FC8D62` | `#8DA0CB` | `#2874A6` | `#AED6F1` |

### 6. Python Import Order

Randomize independent imports. These groups are independent:

```python
# Group 1 (data): pandas, numpy — either order
# Group 2 (stats): statsmodels submodules, pmdarima, arch — any order
# Group 3 (ml): sklearn submodules, lightgbm — any order
# Group 4 (viz): matplotlib, seaborn — either order
```

Within each group, order can be swapped.
Between groups, order can be swapped (as long as no dependency breaks).

### 7. R Library Order

Same principle — randomize non-dependent loads:

```r
# Core (any order): tidyverse, forecast, tseries
# Models (any order): rugarch, vars, strucchange, randomForest, lightgbm
# Viz (already in tidyverse): gridExtra if needed
```

## Application

At code generation time:
1. Pick one option from each dimension (7 choices)
2. Apply consistently throughout the entire script

## What Style Variation Does NOT Change

- Analytical logic (same tests, same models, same order)
- Statistical output (same numbers, same interpretations)
- Package/function calls (same API, same arguments)
- File naming convention (plot_01, plot_02, etc.)

The style variation is cosmetic. The analysis is identical.
