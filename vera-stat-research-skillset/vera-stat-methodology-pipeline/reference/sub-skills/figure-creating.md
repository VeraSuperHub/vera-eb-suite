<!-- Absorbed from skills/paper-figure/SKILL.md -->

# Paper Figure: Statistics Publication Figures

Generate publication-quality figures from: **$ARGUMENTS**

## Auto-Generation Scope

| Can auto-generate | Needs manual creation |
|---|---|
| Line plots (MSE vs n, convergence rates) | DAG / causal diagrams |
| Coverage probability plots | Complex model diagrams |
| Power curve plots | Conceptual illustrations |
| Box plots (estimate distributions) | Workflow/pipeline diagrams |
| Heatmaps (correlation, parameter sensitivity) | |
| QQ plots | |
| Trace plots (MCMC) | |
| Forest plots (meta-analysis style) | |
| Bar charts with error bars | |
| Comparison tables (as figures) | |

## Setup

```python
# Standard imports for statistics figures
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns

# Publication quality settings
matplotlib.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman'],
    'text.usetex': True,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.figsize': (6, 4),
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# Colorblind-safe palette
CB_COLORS = ['#0072B2', '#D55E00', '#009E73', '#CC79A7', '#F0E442', '#56B4E9']
```

Or in R:
```r
library(ggplot2)
theme_set(theme_bw(base_size = 11))
# Colorblind-safe palette
cb_palette <- c("#0072B2", "#D55E00", "#009E73", "#CC79A7", "#F0E442", "#56B4E9")
```

## Figure Types for Statistics Papers

### 1. Convergence Rate Plot (log-log)
```python
# MSE vs sample size on log-log scale
# Should show slope matching theoretical rate
fig, ax = plt.subplots()
for i, method in enumerate(methods):
    ax.loglog(n_vec, mse[method], 'o-', color=CB_COLORS[i], label=method)
# Add reference slope for theoretical rate
ax.loglog(n_vec, C * n_vec**(-rate), '--', color='gray', label=f'$O(n^{{{-rate}}})$')
ax.set_xlabel('Sample size $n$')
ax.set_ylabel('MSE')
ax.legend()
```

### 2. Coverage Probability Plot
```python
# Coverage vs n with nominal level reference line
fig, ax = plt.subplots()
for i, method in enumerate(methods):
    ax.errorbar(n_vec, coverage[method], yerr=2*mc_se[method],
                fmt='o-', color=CB_COLORS[i], label=method, capsize=3)
ax.axhline(y=0.95, color='black', linestyle='--', linewidth=0.8, label='Nominal')
ax.set_xlabel('Sample size $n$')
ax.set_ylabel('Coverage probability')
ax.set_ylim([0.88, 1.0])
ax.legend()
```

### 3. Power Curves
```python
# Power vs effect size for competing tests
fig, ax = plt.subplots()
for i, method in enumerate(methods):
    ax.plot(effect_sizes, power[method], 'o-', color=CB_COLORS[i], label=method)
ax.axhline(y=0.05, color='black', linestyle=':', linewidth=0.8, label='Size')
ax.set_xlabel('Effect size $\\delta$')
ax.set_ylabel('Rejection probability')
ax.legend()
```

### 4. Box Plots (Estimate Distributions)
```python
# Distribution of estimates across replications
fig, axes = plt.subplots(1, len(n_vec), figsize=(3*len(n_vec), 4), sharey=True)
for j, n in enumerate(n_vec):
    data = [estimates[method][n] for method in methods]
    bp = axes[j].boxplot(data, labels=methods)
    axes[j].axhline(y=true_value, color='red', linestyle='--', linewidth=0.8)
    axes[j].set_title(f'$n = {n}$')
```

### 5. MCMC Trace Plots
```python
# Trace plots for MCMC diagnostics
fig, axes = plt.subplots(n_params, 2, figsize=(10, 2.5*n_params))
for i, param in enumerate(params):
    # Trace plot
    for chain in range(n_chains):
        axes[i, 0].plot(samples[chain][:, i], alpha=0.7)
    axes[i, 0].set_ylabel(param)
    # Density plot
    for chain in range(n_chains):
        axes[i, 1].density(samples[chain][:, i], alpha=0.7)
```

### 6. QQ Plots
```python
# QQ plot to verify distributional assumption
from scipy import stats
fig, ax = plt.subplots()
stats.probplot(residuals, dist="norm", plot=ax)
ax.set_title('Normal Q-Q Plot')
```

## Output Requirements

1. **Format**: PDF vector graphics (for LaTeX) + PNG rasterized (for preview)
2. **Resolution**: 300 DPI for raster elements
3. **Colors**: Colorblind-safe palette (CB_COLORS above)
4. **LaTeX integration**: Generate include snippets
   ```latex
   \begin{figure}[t]
   \centering
   \includegraphics[width=\textwidth]{figures/coverage_plot.pdf}
   \caption{Empirical coverage probabilities of 95\% confidence intervals...}
   \label{fig:coverage}
   \end{figure}
   ```
5. **Standalone scripts**: Each figure has its own reproducible script
6. **Consistent styling**: All figures in the paper should match

## Publication Checklist

- [ ] Font size readable when printed (≥ 8pt for smallest text)
- [ ] Colorblind-safe colors used
- [ ] Axis labels include units/description and use LaTeX math mode
- [ ] Legend doesn't obscure data
- [ ] Reference lines (nominal level, true value) clearly marked
- [ ] Monte Carlo error bars included where applicable
- [ ] PDF output for LaTeX, not PNG/JPG
- [ ] Figure caption is informative (can understand the figure without reading the paper)
- [ ] No unnecessary 3D plots or chartjunk
- [ ] Consistent style across all figures in the paper

## Key Rules

- Statistics figures should be clean and informative, not flashy
- Always include reference lines (nominal coverage, true parameter value, theoretical rate)
- Always include error bars or confidence bands when based on simulation
- Log-log plots for convergence rates — the slope tells the story
- Use the SAME color for the SAME method across all figures
- Label axes with mathematical notation using LaTeX
- Caption should state what the figure shows AND what the reader should conclude
