# Step 05: Manuscript Assembly

> **Executor**: Main Agent
> **Input**: All `output/` artifacts from Step 04 + `PIPELINE_STATE.json`
> **Output**: `output/manuscript.md`

---

## Execution Instructions

Read `reference/manuscript-template.md` for the exact Markdown structure.
Read `reference/assembly-rules.md` for stitching, numbering, and cross-referencing rules.

### 5.1 Pre-Assembly Inventory

Verify all required inputs exist:

| File | Source | Required |
|------|--------|----------|
| `output/methods.md` | Step 04 (merged) | Yes |
| `output/results.md` | Step 04 (merged) | Yes |
| `output/literature_review.md` | Step 04 Stream A | Yes |
| `output/analysis_strategy.md` | Step 03 | Yes |
| `output/tables/` | Step 04 (merged) | Yes |
| `output/figures/` | Step 04 (merged) | Yes |
| `output/references.bib` | Step 04 (merged) | Yes |
| `PIPELINE_STATE.json` | Steps 01-04 | Yes |

If any required file is missing, check `output/track_outputs/` for raw track outputs and attempt to recover.

### 5.2 Section Assembly

Assemble `output/manuscript.md` in this order. Write sections 1-5 first, then write the Abstract last.

#### Section 1: Introduction

Generate NEW content (do not copy from literature_review.md verbatim). Structure:

**Paragraph 1 — Context & Significance**:
- What is the broad area? Why does it matter?
- Draw from `output/literature_review.md` background section

**Paragraph 2 — What Is Known**:
- Summarize existing findings from literature review
- Cite key prior studies

**Paragraph 3 — Gap & Motivation**:
- What remains unknown or under-explored?
- Draw from lit scan gaps + analysis strategy rationale
- Why do existing analyses fall short?

**Paragraph 4 — This Study**:
- "In this study, we..." — state the objective
- Briefly mention the analytical approach (informed by literature)
- State the hypothesis if applicable

**Paragraph 5 — Contribution / Outline** (optional):
- What this study adds beyond prior work
- Brief roadmap of the paper

**Rules**:
- 3-5 paragraphs total, ~600-1000 words
- Cite 8-12 references (from literature_review.md)
- End with a clear statement of what THIS study does
- Do NOT describe methods in detail (save for Methods section)

#### Section 2: Data & Study Design

Generate from PIPELINE_STATE.json metadata:

**2.1 Data Source**:
- Where the data comes from (describe dataset)
- Study design (cross-sectional, cohort, RCT, etc.) — infer from data structure or ask in Step 01
- Time period, setting, population

**2.2 Variables**:
- Outcome: name, measurement, units
- Predictors: name, type, measurement
- Covariates: name, rationale for inclusion
- Subgroup variable (if applicable)

**2.3 Sample Characteristics**:
- N (after exclusions)
- Missing data handling approach
- Descriptive statistics table (Table 1): demographics, outcome distribution, predictor distributions

**Generate Table 1** if not already in `output/tables/`:
```
Table 1: Sample Characteristics
| Variable | Overall (N=X) | [Group 1] (n=Y) | [Group 2] (n=Z) |
|----------|---------------|------------------|------------------|
| Age, mean (SD) | ... | ... | ... |
| Female, n (%) | ... | ... | ... |
| [Outcome], median (IQR) | ... | ... | ... |
```

#### Section 3: Statistical Methods

Insert `output/methods.md` content.

Adjust ordering based on outcome family:

**Standard outcome types** (continuous, binary, ordinal, nominal, count, survival, repeated, timeseries, multivariate, doe, meta):
1. Descriptive statistics approach
2. Primary hypothesis tests
3. Regression modeling
4. Alternative methods (QR, trees, etc.)
5. Subgroup / interaction analysis
6. Model comparison approach
7. Software and packages

**SEM families** (sem-cfa, sem-full, sem-longchange):
1. Measurement model specification
2. Model fit evaluation
3. Reliability and validity (CFA) / structural paths (full SEM) / growth trajectories (longchange)
4. Model comparison and alternative specifications
5. Invariance testing (if applicable)
6. Software and packages

