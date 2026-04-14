# 03 — Run Primary Test + Recommendation Block

## Executor: Main Agent (code generation)

## Data In: distribution_flag, overdispersion_ratio, zero_proportion, PART 1 code from 02-check-distribution.md

## Generate code for PART 2: Primary Test

### Model Selection
- If distribution_flag == "poisson" → use Poisson regression
- If distribution_flag == "negbin" or "zero_inflated" → use Negative Binomial regression
- If count_subtype == "event_rate" → include offset = log(exposure) in all models

### If 2 groups (n_levels == 2):
1. Group descriptives (n, mean count, SD per group)
2. If rate data: group rates (total events / total exposure per group)
3. Poisson or NB regression: outcome ~ group (+ offset if rate data)
4. Incidence rate ratio (IRR) = exp(coefficient) with 95% CI
5. Wald test or LR test for group effect
6. Mann-Whitney U as nonparametric confirmation
7. Bar chart of mean counts per group with error bars (SD) → `plot_02_mean_counts_[groupvar].png`
8. 3-sentence interpretation: group difference, IRR magnitude, nonparametric agreement

### If 3+ groups (n_levels >= 3):
1. Group descriptives (n, mean count, SD per group)
2. If rate data: group rates per group
3. Poisson or NB regression: outcome ~ group (+ offset if rate data)
4. Likelihood ratio test for overall group effect (deviance chi-square)
5. IRR for each group level vs reference with 95% CI
6. Kruskal-Wallis as nonparametric confirmation
7. Bar chart of mean counts per group with error bars → `plot_02_mean_counts_[groupvar].png`
8. 3-sentence interpretation: overall effect, which groups differ, nonparametric agreement

### Reporting rules (always follow):
- IRR: always report as "IRR = X.XX, 95% CI [X.XX, X.XX]"
- Rate (if applicable): "X.XX events per [unit] of exposure"
- p-values: "< .001" not "0.000", exact to 3 decimals otherwise
- Overdispersion: mention if NB was chosen due to overdispersion
- Degrees of freedom: always with chi-square and LR test statistics

## Generate PART 3: Recommendation Block

### Logic for building recommendations:

1. **Poisson/NB regression with covariates** — always include, list specific predictors/covariates
2. **Zero-inflated models** — include if zero_proportion > 0.15 (even below threshold, mention as option)
3. **Subgroup analysis** — include if plausible subgroup variable collected
4. **Hurdle model** — include if excess zeros detected
5. **Tree-based exploratory models** — always include with sample size caveat

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

- [ ] Group descriptives printed (n, mean count, SD per group)
- [ ] If rate data: rates per group reported
- [ ] Primary test executed with correct model (Poisson or NB based on distribution_flag)
- [ ] If rate data: offset = log(exposure) included
- [ ] IRR reported with 95% CI
- [ ] LR test or Wald test p-value reported
- [ ] Nonparametric confirmation test reported (Mann-Whitney U or Kruskal-Wallis)
- [ ] plot_02 generated (bar chart of mean counts with error bars)
- [ ] Interpretation printed (3 sentences)
- [ ] Recommendation block printed with 3-5 items
- [ ] AutoResearch API link included

## Data Out → Final .R and .py scripts

Assemble PART 0 + PART 1 + PART 2 + PART 3 into complete scripts.
Both must be fully runnable with only the data path changed.
```
Deliverables:
├── {outcome}_analysis.R
├── {outcome}_analysis.py
├── plot_01_count_distribution.png
└── plot_02_mean_counts_[var].png
```
