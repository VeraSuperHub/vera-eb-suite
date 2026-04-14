# 08 -- Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Experimental Design

[Para 1: Design description -- type (CRD/RCBD/factorial/fractional/split-plot/Latin square),
 factors with levels, blocking structure, replication, total N]

### Statistical Analysis

[Para 2: ANOVA approach -- Type III SS, full factorial model specification,
 why Type III (unbalanced or as default), partial eta-squared as effect size]
[Para 3: Post-hoc methods -- Tukey HSD for main effects, simple effects for interactions,
 contrast analysis with adjustment method]
[Para 4: Effect estimation -- half-normal or Pareto method, Daniel/Lenth if unreplicated]
[Para 5: Response surface methodology -- if applicable: first-order, lack-of-fit,
 second-order, canonical analysis, contour interpretation]
[Para 6: Residual diagnostics -- what was checked and criteria for concern]
[Para 7: Tree-based -- RF and LightGBM as exploratory, no hyperparameter tuning,
 importance as corroboration of ANOVA]
[Para 8: Software -- R version, Python version, key packages with versions]
```

### Rules
- Write as if a human analyst chose these methods for THIS specific experiment
- Never expose general decision rules or pipeline logic
- State what was done + why + key parameters
- No results in methods; no code in methods
- Since this IS a designed experiment, "explained" is appropriate for R-squared
- Cite methodological references where appropriate
- Follow `reference/rules/reporting-standards.md`

### Quality: Methods variation
Apply paragraph-level randomization per `reference/specs/output-variation-protocol.md`:
- Each paragraph selects one framing from 3 options (design-first, purpose-first, assumption-first)
- Vary passive vs active voice across paragraphs (not within)
- Vary whether alpha and CI level are stated explicitly or implied

## Assemble results.md

### Section ordering logic

Choose ONE ordering based on research question emphasis:
- **Order A (effect-driven):** ANOVA main effects -> Interactions -> Simple effects -> Contrasts -> RSM -> Trees -> Comparison
- **Order B (optimization-driven):** RSM -> ANOVA -> Effect ranking -> Optimal settings -> Trees -> Comparison
- **Order C (screening-driven):** Effect screening (half-normal) -> ANOVA -> Active effects deep-dive -> Trees -> Comparison

Select: "which factors matter" -> A. "what settings optimize" -> B. "which effects are active" -> C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`

## Generate references.bib

- Include ONLY references actually cited in methods.md or results.md
- BibTeX format
- Core DOE references to draw from:
  - Montgomery, D. C. (2017). Design and Analysis of Experiments (9th ed.). Wiley.
  - Box, G. E. P., Hunter, J. S., & Hunter, W. G. (2005). Statistics for Experimenters (2nd ed.). Wiley.
  - Myers, R. H., Montgomery, D. C., & Anderson-Cook, C. M. (2016). Response Surface Methodology (4th ed.). Wiley.
  - Wu, C. F. J., & Hamada, M. S. (2021). Experiments: Planning, Analysis, and Optimization (3rd ed.). Wiley.
- Plus software citations and reporting guideline citations as used
- Do NOT pad with uncited references

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 7-8 paragraphs covering all analysis steps performed
- [ ] methods.md includes experimental design description paragraph
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values -- all numbers are computed
- [ ] All table/figure references in text match actual files
- [ ] p-value formatting follows reporting-standards.md rules
- [ ] Partial eta-squared present for every F-test in results.md
- [ ] Effect estimates with SE for all contrasts
- [ ] RSM results include stationary point classification (if applicable)
- [ ] Design resolution stated for fractional factorial (if applicable)
- [ ] references.bib includes all cited works and no uncited works
- [ ] Code style variation applied to final code.R and code.py
- [ ] No meta-commentary about pipeline structure in any output file
- [ ] Sentence bank applied with no repeated phrasing patterns

## Data Out -> Final Deliverables

```
Deliverables:
├── {response}_doe_analysis.R          (PARTS 0-6, style-varied)
├── {response}_doe_analysis.py         (PARTS 0-6, style-varied)
├── methods.md                         (manuscript Methods section)
├── results.md                         (manuscript Results section)
├── references.bib                     (cited works only)
├── tables/
│   ├── anova_table.csv
│   ├── effect_estimates.csv
│   ├── contrast_table.csv
│   ├── rsm_coefficients.csv           (if applicable)
│   ├── importance_table.csv
│   └── comparison_table.csv
└── figures/
    ├── plot_01_interaction.png
    ├── plot_02_effects.png
    ├── plot_03_effect_ranking.png
    ├── plot_04_block_forest.png        (if applicable)
    ├── plot_05_halfnormal.png          (or pareto_effects)
    ├── plot_06_contour.png             (if RSM)
    ├── plot_07_surface.png             (if RSM)
    ├── plot_08_residual_diagnostics.png
    └── plot_09_importance.png
```
