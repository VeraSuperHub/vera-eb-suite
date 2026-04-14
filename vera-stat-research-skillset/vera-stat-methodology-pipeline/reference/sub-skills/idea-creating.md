<!-- Absorbed from skills/idea-creator/SKILL.md -->

# Statistics Research Idea Creator

Generate publishable statistics research ideas for: $ARGUMENTS

## Overview

Given a broad research direction, systematically generate, validate, and rank concrete statistics research ideas. This skill composes with `reference/sub-skills/literature-reviewing.md`, `reference/sub-skills/novelty-checking.md`, and `reference/sub-skills/research-reviewing.md` to form a complete idea discovery pipeline.

## Constants

- **PILOT_MAX_MINUTES = 30** — Skip any pilot simulation estimated to take > 30 minutes. Flag as "needs full simulation".
- **PILOT_TIMEOUT_MINUTES = 45** — Hard timeout: kill pilots exceeding 45 minutes. Collect partial results if available.
- **MAX_PILOT_IDEAS = 3** — Pilot at most 3 ideas in parallel.
- **MAX_TOTAL_CPU_HOURS = 4** — Total CPU budget for all pilot simulations combined.
- **PILOT_REPLICATIONS = 500** — Quick pilot uses fewer replications than full study.
- **REVIEWER_MODEL = `gpt-5.4`** — Model used via Codex MCP for brainstorming and review.

> Override via argument, e.g., invoke idea-creating with context: "topic" — pilot budget: 2h total, 1000 reps.

## Workflow

### Phase 1: Landscape Survey (5-10 min)

Map the research area to understand what exists and where the gaps are.

1. **Scan local paper library first**: Check `papers/` and `literature/` in the project directory for existing PDFs. Read first 3 pages of relevant papers to build a baseline understanding.

2. **Search recent literature** using WebSearch:
   - Top statistics journals in the last 3 years: JASA, Annals of Statistics, JRSS-B, Biometrika, Statistical Science, Bayesian Analysis, JCGS, Electronic Journal of Statistics, Bernoulli
   - Methodology-focused venues: AISTATS, UAI, Journal of Machine Learning Research (statistical theory papers)
   - Recent arXiv stat.ME, stat.TH, stat.ML preprints (last 12 months)
   - Use 5+ different query formulations
   - Read abstracts and introductions of the top 10-15 papers

3. **Build a landscape map**:
   - Group papers by sub-direction / approach (e.g., frequentist vs. Bayesian, parametric vs. nonparametric)
   - Identify what has been tried and what hasn't
   - Note recurring limitations in "Discussion" and "Future Work" sections
   - Flag open problems explicitly stated by multiple papers
   - Note which asymptotic regimes have been studied (fixed-p, high-dimensional, functional)

4. **Identify structural gaps**:
   - Methods that work under condition A but haven't been extended to condition B
   - Estimators that lack theoretical guarantees (consistency, rates, efficiency)
   - Tests with unknown power properties under specific alternatives
   - Bayesian methods lacking frequentist calibration analysis (or vice versa)
   - Computational methods without convergence guarantees
   - Classical methods that haven't been adapted to modern data structures (high-dimensional, functional, network)
   - Missing connections between statistics and adjacent fields (causal inference, ML theory, information theory)

### Phase 2: Idea Generation (brainstorm with external LLM)

Use the external LLM via Codex MCP for divergent thinking:

