---
name: vera-niw-pillar
description: >
  Generates full petition letter content for one NIW pillar at a time,
  covering all three Dhanasar prongs per pillar: (1) Substantial Merit and
  National Importance, (2) Well-Positioned to Advance the Endeavor, and
  (3) Benefit of Waiver -- why the national interest served by this pillar
  outweighs the labor certification process. Also produces a phased future
  plan and recommender guidance for each pillar.

  Requires the proposed endeavor statement and all three pillar definitions
  from vera-niw-endeavor as input. Outputs content for one specified pillar
  per run. Run once per pillar -- a 3-pillar petition requires 3 runs.

  ALWAYS use this skill when the user: has a completed endeavor and pillar
  definitions and wants to draft NIW petition content, asks to write NIW
  pillar content, wants to generate argument sections for a specific pillar,
  or is building toward a full I-140 petition letter. Part of the NIW
  Petition Skill System.
---

# NIW Pillar Content Generator

## Purpose

This skill generates full petition letter content for **one NIW pillar at a time**. It produces
attorney-grade prose covering all three Dhanasar prongs for the specified pillar, following the
structure and argumentation conventions of successful NIW petitions and RFE responses.

It does NOT generate the overall petition introduction or endeavor clarification — those
come from vera-niw-endeavor. Full petition assembly is handled by NIW_Assemble.

**Prong 3 is generated per pillar.** Each pillar produces its own balance test argument
tied to that pillar's specific evidence. NIW_Assemble synthesizes these into a unified
Prong 3 conclusion — but the building blocks live here, one per pillar.

---

## Required Inputs

Confirm all of the following before generating. If any are missing, ask.

### 1. Applicant Profile
- Full name and pronouns
- Degree(s), field(s), institution(s), year(s)
- Current title and employer

### 2. Full Endeavor Description
The complete proposed endeavor text. Needed for cross-pillar cohesion.

### 3. All Pillars (for context)
Brief description of all pillars — even those not being written now. Prevents redundancy.

### 4. Target Pillar
Which pillar to write now. Name it explicitly.

### 5. Pillar-Specific Evidence
Raw evidence for THIS pillar. Ask for anything missing. More is better.

| Evidence Type | Examples |
|---|---|
| Foundational work | Paper titles, dissertation chapters, working papers |
| Methodologies used | Named techniques (DiD, NLP, survival analysis, etc.) |
| Data scale | Number of records, years covered, national coverage % |
| Outcomes/results | Quantified findings ("20% price discount elimination") |
| Publications | Journal, conference, status (published / under review / SSRN) |
| **Publication integrity** | For each journal: verify it is indexed in ISI/Scopus/PubMed. If unknown, flag before writing — generating confident Prong 2 prose around a predatory journal creates an RFE. |
| Awards/recognition | Conference awards, rankings, invitations |
| Citations by others | Who cited, their institution, their paper |
| Tool/code adoption | GitHub, downloads, practitioner signals |
| Expert endorsements | Name, title, institution, what they said |
| Future plan details | Phases, partners, target agencies, deliverables |
| Federal policy hooks | Government programs, agency mandates, legislation |

---

## Output Structure

Generate these sections in order as petition-ready prose.

---

### SECTION 1 — PRONG 1A: Distinguished from Routine Practice

**Heading format:**
`[Petitioner]'s [Pillar Title] Goes Beyond Routine [Academic/Industry] Practice and Offers Unique, Scalable, and Transferable Solutions`

#### 1.1 Nationwide Critical Problem — National in Scope
- Name the structural/systemic problem. Frame as national, not regional.
- Establish that the mechanism operates nationally even if validation data is regional.
- Anchor with a national-scale statistic: dollar figure, % of economy, number of households/jobs.
- Name the failure in existing practice: why current approaches are insufficient.

