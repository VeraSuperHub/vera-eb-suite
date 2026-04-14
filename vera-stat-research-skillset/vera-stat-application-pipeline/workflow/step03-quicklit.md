# Step 03: Quick Literature Scan

> **Executor**: Main Agent
> **Input**: `PIPELINE_STATE.json` (research question, outcome type, discipline)
> **Output**: `output/lit_scan.md` + `output/analysis_strategy.md`

---

## Execution Instructions

### 3.1 Purpose

Before running our own analysis, understand how prior work has approached similar data and questions. This shapes which method tracks to include and ensures our analysis is grounded in established practice.

### 3.2 Fast Literature Survey

Read and execute `reference/sub-skills/literature-reviewing.md` with a focused query:

```
Read and execute reference/sub-skills/literature-reviewing.md with context: "{research_question} {outcome_type} analysis methods {discipline}"
```

Time-box this to 15 minutes maximum. Focus on:

1. **Analytical precedents**: What methods have others used for this type of outcome in this domain?
   - Common primary tests (e.g., "most lung function studies use mixed models")
   - Standard modeling approaches (e.g., "Cox regression is standard for oncology endpoints")
   - Emerging alternatives (e.g., "recent work uses machine learning as complement")

2. **Reporting norms**: What do journals in this discipline expect?
   - Effect size conventions (OR, HR, Cohen's d, etc.)
   - Table/figure conventions
   - Subgroup analysis expectations

3. **Methodological gaps**: What analyses are common but rarely complemented?
   - e.g., "Most studies use only logistic regression; few explore nonlinear effects"
   - This identifies opportunities for our analysis to add value

### 3.3 Produce Literature Scan

Write `output/lit_scan.md`:

```markdown
# Quick Literature Scan

## Research Question
[Verbatim from PIPELINE_STATE]

## How Others Have Analyzed Similar Data

### Common Methods
- [Method 1]: Used in [cite 2-3 representative papers]
- [Method 2]: Used in [cite]
- [Method 3]: Emerging approach [cite]

### Reporting Conventions in [Discipline]
- Standard effect sizes: [list]
- Expected tables: [list]
- Subgroup analysis: [yes/no, what kind]

### Gaps in Existing Analyses
- [Gap 1]: Most studies only use [X], missing [Y] perspective
- [Gap 2]: Few studies examine [subgroup/interaction]

### Key References (for Introduction)
- [Author (Year)]: [1-sentence relevance]
- [Author (Year)]: [1-sentence relevance]
- ... (aim for 8-15 references)
```

### 3.4 Define Analysis Strategy

Based on the lit scan + outcome type, define which method tracks to run.

**CRITICAL**: Read `reference/method-tracks.md` and look up the EXACT track table for
this outcome type. Do NOT use a universal T1-T5 template. Track counts, names,
dependencies, and parallel/sequential status vary by outcome type:
- Some types skip T4 entirely (nominal has no T4)
- Some types have T4 depending on T2, not independent (survival: T4_aft depends on T2_regression PH check)
- SEM families are routed separately (`sem-cfa`, `sem-full`, `sem-longchange`) and have different sequential track definitions
- Subgroup tracks (T5) may depend on T1 alone, or T1+T2, depending on outcome type

Copy the exact track table from method-tracks.md for the detected outcome type,
then adjust based on literature scan:

- **Add tracks** if the literature shows a method is standard but not in defaults
- **Remove tracks** marked "skip" or "not applicable" for this outcome type
- **Adjust dependencies** if the literature suggests a different ordering
- **Note gaps** our analysis can fill

Write `output/analysis_strategy.md`:

```markdown
# Analysis Strategy

## Outcome Type: [type]
## Informed By: Quick literature scan (Step 03)
## Source: reference/method-tracks.md — [outcome type] section

## Method Tracks

[Copy the EXACT track table for this outcome type from method-tracks.md,
 then annotate with literature-informed adjustments]

| Track | ID | Methods | Depends On | Parallel? | Notes |
|-------|----|---------|------------|-----------|-------|
| [from method-tracks.md for this outcome type] | ... | ... | ... | ... | [lit-informed] |

## Dependency Graph
[Draw the ACTUAL dependency graph for this outcome type — NOT a generic T1-T5 parallel template]

## Literature-Informed Adjustments
- [Adjustment 1]: Added/removed [method] because [lit reason]
- [Adjustment 2]: Changed dependency because [reason]

## Tracks Skipped
- [Track X]: Not applicable for [outcome type] — [reason]
```

### 3.5 Update State

The `method_tracks` array must reflect the ACTUAL tracks for this outcome type,
not a universal template. Example for continuous:

```json
{
  "stage": 3,
  "status": "completed",
  "method_tracks": [
    {"id": "T1_primary", "parallel": true, "depends_on": null},
    {"id": "T2_regression", "parallel": true, "depends_on": null},
    {"id": "T3_trees", "parallel": true, "depends_on": null},
    {"id": "T4_qr", "parallel": true, "depends_on": null},
    {"id": "T5_subgroup", "parallel": false, "depends_on": ["T1_primary"]}
  ],
  "lit_scan_references": 12,
  "timestamp": "..."
}
```

Example for survival (different dependencies):
```json
{
  "method_tracks": [
    {"id": "T1_primary", "parallel": true, "depends_on": null},
    {"id": "T2_regression", "parallel": true, "depends_on": null},
    {"id": "T3_trees", "parallel": true, "depends_on": null},
    {"id": "T4_aft", "parallel": false, "depends_on": ["T2_regression"]},
    {"id": "T5_subgroup", "parallel": false, "depends_on": ["T1_primary", "T2_regression"]}
  ]
}
```

Example for SEM-CFA (family-specific, fully sequential):
```json
{
  "method_tracks": [
    {"id": "T1_primary", "parallel": false, "depends_on": null},
    {"id": "T2_validity", "parallel": false, "depends_on": ["T1_primary"]},
    {"id": "T3_invariance", "parallel": false, "depends_on": ["T1_primary"]},
    {"id": "T4_models", "parallel": false, "depends_on": ["T2_validity"]},
    {"id": "T5_compare", "parallel": false, "depends_on": ["T4_models"]}
  ]
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 3a | Lit scan completed | `output/lit_scan.md` exists, non-empty | Proceed with default tracks; note limited lit context |
| 3b | Strategy defined | `output/analysis_strategy.md` exists with ≥2 tracks | Use default tracks from method-tracks.md |
| 3c | At least 1 launchable track | Tracks array has ≥1 entry with depends_on=null | Always true — first track in any sequence has no deps |
| 3d | Dependencies valid | Sequential tracks reference existing parallel tracks | Fix dependency graph |

---

## Next Step
→ Step 04: Parallel Execution (Full Lit Review + Analysis Tracks)
