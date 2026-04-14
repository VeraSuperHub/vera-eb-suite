# 02 — Check Model Setup

## Executor: Main Agent

## Data In: measurement_model, structural_paths, indicator_type, N from 01-collect-inputs.md

## Measurement Block Validation

1. **Per-factor identification** — same rules as CFA
   - 3+ indicators: standard
   - 2 indicators: constrain or fix
   - 1 indicator: set error variance to (1 - reliability) * variance
2. **Weak measurement flag**
   - If any factor has only 2 indicators with expected low loadings, recommend CFA refinement first
   - "Measurement before structure" principle

## Structural Model Check

### Recursivity:
```
if all structural paths are one-directional (no feedback loops):
    model = "recursive" → standard estimation
elif feedback loops present:
    model = "nonrecursive" → requires instrumental variables or constraints
    flag: "Nonrecursive model detected — confirm this is intentional"
```

### Identification:
- Count free parameters vs data points (unique elements in cov matrix)
- df = p*(p+1)/2 - number_of_free_parameters (where p = number of observed variables)
- df must be > 0

## Estimator Selection

Same decision logic as CFA:
- Continuous + normal → ML or MLR
- Continuous + non-normal → MLR
- Ordinal/binary → WLSMV or DWLS

## Blocker Flagging

Flag before code generation:
- N < 10 * free_parameters → underpowered
- Endogenous variable without structural predictor → isolate or model
- Mediator with only direct path (no indirect path possible) → clarify
- Extremely complex model relative to N → simplify
- Categorical mediators with ML → switch to WLSMV or Bayesian

## Validation Checkpoint

- [ ] Measurement blocks all identified (3+ indicators per factor preferred)
- [ ] Structural model is recursive (or nonrecursive confirmed as intentional)
- [ ] Overall model df > 0 (over-identified)
- [ ] Estimator selected and justified
- [ ] N-to-parameter ratio checked (minimum 5:1, preferred 10:1)
- [ ] Mediators have both a and b paths (for indirect effects)
- [ ] No obvious blockers remaining

## Data Out → 03-run-primary-sem.md

```
recursive: true | false
estimator: ML | MLR | WLSMV
n_free_params: int
df: int
n_to_param_ratio: float
measurement_adequate: true | false
blockers: [] or [list of issues]
proceed: true | false
```