#### 1.2 Unique Capabilities — What This Work Provides That Doesn't Exist
- Describe what the petitioner's approach makes possible that wasn't possible before.
- Name the specific methodology and explain why it is non-routine.
- Contrast with existing commercial and academic alternatives — explain their limitations.
- Use "replicable," "portable," "transferable" language where applicable.
- **Innovation vs. Implementation (2024-2025 AAO priority):** Explicitly argue
  how this work represents a genuine improvement over existing solutions using
  unique methodologies. The AAO has dismissed petitions where the endeavor was
  merely implementing existing technology. Use language demonstrating that this
  work is "different, better, or less costly than current solutions" — frame
  as advancing beyond what is currently available on the market, not applying it.

#### 1.3 Transferable Solutions with Broad Economic and Societal Benefits
- Scale the impact: which sectors, agencies, or populations benefit.
- Quantify wherever possible.
- Explain why this work can be adopted beyond any single employer or region.
- Connect to public benefit: fiscal stability, investor protection, job preservation, etc.

---

### SECTION 2 — PRONG 1B: Broader Societal Implications

**Heading format:**
`[Petitioner]'s [Pillar Title] Has Broader Societal Implications for National Security, Economic Stability, and Public Welfare`

Generate only sub-sections that apply. Always include at least 2–3.

#### 2.1 National Security (if applicable)
- Identify the national security dimension.
- Connect petitioner's work directly to preventing or mitigating that risk.

#### 2.2 Economic Stakes — Quantified
- Lead with the scale: "$X trillion," "X million jobs," "X% of U.S. GDP."
- Source the number to a government report, industry study, or federal agency.
- Explain the causal chain: without this work → what happens → economic consequence.

#### 2.3 Public Welfare
- Identify the specific population that benefits.
- Use concrete beneficiary language: "54% of U.S. households," "over 19,000 municipalities," etc.
- Frame in terms of equity and access, not just aggregate economic efficiency.

#### 2.4 Critical Government Initiatives (ALWAYS include)
- List 2–4 specific named federal programs, legislation, or agency mandates.
- For each: name, year, dollar amount or scope if available, direct connection to this pillar.
- This section proves national importance through government validation.
- Examples: CHIPS Act, SEC rulemaking, NSF programs, Treasury initiatives, Patent Eligibility Restoration Act, IRA provisions, FINRA oversight mandates, etc.

---

### SECTION 3 — PRONG 2: Well-Positioned to Advance This Pillar

**Heading format:**
`[Petitioner] Is Exceptionally Well-Positioned to Advance [Pillar Title]`

#### 3.1 Primary Author and Intellectual Driver
- Identify the specific paper(s) or dissertation chapter(s) underpinning this pillar.
- Establish petitioner as the primary intellectual contributor, not a participant.
- If co-authored: describe petitioner's specific role explicitly.
- Required language: "primary author," "intellectual driver," "driving force behind."

#### 3.2 Demonstrated Expertise in Required Methodologies
- List specific technical methods required for this pillar.
- For each: name the method, confirm petitioner has applied it, cite the specific application with a result.
- Include data scale where impressive (records analyzed, years covered, coverage %).
- Format as named sub-items.

#### 3.3 Proven Record of Success
- Named journal publication with journal prestige noted.
- Named conference presentations with conference prestige noted.
- Citations by independent scholars: name, institution, their paper, what they said.
- Awards and competitive recognitions.
- Public tools, code, or datasets and any adoption signals.
- Papers under review at named top journals.
- **Critical (2024-2025 AAO trend):** Citation records alone are insufficient
  without evidence of real-world impact. Pair citation evidence with expert
  testimonials, documented adoption, or practitioner use. The AAO has dismissed
  cases where citations were presented without evidence of broader significance.
- **Postdoctoral researcher note:** The AAO has overturned denials claiming
  postdoctoral researchers cannot be "influential leaders." Strong citation
  records paired with expert testimonials can successfully rebut this claim.
  If the petitioner is a postdoc or early-career researcher, frame their
  record of success as demonstrating emerging leadership, not just potential.

#### 3.4 Endorsement by Independent Experts
- For each: full name, title, institution, why credible for THIS pillar.
- Include a specific 1–3 sentence quote that addresses this pillar directly.
- Explain why the endorsement carries weight.
- Minimum 2 endorsers. At least one academic, one industry/regulatory.

