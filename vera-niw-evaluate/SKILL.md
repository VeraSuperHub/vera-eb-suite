---
name: vera-niw-evaluate
description: >
  Evaluates whether a user qualifies for a National Interest Waiver (NIW)
  self-petition based on a structured rubric. Assigns a qualification tier
  (QUALIFIED / LIKELY_QUALIFIED / BORDERLINE / NOT_QUALIFIED), identifies
  strengths and gaps with evidence scoring, and produces a structured JSON
  output consumed by downstream NIW skills (NIW_Endeavor, NIW_Pillar,
  NIW_Assemble). Always errs conservative — the NIW bar is high. Part of
  the NIW Petition Skill System v1.0.
---

# NIW_Evaluate — Background Evaluation Skill

## Purpose

Determine whether a user's background meets the USCIS NIW standard before
investing time in petition drafting. Output a clear verdict with evidence
assessment, gap analysis, and a recommendation on how to proceed.

**Default stance: conservative.** When evidence is ambiguous or thin, flag it.
USCIS scrutiny on NIW has increased significantly. A weak petition does more
harm than waiting.

---

## Step 0 — Information Gathering

Before evaluating, collect the following. Ask for missing items explicitly.
Do not guess or assume.

### Required Inputs

```
PERSONAL
- Full name, pronoun
- Highest degree, field, university, year
- Undergraduate degree (if claiming 5yr experience pathway)

PROFESSIONAL EXPERIENCE
- Current title, employer, years in role
- Total years of professional experience post-graduation
- Key projects (title, what you built, measurable outcome, evidence available?)

ACADEMIC RECORD (if applicable)
- Number of peer-reviewed publications (breakdown: journal vs conference)
- Top venues (if any) — journal names or conference names
- Total citation count (source: Google Scholar, Semantic Scholar, etc.)
- h-index (if known)
- Number of peer review invitations completed
- Any patents (granted or pending)

EVIDENCE INVENTORY
For each major claim, ask: what evidence do you have?
  - Objective evidence: company press releases, CEO/exec statements, official reports,
    measurable metrics, patents, published data, news coverage, government reports
  - Subjective evidence: reference letters from managers, collaborators, stakeholders,
    clients — note their title and affiliation

FIELD & NATIONAL INTEREST
- Primary field/domain
- Can you describe how your work connects to a U.S. national interest area?
  (e.g., national security, economic competitiveness, public health, energy,
   AI/STEM leadership, infrastructure, climate)
```

If the user provides a resume or CV, extract the above automatically and confirm.

---

## Step 0.5 — EB-2 Eligibility Gate (Hard Prerequisite)

USCIS evaluates EB-2 eligibility **before** the Dhanasar NIW analysis.
If this gate fails, the petition cannot proceed regardless of NIW strength.
Check this first. If it fails → verdict is NOT_QUALIFIED. Explain the specific
gap and provide a concrete path to eligibility.

**Advanced Degree route — confirm all:**
- [ ] Occupation requires at least a U.S. bachelor's degree (or equivalent)
  as a standard entry requirement — not just preferred
- [ ] Petitioner holds a relevant advanced degree (Master's, PhD, or equivalent
  foreign degree) OR a bachelor's plus 5+ years of **progressive** post-degree
  experience in the specialty
- [ ] If claiming experience in lieu of advanced degree: experience letters must
  explicitly state **"full-time"** — USCIS now rejects letters that document
  years without this phrase
- [ ] Advanced degree (or claimed experience) relates directly to the proposed
  endeavor — a mismatch is a standalone RFE trigger

**Exceptional Ability route (alternative to advanced degree) — confirm 3 of 6:**
1. Official academic record showing degree related to exceptional ability area
2. Letters documenting 10+ years of **full-time** experience in the occupation
3. License to practice the profession (where applicable)
4. Commanding salary evidencing exceptional ability relative to peers
5. Membership in professional associations requiring outstanding achievement
6. Recognition for achievements from peers, government, or professional organizations

**Critical rule:** Exceptional ability must relate to the **same endeavor**
as the NIW request. Mismatch = standalone RFE regardless of Dhanasar analysis.

