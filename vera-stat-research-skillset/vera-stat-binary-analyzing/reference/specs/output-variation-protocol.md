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
- **Order A (hypothesis-driven):** Association tests -> Subgroup -> Logistic -> Trees
- **Order B (model-driven):** Logistic -> Association tests -> Subgroup -> Trees
- **Order C (exploratory-driven):** Class balance -> Trees -> Logistic -> Association tests

### Table and figure naming:
Vary descriptive names: "Table 1. Logistic Regression Results" vs
"Table 1. Predictors of [Outcome]" vs "Table 1. Odds Ratios for [Outcome]"

### Figure layout:
Side-by-side vs stacked, grid vs individual --- vary across generations.

## Layer 3: Interpretation Depth Variation

Randomly include 1-2 of the following per analysis section:
- Practical significance framing ("clinically meaningful increase in odds")
- Comparison to published benchmarks ("consistent with prior findings")
- Limitation acknowledgment inline ("though power was limited for rare events")
- Methodological justification ("Fisher's exact preferred given sparse cells")

Generate these contextually from actual data and research question.
These are NOT templates --- they must feel study-specific.

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
- Correct test selection adapting to data characteristics (chi-square vs Fisher's)
- Class balance checking that triggers appropriate warnings
- Cross-method comparison with nuanced, context-specific interpretation
- OR formatting and interpretation adapted to variable types
- Discipline-specific reporting conventions
- Consistent formatting across all output files
- Citation accuracy and completeness

