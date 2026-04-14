# Simulation Standards

Hard rules for simulation code quality in methodology research.

## Code Structure Rules

1. **Random seed**: Set ONCE at the top. Record the seed value.
   ```r
   set.seed(2026)  # Fixed seed for reproducibility
   ```
   ```python
   np.random.seed(2026)
   ```

2. **Package versions**: Document at the top of every script.
   ```r
   # sessionInfo() at bottom, or explicit version comments
   # R 4.3.1, MASS 7.3-60, quantreg 5.97
   ```

3. **Parallel execution**: Use established frameworks.
   ```r
   library(foreach); library(doParallel)
   cl <- makeCluster(detectCores() - 1)
   registerDoParallel(cl)
   ```
   ```python
   from multiprocessing import Pool
   pool = Pool(os.cpu_count() - 1)
   ```

4. **Output format**: Structured, self-describing results.
   ```r
   results <- list(
     methods = c("proposed", "competitor1", "competitor2"),
     n_vec = c(100, 200, 500, 1000),
     B = 1000,
     seed = 2026,
     metrics = array(..., dimnames = list(method, n, metric, rep))
   )
   saveRDS(results, "results/sim_results.rds")
   ```

## Reporting Rules

| Element | Rule | Example |
|---------|------|---------|
| Monte Carlo SE | ALWAYS report alongside point estimates | "Coverage: 94.2% (MC SE: 0.7%)" |
| Bias | Report absolute and relative (if meaningful) | "Bias: 0.003 (0.6% of true value)" |
| Coverage | Report empirical vs nominal | "94.2% empirical for 95% nominal" |
| Power | Report at specific alternatives | "Power: 82% at δ = 0.5" |
| RMSE | Prefer over MSE for interpretability | "RMSE: 0.15" |
| Timing | Report per-replication median | "Median time: 0.3s per rep" |
| Sample sizes | Always test multiple | n ∈ {100, 200, 500, 1000} minimum |

## MC Standard Error Formulas

| Metric | MC SE Formula | At B=1000 |
|--------|---------------|-----------|
| Coverage (p) | √(p(1-p)/B) | ≈ 0.7% if p ≈ 0.95 |
| Power (p) | √(p(1-p)/B) | ≈ 1.4% if p ≈ 0.80 |
| Bias | SD(estimates) / √B | Data-dependent |
| RMSE | Complex, use bootstrap | Approximate |

## Sanity Checks (Pre-Flight)

Run with B=10 before full simulation:

| Check | What to Verify | Action if Failed |
|-------|----------------|------------------|
| No errors | All methods run to completion | Fix bugs |
| Correct output shape | Results array has expected dimensions | Fix output code |
| Finite values | No NaN/Inf/-Inf | Check edge cases in method |
| Timing estimate | Extrapolate total runtime | Reduce scope if > MAX_TOTAL_CPU_HOURS |
| Memory estimate | Check RAM usage per rep | Reduce parallel workers or batch |

## DGP Design Principles

1. **Well-specified scenario**: Data generated exactly from the model your method assumes
2. **Misspecified scenario**: Realistic violation (heavier tails, non-linearity, heteroscedasticity)
3. **Increasing difficulty**: At least one scenario where competing methods struggle
4. **Realistic parameters**: Use parameter values from real data or prior literature
5. **Multiple dimensions**: If method is for high-dimensional data, vary p and p/n ratio

## What NOT to Do

- Never cherry-pick DGP scenarios that favor your method
- Never omit a standard competitor
- Never use B < 500 for published results (B < 100 OK for pilot only)
- Never report coverage without MC SE
- Never claim "method X is best" — describe WHERE it's better
- Never hide negative results (high bias, poor coverage)
- Never use in-sample metrics as evidence of prediction accuracy
