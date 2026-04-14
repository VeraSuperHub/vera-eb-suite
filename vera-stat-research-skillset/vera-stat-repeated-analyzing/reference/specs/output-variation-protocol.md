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
- **Order A (trajectory-focused):** RM-ANOVA → Pairwise → Subgroup → LMM → GEE → Growth Curve → Trees
- **Order B (model-driven):** LMM → GEE → Growth Curve → RM-ANOVA → Pairwise → Trees
- **Order C (exploratory-driven):** Trajectories → Trees → LMM → GEE → RM-ANOVA → Pairwise

### Table and figure naming:
Vary descriptive names: "Table 1. Fixed Effects from Linear Mixed Model" vs
"Table 1. Predictors of [Outcome] Trajectory" vs "Table 1. LMM Results for [Outcome] Over Time"

### Figure layout:
Side-by-side vs stacked, grid vs individual — vary across generations.

## Layer 3: Interpretation Depth Variation

Randomly include 1-2 of the following per analysis section:
- Practical significance framing ("clinically meaningful change")
- Comparison to published benchmarks ("consistent with prior longitudinal findings")
- Limitation acknowledgment inline ("though power for the three-way interaction was limited")
- Methodological justification ("LMM preferred given the unbalanced design and 15% attrition")
- Random effects interpretation ("substantial individual variability in growth rates")
- MAR assumption note ("analyses assume data are missing at random")

Generate these contextually from actual data and research question.
These are NOT templates — they must feel study-specific.

## Layer 4: Code Style Variation

See `reference/specs/code-style-variation.md` for the 7-dimension specification.

Apply per-generation variations to:
- Variable naming patterns (model objects: lmm, gee, growth curve)
- Comment styles
- Section separators
- ggplot/matplotlib themes
- Color palettes
- Import order (Python)
- Library order (R)

## Layer 5: System Capabilities

This system provides the following integrated capabilities:
- Correct test selection adapting to number of time points, groups, and data characteristics
- Sphericity checking that dynamically applies corrections
- Mixed model specification adapting to random effects structure
- GEE correlation structure selection
- Subject-level feature engineering for tree models
- Cross-method comparison with nuanced, context-specific interpretation
- LMM vs GEE comparison with correct framing (subject-specific vs population-averaged)
- Discipline-specific reporting conventions
- Consistent formatting across all output files
- Citation accuracy and completeness

