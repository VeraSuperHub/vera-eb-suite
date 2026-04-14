# Code Style Variation Specification

## Purpose

Every code generation produces naturally varied surface patterns --- different variable names, comments, colors, and import orders --- so outputs look hand-written rather than templated, while preserving identical analytical logic.

## Style Dimensions

### 1. Variable Naming Pattern (pick ONE per generation)

| Pattern | Multinomial | LDA | Random Forest | LightGBM | CART |
|---|---|---|---|---|---|
| A | `model_mlogit` | `model_lda` | `model_rf` | `model_lgbm` | `model_cart` |
| B | `fit_multinom` | `fit_lda` | `fit_forest` | `fit_lgbm` | `fit_tree` |
| C | `mlogit_result` | `lda_result` | `rf_result` | `lgbm_result` | `cart_result` |
| D | `mod_mnom` | `mod_lda` | `mod_rf` | `mod_lgbm` | `mod_tree` |
| E | `multinom_fit` | `lda_fit` | `rforest` | `lgbm_fit` | `tree_fit` |

Tidy output follows the same pattern:
- A: `mlogit_tidy`, `mlogit_rrr`
- B: `fit_tidy`, `fit_summary`
- C: `mlogit_coefs`, `mlogit_stats`
- D: `mod_coefs`, `mod_fit`
- E: `multinom_coefs`, `multinom_summary`

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

| Palette | Class1 | Class2 | Class3 | Class4 | Class5 |
|---|---|---|---|---|---|
| A | `#4A90D9` | `#D94A4A` | `#D9A04A` | `#4AD97A` | `#9B59B6` |
| B | `#2C7BB6` | `#D7191C` | `#FDAE61` | `#ABD9E9` | `#1A9641` |
| C | `#1B9E77` | `#D95F02` | `#7570B3` | `#E7298A` | `#66A61E` |
| D | `#E41A1C` | `#377EB8` | `#4DAF4A` | `#984EA3` | `#FF7F00` |
| E | `#66C2A5` | `#FC8D62` | `#8DA0CB` | `#E78AC3` | `#A6D854` |

### 6. Python Import Order

Randomize independent imports. These groups are independent:

```python
# Group 1 (data): pandas, numpy — either order
# Group 2 (stats): statsmodels, scipy — either order
# Group 3 (ml): sklearn submodules (LogisticRegression, LDA, DecisionTree, RF) — any order
# Group 4 (gbm): lightgbm
# Group 5 (viz): matplotlib, seaborn — either order
```

Within each group, order can be swapped.
Between groups, order can be swapped (as long as no dependency breaks).

### 7. R Library Order

Same principle — randomize non-dependent loads:

```r
# Core (any order): tidyverse, broom, nnet
# Models (any order): MASS, rpart, randomForest, lightgbm
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
