---
name: vera-niw-assemble
description: >
  Assembles a complete, formatted NIW I-140 petition letter as a .docx file
  from all upstream skill outputs. Takes vera-niw-evaluate JSON, vera-niw-endeavor
  output, three vera-niw-pillar prose outputs, and Google Scholar data (JSON + CSV)
  and produces a single attorney-quality Word document ready for attorney review
  or filing.

  ALWAYS use this skill when the user: has completed all three pillar runs and
  wants to assemble the final petition, asks to "build my NIW petition letter",
  asks to "generate the final petition document", wants to combine pillar outputs
  into a single Word file, or provides Google Scholar data and wants it integrated
  into the petition. Part of the NIW Petition Skill System.
---

# Vera NIW Assemble

This skill is the final stage of the NIW petition pipeline. It does NOT
redraft content — the upstream skills already produced the substance. Its job
is to stitch, synthesize the three missing sections, and output a properly
formatted .docx file ready for attorney review.

**Read `references/petition-structure.md` before generating any code.**
It contains the docx-js formatting spec, section templates, and the
credentials block pattern specific to NIW petitions.

**Read `references/gs-schema.md` before parsing Google Scholar data.**
It defines the expected JSON and CSV field names from the GS notebook.

---

## Step 1 — Collect and Validate All Inputs

Confirm all inputs before proceeding. For each missing input, ask explicitly.

### Required inputs

**1. vera-niw-evaluate output JSON**
Fields needed: `applicant` (name, pronoun, degree, field, university,
year_degree, current_title, current_employer), `pathway`, `verdict`,
`academic_metrics` (if Pathway A or C).

**2. vera-niw-endeavor output**
Fields needed: the final endeavor statement (3–5 sentences) and the three
pillar titles. These are the Output 1 and Output 2 from that skill.

**3. vera-niw-pillar outputs — all three runs**
For each pillar, collect the full petition prose (Sections 1–5 from the
pillar skill output). These are labeled "Part 1 — Petition prose" in the
pillar output.

Also extract the three Prong 3 sections (Section 5 from each pillar run).
These feed Section 7 (Unified Prong 3 Conclusion).

**4. Google Scholar data**
Two files expected from the GS notebook (see `references/gs-schema.md`):
- JSON file: summary metrics + papers array
- CSV file: papers table (used for the formatted publications table)

If GS data is not yet available, generate Section 3 with
`[GS_DATA_NEEDED: field description]` placeholders — do not block assembly.

### Input checklist before generating

- [ ] Applicant name, pronoun, degree confirmed
- [ ] Endeavor statement text in hand
- [ ] All three pillar titles confirmed
- [ ] Pillar 1 prose complete (Sections 1–5)
- [ ] Pillar 2 prose complete (Sections 1–5)
- [ ] Pillar 3 prose complete (Sections 1–5)
- [ ] Prong 3 text from all three pillars extracted
- [ ] GS JSON loaded (or placeholder mode confirmed)
- [ ] GS CSV loaded (or placeholder mode confirmed)

---

## Step 2 — Parse Google Scholar Data

→ Read `references/gs-schema.md` for exact field names.

**From JSON extract:**
- `total_citations`, `h_index`, `i10_index` (or equivalents)
- `papers` array: for each paper — title, venue, year, citation_count,
  is_first_authored, is_indexed (ISI/Scopus/PubMed)

**From CSV extract:**
- Same papers in tabular form — use to build the formatted publications table
- Sort by citation_count descending for the credentials table

**Pattern D check (run automatically):**
For each paper, check `is_indexed`. If any paper is not indexed in
ISI/Scopus/PubMed, flag it inline in the credentials section:
`[NOTE: [journal name] — indexing status unconfirmed. Verify before filing.]`
Do not silently include unverified journals.

**Independence signal scan:**
Scan `notable_citers` if present. Flag any citer from a government agency,
standards body, or named institution — these belong in Prong 2 of the
relevant pillar as additional evidence. Add a note after the credentials
section: "Notable citations from [institution] — consider adding to
Pillar [N] Prong 2."

---

## Step 3 — Generate the Four New Sections

These are the only sections this skill drafts from scratch. The rest is
pass-through from upstream skills.

### Section 1 — Opening / Introduction

Generate 2–3 paragraphs:

