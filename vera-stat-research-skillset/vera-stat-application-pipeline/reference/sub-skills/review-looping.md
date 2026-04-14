<!-- Absorbed from skills/auto-review-loop/SKILL.md -->

# Auto Review Loop: Autonomous Statistics Research Improvement

Autonomously iterate: review → implement fixes → re-review, until the external reviewer gives a positive assessment or MAX_ROUNDS is reached.

## Context: $ARGUMENTS

## Constants

- MAX_ROUNDS = 4
- POSITIVE_THRESHOLD: score >= 6/10, or verdict contains "accept", "sufficient", "ready for submission"
- REVIEW_DOC: `AUTO_REVIEW.md` in project root (cumulative log)
- REVIEWER_MODEL = `gpt-5.4` — Model used via Codex MCP. Must be an OpenAI model (e.g., `gpt-5.4`, `o3`, `gpt-4o`)

## State Persistence (Compact Recovery)

Long-running loops may hit the context window limit, triggering automatic compaction. To survive this, persist state to `REVIEW_STATE.json` after each round:

```json
{
  "round": 2,
  "threadId": "019cd392-...",
  "status": "in_progress",
  "last_score": 5.0,
  "last_verdict": "not ready",
  "pending_simulations": ["sim_coverage_n500", "mcmc_convergence"],
  "timestamp": "2026-03-13T21:00:00"
}
```

**Write this file at the end of every Phase E**. Overwrite each time — only the latest state matters.

**On completion** (positive assessment or max rounds), set `"status": "completed"`.

## Workflow

### Initialization

1. **Check for `REVIEW_STATE.json`** in project root:
   - If it does not exist: **fresh start**
   - If it exists AND `status` is `"completed"`: **fresh start**
   - If it exists AND `status` is `"in_progress"` AND `timestamp` is older than 24 hours: **fresh start** (stale state)
   - If it exists AND `status` is `"in_progress"` AND `timestamp` is within 24 hours: **resume**
     - Read the state file to recover `round`, `threadId`, `last_score`, `pending_simulations`
     - Read `AUTO_REVIEW.md` to restore full context of prior rounds
     - Resume from the next round (round = saved round + 1)
     - Log: "Recovered from context compaction. Resuming at Round N."
2. Read project narrative documents, memory files, and any prior review documents
3. Read recent simulation results (check output directories, logs, R/Python output)
4. Identify current weaknesses and open TODOs from prior reviews
5. Initialize round counter = 1 (unless recovered from state file)
6. Create/update `AUTO_REVIEW.md` with header and timestamp

### Loop (repeat up to MAX_ROUNDS)

#### Phase A: Review

Send comprehensive context to the external reviewer:

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    [Round N/MAX_ROUNDS of autonomous review loop]

    [Full research context: theoretical claims, methodology, simulation results, real data analysis, known weaknesses]
    [Changes since last round, if any]

    Please act as a senior statistics reviewer (JASA / Annals of Statistics / Biometrika / JRSS-B level).

    Evaluate this work on the following dimensions:
    1. **Theoretical rigor**: Are regularity conditions clearly stated? Are proofs correct and complete? Are asymptotic arguments valid?
    2. **Methodological contribution**: Is the proposed estimator/test/model genuinely new? How does it compare to existing approaches?
    3. **Simulation study design**: Is the data-generating process realistic? Are enough scenarios covered (sample sizes, dimensions, violation of assumptions)? Are replications sufficient (≥1000 for coverage, ≥5000 for size/power)?
    4. **Real data analysis**: Is the application meaningful and well-motivated? Are results interpreted correctly?
    5. **Presentation and clarity**: Is notation consistent? Are assumptions clearly separated from results?

    Score this work 1-10 for a top statistics venue.
    List remaining critical weaknesses (ranked by severity).
    For each weakness, specify the MINIMUM fix (additional simulation, proof correction, reframing, or new analysis).
    State clearly: is this READY for submission? Yes/No/Almost.

    Be brutally honest. If the work is ready, say so clearly.
