---
name: vera-niw-recommendation
description: >
  Drafts a complete NIW reference letter from a recommender's perspective.
  Supports three letter types: (A) Methodology — praises technical innovation;
  (B) Domain Application — describes real-world impact in the recommender's
  field; (C) Hybrid — methodology innovation + domain application together.
  Input includes the proposed endeavor, the target pillar, and full details
  about the recommender and their relationship to the petitioner's work.
  Output is a signed, publication-ready reference letter in formal legal-academic
  tone. Part of the NIW Petition Skill System.
---

# NIW Recommendation Letter Skill

Generates a complete, publication-ready NIW reference letter.
One letter per recommender. Each letter is written entirely from the
recommender's first-person perspective.

---

## Step 1: Determine the Letter Type

Before writing, identify which type of letter this should be:

### Type A — Methodology Letter
**Use when:** The recommender is an expert in the same technical/methodological
field. They understand the innovation at a technical level and can validate
that it is a genuine advance over existing approaches.

**Focus:** What problem existed in the field, what the existing approaches
couldn't do, exactly how the petitioner's method solved it, and why this
is a theoretical breakthrough. Named model/method acronyms, journal names,
before/after framing.

**Best recommender profile:** Academic researcher, professor, or scientist
in the same or closely adjacent methodology field. Ideally: read the paper,
used the code, or extended the work.

---

### Type B — Domain Application Letter
**Use when:** The recommender is a practitioner or researcher in the
application domain. They encountered the petitioner's work because it solved
a real problem they faced. They can validate real-world impact with specifics.

**Focus:** The specific application, the problem that couldn't be solved
before, how the petitioner's method was applied, and the concrete measurable
outcome. Named clinical procedures, named companies, named patient populations,
dollar figures, policy connections.

**Best recommender profile:** Clinician, industry executive, policy expert,
regulator, or applied researcher. Met the petitioner at a seminar or through
their published work/open-source tool.

---

### Type C — Hybrid Letter
**Use when:** The recommender has both methodological expertise and experience
applying the work. Covers the technical innovation AND real-world impact.
Usually used when fewer recommenders are available and one letter must serve
both purposes.

**Structure:** Methodology section first (2-3 contributions), then application
section (2-3 specific examples).

---

## Step 2: Inputs Required

Collect ALL of the following before writing. If anything is missing, ask.

```
PROPOSED_ENDEAVOR     Full text of proposed endeavor
TARGET_PILLAR         The pillar this letter supports (title + description)
PETITIONER_NAME       Full name and title (e.g., Dr. Jin Liu)
PETITIONER_PRONOUN    she/her | he/him | they/them

RECOMMENDER_NAME      Full name (e.g., Dr. James Richardson)
RECOMMENDER_TITLE     Current title
RECOMMENDER_INSTITUTION  Current institution
RECOMMENDER_BACKGROUND   PhD institution + field + past positions
RECOMMENDER_CREDENTIALS  Research focus, grants, publications summary
RECOMMENDER_INDEPENDENCE How they are independent:
                          - Never collaborated
                          - Different departments (if same employer)
                          - Found work through literature / at conference
                          - Became aware through scholarly impact
HOW_THEY_DISCOVERED   Exactly how they found the petitioner's work:
                          - Read a specific paper
                          - Attended a seminar/presentation
                          - Requested code for their own research
                          - Cited by a colleague
                          - Found on GitHub/SSRN
LETTER_TYPE           A (methodology) | B (application) | C (hybrid)

CONTRIBUTIONS         List of 2-4 specific contributions to highlight:
  For Type A:
    - What existed before (named prior approach + its limitation)
    - What the petitioner did specifically (named method/model)
    - What it enables now that wasn't possible before
    - How the recommender personally validated or used the work

  For Type B:
    - The specific problem in the recommender's domain
    - How they encountered the petitioner's work
    - Specific application with concrete outcome (numbers required)
    - Any additional applications they know of

FEDERAL_NATIONAL_HOOK  Named federal initiative, policy, or scale stat
                       (e.g., Precision Medicine Initiative, NIH, NSF,
                        SEC, FINRA, CHIPS Act, 47 million jobs, etc.)

SPECIFIC_QUOTES        Any real quotes from the recommender about the work
                       (if already collected — otherwise Claude drafts them)

CLOSING_STRENGTH       "strongest recommendation" | "strongest possible recommendation"
                       | "irreplaceable figure" | custom

PILLAR_RECOMMENDER_GUIDANCE  [OPTIONAL] The recommender profile block generated
                             by vera-niw-pillar Section 6 for this recommender.
                             If provided, pre-populate CONTRIBUTIONS and KEY_CLAIMS
                             from it — do not ask the user to re-enter what the
                             pillar skill already generated. The profile block
                             contains: ideal profile, independence requirements,
                             4 key claims to include, and what makes this letter
                             distinctive. Use it as the starting scaffold and ask
                             only for what it doesn't already specify.
```

