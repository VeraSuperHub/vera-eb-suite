# 02 — Check Longitudinal Setup

## Executor: Main Agent

## Data In: construct, waves, time_spacing, sample_size, model_candidate from 01-collect-inputs.md

## Wave Ordering Verification

1. Confirm waves are correctly ordered chronologically
2. Verify time coding for growth model:
   - Equal spacing: loadings fixed at 0, 1, 2, ... (or 0, 1, 2, 3)
   - Unequal spacing: loadings fixed at actual time values (e.g., 0, 6, 12, 24 for months)
3. Check that no wave is entirely missing or has > 50% attrition

## Measurement Invariance Need

### Decision logic:
```
if construct is measured by multiple indicators at each wave:
    measurement_invariance = "required before growth modeling"
    note: "Strong (scalar) invariance needed for meaningful mean comparisons"
elif construct is a single observed variable per wave:
    measurement_invariance = "not applicable"
    note: "Proceed directly to growth/change model"
```

## Model Selection

### Starting model decision:
```
if research_question is "overall trajectory shape" or "rate of change":
    model = "linear latent growth model"
    parameters: intercept mean/variance, slope mean/variance, intercept-slope covariance
elif research_question is "adjacent wave-to-wave dynamics":
    model = "latent change score model"
    parameters: change factor means, proportional change coefficient, coupling
elif n_waves >= 5 and nonlinearity suspected:
    model = "latent basis growth model" (free time scores)
    note: "Start with linear, test latent basis as follow-up"
```

## Blocker Flagging

Flag before code generation:
- Only 2 waves → not a growth model, redirect to paired t-test / repeated measures
- N < 50 with 4+ parameters → convergence risk
- > 30% attrition at final wave → note FIML assumption and sensitivity
- Unequal spacing without explicit time coding → must specify loading matrix
- Data in long format → must reshape to wide for lavaan (or use definition variables)

## Validation Checkpoint

- [ ] At least 3 waves confirmed
- [ ] Time coding specified (equal or unequal with values)
- [ ] Data shape compatible with modeling approach (wide for lavaan)
- [ ] Measurement invariance need assessed
- [ ] Starting model selected (LGM or LCSM)
- [ ] Attrition pattern noted (FIML will handle MAR)
- [ ] No critical blockers remaining

## Data Out → 03-run-primary-model.md

```
n_waves: int
time_coding: [0, 1, 2, ...] or [0, 6, 12, 24]
model_type: linear_growth | latent_change_score | latent_basis
measurement_invariance: required | not_applicable
estimator: ML | MLR | WLSMV
attrition_flag: low | moderate | high
blockers: [] or [list of issues]
proceed: true | false
```
