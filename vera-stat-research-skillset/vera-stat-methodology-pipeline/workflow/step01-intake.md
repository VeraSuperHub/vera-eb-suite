# Step 01: Research Direction Intake

> **Executor**: Main Agent
> **Input**: $ARGUMENTS (research direction) + local project files
> **Output**: `PIPELINE_STATE.json` with research context

---

## Execution Instructions

### 1.1 Parse Research Direction

Extract from $ARGUMENTS:
- **Research direction**: The broad methodological area (e.g., "robust estimation for high-dimensional linear models with heavy-tailed errors")
- **Specificity level**: Is this broad ("causal inference") or narrow ("doubly robust estimators for missing data with high-dimensional confounders")?

If too broad (< 5 words), ask user to narrow:
```
Your direction "{direction}" is quite broad. Could you narrow it?
For example:
- "robust estimation for high-dimensional linear models"
- "semiparametric efficiency bounds for missing data"
- "Bayesian nonparametric methods for survival analysis"
```

### 1.2 Scan Existing Work

Check for prior work in the project directory:

| Directory | What to Look For |
|-----------|-----------------|
| `papers/`, `literature/`, `references/` | PDFs the user has already collected |
| `proofs/`, `theory/` | Existing proof sketches or theorem statements |
| `simulation/`, `sims/`, `code/` | Existing simulation code |
| `results/` | Prior simulation results |
| `paper/`, `manuscript/` | Draft manuscript in progress |
| `IDEA_DISCOVERY_REPORT.md` | Prior idea discovery run (enriched) |
| `IDEA_REPORT.md` | Prior raw idea brainstorm (from idea-creator) |
| `AUTO_REVIEW.md` | Prior review loop |
| `PIPELINE_STATE.json` | Prior pipeline state (check for resume) |

If `PIPELINE_STATE.json` exists with `status: "in_progress"` and is < 24 hours old:
- Offer to **resume** from last checkpoint
- Or **fresh start** (user chooses)

### 1.3 Identify Computational Environment

Detect available tools:
- R: check for `Rscript --version`
- Python: check for `python3 --version`
- LaTeX: check for `latexmk --version` or `pdflatex --version`
- Preferred language: check for existing `.R` or `.py` files in project

### 1.4 Set Up Project Structure

Create directories if they don't exist (all at project root):
```
simulation/
proofs/
real_data/
results/
logs/
paper/
paper/sections/
paper/figures/
```

**Note**: `proofs/` and `real_data/` are top-level directories, NOT nested under `simulation/`.
`logs/` is top-level (run-experiment writes `logs/sim_*.log`, monitor-experiment tails them there).

### 1.5 Write Initial State

```json
{
  "stage": 1,
  "status": "completed",
  "research_direction": "...",
  "specificity": "narrow",
  "existing_work": {
    "papers": 5,
    "prior_proofs": false,
    "prior_simulations": false,
    "prior_manuscript": false
  },
  "environment": {
    "r_available": true,
    "python_available": true,
    "latex_available": true,
    "preferred_language": "R"
  },
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 1a | Direction provided | Non-empty, ≥ 5 words | Ask user to elaborate |
| 1b | At least 1 language available | R or Python found | Error — need computation |
| 1c | Directory structure created | All dirs exist | Retry mkdir |
| 1d | State file written | PIPELINE_STATE.json valid JSON | Rewrite |

---

## Next Step
→ Step 02: Idea Discovery
