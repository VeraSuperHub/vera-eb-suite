# Code Style Variation Specification

## Purpose

Every code generation produces naturally varied surface patterns --- different variable names, comments, colors, and import orders --- so outputs look hand-written rather than templated, while preserving identical analytical logic.

## Style Dimensions

### 1. Variable Naming Pattern (pick ONE per generation)

| Pattern | RE Model | FE Model | Trim-Fill | Meta-Reg |
|---|---|---|---|---|
| A | `model_re` | `model_fe` | `model_tf` | `model_reg` |
| B | `fit_random` | `fit_fixed` | `fit_trimfill` | `fit_metareg` |
| C | `rma_result` | `fe_result` | `tf_result` | `reg_result` |
| D | `mod_re` | `mod_fe` | `mod_tf` | `mod_metareg` |
| E | `re_fit` | `fe_fit` | `trimfill_fit` | `metareg_fit` |

Data objects follow the same pattern:
- A: `study_data`, `effect_data`
- B: `dat_studies`, `dat_effects`
- C: `meta_df`, `effects_df`
- D: `d_studies`, `d_effects`
- E: `studies_tbl`, `effects_tbl`

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

### 4. Plot Theme (pick ONE, maintain within script)

| Theme | R | Python equivalent |
|---|---|---|
| A | `theme_minimal(base_size = 12)` | `plt.style.use('seaborn-v0_8-whitegrid')` |
| B | `theme_bw(base_size = 12)` | `plt.style.use('seaborn-v0_8-white')` |
| C | `theme_classic(base_size = 12)` | `plt.style.use('classic')` with grid off |
| D | `theme_light(base_size = 12)` | `plt.style.use('seaborn-v0_8-ticks')` |

### 5. Color Palette (pick ONE per generation)

| Palette | Study Point | Summary Diamond | CI Line | Imputed Point |
|---|---|---|---|---|
| A | `#4A90D9` | `#D94A4A` | `#333333` | `#999999` |
| B | `#2C7BB6` | `#D7191C` | `#444444` | `#AAAAAA` |
| C | `#1B9E77` | `#D95F02` | `#333333` | `#888888` |
| D | `#E41A1C` | `#377EB8` | `#555555` | `#BBBBBB` |
| E | `#66C2A5` | `#FC8D62` | `#333333` | `#999999` |

### 6. Python Import Order

Randomize independent imports. These groups are independent:

```python
# Group 1 (data): pandas, numpy — either order
# Group 2 (stats): statsmodels, scipy — either order
# Group 3 (meta): custom functions — any order
# Group 4 (viz): matplotlib, seaborn — either order
```

Within each group, order can be swapped.
Between groups, order can be swapped (as long as no dependency breaks).

### 7. R Library Order

Same principle — randomize non-dependent loads:

```r
# Core (any order): metafor, tidyverse, broom
# Bias (any order): meta (if used for trimfill)
# Bayesian (if used): brms, bayesmeta
# Viz (already in tidyverse): gridExtra if needed
```

## Application

At code generation time:
1. Pick one option from each dimension (7 choices)
2. Apply consistently throughout the entire script

## What Style Variation Does NOT Change

- Analytical logic (same models, same tests, same order)
- Statistical output (same numbers, same interpretations)
- Package/function calls (same API, same arguments)
- File naming convention (plot_01, plot_03, etc.)

The style variation is cosmetic. The analysis is identical.
