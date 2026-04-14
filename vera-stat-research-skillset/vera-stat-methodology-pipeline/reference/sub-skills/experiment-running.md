<!-- Absorbed from skills/run-experiment/SKILL.md -->

# Run Simulation: Statistics Experiment Deployment

Deploy and run statistical simulations for: **$ARGUMENTS**

## Environment Detection

1. **Check local environment**:
   - R installation: `which R`, `R --version`
   - Python installation: `which python3`, check for numpy, scipy, statsmodels, rpy2
   - Stan/JAGS: check for `rstan`, `cmdstanr`, `pystan`, `pyjags`
   - Available cores: `nproc` or `sysctl -n hw.ncpu`

2. **Check for remote servers** (if configured):
   - SSH config for compute servers
   - Check available cores and memory on remote

## Pre-flight Checks

Before launching any simulation:

1. **Verify the simulation script exists and is syntactically valid**:
   - R: `R -e "parse('script.R')"`
   - Python: `python3 -c "import py_compile; py_compile.compile('script.py')"`

2. **Estimate runtime**:
   - Check number of replications (B), sample sizes (n_vec), number of DGPs
   - Total iterations = B × length(n_vec) × n_DGPs × n_methods
   - Rough estimate: flag if > 4 hours on available cores

3. **Check disk space**: Simulation output can be large (especially if saving all replicates)

4. **Verify seed is set**: Every simulation MUST have a reproducible seed
   - R: `set.seed(42)` or use `.Random.seed`
   - Python: `np.random.seed(42)` or `rng = np.random.default_rng(42)`

## Deployment

### Local Execution

For simulations estimated < 2 hours:

```bash
# R simulation
nohup Rscript simulation_study.R > logs/sim_$(date +%Y%m%d_%H%M%S).log 2>&1 &
echo $! > .sim_pid

# Python simulation
nohup python3 simulation_study.py > logs/sim_$(date +%Y%m%d_%H%M%S).log 2>&1 &
echo $! > .sim_pid
```

Use `run_in_background: true` for the Bash call.

### Parallel Execution (Multiple Scenarios)

For large simulation studies, split across cores:

```r
# R: parallel simulation template
library(parallel)
n_cores <- detectCores() - 1
cl <- makeCluster(n_cores)
# ... export functions and run parLapply ...
```

```python
# Python: parallel simulation template
from multiprocessing import Pool
with Pool(processes=n_cores) as pool:
    results = pool.starmap(run_one_scenario, scenario_list)
```

Or split into separate scripts per scenario and launch in parallel:
```bash
# Launch multiple simulation scenarios in parallel
for scenario in 1 2 3 4; do
  nohup Rscript sim_scenario_${scenario}.R > logs/scenario_${scenario}.log 2>&1 &
done
```

### Remote Execution (via SSH)

For long-running simulations on a compute server:

1. **Sync code**: `rsync -avz --exclude='.git' ./ server:~/project/`
2. **Launch in screen/tmux**:
   ```bash
   ssh server "cd ~/project && screen -dmS sim_main bash -c 'Rscript simulation_study.R > logs/sim.log 2>&1'"
   ```
3. **Verify launch**: `ssh server "screen -ls | grep sim_main"`

### MCMC-Specific Deployment

For Bayesian simulations with MCMC:

1. **Stan models**: Compile first, then run
   ```r
   # Compile Stan model (do once)
   model <- cmdstan_model("model.stan")
   # Run chains in parallel
   fit <- model$sample(data = stan_data, chains = 4, parallel_chains = 4)
   ```

2. **Monitor convergence**: Set up interim diagnostics
   ```r
   # Save interim results every N iterations for monitoring
   fit <- model$sample(data = stan_data, save_warmup = TRUE,
                        output_dir = "mcmc_output/")
   ```

## Post-Launch Verification

After launching:

1. **Verify process is running**: Check PID or screen session
2. **Check initial output**: Read first few lines of log file after 30 seconds
3. **Estimate completion time**: Based on first iteration timing
4. **Report to user**:
   ```
   Simulation launched:
   - Script: simulation_study.R
   - Scenarios: 5 DGPs × 5 sample sizes × 4 methods
   - Replications: 2000
   - Estimated runtime: ~45 minutes on 8 cores
   - Log: logs/sim_20260314_103000.log
   - PID: 12345
   ```

## Key Rules

- ALWAYS set a random seed for reproducibility
- ALWAYS log output to a file (never just stdout)
- Save PID or screen session name for monitoring
- For R: use `saveRDS()` for results, not `save()` (more portable)
- For Python: use pickle or JSON for results
- Always include timing information in the simulation output
- For MCMC: always run multiple chains (≥ 4) and save diagnostics
- Never launch a simulation without estimating runtime first
- If estimated runtime > 4 hours, warn the user and suggest parallelization or reduced replications for a pilot
