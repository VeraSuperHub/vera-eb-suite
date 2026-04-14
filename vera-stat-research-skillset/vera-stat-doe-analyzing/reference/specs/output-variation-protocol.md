# Output Quality Variation Protocol

Read this file before every generation. Apply all variation layers for natural, diverse, non-repetitive output.

## Layer 1: Phrasing Variation

For each statistical result, maintain 4-6 alternative phrasings. Select
contextually per generation. Never repeat the same phrasing pattern for
the same type of result within a single document.

See `reference/patterns/sentence-bank.md` for the full bank.

Rules:
- Rotate across paragraphs within the same document
- Select based on data context (factor names, direction, magnitude)
- Someone reading 10 outputs should see 10 different interpretive choices

## Layer 2: Structure Variation

### Section ordering (within scientific validity constraints):

Choose ONE ordering for results.md based on research question:
- **Order A (effect-driven):** ANOVA main effects -> Interactions -> Simple effects -> Contrasts -> RSM -> Trees
- **Order B (optimization-driven):** RSM -> ANOVA -> Effect ranking -> Optimal settings -> Trees
- **Order C (screening-driven):** Effect screening (half-normal) -> ANOVA -> Active effects -> Trees

### Table and figure naming:
Vary descriptive names: "Table 1. ANOVA Results" vs
"Table 1. Factorial Effects on [Response]" vs "Table 1. Main Effects and Interactions"

### Figure layout:
Side-by-side vs stacked, grid vs individual -- vary across generations.

## Layer 3: Interpretation Depth Variation

Randomly include 1-2 of the following per analysis section:
- Practical significance framing ("industrially meaningful improvement")
- Comparison to published benchmarks ("consistent with prior experimental findings")
- Limitation acknowledgment inline ("though replication was limited")
- Methodological justification ("Type III SS used to ensure invariance to cell frequencies")
- Design efficiency note ("the fractional design achieved Resolution IV")

Generate these contextually from actual data and research question.
These are NOT templates -- they must feel study-specific.

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
- Correct model specification adapting to design type
- Assumption checking that changes the pipeline dynamically
- Cross-method comparison (ANOVA + RSM + trees) with nuanced interpretation
- Design-specific reporting (resolution for fractional, error terms for split-plot)
- Consistent formatting across all output files
- Citation accuracy and completeness

