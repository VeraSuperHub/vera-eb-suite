# Endeavor Anatomy Reference

*Read this during Phase 2 (Ingredient Interview) and before drafting.*

---

## Table of Contents

1. What makes an endeavor valid under Dhanasar
2. The 6 ingredients — definitions, strong/weak examples, interview prompts
3. Strong vs. weak endeavor statements — annotated
4. Rewrite templates for the four most common failure modes
5. Naming a project: why it matters and how to do it

---

## 1. What Makes an Endeavor Valid Under Dhanasar

USCIS must be able to answer three questions from the endeavor statement alone:

**Question 1 (Prong 1):** What specific national problem does this undertaking address, and why does it matter at national scale?

**Question 2 (Prong 2):** Why is *this petitioner* — not any qualified professional in the field — the one to do it?

**Question 3 (Prong 3):** Why is a waiver of the labor certification process appropriate for this specific undertaking?

If the endeavor statement cannot seed the answers to all three, it is incomplete. The interview and drafting process in this skill is designed to build each answer in.

**The core rule:**
> "The plain language of Dhanasar calls an endeavor an *undertaking.*"
> An occupation is not an undertaking. A field is not an undertaking.
> A job description is not an undertaking.

---

## 2. The 6 Ingredients

### Ingredient 1 — Named Project or Initiative

**What it is:** A proper-noun identifier for the specific work being proposed. Not a job title, not a technology label, not a domain. The name of the thing itself.

**Why it matters:** Named initiatives signal to officers that a bounded, real undertaking exists. Unnamed work signals job duties. This is a cognitive cue, not just a stylistic one.

| Weak | Strong |
|---|---|
| "my AI research" | "the PharmacoSignal Detection Suite" |
| "fraud detection work" | "the FraudNet critical infrastructure framework" |
| "my drug safety studies" | "the FAERS-NLP Adverse Event Surveillance System" |
| "healthcare AI projects" | "the ClinicalBERT-ADE pipeline for post-market surveillance" |

**Interview prompt if no name exists:**
> "If you had to put this on a poster at a conference, what would the title be?
> What would you call it in a grant proposal? That's the name we want."

**Naming formula:** `[Descriptive adjective] + [application domain] + [what it does] + [type of system/framework/tool]`
- e.g., "Real-Time Pharmacovigilance Signal Detection Framework using LLM Annotation"

---

### Ingredient 2 — Specific National-Scale Problem

**What it is:** The documented gap, failure, or threat that the undertaking addresses — named, quantified, and anchored to a national-scale source.

**Why it matters:** Officers cannot evaluate national importance without a specific problem statement. "Healthcare is important" is not a problem statement. "1.5 million preventable adverse drug events annually, causing $3.5 billion in excess hospital costs (IOM, FDA Safety Report 2022)" is a problem statement.

| Weak | Strong |
|---|---|
| "drug safety is a major concern" | "FDA receives 2+ million FAERS reports annually; fewer than 12% are systematically analyzed for novel signal patterns due to NLP tool limitations" |
| "cybersecurity threats are increasing" | "CISA documented 557 ransomware attacks on U.S. critical infrastructure in 2023, costing $1.1B in recovery (CISA Annual Report)" |
| "financial fraud affects many people" | "Investment fraud caused $4.6 billion in U.S. consumer losses in 2023 (FTC Consumer Sentinel), disproportionately affecting retirement savers" |
| "healthcare billing fraud is a problem" | "Medicare and Medicaid fraud cost U.S. taxpayers an estimated $95 billion annually (HHS OIG 2022)" |

**Interview prompt when the problem is vague:**
> "What specifically fails right now — in the U.S. at national scale —
> because your approach doesn't exist yet or isn't widely deployed?
> What is the documented cost of that failure in dollars, lives, or systems?"

**Source hierarchy (strongest to weakest):**
1. Federal agency reports (HHS, FDA, CISA, NIH, Treasury)
2. Congressional reports or GAO findings
3. Peer-reviewed public health / policy literature
4. Industry association data (if the association is the authoritative source)
5. News coverage (weakest — only use to supplement, not anchor)

---

### Ingredient 3 — Named Methodology

**What it is:** The specific technique, algorithm, model architecture, or analytical framework the petitioner uses. Not "machine learning." Not "advanced methods." A named, non-generic approach.

**Why it matters:** Named methodology does two jobs: it distinguishes the petitioner from any generic practitioner in the field, and it gives Prong 2 a concrete technical anchor that recommenders can independently validate.

| Weak | Strong |
|---|---|
| "machine learning" | "transformer-based named entity recognition with domain-adapted pre-training on clinical text (BioBERT architecture)" |
| "statistical analysis" | "survival analysis using Cox proportional hazards and Fine & Gray competing risks models on longitudinal IPO data" |
| "NLP techniques" | "transformer-based relation extraction with domain-adaptive pre-training on clinical discharge notes (BioBERT fine-tuned on MIMIC-III)" |
| "AI for drug safety" | "named entity recognition pipeline for adverse event detection in unstructured EHR text, evaluated on NCBI disease corpus with F1 > 0.87" |
| "data science approaches" | "multi-task learning framework combining sequence labeling and document classification on imbalanced biomedical corpora" |

