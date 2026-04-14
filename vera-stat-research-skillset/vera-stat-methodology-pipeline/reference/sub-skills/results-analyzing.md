<!-- Absorbed from skills/analyze-results/SKILL.md -->

# Analyze Results: Statistics Simulation Analysis

Systematically analyze simulation results for: **$ARGUMENTS**

## Workflow

### Step 1: Locate Results

Search for output files:
```bash
# R results
find . -name "*.rds" -o -name "*.RData" | head -20
find results/ -name "*.csv" 2>/dev/null

# Python results
find . -name "*.pkl" -o -name "*.json" | head -20

# Log files with embedded results
find logs/ -name "*.log" 2>/dev/null
```

### Step 2: Load and Structure Results

Read results and organize into comparison tables. Standard statistics simulation metrics:

**For estimation:**
| Method | n | Bias | Var | MSE | RMSE | Relative Efficiency |
|--------|---|------|-----|-----|------|---------------------|

**For confidence intervals / coverage:**
| Method | n | Coverage (nominal 95%) | MC SE | Avg Width | Median Width |
|--------|---|------------------------|-------|-----------|-------------|

**For hypothesis testing:**
| Method | n | Size (nominal 5%) | MC SE | Power (δ=0.2) | Power (δ=0.5) | Power (δ=1.0) |
|--------|---|-------------------|-------|----------------|----------------|----------------|

**For MCMC / Bayesian:**
| Model | Parameter | Rhat | ESS_bulk | ESS_tail | Posterior Mean | 95% CI | Coverage |
|-------|-----------|------|----------|----------|----------------|--------|----------|

**For computation:**
| Method | n | Median Time (s) | IQR Time | Scalability (time ratio n=1000/n=100) |
|--------|---|-----------------|----------|---------------------------------------|

### Step 3: Statistical Analysis of Simulation Results

For each comparison:

1. **Point estimates with MC standard errors**:
   - Bias MC SE = SD(estimates) / √B
   - Coverage MC SE = √(p̂(1-p̂)/B)
   - Always report these — a coverage of 94.2% at B=1000 has MC SE ≈ 0.74%, so it's not significantly different from 95%

2. **Convergence rate verification** (for theory papers):
   - Plot log(MSE) vs log(n) — slope should match theoretical rate
   - Plot log(bias) vs log(n) — check bias order
   - Compute empirical convergence rates and compare with theory

3. **Multi-seed analysis** (if multiple random seeds):
   - Report mean ± std across seeds
   - Flag high variance across seeds (simulation instability)

4. **Trend identification**:
   - How do metrics change with n? (should improve)
   - How do metrics change with dimension p? (for high-dimensional settings)
   - How do metrics change under model misspecification?
   - Identify the "crossover point" where the proposed method starts outperforming competitors

5. **Outlier detection**:
   - Identify scenarios where the method fails or degrades
   - Check for non-monotone behavior (e.g., coverage getting worse with larger n — indicates a bug)
   - Flag any NaN, Inf, or extreme values

### Step 4: Generate Insights

For each finding, structure as:

```markdown
### Finding: [title]
- **Observation**: [what the data shows — specific numbers]
- **Statistical significance**: [is this beyond MC error?]
- **Interpretation**: [why this happens — connect to theory]
- **Implication for the paper**: [what claim this supports or contradicts]
- **Next step**: [what to do about it]
```

Example findings:

```markdown
### Finding: Proposed estimator achieves faster convergence under heavy tails
- **Observation**: MSE ratio (proposed/MLE) = 0.72 at n=100, 0.58 at n=1000 under t(3) errors
- **Statistical significance**: Difference is 8× MC SE — clearly significant
- **Interpretation**: Consistent with Theorem 2 which predicts O(n^{-4/5}) vs O(n^{-2/3}) rate under heavy tails
- **Implication**: This is the paper's strongest empirical result — should be highlighted in abstract
- **Next step**: Add t(5) and Cauchy to show the effect across tail heaviness
```

### Step 5: Generate Summary Tables and Figures

Create publication-ready summary:

```markdown
## Results Summary

### Main Findings
1. [Most important finding with specific numbers]
2. [Second most important]
3. [Third]

### Evidence for Each Claim
| Claim | Supported? | Key Evidence | Strength |
|-------|-----------|--------------|----------|
| [claim 1] | Yes | MSE 25% lower, p < MC SE | Strong |
| [claim 2] | Partially | Coverage 94.2% (MC SE 0.49%) | Moderate |
| [claim 3] | No | Power comparable, not superior | Weak |

### Recommended Figures for Paper
1. [Figure description — what to plot, what message it conveys]
2. [Figure description]

### Anomalies and Concerns
- [Any unexpected results that need investigation]

### Additional Simulations Needed
- [Scenarios not yet covered]
- [Comparison methods not yet included]
```

### Step 6: Update Documentation

Write analysis to `RESULTS_ANALYSIS.md` and update project notes.

## Key Rules

- ALWAYS report Monte Carlo standard errors — a result without MC SE is uninterpretable
- Compare with THEORY when available (rates, efficiency bounds)
- Don't over-interpret differences within MC error
- Coverage within 2 MC SE of nominal is acceptable (e.g., at B=2000, 95% ± 0.97%)
- Size inflation > 1 percentage point is a real concern — don't dismiss it
- For high-dimensional simulations: report p/n ratio, not just n
- Check that results are consistent across random seeds
- Always compute relative efficiency (MSE ratio) when comparing estimators
- For Bayesian methods: posterior coverage ≠ frequentist coverage — report both if relevant
