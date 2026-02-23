---
name: vera-niw-rfe-response
description: >
  Generates a complete, point-by-point NIW RFE (Request for Evidence) response
  document. Takes the original petition letter, the RFE notice (scanned or text),
  and reference letters as inputs. Produces an attorney-quality response that
  quotes each USCIS finding verbatim and rebuts it with evidence, updated
  metrics, and new exhibits — structured to force the officer to "write from
  scratch" rather than reuse their negative draft. Triggers when the user
  receives an RFE on their NIW I-140 petition, uploads or pastes an RFE notice,
  mentions "RFE response", "request for evidence", "USCIS asked for more
  evidence", "how do I respond to my NIW RFE", needs a point-by-point rebuttal,
  or asks "what should I include in my RFE response". Part of the NIW Petition
  Skill System v1.0.
---

# Vera NIW RFE Response

---

## Table of Contents

| Section | Description |
|---|---|
| [Purpose](#purpose) | Core goal, critical rules, and tone guidance |
| [Step 0 — Collect and Validate All Inputs](#step-0--collect-and-validate-all-inputs) | Required inputs and input checklist |
| [Step 1 — RFE Triage and Finding Classification](#step-1--rfe-triage-and-finding-classification) | Extract findings, detect EB-1A misapplication, new endeavor trap |
| [Step 2 — Rebuttal Patterns](#step-2--common-rfe-finding-patterns-and-rebuttal-frameworks) | R1–R8 pattern reference (see `reference/rebuttal-patterns.md`) |
| [Step 3 — Document Structure](#step-3--document-structure) | Header, opening, Sections I–V, appendix |
| [Step 4 — Evidence Presentation Rules](#step-4--evidence-presentation-rules) | Quoting letters, tables, metrics, exhibit references |
| [Step 5 — Writing Conventions](#step-5--writing-conventions) | Tone, structure, language rules, formatting |
| [Step 6 — Quality Checks](#step-6--quality-checks-before-finalizing) | Consistency, evidence, legal standard, formatting, authenticity |
| [Step 7 — Post-Draft Review](#step-7--post-draft-review) | Run vera-niw-pl-review on the complete document |
| [RFE Response Heuristics](#rfe-response-heuristics) | Five self-tests before finalizing |

---

## Purpose

Generate a complete RFE response document that addresses every USCIS finding
point-by-point, introduces new evidence gathered since filing, and presents
an affirmative case so compelling that the officer cannot reuse their negative
draft language. The goal is to force the officer to "write from scratch" to
justify approval.

**Critical rule:** The RFE response must NOT introduce a new or materially
reframed proposed endeavor. The endeavor can be *sharpened* and *clarified*
with greater specificity, but it must remain substantively identical to the
original petition. Introducing a "new endeavor" in the RFE response is a
documented ground for denial.

**Tone:** The RFE response is not the time for humility. Switch into
assertive self-promotion mode. Every claim must be backed by evidence, but
the framing must be confident, direct, and unhedged. This is a final merits
determination — treat it accordingly.

---

## Step 0 — Collect and Validate All Inputs

Confirm all inputs before proceeding. For each missing input, ask explicitly.

### Required Inputs

**1. RFE Notice (primary input)**
The actual USCIS RFE letter — scanned PDF, pasted text, or transcribed.
Extract:
- Case identifiers: IOE number, A-Number, receipt number
- Response deadline
- Classification sought (should be EB-2 NIW)
- Each specific finding/concern raised — quote verbatim
- Which Dhanasar prong(s) each finding addresses
- Any incorrect standards applied (EB-1A language in an NIW RFE)

**2. Original Petition Letter**
The I-140 petition letter that was filed. Needed to:
- Confirm the original proposed endeavor statement (must not change)
- Identify what evidence was originally submitted
- Check for consistency — the RFE response must not contradict the original
- Identify which pillars/arguments the officer found insufficient

**3. Reference / Recommendation Letters (if applicable)**
- Original letters filed with the petition
- Any new letters gathered since filing
- For new letters: confirm recommender name, title, institution, independence

**4. Updated Metrics (if applicable)**
- Updated Google Scholar profile (citations, h-index, i10-index)
- New publications since filing
- New patents, grants, contracts, or deployments since filing
- Any new media coverage, adoption signals, or institutional interest

**5. New Evidence Gathered Since Filing**
- New expert letters (the "second string" if strategically held back)
- Co-author attribution letters (if authorship was questioned)
- Contracts, MOUs, or letters of interest from U.S. organizations
- U.S. business incorporation documents (if applicable)
- Updated citation analysis (independent vs. self-citations)
- Any evidence specifically addressing the RFE's concerns

### Input Checklist

- [ ] RFE notice text extracted with all findings identified
- [ ] Original petition letter in hand
- [ ] Original proposed endeavor statement confirmed
- [ ] Each RFE finding mapped to a Dhanasar prong
- [ ] Incorrect standard application detected (if any)
- [ ] Updated metrics available (or gaps identified)
- [ ] New evidence inventory complete
- [ ] Response deadline confirmed

---

## Step 1 — RFE Triage and Finding Classification

Before drafting anything, classify every finding in the RFE.

### 1.1 Extract and Quote Each Finding

For each finding in the RFE, create an entry:

```
FINDING [#]:
Prong: [1 / 2 / 3 / Threshold / Procedural]
USCIS Quote: "[Exact verbatim quote from the RFE]"
Core Concern: [1-sentence summary of what the officer is really asking for]
Incorrect Standard: [YES/NO — does this finding apply EB-1A criteria to NIW?]
Evidence Available: [What evidence exists to rebut this]
Evidence Gap: [What additional evidence is needed]
Rebuttal Strategy: [Brief approach — see patterns below]
```

### 1.2 Detect EB-1A Standard Misapplication

Scan all findings for language that applies EB-1A criteria:
- "original contributions of major significance"
- "top of the field" / "at the very top"
- "extraordinary ability"
- "sustained national or international acclaim"
- Demanding proof of being "the best" rather than "well-positioned"
- Requiring evidence beyond the Dhanasar three-prong framework

**If detected:** Flag immediately. The response must include a respectful
but firm rebuttal establishing the correct legal standard. Cite Matter of
Dhanasar, 26 I&N Dec. 884 (AAO 2016) and the USCIS Policy Manual. Failing
to challenge misapplication of the law increases denial risk — the officer
may believe they are correct if not corrected.

### 1.3 Identify the "New Endeavor" Trap

Compare the original petition's endeavor statement with what the RFE seems
to expect. The response must sharpen and clarify the endeavor — but NEVER
introduce a materially new or reframed endeavor. If the original endeavor
was vague, the response clarifies what was always meant. It does not pivot.

**Red flag language to avoid in the response:**
- "The petitioner's endeavor is now..." (implies change)
- "The petitioner has refined their endeavor to..." (implies it was different)
- "In light of the RFE, the petitioner's endeavor is better described as..."

**Acceptable language:**
- "To clarify the proposed endeavor as described in the original petition..."
- "The petitioner's proposed endeavor, as stated in the original filing, is..."
- "The original petition describes the endeavor as [quote] — this response
  provides additional detail and evidence supporting this endeavor."

---

## Step 2 — Common RFE Finding Patterns and Rebuttal Frameworks

Read `reference/rebuttal-patterns.md` for the full R1–R8 pattern library. Match each triaged finding to the closest pattern and adapt the framework.

**Quick index:**

| Pattern | Finding Type | Key Strategy |
|---|---|---|
| R1 | Publications too recent | Peer review cycles + pre-publication evidence |
| R2 | No government letters | Dhanasar doesn't require it + federal mandate mapping |
| R3 | No economic effects | Supplementary confirmation + three independent lines |
| R4 | Work not adopted | Citation independence analysis + usage categorization |
| R5 | Not lead author | Authorship conventions + co-author attribution letters |
| R6 | Low citation count | Growth trajectory + quality over quantity |
| R7 | Peer review insufficient | Editorial attestation + independent recognition |
| R8 | Prong 3 balance | Counterfactual + PERM incompatibility + urgency |

---

## Step 3 — Document Structure

Generate the RFE response in this exact structure:

---

### Header Block

```
RESPONSE TO REQUEST FOR EVIDENCE

Petitioner and Beneficiary: [Full Name]
Classification Sought: Employment-Based Immigration, Second Preference
EB-2 National Interest Waiver, INA §203(b)(2)(B)
IOE: [IOE Number] | A-Number: [A-Number] | Response Due: [Date]
```

### Opening Paragraphs (2-3 paragraphs)

**Paragraph 1 — Framing:**
State that this response addresses each finding raised by USCIS. Invoke
the Dhanasar standard explicitly. State that the evidence demonstrates
all three prongs by a preponderance of the evidence.

**Paragraph 2 — Updated metrics headline (if applicable):**
If metrics have improved since filing, lead with the growth:
> "Since the petition filing (priority date: [date]), [Petitioner]'s
> [metric] has grown from [X] to [Y] — a [Z]% increase."

This immediately signals that the case is stronger now than at filing.

**Paragraph 3 — EB-1A standard correction (if applicable):**
If the RFE applied EB-1A standards, include the correction early:
> "We note that certain findings in the RFE apply standards from the
> EB-1A extraordinary ability classification rather than the EB-2 NIW
> framework established in Matter of Dhanasar, 26 I&N Dec. 884 (AAO 2016).
> This response addresses the correct Dhanasar standard throughout."

---

### Section I — Clarification of Proposed Endeavor

Restate the proposed endeavor with greater precision and detail.
**The endeavor must be substantively identical to the original filing.**

Structure:
1. Endeavor statement (same as original, may add detail but not change scope)
2. Execution model (how the endeavor operates — tracks, programs, phases)
3. Named programs within the endeavor (if the work has multiple dimensions)
4. For each program: what it does, what problem it solves, current status

**Formatting:** Use bold program names and brief descriptions. The officer
should be able to scan this section in 60 seconds and understand the full
scope of the endeavor.

---

### Section II — Prong One: Substantial Merit and National Importance

**Part A — Point-by-Point Response to USCIS Findings**

For each Prong 1 finding:

```
### Finding [#]: [Short Title]

**USCIS Finding:** "[Exact verbatim quote from RFE]"

**Response:**

[Rebuttal using the appropriate Pattern R# framework. Structure as:]
1. [Correct the legal standard if misapplied]
2. [Present the core evidence]
3. [Quote expert letters with bolded connection sentences]
4. [Reference specific exhibits]
5. [Conclude with why this finding is addressed]
```

**Part B — Affirmative Case: Substantial Merit and National Importance**

After addressing all findings, present a positive affirmative case:
1. Three independently sufficient grounds for national importance
2. Expert letter quotes organized by ground
3. Federal policy alignment across all endeavor programs
4. Tables where helpful (publication venues, citation analysis, etc.)

---

### Section III — Prong Two: Well-Positioned to Advance the Endeavor

**Part A — Undisputed Factors**

List what USCIS did NOT contest:
- Education and qualifications
- Technical skills
- Publication record (if not contested)
- Plans for future activity (if not contested)

This frames the RFE as narrow, not comprehensive.

**Part B — Point-by-Point Response to USCIS Findings**

For each Prong 2 finding: same structure as Prong 1 findings.

**Part C — Affirmative Case: Progress and Stakeholder Interest**

Present evidence of:
1. Progress already made toward the endeavor since filing
2. Interest from relevant stakeholders (industry, academic, government)
3. Unique dual-track or multi-dimensional positioning
4. "Record of success at a glance" summary (bullet points with numbers)

---

### Section IV — Prong Three: Balance Test

Structure:
1. Expert counterfactual quote (what happens without this person)
2. Federal urgency argument (compliance deadlines, mandate timing)
3. Substitutability argument (specific scarcity, not labor shortage)
4. Structural incompatibility with PERM (multi-track work, independence)
5. Non-speculative benefit (already deployed, adopted, in use)

**Hard rule:** Never argue labor shortage. Frame as unique contribution
that cannot be sourced through a standard PERM posting.

---

### Section V — Conclusion

Structure:
1. One paragraph per prong summarizing the strongest evidence
2. Prayer for approval citing Dhanasar by name and full citation
3. Statement that all new exhibits are submitted contemporaneously

---

### Appendix — New Exhibits

Table listing all new exhibits submitted with this response:

| Exhibit | Description | Prong Supported |
|---|---|---|
| X1 | [New expert letter — Name, Title, Institution] | Prong 1, 2 |
| X2 | [Updated Google Scholar profile] | Prong 2 |
| ... | ... | ... |

---

## Step 4 — Evidence Presentation Rules

### Quoting Expert Letters

Every expert letter quote must follow this pattern:
1. Introduce the recommender: full name, title, institution, exhibit number
2. Quote the specific language (in quotation marks)
3. **Bolded connection sentence:** Explain exactly how this quote addresses
   the specific RFE finding or legal requirement
4. If the recommender's independence is relevant, state it explicitly

### Tables

Use tables for:
- Citation distribution (geographic, domain, institutional)
- Publication venue quality (Scimago rankings, impact factors)
- Updated metrics comparison (filing date vs. current)
- Cross-domain adoption evidence
- Exhibit lists

### Updated Metrics

Present growth since filing prominently:
- Use percentage growth figures
- Show trajectory (filing → current → projected)
- Contextualize with field-appropriate benchmarks (ESI percentiles, etc.)
- Pair quantitative growth with qualitative significance

### Exhibit References

Every factual claim must reference a specific exhibit:
- Use format: `(Exhibit [ID])` or `(Exhibit [ID]: [Brief Description])`
- New exhibits use a distinct numbering scheme (e.g., X1, X2, D1, D2)
  to distinguish from original petition exhibits
- Every new exhibit appears in the Appendix table

---

## Step 5 — Writing Conventions

**Tone:**
- Formal, attorney-quality prose
- Third person throughout (except when quoting letters)
- Assertive — no hedging ("may," "might," "could potentially")
- Respectful but firm when correcting officer's legal standards
- Not humble — this is a final merits determination

**Structure pattern for each rebuttal:**
1. Quote the USCIS finding verbatim
2. Identify the legal standard (correct it if wrong)
3. Present evidence organized by strength
4. Bold the connection to the legal requirement
5. Conclude with a clear statement that the finding is addressed

**Language rules:**
- Never use EB-1A language ("original contributions of major significance,"
  "top of the field," "extraordinary ability")
- Never argue labor shortage
- Never introduce a new endeavor
- Always cite Dhanasar by full name and citation on first reference
- Use "preponderance of the evidence" standard language
- Reference specific exhibit numbers for every factual claim

**Formatting for persuasion:**
- Bold key connection sentences after evidence
- Front-load strongest evidence within each section
- Use tables for data-dense arguments (citations, publications, metrics)
- Use numbered lists for multi-part rebuttals
- Keep paragraphs focused — one argument per paragraph

---

## Step 6 — Quality Checks Before Finalizing

### Consistency Checks

- [ ] Proposed endeavor in response is substantively identical to original
      petition — sharpened and clarified, but not changed
- [ ] No "new endeavor" language present
- [ ] All RFE findings addressed — none skipped or glossed over
- [ ] EB-1A standard correction included if misapplication detected
- [ ] Dhanasar cited by full name and citation on first reference

### Evidence Checks

- [ ] Every factual claim references a specific exhibit
- [ ] All new exhibits listed in Appendix table
- [ ] Updated metrics presented with growth percentages
- [ ] Expert letter quotes include full recommender identification
- [ ] Bolded connection sentences follow every key evidence point
- [ ] No unexhibited assertions — if evidence is not in hand, flag it
      as `[EXHIBIT NEEDED: description]`

### Legal Standard Checks

- [ ] No EB-1A language used anywhere in the response
- [ ] No labor shortage argument in Prong 3
- [ ] "Preponderance of the evidence" standard invoked
- [ ] Dhanasar three-prong framework explicitly stated
- [ ] Matter of Dhanasar cited correctly: 26 I&N Dec. 884 (AAO 2016)

### Formatting Checks

- [ ] All USCIS findings quoted verbatim in quotation marks
- [ ] Key evidence points followed by bolded connection sentences
- [ ] Tables used for citation data, publication venues, exhibit lists
- [ ] Strongest evidence front-loaded in each section
- [ ] Response deadline noted in header

### Authenticity Checks

- [ ] Expert letter quotes sound authentic, not regulatory-parroting
- [ ] No generic superlatives without factual support
- [ ] Each letter quote is specific to the relevant finding
- [ ] Independence of recommenders stated where applicable

---

## Step 7 — Post-Draft Review

After generating the response, run **vera-niw-pl-review** on the complete
document. The review skill will check:
- Pattern A (Occupation ≠ Endeavor) — is the sharpened endeavor still valid?
- Pattern B (Vagueness) — is the response specific enough?
- Pattern C (National Importance) — field vs. specific importance
- Pattern D (Publication Due Diligence) — updated metrics valid?
- Pattern E (Prong 2 Failures) — well-positioned argument sufficient?
- Pattern F (Recommendation Letters) — new letters authentic?
- Pattern G (Prong 3) — balance test argument complete?
- Pattern H (Evidence Organization) — exhibits indexed and cross-referenced?
- Pattern I (Innovation vs. Implementation) — not just implementing?
- Pattern J (EB-1A Misapplication) — correct standard throughout?

**Additionally:** The review should specifically check for the "new endeavor"
trap — if the response introduces a materially different endeavor, flag it
as a critical, case-ending risk.

---

## RFE Response Heuristics

Run these five self-tests before finalizing:

| Test | Question | Fail Action |
|---|---|---|
| **Write from Scratch** | Does this contain enough NEW evidence that the officer's draft denial is no longer usable? | Add stronger evidence or new letters |
| **Every Finding** | Does the response quote and rebut every single RFE finding? | Address missing findings — unaddressed = conceded |
| **Officer Education** | If EB-1A misapplied, can a cross-trained officer understand the correct Dhanasar standard? | Strengthen the legal framework section |
| **Fresh Evidence** | Are there genuinely new exhibits the officer hasn't seen? | Gather new letters, updated metrics, adoption signals |
| **60-Second Scan** | If scanned for 60 seconds, is the strongest evidence visually prominent? | Add bold connection sentences, front-load evidence |

---

## What This Skill Does NOT Do

| Task | Use Instead |
|---|---|
| Evaluate NIW qualification | vera-niw-evaluate |
| Generate the original petition | vera-niw-endeavor + vera-niw-pillar + vera-niw-assemble |
| Draft recommendation letters | vera-niw-recommendation |
| Post-draft review | vera-niw-pl-review |
| Provide legal advice | Always recommend attorney review before filing |

