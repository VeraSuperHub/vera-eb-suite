<!-- Absorbed from skills/idea-discovery/SKILL.md -->

# Idea Discovery: Statistics Research Pipeline (Workflow 1)

Full idea discovery pipeline for: **$ARGUMENTS**

## Constants

- AUTO_PROCEED = true — Automatically proceed between phases (set false for manual checkpoints)

## Pipeline

### Phase 1: Literature Survey
```
Read and execute reference/sub-skills/literature-reviewing.md with context: "$ARGUMENTS"
```
Output: structured literature review with gaps identified.

**Checkpoint**: If AUTO_PROCEED is false, present the literature review and ask whether to continue.

### Phase 2: Idea Generation
```
Read and execute reference/sub-skills/idea-creating.md with context: "$ARGUMENTS"
```
Input: literature review from Phase 1.
Output: ranked idea report with pilot results (if simulations were run).

**Checkpoint**: Present ranked ideas. If AUTO_PROCEED is false, ask which ideas to validate further.

### Phase 3: Deep Novelty Verification
For the top 2-3 ideas from Phase 2:
```
Read and execute reference/sub-skills/novelty-checking.md with context: "[idea description]"
```
Output: novelty report for each top idea.

**Checkpoint**: If any idea has low novelty, flag it and suggest pivots.

### Phase 4: External Critical Review
```
Read and execute reference/sub-skills/research-reviewing.md with context: "$ARGUMENTS — focusing on top ideas from idea report"
```
Output: multi-round review with actionable feedback.

### Phase 5: Final Summary

Compile everything into a final `IDEA_DISCOVERY_REPORT.md`:

```markdown
# Idea Discovery Report

**Direction**: [research direction]
**Date**: [today]
**Pipeline**: research-lit → idea-creator → novelty-check → research-review

## Literature Landscape
[Summary from Phase 1]

## Recommended Ideas (post-review)
1. [Idea 1]: Novelty X/10, Reviewer assessment: [summary]
2. [Idea 2]: Novelty X/10, Reviewer assessment: [summary]

## Execution Plan
- Idea 1: [concrete next steps — what to prove, what to simulate, what data to analyze]
- Idea 2: [concrete next steps]

## Next Steps
- [ ] Implement the chosen idea (write R/Python code + proofs)
- [ ] Run full simulation study: read and execute reference/sub-skills/experiment-running.md
- [ ] Iterate with review: read and execute reference/sub-skills/review-looping.md
- [ ] Write the paper: read and execute reference/sub-skills/paper-writing.md
```

## Key Rules

- This is a DISCOVERY pipeline — the goal is to find the best idea, not to implement it
- Each phase builds on the previous one — don't skip phases
- Be honest about novelty — better to abandon a non-novel idea early
- The final report should give the user everything they need to start implementation
- Total pipeline time: 30-60 minutes depending on pilot simulations
