# 08 — Generate Manuscript

## Executor: Main Agent (assembly)

## Data In: All code, prose, tables, plots, and style_vector from steps 04-07

## Assemble methods.md

### Structure (order fixed, content varies)

```markdown
## Methods

### Search Strategy and Study Selection
[Para 1: Brief note — defer to user's PRISMA flow; this skill covers analysis only]

### Effect Size Calculation
[Para 2: How effect sizes were computed or extracted — metric, direction convention]

### Pooled Estimation
[Para 3: Random-effects model as primary, REML estimator, DerSimonian-Laird for comparison]

### Heterogeneity Assessment
[Para 4: Q statistic, I², tau², prediction interval, thresholds used]

### Publication Bias
[Para 5: Funnel plot visual inspection, Egger's regression, Begg's rank, trim-and-fill]

### Sensitivity Analysis
[Para 6: Leave-one-out, influence diagnostics, cumulative meta-analysis]

### Moderator Analysis
[Para 7: Subgroup analysis (Q_between), meta-regression, if applicable]

### Additional Models
[Para 8: Knapp-Hartung, Bayesian, three-level — why each was included]

### Software
[Para 9: R version, metafor package with version, additional packages]
```

### Rules
- Write as if a human analyst chose these methods for THIS specific review
- Never expose general decision rules or pipeline logic
- State what was done + why + key parameters
- No results in methods; no code in methods
- Cite methodological references where appropriate
- Follow `reference/rules/reporting-standards.md`
- Reference PRISMA guidelines for overall structure

### Quality: Methods variation
Apply paragraph-level randomization per `reference/specs/output-variation-protocol.md`:
- Each paragraph selects one framing from 3 options (method-first, purpose-first, data-first)
- Vary passive vs active voice across paragraphs (not within)
- Vary whether heterogeneity thresholds are stated explicitly or cited

## Assemble results.md

### Section ordering logic

Choose ONE ordering based on research question emphasis:
- **Order A (effect-driven):** Pooled estimate → Heterogeneity → Publication bias → Sensitivity → Moderators → Model comparison
- **Order B (bias-driven):** Pooled estimate → Publication bias → Sensitivity → Heterogeneity → Moderators → Model comparison
- **Order C (moderator-driven):** Pooled estimate → Heterogeneity → Moderators → Sensitivity → Publication bias → Model comparison

Select: "what is the overall effect" → A. "is the evidence trustworthy" → B. "what explains variability" → C.

### Rules
- All statistics are final computed values (no placeholders)
- Apply sentence bank rotation from `reference/patterns/sentence-bank.md`
- Include 1-2 cross-references between sections where findings connect
- Tables and figures referenced by number (actual files in tables/ and figures/)
- Follow `reference/rules/reporting-standards.md`

## Generate references.bib

Required references (include only those actually cited):

- DerSimonian, R., & Laird, N. (1986). Meta-analysis in clinical trials. *Controlled Clinical Trials*, 7(3), 177-188.
- Higgins, J. P. T., & Thompson, S. G. (2002). Quantifying heterogeneity in a meta-analysis. *Statistics in Medicine*, 21(11), 1539-1558.
- Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *BMJ*, 315(7109), 629-634.
- Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank correlation test for publication bias. *Biometrics*, 50(4), 1088-1101.
- Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software*, 36(3), 1-48.
- Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method. *Biometrics*, 56(2), 455-463.
- Knapp, G., & Hartung, J. (2003). Improved tests for a random effects meta-regression. *Statistics in Medicine*, 22(17), 2693-2710.
- Hedges, L. V., & Vevea, J. L. (1998). Fixed- and random-effects models in meta-analysis. *Psychological Methods*, 3(4), 486-504.
- IntHout, J., Ioannidis, J. P. A., & Borm, G. F. (2014). The Hartung-Knapp-Sidik-Jonkman method. *BMC Medical Research Methodology*, 14, 25.
- Moher, D., et al. (2009). Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement. *PLoS Medicine*, 6(7), e1000097.
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ*, 372, n71.

## Apply code style variation

Apply style_vector from step 06 to final code.R and code.py per `reference/specs/code-style-variation.md`.

## Validation Checkpoint

- [ ] methods.md contains no results or numbers
- [ ] methods.md has 9 paragraphs covering all analysis steps
- [ ] results.md section order matches research question type
- [ ] results.md has no placeholder values — all numbers are computed
- [ ] All table/figure references in text match actual files
- [ ] p-value formatting follows reporting-standards.md rules
- [ ] Heterogeneity statistics present (Q, I², tau²)
- [ ] Publication bias results complete (Egger's, Begg's, trim-fill)
- [ ] references.bib includes all cited works and no uncited works
- [ ] Code style variation applied to final code.R and code.py
- [ ] No meta-commentary about pipeline structure in any output file
- [ ] Sentence bank applied with no repeated phrasing patterns
- [ ] PRISMA guidelines referenced

## Data Out → Final Deliverables

```
Deliverables:
├── meta_analysis.R               (PARTS 0-6, style-varied)
├── meta_analysis.py              (PARTS 0-6, style-varied)
├── methods.md                    (manuscript Methods section)
├── results.md                    (manuscript Results section)
├── references.bib                (cited works only)
├── tables/
│   ├── study_summary_table.csv
│   ├── leave1out_table.csv
│   ├── subgroup_table.csv
│   ├── metareg_table.csv
│   ├── model_comparison_table.csv
│   └── robustness_table.csv
└── figures/
    ├── plot_01_forest.png
    ├── plot_03_funnel.png
    ├── plot_03b_trimfill.png
    ├── plot_03c_cumulative.png
    ├── plot_04_subgroup_[mod].png
    └── plot_04_bubble_[mod].png
```
