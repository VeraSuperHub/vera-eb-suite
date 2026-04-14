## Methods

A full structural equation model was fit in R using lavaan on 75 observations from the PoliticalDemocracy dataset. The model included one exogenous latent factor (industrialization in 1960), one mediator latent factor (democracy in 1960), and one outcome latent factor (democracy in 1965). Equality constraints were applied to parallel loadings across the two democracy factors, and selected residual covariances followed the standard tutorial specification. The model was estimated with ML. Global fit was evaluated using chi-square, CFI, TLI, RMSEA with 90% confidence interval, and SRMR. Structural interpretation focused on direct, indirect, and total effects.

