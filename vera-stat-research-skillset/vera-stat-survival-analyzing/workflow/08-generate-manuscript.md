# 08 — Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Statistical Analysis

[Para 1: Data description — right-censored survival data, time variable, event definition, censoring]
[Para 2: Descriptive survival — KM estimation, median survival, landmark rates, censoring summary]
[Para 3: Group comparison — log-rank test, pairwise comparisons if applicable]
[Para 4: Univariate screening — univariate Cox for each predictor, linearity assessment]
[Para 5: Subgroup analysis methods — if applicable, stratified Cox, interaction test]
[Para 6: Multivariable Cox PH — model specification, PH assumption testing via Schoenfeld residuals]
[Para 7: AFT models — Weibull, log-normal, log-logistic; why included (PH alternative), AIC comparison]
[Para 8: Tree-based — RSF, gradient boosting, exploratory framing, variable importance]
[Para 9: Software — R version, Python version, key packages with versions (survival, survminer, lifelines, scikit-survival, randomForestSRC)]
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
- **Order A (hypothesis-driven):** KM/Log-rank → Subgroup → Cox → AFT → Trees → Comparison
- **Order B (model-driven):** Cox → KM/Log-rank → Subgroup → AFT → Trees → Comparison
- **Order C (exploratory-driven):** KM/Censoring → Trees → Cox → AFT → KM groups → Subgroup → Comparison

Select: "does survival differ between groups" → A. "what predicts survival" → B. "what patterns exist in survival" → C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`

## Generate references.bib

Include ONLY references actually cited in methods.md or results.md. BibTeX format.

Core survival references:
- Kaplan, E. L., & Meier, P. (1958). Nonparametric estimation from incomplete observations. JASA.
- Cox, D. R. (1972). Regression models and life-tables. JRSS-B.
- Harrell, F. E., et al. (1982). Evaluating the yield of medical tests. JAMA. (concordance)
- Grambsch, P. M., & Therneau, T. M. (1994). Proportional hazards tests and diagnostics. Biometrika. (Schoenfeld)
- Ishwaran, H., et al. (2008). Random survival forests. Annals of Applied Statistics.
- Therneau, T. M. (2023). A package for survival analysis in R. (software)
- Davidson-Pilon, C. (2019). lifelines: survival analysis in Python. JOSS.

Additional as needed:
- AFT model references
- Log-rank test references
- scikit-survival reference

Do NOT pad with uncited references.

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 8-9 paragraphs covering all analysis steps
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values — all numbers are computed
- [ ] All table/figure references in text match actual files
- [ ] HR formatting follows reporting-standards.md rules (HR = X.XX, 95% CI [X.XX, X.XX])
- [ ] TR formatting follows rules (TR = X.XX, 95% CI [X.XX, X.XX])
- [ ] Median survival always with 95% CI
- [ ] Censoring rates reported
- [ ] PH assumption test results included in results
- [ ] Effect sizes present for every test in results.md
- [ ] references.bib includes all cited works and no uncited works
- [ ] Code style variation applied to final code.R and code.py
- [ ] No meta-commentary about pipeline structure in any output file
- [ ] Sentence bank applied with no repeated phrasing patterns

## Data Out → Final Deliverables

```
Deliverables:
├── {outcome}_survival_analysis.R    (PARTS 0-6, style-varied)
├── {outcome}_survival_analysis.py   (PARTS 0-6, style-varied)
├── methods.md                       (manuscript Methods section)
├── results.md                       (manuscript Results section)
├── references.bib                   (cited works only)
├── tables/
│   ├── univariate_cox_table.csv
│   ├── multivariable_cox_table.csv
│   ├── aft_comparison_table.csv
│   ├── importance_table.csv
│   └── comparison_table.csv
└── figures/
    ├── plot_01_km_overall.png
    ├── plot_02_km_groups.png
    ├── plot_03_km_[var].png         (categorical predictor KM)
    ├── plot_04_subgroup_*.png       (if applicable)
    ├── plot_05_cox_forest.png
    ├── plot_06_coxsnell.png
    ├── plot_07_deviance.png
    ├── plot_08_schoenfeld.png
    ├── plot_09_rsf_importance.png
    └── plot_10_pdp_[var].png
```