```
mcp__codex__codex:
  model: REVIEWER_MODEL
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are a senior statistics researcher brainstorming research ideas.

    Research direction: [user's direction]

    Here is the current landscape:
    [paste landscape map from Phase 1]

    Key gaps identified:
    [paste gaps from Phase 1]

    Generate 8-12 concrete statistics research ideas. For each idea:
    1. One-sentence summary
    2. Core hypothesis or conjecture (what you expect to prove/show and why)
    3. Minimum viable validation:
       - For theory ideas: key lemma or proof sketch that would confirm feasibility
       - For methods ideas: small-scale simulation (n=100-500, 500 reps) showing the method works
       - For applied ideas: pilot analysis on a representative dataset
    4. Expected contribution type: new estimator / new test / theoretical result (rate, bound, efficiency) / computational method / new model / diagnostic tool
    5. Risk level: LOW (likely works) / MEDIUM (50-50) / HIGH (speculative)
    6. Estimated effort: weeks / months / semester

    Prioritize ideas that are:
    - Theoretically interesting AND practically useful
    - Testable with moderate computation (standard workstation, R/Python)
    - Likely to produce clean, interpretable results
    - Not "apply method X to dataset Y" unless the application reveals new statistical phenomena
    - Addressing genuine gaps, not incremental extensions

    Statistics-specific criteria:
    - Does the method have provable properties (consistency, asymptotic normality, optimality)?
    - Is there a clear comparison with existing estimators/tests?
    - Does the simulation study design allow fair evaluation?
    - Is there a compelling real data application?

    Be creative but rigorous. A great statistics idea solves a problem that practitioners face but theoreticians haven't addressed (or vice versa).
```

Save the threadId for follow-up.

### Phase 3: First-Pass Filtering

For each generated idea, quickly evaluate:

1. **Feasibility check**: Can we actually validate this with available resources?
   - Computational requirements (estimate CPU-hours for simulations)
   - Data availability for real data analysis
   - Mathematical complexity (can the key proof be outlined in a few pages?)
   - Skip ideas requiring massive computation or unavailable datasets

2. **Novelty quick-check**: For each idea, do 2-3 targeted searches to see if it's already been done. Full novelty-checking comes later.

3. **Impact estimation**: Would a statistics reviewer care?
   - "So what?" test: if the theorem is proved / simulation succeeds, does it change practice or understanding?
   - Does it connect to active areas (high-dimensional inference, causal inference, Bayesian computation, distribution-free methods)?
   - Is the result likely to be cited?

Eliminate ideas that fail any of these. Typically 8-12 ideas reduce to 4-6.

### Phase 4: Deep Validation (for top ideas)

For each surviving idea:

1. **Novelty check**: Read and execute `reference/sub-skills/novelty-checking.md` (multi-source search + cross-verification)

2. **Critical review**: Use GPT-5.4 via `mcp__codex__codex-reply` (same thread):
   ```
   Here are our top ideas after filtering:
   [paste surviving ideas with novelty check results]

   For each, play devil's advocate as a senior statistics reviewer:
   - What's the strongest theoretical objection?
   - Is the proof strategy likely to work, or is there a fundamental obstacle?
   - What competing method would a referee demand comparison with?
   - What's the most likely failure mode in simulations?
   - How would you rank these for JASA / Annals of Statistics?
   - Which 2-3 would you actually work on?
   ```

3. **Combine rankings**: Merge assessments. Select top 2-3 for pilot validation.

### Phase 5: Pilot Simulations (for top 2-3 ideas)

Run quick pilot simulations to get empirical signal before committing.

1. **Design pilots**: For each top idea, define the minimal simulation:
   - **For new estimators**: Compare bias and MSE against 1-2 existing estimators at n=100,500. Use PILOT_REPLICATIONS reps.
   - **For new tests**: Check size (Type I error at nominal 5%) and power against 2-3 alternatives at n=100,500.
   - **For theoretical results**: Verify the predicted rate/bound matches simulation. Plot log-log convergence.
   - **For Bayesian methods**: Run short MCMC (1000 iterations) to check mixing and basic posterior behavior.
   - Clear success metric defined upfront (e.g., "if coverage is within 1% of nominal at n=500, signal is positive")

2. **Deploy pilots**: Write R or Python scripts and run them:
   ```r
   # Pilot simulation template
   set.seed(42)
   n_vec <- c(100, 500)
   B <- 500  # pilot replications
   results <- expand.grid(n = n_vec, method = c("proposed", "competitor"))
   # ... run simulation ...
   ```
   Use `run_in_background: true` to launch pilots in parallel.

3. **Collect results**: Check for completion and compare:
   - Which ideas showed positive signal (method works as expected)?
   - Which showed problems (poor coverage, inflated size, slow convergence)?
   - Any surprising findings suggesting a pivot?
   - Total CPU time consumed (track against MAX_TOTAL_CPU_HOURS)

