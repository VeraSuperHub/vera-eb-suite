# Outcome Type Detection Rules

Three-signal system for auto-detecting the outcome variable type from data characteristics, variable metadata, and research question context.

## Signal 1: Primary — Data Characteristics

Inspect the outcome variable's data properties.

### Decision Tree

```
outcome variable
│
├── Is it a time-to-event pair? (time column + event/censor indicator)
│   └── YES → survival
│
├── Is it multiple columns designated as outcomes?
│   └── YES → multivariate
│
├── Is it a single time-indexed series? (ordered time index, one observation per time point)
│   └── YES → timeseries
│
├── Is there repeated measurement structure? (multiple rows per subject, or wide-format with time suffixes)
│   └── YES → repeated
│
├── Is the data structure a factorial design? (crossed factor predictors, balanced cells)
│   └── YES → doe
│
├── Does it contain effect sizes + SEs/variances from multiple studies?
│   └── YES → meta
│
├── Is the user requesting latent variable or factor analysis?
│   └── YES → sem-cfa or sem-full
│
├── Is it numeric/continuous?
│   ├── >20 unique values AND continuous range → continuous
│   ├── Non-negative integers only AND mean ≈ variance → count
│   └── 3-20 unique values AND ordered → ordinal (numeric-coded)
│
├── Is it a factor/categorical?
│   ├── Exactly 2 levels → binary
│   ├── Ordered factor → ordinal
│   ├── 3+ unordered levels → nominal
│   └── 2 levels (character "yes"/"no" etc.) → binary
│
└── Ambiguous → flag for user confirmation
```

### Numeric Outcome Sub-Rules

| Property | Test | Threshold | Result |
|----------|------|-----------|--------|
| Unique values | `n_distinct(outcome)` | ≤ 2 | binary |
| Unique values | `n_distinct(outcome)` | 3-10, all integers, ordered | ordinal (possible) |
| Unique values | `n_distinct(outcome)` | > 20 | continuous |
| Distribution shape | `mean(outcome) ≈ var(outcome)` | ratio 0.5-2.0 | count (possible) |
| Value range | `min(outcome) ≥ 0` AND all integers | — | count (if also Poisson-like) |
| Value range | continuous, any real values | — | continuous |

### Survival Detection

Both conditions must hold:
1. A numeric column interpretable as time (positive values, often named time/duration/followup/os_months)
2. A binary column interpretable as event indicator (0/1, often named event/status/censor/dead)

If detected: outcome type = survival, outcome_var = the time column, event_var = the indicator column.

### Repeated Measures Detection

Any of:
1. Long format: multiple rows share the same subject ID, with a time/visit column
2. Wide format: columns with systematic time suffixes (score_t1, score_t2, score_t3)
3. User states "longitudinal", "within-subject", "paired"

### DOE Detection

All of:
1. Predictors are all categorical with few levels (2-5 each)
2. Design appears balanced or near-balanced (equal/similar cell counts)
3. User mentions "experiment", "factorial", "treatment combinations"

---

## Signal 2: Secondary — Variable Name & Label Heuristics

Scan the outcome variable name, column label, and value labels for keywords.

| Keyword Pattern | Inferred Type |
|-----------------|---------------|
| "survived", "died", "dead", "alive", "yes_no", "pass_fail", "positive_negative", "admitted", "readmit" | binary |
| "0/1 coded", "true/false", "success/failure" | binary |
| "likert", "severity", "grade", "stage", "rating", "satisfaction", "agree_disagree" | ordinal |
| "none_mild_moderate_severe", "low_medium_high", "poor_fair_good_excellent" | ordinal |
| "species", "diagnosis_type", "category", "group", "class", "ethnicity", "region" | nominal |
| "count", "events", "incidents", "visits", "breaks", "accidents", "n_episodes" | count |
| "time_to", "duration", "os_time", "pfs", "followup", "survival_months" | survival |
| "score_t1", "visit_1", "wave_", "baseline_", "pre_post" | repeated |
| "price", "index", "rate", "daily", "monthly", "quarterly" (with time index) | timeseries |
| "factor1", "latent", "construct", "loading" | sem |

Also check value labels (if SPSS/Stata):
- Ordered value labels (1="Never", 2="Rarely", ..., 5="Always") → ordinal
- Binary value labels (0="No", 1="Yes") → binary

---

## Signal 3: Contextual — Research Question Text

Parse the research question for analytical intent keywords.

| Research Question Pattern | Inferred Type |
|---------------------------|---------------|
| "predict survival", "time to event", "hazard", "mortality risk" | survival |
| "compare groups", "difference between", "effect of X on Y" | depends on outcome: if numeric → continuous; if binary → binary |
| "trend over time", "longitudinal change", "growth trajectory" | repeated |
| "forecast", "predict next period", "seasonal pattern" | timeseries |
| "which factors predict", "risk factors for", "determinants of" | matches outcome type |
| "classify", "which category", "discriminate between" | nominal |
| "dose-response", "ordered response" | ordinal |
| "pooled estimate", "across studies", "systematic review" | meta |
| "factor structure", "latent variable", "measurement model" | sem-cfa |
| "mediation", "path analysis", "structural model" | sem-full |
| "optimize response", "factorial experiment", "treatment combination" | doe |
| "incidence rate", "event frequency", "number of occurrences" | count |

---

## Confidence Scoring

| Level | Condition | Action |
|-------|-----------|--------|
| **HIGH** | All 3 signals agree, OR Signal 1 is unambiguous (e.g., exactly 2 levels = binary) | Auto-proceed after timeout |
| **MEDIUM** | 2 of 3 signals agree, OR Signal 1 clear but Signals 2-3 suggest alternative | Present detection, ask to confirm |
| **LOW** | Signals conflict, OR outcome could be multiple types (e.g., 5-value numeric = ordinal or continuous?) | Present top 2-3 candidates, require user selection |

### Ambiguity Resolution Rules

| Ambiguity | Resolution |
|-----------|------------|
| Numeric with 3-10 unique integers: ordinal or continuous? | If values are Likert-like (1-5, 1-7) → ordinal. If arbitrary range → continuous. Ask if unclear. |
| Numeric with 2 values: binary or continuous? | If values are 0/1 or coded categories → binary. If truly continuous but only 2 observed → ask user. |
| Count-like but high mean: count or continuous? | If mean > 30 and approximately normal → treat as continuous. If clearly count data with many zeros → count. |
| Time column exists but no censor indicator: survival or continuous? | Ask user if censoring applies. If no censoring → continuous. |
| Multiple outcomes: multivariate or run separately? | If user wants joint analysis → multivariate. If independent questions → run pipeline separately per outcome. |

---

## Edge Cases

1. **Composite scores** (sum of Likert items): Treat as continuous if >20 possible values; ordinal if ≤20.
2. **Proportion outcomes** (bounded 0-1): Treat as continuous with beta regression note in methods.
3. **Zero-inflated continuous**: Flag for user — could use two-part model (binary for zero/non-zero + continuous for positive values).
4. **Competing risks**: Variant of survival — detect if event indicator has >2 levels (0=censor, 1=event A, 2=event B).
5. **Clustered data**: Not an outcome type but a data structure. Detect and flag — methods should account for clustering regardless of outcome type.
