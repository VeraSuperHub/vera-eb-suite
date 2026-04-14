# 08 — Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Statistical Analysis

[Para 1: Multivariate distribution assessment — Mardia's test, Henze-Zirkler, Box's M, rationale]
[Para 2: MANOVA — test statistics reported, which primary, why, follow-up strategy]
[Para 3: Follow-up univariate ANOVAs — Bonferroni correction, pairwise comparisons]
[Para 4: Discriminant function analysis — purpose, classification approach]
[Para 5: MANCOVA / Two-way MANOVA / Profile analysis — if applicable, why included]
[Para 6: Canonical correlation — if applicable, purpose and interpretation approach]
[Para 7: PCA — purpose, rotation if applied, retention criteria]
[Para 8: Multivariate regression — if applicable, specification]
[Para 9: Tree-based — which models, exploratory framing, importance comparison rationale]
[Para 10: Software — R version, Python version, key packages with versions]
```

### Rules
- Write as if a human analyst chose these methods for THIS specific study
- Never expose general decision rules or pipeline logic
- State what was done + why + key parameters
- No results in methods; no code in methods
- Cite methodological references where appropriate
- Follow `reference/rules/reporting-standards.md`

### Quality: Methods variation
Apply paragraph-level randomization per `reference/specs/output-variation-protocol.md`:
- Each paragraph selects one framing from 3 options (test-first, purpose-first, data-first)
- Vary passive vs active voice across paragraphs (not within)
- Vary whether CI level and alpha are stated explicitly or implied

## Assemble results.md

### Section ordering logic

Choose ONE ordering based on research question emphasis:
- **Order A (hypothesis-driven):** MANOVA → Follow-up ANOVAs → Discriminant → Profile → CCA → PCA → Trees → Comparison
- **Order B (classification-driven):** Discriminant → MANOVA → Follow-up ANOVAs → CCA → PCA → Trees → Comparison
- **Order C (exploratory-driven):** PCA → MANOVA → Discriminant → CCA → Profile → Trees → Comparison

Select: "do groups differ on multiple DVs" → A. "which variables classify groups" → B. "what structure exists" → C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`

## Generate references.bib

- Include ONLY references actually cited in methods.md or results.md
- BibTeX format
- Include: methodological references, software citations, reporting guideline citations
- Key references: Tabachnick & Fidell, Mardia et al., Rencher, plus method-specific
- Do NOT pad with uncited references

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 8-10 paragraphs covering all analysis steps
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values — all numbers are computed
- [ ] All table/figure references in text match actual files
- [ ] p-value formatting follows reporting-standards.md rules
- [ ] MANOVA: all four test statistics in results (Pillai, Wilks, Hotelling-Lawley, Roy)
- [ ] Effect sizes present for every test in results.md
- [ ] Canonical correlations with Wilks' lambda tests (if CCA)
- [ ] references.bib includes all cited works and no uncited works
- [ ] Code style variation applied to final code.R and code.py
- [ ] No meta-commentary about pipeline structure in any output file
- [ ] Sentence bank applied with no repeated phrasing patterns

## Data Out → Final Deliverables

```
Deliverables:
├── multivariate_analysis.R       (PARTS 0-6, style-varied)
├── multivariate_analysis.py      (PARTS 0-6, style-varied)
├── methods.md                    (manuscript Methods section)
├── results.md                    (manuscript Results section)
├── references.bib                (cited works only)
├── tables/
│   ├── manova_table.csv
│   ├── univariate_anova_table.csv
│   ├── pairwise_table.csv
│   ├── discriminant_table.csv
│   ├── confusion_matrix.csv
│   ├── cca_table.csv
│   ├── pca_table.csv
│   ├── mvreg_table.csv
│   ├── importance_table.csv
│   └── convergence_table.csv
└── figures/
    ├── plot_01_scattermatrix.png
    ├── plot_02_groupmeans.png
    ├── plot_03_univariate_*.png
    ├── plot_04_discriminant.png
    ├── plot_05_interaction.png      (if two-way)
    ├── plot_06_profile.png          (if same scale)
    ├── plot_07_cca.png              (if predictors)
    ├── plot_08_profile_full.png     (if same scale)
    ├── plot_09_scree.png
    ├── plot_10_biplot.png
    ├── plot_11_territorial.png
    ├── plot_12_mv_regression.png    (if predictors)
    └── plot_13_importance_heatmap.png
```
