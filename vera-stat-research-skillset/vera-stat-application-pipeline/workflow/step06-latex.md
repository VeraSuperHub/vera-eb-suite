# Step 06: LaTeX Manuscript & PDF Compilation

> **Executor**: Main Agent (invokes paper-writing sub-skills)
> **Input**: `output/manuscript.md` + all `output/` artifacts
> **Output**: `paper/main.tex`, `paper/sections/*.tex`, `paper/figures/*.pdf`, `paper/main.pdf`

---

## Execution Instructions

### 6.1 Prerequisites

Verify Stage 5 outputs exist:
- `output/manuscript.md` — complete Markdown manuscript
- `output/figures/` — all figures (PNG, 300 DPI)
- `output/tables/` — all tables
- `output/references.bib` — merged bibliography
- `PIPELINE_STATE.json` — venue/style info

Read target venue from PIPELINE_STATE.json (`venue_style` field).

### 6.2 Prepare Inputs for Paper Sub-Skills

The `reference/sub-skills/paper-planning.md` procedure expects specific root-level files, NOT `output/manuscript.md`.
Prepare these files so the sub-skills can find them:

```
# 1. Copy simulation/analysis results to where paper-plan expects them
cp output/results.md RESULTS_ANALYSIS.md          # paper-plan reads this
cp output/references.bib references.bib            # root-level bib

# 2. Create NARRATIVE_REPORT.md from manuscript.md (paper-plan's expected input)
#    This is NOT a copy — extract the structured content paper-plan needs:
Write NARRATIVE_REPORT.md containing:
  - Research question (from PIPELINE_STATE.json)
  - Key findings (from output/results.md — summary)
  - Methods used (from output/methods.md — summary)
  - Literature context (from output/literature_review.md — summary)

# 3. Ensure figures are accessible
cp -r output/figures/ figures/                     # paper-figure reads from here
cp -r output/tables/ tables/                       # paper-plan reads from here
```

**Why**: The paper-writing sub-skills were designed for the methodology pipeline where
results accumulate in root-level files (RESULTS_ANALYSIS.md, AUTO_REVIEW.md, etc.).
Our application pipeline stores outputs under `output/`. This step bridges the gap.

### 6.3 Paper Planning

```
Read and execute reference/sub-skills/paper-planning.md with context: "$ARGUMENTS"
```

Now that root-level files are prepared, the paper-planning procedure will:
- Read NARRATIVE_REPORT.md + RESULTS_ANALYSIS.md
- Extract claims → build claims-evidence matrix
- Map sections to target venue structure
- Generate figure/table plan from existing figures

Output: `PAPER_PLAN.md`