**Membership evaluation (2024-2025 AAO guidance):**
- Memberships must be merit-based with selection by recognized national or
  international experts based on outstanding achievement — not paid subscriptions
- Memberships obtained primarily through payment of an annual fee are excluded,
  even if the organization appears prestigious
- General titles like "advisor," "faculty member," or "committee member" are
  employment roles, not qualifying memberships requiring outstanding achievement
- The level of membership must demonstrate the individual was judged by experts
  to have reached the top of their field (e.g., selection for a national athletic
  team qualifies because selection is performed by national-level judges)

If EB-2 gate fails → assign NOT_QUALIFIED, explain the specific gap, and
provide a concrete path to eligibility before reassessing NIW merits.

---

## Step 1 — Determine Qualification Pathway

There are three pathways. Evaluate which one(s) apply.

---

### Pathway A — Academic / Research Track

**Threshold (all must be met):**

| Criterion | Minimum Bar | Strong |
|---|---|---|
| Degree | Master's or PhD in relevant field | PhD preferred |
| Publications | 5+ peer-reviewed (journal + conference mix) | Top-venue papers = strong bonus |
| Citations | ~50+ from **independent sources** (exclude self-citations) | 100+ = strong; 200+ = very strong |
| Evidence | Google Scholar profile, published papers | ISI/Scopus indexing preferred |

**Elite venue exception:** 2-3 publications in top-tier venues (Nature, Science,
Cell, PNAS, NeurIPS, ICML, ICLR) with 200+ independent citations may satisfy
the threshold with fewer papers. USCIS applies holistic review — 5+ is a
reliable typical bar, not an absolute floor. Apply judgment.

**Bonus factors (add weight, not required):**
- First-authored papers in recognized journals (note impact factor if known)
- Papers cited by government reports, industry white papers, or standards bodies
- Peer review invitations completed (10+ adds credibility; not a standalone gate)
- Invited speaker, editorial board, conference program committee
- h-index >= 5 (rough threshold for emerging independent researcher)
- Open-source tools/datasets that others have adopted

