# 08 — Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Statistical Analysis

[Para 1: Outcome description — nominal variable, number of classes, reference category]
[Para 2: Association tests — Chi-square/Fisher's for categorical, ANOVA/Kruskal-Wallis for continuous predictors]
[Para 3: Subgroup analysis methods — if applicable]
[Para 4: Multinomial logistic regression — baseline-category logit, reference category, RRR interpretation]
[Para 5: Linear Discriminant Analysis — classification and variable importance via loadings]
[Para 6: Tree-based — CART, RF, LightGBM multi-class, exploratory framing, hyperparameters]
[Para 7: Model comparison — unified importance, no accuracy horse-race, lens philosophy]
[Para 8: Software — R version, Python version, key packages with versions]
```

### Rules
- Write as if a human analyst chose these methods for THIS specific study
- Never expose general decision rules or pipeline logic
- State what was done + why + key parameters
- No results in methods; no code in methods
- Cite methodological references where appropriate
- Follow `reference/rules/reporting-standards.md`
- State reference category and justify choice

### Quality: Methods variation
Apply paragraph-level randomization per `reference/specs/output-variation-protocol.md`:
- Each paragraph selects one framing from 3 options (test-first, purpose-first, data-first)
- Vary passive vs active voice across paragraphs (not within)
- Vary whether CI level and alpha are stated explicitly or implied

## Assemble results.md

### Section ordering logic

Choose ONE ordering based on research question emphasis:
- **Order A (classification-driven):** Association tests → Multinomial → LDA → Trees → Comparison
- **Order B (predictor-driven):** Multinomial → Association tests → LDA → Trees → Comparison
- **Order C (exploratory-driven):** Class distribution → Trees → LDA → Multinomial → Association tests → Comparison

Select: "which class does X belong to" → A. "what predicts class membership" → B. "what patterns exist" → C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`
- RRR always reported relative to stated reference category
- Confusion matrices: note in-sample caveat explicitly

## Generate references.bib

- Include ONLY references actually cited in methods.md or results.md
- BibTeX format
- Include: methodological references, software citations, reporting guideline citations
- Do NOT pad with uncited references

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 8 paragraphs covering all analysis steps
- [ ] Reference category stated and justified in methods.md
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values — all numbers are computed
- [ ] RRR reported with 95% CI relative to reference category
- [ ] Confusion matrices include in-sample caveat
- [ ] All table/figure references in text match actual files
- [ ] p-value formatting follows reporting-standards.md rules
- [ ] Effect sizes present for every test in results.md
- [ ] references.bib includes all cited works and no uncited works
- [ ] Code style variation applied to final code.R and code.py
- [ ] No meta-commentary about pipeline structure in any output file
- [ ] Sentence bank applied with no repeated phrasing patterns

## Data Out → Final Deliverables

```
Deliverables:
├── {outcome}_analysis.R          (PARTS 0-6, style-varied)
├── {outcome}_analysis.py         (PARTS 0-6, style-varied)
├── methods.md                    (manuscript Methods section)
├── results.md                    (manuscript Results section)
├── references.bib                (cited works only)
├── tables/
│   ├── multinomial_coef_table.csv
│   ├── lda_loadings_table.csv
│   ├── confusion_matrices.csv
│   ├── importance_table.csv
│   └── comparison_table.csv
└── figures/
    ├── plot_01_class_distribution.png
    ├── plot_02_association_[var].png
    ├── plot_03_*.png             (additional predictor plots)
    ├── plot_04_subgroup_*.png    (if applicable)
    ├── plot_05_multinomial_rrr.png
    ├── plot_06_lda_scores.png
    ├── plot_07_cart_tree.png
    ├── plot_08_rf_importance.png
    ├── plot_09_lgbm_importance.png
    └── plot_10_unified_importance.png
```