---

## Step 3: Letter Structure

Write the letter in the following structure, exactly.
All sections are in **first person from the recommender's perspective.**

---

**[Please insert date of signature and letterhead]**

RE: [Petitioner Name]'s Independent Reference Letter
*(omit "Independent" if recommender is advisor or close collaborator)*

Dear Immigration Officer, / To Whom It May Concern,

---

### Paragraph 1 — Opening + Who I Am + Independence + How I Discovered the Work

Open with the recommender's strongest statement of support (1 sentence).
Then: full name, current title, current institution.
Then: academic background (PhD institution, field).
Then: brief credentials (research focus, grants if notable, publications if notable).
Then: independence statement — be explicit. Use one of these framings:
  - "I have never worked or collaborated with [name] in any fashion."
  - "While we are both at [institution], we work in entirely different departments
    and have never collaborated."
  - "[Name] and I have no professional or personal relationship."
Then: how they discovered the work — be specific:
  - "I started to follow [pronoun] work after reading [specific paper title]"
  - "I met Dr. [name] at [conference] when [pronoun] presented [specific topic]"
  - "I encountered [pronoun] work through its impact in my field and subsequently
    requested [pronoun] statistical code to advance my own research"

---

### Paragraph 2 — My Credentials (Why I Am Qualified to Assess This Work)

2-3 sentences establishing why the recommender can evaluate the petitioner's
contributions. Connect recommender's research focus to the petitioner's domain.
If the recommender's own work was extended or used by the petitioner, introduce
that here (develops naturally into the next section).

---

### [METHODOLOGY SECTION — Type A and C only]

### Paragraph 3 — The Problem in the Field (Before the Petitioner's Work)

Establish what the state of the art was BEFORE the petitioner's contribution.
Name the prior approach. Name its specific limitation. Write in plain language
that a USCIS officer can understand, not just specialists.

Pattern: "Prior to Dr. [name]'s work, [the standard approach] was [X].
However, [limitation of existing approach]. As a result, [consequence
for the field/practice]."

---

### Paragraphs 4–6 — Specific Contributions (2-4, each its own paragraph)

For each contribution:

**Before/After Structure:**
- What was the specific problem or limitation?
- What exactly did the petitioner do? (name the method, model, tool)
- What does it enable now? (name the specific capability)
- How has it been used? (by whom, in what context, with what result)

**Naming requirements:**
- Name the method/model (even acronyms: BLSGM-TICs, DiD, NLP pipeline)
- Name the journal it appeared in, with ranking if notable
- Name any named statistics or published results
- Name any federal policy, initiative, or program connection

**For Type A specifically:** Use the "as the original developer of X, I can
confirm that Dr. [name] solved a limitation I could not" framing if applicable.
This is the most powerful validation available.

---

### [APPLICATION SECTION — Type B and C only]

### Paragraph — Context: The National/Domain Problem

Establish why this domain problem matters at national scale.
Reference a named federal initiative, policy, or large-scale statistic.
This is the bridge between the recommender's personal encounter and
why it matters for the U.S. national interest.

Example: "Since the Obama administration launched the Precision Medicine
Initiative, precision medicine has gained increasing recognition by patients,
physicians, pharmaceutical companies, healthcare systems, and regulatory agencies."

---

### Paragraphs — Specific Applications (2-4, each its own paragraph)

For each application:
- The specific clinical/business/regulatory problem
- How the petitioner's method was applied (name the tool or model)
- The concrete outcome — with a number if at all possible
  ("almost one million knee replacement surgeries annually, ~200,000 non-responders per year")