If methods.md uses a different ordering, re-sequence to match the appropriate family flow.
Do NOT alter statistical content — only reorder sections.

#### Section 4: Results

Insert `output/results.md` content.

Ensure results ordering matches methods ordering from Section 3.
Insert table and figure references at appropriate points:
- "Table N shows..." or "(Table N)"
- "Figure N displays..." or "(Figure N)"

Renumber all tables and figures sequentially starting from Table 1 / Figure 1.
Table 1 (sample characteristics) is in Section 2; results tables start from Table 2.

#### Section 5: Discussion

Generate NEW content. Read `reference/discussion-patterns.md` for structure.

**Paragraph 1 — Key Findings Summary**:
- Restate main results in plain language (no p-values)
- Connect back to the research question

**Paragraph 2-3 — Comparison with Prior Work**:
- Compare findings with key studies from literature review
- Where do our results agree/disagree?
- Why might differences exist?

**Paragraph 4 — Methodological Strengths**:
- Multi-method approach (what each method contributed)
- Cross-method convergence (from synthesis)
- What our analytical strategy reveals beyond standard approaches

**Paragraph 5 — Limitations**:
- Sample size / power considerations
- Data limitations (missing data, measurement error, unmeasured confounders)
- Generalizability
- Tree-based results are exploratory (if small N)

**Paragraph 6 — Implications & Future Directions**:
- Practical implications of findings
- Recommendations for future research
- What should the next study do differently?

**Rules**:
- 5-7 paragraphs, ~800-1200 words
- Cite literature (from literature_review.md references)
- Do NOT introduce new results
- Do NOT overstate findings ("associated with" not "caused")
- Acknowledge what the study cannot answer

#### Abstract (Write Last)

After all sections complete, write the abstract:

**Structure** (150-250 words):
- **Background**: 1-2 sentences (context + gap)
- **Objective**: 1 sentence (what this study does)
- **Methods**: 2-3 sentences (data, design, key methods)
- **Results**: 3-4 sentences (main findings with key numbers)
- **Conclusions**: 1-2 sentences (implications)

**Rules**:
- No citations in abstract
- Include specific numbers (N, effect size, CI, p)
- No abbreviations unless universally known
- Must stand alone — reader should understand the study from abstract only

#### References

Append the full `output/references.bib` at the end.
Verify every citation in the text has an entry in references.
Verify no orphan references (in bib but not cited).

### 5.3 Final Manuscript Structure

```markdown
# [Title]

## Abstract
[150-250 words]

## 1. Introduction
[3-5 paragraphs, ~600-1000 words]

## 2. Data and Study Design
### 2.1 Data Source
### 2.2 Variables
### 2.3 Sample Characteristics

## 3. Statistical Methods
[From methods.md, reordered]

## 4. Results
[From results.md, with table/figure references]

## 5. Discussion
[5-7 paragraphs, ~800-1200 words]

## References
[From references.bib]

## Tables
[All tables, numbered sequentially]

## Figures
[All figure captions; actual PNGs in output/figures/]
```

### 5.4 Update State

```json
{
  "stage": 5,
  "status": "completed",
  "manuscript_word_count": 4500,
  "n_tables": 5,
  "n_figures": 8,
  "n_references": 28,
  "timestamp": "..."
}
```

---

## Validation Checkpoints

| ID | Check Item | Pass Criteria | Failure Handling |
|----|------------|---------------|------------------|
| 5a | All 5 sections present | Introduction through Discussion exist | Generate missing section |
| 5b | Abstract present | 150-250 words, no citations | Regenerate |
| 5c | Table numbering sequential | Table 1, 2, 3... no gaps | Renumber |
| 5d | Figure numbering sequential | Figure 1, 2, 3... no gaps | Renumber |
| 5e | All cited refs in bibliography | No [??] or missing citations | Add missing refs |
| 5f | No orphan references | Every bib entry cited somewhere | Remove orphans |
| 5g | Methods ↔ Results alignment | Every method described has corresponding result | Flag gaps |
| 5h | manuscript.md written | File exists, >3000 words | Re-assemble |

---

## Next Step
→ Step 06: LaTeX Manuscript & PDF Compilation
