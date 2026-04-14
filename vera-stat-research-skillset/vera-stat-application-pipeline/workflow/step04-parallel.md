# Step 04: Parallel Execution — Full Literature Review + Analysis Tracks

> **Executor**: Main Agent orchestrating SubAgents
> **Input**: `PIPELINE_STATE.json` + `output/analysis_strategy.md` + data file
> **Output**: `output/literature_review.md` + all track outputs in `output/track_outputs/`

---

## Execution Instructions

### 4.1 Preparation

Read from PIPELINE_STATE.json:
- `research_question`, `outcome_type`, `discipline`, `venue_style`
- `variables` (outcome, predictors, covariates, subgroup)
- `testing_skill_path`
- `analysis_skill_path`
- `method_tracks` (from Step 03)
- `data_file` path

Read the routed skills using the paths from `PIPELINE_STATE.json` — do NOT reconstruct
them from `outcome_type`. The routing table handles nonstandard families and keeps
the testing/analyzing ownership split explicit.

```
REPO_ROOT discovery (in priority order):
1. Check STATRESEARCH_ROOT environment variable
2. Resolve relative to THIS skill file: ../../vera-stat-analysis-engine/
3. Walk upward from PWD looking for vera-stat-analysis-engine/ directory

TESTING_SKILL_PATH = {REPO_ROOT}/{testing_skill_path}
ANALYZING_SKILL_PATH = {REPO_ROOT}/{analysis_skill_path}

Read:
  {TESTING_SKILL_PATH}/SKILL.md
  {TESTING_SKILL_PATH}/workflow/*.md
  {ANALYZING_SKILL_PATH}/SKILL.md
  {ANALYZING_SKILL_PATH}/workflow/*.md
  {ANALYZING_SKILL_PATH}/reference/
```

Create output directories for each track listed in `method_tracks` from PIPELINE_STATE.json:
```
for each track in method_tracks:
  mkdir -p output/track_outputs/{track.id}/
```

Do NOT hardcode track IDs — read them from state. The number and names of tracks
vary by outcome type (see reference/method-tracks.md).

### 4.2 Launch Streams Using Dependency Graph

Read `method_tracks` from PIPELINE_STATE.json. Partition into:
- **Independent tracks**: `depends_on` is null → launch immediately as parallel SubAgents
- **Dependent tracks**: `depends_on` is non-null → launch ONLY after all dependencies complete

**SEM special case**: If ALL tracks have `parallel: false`, run them sequentially
in order (T1→T2→T3→...) rather than spawning SubAgents.

Launch ALL independent work simultaneously using the Agent tool with multiple parallel calls.

#### Stream A: Full Literature Review (SubAgent)

Launch one SubAgent:

```
Prompt: "Conduct a comprehensive literature review for the following research:

Research question: {research_question}
Discipline: {discipline}
Outcome type: {outcome_type}
Methods being used: {list from analysis_strategy.md}

Follow reference/sub-skills/literature-reviewing.md to search across arXiv, Google Scholar, Semantic Scholar, and statistics journals.

Produce output/literature_review.md with:
1. Background & significance (2-3 paragraphs)
2. Prior analytical approaches (what methods others used, key findings)
3. Methodological justification (why our chosen methods are appropriate)
4. Gaps this study addresses
5. Key references organized thematically

Also append any new references to output/references.bib.
Target: 15-25 well-chosen references."
```

#### Stream B: Analysis Tracks (SubAgents — one per independent track)

For each track marked `parallel: true` in the analysis strategy, launch a SubAgent.
Each SubAgent reads the relevant workflow step files from the routed owning skill and executes them.