**Interview prompt when methodology is vague:**
> "What specific algorithm, model, or technique do you use that's not just
> 'off-the-shelf'? If I hired a standard data scientist, what would they miss
> that you specifically bring? Name it."

---

### Ingredient 4 — Application Domain and National Interest Tier

**What it is:** The actual domain of national importance — stripped of any technology label. This is what NIW_Evaluate calls the "application domain."

**Key rule:** AI, ML, NLP, data science, and similar technologies are *methods*. They carry no independent national importance. The domain of application carries the weight.

→ See `references/field-alignment.md` for full Tier 1/2/3 table.

**The domain identification test:**
> "If I removed all references to AI/ML/NLP from your work description,
> what field would be left? That is your domain."

| Tech label stripped | Actual domain | Tier |
|---|---|---|
| LLMs for drug safety | Pharmacovigilance / public health | Tier 1 |
| NLP for financial markets | Financial market integrity / fraud prevention | Tier 2 |
| AI for biosurveillance | Pandemic preparedness / public health | Tier 1 |
| ML for power grid anomaly detection | Critical infrastructure / cybersecurity | Tier 1 |
| Transformers for clinical notes | Public health / precision medicine | Tier 1 |
| Data science for retail optimization | Consumer / retail | Tier 3 — weak |

---

### Ingredient 5 — Measurable National-Scale Outcome

**What it is:** The specific, quantified end-state if the proposed endeavor succeeds. What changes at national scale.

**Why it matters:** USCIS asks whether the work has national importance. Vague outcomes ("improve patient safety," "advance the field") do not answer this. Numbers do.

| Weak | Strong |
|---|---|
| "improve drug safety monitoring" | "enable systematic NLP-based signal detection across 2M+ annual FAERS reports, reducing time-to-signal from 18 months to 3 months for 200+ priority drug-event pairs" |
| "help financial regulators" | "provide SEC and FINRA with automated analyst-report surveillance covering $24 trillion in U.S. equity markets" |
| "advance cybersecurity" | "deploy anomaly detection across 600+ U.S. utilities serving 140 million households, aligned with CISA's $1.9B infrastructure protection mandate" |
| "improve healthcare outcomes" | "reduce preventable adverse drug events by an estimated 15% in monitored populations, translating to $525M in annual avoided costs" |

**Interview prompt:**
> "If your endeavor fully succeeds in five years, give me one sentence with
> a number in it that describes what changed in the U.S. What can we measure?"

---

### Ingredient 6 — The Substitutability Answer

**What it is:** The specific reason *this petitioner* and no equally qualified peer can lead this undertaking. The answer to: "Why not hire someone else?"

**Why it matters:** This is what separates an NIW petition from a PERM argument. The whole point of a National Interest Waiver is that the petitioner's specific contribution cannot be adequately captured by posting a job description. If any competent peer could do it, the waiver logic fails.

**Types of substitutability evidence (strongest to weakest):**
1. Published research or patent that is the foundation of the endeavor (only this person holds this IP)
2. Deployed system with government or institutional adoption (they already did it)
3. Unique dataset or methodology developed through years of prior work
4. Named expert endorsements saying specifically why this person (not "she is talented")
5. First-mover status in a new subfield where they defined the methodology

| Weak | Strong |
|---|---|
| "I am a skilled researcher in this area" | "Primary author of the only validated pipeline for zero-shot adverse event extraction from multilingual social media using cross-lingual BERT — no commercially available tool performs this function (Rodriguez et al., 2023, Journal of Biomedical Informatics)" |
| "I have relevant experience" | "Sole developer of the FAERS-NLP system currently in pilot at [institution]; the system's architecture is documented in three peer-reviewed papers that form the technical foundation of this endeavor" |
| "I am uniquely qualified" | "The only research team to have validated cross-lingual biomedical NER transfer across 12 low-resource clinical languages, documented in three peer-reviewed studies — no open-source system replicates this multilingual coverage (Patel et al., 2023, EMNLP; 2024, ACL)" |

---

## 3. Strong vs. Weak Endeavor Statements — Annotated

### Example A — Weak (fails Pattern A and B)

> "Dr. Chen's proposed endeavor is to work as a data scientist applying machine
> learning techniques to improve healthcare outcomes in the United States."

❌ **Pattern A:** Describes a job role, not an undertaking  
❌ **Pattern B:** Any data scientist in healthcare could match this description  
❌ **No named project, no named methodology, no named problem, no outcome**  
❌ **No federal anchor, no substitutability signal**

---

### Example B — Partially improved (passes A, still fails B and C)

> "Dr. Chen's proposed endeavor is to develop AI-powered tools for adverse
> drug event detection using electronic health record data."

⚠️ **Pattern A:** Slightly better — names a category of work, but not a specific undertaking  
❌ **Pattern B:** Still describes what any NLP engineer in pharma could do  
❌ **Pattern C:** "AI-powered tools" and "adverse drug event detection" are field-level; no national scope argument, no federal anchor  