- Why this matters beyond the immediate case (generalizability, policy, scale)

The best application paragraphs read as: "Here was a problem we couldn't solve.
Dr. [name]'s tool let us solve it. Here is exactly what happened. Here is why it matters."

---

### Final Paragraph — Closing Recommendation

2-3 sentences. Must include:
- The explicit "strongest recommendation" phrase
- A statement of national/global benefit
- Invitation to contact for further questions

Examples of strong closings:
- "I would like to express my strongest recommendation and full support for
  Dr. [name]'s petition for these reasons."
- "Dr. [name] is an irreplaceable figure in our shared field, and [pronoun]
  stay in the United States will help [pronoun] to continue [pronoun] research.
  Please contact me should you require any additional information."
- "As a [title] having extensive expertise from [domain], I believe it is a
  fortune for the U.S. and global [field] community to have Dr. [name] continue
  [pronoun] extraordinary work. I would like to express my strongest
  recommendation and full support."

---

**Sincerely,**
[Recommender Name]
[Title]
[Institution]

---

## Writing Rules

1. **First person throughout.** This letter is written AS the recommender.
   Never slip into third person about the recommender.

2. **Name everything.** Model names (acronyms included), journal names with
   rankings, federal programs with dollar figures, specific medical procedures,
   specific case outcomes.

3. **Before/after framing.** Every contribution paragraph must explain
   what existed BEFORE and what changed AFTER. "Prior to Dr. [name]'s work..."
   is the required setup.

4. **Numbers anchor credibility — quantify outcomes with objective markers
   (2024-2025 critical).** Every application must have at least one specific
   number: patients, surgeries, jobs, dollar amounts, citation counts, grant
   amounts. Officers now specifically look for **objective markers of success**
   within the field, not just qualitative praise. A letter that offers only
   "brilliant researcher" or "exceptional contributions" without quantified
   outcomes is increasingly discounted. Every letter must cite at least one
   objective, verifiable outcome that the recommender can speak to from
   their own professional vantage point.

5. **Independence must be explicit and early.** USCIS weighs independent letters
   more heavily. The independence statement must appear in Paragraph 1, not buried.

6. **How they found the work matters.** The discovery story (read the paper,
   attended seminar, requested code, code used in their own research) is what
   makes the independence real and credible. Make it specific and vivid.

7. **National hook is required.** Every letter must tie the work to a named
   federal policy, initiative, regulatory agency, or national-scale statistic.
   A letter about purely academic contributions without a national hook is weak.

8. **Recommender credentials > praise.** A detailed paragraph establishing
   why the recommender is qualified to assess the work is more persuasive than
   superlatives. "As the original developer of the model that Dr. Liu extended..."
   beats "as a leading expert in..."

9. **Do not fabricate quotes or statistics.** If the user provides quotes, use
   them. If the user provides statistics, use them. If neither are provided,
   draft placeholder text and flag it clearly with [DRAFT — please verify/replace].

10. **Letter length:** 800–1,500 words. Long enough to be substantive, short
    enough to be read. A letter that is 3 paragraphs is too weak. A letter
    that is 10+ dense paragraphs is too long.

11. **No labor shortage language.** Never frame the recommender's endorsement
    as a staffing need. Phrases like "hard to find qualified candidates,"
    "filled a critical gap in our team," "we couldn't recruit anyone with this
    background," or "uniquely difficult to source" actively weaken the NIW case.
    USCIS explicitly discounts labor shortage arguments. The argument is about
    national benefit from this specific person's contributions — not about
    employer hiring difficulty. This rule applies to industry recommenders
    especially — their instinct is often to frame the petitioner as irreplaceable
    for their company, which is Pattern G territory. Redirect to national benefit.

---

## Authenticity Checklist (Critical for 2025-2026)

USCIS officers are increasingly trained to identify letters that appear attorney-drafted
or AI-generated rather than genuinely authored by the recommender. Authentic letters
are more persuasive; detected template letters are discounted or flagged.

### Pre-Submission Authenticity Verification

Before any letter is sent to the recommender for signature, verify:

- [ ] **CRITICAL — No mismatched fonts:** The entire letter must use one font,
      one size, one style throughout. Mixed fonts are the **#1 signal** officers
      look for to identify attorney-drafted templates — this is now elevated to
      the top priority check based on 2024-2025 adjudication patterns. A single
      font inconsistency can cause an officer to discount the entire letter.
- [ ] **No copy-paste errors:** Check for wrong gender pronouns, wrong field name,
      wrong petitioner name, or text that clearly belongs to a different letter.
      These are the #2 signal of attorney-drafted templates.
- [ ] **Consistent voice:** The letter should sound like a specific human being
      writing, not a legal document. Vary sentence structure. Include one or two
      personal observations that only this recommender would make.
- [ ] **Recommender's actual expertise reflected:** The technical depth should
      match the recommender's real expertise. A clinician should not write like
      a statistician about methodology. A methodologist should not write like a
      policy expert about federal programs.
- [ ] **Organic discovery story:** The "how I found this work" narrative should
      feel natural and specific — not formulaic. "I encountered Dr. Kim's work
      when I was searching for a solution to [specific problem] and her 2022
      paper in [journal] described exactly the approach I needed" beats "I became
      aware of Dr. Kim's distinguished contributions to the field."
- [ ] **No regulatory parroting (elevated priority 2024-2025):** Letters that
      repeat USCIS regulatory language verbatim ("original contributions of major
      significance," "well-positioned to advance the proposed endeavor") are now
      actively discounted by officers as obviously attorney-drafted. This is no
      longer a style preference — it is an effectiveness issue. Use natural
      language that conveys the same meaning without copying the legal standard.
      Officers are specifically trained to detect this pattern.
- [ ] **Recommender-specific details:** Include at least one detail that could
      only come from this specific recommender — their own research challenge
      that the petitioner's work addressed, a specific seminar where they met,
      a specific dataset they applied the petitioner's method to.
- [ ] **Passion and conviction:** Officers report being more persuaded by letters
      that convey genuine enthusiasm. Include language that reflects real
      intellectual excitement, not just professional endorsement:
      "When I first applied Dr. Kim's framework to our clinical trial data,
      the results fundamentally changed how I think about [topic]."

### Red Flags Officers Look For

If any of these appear in a letter, rewrite before sending:
- Identical paragraph structures across multiple letters in the same petition
- Regulatory language quoted verbatim
- Superlatives without factual support ("extraordinary," "brilliant," "world-class")
- Generic field-importance arguments instead of petitioner-specific claims
- Multiple letters using the same statistics or same phrasing for different claims
- Letters that read as third-person descriptions reformatted to first-person

---

## What to Ask If Inputs Are Incomplete

**Missing recommender credentials:**
"What is [recommender]'s educational background and current research focus?
Do they have notable grants, publications, or positions that establish their
authority to evaluate this work?"

**Missing independence details:**
"How does [recommender] know [petitioner]'s work? Did they meet at a conference,
read a specific paper, or use the petitioner's code in their own research?
Have they ever collaborated or been in the same research group?"

**Missing specific application details (Type B):**
"What specific problem did [recommender] encounter that [petitioner]'s work
solved? Is there a concrete example with measurable outcome — number of patients,
dollar savings, policy change, or similar?"

**Missing methodology depth (Type A):**
"What was the limitation of the existing approach that [petitioner] solved?
What is the name of the prior method and what specifically was wrong with it?
What is the name of [petitioner]'s new method?"

**Missing national hook:**
"Is there a named federal program, regulatory agency, or national-scale
statistic that connects [recommender]'s domain to national interest?
(e.g., NIH grant, Precision Medicine Initiative, CHIPS Act, SEC regulations,
number of Americans affected)"

---

## Gap Flags

After drafting, append a brief flag section:

```
[DRAFT FLAGS]
- [VERIFY] Any statistic or outcome I could not confirm from provided info
- [PLACEHOLDER] Any quote drafted for the recommender — must be reviewed and signed off
- [STRENGTHEN] Any section that would benefit from additional specific detail
- [INDEPENDENCE RISK] Any relationship detail that might weaken independence claim
```

---

## After Drafting

Run **vera-niw-pl-review** on the completed letter before sending it to the
recommender. Pattern F in that skill checks recommendation letters specifically for:
- Generic praise without specifics
- Missing before/after framing
- Weak or buried independence statement
- Labor shortage language (Pattern G bleed-through)
- Recommender credentials insufficiently established

A letter that passes vera-niw-pl-review Pattern F is ready to send.
A letter that fails it needs revision before the recommender sees it —
recommenders should sign letters that are already strong, not letters
that need fixing after the fact.

---

## Letter Types Quick Reference

| Letter Type | Primary Audience | Core Message | Best For |
|---|---|---|---|
| A — Methodology | Same-field academics, USCIS | "This is a genuine theoretical breakthrough" | Academic applicants, statistical/methodological work |
| B — Application | Practitioners, USCIS | "This solved a real problem in my field" | Industry applicants, applied research |
| C — Hybrid | Both | "Novel method + real impact" | When fewer recommenders available |

Recommended portfolio per NIW petition:
- 1 pure methodology letter (Type A) — validates technical originality
- 1-2 application letters (Type B) — validates real-world impact
- 1 letter from advisor or close collaborator (affiliated, clearly labeled) — validates petitioner's role
- 1 letter from senior practitioner (industry executive, regulator, clinician) — validates national-scale relevance

---

## Strategic Letter Staggering for RFE Preparedness

### The Principle

Three strong, highly specific letters are more effective than ten generic ones.
But the optimal strategy goes further: plan a filing-stage portfolio AND an
RFE-stage reserve.

### Recommended Portfolio Strategy

**Initial filing (3-4 letters):**
- 1 pure methodology letter (Type A) — validates technical originality
- 1-2 application letters (Type B) — validates real-world impact
- 1 letter from advisor or close collaborator (affiliated, clearly labeled) — validates petitioner's role

**Held in reserve for potential RFE (1-2 letters):**
- 1 senior industry practitioner or government/regulatory expert — strongest
  independent validation, held back so the RFE response contains genuinely
  new evidence the officer hasn't seen
- 1 additional independent academic from a different subfield — demonstrates
  cross-domain recognition

### Why Stagger?

When an officer issues an RFE, they typically draft language they intend to reuse
in a denial letter. The strategic goal of the RFE response is to introduce evidence
so compelling that the officer's draft denial no longer applies — forcing them to
"write from scratch" to justify an approval.

Fresh, never-before-seen recommendation letters are the most effective tool for this:
- They provide genuinely new evidence (not a repeat of what was already dismissed)
- They can be specifically tailored to address the RFE's concerns (since you now know
  exactly what the officer cares about)