#### 3.5 Documented Interest from U.S. Entities (2024-2025 AAO emphasis)
- Letters of interest from leading U.S. organizations demonstrating demand
  for the petitioner's specific work — among the strongest Prong 2 evidence
  per recent AAO decisions.
- Contracts with American clients naming the petitioner's specific method,
  tool, or service.
- U.S. business incorporation (LLC, Corp) with evidence of active operations.
- Government agency engagement: MOUs, letters of support, grant awards, or
  formal consultations with named federal agencies.
- This section proves the endeavor is viable and has real U.S. stakeholders —
  not speculative. The AAO remanded a 2024 denial specifically because the
  petitioner demonstrated U.S. incorporation and active American contracts.

---

### SECTION 4 — FUTURE PLAN

**Heading format:**
`[Petitioner]'s Plan for Future Activities: [Pillar Title]`

Generate 3–4 phases. Each phase must include:
- Phase name and focus area
- 2–4 specific activities with concrete deliverables
- Named data sources, partner types, or target agencies
- Measurable outcomes (accuracy targets, jurisdictions served, publication targets)

Standard structure (adapt to pillar):
- **Phase I:** Data infrastructure, dataset construction, baseline model
- **Phase II:** Model refinement, validation, technical testing
- **Phase III:** Pilot implementation with named stakeholder types
- **Phase IV:** National scaling, open publication, federal agency engagement

Future plan must:
- Name specific databases, agencies, or platforms (USPTO, EDGAR, IRS, SEC, NSF, GitHub, etc.)
- Name specific journals or conference tracks for planned publications
- Name specific federal agencies as dissemination targets
- Include a measurable national-scale outcome as the end state

---

### SECTION 5 — PRONG 3: Benefit of Waiver for This Pillar

**Heading format:**
`The National Interest Served by [Petitioner]'s [Pillar Title] Substantially Outweighs the Protections Afforded by the Labor Certification Process`

This section argues the balance test *specifically for this pillar's contribution*.
Each pillar has different evidence; each Prong 3 argument is therefore distinct.
NIW_Assemble will synthesize all three into a unified conclusion — but each pillar
must stand on its own here.

**Hard rule:** Never argue labor shortage as the primary justification. USCIS
explicitly rejects this. The argument must center on the petitioner's specific,
indispensable contribution that cannot be replicated through a standard PERM posting.

#### 5.1 Impracticality of Labor Certification for This Work

Argue why the nature of THIS pillar's specific work makes the PERM process
inadequate or inappropriate. Use whichever of these arguments apply:

- **Self-directed research agenda:** The petitioner's work cannot be bounded
  in a standard PERM job description because it is defined by the petitioner's
  own intellectual contributions, not by an employer's operational needs.
- **Cross-institutional methodology:** The petitioner's approach is designed
  to be transferred, adopted, and built upon across multiple institutions —
  no single employer's PERM posting captures this scope.
- **Independence test:** Confirm that the petitioner can and will advance this
  pillar independent of any single employer. Open-source tools, published
  methodologies, consulting, and entrepreneurial paths are strong signals.
- **Proprietary innovation:** The specific approach documented in this pillar
  was originated by the petitioner — no hiring process could source this from
  the domestic labor market because it does not exist elsewhere.

#### 5.2 Urgency of This Pillar's Contribution

Argue why the U.S. needs this specific pillar's contribution NOW, not after
a 12–24 month PERM process. Use the strongest applicable argument:

- **CET alignment:** If this pillar addresses a White House Critical and
  Emerging Technologies priority area, name it explicitly and argue that
  delay creates a measurable gap in a time-sensitive federal priority.
- **Named federal program with a deadline or funding window:** Connect delay
  to a specific consequence for a named initiative.
- **Emerging field window:** If the petitioner is at a formative moment in
  a new subfield, delayed entry allows competing approaches to establish.
