# Step 03: Implementation (Parallel Tracks)

> **Executor**: Main Agent orchestrating SubAgents
> **Input**: `PIPELINE_STATE.json` (selected idea, environment)
> **Output**: `simulation/`, `proofs/`, `real_data/` directories

---

## Execution Instructions

Read `reference/implementation-tracks.md` for detailed track specifications.
Read `reference/simulation-standards.md` for simulation code requirements.
Read `reference/proof-patterns.md` for proof structure patterns.

### 3.1 Determine Active Tracks

Based on the selected idea, determine which tracks to run:

| Track | Condition | Always? |
|-------|-----------|---------|
| A: Simulation Code | Idea involves an estimator/test/procedure | Yes (almost always) |
| B: Proof Sketches | Idea has theoretical claims | If theoretical contribution |
| C: Real Data Prep | Idea has empirical component | If applicable |

All active tracks launch as **parallel SubAgents**.

### 3.2 Launch Parallel Tracks

#### Track A: Simulation Code (SubAgent)

```
Prompt: "Write simulation code for the following methodology idea:

Idea: {selected_idea.title}
Summary: {selected_idea.summary}
Hypothesis: {selected_idea.hypothesis}
Language: {preferred_language}

Create simulation_code.{R/py} in simulation/ with:

1. Data-Generating Process (DGP) Functions:
   - At least 2 DGP scenarios (well-specified + misspecified)
   - Parameters: sample sizes n = (100, 200, 500, 1000)
   - Dimension settings if high-dimensional

2. Proposed Method Implementation:
   - The new estimator/test/procedure
   - Clear function interface: input data, output estimate + SE + CI

3. Competing Methods (at least 2):
   - Standard approach in the field
   - Recent alternative (from literature survey)
   - Same interface as proposed method

4. Evaluation Metrics:
   - Bias, RMSE (or MSE)
   - Coverage probability (nominal 95%)
   - Power (if hypothesis test)
   - Computation time

5. Parallel Execution Setup:
   - Use foreach/parallel (R) or multiprocessing (Python)
   - set.seed() / np.random.seed() for reproducibility
   - B = {main_replications_coverage} replications for coverage studies
   - B = {main_replications_power} for power studies

6. Output Structure:
   - Results as list/dict: methods × n_values × metrics × replications
   - Save to results/sim_results.rds (R) or results/sim_results.pkl (Python)
   - Also save comparison_table.csv for quick viewing

Requirements:
- Document package versions (sessionInfo() / pip freeze)
- Include runtime estimates
- All functions have docstrings
- Pre-flight check: run with B=10 to verify no errors"
```

#### Track B: Proof Sketches (SubAgent)

```
Prompt: "Write proof sketches for the following theoretical claims:

Idea: {selected_idea.title}
Hypothesis: {selected_idea.hypothesis}

Create these files in proofs/:

1. ASSUMPTIONS.md — Numbered assumptions (A1, A2, ...):
   - Clearly state each regularity condition
   - Note which are standard vs. novel
   - For each: cite where it's used in proofs

2. THEOREM_1.tex (and THEOREM_2.tex, etc.):
   - Formal theorem statement in LaTeX
   - Proof sketch (outline major steps)
   - Key lemmas needed (stated, proof deferred or sketched)
   - Mark difficult steps with [TODO: VERIFY]

3. PROOF_OUTLINE.md — Overall proof strategy:
   - How theorems connect
   - Which lemmas serve which theorems
   - Proof techniques used (CLT, delta method, empirical process, etc.)
   - Known gaps or difficulties

Rules:
- Be precise with mathematical notation
- State ALL assumptions explicitly
- Mark any step that requires careful verification with [VERIFY]
- Proofs are SKETCHES — human verification is mandatory
- Use standard theorem environments (assumption, theorem, lemma, corollary)"
```

#### Track C: Real Data Preparation (SubAgent, if applicable)

```
Prompt: "Prepare real data analysis for:

Idea: {selected_idea.title}
Method: {brief method description}

Create these files in real_data/:

1. data_load.{R/py}:
   - Load and preprocess the dataset
   - Handle missing values
   - Describe: N, variables, summary statistics

2. analysis_script.{R/py}:
   - Apply proposed method to real data
   - Apply competing methods for comparison
   - Report: estimates, SEs, CIs, p-values

3. sensitivity_analysis.{R/py}:
   - Vary key assumptions
   - Subset analyses
   - Alternative specifications

Requirements:
- Document data source clearly
- All scripts reproducible (seeds, versions)
- Output results to results/ directory"
```

### 3.3 Wait for All Tracks

Monitor SubAgents. As each completes:
1. Verify output files exist
2. For Track A: run pre-flight check (B=10 quick simulation)
3. For Track B: verify .tex files parse correctly
4. Log completion in PIPELINE_STATE.json

### 3.4 Pre-Flight Simulation Check

After Track A completes, run a quick verification:

```bash
# R
Rscript simulation/simulation_code.R --preflight  # or equivalent B=10 run

# Python
python3 simulation/simulation_code.py --preflight
```

Verify:
- Code runs without errors
- Output has expected structure
- No NaN/Inf values
- Runtime estimate is reasonable (< MAX_TOTAL_CPU_HOURS for full run)

If pre-flight fails: diagnose, fix code, re-run (up to 3 attempts).

### 3.5 Update State

```json
{
  "stage": 3,
  "status": "completed",
  "implementation_tracks": {
    "simulation": {"status": "completed", "preflight": "passed", "language": "R"},
    "proofs": {"status": "completed", "theorems": 2, "lemmas": 3},
    "real_data": {"status": "completed", "dataset": "..."}
  },
  "estimated_runtime_hours": 2.5,
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 3a | Simulation code exists | `simulation/simulation_code.{R,py}` present | Regenerate |
| 3b | Pre-flight passes | B=10 run completes without errors | Fix code, retry (3x) |
| 3c | Seeds set | Random seed in code | Add seed |
| 3d | Competing methods included | ≥ 2 competitors implemented | Add standard competitors |
| 3e | Proofs exist (if theoretical) | At least 1 THEOREM_*.tex + ASSUMPTIONS.md | Regenerate |
| 3f | All functions documented | Docstrings present | Add docstrings |
| 3g | Runtime reasonable | Estimated < MAX_TOTAL_CPU_HOURS | Reduce B or n range |

---

## Next Step
→ Step 04: Run Experiments
