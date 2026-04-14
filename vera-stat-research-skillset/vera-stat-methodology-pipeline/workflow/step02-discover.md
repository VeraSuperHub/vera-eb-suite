# Step 02: Idea Discovery

> **Executor**: Main Agent (invokes sub-skills)
> **Input**: `PIPELINE_STATE.json` (research direction, existing work)
> **Output**: `IDEA_DISCOVERY_REPORT.md` + Gate 1 decision

---

## Execution Instructions

### 2.1 Literature Survey

```
Read and execute reference/sub-skills/literature-reviewing.md with context: "{research_direction}"
```

Comprehensive literature search across:
- arXiv (stat.ME, stat.TH, stat.ML, math.ST)
- Google Scholar, Semantic Scholar
- Target statistics journals (JASA, Annals, JRSS-B, Biometrika, etc.)
- Local PDFs if available

Output: Literature landscape with key papers, open problems, thematic organization.

### 2.2 Idea Generation

```
Read and execute reference/sub-skills/idea-creating.md with context: "{research_direction}"
```

Systematic brainstorming:
1. Survey methodological landscape
2. LLM-assisted brainstorming (8-12 raw ideas)
3. First-pass filtering (feasibility, novelty signal, scope fit)
4. Validation of top 4-6 ideas
5. Pilot simulations for top 2-3 (limited: PILOT_REPLICATIONS=500, MAX_TOTAL_CPU_HOURS=4)

Output: `IDEA_REPORT.md` with ranked ideas + pilot results.

### 2.3 Novelty Verification

For the top 3 ideas, run:
```
Read and execute reference/sub-skills/novelty-checking.md
```

Multi-source search to verify each idea hasn't been published:
- Extract core claims from each idea
- Search across arXiv, Scholar, journals, conference proceedings
- Cross-verify with LLM
- Score novelty 1-10 per idea

### 2.4 External Critical Review

```
Read and execute reference/sub-skills/research-reviewing.md
```

Submit top ideas to external reviewer (Codex MCP) for pre-development assessment:
- Is the problem well-motivated?
- Is the proposed approach sound?
- Are there obvious pitfalls?
- How does it compare to recent work?

### 2.5 Compile Discovery Report

**Note on artifact names**: The `idea-creating` sub-skill writes `IDEA_REPORT.md`
(raw brainstorm + pilot results). This step enriches it with novelty scores and
reviewer feedback into `IDEA_DISCOVERY_REPORT.md`. Both files must exist at project
root — `paper-planning` downstream reads `IDEA_REPORT.md`, and this pipeline reads
`IDEA_DISCOVERY_REPORT.md` for Gate 1. Do NOT rename or overwrite `IDEA_REPORT.md`.

Assemble `IDEA_DISCOVERY_REPORT.md` (project root):

```markdown
# Idea Discovery Report

## Direction
{research_direction}

## Date
{timestamp}

## Literature Landscape
{thematic summary from literature-reviewing}

## Recommended Ideas (Post-Review)

### Idea 1: {Title}
- **Summary**: {one sentence}
- **Hypothesis**: {core conjecture}
- **Minimum viable validation**: {what to prove/simulate}
- **Novelty score**: X/10
- **Reviewer assessment**: {summary}
- **Risk level**: LOW/MEDIUM/HIGH
- **Estimated effort**: {days/weeks}
- **Pilot results**: {if available}

### Idea 2: ...
### Idea 3: ...

## Execution Plan
{concrete next steps per idea}
```

### 2.6 GATE 1: Idea Selection

Present top ideas to user:

```
Top ideas from discovery:

1. [Idea 1 title] — Novelty: X/10, Risk: LOW
   {one-line summary}

2. [Idea 2 title] — Novelty: X/10, Risk: MEDIUM
   {one-line summary}

3. [Idea 3 title] — Novelty: X/10, Risk: HIGH
   {one-line summary}

Which idea should we pursue? (default: #1 ranked)
```

**Decision logic**:
```
ALWAYS wait for user selection.
AUTO_PROCEED only applies to low-stakes confirmations (e.g., modality detection).
Gate 1 is a research-taste decision — it MUST NOT auto-proceed.
If no response after GATE1_TIMEOUT seconds, remind the user and keep waiting.
```

### 2.7 Update State

```json
{
  "stage": 2,
  "status": "completed",
  "ideas_generated": 10,
  "ideas_validated": 3,
  "selected_idea": {
    "title": "...",
    "summary": "...",
    "hypothesis": "...",
    "novelty_score": 8,
    "risk": "MEDIUM",
    "auto_selected": false
  },
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 2a | Literature survey completed | literature-reviewing produced output | Retry; proceed with limited context |
| 2b | Ideas generated | ≥ 3 validated ideas | Lower threshold; ask user for direction |
| 2c | Novelty checked | Top ideas have novelty scores | Proceed with caveat |
| 2d | Discovery report written | IDEA_DISCOVERY_REPORT.md exists | Compile from available outputs |
| 2e | Idea selected | selected_idea in state | Wait for user (override auto) |

---

## Next Step
→ Step 03: Implementation (parallel tracks)
