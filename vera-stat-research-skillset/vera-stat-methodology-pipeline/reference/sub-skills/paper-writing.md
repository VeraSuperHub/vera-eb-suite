<!-- Absorbed from skills/paper-writing/SKILL.md -->

# Paper Writing: Statistics Manuscript Pipeline (Workflow 3)

Full paper writing pipeline for: **$ARGUMENTS**

## Pipeline

### Phase 1: Paper Planning
```
Read and execute reference/sub-skills/paper-planning.md with context: "$ARGUMENTS"
```
Output: `PAPER_PLAN.md` with section-by-section outline, claims-evidence matrix, figure plan.

### Phase 2: Figure Generation
```
Read and execute reference/sub-skills/figure-creating.md
```
Input: figure plan from `PAPER_PLAN.md`.
Output: publication-quality figures in `paper/figures/`.

### Phase 3: LaTeX Writing
```
Read and execute reference/sub-skills/manuscript-writing.md with context: "$ARGUMENTS"
```
Input: `PAPER_PLAN.md` + figures.
Output: complete LaTeX manuscript in `paper/`.

### Phase 4: Compilation
```
Read and execute reference/sub-skills/paper-compiling.md
```
Output: `paper/main.pdf`.

### Phase 5: Improvement Loop
```
Read and execute reference/sub-skills/paper-improving.md
```
Output: polished manuscript (2 rounds of review + fixes).

### Phase 6: Final Report

```markdown
## Paper Writing Complete

- **PDF**: paper/main.pdf
- **Pages**: X (target: Y for [VENUE])
- **Score progression**: Round 0: A/10 → Round 1: B/10 → Round 2: C/10
- **Remaining issues**: [any unresolved items]

### Files Created
- paper/main.tex
- paper/sections/*.tex
- paper/figures/*.pdf
- paper/references.bib
- PAPER_PLAN.md

### Next Steps
- [ ] Author review of manuscript
- [ ] Verify all proofs manually
- [ ] Check simulation reproducibility
- [ ] Prepare supplementary materials
- [ ] Submit to [VENUE]
```

## Timeline

- Phase 1 (planning): 10-15 min
- Phase 2 (figures): 10-20 min
- Phase 3 (writing): 20-30 min
- Phase 4 (compilation): 2-5 min
- Phase 5 (improvement): 15-25 min
- **Total: 60-90 minutes**

## Key Rules

- Each phase must complete before the next begins
- If any phase fails, stop and report the error
- The paper should be submission-ready after Phase 5, but ALWAYS needs author review
- Proofs MUST be verified by the author — do not skip this step
- Simulation code should be reproducible — include seeds and package versions
