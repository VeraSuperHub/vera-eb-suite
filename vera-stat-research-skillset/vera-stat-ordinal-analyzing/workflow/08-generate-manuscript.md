# 08 — Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Statistical Analysis

[Para 1: Distribution assessment — frequency tables, cumulative proportions, sparse level check]
[Para 2: Nonparametric group comparison methods — which tests, why chosen for ordinal data]
[Para 3: Correlation methods — Spearman for continuous predictors, Goodman-Kruskal gamma for ordinal predictors]
[Para 4: Subgroup analysis methods — if applicable]
[Para 5: Ordinal logistic regression — proportional odds model, Brant test, alternative if violated]
[Para 6: Tree-based — which models, exploratory framing, ordinal outcome as classification]
[Para 7: Software — R version, Python version, key packages with versions]
```

### Rules
- Write as if a human analyst chose these methods for THIS specific study
- Never expose general decision rules or pipeline logic
- State what was done + why + key parameters
- No results in methods; no code in methods
- Cite methodological references where appropriate (Agresti for ordinal models, Brant for assumption test)
- Follow `reference/rules/reporting-standards.md`

### Quality: Methods variation
Apply paragraph-level randomization per `reference/specs/output-variation-protocol.md`:
- Each paragraph selects one framing from 3 options (test-first, purpose-first, data-first)
- Vary passive vs active voice across paragraphs (not within)
- Vary whether CI level and alpha are stated explicitly or implied

## Assemble results.md

### Section ordering logic

Choose ONE ordering based on research question emphasis:
- **Order A (hypothesis-driven):** Group comparison → Subgroup → Ordinal regression → Trees → Comparison
- **Order B (model-driven):** Ordinal regression → Group comparison → Subgroup → Trees → Comparison
- **Order C (exploratory-driven):** Distribution → Trees → Ordinal regression → Group comparison → Subgroup → Comparison

Select: "is there a difference" → A. "what predicts" → B. "what patterns exist" → C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`

## Generate references.bib

- Include ONLY references actually cited in methods.md or results.md
- BibTeX format
- Include: methodological references (Agresti, Brant, McCullagh), software citations, reporting guideline citations
- Do NOT pad with uncited references

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 7 paragraphs covering all analysis steps
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values — all numbers are computed
- [ ] All table/figure references in text match actual files
- [ ] p-value formatting follows reporting-standards.md rules
- [ ] Effect sizes present for every test in results.md
- [ ] Cumulative ORs reported with 95% CIs
- [ ] Medians and IQRs used (not means/SDs)
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
│   ├── polr_table.csv
│   ├── brant_table.csv
│   ├── importance_table.csv
│   └── comparison_table.csv
└── figures/
    ├── plot_01_ordinal_distribution.png
    ├── plot_02_stacked_bar_[var].png
    ├── plot_03_*.png             (additional test plots)
    ├── plot_04_subgroup_*.png    (if applicable)
    ├── plot_05_predicted_probs.png
    └── plot_06_importance.png
```
