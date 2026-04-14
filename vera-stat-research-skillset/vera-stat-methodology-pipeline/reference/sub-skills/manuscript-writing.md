<!-- Absorbed from skills/paper-write/SKILL.md -->

# Paper Write: Statistics Manuscript in LaTeX

Generate a complete statistics paper from: **$ARGUMENTS**

## Constants

- **REVIEWER_MODEL = `gpt-5.4`**
- **TARGET_VENUE = `JASA`** — Default. Override via argument.

## Prerequisites

Read `PAPER_PLAN.md` for the outline. If it doesn't exist, read and execute `reference/sub-skills/paper-planning.md` first.

## Workflow

### Step 0: Setup LaTeX Project Structure

```
paper/
├── main.tex              # Master document
├── sections/
│   ├── abstract.tex
│   ├── introduction.tex
│   ├── setup.tex         # or background.tex
│   ├── method.tex        # or main_results.tex
│   ├── theory.tex        # theoretical properties (if applicable)
│   ├── simulations.tex
│   ├── application.tex
│   ├── discussion.tex
│   └── appendix.tex      # proofs and supplementary
├── figures/
│   └── *.pdf
├── tables/
│   └── *.tex
├── references.bib
└── style/                # venue-specific style files
```

### Step 1: Main Document Setup

Create `main.tex` with venue-appropriate preamble:

**JASA / JASA-ACS:**
```latex
\documentclass[12pt]{article}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{natbib}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage[margin=1in]{geometry}
\usepackage{setspace}\doublespacing

\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}{Definition}
\newtheorem{assumption}{Assumption}
\theoremstyle{remark}
\newtheorem{remark}{Remark}
```

**Annals of Statistics:**
```latex
\documentclass[ims-bjps]{imsart}
% Or use generic article class formatted to IMS style
```

**Biometrika:**
```latex
\documentclass[12pt]{article}
% Biometrika style: concise, single-spaced for submission
```

### Step 2: Section-by-Section Writing

Follow `PAPER_PLAN.md` section by section. For each section:

1. Read the plan's content specification
2. Read relevant source materials (results, proofs, notes)
3. Write the LaTeX, following statistics writing conventions

**Statistics Writing Conventions:**

- **Assumptions**: Number as (A1), (A2), ... State clearly and discuss necessity
  ```latex
  \begin{assumption}[Sub-Gaussian errors]\label{ass:subgaussian}
  The error terms $\varepsilon_i$ satisfy...
  \end{assumption}
  ```

- **Theorems**: State formally with all conditions. Include proof sketch in main body, full proof in appendix
  ```latex
  \begin{theorem}[Consistency]\label{thm:consistency}
  Under Assumptions \ref{ass:subgaussian}--\ref{ass:moment}, the estimator $\hat\theta_n$ satisfies
  $\hat\theta_n \xrightarrow{P} \theta_0$ as $n \to \infty$.
  \end{theorem}
  ```

- **Simulation tables**: Always include Monte Carlo standard errors
  ```latex
  \begin{table}[t]
  \caption{Empirical coverage of 95\% confidence intervals (Monte Carlo SE in parentheses).}
  \centering
  \begin{tabular}{lcccc}
  \toprule
  Method & $n=100$ & $n=500$ & $n=1000$ & $n=2000$ \\
  \midrule
  Proposed & 0.938 (0.005) & 0.948 (0.005) & 0.951 (0.005) & 0.949 (0.005) \\
  MLE & 0.942 (0.005) & 0.951 (0.005) & 0.950 (0.005) & 0.950 (0.005) \\
  \bottomrule
  \end{tabular}
  \end{table}
  ```

- **Notation**: Be consistent. Define all symbols in one place (Section 2 typically). Use `\newcommand` for repeated notation.

- **References**: Use `\citet` for "Smith (2024) showed..." and `\citep` for "...has been studied \citep{smith2024}"

### Step 3: Proofs and Appendix

For theory papers:

1. **Main body**: Include proof sketches for main theorems (key ideas, 1/2 to 1 page each)
2. **Appendix**: Full proofs with all technical details
3. **Supplementary material**: Additional lemmas, auxiliary results, extended simulations

Structure appendix clearly:
```latex
\appendix
\section{Proof of Theorem \ref{thm:consistency}}\label{app:proof-thm1}
\section{Proof of Theorem \ref{thm:normality}}\label{app:proof-thm2}
\section{Additional Simulation Results}\label{app:additional-sims}
\section{Technical Lemmas}\label{app:lemmas}
```

### Step 4: Bibliography

1. **Check for existing .bib file** in the project
2. **Build `references.bib`** from citations used in the paper
3. **Verify every citation**: correct authors, year, venue, title
4. **Flag uncertain citations** with a comment: `% [VERIFY] citation`
5. **Include classic references** — statistics reviewers expect proper attribution
6. **Filter**: only include cited references in the final .bib

### Step 5: De-AI Polish Pass

Search and fix AI writing patterns:

Remove/replace these words and patterns:
- "delve", "pivotal", "crucial", "landscape", "paradigm", "leverage" (as verb)
- "It is worth noting that" → delete or rephrase
- "In this paper, we" at the start of every paragraph → vary sentence structure
- Overly promotional language ("groundbreaking", "remarkable", "dramatically")
- Em dashes used excessively — replace some with commas or parentheses
- "Importantly," "Notably," "Interestingly," at sentence starts → remove or integrate

Statistics-specific style:
- Use "we" sparingly — prefer passive voice for methods ("the estimator is defined as") and active for claims ("we show that")
- Be precise: "consistent" means something specific in statistics — don't use it loosely
- Avoid "significant" unless referring to statistical significance
- Don't say "outperforms" without quantification

### Step 6: Cross-Review

Send the complete draft to REVIEWER_MODEL:

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    Review this statistics paper draft for [VENUE].
    [paste full LaTeX or key sections]

    Check:
    1. Are all theorems correctly stated with sufficient conditions?
    2. Is the simulation study design adequate?
    3. Is the writing clear and appropriate for [VENUE]?
    4. Are there any logical gaps or unsupported claims?
    5. Is notation consistent throughout?
    6. Are the most important related papers cited?
    7. Is the abstract self-contained and informative?

    Provide specific suggestions for improvement.
```

### Step 7: Reverse Outline Test

Read the completed draft and verify:
1. Each section's content matches `PAPER_PLAN.md`
2. Every claim in the abstract is supported in the body
3. Every theorem has a proof (main body or appendix)
4. Every entry in Claims-Evidence Matrix is covered
5. Notation is consistent (no symbol used for two things)
6. All figures and tables are referenced in the text
7. All `[VERIFY]` markers are resolved or flagged

### Step 8: Final Output

Ensure all files are written:
- `paper/main.tex` — master document with `\input{sections/...}`
- `paper/sections/*.tex` — one file per section
- `paper/references.bib` — verified bibliography
- `paper/figures/` — all figure files
- `paper/tables/` — all table files (if separate)

## Key Rules

- **Proofs must be correct** — do not write proofs you haven't verified. Mark uncertain steps with `% TODO: verify this step`
- **Assumptions must be stated** — every theorem needs explicit conditions
- **Monte Carlo SE in every simulation table** — non-negotiable for statistics venues
- **Notation consistency** — define once, use consistently
- **Proper citation style** — `\citet` vs `\citep`, journal-appropriate format
- **Don't overclaim** — use "suggests" instead of "proves" for empirical results
- **Abstract must be self-contained** — no citations, no undefined notation
- **Discussion section must include limitations** — reviewers respect honesty