**Paragraph 1 — Identity and basis:**
Identify the petitioner by name, degree, institution, current role.
State the EB-2 basis (advanced degree or exceptional ability — from
evaluate JSON `pathway`). Invoke the NIW request explicitly:
> "[Petitioner] respectfully petitions for classification as an alien of
> exceptional ability in [field] under INA § 203(b)(2)(B)(i), seeking a
> National Interest Waiver of the labor certification requirement."

**Paragraph 2 — Dhanasar framework establishment (2024-2025 addition):**
Include 1–2 sentences explicitly establishing the applicable legal standard.
This preemptive framing reduces the documented risk of officers misapplying
EB-1A standards to NIW cases:
> "This petition is evaluated under the three-prong framework established
> in Matter of Dhanasar, 26 I&N Dec. 884 (AAO 2016), which requires that
> the proposed endeavor has both substantial merit and national importance,
> that the petitioner is well-positioned to advance the endeavor, and that,
> on balance, it would be beneficial to the United States to waive the
> requirements of a job offer and thus of a labor certification."

**Paragraph 3 — Endeavor introduction:**
Introduce the proposed endeavor in 2–3 sentences. This is a shortened
version of the endeavor statement — not a copy. Connect it to the
national interest claim.

**Paragraph 4 — Roadmap:**
Name the three pillars and state that each is addressed in turn:
> "This petition is organized around three pillars demonstrating the
> national importance of [petitioner]'s work and [their] unique position
> to advance it: (1) [Pillar 1 title], (2) [Pillar 2 title], and
> (3) [Pillar 3 title]."

### Section 3 — Academic Credentials and Recognition

Structure:
1. **Opening paragraph** — summarize the record (total publications, total
   citations, h-index, years active, top venue if applicable). One paragraph,
   third person, no hedging.

2. **Publications table** — built from GS CSV. Columns:
   `#` | `Title` | `Venue` | `Year` | `Citations` | `Role`
   Sort by citations descending. Flag first-authored with "First author" in Role.
   Cap at 15 rows; if more, note "X additional publications — see Google Scholar."

3. **Citation analysis paragraph** — 2–3 sentences noting total citations,
   h-index, and any notable citers (government agencies, industry reports,
   standards bodies). If notable citers exist in GS data, name them here.

4. **Peer recognition** — 1–2 sentences on peer review invitations if present
   in evaluate JSON. If not present, omit this sub-section.

### Section 7 — Unified Prong 3 Balance Test Conclusion

This section synthesizes the three per-pillar Prong 3 sections into a
single unified argument. Do not repeat the per-pillar arguments — extract
the core thread and elevate it to the level of the full endeavor.

Structure (3–4 paragraphs):

**Paragraph 1 — Combined national benefit:**
Synthesize what all three pillars together deliver. The combined benefit
is larger than any single pillar — state what the U.S. gains from the
full endeavor, not just one contribution.

**Paragraph 2 — Why labor certification is structurally inadequate:**
The strongest impracticality argument across all three pillars. This is
usually the self-directed research / cross-institutional methodology
argument. State it once, clearly, for the full endeavor.

**Paragraph 3 — Urgency at endeavor level:**
Combine the urgency arguments. If multiple pillars have CET or federal
program anchors, name them together here. This is where the time-sensitive
argument lands hardest.

**Paragraph 4 — Balance test conclusion:**
Invoke the standard explicitly:
> "For all the foregoing reasons, the national interest served by
> [petitioner]'s proposed endeavor substantially outweighs the national
> interest inherent in the labor certification process. A waiver is
> therefore appropriate and warranted."

### Section 8 — Conclusion / Prayer for Relief

Two paragraphs:

**Paragraph 1 — Summary:**
One sentence per pillar summarizing the contribution. Third person,
assertive, no hedging.

**Paragraph 2 — Prayer:**
> "For the foregoing reasons, [petitioner] respectfully requests that
> USCIS approve this I-140 petition for an immigrant visa as a member
> of the professions holding an advanced degree, with a National Interest
> Waiver of the labor certification requirement pursuant to INA
> § 203(b)(2)(B)(i) and Matter of Dhanasar, 26 I&N Dec. 884 (AAO 2016)."

---

## Step 3.5 — Formatting and Presentation Strategy (2024-2025 Best Practices)

Officers make snap judgments. The organization and formatting of the petition
is as critical as the evidence itself. Apply these formatting rules during
assembly:

**"Connect the dots" with bolding:**
After each key piece of evidence (recommender quote, citation statistic,
deployment metric), add a **bolded sentence** explicitly stating which legal
requirement it satisfies. Officers should not have to search for the
connection between evidence and legal standard.

