---
name: vera-sem-full-analyzing
description: >-
  Full SEM analysis skill. Extends the initial structural model with indirect
  effects, alternative-path comparison, multigroup testing, residual review,
  and manuscript-ready methods/results. Trigger after vera-sem-full-testing or
  by a direct request for SEM.
user-invocable: true
allowed-tools: Read, Bash, Write, Edit, Grep, Glob
---

# Full SEM Analyzing — Structural Paths, Indirect Effects, Manuscript

Open-source skill.

Read `reference/specs/output-variation-protocol.md` before every generation.

## Workflow

| Step | File | Executor | Output |
|---|---|---|---|
| Additional tests | `workflow/04-run-additional-tests.md` | Main Agent | Indirect/residual diagnostics |
| Subgroup | `workflow/05-analyze-subgroups.md` | Main Agent | Multigroup SEM |
| Modeling | `workflow/06-fit-models.md` | Main Agent | Alternative structural models |
| Comparison | `workflow/07-compare-models.md` | Main Agent | Cross-model synthesis |
| Manuscript | `workflow/08-generate-manuscript.md` | Main Agent | methods.md + results.md |