```

If this is round 2+, use `mcp__codex__codex-reply` with the saved threadId.

#### Phase B: Parse Assessment

**CRITICAL: Save the FULL raw response** from the external reviewer verbatim. Do NOT discard or summarize.

Extract structured fields:
- **Score** (numeric 1-10)
- **Verdict** ("ready" / "almost" / "not ready")
- **Action items** (ranked list of fixes)

**STOP CONDITION**: If score >= 6 AND verdict contains "ready" or "almost" → stop loop, document final state.

#### Phase C: Implement Fixes (if not stopping)

For each action item (highest priority first):

1. **Proof corrections**: Fix theoretical arguments, add missing regularity conditions, strengthen asymptotic results
2. **Simulation additions**: Write/modify R or Python simulation scripts
   - Coverage probability studies (nominal vs. empirical coverage)
   - Size and power comparisons across sample sizes
   - Robustness checks under model misspecification
   - Convergence rate verification
3. **MCMC diagnostics**: If Bayesian — trace plots, ESS, Gelman-Rubin, posterior predictive checks
4. **Real data re-analysis**: Additional sensitivity analyses, alternative model specifications
5. **Presentation fixes**: Notation consistency, theorem statement clarity, proof reorganization
6. **Documentation**: Update project notes and review document

Prioritization rules:
- Skip simulations requiring > 24 hours of compute — flag for manual follow-up
- Prefer analytical fixes (tighter bounds, cleaner proofs) over additional simulations when both address the concern
- Always add requested comparison methods (cheap, high impact)
- Always fix identified proof errors immediately

#### Phase D: Wait for Results

If simulations were launched:
- Monitor R/Python processes for completion
- Collect results from output files (.rds, .csv, .json)

#### Phase E: Document Round

Append to `AUTO_REVIEW.md`:

```markdown
## Round N (timestamp)

### Assessment (Summary)
- Score: X/10
- Verdict: [ready/almost/not ready]
- Key criticisms: [bullet list]

### Reviewer Raw Response

<details>
<summary>Click to expand full reviewer response</summary>

[Paste the COMPLETE raw response from the external reviewer here — verbatim, unedited.]

</details>

### Actions Taken
- [what was implemented/changed — proof fixes, new simulations, etc.]

### Results
- [simulation outcomes, coverage tables, power curves, etc.]

### Status
- [continuing to round N+1 / stopping]
```

**Write `REVIEW_STATE.json`** with current round, threadId, score, verdict, and any pending simulations.

Increment round counter → back to Phase A.

### Termination

When loop ends (positive assessment or max rounds):

1. Update `REVIEW_STATE.json` with `"status": "completed"`
2. Write final summary to `AUTO_REVIEW.md`
3. Update project notes with conclusions
4. If stopped at max rounds without positive assessment:
   - List remaining blockers
   - Estimate effort needed for each
   - Suggest whether to continue manually or pivot

## Key Rules

- ALWAYS use `config: {"model_reasoning_effort": "xhigh"}` for maximum reasoning depth
- Save threadId from first call, use `mcp__codex__codex-reply` for subsequent rounds
- Be honest — include negative results and failed simulations
- Do NOT hide weaknesses to game a positive score
- Implement fixes BEFORE re-reviewing (don't just promise to fix)
- For simulations taking > 30 minutes, launch them and continue with proof/writing fixes while waiting
- Document EVERYTHING — the review log should be self-contained
- Statistics-specific: always report Monte Carlo standard errors alongside simulation results

## Prompt Template for Round 2+

```
mcp__codex__codex-reply:
  threadId: [saved from round 1]
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    [Round N update]

    Since your last review, we have:
    1. [Action 1]: [result — e.g., "Added coverage simulation at n=100,500,1000: empirical coverage 94.2%, 94.8%, 95.1% for nominal 95%"]
    2. [Action 2]: [result — e.g., "Fixed proof of Theorem 2: added bounded fourth moment condition"]
    3. [Action 3]: [result — e.g., "Added power comparison with competing method X"]

    Updated simulation results:
    [paste tables]

    Please re-score and re-assess. Are the remaining concerns addressed?
    Same format: Score, Verdict, Remaining Weaknesses, Minimum Fixes.
```
