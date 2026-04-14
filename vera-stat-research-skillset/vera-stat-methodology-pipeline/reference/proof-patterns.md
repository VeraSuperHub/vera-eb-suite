# Proof Patterns

Common proof structures and templates for methodology research in statistics.

## Theorem Statement Template

```latex
\begin{assumption}[A\theassumption: Name]\label{asm:name}
[Condition statement in mathematical notation]
\end{assumption}

\begin{theorem}[Main Result]\label{thm:main}
Under Assumptions A1--A$k$, as $n \to \infty$,
\[
  \sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} N(0, V(\theta_0)),
\]
where $V(\theta_0) = [specific variance expression]$.
\end{theorem}
```

## Common Proof Strategies by Method Type

### M-Estimator Consistency

```
Strategy:
1. Define the criterion function M_n(θ)
2. Show M_n converges uniformly to M(θ) (ULLN)
3. Show M(θ) has unique maximum at θ₀ (identifiability)
4. Apply argmax continuous mapping theorem

Key tools: ULLN, compactness, continuity of M
Difficulty: uniform convergence, especially in semiparametric settings
```

### Asymptotic Normality (Z-Estimator)

```
Strategy:
1. Taylor expand the estimating equation ψ_n(θ̂) = 0 around θ₀
2. Show √n · ψ_n(θ₀) → N(0, Σ) (CLT for the score)
3. Show ∂ψ_n/∂θ → A (LLN for the Hessian)
4. Conclude √n(θ̂ - θ₀) → N(0, A⁻¹ΣA⁻ᵀ) (sandwich)

Key tools: CLT, Slutsky, delta method
Difficulty: verifying Lyapunov/Lindeberg conditions, handling non-iid data
```

### Oracle Property (Penalized Estimation)

```
Strategy:
1. Show selection consistency: P(Ŝ = S₀) → 1 (correct active set)
2. Show estimation consistency: √n(θ̂_S₀ - θ₀_S₀) → N(0, V)
3. Key: penalty must grow fast enough to kill noise variables
   but slowly enough to keep signal variables

Key tools: KKT conditions, restricted eigenvalue, irrepresentable condition
Difficulty: balancing penalty rate, establishing restricted eigenvalue
```

### Semiparametric Efficiency

```
Strategy:
1. Compute the efficient influence function (EIF)
2. Show the estimator is RAL (regular asymptotically linear)
3. Show the influence function equals the EIF
4. Conclude efficiency: variance = semiparametric efficiency bound

Key tools: tangent space, pathwise derivatives, projection
Difficulty: computing the EIF, establishing RAL representation
```

### Convergence Rate (Nonparametric)

```
Strategy:
1. Decompose error: bias + variance (bias-variance tradeoff)
2. Bound bias: depends on smoothness class and approximation method
3. Bound variance: depends on effective dimension / degrees of freedom
4. Optimize bandwidth/tuning parameter
5. Show rate matches minimax lower bound (if claiming optimality)

Key tools: approximation theory, empirical process bounds, Fano/Le Cam
Difficulty: tight bounds, matching lower bound
```

## Assumption Categories

### Standard Assumptions (cite, don't prove)

| Assumption | When Used | Standard Citation |
|------------|-----------|-------------------|
| iid sampling | Most settings | State once |
| Finite moments (E[X⁴] < ∞) | CLT applications | Standard |
| Continuous density | Kernel methods | Standard |
| Compact parameter space | Consistency | Standard |
| Interior point (θ₀ ∈ int Θ) | Taylor expansion | Standard |

### Method-Specific Assumptions (state precisely)

| Assumption | When Used | Must Verify |
|------------|-----------|-------------|
| Restricted eigenvalue | LASSO theory | Yes — data dependent |
| Positivity / overlap | Causal inference | Yes — check in data |
| Proportional hazards | Cox model | Yes — Schoenfeld test |
| Stationarity | Time series | Yes — ADF/KPSS test |
| Exchangeability | Bayesian | Justify from design |

### Novel Assumptions (justify carefully)

If your method requires a NEW assumption not standard in the literature:
1. State it formally with mathematical precision
2. Explain WHY it's needed (which proof step uses it)
3. Discuss WHEN it holds (give examples of data-generating processes)
4. Compare with alternatives (is there a weaker sufficient condition?)
5. Verify empirically if possible (does the assumption hold in your real data?)

## Proof Sketch Depth Guide

| Proof Element | Sketch Level | Full Level |
|---------------|-------------|------------|
| Overall strategy | 2-3 sentences | Full paragraph |
| Key inequalities | State without proof | Derive step by step |
| Standard results | "By CLT..." | State lemma, cite |
| Novel arguments | Outline approach | Complete argument |
| Technical lemmas | State, defer to appendix | Full proof |
| Constants | "For some C > 0" | Track exact constants |

For the pipeline, produce **Sketch Level**. Mark anything requiring Full Level with `[VERIFY]`.

## LaTeX Environments

```latex
% In preamble
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}
\theoremstyle{definition}
\newtheorem{assumption}{Assumption}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}
```

## Quality Markers

Use these markers in proof sketches:

| Marker | Meaning |
|--------|---------|
| `[VERIFY]` | Step needs human verification |
| `[STANDARD]` | Standard result, cite but don't prove |
| `[TECHNICAL]` | Requires careful epsilon-delta work |
| `[KEY STEP]` | The conceptually important part of the proof |
| `[TODO]` | Incomplete — needs more work |
| `[CONJECTURE]` | Believed true but not proven |
