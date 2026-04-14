# Code Style Variation Specification

## Purpose

Every code generation produces naturally varied surface patterns --- different variable names, comments, colors, and import orders --- so outputs look hand-written rather than templated, while preserving identical analytical logic.

## Style Dimensions

### 1. Variable Naming Pattern (pick ONE per generation)

| Pattern | LMM-RI | LMM-RS | Growth Curve | GEE | RF | LightGBM |
|---|---|---|---|---|---|---|
| A | `model_lmm_ri` | `model_lmm_rs` | `model_growth` | `model_gee` | `model_rf` | `model_lgbm` |
| B | `fit_ri` | `fit_rs` | `fit_growth` | `fit_gee` | `fit_forest` | `fit_lgbm` |
| C | `lmm_ri_result` | `lmm_rs_result` | `growth_result` | `gee_result` | `rf_result` | `lgbm_result` |
| D | `mod_ri` | `mod_rs` | `mod_growth` | `mod_gee` | `mod_rf` | `mod_lgbm` |
| E | `ri_fit` | `rs_fit` | `gcm_fit` | `gee_fit` | `rforest` | `lgbm_fit` |

Tidy output follows the same pattern:
- A: `lmm_tidy`, `lmm_glance`, `gee_tidy`
- B: `fit_tidy`, `fit_summary`, `gee_summary`
- C: `lmm_coefs`, `lmm_stats`, `gee_coefs`
- D: `mod_coefs`, `mod_fit`, `gee_coefs`
- E: `ri_coefs`, `ri_summary`, `gee_summary`

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

| Palette | Primary | Secondary | Accent | Group3 | Group4 |
|---|---|---|---|---|---|
| A | `#4A90D9` | `#D94A4A` | `#D9A04A` | `#4AD97A` | `#9B59B6` |
| B | `#2C7BB6` | `#D7191C` | `#FDAE61` | `#ABD9E9` | `#1A9641` |
| C | `#1B9E77` | `#D95F02` | `#7570B3` | `#E7298A` | `#66A61E` |
| D | `#E41A1C` | `#377EB8` | `#4DAF4A` | `#984EA3` | `#FF7F00` |
| E | `#66C2A5` | `#FC8D62` | `#8DA0CB` | `#E78AC3` | `#A6D854` |

Note: repeated measures designs often need 4+ colors for groups (e.g., Diet 1-4 in ChickWeight).

### 6. Python Import Order

Randomize independent imports. These groups are independent:

```python
# Group 1 (data): pandas, numpy — either order
# Group 2 (stats): statsmodels, scipy, pingouin — any order
# Group 3 (mixed models): statsmodels.formula.api, statsmodels.regression.mixed_linear_model
# Group 4 (gee): statsmodels.genmod.generalized_estimating_equations
# Group 5 (ml): sklearn submodules, lightgbm — any order
# Group 6 (viz): matplotlib, seaborn — either order
```

Within each group, order can be swapped.
Between groups, order can be swapped (as long as no dependency breaks).

### 7. R Library Order

Same principle — randomize non-dependent loads:

```r
# Core (any order): tidyverse, broom, broom.mixed
# Mixed models (any order): lme4, lmerTest, nlme
# GEE: geepack
# Repeated ANOVA: rstatix, ez, afex
# Post-hoc: emmeans, multcomp
# Trees (any order): randomForest, lightgbm
# Viz (already in tidyverse): gridExtra, patchwork if needed
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
- Random effects specification (same formula structure)
- GEE correlation structure (same corstr argument)

The style variation is cosmetic. The analysis is identical.
