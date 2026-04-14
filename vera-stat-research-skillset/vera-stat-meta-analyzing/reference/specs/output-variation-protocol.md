# Output Quality Variation Protocol

Read this file before every generation. Apply all variation layers for natural, diverse, non-repetitive output.

## Layer 1: Phrasing Variation

For each statistical result, maintain 4-6 alternative phrasings. Select
contextually per generation. Never repeat the same phrasing pattern for
the same type of result within a single document.

See `reference/patterns/sentence-bank.md` for the full bank.

Rules:
- Rotate across paragraphs within the same document
- Select based on data context (effect direction, magnitude, k)
- Someone reading 10 outputs should see 10 different interpretive choices

## Layer 2: Structure Variation

### Section ordering (within scientific validity constraints):

Choose ONE ordering for results.md based on research question:
- **Order A (effect-driven):** Pooled estimate → Heterogeneity → Publication bias → Sensitivity → Moderators → Model comparison
- **Order B (bias-driven):** Pooled estimate → Publication bias → Sensitivity → Heterogeneity → Moderators → Model comparison
- **Order C (moderator-driven):** Pooled estimate → Heterogeneity → Moderators → Sensitivity → Publication bias → Model comparison

### Table and figure naming:
Vary descriptive names: "Table 1. Pooled Effect Sizes" vs
"Table 1. Summary of Meta-Analytic Models" vs "Table 1. Random-Effects Estimates"

### Figure layout:
Forest plot annotations: left-aligned vs right-aligned study labels.
Funnel plot: standard vs contour-enhanced. Vary across generations.

## Layer 3: Interpretation Depth Variation

Randomly include 1-2 of the following per analysis section:
- Clinical significance framing ("the pooled effect exceeds the MCID")
- Comparison to published benchmarks ("consistent with prior meta-analyses")
- Limitation acknowledgment inline ("though k was limited for this subgroup")
- Methodological justification ("REML preferred given unequal study sizes")

Generate these contextually from actual data and research question.
These are NOT templates — they must feel study-specific.

## Layer 4: Code Style Variation

See `reference/specs/code-style-variation.md` for the 7-dimension specification.

Apply per-generation variations to:
- Variable naming patterns (model objects, data frames)
- Comment styles
- Section separators
- Forest plot / funnel plot styling
- Color palettes
- Import order (Python)
- Library order (R)

## Layer 5: System Capabilities

This system provides the following integrated capabilities:
- Correct effect size computation adapting to input format
- Heterogeneity assessment that changes the pipeline dynamically
- Cross-method comparison with nuanced, context-specific interpretation
- Publication bias assessment with multiple complementary tests
- Discipline-specific reporting conventions (PRISMA, Cochrane, APA)
- Consistent formatting across all output files
- Citation accuracy and completeness