**Pre-populate inputs for all tracks** (so they don't ask interactively):
```
outcome_var: {from PIPELINE_STATE}
group_var: {from PIPELINE_STATE — first categorical predictor}
predictors: {from PIPELINE_STATE}
covariates: {from PIPELINE_STATE}
research_question: {from PIPELINE_STATE}
subgroup_var: {from PIPELINE_STATE}
data_file: {from PIPELINE_STATE}

discipline: {from PIPELINE_STATE}
venue_style: {from PIPELINE_STATE}
```

##### Dynamic Track Dispatch (for ALL independent tracks)

For EACH track in `method_tracks` where `depends_on` is null, construct and launch
a SubAgent prompt dynamically. Do NOT use hardcoded track names — read the track's
ID, methods, and workflow step mapping from `output/analysis_strategy.md`.

Path ownership rule:
- `T1_primary` executes against `{TESTING_SKILL_PATH}`
- `T2+` executes against `{ANALYZING_SKILL_PATH}`

```
Prompt template for EACH independent track:

"Execute the '{track.id}' analysis track for:

[pre-populated inputs from above]

Track specification (from analysis strategy):
  Track ID: {track.id}
  Methods: {track.methods — from analysis_strategy.md}
  Workflow steps: {track.workflow_steps — from analysis_strategy.md}

If track.id = T1_primary:
  Read the testing skill at: {TESTING_SKILL_PATH}
  Execute the workflow step file(s) listed above from {TESTING_SKILL_PATH}/workflow/.
Else:
  Read the analyzing skill at: {ANALYZING_SKILL_PATH}
  Execute the workflow step file(s) listed above from {ANALYZING_SKILL_PATH}/workflow/.
  Read {ANALYZING_SKILL_PATH}/reference/ for reporting standards and sentence bank.

Output to output/track_outputs/{track.id}/:

For T1_primary (testing skill, steps 01-03):
- code.R and code.py
- figures/ (2 PNGs: data overview + primary test results, 300 DPI)
- recommendations (text block: what the analyzing skill should do next)
Note: testing skills do NOT produce methods.md, results.md, or tables/.
The pipeline generates T1 manuscript fragments from T1 code output and figures at assembly (Step 05).

For T2-T5 (analyzing skill, steps 04-08):
- methods.md ({track.id} methods description)
- results.md ({track.id} results with effect sizes, CIs, p-values)
- code.R and code.py
- figures/ (track-relevant plots, 300 DPI PNG)
- tables/ (if applicable)
- references.bib (methodological references for this track)

Follow reporting standards: p < .001 never 0.000, always effect sizes, 95% CIs.
If this track involves tree-based methods, frame as EXPLORATORY.
If N < 200 and tree-based, note no train/test split."
```

**Example**: For a continuous outcome, this dispatches 4 parallel SubAgents:
- `T1_primary` → testing workflow steps 01-03
- `T2_regression` → workflow step 06 (regression portion)
- `T3_trees` → workflow step 06 (tree portion)
- `T4_qr` → workflow step 06 (quantile regression portion)

**Example**: For SEM-CFA, this dispatches 0 parallel SubAgents (all are sequential),
and the dependent-track logic in 4.3 runs them one at a time:
- `T1_primary` → launched first (depends_on: null but parallel: false)
- `T2_validity` → after `T1_primary`
- `T3_invariance` / `T4_models` → per dependency graph
- `T5_compare` → after `T4_models`

**Special handling for `parallel: false` with `depends_on: null`**:
If a track has `depends_on: null` but `parallel: false` (first track in a sequential
chain, like SEM), launch it as the ONLY independent track. Do not launch others
until it completes and the dependency check in 4.3 unblocks the next track.

### 4.3 Wait for Independent Tracks and Launch Dependent Tracks

Monitor all SubAgents. As each completes:
1. Verify output files exist in the track's directory
2. Log completion in PIPELINE_STATE.json (`tracks_completed` array)
3. Check for errors — if a track fails, log it and continue
4. **Check if any dependent track's prerequisites are now satisfied**:
   - For each pending track with `depends_on` non-null:
     - If ALL tracks in `depends_on` are now in `tracks_completed`: launch it
   - This handles outcome-specific dependencies correctly:
     - Continuous T5 depends on T1 only → launches after T1
     - Survival T4_aft depends on T2 → launches after T2
     - Survival T5 depends on T1 + T2 → launches after both complete
     - SEM: all tracks sequential → each launches after its predecessor

**For each dependent track**, construct its SubAgent prompt by:
1. Reading the track's methods from `output/analysis_strategy.md`
2. Reading results from its dependency tracks:
   - If dependency is `T1_primary`: read `output/track_outputs/T1_primary/figures/`
     for diagnostics and primary test output, plus its recommendation text.
     T1 does NOT produce methods.md, results.md, or tables/ — extract key findings
     from its code output and figures instead.
   - If dependency is T2-T5: read `output/track_outputs/{dep_id}/results.md`
3. Reading the relevant workflow step from the routed owning skill (testing for `T1_primary`, analyzing otherwise)

```
Prompt template for dependent tracks:

"Execute {track.id} analysis for:
[pre-populated inputs]

Dependency results:
{for each dep in track.depends_on:
  if dep == 'T1_primary':
    read output/track_outputs/T1_primary/figures/ and code output for diagnostics
  else:
    read output/track_outputs/{dep}/results.md and include key findings}

Follow the routed skill's workflow step(s):
- {relevant workflow file(s) from the owning skill path}

Output to output/track_outputs/{track.id}/:
- methods.md, results.md, code.R, code.py, figures/, tables/, references.bib"
```

**Skip tracks** that were marked as not applicable in the analysis strategy.
Do NOT launch tracks whose dependencies failed — log the gap instead.

### 4.5 Convergence — Model Comparison & Synthesis

After ALL tracks (from `method_tracks` in state) AND Stream A complete:

1. **Unified Variable Importance Table** (if ≥ 2 tracks produced importance/coefficient results)
   Iterate over `tracks_completed` **excluding T1_primary** (which has no results.md) —
   read importance/coefficient results from each track's
   `output/track_outputs/{track_id}/results.md`.
   Normalize all to 0-100 scale (max = 100 per method).
   Build consensus ranking across methods.

   **Skip this step** if only 1 modeling track completed, or if outcome type is SEM
   (where tracks are sequential model-building steps, not independent method families).

2. **Cross-Method Insight Synthesis**
   For each completed track **excluding T1_primary**, extract its unique contribution from
   `output/track_outputs/{track_id}/results.md`.
   For T1_primary, summarize its diagnostics and primary test findings from figures/ and code output.

   Write synthesis narrative (3-4 sentences):
   - What converges across methods (if multiple independent tracks)
   - What each track uniquely reveals
   - Overall interpretation

   **For SEM**: The synthesis describes model-building progression instead of
   cross-method comparison (CFA → structural model → fit comparison).

3. **Merge Track Outputs**
   Iterate over `tracks_completed` in the order they appear in the analysis strategy.
   Combine outputs into unified files:
   - `output/methods.md` ← for T1_primary: generate a brief methods fragment from its
     code output (data diagnostics, primary tests performed, sample sizes).
     For T2-T5: concatenate `{track_id}/methods.md`.
   - `output/results.md` ← for T1_primary: generate a brief results fragment from its
     figures/ and code output (distributions, primary test statistics, effect sizes).
     For T2-T5: concatenate `{track_id}/results.md`. Append synthesis narrative.
   - `output/tables/` ← merge all track tables, renumber sequentially
   - `output/figures/` ← merge all track figures, renumber sequentially
   - `output/code.R` ← merge all track R code with section headers per track
   - `output/code.py` ← merge all track Python code with section headers per track
   - `output/references.bib` ← merge + deduplicate all track references

   For tracks that failed or were skipped: omit from merge, do not leave placeholders.

4. **Apply Output Quality Variation Protocol**
   Read the analyzing skill's `reference/specs/output-variation-protocol.md` and `reference/specs/code-style-variation.md`
   (at `{ANALYZING_SKILL_PATH}/reference/specs/`).
   Apply all six layers to the merged outputs:
   - Layer 1: Output variation (sentence bank for merged prose)
   - Layer 2: Structure randomization (results ordering)
   - Layer 3: Interpretation depth variation
   - Layer 4: Code style variation (7 dimensions)
   - Layer 5: System capabilities
   - Layer 6: Cumulative advantage (orchestration is the moat)

### 4.6 Update State

Record the ACTUAL tracks that were completed/failed — not a hardcoded list:

```json
{
  "stage": 4,
  "status": "completed",
  "tracks_completed": ["list of actual track IDs that completed"],
  "tracks_failed": ["list of actual track IDs that failed, if any"],
  "tracks_skipped": ["list of track IDs skipped as not applicable"],
  "lit_review_status": "completed",
  "lit_review_references": 22,
  "synthesis_complete": true,
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 4a | Stream A complete | `output/literature_review.md` exists | Proceed; note gap in manuscript |
| 4b | All independent tracks complete | T1_primary: directory has code.R/code.py + figures/. T2-T4: directory has methods.md + results.md | Log failed tracks; continue |
| 4c | All dependent tracks complete | Each dependent track launched after deps satisfied | Log; skip in manuscript |
| 4d | Merged methods.md exists | `output/methods.md` non-empty, covers all completed tracks | Re-merge from track outputs |
| 4e | Merged results.md exists | `output/results.md` non-empty, covers all completed tracks | Re-merge from track outputs |
| 4f | Synthesis built (if applicable) | Importance table or SEM progression narrative exists | Build from available tracks |
| 4g | Code files merged | `output/code.R` and `output/code.py` exist | Merge from track outputs |
| 4h | References merged | `output/references.bib` exists, no duplicates | Re-merge and dedup |

---

## Next Step
→ Step 05: Manuscript Assembly
