---
name: vera-niw-endeavor
description: >
  Guides NIW applicants through brainstorming and crystallizing their proposed
  endeavor — the single most important element of an NIW petition and the #1
  RFE trigger when done wrong. Transforms raw expertise into a specific, named,
  bounded undertaking that passes USCIS scrutiny under the Dhanasar framework.

  Always produces TWO mandatory outputs together: (1) a petition-ready proposed
  endeavor statement (3-5 sentences, third person, all pattern checks passed),
  and (2) three named NIW pillars with rationale, structured as direct input
  for NIW_Pillar. Both outputs are always delivered together, never omitted.

  ALWAYS use this skill when the user:
  - Asks "what should my proposed endeavor be?" or "how do I define my endeavor"
  - Has a draft endeavor that feels vague or job-description-like
  - Says they got an RFE citing vague or broad endeavor description
  - Has completed NIW_Evaluate and is ready to move to drafting
  - Mentions NIW petition planning, endeavor statement, or Prong 1 strategy
  - Asks "is my NIW endeavor good enough?" or "can you help me refine my endeavor"

  Use even if the user already has a draft endeavor -- run the diagnostic first.
  Part of the NIW Petition Skill System.
---

# Vera NIW Endeavor

The proposed endeavor is the spine of the entire NIW petition. Every argument
in every pillar, every recommender quote, and the Prong 3 balance test all flow
from a well-defined endeavor. A weak endeavor doesn't just fail Prong 1 — it
collapses the whole petition.

The most common failure: describing a job. USCIS explicitly states that
"an occupation and the general work performed in an occupation does not
constitute an endeavor." A valid endeavor is a specific, named, bounded
*undertaking* with a defined goal, a named method, and a measurable national
outcome. This skill builds that.

---

## Entry Point Detection

Before doing anything else, determine how the user is arriving:

**Route A — Has NIW_Evaluate output:**
User provides a JSON block from the NIW_Evaluate skill (or describes their
verdict + pillar previews). Extract the `recommended_pillars_preview` field
— these are pre-validated seeds. Skip to Phase 2 (Ingredient Interview),
pre-populating what you already know.

**Route B — Starting fresh:**
No prior evaluation. Proceed through all four phases. Conduct the full
ingredient interview before drafting anything.

**Route C — Has a draft endeavor to diagnose:**
User provides an existing endeavor statement. Go directly to Phase 1
(Diagnose), score it, then proceed to Phase 2 to address what's missing.

---

## Phase 1 — Diagnose (skip if no draft exists)

If the user has an existing endeavor statement, score it before anything else.
Run the three USCIS failure patterns as a rapid triage:

**Pattern A — Occupation test:**
> Is this describing a job/role, or a specific undertaking?
- FAIL: "work as a software engineer," "continue my research," "apply AI to X"
- PASS: Named project/system/framework with a specific goal

**Pattern B — Specificity test:**
> Could this statement describe any competent professional in the field?
- FAIL: Endeavor is field-level ("advance AI in healthcare") or domain-level
- PASS: Only this person's specific project fits this description

**Pattern C — National scope test:**
> Does national importance come from the field, or from this specific work?
- FAIL: Argues importance of the field/technology
- PASS: Named federal program, quantified national-scale outcome, CET alignment

**Substitutability test:**
> Could any qualified person at the same institution/company do this?
- FAIL: Routine professional work any competent peer could perform
- PASS: Requires this specific person's unique combination of expertise

**Pattern D — Innovation vs. Implementation test (2024-2025 AAO priority):**
> Is this proposing to create something genuinely new, or to implement/install
> existing technology?
- FAIL: Standard energy-efficient upgrades, installing known cybersecurity
  measures, applying existing ML models to routine problems, deploying
  off-the-shelf solutions
- PASS: Developing new processes, products, or methodologies that offer
  advances beyond what is currently available on the market; creating
  solutions that are "different, better, or less costly than current
  U.S. services"

