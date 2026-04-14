# 01 -- Collect Inputs

## Executor: Main Agent

## Data In: User request (natural language)

## Required

Ask for anything missing. Do not proceed until all required inputs are collected.

1. **Data** -- one of:
   - CSV/data file uploaded
   - Dataset description (variables, types, N, source)
   - Variable names + context

2. **Response variable (Y)** -- the measured outcome
   - Name, units, what it measures
   - Confirm it is continuous (not binary, count, ordinal)

3. **Factors** -- the experimental treatments
   - Name of each factor
   - Levels of each factor (e.g., Low/High, or 0/5/10/15)
   - Type: fixed or random
   - Whether each factor was deliberately manipulated (must be YES for DOE)

4. **Design type** -- one of:
   - CRD (Completely Randomized Design)
   - RCBD (Randomized Complete Block Design)
   - Full factorial (2^k, 3^k, mixed)
   - Fractional factorial (specify resolution if known)
   - Split-plot (specify whole-plot and subplot factors)
   - Latin square
   - Other (describe)

5. **Blocking variable** -- if applicable
   - Name, number of blocks
   - Purpose of blocking (what source of variation it controls)

6. **Replication info**
   - Number of replicates per treatment combination (cell)
   - Total N
   - Whether design is balanced (equal N per cell) or unbalanced

## Validation Checkpoint

- [ ] Response is truly continuous (not ordinal, not count)
- [ ] All factors were deliberately manipulated (this is a designed experiment, not observational)
- [ ] If observational data detected, redirect to appropriate skill (continuous-testing, etc.)
- [ ] Design type identified and consistent with factor structure
- [ ] If blocked: blocking variable identified with number of blocks
- [ ] Cell sizes noted (balanced or unbalanced)
- [ ] If N < 3 per cell, power limitation warning issued
- [ ] If fractional: resolution noted or flagged as unknown
- [ ] At least response + one factor collected

## Data Out -> 02-check-distribution.md

Structured input summary containing:
```
response_var: {name, units, description}
factors: [{name, levels, n_levels, type: fixed|random}]
design_type: CRD | RCBD | factorial | fractional | split_plot | latin_square
blocking_var: {name, n_blocks} or null
replication: {per_cell, total_n, balanced: TRUE|FALSE}
data_source: {file_path | description | variable_list}
```
