# 02 — Check Distribution

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1: Trajectory Diagnostics

### Reshape (if needed)
- If data is wide format, convert to long format first
- Ensure columns: outcome, time, subject_id, group (if applicable)

### Spaghetti Plot
- Individual trajectories over time (one line per subject)
- Color/facet by group if between-subjects factor exists
- Overlay group mean trajectory with SE or 95% CI ribbons
- Save as `plot_01_trajectories.png` (12x5, 300 DPI)

### Descriptives per Time Point per Group
- Table: Time | Group | N | Mean | SD
- If no group variable: Time | N | Mean | SD

### Attrition Check
- N per time point (overall and per group)
- Flag if any time point has > 20% dropout from baseline N
- Print attrition table

### Distribution at Each Time Point
- Outcome distribution per time point (density or histogram)
- Check for floor/ceiling effects at any wave

### ICC (Intraclass Correlation Coefficient)
- How much variance is between-subjects vs within-subjects?
- Fit null model: outcome ~ 1 + (1 | subject)
- ICC = between-subject variance / total variance
- Interpretation:
  - ICC > 0.05: substantial clustering, mixed models appropriate
  - ICC < 0.05: minimal clustering, simpler methods may suffice (but still proceed with RM design)
- Print ICC value with interpretation

### Sphericity Note (if 3+ time points)
- Print note: "With [N] time points, repeated measures ANOVA requires sphericity. Mauchly's test will be conducted in the primary test step."

### Decision Logic (printed in console)

```
if n_timepoints == 2:
    → "Two time points detected. Paired comparison will be used."
    → test_path = "paired"
elif n_levels == 0 or n_levels == 1:
    → "3+ time points, single group. One-way RM-ANOVA will be used."
    → test_path = "rm_anova"
else:
    → "3+ time points, [n_levels] groups. Mixed ANOVA (time × group) will be used."
    → test_path = "mixed_anova"
```

### Interpretation
Print 3-4 sentences: trajectory patterns observed, ICC magnitude and what it means for the analysis, attrition assessment, and test path decision.

## Validation Checkpoint

- [ ] Data reshaped to long format if originally wide
- [ ] Spaghetti plot with individual trajectories generated
- [ ] Group mean ribbons overlaid (if groups exist)
- [ ] plot_01_trajectories.png saved
- [ ] Descriptives per time point per group complete (N, M, SD)
- [ ] Attrition table printed with N per time point
- [ ] Attrition flag raised if > 20% dropout at any wave
- [ ] ICC computed and interpreted
- [ ] Sphericity note printed (if 3+ time points)
- [ ] Test path decision printed
- [ ] Distribution checked at each time point

## Data Out → 03-run-primary-test.md

```
test_path: "paired" | "rm_anova" | "mixed_anova"
icc_value: float
attrition_flag: true | false
descriptives_table: [{time, group, n, mean, sd}]
trajectory_code_r: [PART 1 R code block]
trajectory_code_py: [PART 1 Python code block]
```
