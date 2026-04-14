# Code Style Variation Specification

## Purpose

Every code generation produces subtly different surface patterns.
Two users comparing code will see different variable names, comments,
colors, and import orders -- despite identical analytical logic.

This serves two purposes:
1. Prevents direct code sharing from substituting for access
2. Enables generation tracing if leaked code is identified

## Style Dimensions

### 1. Variable Naming Pattern (pick ONE per generation)

| Pattern | ANOVA Model | RSM Model | Random Forest | LightGBM |
|---|---|---|---|---|
| A | `model_aov` | `model_rsm` | `model_rf` | `model_lgbm` |
| B | `fit_anova` | `fit_rsm` | `fit_forest` | `fit_lgbm` |
| C | `aov_result` | `rsm_result` | `rf_result` | `lgbm_result` |
| D | `mod_aov` | `mod_rsm` | `mod_rf` | `mod_lgbm` |
| E | `anova_fit` | `rsm_fit` | `rforest` | `lgbm_fit` |

Tidy output follows the same pattern:
- A: `aov_tidy`, `aov_summary`
- B: `fit_tidy`, `fit_summary`
- C: `aov_coefs`, `aov_stats`
- D: `mod_coefs`, `mod_summary`
- E: `anova_coefs`, `anova_summary`

### 2. Comment Style (pick ONE per generation)

```
Style A: # -- Section Name ----------------------------------------
Style B: # --- Section Name ---
Style C: # == Section Name ==
Style D: # Section Name
Style E: # > Section Name
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

| Palette | Primary | Secondary | Accent | Group3 |
|---|---|---|---|---|
| A | `#4A90D9` | `#D94A4A` | `#D9A04A` | `#4AD97A` |
| B | `#2C7BB6` | `#D7191C` | `#FDAE61` | `#ABD9E9` |
| C | `#1B9E77` | `#D95F02` | `#7570B3` | `#E7298A` |
| D | `#E41A1C` | `#377EB8` | `#4DAF4A` | `#984EA3` |
| E | `#66C2A5` | `#FC8D62` | `#8DA0CB` | `#E78AC3` |

### 6. Python Import Order

Randomize independent imports. These groups are independent:

```python
# Group 1 (data): pandas, numpy -- either order
# Group 2 (stats): statsmodels, scipy -- either order
# Group 3 (ml): sklearn submodules, lightgbm -- any order
# Group 4 (viz): matplotlib, seaborn -- either order
```

Within each group, order can be swapped.
Between groups, order can be swapped (as long as no dependency breaks).

### 7. R Library Order

Same principle -- randomize non-dependent loads:

```r
# Core (any order): tidyverse, broom, car
# DOE-specific (any order): rsm, FrF2, agricolae, emmeans
# Models (any order): randomForest, lightgbm
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
