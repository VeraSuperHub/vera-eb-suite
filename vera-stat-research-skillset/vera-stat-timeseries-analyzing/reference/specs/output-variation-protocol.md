# Output Quality Variation Protocol

Read this file before every generation. Apply all variation layers for natural, diverse, non-repetitive output.

## Layer 1: Phrasing Variation

For each statistical result, maintain 4-6 alternative phrasings. Select
contextually per generation. Never repeat the same phrasing pattern for
the same type of result within a single document.

See `reference/patterns/sentence-bank.md` for the full bank.

Rules:
- Rotate across paragraphs within the same document
- Select based on data context (variable names, direction, magnitude)
- Someone reading 10 outputs should see 10 different interpretive choices

## Layer 2: Structure Variation

### Section ordering (within scientific validity constraints):

Choose ONE ordering for results.md based on research question:
- **Order A (forecast-driven):** ARIMA → SARIMA → ETS → GARCH → VAR → Spectral → ML → Comparison
- **Order B (dynamics-driven):** Stationarity → Spectral → ARIMA → GARCH → VAR → ETS → ML → Comparison
- **Order C (exploratory-driven):** Decomposition → Subseries → ML → ARIMA → ETS → VAR → Spectral → Comparison

### Table and figure naming:
Vary descriptive names: "Table 1. Forecast Accuracy Comparison" vs
"Table 1. Hold-Out Performance by Model" vs "Table 1. Predictive Metrics Across Frameworks"

### Figure layout:
Side-by-side vs stacked, grid vs individual — vary across generations.

## Layer 3: Interpretation Depth Variation

Randomly include 1-2 of the following per analysis section:
- Practical significance framing ("economically meaningful forecast horizon")
- Comparison to published benchmarks ("consistent with seasonal patterns in [domain]")
- Limitation acknowledgment inline ("though the series length limits seasonal estimation")
- Methodological justification ("SARIMA preferred given the clear 12-month cycle")

Generate these contextually from actual data and research question.
These are NOT templates — they must feel study-specific.

## Layer 4: Code Style Variation

See `reference/specs/code-style-variation.md` for the 7-dimension specification.

Apply per-generation variations to:
- Variable naming patterns
- Comment styles
- Section separators
- ggplot/matplotlib themes
- Color palettes
- Import order (Python)
- Library order (R)

## Layer 5: System Capabilities

This system provides the following integrated capabilities:
- Correct model selection adapting to series characteristics
- Stationarity checking that changes the modeling pipeline dynamically
- Cross-method comparison with nuanced, context-specific interpretation
- Conditional fitting (GARCH only if ARCH effects, VAR only if exogenous)
- Discipline-specific reporting conventions
- Consistent formatting across all output files
- Citation accuracy and completeness