If the paper-planning procedure asks for a description (because it can't find expected files),
provide: "{research_question}. Full analysis results are in RESULTS_ANALYSIS.md
and NARRATIVE_REPORT.md."

### 6.4 Figure Conversion

```
Read and execute reference/sub-skills/figure-creating.md
```

Convert existing PNG figures to PDF vector format for LaTeX:
- For each `output/figures/*.png` (now also in `figures/`):
  - If the figure was generated from R/Python code: re-render as PDF using the track's code
  - If re-rendering not feasible: convert PNG → PDF at high quality
- Apply consistent sizing for the target venue
- Ensure colorblind-safe palettes preserved

Output: `paper/figures/*.pdf` + `paper/figures/*.png` (keep both formats)

### 6.5 LaTeX Writing

```
Read and execute reference/sub-skills/manuscript-writing.md with context: "$ARGUMENTS"
```

The manuscript-writing procedure requires `PAPER_PLAN.md` (created in 6.3). It reads the plan's
claims-evidence matrix and section outline, then writes LaTeX.

Since we already have full prose in `output/manuscript.md`, the LaTeX writing step
should CONVERT the existing content rather than generating from scratch. Provide
this guidance to the manuscript-writing procedure:

"Convert the existing manuscript content from output/manuscript.md into LaTeX format.
Use PAPER_PLAN.md for structure. The prose is already written — translate it to
LaTeX with proper environments, citations, and formatting."

Convert `output/manuscript.md` sections into LaTeX:

| Markdown Section | LaTeX File | Notes |
|------------------|------------|-------|
| Abstract | `paper/sections/abstract.tex` | 150-250 words, no citations |
| 1. Introduction | `paper/sections/introduction.tex` | `\citet{}` / `\citep{}` citations |
| 2. Data & Study Design | `paper/sections/data.tex` | Table 1 as `\begin{table}` |
| 3. Statistical Methods | `paper/sections/methods.tex` | Math notation via `\newcommand` |
| 4. Results | `paper/sections/results.tex` | `\begin{table}`, `\begin{figure}` |
| 5. Discussion | `paper/sections/discussion.tex` | Standard prose |
| References | `paper/references.bib` | Copy from `output/references.bib` |

**Venue-specific preamble** (from manuscript-writing procedure):

| Venue | Document Class | Key Packages |
|-------|----------------|--------------|
| JASA | `\documentclass[default]{jasa}` | asa template |
| Annals of Statistics | `\documentclass[imsstyle]{imsart}` | IMS template |
| Biometrika | `\documentclass{biomet}` | Biometrika template |
| APA 7th | `\documentclass[man]{apa7}` | apa7 package |
| General | `\documentclass[12pt]{article}` | amsmath, natbib, graphicx |

**LaTeX conventions**:
- Define `\newcommand` for frequently used notation
- `\begin{assumption}`, `\begin{theorem}` environments where applicable
- Tables: `\begin{table}[t]` with `\caption` above, `\label{tab:X}`
- Figures: `\begin{figure}[t]` with `\caption` below, `\label{fig:X}`
- Citations: `\citet{author2024}` for narrative, `\citep{author2024}` for parenthetical

**`paper/main.tex` structure**:
```latex
\documentclass[...]{...}
% Preamble (venue-specific)
\usepackage{amsmath,amsthm,amssymb}
\usepackage{natbib}
\usepackage{graphicx}
\usepackage{booktabs}
% Custom commands
\newcommand{\...}{...}

\begin{document}
\title{...}
\author{[Author names — left blank for user]}

\input{sections/abstract}
\input{sections/introduction}
\input{sections/data}
\input{sections/methods}
\input{sections/results}
\input{sections/discussion}

\bibliographystyle{...}
\bibliography{references}

\appendix
\input{sections/appendix}
\end{document}
```

### 6.5 Compilation

```
Read and execute reference/sub-skills/paper-compiling.md
```

Compile LaTeX to PDF:
1. Pre-flight: verify all `\input` files exist, all figures referenced are present
2. Compile: `latexmk -pdf paper/main.tex`
3. If errors: diagnose, auto-fix (up to 3 attempts), recompile
4. Post-check: no `??` references, no missing figures, bibliography renders

Output: `paper/main.pdf` + `COMPILE_REPORT.md`

### 6.6 Update State

```json
{
  "stage": 6,
  "status": "completed",
  "latex_venue": "article",
  "pdf_pages": 14,
  "compile_status": "success",
  "compile_warnings": [],
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 6a | PAPER_PLAN.md exists | File created by paper-planning procedure | Regenerate from manuscript.md |
| 6b | PDF figures created | `paper/figures/*.pdf` for each figure | Fall back to PNG conversion |
| 6c | All .tex sections exist | One file per manuscript section | Regenerate missing section |
| 6d | main.tex compiles | PDF generated without errors | Auto-fix up to 3 times |
| 6e | No unresolved refs | No `??` in PDF | Fix `\ref` and `\cite` |
| 6f | Page count reasonable | Within venue target ± 3 pages | Note in log |
| 6g | Bibliography renders | All citations appear in references | Fix .bib entries |

---

## Next Step
→ Step 07: External Review via Codex MCP