- **Already-demonstrated urgency:** If adoption has already occurred
  (government, institutional), the benefit is not speculative — it is
  ongoing and delay means continued operation without the petitioner.

#### 5.3 Demonstrated Interest and Non-Speculative Benefit

Distinguish this pillar's benefit from a hypothetical future contribution:

- Name any parties already interested in, using, or building on this work
  (agencies, institutions, companies, standards bodies).
- Cite any government adoption, licensing, formal endorsement, or
  practitioner citations — these show the benefit exists, not merely that
  it might exist after the petitioner arrives.
- If the work is already deployed or ongoing, frame the waiver as enabling
  continuation, not initiation: "The national benefit is not speculative —
  it is already being realized and would be interrupted by a protracted
  labor certification process."

#### 5.4 Preemptive Dhanasar Standard Framing (2024-2025 AAO trend)

If the petitioner's case is vulnerable to EB-1A standard misapplication
(academic-heavy profile, researcher, technical field), include 1–2 sentences
explicitly establishing the correct legal standard:

> "This petition is evaluated under the three-prong framework of Matter of
> Dhanasar, 26 I&N Dec. 884 (AAO 2016), which requires that the proposed
> endeavor has substantial merit and national importance, that the petitioner
> is well-positioned to advance it, and that the balance of factors favors
> waiving the labor certification requirement. The Dhanasar framework does
> not require the petitioner to demonstrate 'extraordinary ability' or
> 'original contributions of major significance' — standards applicable to
> EB-1A, not EB-2 NIW."

This preemptive framing reduces the risk of officers defaulting to the wrong
standard. Include only when the EB-1A misapplication risk is medium or high.

#### 5.5 Balance Test Conclusion

One concise paragraph (3–4 sentences) synthesizing the above for this pillar:

- State the specific national benefit this pillar delivers
- State why labor certification cannot adequately source this contribution
- Invoke: "the national interest served by [pillar] substantially outweighs
  the national interest inherent in the labor certification process"
- Do not end with a generic closing — end with the strongest specific claim

---

### SECTION 6 — RECOMMENDER GUIDANCE (internal, not for petition)

For each recommended letter writer, generate this block:

```
RECOMMENDER [#]
Type: [Academic / Industry / Regulatory / Government]
Ideal profile: [expertise that makes them credible for THIS pillar]
Independence: [no direct reporting relationship to petitioner — should not be petitioner's
  current supervisor, PhD advisor, or close collaborator. At least 1 of 3 must be
  completely independent. Supervisors/advisors weigh less; independent experts weigh more.]

Key claims to include:
1. [National importance claim with statistic if possible]
2. [Claim about petitioner's unique methodology — name the specific technique]
3. [Before/after framing: "Before [petitioner's work], the field lacked X.
   [Petitioner] developed Y, which now enables Z."]
4. [Claim about petitioner's impact — ideally citing their own use of petitioner's work]
5. [Forward-looking claim about why petitioner is uniquely positioned]

What makes this letter distinctive:
[What this recommender can say that others cannot — must be specific to THIS pillar]

What to avoid:
- Generic praise without specifics ("brilliant researcher," "exceptional talent")
- Claims not tied to verifiable evidence
- Repeating the petitioner's CV without independent assessment
- Describing the field's importance rather than THIS petitioner's contribution
```

**Critical rule for all 3 letters:** The letter must include explicit before/after
framing — describe what existed before the petitioner's contribution and what became
possible after. USCIS officers are trained to spot generic letters; before/after
framing is the signal that a letter is substantive, not boilerplate.

Provide 3 recommender profiles: 1 senior academic, 1 industry practitioner, 1 government/regulatory/policy.
At least 1 must have no reporting relationship to the petitioner.

---

## Writing Conventions (ALWAYS FOLLOW)

**Tone:**
- Formal, attorney-quality prose
- Third person throughout
- Assertive — no hedging ("may," "might," "could potentially")
- Present tense for ongoing work, past tense for completed work

**Argumentation pattern:**
Problem → Gap in existing practice → Petitioner's solution → National scale of impact → Evidence

