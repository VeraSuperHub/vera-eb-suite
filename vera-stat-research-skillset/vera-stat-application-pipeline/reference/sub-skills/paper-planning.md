<!-- Absorbed from skills/paper-plan/SKILL.md -->

# Paper Plan: Statistics Paper Outline

Generate a structured, section-by-section paper outline from: **$ARGUMENTS**

## Constants

- **REVIEWER_MODEL = `gpt-5.4`**
- **TARGET_VENUE = `JASA`** — Default venue. User can override (e.g., `/paper-plan "topic" — venue: Annals`).
  Supported: `JASA` (JASA T&M), `JASA-ACS` (Applications), `Annals`, `JRSSB`, `Biometrika`, `BayesAnal`, `EJS`.
- **MAX_PAGES** — Varies by venue:
  - JASA: ~25-30 pages (double-spaced manuscript format)
  - Annals of Statistics: ~30-40 pages (manuscript format)
  - JRSS-B: ~25-30 pages
  - Biometrika: ~15-20 pages (shorter, more concise style)
  - EJS: no strict limit, but 20-35 pages typical

## Inputs

The skill expects one or more of these in the project directory:
1. **NARRATIVE_REPORT.md** or **STORY.md** — research narrative
2. **AUTO_REVIEW.md** — auto-review loop conclusions
3. **Simulation results** — .rds, .csv, .json files in `results/` or `simulations/`
4. **Proof sketches** — .tex or .md files with theorem statements and proofs
5. **IDEA_REPORT.md** — from idea-discovery pipeline

If none exist, ask the user to describe the paper's contribution in 3-5 sentences.

## Workflow

### Step 1: Extract Claims and Evidence

Read all available documents and extract:

1. **Core theoretical claims** (theorems, propositions, corollaries)
2. **Methodological claims** (the proposed method has property X)
3. **Empirical evidence** (which simulations support which claims)
4. **Real data results** (application findings)
5. **Known weaknesses** (from reviewer feedback)

Build a **Claims-Evidence Matrix**:

```markdown
| Claim | Type | Evidence | Status | Section |
|-------|------|----------|--------|---------|
| Estimator is consistent | Theory | Theorem 1 proof | Proved | §2 |
| Rate is minimax optimal | Theory | Theorem 2 + lower bound | Proved | §2.3 |
| Outperforms MLE under contamination | Empirical | Sim Study 1 | Supported | §4 |
| Coverage is nominal | Empirical | Sim Study 2 | Supported (94.8% at n=500) | §4 |
| Real data: detects effect missed by standard approach | Applied | NHANES analysis | Demonstrated | §5 |
```

### Step 2: Determine Paper Type and Structure

**Theory paper (Annals / Biometrika style):**
```
1. Introduction (3-4 pages)
2. Problem Setup and Notation (2-3 pages)
3. Main Results (4-6 pages)
   3.1 Estimation / The Proposed Method
   3.2 Theoretical Properties (consistency, rates)
   3.3 Inference (confidence intervals, testing)
4. Simulation Study (3-4 pages)
5. Real Data Application (2-3 pages)
6. Discussion (1-2 pages)
Appendix: Proofs (as long as needed)
Supplementary Material: Additional simulations, technical lemmas
```

**Methodology paper (JASA T&M style):**
```
1. Introduction (3-4 pages)
2. Background and Related Work (2-3 pages)
3. Proposed Method (4-5 pages)
   3.1 Model and Setup
   3.2 Estimation Procedure
   3.3 Computational Algorithm
   3.4 Theoretical Properties
4. Simulation Study (4-5 pages)
5. Application (3-4 pages)
6. Discussion (1-2 pages)
Appendix: Proofs, Additional simulations
```

**Applied statistics paper (JASA ACS / JRSS-A style):**
```
1. Introduction (2-3 pages)
2. Data and Scientific Background (2-3 pages)
3. Statistical Model (3-4 pages)
4. Results (4-5 pages)
5. Sensitivity Analysis / Model Checking (2-3 pages)
6. Discussion (2-3 pages)
Appendix: Technical details
```

**Bayesian paper (Bayesian Analysis style):**
```
1. Introduction (2-3 pages)
2. Model Specification (3-4 pages)
   2.1 Likelihood
   2.2 Prior Specification and Justification
3. Posterior Computation (2-3 pages)
   3.1 MCMC Algorithm
   3.2 Convergence Diagnostics
4. Theoretical Properties (2-3 pages)
   4.1 Posterior Consistency / Contraction Rate
5. Simulation Study (3-4 pages)
6. Application (3-4 pages)
7. Discussion (1-2 pages)
```

### Step 3: Section-by-Section Planning

For each section, specify:

```markdown
### §0 Abstract
- **Problem**: [what statistical problem, in one sentence]
- **Gap**: [what's missing in existing approaches]
- **Contribution**: [what this paper provides — method, theory, or both]
- **Key finding**: [most compelling result — rate, efficiency gain, or empirical improvement]
- **Estimated length**: 150-250 words

### §1 Introduction
- **Opening**: [motivating application or statistical problem]
- **Gap in literature**: [what existing methods cannot do]
- **Contribution summary**: [numbered list matching Claims-Evidence Matrix]
- **Key notation introduced**: [define main symbols]
- **Organization paragraph**: [roadmap of the paper]
- **Key citations**: [5-8 foundational papers]

### §2 Setup / Background
- **Notation table**: [all key symbols defined in one place]
- **Model**: [formal statistical model: X_i ~ F_θ, etc.]
- **Assumptions**: [numbered list: (A1), (A2), ... with discussion of each]
- **Existing approaches**: [brief review of alternatives, positioned for comparison]

### §3 Main Results / Proposed Method
- **Theorem statements**: [list each theorem with its assumptions]
- **Proof strategy**: [outline the proof approach for each major result]
- **Main body vs. appendix**: [which proof details go where]
- **Algorithms**: [pseudocode for computational procedures]
- **Remark blocks**: [discuss implications of each result]

### §4 Simulation Study
- **Data-generating processes**: [list each DGP with full parameter specification]
- **Sample sizes**: [e.g., n = 100, 200, 500, 1000, 2000]
- **Competing methods**: [which existing methods to compare]
- **Metrics**: [bias, MSE/RMSE, coverage probability, power, computation time]
- **Number of replications**: [B = 2000 minimum for coverage; B = 5000 for size/power]
- **Tables planned**: [which tables show which comparisons]
- **Figures planned**: [which plots — box plots, coverage curves, power curves]

### §5 Real Data Application
- **Dataset**: [source, size, variables]
- **Scientific question**: [what the analysis aims to answer]
- **Analysis approach**: [how the proposed method is applied]
- **Comparison with standard approach**: [what existing analysis shows vs. what we find]
- **Sensitivity checks**: [robustness to model assumptions]

### §6 Discussion
- **Summary of contributions**: [rephrased, not copy-pasted]
- **Limitations**: [honest assessment — conditions not covered, computational constraints]
- **Future work**: [1-2 concrete extensions]
- **Broader impact**: [how this method could be used in practice]
```

### Step 4: Figure and Table Plan

```markdown
## Figure and Table Plan

| ID | Type | Description | Data Source | Priority |
|----|------|-------------|-------------|----------|
| Fig 1 | Schematic | Method overview / intuition diagram | manual | HIGH |
| Fig 2 | Line plot | MSE vs. n (log-log) for proposed vs. competitors | results/sim1.csv | HIGH |
| Fig 3 | Coverage plot | Empirical vs. nominal coverage across n | results/sim2.csv | HIGH |
| Fig 4 | Power curves | Power vs. effect size for competing tests | results/sim3.csv | MEDIUM |
| Fig 5 | Box plots | Distribution of estimates across DGPs | results/sim1.csv | MEDIUM |
| Fig 6 | Real data | Application results visualization | data/application.csv | HIGH |
| Table 1 | Comparison | Bias and MSE across methods and sample sizes | results/sim1.csv | HIGH |
| Table 2 | Coverage | Coverage probabilities and interval widths | results/sim2.csv | HIGH |
| Table 3 | Real data | Application results table | data/application.csv | HIGH |
| Table 4 | Theory comparison | This paper's rates vs. prior work | manual | HIGH (theory papers) |
```

### Step 5: Citation Scaffolding

```markdown
## Citation Plan
- §1 Intro: [foundational papers motivating the problem]
- §2 Setup: [key references for the statistical framework]
- §3 Method: [papers whose techniques we build on or extend]
- §4 Simulations: [papers proposing competing methods]
- §5 Application: [papers analyzing the same or similar data]
- Classic references: [Lehmann, van der Vaart, Bickel et al., etc.]
```

**Citation rules:**
1. NEVER generate BibTeX from memory — always verify via search or existing .bib files
2. Flag uncertain citations with `[VERIFY]`
3. Prefer published journal versions over arXiv preprints
4. Statistics values proper attribution to classic work — don't omit foundational references

### Step 6: Cross-Review with REVIEWER_MODEL

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    Review this paper outline for a [VENUE] submission in statistics.
    [full outline including Claims-Evidence Matrix]

    Score 1-10 on:
    1. Logical flow — does the paper build naturally from problem to solution to evidence?
    2. Claim-evidence alignment — every theorem supported by proof, every claim by simulation?
    3. Simulation study completeness — are enough scenarios covered?
    4. Theoretical depth — are the results strong enough for [VENUE]?
    5. Application quality — is the real data analysis compelling?
    6. Positioning — how well does this compare to the best recent papers in [VENUE]?

    For each weakness, suggest the MINIMUM fix.
```

### Step 7: Output

Save to `PAPER_PLAN.md`:

```markdown
# Paper Plan

**Title**: [working title]
**Venue**: [target venue]
**Type**: [theory/methodology/applied/Bayesian]
**Date**: [today]
**Estimated length**: [X pages manuscript format]

## Claims-Evidence Matrix
[from Step 1]

## Structure
[from Steps 2-3, section by section]

## Figure and Table Plan
[from Step 4]

## Citation Plan
[from Step 5]

## Reviewer Feedback
[from Step 6]

## Next Steps
- [ ] /paper-figure to generate simulation plots
- [ ] /paper-write to draft LaTeX
- [ ] /paper-compile to build PDF
```

## Key Rules

- **Do NOT generate author information** — leave as placeholder or anonymous
- **Assumptions are critical** — every theorem needs clearly stated conditions
- **Simulation design must be defensible** — reviewers WILL question DGP choices
- **Include proofs or proof sketches** — statistics papers require them (appendix is fine)
- **Monte Carlo standard errors** must be reported in all simulation tables
- **Claims-Evidence Matrix is the backbone** — every claim maps to evidence
- **Different venues have very different styles** — Biometrika is concise; Annals allows long proofs; JASA wants applications