The AAO has repeatedly dismissed petitions in 2024-2025 where the proposed
endeavor was implementation rather than innovation. This is now a top-tier
failure mode alongside Pattern A (Occupation ≠ Endeavor).

Score each: ✅ Pass / ⚠️ Weak / ❌ Fail

If all four pass → proceed to Phase 3 (Draft) to polish.
If any fail → identify which ingredients are missing → proceed to Phase 2.

---

## Phase 2 — Ingredient Interview

Gather the 6 required ingredients. Ask for missing ones explicitly.
Do not draft without them. One question at a time — don't overwhelm.

> **→ Read `references/endeavor-anatomy.md`** for the full ingredient
> definitions, examples of strong vs. weak answers, and rewrite templates
> for common failure modes.

**Ingredient 1 — Named project or initiative**
> "What do you call your work? Not your job title — the specific project,
> system, tool, or research program. If it doesn't have a name yet, that's
> okay — we'll name it together."
- Looking for: a proper noun-level identifier (TGADF, MedNLP-Verify, the
  PharmacovigilanceNLP Suite, not "my research" or "my AI system")

**Ingredient 2 — The specific national-scale problem**
> "What specific problem does your work address, and how big is it nationally?
> Dollar figure, population affected, or documented failure rate preferred."
- Looking for: a named, quantified gap — not "healthcare is important" but
  "1.5 million preventable medication errors annually (IOM, HHS 2022)"
- If they give a field-level problem, ask: "What specifically fails without
  your approach that currently exists? What's the gap?"

**Ingredient 3 — Named methodology**
> "How does your approach work — specifically? Name the method, model, or
> technique. Not 'machine learning' but 'transformer-based named entity
> recognition' or 'survival analysis using Cox proportional hazards models.'"
- Looking for: a named, non-generic technique that signals expertise
- If they say "AI" or "machine learning," press: "What specific architecture,
  algorithm, or framework? What makes it distinct from what already exists?"

**Ingredient 4 — Application domain and national interest tier**
> Check `references/field-alignment.md` to classify the domain.
> If the user claims AI/ML/data science as their field, apply the
> "AI is a method, not a domain" rule: ask what the AI is applied to.
- Target: Tier 1 or Tier 2 domain with a named government priority
- If Tier 3: flag it directly — "This domain as described is difficult to
  justify for NIW. Here are two ways to reframe toward a stronger anchor..."

**Ingredient 5 — Measurable national-scale outcome with broader implications**
> "If your work fully succeeds, what changes in the U.S. at national scale?
> Give me a number — a dollar figure, a population served, a % improvement,
> or a federal program advanced. And critically: how do those positive effects
> *ripple* beyond the immediate beneficiary?"
- Looking for: "reduces X by Y%," "serves Z million patients," "addresses
  $Xbn federal initiative," not "improves patient care"
- **Broader implications requirement (2024-2025 AAO emphasis):** The AAO now
  explicitly looks for how the endeavor's positive effects ripple across
  the United States — not just direct impact on one employer or one client.
  Push the user to articulate second-order and third-order effects:
  e.g., "This tool reduces hospital readmissions → saving $X billion in
  Medicare costs → freeing resources for underserved populations nationwide."
- While quantifiable economic impact is not strictly required by Dhanasar,
  providing such evidence is increasingly treated as a **critical positive
  factor** in adjudication. In the current ~54% approval rate environment,
  petitions without quantifiable outcomes face substantially higher RFE risk.

**Ingredient 6 — The substitutability answer**
> "Why you specifically? What do you bring to this that a qualified peer at
> your institution or company cannot? What's the unique combination?"
- Looking for: specific publications, patents, deployed systems, or
  methodological contributions that belong uniquely to this person
- This becomes the "well-positioned" thread that runs through Prong 2

