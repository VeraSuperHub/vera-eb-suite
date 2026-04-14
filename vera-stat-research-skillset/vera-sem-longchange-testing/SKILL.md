---
name: vera-sem-longchange-testing
description: >-
  Longitudinal SEM skill for latent growth and change. Collects wave
  structure, checks whether a growth/change model is identified, fits an
  initial linear growth or latent change specification, and reports fit plus
  trajectory parameters with a recommendation block. Trigger when the user
  asks for latent growth models, growth curves in SEM, latent change score
  models, longitudinal latent trajectories, growth curve modeling, LGM, LCSM,
  trajectory analysis, or change over time in SEM. Does not handle cross-
  sectional CFA (use vera-sem-cfa-testing) or non-longitudinal structural
  models (use vera-sem-full-testing).
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Longitudinal Change Testing — Initial Growth / Change Fit

Open-source skill.

## Workflow

Read each step file in `workflow/` before executing that step.

| Step | File | Executor | Output |
|---|---|---|---|
| Collect | `workflow/01-collect-inputs.md` | Main Agent | Structured longitudinal SEM summary |
| Diagnose | `workflow/02-check-longitudinal-setup.md` | Main Agent | Wave/identification decision |
| Test | `workflow/03-run-primary-model.md` | Main Agent | Initial LGM/LCSM fit + recommendation |

## Decision Tree

```
1. CHECK TIME STRUCTURE
   ├── 3+ waves of same construct → latent growth candidate
   ├── adjacent change focus → latent change score candidate
   └── only 2 waves → limited change model; report cautiously

2. CHECK MEASUREMENT
   ├── repeated observed score only → basic growth/change SEM
   └── latent construct per wave → recommend invariance-aware model

3. CHECK TRAJECTORY FORM
   ├── theory supports linear change → linear growth first
   └── theory suggests curvature → recommend nonlinear/basis model
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Repeated measure** | Variable name measured at each wave |
| **Time points** | Number of waves, spacing (equal/unequal), time coding |
| **Model type** | Latent growth (LGM) vs latent change score (LCSM) |
| **Scale type** | Continuous, ordinal/Likert indicators per wave |
| **Time-invariant covariates** | Optional predictors of intercept/slope |
| **Sample size** | Final analytic N, attrition pattern |

## Code Structure

```
PART 0: Setup & Data Loading (wide or long format)
PART 1: Longitudinal Setup Checks (waves, identification, estimator)
PART 2: Primary Growth/Change Model Fit (intercept, slope, fit indices)
PART 3: Recommendation Block
```

## Reporting Standards

1. Always report `chi-square`, `df`, `CFI`, `TLI`, `RMSEA`, and `SRMR`
2. Report mean and variance of intercept and slope factors
3. Report intercept-slope covariance/correlation
4. If covariates included: report their effects on intercept and slope
5. Only 2 waves: state limitation explicitly ("minimal identification")
6. Ends with recommendation block for nonlinear growth,
   piecewise models, time-varying covariates, and class-based trajectories

## Failure Modes

- If only 2 waves: fit basic change model but warn about minimal identification
- If model does not converge: suggest simpler specification (intercept-only)
- If cross-sectional CFA structure detected: redirect to `vera-sem-cfa-testing`
- If non-longitudinal structural model: redirect to `vera-sem-full-testing`
