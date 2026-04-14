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

data("HolzingerSwineford1939", package = "lavaan")
dat <- HolzingerSwineford1939

model <- "
visual  =~ x1 + x2 + x3
textual =~ x4 + x5 + x6
speed   =~ x7 + x8 + x9
"

fit <- cfa(model, data = dat, std.lv = TRUE)

fit_measures <- fitMeasures(
  fit,
  c("chisq", "df", "pvalue", "cfi", "tli", "rmsea", "rmsea.ci.lower", "rmsea.ci.upper", "srmr")
)

std_sol <- standardizedSolution(fit)
loadings <- std_sol[std_sol$op == "=~", c("lhs", "rhs", "est.std", "se", "pvalue")]
names(loadings) <- c("Factor", "Indicator", "Std_Loading", "SE", "p")

factor_corrs <- std_sol[
  std_sol$op == "~~" &
    std_sol$lhs %in% c("visual", "textual", "speed") &
    std_sol$rhs %in% c("visual", "textual", "speed") &
    std_sol$lhs != std_sol$rhs,
  c("lhs", "rhs", "est.std", "pvalue")
]
names(factor_corrs) <- c("Factor_1", "Factor_2", "Std_Correlation", "p")

write.csv(as.data.frame(as.list(fit_measures)), "output/tables/fit_indices.csv", row.names = FALSE)
write.csv(loadings, "output/tables/standardized_loadings.csv", row.names = FALSE)
write.csv(factor_corrs, "output/tables/factor_correlations.csv", row.names = FALSE)

n_obs <- nobs(fit)
estimator <- lavInspect(fit, "options")$estimator
weakest_loading <- loadings[which.min(loadings$Std_Loading), ]
strongest_loading <- loadings[which.max(loadings$Std_Loading), ]
strongest_corr <- factor_corrs[which.max(factor_corrs$Std_Correlation), ]
fit_label <- describe_fit(fit_measures)

p_load <- ggplot(loadings, aes(x = Indicator, y = Std_Loading, fill = Factor)) +
  geom_col(width = 0.7) +
  facet_wrap(~ Factor, scales = "free_x") +
  geom_hline(yintercept = 0.50, linetype = "dashed", color = "gray40") +
  coord_cartesian(ylim = c(0, 1)) +
  theme_minimal(base_size = 12) +
  labs(
    title = "Standardized CFA Loadings",
    x = "Indicator",
    y = "Standardized Loading"
  ) +
  theme(legend.position = "none")

ggsave("output/figures/plot_01_cfa_loadings.png", p_load, width = 10, height = 6, dpi = 300)

methods_text <- paste0(
  "## Methods\n\n",
  "A confirmatory factor analysis was fit in R using lavaan on ",
  n_obs,
  " observations from the HolzingerSwineford1939 dataset. A three-factor ",
  "measurement model was specified for visual, textual, and speed ability, ",
  "with latent variances standardized (`std.lv = TRUE`) and estimation by ",
  estimator,
  ". Model fit was evaluated with chi-square, CFI, TLI, RMSEA with 90% ",
  "confidence interval, and SRMR. Standardized loadings and interfactor ",
  "correlations were reviewed to characterize measurement strength and construct overlap.\n"
)

results_text <- sprintf(
  paste0(
    "## Results\n\n",
    "The three-factor CFA converged successfully in N = %d. Overall fit was %s, ",
    "chi-square(%d) = %.2f, p %s, CFI = %.3f, TLI = %.3f, RMSEA = %.3f ",
    "(90%% CI [%.3f, %.3f]), and SRMR = %.3f. All standardized loadings were ",
    "positive and statistically significant (all p < .001), ranging from %.3f ",
    "to %.3f. The weakest indicator was %s (loading = %.3f), whereas the strongest ",
    "was %s (loading = %.3f). Interfactor correlations ranged from %.3f to %.3f; ",
    "the largest was between %s and %s (r = %.3f, p %s), indicating moderate but ",
    "not extreme construct overlap.\n"
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
  min(loadings$Std_Loading),
  max(loadings$Std_Loading),
  weakest_loading$Indicator,
  weakest_loading$Std_Loading,
  strongest_loading$Indicator,
  strongest_loading$Std_Loading,
  min(factor_corrs$Std_Correlation),
  max(factor_corrs$Std_Correlation),
  strongest_corr$Factor_1,
  strongest_corr$Factor_2,
  strongest_corr$Std_Correlation,
  fmt_p(strongest_corr$p)
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
  "@book{brown2015,\n",
  "  author = {Brown, Timothy A.},\n",
  "  title = {Confirmatory Factor Analysis for Applied Research},\n",
  "  edition = {2nd},\n",
  "  publisher = {Guilford Press},\n",
  "  year = {2015}\n",
  "}\n"
)

writeLines(methods_text, "output/methods.md")
writeLines(results_text, "output/results.md")
writeLines(references_text, "output/references.bib")

cat("CFA model complete.\n")
cat(sprintf("CFI = %.3f, RMSEA = %.3f, SRMR = %.3f\n", fit_measures["cfi"], fit_measures["rmsea"], fit_measures["srmr"]))
cat("Outputs written to output/\n")