**Disqualifiers / Red flags:**
- All publications in predatory journals (check against Beall's List heuristics)
- Self-citations account for majority of citation count
- No first-authored papers at all
- Publications outside the claimed field of national importance

---

### Pathway B — Professional / Industry Track

**Threshold (all must be met):**

| Criterion | Minimum Bar | Strong |
|---|---|---|
| Degree | Advanced degree OR Bachelor's + 5+ yrs post-grad experience | Advanced degree + experience = ideal |
| Experience | 3+ years in relevant professional role | 5+ years preferred |
| Project Quality | At least one project reframable to national importance | Multiple = stronger |
| Evidence (Objective) | At least one verifiable external source per major claim | Official company/govt source preferred |
| Evidence (Subjective) | Reference letter from manager or senior stakeholder | Senior title at credible org preferred |

**Project reframability test** (apply to each claimed project):
1. Can you name a concrete U.S. national interest this work advances?
   (Use: national security, economic competitiveness, public health, STEM workforce,
   energy independence, infrastructure resilience, fraud/crime prevention)
2. Is there a measurable outcome that can be cited?
   (e.g., "reduced fraud by X%", "secured X users", "saved $X", "processed X transactions")
3. Does objective evidence exist that confirms this outcome?
   (e.g., Chase CEO statement on biometric login reducing fraud — this is strong
   objective evidence even for a SWE; a LinkedIn post by the user is not)

**Examples of strong vs. weak evidence:**

| Claim | Weak Evidence | Strong Evidence |
|---|---|---|
| "My feature reduced fraud" | User's own LinkedIn post | CEO/exec press release citing fraud reduction metrics |
| "My model improved patient outcomes" | Internal slide deck | Peer-reviewed paper or hospital's published outcome report |
| "My work is widely used" | "Thousands of users" (unverified) | GitHub stars + downloads + company blog with numbers |
| "I led a critical project" | Job description | Manager reference letter with specific outcomes + org chart |

---

### Pathway C — Mixed / Hybrid Track

User has some publications AND some professional experience, but neither is
individually sufficient.

**Minimum combination for consideration:**
- 2–4 publications (at least 1 first-authored) + 25+ **independent** citations
  (exclude self-citations) AND 3+ years professional experience with 1
  reframable project with objective evidence
- OR strong professional track (5+ years, strong objective evidence) with
  1–2 publications that directly validate the professional work

**Pathway C is always LIKELY_QUALIFIED at best — never QUALIFIED.**
The portfolio must exceed the sum of its parts. If either the academic or
professional side is thin, assign BORDERLINE.

**Evaluation approach:**
- Treat as a portfolio — does the whole exceed the sum of the parts?
- Apply extra scrutiny to evidence quality; both sides must have real evidence
- If either side is thin (weak publications OR weak professional evidence),
  assign BORDERLINE — not LIKELY_QUALIFIED

---

## Step 1.5 — Quantifiable Outcomes Assessment (2024-2025 AAO Emphasis)

The AAO has sharpened its focus on quantifiable outcomes and strong economic
benefits. While significant economic impact is not strictly required by the
Dhanasar framework, providing quantifiable evidence is increasingly treated
as a **critical positive factor** in adjudication.

For each major claim or project, assess:
- Is there a quantifiable outcome? (dollar figure, % improvement, population served, users reached)
- Is the quantification sourced to a verifiable third party? (government report, employer press release, published study)
- Does the outcome demonstrate national-scale ripple effects beyond the immediate beneficiary?

**If the petitioner's case lacks quantifiable outcomes entirely:** Flag this as
a significant gap. In the current adjudication climate (~54% NIW approval rate
in 2025), a petition without quantifiable evidence faces substantially higher
RFE risk.

---

## Step 2 — Field Alignment Check

Regardless of pathway, the applicant's field must be alignable to a recognized
U.S. national interest priority area.

---

→ **Read `rubric/field_alignment.md`** for detailed tier examples, edge cases, and domain reframing guidance before evaluating field alignment.

### Critical Rule: AI (and similar technologies) are Methods, Not Domains

**AI, ML, deep learning, LLMs, data science, and similar technologies are tools.**
They do not carry national importance on their own. National importance lives in
the *application domain* — what problem is being solved, for whom, at what scale.

When a user claims "AI" as their field, always ask:
> "AI applied to *what*?"

Then evaluate the application domain, not the technology.

**Examples:**

| User Claims | Actual Domain | Verdict |
|---|---|---|
| "AI for public health / pandemic surveillance" | Public Health | ✅ Tier 1 — public health has its own national priority standing |
| "AI for semiconductor defect detection" | Semiconductor Manufacturing | ✅ Tier 1 |
| "AI for cybersecurity threat detection" | Cybersecurity | ✅ Tier 1 |
| "AI for drug discovery" | Biotechnology | ✅ Tier 1 |
| "AI for climate modeling" | Clean Energy / Climate | ✅ Tier 1 |
| "AI for fraud detection in banking" | Financial Security | ✅ Tier 2 — strong framing needed |
| "AI for crop yield prediction" | Agriculture / Food Security | ✅ Tier 2 |
| "AI for personalized marketing" | Marketing | ❌ Tier 3 — marketing has no independent national importance standing |
| "AI for content recommendation" | Consumer AdTech | ❌ Tier 3 |
| "AI for fashion trend prediction" | Retail / Consumer | ❌ Tier 3 |
| "Machine learning research" (no application) | None identified | ❌ Insufficient — must anchor to a domain |

**The same logic applies to:** data science, cloud computing, blockchain,
cybersecurity tools, robotics, NLP, computer vision. Strip the technology
label and ask: what domain does this serve?

**Edge case — Foundational AI/CS Research:**
If the user's work is genuinely foundational (e.g., new training algorithms,
model architectures, safety alignment research) and is field-agnostic by nature,
this *can* qualify under AI/STEM leadership — but only if:
- Published in top venues (NeurIPS, ICML, ICLR, Nature, Science, etc.)
- Work is cited or adopted by others across multiple domains
- Strong evidence of broader research impact (not just one company's use)

Without these, "foundational AI research" is not sufficient on its own.

---

### Field Alignment Tiers

**Tier 1 — Explicitly listed in NSTC/White House priority areas (strongest):**
- Semiconductor / Microelectronics
- Cybersecurity / Critical Infrastructure Protection
- Biotechnology / Public Health / Pandemic Preparedness
- Clean Energy / Climate Technology
- Quantum Information Science
- Advanced Manufacturing
- Space Technology
- STEM Education / Workforce Pipeline
- Foundational AI/CS Research (with evidence bar above — not AI-as-tool)

**Tier 2 — Recognized national interest, requires stronger evidence and framing:**
- Financial security / fraud prevention / systemic risk
- Transportation safety / Autonomous systems
- Agriculture / Food security
- Supply chain resilience
- Drug safety / Pharmaceutical research
- Education technology tied to workforce or equity outcomes
- Environmental monitoring / disaster response

**Tier 3 — Hard to justify; evidence and framing must be exceptional:**
- Marketing / AdTech (even AI-powered)
- Consumer product optimization
- Entertainment / Media (unless specifically disinformation, IP protection, or accessibility)
- Retail / E-commerce
- Social media engagement optimization
- General business intelligence / analytics without public benefit argument

**If Tier 3:** Flag explicitly —
> "The application domain is the weakest part of this case. Technology alone
> (e.g., using AI or ML) does not elevate a Tier 3 domain. The user must
> either reframe toward a Tier 1–2 domain or demonstrate exceptional evidence
> of public benefit that is not typical of this industry."

**If no domain can be identified at all:** Verdict is NOT_QUALIFIED on field
alignment regardless of academic or professional strength.

---

## Step 3 — Evidence Quality Scoring

For each major claim, score evidence quality:

| Score | Label | Description |
|---|---|---|
| 3 | Strong | Objective, verifiable, third-party source with specifics |
| 2 | Moderate | Objective but general, OR subjective but senior/credible source |
| 1 | Weak | Self-reported, internal-only, vague, or unverifiable |
| 0 | Missing | No evidence identified |

**Rule:** Any criterion with a score of 0 is a blocking gap.
Any criterion with avg score < 1.5 across its evidence is a significant gap.

**2024-2025 AAO evidence scoring updates:**

- **Patents:** A patent without evidence of licensing, commercial application,
  or adoption by others scores **Moderate (2)** at best, not Strong. The AAO
  has affirmed that a patent alone, without evidence of its significance to the
  field, is insufficient to prove "major significance."

- **Research grants:** Grants are for funding work and do **NOT** count as
  prizes or awards for excellence. Score grants as Moderate (2) for evidence
  of project viability, but never as evidence of recognition or achievement.

- **Published material / media coverage:** Must constitute substantial
  discussion "about" the petitioner specifically — not passing mentions,
  citations of their work, or articles about the broader field. A journal
  article that mentions the petitioner's work in passing does not qualify
  as published material "about" the petitioner. Score passing mentions as
  Weak (1); substantial profiles or features as Strong (3).

- **Citation counts:** Citations alone, without evidence of real-world impact
  or independent expert validation, are increasingly insufficient. Pair
  citation evidence with expert testimonials or documented adoption for
  Strong (3) scoring.

---

## Step 4 — Assign Qualification Verdict

Based on pathway(s) met, field alignment tier, and evidence scores:

| Verdict | Meaning |
|---|---|
| **QUALIFIED** | Meets threshold on primary pathway, Tier 1–2 field, evidence scores mostly 2–3. Proceed to NIW_Endeavor. |
| **LIKELY_QUALIFIED** | Meets most criteria, has addressable gaps. Proceed with caution — note conditions. |
| **BORDERLINE** | Meaningful gaps in evidence or criteria. Can proceed only if gaps can be addressed before filing. List exactly what is needed. |
| **NOT_QUALIFIED** | Does not meet threshold on any pathway, OR critical evidence is missing or fraudulent. Do not proceed. Provide honest gap analysis and timeline to qualify. |

**Conservative rule:** When in doubt between two tiers, assign the lower one.
NIW rejections are costly — underselling a strong case is recoverable;
overselling a weak case wastes years and filing fees.

---

## Step 5 — Output

Produce a structured evaluation report conforming to `schema/output_schema.json`.
The schema file is authoritative — this template summarizes the required fields:

```json
{
  "applicant": {
    "name": "",
    "pronoun": "she/her | he/him | they/them",
    "degree": "PhD | Master of Science | ...",
    "field": "",
    "university": "",
    "year_degree": "",
    "years_experience": 0,
    "current_title": "",
    "current_employer": ""
  },
  "pathway": "A | B | C | None",
  "field_alignment_tier": "1 | 2 | 3 | None",
  "application_domain": "Actual domain stripped of technology labels",
  "verdict": "QUALIFIED | LIKELY_QUALIFIED | BORDERLINE | NOT_QUALIFIED",
  "strengths": [
    { "description": "Specific strength", "evidence_reference": "Source" }
  ],
  "gaps": [
    {
      "criterion": "Name of criterion",
      "current_state": "What they have",
      "required_state": "What is needed",
      "evidence_score": 0,
      "how_to_address": "Concrete action to close this gap",
      "blocking": true
    }
  ],
  "evidence_inventory": [
    {
      "claim": "Claim being evidenced",
      "objective_evidence": ["list"],
      "subjective_evidence": ["list"],
      "score": 0,
      "notes": "Any caveats on evidence quality"
    }
  ],
  "academic_metrics": {
    "publication_count": 0,
    "journal_count": 0,
    "conference_count": 0,
    "first_authored": 0,
    "citation_count": 0,
    "h_index": null,
    "peer_review_count": 0,
    "top_venue_papers": [],
    "citation_source": "Google Scholar | Semantic Scholar | Scopus"
  },
  "recommended_pillars_preview": [
    { "title": "Pillar title (5-10 words)", "rationale": "1-2 sentences" }
  ],
  "conditions_to_proceed": [],
  "field_alignment_notes": "Domain identification and tier assignment reasoning",
  "evaluator_notes": "Honest narrative. Flag thin areas, reframing risks, India/China backlog if applicable."
}
```

**Note on key fields:**
- `blocking: true` on any gap overrides a QUALIFIED verdict — address it first
- `academic_metrics` is populated for Pathway A or C; set to `null` for Pathway B
- `conditions_to_proceed` lists specific actions required before vera-niw-endeavor

---

## Step 6 — Communicate Results to User

After producing the JSON internally, present results to the user as:

1. **Verdict** (one clear line)
2. **Why** — top 3 strengths and top 3 gaps in plain English
3. **What's needed** — if BORDERLINE or NOT_QUALIFIED, a concrete action list with realistic timelines
4. **Honest risk note** — if proceeding despite gaps, state the risk plainly. Do not sugarcoat.
5. **Next step** — if QUALIFIED or LIKELY_QUALIFIED, confirm readiness to proceed to vera-niw-endeavor

**Tone:** Honest, direct, supportive. This person's immigration future may depend
on this assessment. Neither overpromise nor discourage unfairly.

**Always include in evaluator_notes when applicable:**
- **India/China backlog:** If petitioner is born in India or China, flag EB-2
  visa bulletin backlog explicitly. An approved I-140 ≠ visa availability. The
  EB-2 queue for India can be 10+ years; for China, several years. Filing
  strategy differs — EB-1A consideration, AC21 portability, NIW as a long-term
  hedge. Do not present I-140 approval as the finish line.
- **BORDERLINE/NOT_QUALIFIED roadmap:** Give a realistic timeline — months
  needed for citations to accumulate, peer reviews to complete, or objective
  evidence to become available. Reframe as a roadmap, not a rejection.
- **2025 approval rate context:** NIW approval rates have dropped to
  approximately 54% in 2025, while EB-1A rates remain more stable at ~74%.
  This heightened scrutiny makes the conservative evaluation stance more
  important than ever. Note this context when the case is BORDERLINE.
- **Creative professionals / artists:** The mere act of displaying artwork,
  performing, or exhibiting creative work is NOT sufficient. The AAO requires
  evidence of significant recognition, critical acclaim, or notable audience
  engagement. Exhibitions without critical reviews in major publications,
  commercial success metrics, or documented audience impact are insufficient.
- **Researchers — citations alone insufficient:** Citation counts without
  evidence of real-world impact beyond academia (licensing, commercial
  application, government adoption, practitioner use) are increasingly
  insufficient for Prong 2. The AAO has dismissed cases where citation
  records were presented without evidence of broader significance.
- **EB-1A misapplication risk:** If the petitioner's profile is academic-heavy,
  flag the documented trend of officers incorrectly applying EB-1A standards
  to NIW cases and recommend preemptive Dhanasar framing in the petition.

---

## Step 4.5 — EB-1A Misapplication Risk Assessment (2024-2025 Trend)

A documented trend in 2024-2025: some USCIS officers incorrectly demand that
EB-2 NIW petitioners meet the higher EB-1A "extraordinary ability" standard.
This includes requiring proof of being at the "top of the field" or having
made "original contributions of major significance" — standards that apply
to EB-1A, not EB-2 NIW under Dhanasar.

**Assessment:** After assigning the verdict, evaluate whether the petitioner's
case is vulnerable to this misapplication:

- **HIGH RISK:** Petitioner is a researcher or academic whose case relies
  heavily on publications and citations. Officers may default to EB-1A
  criteria when reviewing academic profiles.
- **MEDIUM RISK:** Petitioner works in a technical field (engineering, CS,
  data science) where "original contributions" language is commonly used.
- **LOW RISK:** Petitioner's case is clearly industry-focused with business
  evidence, contracts, and deployment metrics.

**If HIGH or MEDIUM risk:** Add to `evaluator_notes`:
> "This case may be vulnerable to EB-1A standard misapplication. Recommend
> including preemptive language in the petition explicitly establishing the
> Dhanasar three-prong framework as the applicable standard, citing Matter
> of Dhanasar, 26 I&N Dec. 884 (AAO 2016) and the USCIS Policy Manual.
> Do not use language that mirrors EB-1A criteria (e.g., 'original
> contributions of major significance,' 'top of the field,' 'extraordinary
> ability'). If an RFE applies EB-1A standards, respectfully but firmly
> rebut — failing to challenge misapplication increases denial risk."

---

## Evaluation Heuristics (Additional — Claude's Judgment)

Apply these when the rubric alone is ambiguous:

- **Innovation vs. Implementation test (2024-2025 AAO priority)**: Is the
  petitioner proposing to create something genuinely new — a new process,
  product, methodology, or system — or merely implementing existing technology?
  The AAO has dismissed petitions where the proposed endeavor was to implement
  or install existing solutions rather than develop new ones. Examples:
  - DISMISSED: Engineer proposing sustainable energy upgrades using existing
    practices — implementation, not innovation
  - DISMISSED: IT consultant installing known cybersecurity measures — no
    evidence of solutions that are "different, better, or less costly than
    current U.S. services"
  - PASSES: Developing a new detection algorithm, creating a novel framework,
    building a system that offers advances beyond what is currently available
  If the petitioner's work is primarily implementation, flag it as a
  **blocking gap** for Prong 1. The endeavor must offer something beyond
  what is currently available on the market.

- **Substitutability test**: Could any qualified engineer/researcher do what this
  person does? If yes, the NIW argument is weak. The work should require *this
  specific person's* unique combination of skills and experience.

- **Scale test**: Does the work affect hundreds, thousands, or millions of people?
  NIW favors national-scale impact over local or company-internal impact.

- **Independence test**: Can the applicant continue this work without being tied
  to one employer? Self-directed research, open-source work, and consultancy
  strengthen the case vs. work that only existed because of one company's needs.

- **Urgency test**: Is there a reason the U.S. needs this person *now*?
  Emerging fields (AI, biosecurity, quantum) carry more urgency than mature fields.

- **The Chase Biometrics Example (model case):**
  SWE at Chase built biometric login → reduces fraud → Chase CEO stated fraud
  reduction metrics publicly → manager reference letter confirms her role.
  This is a strong Pathway B case because: (1) the project is clearly reframable
  to national economic/security interest; (2) objective evidence is a credible
  third-party source (CEO press release); (3) subjective evidence names her
  specifically. The field (fintech security) is Tier 2, so evidence quality
  must be high — and it is.

---

## Evals

See `evals/evals.json` for test cases.