**Ingredient 7 — U.S. operational presence and intent (2024-2025 AAO trend)**
> "What evidence do you have of your intent and ability to pursue this
> endeavor in the United States? Do you have a U.S. business entity,
> contracts with American clients, letters of interest from U.S.
> organizations, or other concrete U.S.-based operational evidence?"
- Looking for: U.S. business incorporation (LLC, Corp), signed contracts
  with American clients, letters of interest from leading U.S. organizations,
  active U.S. collaborations, or a documented U.S. research program
- The AAO remanded a 2024 denial (In Re: 31109123) specifically because
  the petitioner proved U.S. business incorporation and active American
  contracts — these established clear intent to work in the U.S.
- For entrepreneurs/self-employed: U.S. incorporation + client contracts
  are now among the strongest evidence for both intent and Prong 2
- For researchers: active U.S. institutional affiliation, grant funding
  from U.S. agencies, or collaboration agreements with U.S. entities
- This ingredient is not strictly required for all petitioners but
  **significantly strengthens** any case, especially for Prong 2 and
  when the petitioner's U.S. presence is questioned

---

## Phase 3 — Draft Candidate Statements

Once all 6 ingredients are collected, generate **2 candidate endeavor
statements** — narrow and broad — so the user can see the spectrum and choose
the right level of specificity for their case.

**Narrow candidate:** Maximum specificity. Names the exact project, exact
problem, exact method, exact federal anchor, and exact measurable outcome.
Best when the petitioner has strong, specific evidence. Stronger for RFE
response.

**Broad candidate:** Slightly wider scope — covers the project plus its
downstream applications or a family of related initiatives. Useful when
the evidence base spans multiple projects that share a common thread.

**Endeavor statement structure** (follow this pattern for both):

> [Petitioner]'s proposed endeavor is to [develop/deploy/build] [NAMED
> PROJECT] — [one-sentence description of what it does and how (named
> method)] — to address [SPECIFIC NATIONAL-SCALE PROBLEM] affecting
> [QUANTIFIED POPULATION OR SCALE]. This work directly advances [NAMED
> FEDERAL INITIATIVE/CET AREA] by [SPECIFIC CAUSAL MECHANISM]. [Petitioner]
> is uniquely positioned to lead this endeavor through [SPECIFIC EVIDENCE
> OF PRIOR CONTRIBUTION].

**Tone rules:**
- Third person throughout
- No hedging ("may," "could potentially," "aims to")
- Present tense for ongoing work, past for completed
- 3–5 sentences maximum — dense, not padded

---

## Phase 4 — Stress-Test and Finalize

Run the USCIS patterns on the drafted statements before presenting them.
If either candidate fails a pattern, fix it before showing the user.

**Self-check before presenting:**
- [ ] No job title or role description in the endeavor
- [ ] Endeavor is specific enough that it could not apply to any peer
- [ ] National importance anchored to a named program, not the field generally
- [ ] Named methodology (not "advanced AI" or "novel approach")
- [ ] Measurable national-scale outcome stated
- [ ] Federal government connection present (agency, act, or program named)
- [ ] No hedging language
- [ ] Passes substitutability test — "only this person" logic is visible
- [ ] Endeavor proposes innovation/creation, not implementation of existing solutions (Pattern D)
- [ ] Broader implications articulated — ripple effects beyond immediate beneficiary
- [ ] No EB-1A language used ("original contributions of major significance," "top of the field," "extraordinary ability")

If any check fails: fix the candidate statement before presenting, or flag
what additional information is needed to address the gap.

---

## Output Format

This skill always produces both outputs below — they are delivered together,
never separately. Do not finalize a session without both.

Present the final output in this exact structure:

---

**PROPOSED ENDEAVOR — [Applicant Name]**

---

**OUTPUT 1 — Endeavor Statement:**

> [3–5 sentence petition-ready statement in third person. Must name the
> specific project, the national-scale problem, the named methodology,
> the federal anchor, and the substitutability claim.]

---

**Pattern Check:**

