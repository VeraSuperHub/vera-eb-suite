<!-- Absorbed from skills/research-lit/SKILL.md -->

# Statistics Literature Review

Search and review statistics literature on: **$ARGUMENTS**

## Source Priority

Search sources in this order, using all that are available:

### Source 1: Zotero (if MCP available)
- Check for `mcp__zotero__*` tools
- Search user's personal library first — they may already have relevant papers organized
- If available, search by tags, collections, and full text

### Source 2: Obsidian (if MCP available)
- Check for `mcp__obsidian__*` tools
- Search user's research notes for prior reading and summaries

### Source 3: Local PDFs
- Search `papers/`, `literature/`, `references/`, `pdfs/` directories
- Read first 3 pages of up to 20 relevant PDFs
- Extract: title, authors, year, key results, methodology

### Source 4: Web Search
Search across multiple databases:

1. **arXiv** (stat.ME, stat.TH, stat.ML, math.ST):
   - Recent preprints (last 12-24 months)
   - Use specific statistical terminology

2. **Google Scholar**:
   - Broad search with year filters
   - Check citation counts for influence assessment

3. **Semantic Scholar**:
   - API search for related papers
   - Check "influential citations" metric

4. **Target Statistics Journals**:
   - JASA (Theory & Methods, Applications & Case Studies)
   - Annals of Statistics, Annals of Applied Statistics
   - JRSS-B, JRSS-A
   - Biometrika, Biometrics
   - Statistical Science, Bayesian Analysis
   - JCGS, Electronic Journal of Statistics
   - Bernoulli, Statistica Sinica
   - Scandinavian Journal of Statistics

5. **Adjacent venues** (when relevant):
   - JMLR (statistical theory papers)
   - AISTATS, UAI
   - Biostatistics, Statistics in Medicine
   - Annals of Applied Probability
   - Journal of Econometrics (for causal inference, time series)

6. **Classic references**:
   - Statistics has a long memory — search for foundational work
   - Check textbooks: van der Vaart, Lehmann & Casella, Wasserman, etc.
   - Don't ignore pre-2000 work

### Source Behavior
- Try each source in order; gracefully skip unavailable sources
- Override with argument: invoke literature-reviewing with context: "topic" — sources: web only
- Always search at least 2 sources

## Query Strategy

For each topic, generate at least 5 query formulations:
1. Technical/precise: exact method name + statistical property
2. Broad/conceptual: problem class + approach type
3. Application-oriented: domain + statistical method
4. Alternative terminology: different names for the same concept (statistics has many!)
5. Related but distinct: adjacent methods that should be compared

**Important**: Statistics terminology varies across traditions:
- Frequentist vs. Bayesian names for the same quantity
- Older vs. modern terminology (e.g., "variance stabilization" vs. "normalizing transformation")
- Statistics vs. ML terminology (e.g., "regularization" vs. "penalization", "features" vs. "covariates")
- Different subfields' jargon (biostatistics vs. econometrics vs. survey sampling)

## Output Format

```markdown
# Literature Review: [topic]
**Date**: [today]
**Sources searched**: [list]
**Queries used**: [list]

## Summary
[2-3 paragraph overview of the field and current state]

## Key Papers

| # | Title | Authors | Year | Venue | Relevance | Key Contribution |
|---|-------|---------|------|-------|-----------|------------------|
| 1 | ... | ... | ... | JASA | HIGH | Introduced [method] |
| 2 | ... | ... | ... | Annals | HIGH | Proved [rate] |
| ... |

## Thematic Organization

### Theme 1: [approach/subarea]
- [Paper A] did X, [Paper B] extended to Y, [Paper C] showed Z
- Current state: [summary]
- Gap: [what's missing]

### Theme 2: [approach/subarea]
...

## Open Problems
1. [Explicitly stated open problems from the literature]
2. [Gaps identified from the survey]

## Classic References (pre-2010)
[Important foundational work that must be cited]

## Notes
- [Deduplication notes: papers found in multiple sources]
- [Source attribution: where each paper was found]
```

## Key Rules

- Deduplicate across sources (same paper may appear in multiple searches)
- Always note the source where each paper was found
- Read abstracts and introductions, not just titles
- Statistics literature extends back decades — don't ignore classic work
- Note the distinction between journal versions and arXiv preprints
- Flag any papers you're uncertain about with `[VERIFY]`
- Organize thematically, not chronologically
- Always identify gaps — this feeds into idea generation
