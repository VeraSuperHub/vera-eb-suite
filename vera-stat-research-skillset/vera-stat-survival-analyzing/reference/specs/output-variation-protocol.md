# Output Quality Variation Protocol

Read this file before every generation. Apply all variation layers for natural, diverse, non-repetitive output.

## Layer 1: Phrasing Variation

For each statistical result, maintain 4-6 alternative phrasings. Select
contextually per generation. Never repeat the same phrasing pattern for
the same type of result within a single document.

See `reference/patterns/sentence-bank.md` for the full bank.

Rules:
- Rotate across paragraphs within the same document
- Select based on data context (variable names, direction, HR magnitude)
- Someone reading 10 outputs should see 10 different interpretive choices

## Layer 2: Structure Variation

### Section ordering (within scientific validity constraints):

Choose ONE ordering for results.md based on research question:
- **Order A (hypothesis-driven):** KM/Log-rank → Subgroup → Cox → AFT → Trees
- **Order B (model-driven):** Cox → KM/Log-rank → Subgroup → AFT → Trees
- **Order C (exploratory-driven):** KM/Censoring → Trees → Cox → AFT → Groups

### Table and figure naming:
Vary descriptive names: "Table 1. Cox Regression Results" vs
"Table 1. Predictors of Survival" vs "Table 1. Hazard Ratios for [Outcome]"

### Figure layout:
Side-by-side vs stacked, grid vs individual — vary across generations.

## Layer 3: Interpretation Depth Variation

Randomly include 1-2 of the following per analysis section:
- Clinical significance framing ("a 40% reduction in hazard is clinically meaningful")
- Comparison to published benchmarks ("consistent with prior survival studies")
- Limitation acknowledgment inline ("though the PH assumption was borderline")
- Methodological justification ("AFT preferred given PH violation for [predictor]")

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
- Correct handling of censored data across all models
- PH assumption checking that dynamically adjusts the pipeline
- Cross-method comparison (Cox vs AFT vs RSF) with nuanced interpretation
- Discipline-specific reporting (HR vs TR framing for different audiences)
- Consistent formatting across all output files
- Citation accuracy and completeness