| Check | Result | Note |
|---|---|---|
| Named undertaking (Pattern A) | ✅/⚠️/❌ | [brief note] |
| Specific to this person (Pattern B) | ✅/⚠️/❌ | [brief note] |
| National scope anchored (Pattern C) | ✅/⚠️/❌ | [named federal anchor] |
| Substitutability test | ✅/⚠️/❌ | [why this person, not any peer] |
| Measurable national outcome | ✅/⚠️/❌ | [the outcome stated] |

**Overall endeavor strength:** [STRONG / ADEQUATE / NEEDS WORK]

If any check is ❌, fix the statement before proceeding to Output 2.

---

**OUTPUT 2 — Three NIW Pillars:**

Each pillar is a distinct dimension of the endeavor that becomes one full
section in the NIW petition letter, written by NIW_Pillar. Every session
ends with exactly three pillars defined.

**Pillar 1: [Title]**
- **What it covers:** [1 sentence — the specific contribution this pillar documents]
- **National importance anchor:** [named federal program, CET area, or quantified national problem]
- **Evidence base:** [the specific work products, publications, or deployments that support this pillar]
- **Why it works as a NIW pillar:** [1 sentence — what makes this non-routine and nationally important]

**Pillar 2: [Title]**
- **What it covers:** [same format]
- **National importance anchor:** [same format]
- **Evidence base:** [same format]
- **Why it works as a NIW pillar:** [same format]

**Pillar 3: [Title]**
- **What it covers:** [same format]
- **National importance anchor:** [same format]
- **Evidence base:** [same format]
- **Why it works as a NIW pillar:** [same format]

---

**Next step:** Pass the endeavor statement and all three pillar definitions
to NIW_Pillar. Run NIW_Pillar once per pillar, providing the full endeavor
statement and the titles of all three pillars as context for each run.

---

## Brainstorming Heuristics

Apply these when the user is stuck or the ingredients are thin:

**The "newspaper test":** Could a journalist write a 2-sentence news story
about this work's national impact? If not, the endeavor lacks the scale and
specificity needed. Help them find the angle that clears that bar.

**The "elevator to a senator" test:** If the petitioner had 30 seconds in
an elevator with a senator from the relevant committee, could they explain
why the federal government should care about their specific project? If not,
the national importance argument isn't there yet.

**The "field without me" test:** Ask the user — "If you left the U.S. tomorrow
and no one else continued this specific work, what specific national-scale
problem would go unaddressed that is currently being addressed?" If they can't
answer, the uniqueness and substitutability argument needs work.

**The naming drill:** If the project doesn't have a name yet, push for one.
Named initiatives (TGADF, MedNLP-Verify, the FraudNet Framework) feel like
real undertakings to officers. Unnamed projects feel like job duties. Naming
is not vanity — it is a structural signal.

**The anchor drill:** For every national importance claim, ask: "Is there a
federal report, an executive order, a piece of legislation, or a named agency
program that explicitly identifies this problem as a national priority?" If
yes, name it. If no, this is the most important gap to fill.

---

## Common Reframe Patterns

When the user's work is in a weak-framing domain, these pivots often work:

| User's initial framing | Stronger reframe |
|---|---|
| "I do AI research" | Identify application domain → Tier 1/2 anchor |
| "I work in cybersecurity" | → "I develop [named tool] for [specific infrastructure threat] affecting [N] critical systems designated under CISA's [program]" |
| "I improve healthcare processes" | → "I build [named system] that reduces [specific adverse outcome] in [population] — a gap costing [figure] annually per [source]" |
| "I do financial modeling" | → "I develop [named framework] for [systemic risk type] — risks documented in [named federal report] affecting [scale]" |
| "I research drug safety" | → "I build [named pipeline] to detect [specific signal type] in [data source], directly advancing FDA's [program] by [mechanism]" |

---

## What This Skill Does NOT Do

- Generate full pillar content → use NIW_Pillar
- Evaluate whether the user qualifies → use NIW_Evaluate
- Review a completed petition for RFE risk → use vera-niw-pl-review
- Write recommendation letters → use NIW_Recommendation (when available)
