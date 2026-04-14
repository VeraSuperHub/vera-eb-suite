required_packages <- c("lavaan", "ggplot2")

if (is.null(getOption("repos")) || identical(getOption("repos")[["CRAN"]], "@CRAN@")) {
  options(repos = c(CRAN = "https://cloud.r-project.org"))
}

ensure_package <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    tryCatch(install.packages(pkg, dependencies = TRUE), error = function(e) stop("Package install failed (network may be unavailable). Please install required packages manually before running this example.", call. = FALSE))
  }
}

invisible(lapply(required_packages, ensure_package))

# lavaan queries parallel::detectCores() while building its defaults; on some
# sandboxed macOS environments this returns NA and aborts model fitting.
if (is.na(suppressWarnings(tryCatch(parallel::detectCores(), error = function(e) NA_integer_)))) {
  assignInNamespace(
    "detectCores",
    function(all.tests = FALSE, logical = TRUE) 2L,
    ns = "parallel"
  )
}

library(lavaan)
library(ggplot2)

fmt_p <- function(p) {
  if (is.na(p)) {
    "NA"
  } else if (p < 0.001) {
    "< .001"
  } else {
    paste0("= ", sprintf("%.3f", p))
  }
}

describe_fit <- function(fm) {
  if (fm["cfi"] >= 0.95 && fm["rmsea"] <= 0.06 && fm["srmr"] <= 0.08) {
    "good"
  } else if (fm["cfi"] >= 0.90 && fm["rmsea"] <= 0.10 && fm["srmr"] <= 0.08) {
    "adequate"
  } else {
    "suboptimal"
  }
}

dir.create("output", showWarnings = FALSE)
dir.create("output/tables", showWarnings = FALSE, recursive = TRUE)
dir.create("output/figures", showWarnings = FALSE, recursive = TRUE)

data("PoliticalDemocracy", package = "lavaan")
dat <- PoliticalDemocracy

model <- "
ind60 =~ x1 + x2 + x3
dem60 =~ y1 + a*y2 + b*y3 + c*y4
dem65 =~ y5 + a*y6 + b*y7 + c*y8

dem60 ~ a1*ind60
dem65 ~ c1*ind60 + b1*dem60

y1 ~~ y5
y2 ~~ y4 + y6
y3 ~~ y7
y4 ~~ y8
y6 ~~ y8

indirect := a1*b1
total := c1 + (a1*b1)
"

fit <- sem(model, data = dat)

fit_measures <- fitMeasures(
  fit,
  c("chisq", "df", "pvalue", "cfi", "tli", "rmsea", "rmsea.ci.lower", "rmsea.ci.upper", "srmr")
)

pe <- parameterEstimates(fit, standardized = TRUE)
paths <- pe[pe$op == "~", c("lhs", "rhs", "est", "se", "pvalue", "std.all")]
effects <- pe[pe$op == ":=", c("lhs", "est", "se", "z", "pvalue")]
loadings <- pe[pe$op == "=~", c("lhs", "rhs", "est", "se", "pvalue", "std.all")]

write.csv(as.data.frame(as.list(fit_measures)), "output/tables/fit_indices.csv", row.names = FALSE)
write.csv(paths, "output/tables/structural_paths.csv", row.names = FALSE)
write.csv(effects, "output/tables/indirect_effects.csv", row.names = FALSE)
write.csv(loadings, "output/tables/loadings.csv", row.names = FALSE)

n_obs <- nobs(fit)
estimator <- lavInspect(fit, "options")$estimator
fit_label <- describe_fit(fit_measures)
r2_values <- lavInspect(fit, "rsquare")
dem60_row <- paths[paths$lhs == "dem60" & paths$rhs == "ind60", ][1, ]
dem65_direct_row <- paths[paths$lhs == "dem65" & paths$rhs == "ind60", ][1, ]
dem65_mediator_row <- paths[paths$lhs == "dem65" & paths$rhs == "dem60", ][1, ]
indirect_row <- effects[effects$lhs == "indirect", ][1, ]
total_row <- effects[effects$lhs == "total", ][1, ]

