# How Skills Work: Decomposing Workflows into Reviewable Units

## The Problem

Many domains contain workflow steps that follow discoverable patterns — evidence that tends to be persuasive, narrative structures that hold up under scrutiny, common gaps that reviewers flag. An experienced reader of NIW petition letters can quickly point to passages that commonly trigger RFEs. A senior statistician can flag designs that won't survive review. These pattern judgments are valuable — but they're not the same as case-specific legal or scientific judgment, which still requires a qualified human.

The patterns themselves are discoverable, describable, and — crucially — encodable as structured workflows.

## The Insight

Workflow patterns decompose into three layers:

**Layer 1: Public Domain Knowledge.** Facts, rules, frameworks. For NIW: the Dhanasar three-prong test, USCIS Policy Manual sections, public AAO decisions. For EB-1: the Kazarian two-step framework and 8 CFR 204.5(h) criteria. This layer is sourced from public materials.

**Layer 2: Pattern Heuristics.** The recurring "if X is missing, reviewers commonly flag Y" patterns visible in public AAO reasoning and policy guidance. "If the endeavor statement describes a job rather than an undertaking, it commonly fails Prong 1 review." "If a recommendation letter parrots regulatory language, it weakens credibility." These are pattern observations, not legal conclusions.

**Layer 3: Calibration.** Distinguishing thin / workable / strong evidence postures. This requires exposure to a wide range of public examples and reference cases. Calibration outputs are evidence-readiness summaries for human review, not eligibility determinations.

## The Method

A skill encodes all three layers into a structured Claude instruction set:

### Step 1: Decompose

Map every decision point in the workflow. For the NIW domain, this revealed a 7-step pipeline: evaluate → endeavor → pillar (×3) → recommendation → assemble → review → RFE response. Each step has its own structured rubric, common-weakness checks, and review criteria.

### Step 2: Encode as Rubric

Convert pattern heuristics into explicit, reviewable criteria. Don't say "the endeavor should be specific" — say "the endeavor draft should contain a proper-noun project name, a named methodology, and a quantified national outcome; if any are missing, flag for human revision." Rubrics make output reviewable.

### Step 3: Add Reference Material

Layer 1 knowledge goes into `references/` files that the skill can consult. For NIW PL Review, this includes USCIS RFE language patterns, publication diligence rules, EB-2 eligibility criteria from the USCIS Policy Manual, and the Dhanasar analytical framework. For NIW Evaluate, this includes field-alignment rubrics and example outputs at each evidence-readiness posture.

### Step 4: Validate with Test Cases

Every skill includes `evals/` — test inputs with expected outputs. These verify the skill behaves consistently on representative cases and document edge cases. If you can't write a test case for a rule, the rule isn't specific enough.

### Step 5: Pipeline Integration

Individual skills are useful. A connected pipeline is transformative. Each skill's output format is designed as input for the next skill — the Evaluate JSON feeds Endeavor, Endeavor's pillar seeds feed Pillar, and all outputs converge in Assemble. This isn't accidental; it's the core architectural decision.

### Step 6: Iterate

Real users find failure modes you didn't anticipate. Every bug report is a missing rubric step. Every unexpected output is a calibration gap. Skills improve through exposure to more public cases and review feedback.

## The Architecture

```
skill/
├── SKILL.md          ← The instruction set (Layers 2 + 3)
├── README.md         ← Usage guide for humans
├── references/       ← Domain knowledge (Layer 1)
├── schema/           ← Input/output structure definitions
├── examples/         ← Calibration samples at different tiers
└── evals/            ← Test cases (validation)
```

This structure is intentionally simple. A skill is a text file, not a software system. It runs on any AI assistant that accepts custom instructions. No dependencies, no deployment, no maintenance burden.

## Applying This to Other Domains

NIW and EB-1 are the first complete implementations — 19 skills covering most of the evidence-building and petition-preparation workflow. The same methodology applies wherever decomposable, reviewable workflow patterns exist alongside human judgment that should not be automated:

| Domain | Layer 1 (Public knowledge) | Layer 2 (Pattern heuristics) | Layer 3 (Calibration) | Layer that stays human |
|---|---|---|---|---|
| **NIW petitions** | Dhanasar framework, USCIS Policy Manual, AAO decisions | Common evidence weaknesses, narrative-risk patterns | Evidence-readiness postures | Case-specific legal eligibility, approval assessment |
| **EB-1 petitions** | Kazarian framework, 8 CFR 204.5(h)/(i), AAO decisions | Criterion-mapping patterns, sustained-acclaim signals | Evidence-readiness postures | Case-specific legal eligibility, approval assessment |
| **Statistical research** | Method assumptions, reporting standards | Common analytical pitfalls | Effect-size and uncertainty framing | Substantive interpretation, claim validity |
| **AI/ML research** | Benchmark norms, evaluation standards | Common comparison and reporting flaws | Empirical posture framing | Scientific claim validity, novelty judgment |

To build a skill for a new domain:

1. Identify the workflow patterns that are repeatable and reviewable — not the judgment that must stay human
2. Map the decision points (Step 1)
3. Extract the pattern heuristics from public materials (Step 2)
4. Gather reference material (Step 3)
5. Collect representative cases at each quality tier (Step 4)
6. Design the pipeline — what feeds what (Step 5)
7. Ship it, then iterate on real user feedback (Step 6)

The question isn't whether workflow patterns can be decomposed into reviewable units. It's where the line between execution and judgment belongs.