- They demonstrate that the petitioner's support base is broader than initially shown

### Rebutting EB-1A Misapplication in RFE-Stage Letters (2024-2025 Trend)

When an RFE applies EB-1A standards to an EB-2 NIW case (e.g., demanding
"original contributions of major significance" or proof of being "at the
top of the field"), reserve letters should:
- Include language from recommenders that speaks to "substantial merit and
  national importance" (Dhanasar Prong 1), NOT "extraordinary ability"
- Frame the petitioner's contributions in terms of the Dhanasar three-prong
  framework, explicitly distinguishing from EB-1A criteria
- The recommender should describe how the petitioner's work benefits the
  national interest, not whether they are "extraordinary" or "at the top"
- Include a natural-language statement equivalent to: "The significance of
  [petitioner]'s work lies not in whether [they] stand at the pinnacle of
  [their] field, but in the measurable national benefit [their] specific
  endeavor delivers" — adapted to the recommender's authentic voice

### When the User Didn't Plan Ahead

If the user receives an RFE and did not hold letters back:
- Commission new letters immediately, specifically targeting the RFE gaps
- Use vera-niw-rfe-response to identify which gaps need new letters
- Provide the RFE text to new recommenders so they can directly address concerns
- New letters should be from recommenders NOT in the initial filing — the officer
  needs to see new voices, not the same supporters saying more
- **If the RFE misapplied EB-1A standards:** New letters should explicitly
  address the Dhanasar framework and rebut the incorrect standard — this is
  the most effective use of fresh recommendation letters in this scenario

### Integration with vera-niw-rfe-response

When vera-niw-rfe-response identifies letter gaps, it will specify:
- Which prong needs reinforcement
- What type of recommender would be most credible
- What specific claims the new letter should contain
- What before/after framing is needed

Use those specifications as direct input for generating the reserve letters.
