# Implementation Tracks

Defines the three parallel implementation tracks for Stage 3. All tracks launch simultaneously as SubAgents when their conditions are met.

## Track Architecture

```
Selected Idea
     │
     ├── Track A: Simulation Code ──→ simulation/
     │     (always active)
     │
     ├── Track B: Proof Sketches ──→ proofs/
     │     (if theoretical claims exist)
     │
     └── Track C: Real Data Prep ──→ real_data/
           (if empirical component exists)
```

All tracks are **independent** — no track depends on another's output. They can run fully in parallel.

## Track A: Simulation Code

**Always active.** Even purely theoretical work needs empirical validation.

### Output Structure
```
simulation/
├── simulation_code.R (or .py)
│   ├── # Setup: packages, seeds, parallel config
│   ├── # DGP functions: generate_data_scenario1(), generate_data_scenario2()
│   ├── # Proposed method: estimate_proposed(data, ...)
│   ├── # Competitor 1: estimate_competitor1(data, ...)
│   ├── # Competitor 2: estimate_competitor2(data, ...)
│   ├── # Metrics: compute_bias(), compute_coverage(), compute_power()
│   ├── # Main simulation loop (parallelized)
│   └── # Output: save results to results/
└── README.md (brief description of what the simulation does)
```

### DGP Requirements

| Element | Minimum | Notes |
|---------|---------|-------|
| Scenarios | 2 | Well-specified + misspecified |
| Sample sizes | 4 | n = (100, 200, 500, 1000) |
| Dimensions | 2+ (if HD) | p = (50, 200) or similar |
| Error distributions | 2 | Normal + heavy-tailed (if robust methods) |

### Method Interface Contract

Every method function must have the same interface:
```r
# R
estimate_method <- function(data, ...) {
  list(
    estimate = numeric,    # point estimate(s)
    se = numeric,          # standard error(s)
    ci_lower = numeric,    # 95% CI lower
    ci_upper = numeric,    # 95% CI upper
    pvalue = numeric,      # p-value (if test)
    time_seconds = numeric # computation time
  )
}
```

```python
# Python
def estimate_method(data, **kwargs):
    return {
        "estimate": float,
        "se": float,
        "ci_lower": float,
        "ci_upper": float,
        "pvalue": float,
        "time_seconds": float
    }
```

### Replication Counts

| Study Type | Replications (B) | Rationale |
|------------|-------------------|-----------|
| Coverage | ≥ 1,000 | MC SE of coverage ≈ 0.7% at B=1000 |
| Size/Power | ≥ 5,000 | MC SE of size ≈ 0.3% at B=5000 |
| Bias/RMSE | ≥ 1,000 | Sufficient for stable estimates |
| Timing | ≥ 100 | Enough to average out system noise |

## Track B: Proof Sketches

**Active when**: Selected idea has theoretical claims (consistency, asymptotic normality, efficiency bounds, convergence rates, etc.)

### Output Structure
```
proofs/
├── ASSUMPTIONS.md
│   ├── A1: [condition] — used in Theorem 1
│   ├── A2: [condition] — used in Theorems 1, 2
│   ├── ...
│   └── Note which are standard vs. novel
│
├── THEOREM_1.tex
│   ├── \begin{theorem}[Title] ... \end{theorem}
│   ├── Proof sketch (major steps)
│   ├── Key lemmas (stated)
│   └── [VERIFY] markers on difficult steps
│
├── THEOREM_2.tex (if applicable)
│   └── (same structure)
│
├── LEMMA_1.tex (if needed separately)
│
└── PROOF_OUTLINE.md
    ├── Overall strategy
    ├── Theorem → lemma dependency graph
    ├── Proof techniques (CLT, delta method, etc.)
    └── Known gaps or difficulties
```

### Common Proof Patterns

| Method Type | Typical Theorems | Proof Techniques |
|-------------|------------------|------------------|
| M-estimator | Consistency, asymptotic normality | Empirical process theory, Z-estimator CLT |
| Penalized regression | Oracle property, selection consistency | KKT conditions, restricted eigenvalue |
| Semiparametric | Efficiency bound, rate optimality | Influence function, semiparametric theory |
| Bayesian | Posterior consistency, BvM theorem | Prior concentration, testing conditions |
| Nonparametric | Convergence rate, adaptivity | Kernel/basis expansion, bias-variance |
| Causal inference | Identification, doubly robust | Potential outcomes, IF derivation |

### Proof Sketch Quality Bar

A proof sketch should contain enough detail that a human mathematician can:
1. Understand the overall strategy
2. Fill in routine steps without guidance
3. Identify which steps are genuinely difficult
4. Verify the logic of the argument

Mark with `[VERIFY]` any step that:
- Involves a non-trivial bound
- Requires a careful epsilon-delta argument
- Depends on a condition that might not hold
- Uses a technique you're not 100% sure applies

## Track C: Real Data Preparation

**Active when**: Selected idea has an empirical component beyond simulations.

### Output Structure
```
real_data/
├── data_load.R (or .py)
│   ├── # Load dataset
│   ├── # Preprocessing (missingness, transformations)
│   ├── # Summary statistics
│   └── # Save processed data
│
├── analysis_script.R (or .py)
│   ├── # Apply proposed method
│   ├── # Apply competitors
│   ├── # Compare results
│   └── # Save output to results/
│
└── sensitivity_analysis.R (or .py)
    ├── # Vary assumptions
    ├── # Subset analyses
    └── # Alternative specifications
```

### Common Real Data Sources for Statistics Papers

| Domain | Datasets | Where to Find |
|--------|----------|---------------|
| Biostatistics | Clinical trials, observational health data | R packages (survival, KMsurv) |
| Economics | Panel data, policy evaluations | R packages (AER, wooldridge) |
| Environmental | Air quality, climate | EPA, NOAA public data |
| Genetics | GWAS, gene expression | Bioconductor |
| Social science | Survey data, experiments | R packages (MASS, datasets) |

If no natural real dataset exists for the method, the analysis script should:
1. Use a well-known benchmark dataset
2. Clearly state why it was chosen
3. Demonstrate the method works on real-world structure (not just simulated data)

---

## Parallelization Rules

1. All active tracks launch simultaneously — no waiting
2. Each track is a separate SubAgent with its own context
3. Tracks share no intermediate outputs (fully independent)
4. Main Agent monitors all tracks and collects results
5. Pre-flight check (Track A only) runs after Track A completes but doesn't block B or C
6. If any track fails: log error, continue other tracks, note gap in state