Example flow:
> Dr. Smith states: "Dr. Kim's framework fundamentally changed how we
> approach clinical trial design in our 2,000-patient study."
> **This independent endorsement directly establishes that the Petitioner
> is well-positioned to advance the proposed endeavor under the second
> prong of the Dhanasar framework.**

**Front-load strongest evidence:**
Do not feel obligated to follow the regulatory 1-through-10 order. Present
the strongest "pieces of the puzzle" first to ensure they are seen during
the officer's initial assessment. The most compelling pillar should appear
first in the document.

**Avoid "document dumps":**
Use detailed exhibit lists and cover letters to guide the officer through
the evidence rather than simply submitting a large volume of papers.
Every exhibit should have a cover sheet explaining which requirement it
proves and how it connects to the petition narrative.

**Exhibit cover sheets:**
For each exhibit in the index, generate a brief cover sheet (2–3 sentences)
explaining:
- What the exhibit is
- Which specific legal requirement it supports (Prong 1, 2, or 3)
- How it connects to the petition narrative

---

## Step 4 — Build Exhibit Index

Scan all pillar prose for `(See Exhibit [X])` tags. Collect every unique
exhibit name. Assign sequential numbers. Build a two-column table:

| Exhibit # | Description |
|---|---|
| Exhibit 1 | Google Scholar Profile printout — [Petitioner Name] |
| Exhibit 2 | [Paper title] — [Journal], [Year] (full text) |
| ... | ... |

**Standard exhibits always present (add even if not explicitly tagged):**
- Google Scholar Profile printout
- Curriculum Vitae
- Degree certificate(s)

**For each exhibit tagged in pillar prose:**
Replace `(See Exhibit [Description])` with `(See Exhibit [N])` using
the assigned number. This cross-referencing is the final edit before
generating the docx.

---

## Step 5 — Generate the .docx File

→ Read `references/petition-structure.md` for the full docx-js code
  pattern, heading styles, table formatting, and page setup.

Use the docx skill (JavaScript + docx-js) to generate the file.

**File path:** `/home/claude/niw_petition_[LastName].docx`
**Output:** Copy to `/mnt/user-data/outputs/niw_petition_[LastName].docx`

**Section order in the docx:**
1. Opening / Introduction (generated)
2. Proposed Endeavor (from vera-niw-endeavor)
3. Academic Credentials (generated from GS data)
4. Pillar 1 full prose (from pillar run 1, with exhibit numbers applied)
5. Pillar 2 full prose (from pillar run 2, with exhibit numbers applied)
6. Pillar 3 full prose (from pillar run 3, with exhibit numbers applied)
7. Unified Prong 3 Conclusion (generated)
8. Conclusion / Prayer for Relief (generated)
9. Exhibit Index (table)

**After generating:** validate with the docx validation script. If
validation fails, fix before presenting the file.

---

## Step 6 — Post-Assembly Check

Before presenting the file, confirm:

- [ ] All `[GS_DATA_NEEDED]` placeholders are either filled or clearly
      labeled so the petitioner knows what to add
- [ ] All `[EVIDENCE NEEDED: ...]` tags from pillar prose are visible
      (not hidden) — petitioner must know what evidence to gather
- [ ] Exhibit numbers are sequential with no gaps
- [ ] All exhibit numbers in prose match the exhibit index
- [ ] Unified Prong 3 does not simply repeat pillar Prong 3 prose
- [ ] Prayer for Relief cites Dhanasar by name and citation
- [ ] No hedging language anywhere in generated sections
- [ ] No EB-1A standard language inadvertently used (e.g., "original
      contributions of major significance," "top of the field,"
      "extraordinary ability") — these invite officers to apply the
      wrong (higher) standard
- [ ] Key evidence points followed by bolded connection sentences
      linking evidence to specific Dhanasar prongs
- [ ] Strongest evidence front-loaded in presentation order
- [ ] Exhibit cover sheets present explaining which requirement each
      exhibit proves
- [ ] Dhanasar framework explicitly established in the Opening section
      to preempt EB-1A misapplication

---

## What This Skill Does NOT Do

- Redraft pillar content — that is vera-niw-pillar's job
- Evaluate NIW qualification — that is vera-niw-evaluate's job
- Generate recommendation letters — that is NIW_Recommendation (planned)
- Review the assembled petition for RFE risk — run vera-niw-pl-review after
  assembly as the final quality gate before attorney review