paths$Label <- paste(paths$lhs, "~", paths$rhs)
p_paths <- ggplot(paths, aes(x = reorder(Label, std.all), y = std.all)) +
  geom_col(fill = "#4A90D9") +
  coord_flip() +
  theme_minimal(base_size = 12) +
  labs(
    title = "Standardized Structural Paths",
    x = "",
    y = "Standardized Estimate"
  )

ggsave("output/figures/plot_01_structural_paths.png", p_paths, width = 8, height = 5, dpi = 300)

methods_text <- paste0(
  "## Methods\n\n",
  "A full structural equation model was fit in R using lavaan on ",
  n_obs,
  " observations from the PoliticalDemocracy dataset. The model included one ",
  "exogenous latent factor (industrialization in 1960), one mediator latent factor ",
  "(democracy in 1960), and one outcome latent factor (democracy in 1965). Equality ",
  "constraints were applied to parallel loadings across the two democracy factors, ",
  "and selected residual covariances followed the standard tutorial specification. ",
  "The model was estimated with ",
  estimator,
  ". Global fit was evaluated using chi-square, CFI, TLI, RMSEA with 90% confidence ",
  "interval, and SRMR. Structural interpretation focused on direct, indirect, and total effects.\n"
)

results_text <- sprintf(
  paste0(
    "## Results\n\n",
    "The SEM converged successfully in N = %d and showed %s fit, chi-square(%d) = %.2f, ",
    "p %s, CFI = %.3f, TLI = %.3f, RMSEA = %.3f (90%% CI [%.3f, %.3f]), and SRMR = %.3f. ",
    "Industrialization was positively associated with democracy in 1960 (b = %.3f, standardized = %.3f, p %s), ",
    "and democracy in 1960 was strongly associated with democracy in 1965 (b = %.3f, standardized = %.3f, p %s). ",
    "The direct path from industrialization to democracy in 1965 remained statistically significant ",
    "(b = %.3f, standardized = %.3f, p %s), consistent with partial mediation. The estimated indirect ",
    "effect was %.3f (p %s), and the total effect was %.3f (p %s). The model explained %.3f of the variance ",
    "in democracy in 1960 and %.3f of the variance in democracy in 1965.\n"
  ),
  n_obs,
  fit_label,
  as.integer(fit_measures["df"]),
  fit_measures["chisq"],
  fmt_p(fit_measures["pvalue"]),
  fit_measures["cfi"],
  fit_measures["tli"],
  fit_measures["rmsea"],
  fit_measures["rmsea.ci.lower"],
  fit_measures["rmsea.ci.upper"],
  fit_measures["srmr"],
  dem60_row$est,
  dem60_row$std.all,
  fmt_p(dem60_row$pvalue),
  dem65_mediator_row$est,
  dem65_mediator_row$std.all,
  fmt_p(dem65_mediator_row$pvalue),
  dem65_direct_row$est,
  dem65_direct_row$std.all,
  fmt_p(dem65_direct_row$pvalue),
  indirect_row$est,
  fmt_p(indirect_row$pvalue),
  total_row$est,
  fmt_p(total_row$pvalue),
  r2_values["dem60"],
  r2_values["dem65"]
)

references_text <- paste0(
  "@article{rosseel2012,\n",
  "  author = {Rosseel, Yves},\n",
  "  title = {lavaan: An R Package for Structural Equation Modeling},\n",
  "  journal = {Journal of Statistical Software},\n",
  "  volume = {48},\n",
  "  number = {2},\n",
  "  pages = {1--36},\n",
  "  year = {2012}\n",
  "}\n\n",
  "@book{kline2023,\n",
  "  author = {Kline, Rex B.},\n",
  "  title = {Principles and Practice of Structural Equation Modeling},\n",
  "  edition = {5th},\n",
  "  publisher = {Guilford Press},\n",
  "  year = {2023}\n",
  "}\n"
)

writeLines(methods_text, "output/methods.md")
writeLines(results_text, "output/results.md")
writeLines(references_text, "output/references.bib")

cat("Full SEM model complete.\n")
cat(sprintf("CFI = %.3f, RMSEA = %.3f, indirect = %.3f\n", fit_measures["cfi"], fit_measures["rmsea"], effects$est[effects$lhs == "indirect"]))
cat("Outputs written to output/\n")
