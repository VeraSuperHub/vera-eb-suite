# Step 02: Outcome Detection & Routing

> **Executor**: Main Agent
> **Input**: `PIPELINE_STATE.json` from Step 01
> **Output**: Confirmed outcome type + analysis strategy baseline

---

## Execution Instructions

### 2.1 Three-Signal Detection

Read `reference/outcome-detection-rules.md` for the full decision tree.

Apply three signal layers to the outcome variable:

#### Signal 1: Primary (Data Characteristics)

| Data Property | Inferred Type |
|---------------|---------------|
| Numeric, >20 unique values, continuous range | continuous |
| Numeric or factor, exactly 2 levels | binary |
| Ordered factor OR numeric with 3-10 discrete values + order implied | ordinal |
| Unordered factor, 3+ levels | nominal |
| Non-negative integer, count-like distribution | count |
| Two columns: time + event indicator (0/1) | survival |
| Repeated measurements per subject (long format or wide with time suffix) | repeated |
| Single time-indexed series, sequential observations | timeseries |
| Multiple outcome columns specified | multivariate |
| Factorial design structure in predictors | doe |
| Effect sizes + SEs from multiple studies | meta |
| Latent variables / factor structure requested | sem-cfa or sem-full |

#### Signal 2: Secondary (Variable Name Heuristics)

Scan outcome variable name and labels for keywords:
- "survived", "died", "yes_no", "pass_fail", "admitted" → binary
- "likert", "severity", "grade", "stage", "mild_moderate_severe" → ordinal
- "species", "diagnosis_type", "category" → nominal
- "count", "events", "incidents", "breaks" → count
- "time_to", "duration", "followup" + censor indicator → survival
- "visit_1", "visit_2", "wave_" prefix pattern → repeated

#### Signal 3: Contextual (Research Question Text)

Parse the research question for analytical intent:
- "predict survival", "time to event" → survival
- "compare groups", "difference between" → continuous or binary (check outcome)
- "trend over time", "longitudinal change" → repeated or timeseries
- "which factors predict", "risk factors for" → matches outcome type
- "pooled estimate", "across studies" → meta
- "factor structure", "latent" → sem

### 2.2 Confidence Scoring

| Confidence | Condition | Action |
|------------|-----------|--------|
| HIGH | All 3 signals agree on same type | Present detection with a default recommendation; only auto-advance in unattended draft mode |
| MEDIUM | 2 of 3 signals agree | Present detection with alternatives, ask user to confirm |
| LOW | All 3 signals disagree, or signals ambiguous | Present top candidates, require user selection |

### 2.3 Human Gate

Present to user:

```
Outcome type detected: [TYPE] (confidence: [HIGH/MEDIUM/LOW])

Signals:
  Data characteristics → [type]
  Variable name/labels → [type]
  Research question → [type]

This means I'll use: [describe the analysis approach briefly]

Confirm? (default recommendation shown if HIGH confidence)
  1. Yes, proceed with [TYPE]
  2. Actually, it's [alternative type]
  3. Let me explain...
```

If HIGH confidence and no user response:
- interactive use: wait for confirmation
- unattended draft runs: log the default recommendation and continue as a draft only
If user corrects: update type and re-route.

### 2.4 Route to Analysis Skill

Look up the confirmed outcome type in `reference/skill-routing-table.md`.
Record BOTH the testing-skill path and the analyzing-skill path in `PIPELINE_STATE.json`.

### 2.5 Update State

```json
{
  "stage": 2,
  "status": "completed",
  "outcome_type": "continuous",
  "detection_confidence": "HIGH",
  "detection_signals": {
    "primary": "continuous",
    "secondary": "continuous",
    "contextual": "continuous"
  },
  "testing_skill_path": "vera-stat-continuous-testing",
  "analysis_skill_path": "vera-stat-analysis-engine/continuous/vera-stat-continuous-analyzing",
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 2a | Outcome type determined | Non-null type from detection | Fall back to asking user |
| 2b | User confirmed (or draft default logged) | Confirmation received or unattended default recorded | Wait for user |
| 2c | Skill path valid | SKILL.md exists at resolved path | Check routing table; ask user |
| 2d | State updated | PIPELINE_STATE.json has stage=2 fields | Rewrite |

---

## Next Step
→ Step 03: Quick Literature Scan
