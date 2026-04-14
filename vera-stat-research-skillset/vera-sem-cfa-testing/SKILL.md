---
name: vera-sem-cfa-testing
description: >-
  Runs the CFA pipeline: collect indicator structure, check basic
  identification and estimator requirements, fit a primary CFA model, and
  report fit indices plus standardized loadings with a recommendation block for
  full SEM analysis. Trigger when the user asks for CFA, confirmatory factor
  analysis, measurement model testing, latent factor validation, factor
  loading assessment, construct validity, scale validation, measurement
  invariance check, or psychometric evaluation. Does not cover full structural
  path modeling (use vera-sem-full-testing) or longitudinal change modeling
  (use vera-sem-longchange-testing).
user-invocable: true
allowed-tools: Read, Bash, Write, Edit
---

# CFA Testing — Identification, Primary Fit, Recommendation

Open-source skill.

## Workflow

Read each step file in `workflow/` before executing that step.

| Step | File | Executor | Output |
|---|---|---|---|
| Collect | `workflow/01-collect-inputs.md` | Main Agent | Structured SEM input summary |
| Diagnose | `workflow/02-check-measurement-setup.md` | Main Agent | Identification + estimator decision |
| Test | `workflow/03-run-primary-cfa.md` | Main Agent | Initial CFA fit + recommendation block |

## Decision Tree

```
1. CHECK MODEL FORM
   ├── Reflective latent factors with named indicators → CFA path
   └── Structural relations without clear latent blocks → recommend sem-full

2. CHECK ESTIMATOR
   ├── Continuous, roughly normal indicators → ML / MLR
   ├── Continuous, non-normal indicators → robust ML
   └── Ordinal indicators → WLSMV / DWLS

3. CHECK IDENTIFICATION
   ├── Each factor has 3+ indicators → standard identification
   ├── 2 indicators → require theory + equality/variance constraints
   └── 1 indicator → do not fit as free CFA factor without extra constraints
```

## Required Inputs

| Role | What to collect |
|---|---|
| **Latent constructs** | Factor names and theoretical meaning |
| **Indicators** | Which observed variables load on each factor |
| **Scale type** | Continuous, ordinal/Likert, binary indicators |
| **Grouping variable** | Optional; for later invariance testing |
| **Sample size** | Final analytic N and missing-data context |

## Code Structure

```
PART 0: Setup & Data Loading
PART 1: Measurement Setup Checks
PART 2: Primary CFA Fit
PART 3: Recommendation Block
```

## Reporting Standards

1. Always report `chi-square`, `df`, `CFI`, `TLI`, `RMSEA`, and `SRMR`
2. Report standardized loadings with SE or CI when available
3. Say "fit was acceptable / borderline / poor" rather than "good" without context
4. Identification problems must be stated explicitly, never silently patched
5. Ends with a recommendation block for reliability/validity,
   invariance, and alternative-model comparison
