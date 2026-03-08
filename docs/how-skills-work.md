# How Skills Work: Turning Expert Judgment into AI-Executable Units

## The Problem

Every domain has experts who make fast, accurate judgment calls that novices can't replicate. An experienced NIW attorney reads a petition letter and knows in minutes whether it will trigger an RFE. A senior statistician glances at an experimental design and spots the fatal flaw. A seasoned editor reads a paragraph and knows exactly why it sounds like AI wrote it.

This expertise isn't magic. It's pattern recognition built from hundreds or thousands of cases. The patterns are discoverable, describable, and — crucially — encodable.

## The Insight

Expert judgment decomposes into three layers:

**Layer 1: Domain Knowledge.** Facts, rules, frameworks. For NIW: the Dhanasar three-prong test, USCIS policy memoranda, AAO decision patterns. This is the easiest layer to encode — it's already written down somewhere.

**Layer 2: Decision Heuristics.** The if-then rules experts apply unconsciously. "If the endeavor statement describes a job rather than an undertaking, it will fail Prong 1." "If a recommendation letter uses the phrase 'to whom it may concern,' it signals the recommender doesn't actually know the petitioner." These rules live in experts' heads and rarely get written down.

**Layer 3: Calibration.** Knowing when a case is borderline vs. clearly strong vs. clearly weak. This requires exposure to the full distribution of cases — not just the extremes. Calibration is the hardest layer to encode because it requires representative examples, not just rules.

## The Method

A skill encodes all three layers into a structured AI instruction set:

### Step 1: Decompose

Map every decision point in the workflow. For the NIW domain, this revealed a 7-step pipeline: evaluate → endeavor → pillar (×3) → recommendation → assemble → review → RFE response. Each step has its own decision rules, failure patterns, and quality criteria.

### Step 2: Encode as Rubric

Convert decision heuristics into explicit scoring criteria. Don't say "the endeavor should be specific" — say "the endeavor must contain a proper-noun project name, a named methodology, and a quantified national outcome." Rubrics eliminate ambiguity.

### Step 3: Add Reference Material

Layer 1 knowledge goes into `references/` files that the skill can consult. For NIW PL Review, this includes USCIS RFE language patterns, publication diligence rules, EB-2 eligibility criteria, and the full Dhanasar analytical framework. For NIW Evaluate, this includes field alignment rubrics and example outputs at each qualification tier.

### Step 4: Validate with Test Cases

Every skill includes `evals/` — test inputs with expected outputs. These serve two purposes: verifying the skill works correctly, and documenting edge cases the skill must handle. If you can't write a test case for a decision rule, the rule isn't specific enough.

### Step 5: Pipeline Integration

Individual skills are useful. A connected pipeline is transformative. Each skill's output format is designed as input for the next skill — the Evaluate JSON feeds Endeavor, Endeavor's pillar seeds feed Pillar, and all outputs converge in Assemble. This isn't accidental; it's the core architectural decision.

### Step 6: Iterate

Real users find failure modes you didn't anticipate. Every bug report is a missing decision rule. Every unexpected output is a calibration gap. The skill improves the same way expert judgment improves — through exposure to more cases.

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

The NIW domain is the first complete implementation — 8 skills covering the entire petition lifecycle. The same methodology applies wherever expert judgment follows discoverable patterns:

| Domain | Layer 1 (Knowledge) | Layer 2 (Heuristics) | Layer 3 (Calibration) |
|---|---|---|---|
| **NIW Petitions** | Dhanasar framework, AAO decisions | 10 denial patterns (A–J), 8 rebuttal patterns (R1–R8) | 31 eval test cases across tiers |
| **Academic Peer Review** | Journal standards, field norms | Common rejection reasons, methodology red flags | Accept/revise/reject distribution |
| **Regulatory Compliance** | Statute text, agency guidance | Violation patterns, audit triggers | Severity scoring by precedent |
| **Clinical Diagnostics** | Diagnostic criteria, treatment protocols | Differential diagnosis heuristics | Probability calibration by presentation |

To build a skill for a new domain:

1. Find the expert whose judgment you want to encode
2. Map their decision process (Step 1)
3. Extract the heuristics they can't easily articulate (Step 2)
4. Gather the reference material they consult (Step 3)
5. Collect representative cases at each quality tier (Step 4)
6. Design the pipeline — what feeds what (Step 5)
7. Ship it, then iterate on real user feedback (Step 6)

The question isn't whether expertise can be decomposed into AI-executable units. It's which domain gets decomposed next.
