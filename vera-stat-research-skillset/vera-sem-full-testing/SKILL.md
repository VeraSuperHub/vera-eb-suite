---
name: vera-sem-full-testing
description: >-
  Structural equation modeling skill. Collects latent constructs and
  path structure, checks identification and estimator requirements, fits one
  primary SEM, and reports global fit plus key structural paths with a
  recommendation block for advanced analyses. Trigger when the user asks
  for SEM, latent path analysis, full structural equation modeling, path
  coefficients, structural paths, mediation model, latent variable model,
  causal SEM, direct and indirect effects, or path diagram. Does not handle
  CFA-only models (use vera-sem-cfa-testing) or longitudinal growth models
  (use vera-sem-longchange-testing).
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# Full SEM Testing — Initial Structural Model

Open-source skill.

## Workflow

Read each step file in `workflow/` before executing that step.

| Step | File | Executor | Output |
|---|---|---|---|
| Collect | `workflow/01-collect-inputs.md` | Main Agent | Structured SEM summary |
| Diagnose | `workflow/02-check-model-setup.md` | Main Agent | Identification + estimator decision |
| Test | `workflow/03-run-primary-sem.md` | Main Agent | Initial SEM fit + recommendation |

## Decision Tree

```
1. CHECK MEASUREMENT COMPONENT
   ├── latent factors specified → SEM path
   └── only observed variables → consider path analysis, but keep SEM framing explicit

2. CHECK STRUCTURAL COMPONENT
   ├── direct paths only → baseline SEM
   ├── mediation present → label indirect paths for later testing
   └── multigroup / longitudinal / nonlinear elements → recommend specialized SEM skills

3. CHECK ESTIMATOR
   ├── continuous indicators → ML / MLR
   └── categorical indicators → WLSMV / DWLS
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Latent constructs** | Factor names, theoretical meaning, indicators per factor |
| **Structural paths** | Which latent/observed variables predict which |
| **Mediators** | Any indirect paths (X → M → Y) |
| **Scale type** | Continuous, ordinal/Likert, binary indicators |
| **Grouping variable** | Optional; for later multi-group comparison |
| **Sample size** | Final analytic N and missing-data context |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Model Setup Checks (identification, estimator)
PART 2: Primary SEM Fit (global fit + structural coefficients)
PART 3: Recommendation Block
```

## Reporting Standards

1. Always report `chi-square`, `df`, `CFI`, `TLI`, `RMSEA`, and `SRMR`
2. Report standardized path coefficients with SE or CI
3. Report R-squared for endogenous latent variables
4. Identification problems must be stated explicitly, never silently patched
5. Mediation paths: label but do not test significance (recommend full analysis)
6. Ends with recommendation block for mediation testing,
   multi-group analysis, model modification, and indirect effect bootstrapping

## Failure Modes

- If model does not converge: report non-convergence, suggest simplifying structure
- If outcome type is CFA-only (no structural paths): redirect to `vera-sem-cfa-testing`
- If longitudinal growth structure detected: redirect to `vera-sem-longchange-testing`
