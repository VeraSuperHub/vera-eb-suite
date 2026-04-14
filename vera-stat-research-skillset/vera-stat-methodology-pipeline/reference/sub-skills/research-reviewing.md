<!-- Absorbed from skills/research-review/SKILL.md -->

# Statistics Research Review via Codex MCP (xhigh reasoning)

Get a multi-round critical review of statistics research work from an external LLM with maximum reasoning depth.

## Constants

- REVIEWER_MODEL = `gpt-5.4`

## Context: $ARGUMENTS

## Prerequisites

- **Codex MCP Server** configured in Claude Code:
  ```bash
  claude mcp add codex -s user -- codex mcp-server
  ```

## Workflow

### Step 1: Gather Research Context
Before calling the external reviewer, compile a comprehensive briefing:
1. Read project narrative documents (STORY.md, README.md, paper drafts, proof sketches)
2. Read simulation results, tables, figures
3. Identify: core claims, methodology, key theoretical results, simulation evidence, known weaknesses

### Step 2: Initial Review (Round 1)
Send a detailed prompt with xhigh reasoning:

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    [Full research context + specific questions]

    Please act as a senior statistics reviewer for a top journal (JASA, Annals of Statistics, JRSS-B, or Biometrika).

    Evaluate on these dimensions:

    **Theoretical Rigor:**
    - Are all regularity conditions explicitly stated?
    - Are proofs correct? Identify any gaps or errors.
    - Are asymptotic arguments valid (correct mode of convergence, proper application of CLT/delta method/contraction)?
    - Is the result sharp, or can the rate/bound be improved?

    **Methodological Contribution:**
    - Is the proposed estimator/test/procedure genuinely new?
    - How does it compare with existing approaches (efficiency, robustness, computational cost)?
    - Are there important special cases or extensions to discuss?

    **Simulation Study:**
    - Is the data-generating process realistic and well-motivated?
    - Are enough scenarios covered (sample sizes, dimensions, correlation structures, departures from assumptions)?
    - Are replications sufficient? (≥1000 for coverage, ≥5000 for size/power)
    - Is the comparison with existing methods fair (same tuning effort)?
    - Are Monte Carlo standard errors reported?

    **Real Data Analysis:**
    - Is the application well-motivated?
    - Does it demonstrate practical value beyond simulations?
    - Are results interpreted correctly and conservatively?

    **Presentation:**
    - Is notation consistent throughout?
    - Is the paper well-organized for the target venue?
    - Are assumptions cleanly separated from results?

    Be brutally honest. Identify the 3 most critical weaknesses.
```

### Step 3: Iterative Dialogue (Rounds 2-N)
Use `mcp__codex__codex-reply` with the returned `threadId`:

Key follow-up patterns for statistics:
- "If we weaken assumption X to Y, does the result still hold?"
- "What's the minimum simulation scenario needed to address concern Z?"
- "Is this result a special case of [known theorem]? If so, how to position it?"
- "Please check this proof sketch for Theorem 2: [paste proof]"
- "What competing estimator/test should we absolutely include in the comparison?"
- "Please write a mock JASA/Annals review with scores"
- "What additional regularity conditions are needed for this convergence result?"
- "Is the minimax rate for this problem known? Are we achieving it?"

### Step 4: Convergence
Stop iterating when:
- Both sides agree on the core claims and their evidence requirements
- Proof strategy is validated or counterexample identified
- Simulation study design is settled
- The theoretical contribution is clearly positioned

### Step 5: Document Everything
Save the full interaction and conclusions to a review document:
- Round-by-round summary of criticisms and responses
- Final consensus on claims, proofs, and simulations
- Claims matrix (what claims are supported under which assumptions)
- Prioritized TODO list with estimated effort
- Paper outline if discussed

## Key Rules

- ALWAYS use `config: {"model_reasoning_effort": "xhigh"}`
- Send comprehensive context in Round 1 — the external model cannot read your files
- Be honest about proof gaps — hiding them leads to worse feedback
- Push back on criticisms you disagree with, but accept valid ones
- Focus on ACTIONABLE feedback — "what specific simulation would fix this?"
- Statistics papers live or die on proof correctness — always request proof checking
- The review document should be self-contained

## Prompt Templates

### For proof checking:
"Please verify this proof of [theorem]. Here is the full proof: [paste]. Check: (1) are all steps justified? (2) are regularity conditions sufficient? (3) is the convergence mode correct? (4) are there any implicit assumptions?"

### For simulation design:
"Please design the minimal simulation study that would satisfy a JASA reviewer. Our method is [describe]. What DGPs, sample sizes, competing methods, and metrics should we include? Be specific about parameter choices."

### For positioning:
"How should we position this contribution relative to [list of related papers]? What is our unique angle? What should the abstract emphasize?"

### For mock review:
"Please write a mock JASA review with: Summary, Assessment of Novelty, Assessment of Theoretical Contribution, Assessment of Simulations, Assessment of Application, Minor Comments, Recommendation (Accept/Minor Revision/Major Revision/Reject), and What Would Move Toward Accept."
