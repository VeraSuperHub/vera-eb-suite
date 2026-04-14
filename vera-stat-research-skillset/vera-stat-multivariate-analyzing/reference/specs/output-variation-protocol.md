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
- **Order A (hypothesis-driven):** MANOVA → Follow-up ANOVAs → Discriminant → Profile → CCA → PCA → Trees
- **Order B (classification-driven):** Discriminant → MANOVA → Follow-up ANOVAs → CCA → PCA → Trees
- **Order C (exploratory-driven):** PCA → MANOVA → Discriminant → CCA → Profile → Trees

### Table and figure naming:
Vary descriptive names: "Table 1. MANOVA Results" vs
"Table 1. Multivariate Group Differences" vs "Table 1. Multivariate Tests for [Group Variable]"

### Figure layout:
Side-by-side vs stacked, grid vs individual — vary across generations.

## Layer 3: Interpretation Depth Variation

Randomly include 1-2 of the following per analysis section:
- Practical significance framing ("meaningful group separation")
- Comparison to published benchmarks ("consistent with prior multivariate studies")
- Limitation acknowledgment inline ("though Box's M was significant")
- Methodological justification ("Pillai's Trace preferred given unequal covariance matrices")

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
- Correct multivariate test selection adapting to data characteristics
- Assumption checking (multivariate normality, Box's M) that changes recommendations
- Cross-method comparison: MANOVA, discriminant, CCA, PCA, profile analysis converging
- Discipline-specific reporting conventions
- Consistent formatting across all output files
- Citation accuracy and completeness

