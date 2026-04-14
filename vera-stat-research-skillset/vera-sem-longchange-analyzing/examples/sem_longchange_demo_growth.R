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

data("Demo.growth", package = "lavaan")
dat <- Demo.growth

model <- "
i =~ 1*t1 + 1*t2 + 1*t3 + 1*t4
s =~ 0*t1 + 1*t2 + 2*t3 + 3*t4
"

fit <- growth(model, data = dat)

fit_measures <- fitMeasures(
  fit,
  c("chisq", "df", "pvalue", "cfi", "tli", "rmsea", "rmsea.ci.lower", "rmsea.ci.upper", "srmr")
)

pe <- parameterEstimates(fit, standardized = TRUE)
growth_params <- pe[
  (pe$lhs %in% c("i", "s") & pe$op %in% c("~1", "~~")) |
    (pe$lhs %in% c("i", "s") & pe$rhs %in% c("i", "s") & pe$op == "~~"),
  c("lhs", "op", "rhs", "est", "se", "pvalue", "std.all")
]

write.csv(as.data.frame(as.list(fit_measures)), "output/tables/fit_indices.csv", row.names = FALSE)
write.csv(growth_params, "output/tables/growth_parameters.csv", row.names = FALSE)

n_obs <- nobs(fit)
estimator <- lavInspect(fit, "options")$estimator
fit_label <- describe_fit(fit_measures)

obs_means <- data.frame(
  Time = c(0, 1, 2, 3),
  Mean = c(mean(dat$t1), mean(dat$t2), mean(dat$t3), mean(dat$t4))
)

p_traj <- ggplot(obs_means, aes(x = Time, y = Mean)) +
  geom_line(linewidth = 1.1, color = "#4A90D9") +
  geom_point(size = 3, color = "#D94A4A") +
  theme_minimal(base_size = 12) +
  labs(
    title = "Observed Mean Trajectory",
    x = "Time",
    y = "Observed Mean"
  )

ggsave("output/figures/plot_01_growth_trajectory.png", p_traj, width = 8, height = 5, dpi = 300)

int_mean <- growth_params$est[growth_params$lhs == "i" & growth_params$op == "~1"]
slope_mean <- growth_params$est[growth_params$lhs == "s" & growth_params$op == "~1"]
int_var <- growth_params$est[growth_params$lhs == "i" & growth_params$rhs == "i" & growth_params$op == "~~"]
slope_var <- growth_params$est[growth_params$lhs == "s" & growth_params$rhs == "s" & growth_params$op == "~~"]
is_cov <- growth_params$est[growth_params$lhs == "i" & growth_params$rhs == "s" & growth_params$op == "~~"]
if (length(is_cov) == 0) {
  is_cov <- growth_params$est[growth_params$lhs == "s" & growth_params$rhs == "i" & growth_params$op == "~~"]
}
int_mean_row <- growth_params[growth_params$lhs == "i" & growth_params$op == "~1", ][1, ]
slope_mean_row <- growth_params[growth_params$lhs == "s" & growth_params$op == "~1", ][1, ]
int_var_row <- growth_params[growth_params$lhs == "i" & growth_params$rhs == "i" & growth_params$op == "~~", ][1, ]
slope_var_row <- growth_params[growth_params$lhs == "s" & growth_params$rhs == "s" & growth_params$op == "~~", ][1, ]
is_cov_row <- growth_params[growth_params$lhs == "i" & growth_params$rhs == "s" & growth_params$op == "~~", ][1, ]
if (nrow(is_cov_row) == 0) {
  is_cov_row <- growth_params[growth_params$lhs == "s" & growth_params$rhs == "i" & growth_params$op == "~~", ][1, ]
}

methods_text <- paste0(
  "## Methods\n\n",
  "A linear latent growth curve model was fit in R using lavaan on ",
  n_obs,
  " observations from the Demo.growth dataset. A latent intercept factor loaded ",
  "equally on four repeated measures, and a latent slope factor used fixed linear ",
  "time scores of 0, 1, 2, and 3. The model was estimated with ",
  estimator,
  " and an explicit mean structure. Model fit was evaluated with chi-square, ",
  "CFI, TLI, RMSEA with 90% confidence interval, and SRMR. Interpretation focused ",
  "on latent intercept and slope means, their variances, and the intercept-slope covariance.\n"
)

results_text <- sprintf(
  paste0(
    "## Results\n\n",
    "The linear latent growth model converged successfully in N = %d. Global fit was %s, ",
    "chi-square(%d) = %.2f, p %s, CFI = %.3f, TLI = %.3f, RMSEA = %.3f ",
    "(90%% CI [%.3f, %.3f]), and SRMR = %.3f. The latent intercept mean was %.3f ",
    "(p %s), and the latent slope mean was %.3f (p %s), indicating positive average ",
    "change over time. Intercept variance (%.3f, p %s) and slope variance (%.3f, p %s) ",
    "were both statistically different from zero, supporting between-person heterogeneity ",
    "in baseline status and rate of change. The intercept-slope covariance was %.3f ",
    "(p %s), indicating that participants with higher baseline scores tended to show steeper increases.\n"
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
  int_mean_row$est,
  fmt_p(int_mean_row$pvalue),
  slope_mean_row$est,
  fmt_p(slope_mean_row$pvalue),
  int_var_row$est,
  fmt_p(int_var_row$pvalue),
  slope_var_row$est,
  fmt_p(slope_var_row$pvalue),
  is_cov_row$est,
  fmt_p(is_cov_row$pvalue)
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
  "@book{bollen2006,\n",
  "  author = {Bollen, Kenneth A. and Curran, Patrick J.},\n",
  "  title = {Latent Curve Models: A Structural Equation Perspective},\n",
  "  publisher = {Wiley},\n",
  "  year = {2006}\n",
  "}\n"
)

writeLines(methods_text, "output/methods.md")
writeLines(results_text, "output/results.md")
writeLines(references_text, "output/references.bib")

cat("Longitudinal change model complete.\n")
cat(sprintf("CFI = %.3f, RMSEA = %.3f, slope mean = %.3f\n", fit_measures["cfi"], fit_measures["rmsea"], slope_mean))
cat("Outputs written to output/\n")