**Scale language (at least one per section):**
- Dollar figures: "$X billion/trillion"
- Population: "X million households/workers/investors"
- Government reach: "over X,000 municipalities," "serving X% of U.S. market"
- Federal citations: specific act names, agencies, programs

**Recommender quotes:**
- Always introduce with full name, title, institution
- Quote must be specific to the pillar — no generic praise
- Quote must contain before/after framing or a specific claim about this petitioner's unique contribution
- Follow with one sentence: why this source is credible

**Evidence tagging:**
- Every factual claim tied to a specific piece of evidence must include a parenthetical
  reference that NIW_Assemble can convert to a numbered exhibit:
  e.g., "(See Exhibit [CDC Guidance Document])" or "(See Exhibit [Google Scholar Profile])"
- Never assert a statistic or outcome without a traceable source tagged in the prose
- If evidence is not yet in hand, write: [EVIDENCE NEEDED: description of what is required]
  — do not generate confident prose around missing evidence

**Future plan:**
- Name specific databases, platforms, agencies, journals
- Each phase ends with a measurable deliverable
- Final phase ends with a national-scale outcome statement

**Dhanasar standard language:**
- "Goes beyond routine academic/industry practice"
- "Primary author and intellectual driver"
- "National in scope" / "nationwide in application"
- "Portable and replicable" / "scalable solution"
- "Directly aligns with [named federal agency/program]"

**Formatting for persuasion (2024-2025 best practices):**
- **"Connect the dots" strategy:** After each strong quote or evidence point,
  add a **bolded sentence** explaining exactly how it proves a specific legal
  requirement. Officers should not have to find key information in long letters —
  make the connection explicit and visually prominent.
  Example: After a recommender quote → **"This endorsement directly establishes
  that [Petitioner]'s methodology goes beyond routine practice in the field,
  satisfying the first prong of the Dhanasar framework."**
- **Front-load strongest evidence:** Do not feel obligated to follow regulatory
  order (1-through-10). Present the strongest "pieces of the puzzle" first to
  ensure they are seen during the officer's initial assessment.
- **Avoid EB-1A language:** Never use "original contributions of major
  significance," "top of the field," or "extraordinary ability" — these
  invite officers to apply the wrong (higher) standard.

---

## Quality Checks Before Finalizing

**Prong 1:**
- [ ] Every importance claim has a number OR a named federal program
- [ ] "Distinguished from routine practice" appears in Prong 1A
- [ ] Government Initiatives section (2.4) always present
- [ ] Pillar connects back to the overall endeavor at least once

**Prong 2:**
- [ ] Petitioner is "primary driver," not a participant
- [ ] At least one named methodology explained with a specific result
- [ ] All publications verified as non-predatory (indexed in ISI/Scopus/PubMed) — if uncertain, flag
- [ ] At least one named independent expert quote specific to this pillar
- [ ] At least one recommender has no direct reporting relationship to petitioner
- [ ] All endorsement quotes contain before/after framing, not generic praise
- [ ] Future plan names at least one agency and one journal per phase

**Prong 3:**
- [ ] Labor shortage argument is absent — if present, rewrite immediately
- [ ] Impracticality argument is specific to this pillar's work (not generic)
- [ ] Urgency argument names a specific federal program or CET area
- [ ] Balance test conclusion paragraph is present (Section 5.4)
- [ ] Independence of petitioner's work is established (Section 5.1)

**General:**
- [ ] No placeholder text remains — flag missing evidence as [EVIDENCE NEEDED: description]
- [ ] No hedging language anywhere ("may," "might," "could potentially")

---

## What This Skill Does NOT Generate

- Petition introduction or endeavor clarification → vera-niw-endeavor
- Per-pillar Prong 3 synthesis into a single unified balance argument → NIW_Assemble
  (NIW_Assemble combines the three per-pillar Prong 3 sections produced here)
- Full petition assembly and cover letter → NIW_Assemble
- Recommendation letter drafts → NIW_Recommendation (when available)
- Qualification assessment → NIW_Evaluate
