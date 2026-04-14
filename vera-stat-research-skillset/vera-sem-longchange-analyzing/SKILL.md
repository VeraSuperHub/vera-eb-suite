---
name: vera-sem-longchange-analyzing
description: >-
  Full longitudinal SEM skill for latent growth and change models.
  Extends the initial fit with nonlinear trajectories, latent-basis and
  change-score variants, subgroup comparisons, parallel-process models when
  available, and manuscript-ready output. Trigger after
  vera-sem-longchange-testing or by a direct request for longitudinal SEM.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Longitudinal Change Analyzing — Full Growth / Change Pipeline

Open-source skill.

Read `reference/specs/output-variation-protocol.md` before every generation.

## Workflow

| Step | File | Executor | Output |
|---|---|---|---|
| Additional tests | `workflow/04-run-additional-tests.md` | Main Agent | Nonlinear/change diagnostics |
| Subgroup | `workflow/05-analyze-subgroups.md` | Main Agent | Multigroup growth/change |
| Modeling | `workflow/06-fit-models.md` | Main Agent | Alternative growth/change models |
| Comparison | `workflow/07-compare-models.md` | Main Agent | Cross-trajectory synthesis |
| Manuscript | `workflow/08-generate-manuscript.md` | Main Agent | methods.md + results.md |
