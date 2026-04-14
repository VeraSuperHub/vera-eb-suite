# Step 04: Run Experiments

> **Executor**: Main Agent (invokes sub-skills)
> **Input**: `simulation/simulation_code.{R,py}` + `PIPELINE_STATE.json`
> **Output**: `results/` directory + `RESULTS_ANALYSIS.md`

---

## Execution Instructions

### 4.1 Deploy Simulations

```
Read and execute reference/sub-skills/experiment-running.md
```

The run-experiment skill handles:
- Environment detection (local vs. remote)
- Pre-flight verification (seeds, packages, expected output structure)
- Deployment (direct, parallel split, or remote via screen/tmux)
- PID tracking for monitoring

**Simulation parameters** (from config):
- Coverage studies: B ≥ 1000 replications
- Size/power studies: B ≥ 5000 replications
- Sample sizes: n = (100, 200, 500, 1000) minimum
- Include timing per method

### 4.2 Monitor Progress

```
Read and execute reference/sub-skills/experiment-monitoring.md
```

Track running simulations:
- Check process status (alive/completed/failed)
- Read log files for progress (iteration count, completion %)
- Estimate time remaining
- Report errors immediately

If simulation appears stuck (no progress for > 30 minutes):
- Check for memory issues
- Check for infinite loops
- Report to pipeline log

### 4.3 Analyze Results

After simulations complete:

```
Read and execute reference/sub-skills/results-analyzing.md
```

The analyze-results skill produces:
- Structured results tables with Monte Carlo SEs
- Convergence rate verification (metrics should improve with larger n)
- Outlier detection (unexpected values)
- Comparison tables across methods

**Mandatory checks**:

| Check | Rule | Action if Failed |
|-------|------|------------------|
| No NaN/Inf | All numeric results finite | Investigate DGP or method |
| Monotonicity | Coverage/power shouldn't degrade with larger n | Flag anomaly |
| MC SE reported | Every point estimate has MC standard error | Compute and add |
| Coverage near nominal | Empirical coverage within MC SE of 95% at largest n | Flag if far off |
| Runtime recorded | Per-method timing available | Re-run with timing |

### 4.4 Generate Results Summary

Write `RESULTS_ANALYSIS.md`:

```markdown
# Simulation Results Analysis

## Setup
- Proposed method: {name}
- Competitors: {list}
- DGP scenarios: {list}
- Sample sizes: n = {list}
- Replications: B = {value}

## Main Results

### Table 1: Bias and RMSE
| Method | n=100 | n=200 | n=500 | n=1000 |
|--------|-------|-------|-------|--------|
| Proposed | bias (MC SE) | ... | ... | ... |
| Competitor 1 | ... | ... | ... | ... |
| Competitor 2 | ... | ... | ... | ... |

### Table 2: Coverage Probability (Nominal 95%)
[same structure with coverage (MC SE)]

### Table 3: Power (if applicable)
[same structure]

### Table 4: Computation Time
[seconds per method per n]

## Key Findings
1. {Finding 1 — how proposed method compares}
2. {Finding 2 — under misspecification}
3. {Finding 3 — convergence behavior}

## Potential Concerns
- {Any anomalies, unexpected results}

## Figures to Generate
- Convergence rate plot (bias/RMSE vs n, log scale)
- Coverage probability plot (with nominal line)
- Power curves (if applicable)
- Box plots of estimate distributions
```

### 4.5 Update State

```json
{
  "stage": 4,
  "status": "completed",
  "simulations": {
    "total_replications": 5000,
    "sample_sizes": [100, 200, 500, 1000],
    "dgp_scenarios": 2,
    "methods_compared": 3,
    "runtime_hours": 1.8
  },
  "key_findings": [
    "Proposed method achieves nominal coverage at n≥200",
    "20% lower RMSE than competitor 1 under misspecification"
  ],
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 4a | Simulation completed | Process exited successfully | Diagnose, retry (3x) |
| 4b | Results files exist | .rds/.pkl/.csv in results/ | Check output path |
| 4c | No NaN/Inf | All values finite | Investigate method |
| 4d | MC SEs computed | Every estimate has SE | Compute from replications |
| 4e | Monotonicity holds | Bias decreases, coverage → nominal with n | Flag anomaly in report |
| 4f | RESULTS_ANALYSIS.md written | Non-empty, all tables present | Regenerate from raw results |

---

## Next Step
→ Step 05: External Review via Codex MCP
