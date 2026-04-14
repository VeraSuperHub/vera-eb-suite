# 08 — Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Statistical Analysis

[Para 1: Repeated measures design — describe time points, subjects, groups, data structure]
[Para 2: RM-ANOVA / Mixed ANOVA — sphericity test, corrections, effects tested]
[Para 3: Pairwise comparisons — simple effects, correction method, which contrasts]
[Para 4: Subgroup analysis methods — if applicable, three-way interaction]
[Para 5: Linear mixed models — random effects specification, estimation method (REML/ML), df method]
[Para 6: GEE — correlation structure, robust SE, population-averaged framing]
[Para 7: Growth curve — polynomial degree, random effects, trajectory modeling]
[Para 8: Tree-based — subject-level feature engineering, RF and LightGBM, exploratory framing]
[Para 9: Model comparison — assumption table, unified importance, convergence assessment]
[Para 10: Software — R version, Python version, key packages with versions:
  lme4, lmerTest, nlme, geepack, emmeans, rstatix, randomForest, lightgbm,
  statsmodels, pingouin, scipy, sklearn, lightgbm]
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
- **Order A (trajectory-focused):** RM-ANOVA/Mixed ANOVA → Pairwise → Subgroup → LMM → GEE → Growth Curve → Trees → Comparison
- **Order B (model-driven):** LMM → GEE → Growth Curve → RM-ANOVA as supplementary → Pairwise → Subgroup → Trees → Comparison
- **Order C (exploratory-driven):** Descriptive trajectories → Trees → LMM → GEE → Growth Curve → RM-ANOVA → Pairwise → Subgroup → Comparison

Select: "does the outcome change differently across groups?" → A. "what predicts individual trajectories?" → B. "what patterns exist in the data?" → C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`

## Generate references.bib

Include ONLY references actually cited in methods.md or results.md. Common references:

- Laird, N. M., & Ware, J. H. (1982). Random-effects models for longitudinal data. *Biometrics*, 38(4), 963-974.
- Liang, K. Y., & Zeger, S. L. (1986). Longitudinal data analysis using generalized linear models. *Biometrika*, 73(1), 13-22.
- Bates, D., Machler, M., Bolker, B., & Walker, S. (2015). Fitting linear mixed-effects models using lme4. *Journal of Statistical Software*, 67(1), 1-48.
- Greenhouse, S. W., & Geisser, S. (1959). On methods in the analysis of profile data. *Psychometrika*, 24(2), 95-112.
- Mauchly, J. W. (1940). Significance test for sphericity of a normal n-variate distribution. *The Annals of Mathematical Statistics*, 11(2), 204-209.
- Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical linear models: Applications and data analysis methods* (2nd ed.). Sage.
- Halekoh, U., Hojsgaard, S., & Yan, J. (2006). The R package geepack for generalized estimating equations. *Journal of Statistical Software*, 15(2), 1-11.
- Kuznetsova, A., Brockhoff, P. B., & Christensen, R. H. B. (2017). lmerTest package: Tests in linear mixed effects models. *Journal of Statistical Software*, 82(13), 1-26.

BibTeX format. Do NOT pad with uncited references.

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 10 paragraphs covering all analysis steps
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values — all numbers are computed
- [ ] All table/figure references in text match actual files
- [ ] p-value formatting follows reporting-standards.md rules
- [ ] Effect sizes present for every test in results.md
- [ ] Fixed effects reported with B, SE, CI, df, t, p
- [ ] Random effects reported with variance and SD
- [ ] ICC reported with interpretation
- [ ] Sphericity reported (Mauchly W, p; GG epsilon if violated)
- [ ] GEE working correlation structure stated
- [ ] Missing data / attrition pattern described
- [ ] MAR assumption stated if LMM used
- [ ] references.bib includes all cited works and no uncited works
- [ ] Code style variation applied to final code.R and code.py
- [ ] No meta-commentary about pipeline structure in any output file
- [ ] Sentence bank applied with no repeated phrasing patterns

## Data Out → Final Deliverables

```
Deliverables:
├── {outcome}_repeated_analysis.R      (PARTS 0-6, style-varied)
├── {outcome}_repeated_analysis.py     (PARTS 0-6, style-varied)
├── methods.md                         (manuscript Methods section)
├── results.md                         (manuscript Results section)
├── references.bib                     (cited works only)
├── tables/
│   ├── descriptives_table.csv
│   ├── pairwise_by_time.csv
│   ├── pairwise_by_group.csv
│   ├── simple_effects.csv
│   ├── lmm_ri_fixed.csv
│   ├── lmm_rs_fixed.csv
│   ├── lmm_random.csv
│   ├── gee_fixed.csv
│   ├── growth_curve_fixed.csv
│   ├── lmm_comparison.csv
│   ├── assumption_comparison.csv
│   └── importance_table.csv
└── figures/
    ├── plot_01_trajectories.png
    ├── plot_02_interaction.png
    ├── plot_03_subgroup_forest.png    (if applicable)
    ├── plot_04_growth_curves.png
    ├── plot_05_lmm_diagnostics.png
    ├── plot_06_coef_forest.png
    └── plot_07_rf_importance.png
```
