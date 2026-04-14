# 02 — Check Measurement Setup

## Executor: Main Agent

## Data In: Factor structure, indicator type, N, estimator candidate from 01-collect-inputs.md

## Identification Check

1. **Per-factor identification**
   - 3+ indicators per factor: identified (standard)
   - 2 indicators per factor: requires constraint (equal loadings or fixed error variance)
   - 1 indicator per factor: not a latent CFA — redirect or fix error variance
2. **Model-level identification**
   - df > 0 required for testable model
   - 1-factor with 3 indicators: just-identified (df = 0), fit indices uninformative
   - Flag if total parameters exceed N/5 rule of thumb

## Estimator Selection

### Decision logic:
```
if indicator_type == "continuous" and distribution ~ normal:
    estimator = "ML" or "MLR" (robust for mild non-normality)
elif indicator_type == "continuous" and non-normal:
    estimator = "MLR" (Satorra-Bentler scaled chi-square)
elif indicator_type in ("ordinal", "binary"):
    estimator = "WLSMV" (default) or "DWLS"
    # Note: WLSMV uses polychoric/tetrachoric correlations
```

## Blocker Check

Flag and report before code generation:
- N < 10 * number_of_free_parameters → power concern
- Zero-variance indicators → remove or recode
- Perfect collinearity between indicators → check data entry
- Heywood cases likely (negative variance estimates) → note constraint strategy
- All factor correlations expected near 1.0 → consider single-factor or bifactor

## Scaling Method

- Default: marker-variable identification (first loading fixed to 1.0)
- Alternative: fixed-factor variance (all factor variances = 1.0)
- Effects-coded: only if explicitly requested

## Validation Checkpoint

- [ ] Every factor has sufficient indicators for identification
- [ ] Estimator justified by indicator type and distributional properties
- [ ] N-to-parameter ratio checked (minimum 5:1, preferred 10:1)
- [ ] No zero-variance or constant indicators
- [ ] Scaling method decided (marker-variable default)
- [ ] Any blockers reported to user with resolution options

## Data Out → 03-run-primary-cfa.md

```
identification_status: identified | just-identified | under-identified
estimator: ML | MLR | WLSMV | DWLS
scaling: marker | fixed_variance | effects_coded
n_free_params: int
n_to_param_ratio: float
blockers: [] or [list of issues]
proceed: true | false
```
