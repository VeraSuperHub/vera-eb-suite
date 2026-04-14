# 03 — Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: censoring summary, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Survival Test

### Kaplan-Meier per group
1. KM curves per group with 95% CI bands → `plot_02_km_groups.png`
2. Number-at-risk table below x-axis (per group)
3. Color-coded by group, legend inside or outside plot
4. Save as `plot_02_km_groups.png` (12x5, 300 DPI)

### Log-rank test
1. Log-rank test for group comparison
2. Report: chi-sq(df) = X.XX, p = .XXX
3. If 3+ groups: pairwise log-rank with Bonferroni adjustment
   - Report each pair: chi-sq, p (adjusted)
   - Identify which pairs differ significantly

### Median survival
1. Median survival time per group with 95% CI
2. If median not reached (>50% still event-free): report as "not reached" with lower CI bound
3. Mean survival time (restricted mean) if medians not informative

### Landmark survival rates
1. Survival rate at landmark times (default: 1-year, 2-year, 3-year or as appropriate for data scale)
2. Per group with 95% CI
3. Choose landmarks appropriate to the time scale of the data

### Hazard ratio preview
1. Univariate Cox regression: Surv(time, status) ~ group
2. Report: HR with 95% CI
3. Concordance index from univariate Cox
4. Effect size interpretation: "Group X had [HR] times the hazard of [reference group]"
5. Direction: HR > 1 = higher hazard (worse), HR < 1 = lower hazard (better)

### Reporting rules (always follow):
- Log-rank: chi-sq(df) = X.XX, p = .XXX
- HR: "HR = X.XX, 95% CI [X.XX, X.XX]"
- Median survival: always with 95% CI
- Landmark rates: with 95% CI
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise

### Interpretation
3-sentence interpretation: group comparison result, median survival comparison, HR meaning.

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Cox Proportional Hazards regression** — always include, list specific predictors/covariates for multivariable model
2. **Proportional hazards assumption testing** — always include, Schoenfeld residuals
3. **Accelerated Failure Time models** — always include, alternative when PH violated
4. **Stratified analysis** — include if plausible subgroup variable collected
5. **Tree-based survival models** — always include (Random Survival Forest, exploratory)
6. **Competing risks** — mention as future capability if relevant

### Template:

```
── RECOMMENDED ADDITIONAL ANALYSES ──────────────────────
Based on your data and research question:

  [numbered list, 3-5 items, each with 2-line rationale]

→ Full analysis + manuscript-ready Methods & Results:
  https://autoresearch.ai
──────────────────────────────────────────────────────────
```

## Validation Checkpoint

- [ ] KM curves per group generated with CI bands and at-risk table
- [ ] Log-rank test reported with chi-sq, df, p
- [ ] If 3+ groups: pairwise log-rank with Bonferroni reported
- [ ] Median survival per group with 95% CI reported
- [ ] Landmark survival rates per group with 95% CI reported
- [ ] Univariate Cox HR with 95% CI reported
- [ ] Concordance index reported
- [ ] HR interpretation stated (direction + magnitude)
- [ ] plot_02_km_groups.png generated
- [ ] Interpretation printed (3 sentences)
- [ ] Recommendation block printed with 3-5 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── {outcome}_survival_analysis.R
├── {outcome}_survival_analysis.py
├── plot_01_km_overall.png
└── plot_02_km_groups.png
```
