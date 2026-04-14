# Manuscript Template

Markdown structure for the assembled manuscript. All manuscripts follow this section order regardless of outcome type or discipline.

## Template

```markdown
# [Title]

## Abstract

[150-250 words. Written LAST after all other sections.]

**Background**: [1-2 sentences: context + gap]
**Objective**: [1 sentence: what this study does]
**Methods**: [2-3 sentences: data, design, key methods]
**Results**: [3-4 sentences: main findings with key numbers]
**Conclusions**: [1-2 sentences: implications]

**Keywords**: [3-5 keywords, separated by commas]

---

## 1. Introduction

[3-5 paragraphs, 600-1000 words]

[Para 1: Broad context and significance]
[Para 2: What is known — prior findings from literature]
[Para 3: Gap — what remains unknown, why existing analyses fall short]
[Para 4: This study — objective, approach, hypothesis]
[Para 5 (optional): Contribution and paper outline]

## 2. Data and Study Design

### 2.1 Data Source

[Dataset description, study design, time period, setting, population]

### 2.2 Variables

**Outcome**: [name, measurement, units, range]

**Predictors**: [list with brief descriptions]

**Covariates**: [list with rationale for inclusion]

**Subgroup Variable**: [if applicable]

### 2.3 Sample Characteristics

[Reference Table 1]

[Brief narrative of key sample features: N, demographics, outcome distribution]

## 3. Statistical Methods

[From merged methods.md — reordered to standard flow]

### 3.1 Descriptive Statistics
[Distribution assessment approach]

### 3.2 Primary Hypothesis Tests
[Test selection rationale and methods]

### 3.3 Regression Analysis
[Model specification, diagnostics]

### 3.4 [Alternative Methods]
[Quantile regression / penalized / GEE / etc.]

### 3.5 Exploratory Analysis
[Tree-based methods — framed as exploratory]

### 3.6 Subgroup Analysis
[Stratification approach, interaction testing]

### 3.7 Model Comparison
[Cross-method synthesis approach]

### 3.8 Software
[R version, Python version, key packages with versions]

## 4. Results

[From merged results.md — follows Section 3 ordering]

### 4.1 Sample Description
[Reference Table 1, key descriptive findings]

### 4.2 Primary Tests
[Test results, effect sizes, CIs, p-values]

### 4.3 Regression Results
[Coefficients, SEs, CIs, model fit]

### 4.4 [Alternative Method Results]
[Method-specific results]

### 4.5 Exploratory Results
[Variable importance, patterns — exploratory framing]

### 4.6 Subgroup Results
[Stratified effects, interaction test, forest plot reference]

### 4.7 Cross-Method Comparison
[Unified importance table, convergence narrative]

## 5. Discussion

[5-7 paragraphs, 800-1200 words]

[Para 1: Key findings in plain language]
[Para 2-3: Comparison with prior work]
[Para 4: Methodological strengths — multi-method value]
[Para 5: Limitations (≥3)]
[Para 6: Implications and future directions]

## References

[From merged references.bib — formatted as numbered list or author-year depending on venue]

## Tables

**Table 1**: Sample Characteristics
[Demographics, outcome distribution, predictor distributions by group]

**Table 2**: [Primary test results / Regression coefficients]
...

**Table N**: Unified Variable Importance Across Methods
[Normalized 0-100 importance scores]

## Figure Captions

**Figure 1**: [Distribution / diagnostic plot]
**Figure 2**: [Primary test visualization]
...
**Figure N**: [Variable importance / forest plot]

[Actual figures stored in output/figures/ as PNG files]
```

## Section Length Guidelines

| Section | Words | Pages (approx) |
|---------|-------|-----------------|
| Abstract | 150-250 | — |
| Introduction | 600-1000 | 2-3 |
| Data & Study Design | 400-700 | 1-2 |
| Statistical Methods | 500-1000 | 2-3 |
| Results | 800-1500 | 3-5 |
| Discussion | 800-1200 | 2-3 |
| **Total** | **3250-5650** | **10-16** |

## Adaptation Notes

- **Epidemiology venues**: Follow STROBE checklist for observational studies
- **Psychology venues**: Follow APA 7th edition
- **Statistics journals**: More technical detail in methods, shorter discussion
- **Medical journals**: Structured abstract, CONSORT if RCT
- **General science**: Shorter methods, longer discussion
