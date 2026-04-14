# Step 01: Intake — Research Question & Data Inspection

> **Executor**: Main Agent
> **Input**: User's research question + data file path
> **Output**: `PIPELINE_STATE.json` with structured metadata + data profile

---

## Execution Instructions

### 1.1 Collect Research Context

Ask the user (or extract from $ARGUMENTS):

| Field | Required | Example |
|-------|----------|---------|
| Research question | Yes | "Does smoking status predict lung function decline?" |
| Hypotheses | Recommended | "Smokers have faster FEV1 decline than non-smokers" |
| Target discipline | Yes | Epidemiology, Psychology, Economics, etc. |
| Target venue/style | Optional | APA 7th, STROBE, JASA, etc. |
| Subgroup of interest | Optional | "Stratify by sex" |

If the user provided a clear research question in $ARGUMENTS, do not re-ask — extract and confirm.

### 1.2 Load and Inspect Data

1. Identify the data file path from user input
2. Determine format: CSV, Excel (.xlsx/.xls), RDS, SPSS (.sav), Stata (.dta), TSV, Parquet
3. Load using appropriate method:
   - CSV/TSV: `read.csv()` or `pandas.read_csv()`
   - Excel: `readxl::read_excel()` or `pandas.read_excel()`
   - RDS: `readRDS()`
   - SPSS: `haven::read_sav()` or `pyreadstat.read_sav()`
   - Stata: `haven::read_dta()` or `pyreadstat.read_dta()`
   - Parquet: `arrow::read_parquet()` or `pandas.read_parquet()`

4. Generate data profile:

```
Data Profile:
├── Dimensions: N rows × P columns
├── Column Types:
│   ├── Numeric: [list with ranges]
│   ├── Categorical: [list with level counts]
│   ├── Date/Time: [list]
│   └── Other: [list]
├── Missing Values:
│   ├── Total: X cells (Y%)
│   └── Per column: [columns with >5% missing]
├── Summary Statistics:
│   ├── Numeric: min, Q1, median, Q3, max, mean, SD
│   └── Categorical: mode, n_levels, top 5 levels with counts
└── Potential Issues:
    ├── Constant columns: [list]
    ├── Near-zero variance: [list]
    ├── High cardinality categoricals (>20 levels): [list]
    └── Suspected ID columns: [list]
```

### 1.3 Assign Variable Roles

Present the data profile and ask user to confirm:

1. **Outcome variable(s)**: Which column is the primary outcome?
2. **Predictor(s)**: Which columns are the main predictors/exposures?
3. **Covariates**: Which columns are confounders/adjusters?
4. **Subgroup variable**: Which column for stratified analysis? (optional)
5. **Exclusion criteria**: Any rows to exclude? (optional)
6. **Clustering/nesting**: Any hierarchical structure? (e.g., patients within hospitals)

If the research question clearly implies roles (e.g., "Does X predict Y?"), pre-assign and confirm.

### 1.4 Write Initial State

Write `PIPELINE_STATE.json`:

```json
{
  "stage": 1,
  "status": "completed",
  "research_question": "...",
  "hypotheses": ["..."],
  "discipline": "...",
  "venue_style": "...",
  "data_file": "/path/to/data.csv",
  "data_format": "csv",
  "n_rows": 500,
  "n_cols": 12,
  "variables": {
    "outcome": {"name": "fev1_decline", "type": "numeric", "n_unique": 487, "missing_pct": 0.2},
    "predictors": [{"name": "smoking_status", "type": "factor", "levels": ["never", "former", "current"]}],
    "covariates": [{"name": "age", "type": "numeric"}, {"name": "sex", "type": "factor"}],
    "subgroup": {"name": "sex", "type": "factor", "levels": ["male", "female"]},
    "cluster": null
  },
  "exclusions": null,
  "timestamp": "2026-04-05T10:00:00"
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 1a | Data file exists | File found at path | Ask user to provide correct path |
| 1b | Data loads successfully | No read errors | Try alternative parser; report error |
| 1c | N > 0 | At least 1 row after exclusions | Abort — empty dataset |
| 1d | Outcome identified | outcome field populated | Ask user explicitly |
| 1e | At least 1 predictor | predictors array non-empty | Ask user explicitly |
| 1f | State file written | PIPELINE_STATE.json exists and valid JSON | Rewrite |

---

## Next Step
→ Step 02: Outcome Detection & Routing
