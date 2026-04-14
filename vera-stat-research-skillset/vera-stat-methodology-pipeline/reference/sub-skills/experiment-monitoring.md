<!-- Absorbed from skills/monitor-experiment/SKILL.md -->

# Monitor Simulation: Check Progress and Collect Results

Monitor running statistical simulations for: **$ARGUMENTS**

## Workflow

### Step 1: Find Running Simulations

Check for active processes:

```bash
# Check by PID file
if [ -f .sim_pid ]; then
  pid=$(cat .sim_pid)
  ps -p $pid -o pid,etime,pcpu,pmem,command
fi

# Check screen sessions (remote)
screen -ls 2>/dev/null | grep sim_

# Check R processes
ps aux | grep "[R]script"

# Check Python processes
ps aux | grep "[p]ython.*sim"
```

### Step 2: Check Progress

1. **Read log files**: Check the latest log output
   ```bash
   tail -50 logs/sim_*.log
   ```

2. **Parse progress indicators**: Look for iteration counters, completion percentages
   - R simulations often print: `"Scenario 3/5, n=500, rep 1500/2000"`
   - Python simulations: progress bars or print statements
   - Stan/MCMC: chain progress, warmup vs. sampling

3. **Check for errors**: Scan logs for warnings and errors
   ```bash
   grep -i "error\|warning\|fail\|nan\|inf\|singular\|convergence" logs/sim_*.log
   ```

4. **Estimate remaining time**: Based on elapsed time and progress percentage

### Step 3: Collect Completed Results

For completed simulations:

1. **Locate output files**:
   ```bash
   # R results
   find results/ -name "*.rds" -newer .sim_pid
   find results/ -name "*.csv" -newer .sim_pid

   # Python results
   find results/ -name "*.pkl" -newer .sim_pid
   find results/ -name "*.json" -newer .sim_pid
   ```

2. **Read and summarize results**:
   ```r
   # Quick R summary
   res <- readRDS("results/sim_results.rds")
   # Build comparison table
   ```

3. **Build comparison table**:
   ```markdown
   | Method | n | Bias | RMSE | Coverage (95%) | Avg Width | Time (s) |
   |--------|---|------|------|----------------|-----------|----------|
   | Proposed | 100 | 0.002 | 0.145 | 0.938 | 0.562 | 0.12 |
   | Proposed | 500 | 0.001 | 0.063 | 0.948 | 0.248 | 0.15 |
   | MLE | 100 | 0.001 | 0.158 | 0.942 | 0.621 | 0.08 |
   | MLE | 500 | 0.000 | 0.068 | 0.951 | 0.267 | 0.09 |
   ```

4. **MCMC-specific diagnostics** (if Bayesian):
   ```markdown
   | Parameter | Rhat | ESS_bulk | ESS_tail | Mean | 95% CI |
   |-----------|------|----------|----------|------|--------|
   | beta_1 | 1.001 | 4200 | 3800 | 0.52 | [0.31, 0.73] |
   ```

### Step 4: Interpret Results

Provide statistical interpretation:

1. **For estimation simulations**:
   - Is bias negligible relative to standard error?
   - Does RMSE decrease at the expected rate (e.g., n^{-1/2})?
   - Is coverage close to nominal? (within Monte Carlo SE: ±2√(0.05×0.95/B))
   - Does the proposed method beat competitors on the metrics that matter?

2. **For testing simulations**:
   - Is size controlled at nominal level? (empirical size within ±2 MC SE of 0.05)
   - How does power compare across methods?
   - Is power monotonically increasing with effect size and sample size?

3. **For MCMC simulations**:
   - Are all Rhat < 1.01?
   - Are ESS values adequate (> 400 per chain)?
   - Any divergent transitions (HMC/NUTS)?

4. **Flag anomalies**:
   - Coverage far from nominal
   - Size inflation (empirical size >> 0.05)
   - Non-monotone power curves
   - Unexpectedly slow convergence rates
   - NaN or Inf values

### Step 5: Suggest Next Steps

Based on results:
- "Coverage is slightly below nominal at n=100 (93.8%) — consider bias correction or larger n in the simulation."
- "Proposed method shows 25% RMSE reduction over MLE — strong signal, proceed to full study."
- "Size is inflated to 7.2% at n=100 — investigate; may need finite-sample correction."
- "MCMC chains have not converged (Rhat=1.05 for beta_3) — increase iterations or reparameterize."

### Step 6: Update Documentation

Write a summary to `SIMULATION_STATUS.md` or update existing notes:

```markdown
## Simulation Status (timestamp)

### Running
- sim_scenario_3.R: 75% complete, ETA 15 min

### Completed
| Simulation | Status | Key Finding |
|------------|--------|-------------|
| sim_bias_mse.R | Done | Proposed method: 25% lower RMSE |
| sim_coverage.R | Done | Coverage 94.8% at n=500 (nominal 95%) |
| sim_power.R | Running | 60% complete |

### Issues
- [any errors or anomalies found]

### Suggested Next Steps
- [based on interpretation above]
```

## Key Rules

- Always report Monte Carlo standard errors alongside point estimates
- Coverage should be evaluated relative to MC SE: at B=2000 reps, MC SE ≈ 0.49%
- Flag size inflation > 1 percentage point above nominal as a concern
- For MCMC: always check Rhat AND ESS, not just one
- Don't over-interpret small differences — check if they're within MC error
- If a simulation has errors, read the full error message before suggesting fixes
