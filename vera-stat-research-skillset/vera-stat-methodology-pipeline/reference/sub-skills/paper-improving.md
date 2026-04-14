<!-- Absorbed from skills/auto-paper-improvement-loop/SKILL.md -->

# Auto Paper Improvement Loop: Statistics Manuscript Polish

Autonomously improve a statistics paper through review-fix-recompile cycles.

## Context: $ARGUMENTS

## Constants

- MAX_ROUNDS = 2 (diminishing returns beyond 2 for prose polish)
- REVIEWER_MODEL = `gpt-5.4`

## State Persistence

Persist state to `PAPER_IMPROVEMENT_STATE.json` after each round:
```json
{
  "round": 1,
  "threadId": "...",
  "status": "in_progress",
  "last_score": 5.5,
  "timestamp": "2026-03-14T10:00:00"
}
```

## Workflow

### Initialization

1. Check for `PAPER_IMPROVEMENT_STATE.json` (same logic as auto-review-loop)
2. Read the current paper (all .tex sections)
3. Read `PAPER_PLAN.md` for the intended structure
4. Compile current version: Read and execute `reference/sub-skills/paper-compiling.md` → save as `round0_original.pdf`

### Loop (up to MAX_ROUNDS)

#### Phase A: Review Writing Quality

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    Review this statistics paper for writing quality (not research content).
    Target venue: [VENUE]

    [paste full paper text]

    Score 1-10 and evaluate:
    1. **Clarity**: Is the writing clear and precise?
    2. **Notation consistency**: Are symbols used consistently?
    3. **Theorem presentation**: Are theorems well-stated with clear conditions?
    4. **Simulation reporting**: Are tables/figures informative and well-formatted?
    5. **Flow**: Does the paper read naturally from section to section?
    6. **Abstract quality**: Self-contained, informative, appropriate length?
    7. **AI artifacts**: Any telltale AI-generated language patterns?
    8. **Statistical precision**: Is statistical language used correctly?

    For each issue found, provide the EXACT location and specific fix.
    Prioritize fixes by impact on acceptance probability.
```

#### Phase B: Implement Fixes (priority order)

1. **Proof/theory fixes**: Correct any mathematical errors or unclear statements
2. **Notation fixes**: Ensure consistency throughout
3. **Claim adjustments**: Soften overclaims, strengthen undersold results
4. **Simulation table improvements**: Add MC SEs, improve formatting
5. **Flow and transitions**: Improve paragraph and section connections
6. **De-AI polish**: Remove AI writing artifacts
7. **Abstract and conclusion**: Ensure they match the paper's actual content

#### Phase C: Recompile and Verify

1. Read and execute `reference/sub-skills/paper-compiling.md`
2. Save as `roundN.pdf`
3. Verify no compilation errors introduced
4. Check page count still within limits

#### Phase D: Document Round

Update `PAPER_IMPROVEMENT_STATE.json` and log changes.

### Termination

After MAX_ROUNDS:
1. Set `"status": "completed"` in state file
2. Report score progression (e.g., "Round 0: 5/10 → Round 1: 7/10 → Round 2: 7.5/10")
3. List any remaining issues not addressed
4. Final PDF saved with round number

## Key Rules

- Focus on WRITING quality, not research direction changes
- Don't change research content or claims — only how they're presented
- Preserve all mathematical notation exactly (don't "simplify" proofs)
- 2 rounds maximum — stop even if not perfect
- Save PDF versions for comparison between rounds
- Track what changed in each round for the author's review