---

### Example C — Strong (passes all four checks)

> "Dr. Chen's proposed endeavor is to develop the FAERS-NLP Adverse Event
> Signal Detection System — a transformer-based named entity recognition
> pipeline that systematically analyzes the 2+ million annual patient-reported
> outcomes in the FDA FAERS database to detect emerging drug safety signals 15x
> faster than current manual review methods. This work directly advances FDA's
> Sentinel System mandate and the White House's Critical and Emerging Technologies
> priority in biotechnology and health security. Dr. Chen is uniquely positioned
> to lead this work as the primary author of the only peer-reviewed methodology
> for automated adverse event extraction from unstructured FAERS narratives
> (Journal of Biomedical Informatics, 2023), with no commercially available
> alternative providing equivalent detection capability."

✅ **Pattern A:** Named specific system (FAERS-NLP), specific method, specific goal  
✅ **Pattern B:** Only Dr. Chen holds the published foundational methodology  
✅ **Pattern C:** Quantified national scope (2M+ reports), named federal initiative (FDA Sentinel), named CET area  
✅ **Substitutability:** Named publication + "no commercially available alternative"  
✅ **Measurable outcome:** "15x faster than current manual review"  
✅ **Third person, no hedging, 3 sentences**

---

## 4. Rewrite Templates for Common Failure Modes

### Template 1 — Job description → undertaking

**Before:** "My endeavor is to work as a [title] applying [technology] to [domain]."

**After:** "[Petitioner]'s proposed endeavor is to develop and deploy [NAMED SYSTEM/FRAMEWORK] — a [NAMED METHOD] approach for [SPECIFIC PROBLEM] in [DOMAIN] — to [MEASURABLE NATIONAL OUTCOME]. This work directly advances [NAMED FEDERAL INITIATIVE] by [SPECIFIC MECHANISM]. [Petitioner] is uniquely positioned through [SPECIFIC PRIOR CONTRIBUTION ONLY THEY HOLD]."

---

### Template 2 — Field-level importance → specific undertaking importance

**Before:** "My work advances the field of X, which is critical to national Y."

**After:** "[Petitioner]'s [NAMED SYSTEM] addresses [SPECIFIC DOCUMENTED FAILURE] in [FIELD] — a gap that [QUANTIFIED NATIONAL COST/CONSEQUENCE] per [FEDERAL SOURCE]. Unlike existing [ALTERNATIVES], [PETITIONER'S APPROACH] achieves [SPECIFIC MEASURABLE IMPROVEMENT] by [NAMED METHOD]."

---

### Template 3 — No federal anchor → named federal connection

**Weakness:** "...which improves public health outcomes."

**Fix:** "...directly advancing [FDA Sentinel System / NIH All of Us / CISA Cybersecurity Advisory / White House CET biotechnology priority] by providing [SPECIFIC CAPABILITY THAT FEDERAL PROGRAM LACKS OR EXPLICITLY NEEDS]."

**Federal anchor sources to check:**
- White House CET list (18 priority technology areas)
- CHIPS Act, IRA, American Rescue Plan program offices
- FDA Sentinel, FAERS, MedWatch — for pharma/health
- CISA advisories and sector-specific plans — for cybersecurity
- NSF, NIH program announcements — for research domains
- SEC, FINRA, Treasury — for financial markets
- DOE, EPA — for energy/climate

---

### Template 4 — Generic expertise → specific substitutability

**Before:** "I am a leading expert in X with extensive experience in Y."

**After:** "[Petitioner] is the [primary author / sole developer / first researcher] to [SPECIFIC UNIQUE CONTRIBUTION] — documented in [NAMED PUBLICATION / PATENT / DEPLOYED SYSTEM] — establishing [SPECIFIC METHODOLOGICAL CLAIM]. No commercially available system provides this capability, and no published methodology to date has [SPECIFIC ADVANCE ONLY THIS PERSON MADE]."

---

## 5. Naming a Project: Why It Matters and How to Do It

Officers read hundreds of petitions. Named projects are landmarks. Unnamed work is fog.

**The naming effect:** Compare:
- "I develop machine learning tools for healthcare" (forgettable, sounds like a job)
- "I develop the ClinicalBERT-ADE Pipeline" (specific, sounds like a real system that exists)

Both may describe identical work. The name changes how the officer perceives concreteness.

**Naming criteria:**
- Should describe *what it does* and *for what domain*
- Can include the methodology if it's distinctive (e.g., "LLM-Based," "NLP-Powered," "Entropy-Guided")
- Should be title-case and function like a proper noun
- 3–6 words is ideal

**Naming formula:**
`[Domain/Application] + [What It Does] + [Type]`

Examples:
- `FAERS-NLP Signal Detection System`
- `CriticalGrid Anomaly Detection Framework`
- `FraudNet Financial Surveillance Platform`
- `PharmacoSignal LLM Annotation Suite`
- `MuniRisk Fiscal Stress Prediction Engine`
