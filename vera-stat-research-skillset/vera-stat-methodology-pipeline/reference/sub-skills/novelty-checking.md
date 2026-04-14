<!-- Absorbed from skills/novelty-check/SKILL.md -->

# Novelty Check Skill (Statistics)

Check whether a proposed method/idea has already been done in the statistics literature: **$ARGUMENTS**

## Constants

- REVIEWER_MODEL = `gpt-5.4` — Model used via Codex MCP.

## Instructions

### Phase A: Extract Key Claims
1. Read the user's method description
2. Identify 3-5 core technical claims that would need to be novel:
   - What is the estimator / test / model / computational method?
   - What statistical problem does it solve?
   - What is the mechanism / key idea (e.g., new loss function, novel prior, projection technique)?
   - What theoretical property is claimed (rate, efficiency, minimax optimality)?
   - What makes it different from obvious existing approaches?

### Phase B: Multi-Source Literature Search
For EACH core claim, search using ALL available sources:

1. **Web Search** (via `WebSearch`):
   - Search arXiv (stat.ME, stat.TH, stat.ML, math.ST), Google Scholar, Semantic Scholar
   - Use specific technical terms from the claim
   - Try at least 3 different query formulations per claim
   - Include year filters for recent work (2023-2026) AND classic references
   - Search both the method name and the statistical property claimed

2. **Target journals and venues**:
   - JASA (both Theory & Methods and Applications & Case Studies)
   - Annals of Statistics, Annals of Applied Statistics
   - JRSS-B (Statistical Methodology), JRSS-A
   - Biometrika, Biometrics
   - Statistical Science, Bayesian Analysis
   - JCGS, Electronic Journal of Statistics, Bernoulli
   - Statistica Sinica, Scandinavian Journal of Statistics
   - AISTATS, UAI proceedings
   - Monographs and textbooks (Lehmann, van der Vaart, Wasserman, etc.)

3. **Read abstracts and key sections**: For each potentially overlapping paper, WebFetch its abstract, introduction, and main results

4. **Check classic references**: Statistics has a longer memory than ML. Check whether the idea appeared decades ago under different terminology (e.g., "kernel smoothing" vs "local polynomial regression", "empirical Bayes" vs "shrinkage estimation").

### Phase C: Cross-Model Verification
Call REVIEWER_MODEL via Codex MCP with xhigh reasoning:
```
config: {"model_reasoning_effort": "xhigh"}
prompt: |
  I need to verify the novelty of a proposed statistics method.

  Proposed method:
  [description]

  Papers found that may overlap:
  [list from Phase B]

  Please assess:
  1. Is this method novel? What is the closest prior work?
  2. Has the theoretical result been established before (possibly under different assumptions)?
  3. Is the contribution sufficiently distinct from existing work?
  4. Could this be considered a special case of a more general existing result?
  5. Are there classic (pre-2000) references that anticipated this idea?

  Be thorough — statistics has deep roots. An idea that seems new in the ML literature may be well-known in the statistics literature (and vice versa).
```

### Phase D: Novelty Report
Output a structured report:

```markdown
## Novelty Check Report

### Proposed Method
[1-2 sentence description]

### Core Claims
1. [Claim 1] — Novelty: HIGH/MEDIUM/LOW — Closest: [paper]
2. [Claim 2] — Novelty: HIGH/MEDIUM/LOW — Closest: [paper]
...

### Closest Prior Work
| Paper | Year | Venue | Overlap | Key Difference |
|-------|------|-------|---------|----------------|

### Classic References to Acknowledge
[Papers from before 2010 that contain related ideas — must be cited even if the contribution is distinct]

### Overall Novelty Assessment
- Score: X/10
- Recommendation: PROCEED / PROCEED WITH CAUTION / ABANDON
- Key differentiator: [what makes this unique, if anything]
- Risk: [what a reviewer would cite as prior work]

### Suggested Positioning
[How to frame the contribution to maximize novelty perception while honestly acknowledging related work]
```

### Important Rules
- Be BRUTALLY honest — false novelty claims waste months of research time
- "Apply method X to data type Y" is NOT novel unless it reveals new statistical phenomena or requires new theory
- Check BOTH the method AND the theoretical result for novelty separately
- If the method is not novel but the THEORETICAL ANALYSIS would be new, say so explicitly
- Statistics has a long history — always check classic references (Stein, Efron, Bickel, etc.)
- An idea published in the ML literature may have appeared in statistics decades earlier (and vice versa)
- Different notation can hide identical ideas — look past surface differences
