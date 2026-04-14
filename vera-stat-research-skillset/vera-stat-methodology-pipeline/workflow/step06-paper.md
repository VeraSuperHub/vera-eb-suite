# Step 06: Paper Writing (LaTeX + PDF)

> **Executor**: Main Agent (invokes `reference/sub-skills/paper-writing.md`)
> **Input**: All project artifacts + `AUTO_REVIEW.md` + `RESULTS_ANALYSIS.md`
> **Output**: `paper/main.pdf` + complete `paper/` directory + `RESEARCH_LOG.md`

---

## Execution Instructions

### 6.1 Launch Paper Writing Pipeline

```
Read and execute reference/sub-skills/paper-writing.md with context: "$ARGUMENTS"
```

This invokes the existing `paper-writing` workflow skill which chains 5 sub-skills:

#### Phase 1: Paper Planning (`reference/sub-skills/paper-planning.md`)

Input: AUTO_REVIEW.md, RESULTS_ANALYSIS.md, simulation results, proofs
Output: `PAPER_PLAN.md` with:
- Claims-evidence matrix (claim → type → evidence → status → section)
- Section-by-section outline with page targets
- Figure and table plan
- Citation plan

Paper type detection (from selected idea):
- **Theory**: Emphasis on assumptions, theorems, proofs. Simulations support theory.
- **Methodology**: Balance of theory + simulations. Real data validates.
- **Applied**: Emphasis on real data. Methods section shorter.
- **Bayesian**: Include MCMC diagnostics, prior sensitivity, posterior checks.

#### Phase 2: Figure Generation (`reference/sub-skills/figure-creating.md`)

Generate publication-quality figures from simulation results:

| Figure Type | Source | Format |
|-------------|--------|--------|
| Convergence rate plot | results/comparison_table.csv | PDF + PNG |
| Coverage probability plot | results/sim_results.* | PDF + PNG |
| Power curves | results/sim_results.* | PDF + PNG |
| Box plots of estimates | results/sim_results.* | PDF + PNG |
| Real data results | real_data/ outputs | PDF + PNG |
| MCMC diagnostics (Bayesian) | results/ | PDF + PNG |

Requirements:
- PDF vector graphics for LaTeX
- 300 DPI PNG raster backup
- Colorblind-safe palettes
- LaTeX math in axis labels
- Monte Carlo error bars on simulation plots
- Nominal reference lines (e.g., 95% coverage line)
- Reproducible generation scripts in `paper/figures/gen_*.{R,py}`

#### Phase 3: LaTeX Writing (`reference/sub-skills/manuscript-writing.md`)

Venue-specific LaTeX manuscript:

| Section | Content Source | Key Elements |
|---------|---------------|--------------|
| Abstract | Synthesize all sections | 150-250 words, key numbers |
| Introduction | Literature + selected idea | Context, gap, contribution |
| Setup/Background | ASSUMPTIONS.md + notation | Formal problem statement |
| Main Results | THEOREM_*.tex | Theorems + proof sketches (full in appendix) |
| Simulations | RESULTS_ANALYSIS.md | Tables with MC SEs, figures |
| Application | real_data/ results | Real data findings |
| Discussion | AUTO_REVIEW.md insights | Summary, limitations, future |
| Appendix | Full proofs | Complete proof details |

Writing standards:
- `\begin{assumption}`, `\begin{theorem}`, `\begin{lemma}` environments
- `\newcommand` for frequently used notation
- `\citet{}` / `\citep{}` citations
- Tables with MC standard errors in parentheses
- All [VERIFY] markers from proofs must be resolved or flagged

#### Phase 4: Compilation (`reference/sub-skills/paper-compiling.md`)

Compile LaTeX to PDF:
1. Pre-flight: all `\input` files exist, all figures present
2. Compile: `latexmk -pdf paper/main.tex`
3. Auto-fix errors (up to 3 iterations)
4. Post-check: no `??` references, bibliography renders

#### Phase 5: Writing Improvement (`reference/sub-skills/paper-improving.md`)

2 rounds of writing-focused polish:
- Notation consistency across sections
- Proof presentation clarity
- De-AI artifacts in prose
- Simulation table formatting
- Citation accuracy
- Abstract ↔ conclusion alignment

### 6.2 Generate Research Log

After paper pipeline completes, write `RESEARCH_LOG.md`:

```markdown
# Methodology Research Pipeline — Execution Log

## Pipeline Metadata
- **Research Direction**: {from PIPELINE_STATE}
- **Selected Idea**: {title} (novelty: {score}/10)
- **Idea Selection**: {auto/manual}, Gate 1

## Stage Progression
| Stage | Status | Duration | Notes |
|-------|--------|----------|-------|
| 1. Intake | Completed | — | {environment summary} |
| 2. Idea Discovery | Completed | ~{X} min | {N} ideas → {N} validated → selected #{N} |
| 3. Implementation | Completed | ~{X} min | Tracks: {list} |
| 4. Experiments | Completed | ~{X} hours | B={reps}, n={sizes}, {N} methods |
| 5. External Review | Completed | ~{X} hours | {N} rounds, final: {score}/10 |
| 6. Paper Writing | Completed | ~{X} min | {pages} pages, {venue} format |

## Key Results
- {Finding 1}
- {Finding 2}
- {Finding 3}

## Review Score Progression
Round 1: {score}/10 → Round 2: {score}/10 → ... → Final: {score}/10

## Deliverables
- `paper/main.pdf` — Manuscript
- `paper/main.tex` — LaTeX source
- `simulation/simulation_code.{R,py}` — Simulation code
- `proofs/` — Theorem statements and proof sketches
- `results/` — Raw simulation output
- `IDEA_DISCOVERY_REPORT.md` — Idea exploration
- `AUTO_REVIEW.md` — Review loop log
- `PAPER_PLAN.md` — Paper outline

## Remaining Work for Author
- [ ] Verify ALL proofs manually — AI proofs need human verification
- [ ] Review simulation results for correctness
- [ ] Check paper for remaining [VERIFY] markers
- [ ] Confirm notation consistency
- [ ] Add acknowledgments, funding, author affiliations
- [ ] Prepare supplementary materials
- [ ] Package reproducibility bundle (code + data + seeds)
- [ ] Review and approve before submission
```

### 6.3 Update Final State

```json
{
  "stage": 6,
  "status": "completed",
  "paper": {
    "venue": "article",
    "pages": 22,
    "compile_status": "success",
    "improvement_rounds": 2,
    "final_improvement_score": 7.5
  },
  "total_pipeline_hours": 4.2,
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 6a | PAPER_PLAN.md exists | Claims-evidence matrix complete | Regenerate |
| 6b | Figures generated | PDF + PNG for each planned figure | Regenerate missing |
| 6c | LaTeX sections complete | All \input files exist | Regenerate missing section |
| 6d | PDF compiles | paper/main.pdf exists, no errors | Auto-fix, retry (3x) |
| 6e | No [VERIFY] in paper | Grep finds 0 instances in .tex files | Flag for author |
| 6f | Bibliography complete | All citations resolve | Fix .bib |
| 6g | RESEARCH_LOG.md written | Complete execution trace | Generate from state |

---

## Pipeline Complete

The methodology research pipeline has produced:
- A novel statistical method with theoretical foundations
- Simulation evidence supporting the method
- Real data application (if applicable)
- A publication-ready LaTeX manuscript
- Complete reproducibility bundle

**Critical reminder**: All proofs MUST be verified by the author. The pipeline produces a DRAFT.