4. **Re-rank based on empirical evidence**: Update ranking using pilot results.

Note: Skip this phase for purely theoretical ideas. Flag as "needs pilot validation" in the report.

### Phase 6: Output — Ranked Idea Report

Write a structured report to `IDEA_REPORT.md`:

```markdown
# Statistics Research Idea Report

**Direction**: [user's research direction]
**Generated**: [date]
**Ideas evaluated**: X generated → Y survived filtering → Z piloted → W recommended

## Landscape Summary
[3-5 paragraphs on the current state of the field, organized by approach/school]

## Recommended Ideas (ranked)

### Idea 1: [title]
- **Hypothesis/Conjecture**: [one sentence]
- **Minimum validation**: [concrete description — what simulation or proof step]
- **Expected outcome**: [what success/failure looks like]
- **Novelty**: X/10 — closest work: [paper]
- **Feasibility**: [computational cost, mathematical difficulty, data needs]
- **Risk**: LOW/MEDIUM/HIGH
- **Contribution type**: estimator / test / theory / computation / model
- **Pilot result**: [POSITIVE: coverage 94.8% at n=500 / NEGATIVE: size inflated to 12% / SKIPPED]
- **Theoretical properties to prove**: [consistency, rate, efficiency, minimax optimality]
- **Reviewer's likely objection**: [strongest counterargument]
- **Target venue**: [JASA / Annals / JRSS-B / Biometrika / other]
- **Why we should do this**: [1-2 sentences]

### Idea 2: [title]
...

## Eliminated Ideas (for reference)
| Idea | Reason eliminated |
|------|-------------------|
| ... | Already done by [paper] |
| ... | Proof strategy appears blocked by [technical obstacle] |
| ... | Result would be incremental over [existing paper] |

## Pilot Simulation Results
| Idea | Metric | n=100 | n=500 | Signal |
|------|--------|-------|-------|--------|
| Idea 1 | Coverage (95% nominal) | 93.2% | 94.8% | POSITIVE |
| Idea 2 | Size (5% nominal) | 8.1% | 6.2% | WEAK — size inflation |
| Idea 3 | MSE ratio vs competitor | 0.72 | 0.65 | POSITIVE — 28-35% efficiency gain |

## Suggested Execution Order
1. Start with Idea 1 (positive pilot, clean theoretical story)
2. Idea 3 as backup (positive pilot, needs more simulation scenarios)
3. Idea 2 deprioritized — size inflation needs investigation

## Next Steps
- [ ] Full simulation study for Idea 1 (n=100,200,500,1000,2000, B=2000+)
- [ ] Prove key theoretical results (consistency, asymptotic distribution)
- [ ] Identify compelling real data application
- [ ] If confirmed, read and execute reference/sub-skills/review-looping.md for full iteration
```

## Key Rules

- The user provides a DIRECTION, not an idea. Your job is to generate the ideas.
- Quantity first, quality second: brainstorm broadly, then filter ruthlessly.
- A clean negative result (proving a method DOESN'T have a property everyone assumed) is publishable.
- Don't fall in love with any idea before validating it.
- Always estimate computational cost for the full simulation study, not just the pilot.
- "Apply X to Y" is the lowest form of research idea unless it reveals surprising statistical phenomena.
- Include eliminated ideas in the report — they save future time.
- **If the user's direction is too broad (e.g., "Bayesian statistics", "nonparametric methods"), STOP and ask them to narrow it.** A good direction is specific — e.g., "robust estimation in high-dimensional linear models with heavy-tailed errors" or "conformal prediction with dependent data".

## Composing with Other Skills

```
reference/sub-skills/idea-creating.md "direction"     → ranked ideas
reference/sub-skills/novelty-checking.md "top idea"   → deep novelty verification
reference/sub-skills/research-reviewing.md "top idea" → external critical feedback
implement                                             → write R/Python code + proofs
reference/sub-skills/experiment-running.md             → deploy simulations
reference/sub-skills/review-looping.md                 → iterate until submission-ready
reference/sub-skills/paper-writing.md                  → write the paper
```
