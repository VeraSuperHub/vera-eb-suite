# 02 — Check Follow-Up and Censoring

## Executor: Main Agent (code generation)

## Data In: Structured input summary from 01-collect-inputs.md

## Generate code for PART 1

### Follow-up time summary
- Median follow-up time (overall)
- Range (min, max)
- IQR (Q1, Q3)
- Mean follow-up with SD

### Censoring assessment
- Total N, number of events, number censored
- Censoring rate: % censored overall
- Censoring rate per group
- If censoring rate > 80%: issue warning — "Limited events detected ([X]% censored). Confidence intervals will be wide and estimates may be unstable."
- If censoring rate < 5%: note — "Very low censoring rate ([X]%). Standard regression may suffice, but survival analysis is still appropriate for time-to-event data."

### Kaplan-Meier overall survival curve
- KM curve for entire sample → `plot_01_km_overall.png`
- Include: 95% confidence band (shaded)
- Include: number-at-risk table below x-axis
- Include: median survival line (dashed horizontal at S=0.5, vertical to time axis)
- Label axes: "Time ([units])" and "Survival Probability"
- Save as `plot_01_km_overall.png` (12x5, 300 DPI)

### Event timeline
- Histogram of event/censoring times (stacked or side-by-side by event/censored)
- Or: event timeline plot showing events (X) and censoring (O) along time axis

### Interpretation
Print 2-3 sentences: follow-up summary, censoring assessment, and any warnings.

## Validation Checkpoint

- [ ] Median follow-up time reported with IQR
- [ ] Range (min, max) reported
- [ ] Censoring rate reported overall and per group
- [ ] High censoring (>80%) or low censoring (<5%) warning issued if applicable
- [ ] plot_01_km_overall.png generated with CI band and number-at-risk table
- [ ] Median survival line shown on KM plot
- [ ] Event/censoring time histogram or timeline generated
- [ ] Interpretation printed (2-3 sentences)

## Data Out → 03-run-primary-test.md

```
followup_summary: {median, iqr_q1, iqr_q3, min, max, mean, sd}
censoring_rate: {overall, per_group: [{group, rate}]}
n_events: int
n_censored: int
n_total: int
censoring_flag: "high" | "low" | "normal"
distribution_code_r: [PART 1 R code block]
distribution_code_py: [PART 1 Python code block]
```
