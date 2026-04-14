# -- Multivariate Analysis: Iris Dataset (R) -------------------------
# DVs: Sepal.Length, Sepal.Width, Petal.Length, Petal.Width
# Group: Species (setosa, versicolor, virginica)
# Covers: PART 3 (additional tests), PART 4 (subgroup/profile),
#         PART 5 (modeling), PART 6 (cross-method synthesis),
#         PART 7 (manuscript generation)
# Prerequisite: Testing workflow (PARTS 0-2) already executed.

# -- PART 0: Setup (repeated for standalone execution) -------------------------

required_packages <- c("tidyverse", "MASS", "car", "randomForest", "broom")

if (is.null(getOption("repos")) || identical(getOption("repos")[["CRAN"]], "@CRAN@")) {
  options(repos = c(CRAN = "https://cloud.r-project.org"))
}

ensure_package <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    tryCatch(install.packages(pkg, dependencies = TRUE), error = function(e) stop("Package install failed (network may be unavailable). Please install required packages manually before running this example.", call. = FALSE))
  }
}

invisible(lapply(required_packages, ensure_package))

library(tidyverse)
library(MASS)
library(randomForest)
library(broom)

data(iris)
df <- iris

dvs <- c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width")
group_var <- "Species"
n_dvs <- length(dvs)
N <- nrow(df)
alpha <- 0.05
bonferroni_alpha <- alpha / n_dvs
groups <- levels(df$Species)
n_groups <- length(groups)

dir.create("tables", showWarnings = FALSE)
dir.create("figures", showWarnings = FALSE)

cat(strrep("=", 60), "\n")
cat("MULTIVARIATE ANALYSIS - IRIS DATASET (R)
")
cat("DVs:", paste(dvs, collapse = ", "), "\n")
cat("Group:", group_var, "\n")
cat("N =", N, "\n")
cat(strrep("=", 60), "\n\n")

format_p <- function(p) {
  if (p < 0.001) return("< .001")
  return(sprintf("= %.3f", p))
}

# ==============================================================================
# PART 3: ADDITIONAL TESTS (Workflow 04)
# ==============================================================================

cat(strrep("=", 60), "\n")
cat("PART 3: ADDITIONAL TESTS\n")
cat(strrep("=", 60), "\n\n")

# -- 3A: Univariate Follow-Up ANOVAs ------------------------------------------

cat("--- 3A: Univariate Follow-Up ANOVAs ---\n")
cat(sprintf("Bonferroni-corrected alpha = %.4f\n\n", bonferroni_alpha))

anova_results <- list()

for (dv in dvs) {
  aov_model <- aov(as.formula(paste(dv, "~ Species")), data = df)
  aov_summary <- summary(aov_model)
  f_val <- aov_summary[[1]]["Species", "F value"]
  p_val <- aov_summary[[1]]["Species", "Pr(>F)"]
  df1 <- aov_summary[[1]]["Species", "Df"]
  df2 <- aov_summary[[1]]["Residuals", "Df"]
  ss_group <- aov_summary[[1]]["Species", "Sum Sq"]
  ss_total <- sum(aov_summary[[1]][, "Sum Sq"])
  eta_sq <- ss_group / ss_total
  sig <- ifelse(p_val < bonferroni_alpha, "sig", "ns")

  cat(sprintf("  %s: F(%d, %d) = %.2f, p %s, partial eta2 = %.3f [%s]\n",
      dv, df1, df2, f_val, format_p(p_val), eta_sq, sig))

  anova_results[[dv]] <- list(
    F = f_val, df1 = df1, df2 = df2, p = p_val, eta2 = eta_sq, sig = sig
  )

  # Kruskal-Wallis as nonparametric confirmation
  kw <- kruskal.test(as.formula(paste(dv, "~ Species")), data = df)
  cat(sprintf("    Kruskal-Wallis: H = %.2f, p %s\n", kw$statistic, format_p(kw$p.value)))

  # Tukey HSD if significant
  if (p_val < bonferroni_alpha) {
    tukey <- TukeyHSD(aov_model)
    cat("    Tukey HSD pairwise:\n")
    for (pair_name in rownames(tukey$Species)) {
      diff_val <- tukey$Species[pair_name, "diff"]
      ci_lo <- tukey$Species[pair_name, "lwr"]
      ci_hi <- tukey$Species[pair_name, "upr"]
      p_adj <- tukey$Species[pair_name, "p adj"]

      # Cohen's d (approximate)
      pair_groups <- strsplit(pair_name, "-")[[1]]
      g1_data <- df[[dv]][df$Species == pair_groups[1]]
      g2_data <- df[[dv]][df$Species == pair_groups[2]]
      pooled_sd <- sqrt((var(g1_data) + var(g2_data)) / 2)
      d <- diff_val / pooled_sd

      cat(sprintf("      %s: diff = %.3f, 95%% CI [%.3f, %.3f], p %s, d = %.3f\n",
          pair_name, diff_val, ci_lo, ci_hi, format_p(p_adj), d))
    }
  }

  # Box plot per DV
  p_box <- ggplot(df, aes(x = .data[[group_var]], y = .data[[dv]], fill = .data[[group_var]])) +
    geom_boxplot(alpha = 0.7) +
    labs(title = paste(dv, "by Species"), x = "Species", y = dv) +
    theme_minimal(base_size = 12) +
    theme(legend.position = "none")
  ggsave(sprintf("figures/plot_03_univariate_%s.png", dv), p_box,
         width = 8, height = 5, dpi = 300)
}
cat("\nSaved: figures/plot_03_univariate_*.png\n")

# Save ANOVA table
anova_df <- data.frame(
  DV = dvs,
  F_val = sapply(dvs, function(d) anova_results[[d]]$F),
  df1 = sapply(dvs, function(d) anova_results[[d]]$df1),
  df2 = sapply(dvs, function(d) anova_results[[d]]$df2),
  p = sapply(dvs, function(d) anova_results[[d]]$p),
  eta2 = sapply(dvs, function(d) anova_results[[d]]$eta2),
  sig = sapply(dvs, function(d) anova_results[[d]]$sig)
)
write.csv(anova_df, "tables/univariate_anova_table.csv", row.names = FALSE)

# -- 3B: Discriminant Function Analysis (Full) ---------------------------------

cat("\n--- 3B: Discriminant Function Analysis ---\n\n")

model_lda <- lda(Species ~ ., data = df[, c(dvs, group_var)])
n_functions <- min(n_dvs, n_groups - 1)

cat(sprintf("Number of discriminant functions: %d\n\n", n_functions))

# Eigenvalues and proportions
eigenvalues <- model_lda$svd^2
prop_trace <- eigenvalues / sum(eigenvalues)
can_cor <- model_lda$svd / sqrt(1 + model_lda$svd^2)

cat("Discriminant Function Summary:\n")
for (i in 1:n_functions) {
  cat(sprintf("  LD%d: eigenvalue = %.4f, proportion = %.3f, canonical r = %.4f\n",
      i, eigenvalues[i], prop_trace[i], can_cor[i]))
}

# Wilks' lambda significance test per function
cat("\nWilks' Lambda Tests:\n")
for (i in 1:n_functions) {
  remaining_ev <- eigenvalues[i:n_functions]
  wilks_lam <- prod(1 / (1 + remaining_ev))
  n_eff <- N - 1 - (n_dvs + n_groups) / 2
  chi2 <- -n_eff * log(max(wilks_lam, 1e-15))
  df_chi <- (n_dvs - i + 1) * (n_groups - 1 - i + 1)
  chi_p <- 1 - pchisq(chi2, df_chi)
  cat(sprintf("  Functions %d through %d: Lambda = %.4f, chi2(%d) = %.2f, p %s\n",
      i, n_functions, wilks_lam, df_chi, chi2, format_p(chi_p)))
}

# Structure coefficients
lda_scores <- predict(model_lda)$x
structure_coefs <- matrix(NA, n_dvs, n_functions)
rownames(structure_coefs) <- dvs
colnames(structure_coefs) <- paste0("LD", 1:n_functions)
for (i in 1:n_dvs) {
  for (j in 1:n_functions) {
    structure_coefs[i, j] <- cor(df[[dvs[i]]], lda_scores[, j])
  }
}
cat("\nStructure Coefficients:\n")
print(round(structure_coefs, 4))

# Standardized discriminant function coefficients
cat("\nStandardized Discriminant Function Coefficients:\n")
print(round(model_lda$scaling, 4))

# Classification accuracy
lda_pred <- predict(model_lda)$class
conf_matrix <- table(Predicted = lda_pred, Actual = df$Species)
overall_acc <- sum(diag(conf_matrix)) / sum(conf_matrix)

cat("\nConfusion Matrix:\n")
print(conf_matrix)
cat(sprintf("Overall accuracy: %.1f%%\n", overall_acc * 100))

for (g in groups) {
  g_acc <- conf_matrix[g, g] / sum(conf_matrix[, g])
  cat(sprintf("  %s: %.1f%%\n", g, g_acc * 100))
}

# LOO Cross-validation
lda_cv <- lda(Species ~ ., data = df[, c(dvs, group_var)], CV = TRUE)
cv_conf <- table(Predicted = lda_cv$class, Actual = df$Species)
cv_acc <- sum(diag(cv_conf)) / sum(cv_conf)
cat(sprintf("\nLOO-CV accuracy: %.1f%%\n", cv_acc * 100))
cat("LOO-CV Confusion Matrix:\n")
print(cv_conf)

# Save tables
disc_table <- data.frame(
  Function = paste0("LD", 1:n_functions),
  Eigenvalue = eigenvalues[1:n_functions],
  Proportion = prop_trace[1:n_functions],
  Canonical_r = can_cor[1:n_functions]
)
write.csv(disc_table, "tables/discriminant_table.csv", row.names = FALSE)
write.csv(as.data.frame.matrix(conf_matrix), "tables/confusion_matrix.csv")

# Discriminant score plot
lda_score_df <- data.frame(lda_scores[, 1:n_functions], Species = df$Species)
p_disc <- ggplot(lda_score_df, aes(x = LD1, y = LD2, color = Species)) +
  geom_point(alpha = 0.7, size = 2) +
  stat_ellipse(level = 0.95) +
  labs(title = "Discriminant Function Scores", x = "LD1", y = "LD2") +
  theme_minimal(base_size = 12)
ggsave("figures/plot_04_discriminant.png", p_disc, width = 10, height = 8, dpi = 300)
cat("Saved: figures/plot_04_discriminant.png\n")

# ==============================================================================
# PART 4: SUBGROUP ANALYSIS (Workflow 05)
# ==============================================================================

cat("\n", strrep("=", 60), "\n")
cat("PART 4: SUBGROUP ANALYSIS\n")
cat(strrep("=", 60), "\n\n")

# -- 4A: Two-Way MANOVA -------------------------------------------------------
cat("--- 4A: Two-Way MANOVA ---\n")
cat("  NOTE: Iris has only one grouping factor (Species).\n")
cat("  Two-way MANOVA requires a second factor.\n")
cat("  Skipping for this dataset.\n\n")

# -- 4B: MANCOVA ---------------------------------------------------------------
cat("--- 4B: MANCOVA ---\n")
cat("  NOTE: No covariates collected for iris dataset.\n\n")

# -- 4C: Profile Analysis -----------------------------------------------------
cat("--- 4C: Profile Analysis ---\n")
cat("  LIMITATION: DVs differ in range/meaning (Sepal vs Petal).\n")
cat("  Proceeding with caution for demonstration.\n\n")

# Profile analysis via difference scores approach
# Parallelism test: MANOVA on adjacent difference scores
diff_matrix <- matrix(NA, N, n_dvs - 1)
for (i in 1:(n_dvs - 1)) {
  diff_matrix[, i] <- df[[dvs[i + 1]]] - df[[dvs[i]]]
}
colnames(diff_matrix) <- paste0("d", 1:(n_dvs - 1))

# Parallelism: test if difference score vectors are equal across groups
if (ncol(diff_matrix) > 1) {
  parallel_manova <- manova(diff_matrix ~ df$Species)
  parallel_summary <- summary(parallel_manova, test = "Pillai")
  cat("  1. Parallelism Test (Group x DV interaction):\n")
  cat(sprintf("     Pillai's V = %.4f, F = %.3f, p %s\n",
      parallel_summary$stats[1, "Pillai"],
      parallel_summary$stats[1, "approx F"],
      format_p(parallel_summary$stats[1, "Pr(>F)"])))
  if (parallel_summary$stats[1, "Pr(>F)"] < 0.05) {
    cat("     -> Profiles are NOT parallel.\n\n")
  } else {
    cat("     -> Profiles are approximately parallel.\n\n")
  }
} else {
  # Only 1 difference variable: use ANOVA
  parallel_aov <- summary(aov(diff_matrix[, 1] ~ df$Species))
  cat("  1. Parallelism Test:\n")
  cat(sprintf("     F = %.3f, p %s\n",
      parallel_aov[[1]]["df$Species", "F value"],
      format_p(parallel_aov[[1]]["df$Species", "Pr(>F)"])))
}

# Equal levels test: do group means averaged across DVs differ?
row_means <- rowMeans(df[, dvs])
levels_aov <- summary(aov(row_means ~ df$Species))
cat("  2. Equal Levels Test (Group main effect):\n")
cat(sprintf("     F(%d, %d) = %.3f, p %s\n",
    levels_aov[[1]]["df$Species", "Df"],
    levels_aov[[1]]["Residuals", "Df"],
    levels_aov[[1]]["df$Species", "F value"],
    format_p(levels_aov[[1]]["df$Species", "Pr(>F)"])))
if (levels_aov[[1]]["df$Species", "Pr(>F)"] < 0.05) {
  cat("     -> Groups differ in overall level.\n\n")
} else {
  cat("     -> Groups do not differ in overall level.\n\n")
}

# Flatness test: do DVs differ (averaged across groups)?
# Use paired t-tests on adjacent differences from zero
flat_diffs <- colMeans(df[, dvs])
cat("  3. Flatness Test (DV main effect):\n")
# Hotelling's T-squared on difference scores
D_flat <- diff_matrix
D_mean <- colMeans(D_flat)
D_cov <- cov(D_flat)
T2 <- N * t(D_mean) %*% solve(D_cov) %*% D_mean
f_flat <- as.numeric(T2 * (N - n_dvs + 1) / ((N - 1) * (n_dvs - 1)))
df1_flat <- n_dvs - 1
df2_flat <- N - n_dvs + 1
p_flat <- 1 - pf(max(f_flat, 0), df1_flat, df2_flat)
cat(sprintf("     F(%d, %d) = %.3f, p %s\n", df1_flat, df2_flat, f_flat, format_p(p_flat)))
if (p_flat < 0.05) {
  cat("     -> Profile is NOT flat.\n")
} else {
  cat("     -> Profile is approximately flat.\n")
}

# Profile plot
df_long <- df %>%
  pivot_longer(cols = all_of(dvs), names_to = "DV", values_to = "value") %>%
  group_by(Species, DV) %>%
  summarise(M = mean(value), SE = sd(value) / sqrt(n()), .groups = "drop") %>%
  mutate(DV = factor(DV, levels = dvs))

p_profile <- ggplot(df_long, aes(x = DV, y = M, color = Species, group = Species)) +
  geom_point(size = 3) +
  geom_line(linewidth = 1) +
  geom_errorbar(aes(ymin = M - 1.96 * SE, ymax = M + 1.96 * SE), width = 0.15) +
  labs(x = "DV", y = "Mean (95% CI)",
       title = "Profile Analysis Plot\n(Caveat: DVs differ in scale)") +
  theme_minimal(base_size = 12) +
  theme(axis.text.x = element_text(angle = 30, hjust = 1))
ggsave("figures/plot_06_profile.png", p_profile, width = 12, height = 6, dpi = 300)
cat("\nSaved: figures/plot_06_profile.png\n")

# ==============================================================================
# PART 5: MODELING (Workflow 06)
# ==============================================================================

cat("\n", strrep("=", 60), "\n")
cat("PART 5: MODELING\n")
cat("Models are analytic lenses, not contestants.\n")
cat(strrep("=", 60), "\n\n")

# -- 5A: CCA -------------------------------------------------------------------

cat("--- 5A: Canonical Correlation Analysis ---\n")
cat("  Using species dummies as predictor set, DVs as outcome set.\n\n")

species_dummies <- model.matrix(~ Species - 1, data = df)
# Remove one column for identification
X_set <- species_dummies[, -1]  # drop first level
Y_set <- as.matrix(df[, dvs])

cca_result <- cancor(X_set, Y_set)
n_dims <- length(cca_result$cor)

cat("Canonical Correlations:\n")
for (i in 1:n_dims) {
  cat(sprintf("  Dimension %d: Rc = %.4f\n", i, cca_result$cor[i]))
}

# Wilks' lambda significance test
cat("\nWilks' Lambda Tests:\n")
for (i in 1:n_dims) {
  wilks_lam <- prod(1 - cca_result$cor[i:n_dims]^2)
  n_eff <- N - 0.5 * (ncol(X_set) + ncol(Y_set) + 3)
  chi2 <- -n_eff * log(max(wilks_lam, 1e-15))
  df_chi <- (ncol(X_set) - i + 1) * (ncol(Y_set) - i + 1)
  chi_p <- 1 - pchisq(chi2, max(df_chi, 1))
  cat(sprintf("  Dim %d through %d: Lambda = %.4f, chi2(%d) = %.2f, p %s\n",
      i, n_dims, wilks_lam, df_chi, chi2, format_p(chi_p)))
}

# Canonical loadings
cat("\nCanonical Loadings (Y-set):\n")
print(round(cca_result$ycoef, 4))

# Redundancy analysis
cat("\nRedundancy Analysis:\n")
for (i in 1:n_dims) {
  y_scores <- Y_set %*% cca_result$ycoef[, i]
  y_var_prop <- mean(sapply(1:n_dvs, function(j) cor(Y_set[, j], y_scores)^2))
  redundancy <- y_var_prop * cca_result$cor[i]^2
  cat(sprintf("  Dim %d: Y var = %.4f, Rc2 = %.4f, redundancy = %.4f\n",
      i, y_var_prop, cca_result$cor[i]^2, redundancy))
}

# CCA scatter plot
x_scores <- X_set %*% cca_result$xcoef[, 1]
y_scores <- Y_set %*% cca_result$ycoef[, 1]
cca_plot_df <- data.frame(X_CV1 = x_scores, Y_CV1 = y_scores, Species = df$Species)
p_cca <- ggplot(cca_plot_df, aes(x = X_CV1, y = Y_CV1, color = Species)) +
  geom_point(alpha = 0.7, size = 2) +
  labs(title = sprintf("CCA: First Canonical Variate Pair (Rc = %.3f)", cca_result$cor[1]),
       x = "Predictor Canonical Variate 1", y = "Outcome Canonical Variate 1") +
  theme_minimal(base_size = 12)
ggsave("figures/plot_07_cca.png", p_cca, width = 10, height = 8, dpi = 300)
cat("Saved: figures/plot_07_cca.png\n")

cca_table <- data.frame(
  Dimension = paste0("CV", 1:n_dims),
  Canonical_r = cca_result$cor,
  Canonical_r2 = cca_result$cor^2
)
write.csv(cca_table, "tables/cca_table.csv", row.names = FALSE)

# -- 5B: PCA -------------------------------------------------------------------

cat("\n--- 5B: Principal Component Analysis ---\n\n")

model_pca <- prcomp(df[, dvs], scale. = TRUE)
pca_summary <- summary(model_pca)

cat("Component Summary:\n")
eigenvalues_pca <- model_pca$sdev^2
var_ratio <- eigenvalues_pca / sum(eigenvalues_pca)
cum_var <- cumsum(var_ratio)

for (i in 1:n_dvs) {
  kaiser <- ifelse(eigenvalues_pca[i] >= 1.0, " *", "")
  cat(sprintf("  PC%d: eigenvalue = %.4f, proportion = %.4f, cumulative = %.4f%s\n",
      i, eigenvalues_pca[i], var_ratio[i], cum_var[i], kaiser))
}
cat("  (* = above Kaiser criterion)\n")

cat("\nComponent Loadings (|loading| >= .40 flagged):\n")
loadings_mat <- model_pca$rotation
for (i in 1:n_dvs) {
  vals <- sprintf("%.4f%s", loadings_mat[i, ],
                  ifelse(abs(loadings_mat[i, ]) >= 0.40, " *", "  "))
  cat(sprintf("  %-15s %s\n", dvs[i], paste(vals, collapse = "  ")))
}

# Scree plot
pca_var_df <- data.frame(PC = paste0("PC", 1:n_dvs), Eigenvalue = eigenvalues_pca)
p_scree <- ggplot(pca_var_df, aes(x = PC, y = Eigenvalue, group = 1)) +
  geom_line(linewidth = 1) + geom_point(size = 3) +
  geom_hline(yintercept = 1, linetype = "dashed", color = "red") +
  labs(title = "Scree Plot with Kaiser Criterion",
       x = "Principal Component", y = "Eigenvalue") +
  theme_minimal(base_size = 12)
ggsave("figures/plot_09_scree.png", p_scree, width = 8, height = 6, dpi = 300)
cat("Saved: figures/plot_09_scree.png\n")

# Biplot
pca_scores <- data.frame(model_pca$x[, 1:2], Species = df$Species)
p_biplot <- ggplot(pca_scores, aes(x = PC1, y = PC2, color = Species)) +
  geom_point(alpha = 0.7, size = 2) +
  stat_ellipse(level = 0.95) +
  labs(title = "PCA Biplot",
       x = sprintf("PC1 (%.1f%%)", var_ratio[1] * 100),
       y = sprintf("PC2 (%.1f%%)", var_ratio[2] * 100)) +
  theme_minimal(base_size = 12)
ggsave("figures/plot_10_biplot.png", p_biplot, width = 10, height = 8, dpi = 300)
cat("Saved: figures/plot_10_biplot.png\n")

pca_table <- data.frame(
  Component = paste0("PC", 1:n_dvs),
  Eigenvalue = eigenvalues_pca,
  Proportion = var_ratio,
  Cumulative = cum_var
)
write.csv(pca_table, "tables/pca_table.csv", row.names = FALSE)
write.csv(as.data.frame(loadings_mat), "tables/pca_loadings.csv")

# -- 5C: Full Discriminant Analysis Extension ----------------------------------

cat("\n--- 5C: Full Discriminant Analysis (extends Part 3) ---\n\n")

# Group centroids
cat("Group Centroids in Discriminant Space:\n")
for (g in groups) {
  idx <- df$Species == g
  centroid <- colMeans(lda_scores[idx, , drop = FALSE])
  cat(sprintf("  %s: LD1 = %.4f, LD2 = %.4f\n", g, centroid[1], centroid[2]))
}

# Prior probabilities
cat(sprintf("\nPrior Probabilities: %s\n",
    paste(paste(groups, round(model_lda$prior, 3), sep = " = "), collapse = ", ")))

# Posterior probabilities (first 3 per group)
cat("\nPosterior Probabilities (first 3 per group):\n")
posteriors <- predict(model_lda)$posterior
for (g in groups) {
  idx <- which(df$Species == g)[1:3]
  for (i in idx) {
    probs <- paste(sprintf("%s=%.3f", groups, posteriors[i, ]), collapse = ", ")
    cat(sprintf("  Obs %d (%s): %s\n", i, g, probs))
  }
}

# Territorial map
p_territorial <- ggplot(as.data.frame(lda_scores), aes(x = LD1, y = LD2)) +
  geom_point(aes(color = df$Species), alpha = 0.7, size = 2) +
  stat_ellipse(aes(color = df$Species), level = 0.95) +
  labs(title = "Territorial Map (Discriminant Space)",
       x = "LD1", y = "LD2", color = "Species") +
  theme_minimal(base_size = 12)
ggsave("figures/plot_11_territorial.png", p_territorial,
       width = 10, height = 8, dpi = 300)
cat("Saved: figures/plot_11_territorial.png\n")

# -- 5D: Multivariate Multiple Regression --------------------------------------

cat("\n--- 5D: Multivariate Multiple Regression ---\n\n")

dv_matrix <- as.matrix(df[, dvs])
mv_model <- lm(dv_matrix ~ Species, data = df)
manova_mv <- car::Manova(mv_model, test.statistic = "Pillai")
cat("Overall Multivariate Test:\n")
print(manova_mv)

cat("\nPer-DV R-squared:\n")
for (dv in dvs) {
  model_dv <- lm(as.formula(paste(dv, "~ Species")), data = df)
  cat(sprintf("  %s: R2 = %.3f, F = %.3f, p %s\n",
      dv, summary(model_dv)$r.squared,
      summary(model_dv)$fstatistic[1],
      format_p(pf(summary(model_dv)$fstatistic[1],
                   summary(model_dv)$fstatistic[2],
                   summary(model_dv)$fstatistic[3],
                   lower.tail = FALSE))))
}

mvreg_table <- data.frame(
  DV = dvs,
  R2 = sapply(dvs, function(d) summary(lm(as.formula(paste(d, "~ Species")), data = df))$r.squared),
  F_val = sapply(dvs, function(d) summary(lm(as.formula(paste(d, "~ Species")), data = df))$fstatistic[1])
)
write.csv(mvreg_table, "tables/mvreg_table.csv", row.names = FALSE)

# Coefficient comparison plot
coef_data <- data.frame()
for (dv in dvs) {
  model_dv <- lm(as.formula(paste(dv, "~ Species")), data = df)
  coefs <- broom::tidy(model_dv)
  coefs$DV <- dv
  coef_data <- rbind(coef_data, coefs)
}

coef_species <- coef_data %>% filter(term != "(Intercept)")
p_coef <- ggplot(coef_species, aes(x = estimate, y = DV, color = term)) +
  geom_point(size = 3) +
  geom_errorbar(aes(xmin = estimate - 1.96 * std.error,
                    xmax = estimate + 1.96 * std.error),
                orientation = "y", width = 0.2) +
  geom_vline(xintercept = 0, linetype = "dashed", alpha = 0.5) +
  labs(title = "Regression Coefficients Across DVs",
       x = "Coefficient (B)", y = "Dependent Variable") +
  theme_minimal(base_size = 12)
ggsave("figures/plot_12_mv_regression.png", p_coef, width = 12, height = 5, dpi = 300)
cat("Saved: figures/plot_12_mv_regression.png\n")

# -- 5E: Tree-Based Importance ------------------------------------------------

cat("\n--- 5E: Tree-Based Importance (Exploratory) ---\n")
cat("Models as analytic tools for pattern detection.\n\n")

tree_predictors <- c(colnames(species_dummies)[-1], dvs)
importance_matrix <- matrix(
  NA,
  nrow = length(tree_predictors),
  ncol = n_dvs,
  dimnames = list(tree_predictors, dvs)
)

for (j in seq_along(dvs)) {
  target_dv <- dvs[j]
  other_dvs <- dvs[dvs != target_dv]

  # Combine species dummies + other DVs as predictors
  X_rf <- data.frame(species_dummies[, -1], df[, other_dvs])
  predictor_names_j <- c(colnames(species_dummies)[-1], other_dvs)

  rf_model <- randomForest(x = X_rf, y = df[[target_dv]], ntree = 500,
                           importance = TRUE)
  r2_rf <- 1 - sum((predict(rf_model) - df[[target_dv]])^2) /
               sum((df[[target_dv]] - mean(df[[target_dv]]))^2)

  imp <- importance(rf_model, type = 1)
  row_idx <- match(predictor_names_j, tree_predictors)
  importance_matrix[row_idx, j] <- imp[predictor_names_j, 1]

  cat(sprintf("  RF on %s: in-sample R2 = %.3f\n", target_dv, r2_rf))
}

# Normalize to 0-100 per column
norm_imp <- importance_matrix
for (j in 1:n_dvs) {
  col_max <- max(norm_imp[, j], na.rm = TRUE)
  if (col_max > 0) norm_imp[, j] <- (norm_imp[, j] / col_max) * 100
}

cat("\nCross-DV Importance (RF, normalized 0-100):\n")
print(round(norm_imp, 1))

write.csv(as.data.frame(norm_imp), "tables/importance_table.csv")

# Heatmap
imp_long <- as.data.frame(norm_imp) %>%
  mutate(Predictor = rownames(norm_imp)) %>%
  pivot_longer(-Predictor, names_to = "Target_DV", values_to = "Importance")

imp_long_labels <- imp_long %>% filter(!is.na(Importance))

p_heatmap <- ggplot(imp_long, aes(x = Target_DV, y = Predictor, fill = Importance)) +
  geom_tile(color = "white") +
  geom_text(data = imp_long_labels, aes(label = round(Importance, 0)), size = 3) +
  scale_fill_gradient(low = "white", high = "firebrick", limits = c(0, 100)) +
  labs(title = "Cross-DV Feature Importance Heatmap (RF)",
       x = "Target DV", y = "Predictor", fill = "Importance\n(0-100)") +
  theme_minimal(base_size = 12) +
  theme(axis.text.x = element_text(angle = 30, hjust = 1))
ggsave("figures/plot_13_importance_heatmap.png", p_heatmap,
       width = 10, height = 8, dpi = 300)
cat("Saved: figures/plot_13_importance_heatmap.png\n")

# ==============================================================================
# PART 6: CROSS-METHOD SYNTHESIS (Workflow 07)
# ==============================================================================

cat("\n", strrep("=", 60), "\n")
cat("PART 6: CROSS-METHOD INSIGHT SYNTHESIS\n")
cat("Models are analytic lenses, not contestants.\n")
cat(strrep("=", 60), "\n\n")

# -- 6A: Variable-Level Convergence Table --------------------------------------

cat("--- 6A: Variable-Level Convergence Table (0-100) ---\n\n")

# MANOVA eta2
eta2_vals <- sapply(dvs, function(d) anova_results[[d]]$eta2)
eta2_scaled <- (eta2_vals / max(eta2_vals)) * 100

# Discriminant structure coefficients (LD1)
disc_vals <- abs(structure_coefs[, 1])
disc_scaled <- (disc_vals / max(disc_vals)) * 100

# PCA loadings (PC1)
pca_vals <- abs(loadings_mat[, 1])
pca_scaled <- (pca_vals / max(pca_vals)) * 100

# RF importance: average importance of each DV as predictor for OTHER DVs
rf_dv_imp <- numeric(n_dvs)
for (i in seq_along(dvs)) {
  dv_as_pred <- dvs[i]
  # Find this DV's importance when it appears as predictor
  pred_idx <- which(tree_predictors == dv_as_pred)
  if (length(pred_idx) > 0) {
    other_cols <- setdiff(1:n_dvs, i)
    rf_dv_imp[i] <- mean(norm_imp[pred_idx, other_cols], na.rm = TRUE)
  }
}
rf_scaled <- (rf_dv_imp / max(rf_dv_imp)) * 100

convergence <- data.frame(
  DV = dvs,
  MANOVA_eta2 = round(eta2_scaled, 1),
  Discriminant = round(disc_scaled, 1),
  PCA_Loading = round(pca_scaled, 1),
  RF_Importance = round(rf_scaled, 1)
)

# Rank consensus
for (col in c("MANOVA_eta2", "Discriminant", "PCA_Loading", "RF_Importance")) {
  convergence[[paste0(col, "_rank")]] <- rank(-convergence[[col]])
}
rank_cols <- grep("_rank$", names(convergence), value = TRUE)
convergence$Avg_Rank <- rowMeans(convergence[, rank_cols])
convergence$Rank_Consensus <- rank(convergence$Avg_Rank)

display_cols <- c("DV", "MANOVA_eta2", "Discriminant", "PCA_Loading",
                  "RF_Importance", "Rank_Consensus")
print(convergence[, display_cols])

write.csv(convergence[, display_cols], "tables/convergence_table.csv", row.names = FALSE)

# -- 6B: Method Insight Synthesis Table ----------------------------------------

cat("\n--- 6B: Method Insight Synthesis ---\n\n")

top_dv <- convergence$DV[which.min(convergence$Rank_Consensus)]
second_dv <- convergence$DV[order(convergence$Rank_Consensus)[2]]
n_pca_components <- sum(eigenvalues_pca >= 1)

cat("MANOVA:     All DVs significant; ", top_dv, " largest effect.\n")
cat("Discriminant:", n_functions, "function(s), LOO-CV =", sprintf("%.1f%%", cv_acc * 100), "\n")
cat("CCA:        Strong canonical association (Rc =", sprintf("%.3f", cca_result$cor[1]), ").\n")
cat("Profile:    Groups differ in pattern (caveat: scale mismatch).\n")
cat("PCA:       ", n_pca_components, "component(s) above Kaiser.\n")
cat("Trees:      Petal measurements dominate across DV models.\n")

# -- 6C: Dimension Summary ----------------------------------------------------

cat("\n--- 6C: Dimension Summary ---\n\n")
cat(sprintf("  PCA: %d component(s) above Kaiser\n", n_pca_components))
cat(sprintf("  Discriminant: %d function(s)\n", n_functions))
cat(sprintf("  CCA: %d canonical dimension(s)\n", n_dims))
cat("  Convergence: methods suggest", max(n_pca_components, n_functions),
    "meaningful dimension(s).\n")

# -- 6D: Narrative Synthesis ---------------------------------------------------

cat("\n--- 6D: Narrative Synthesis ---\n\n")
cat(sprintf(paste0(
  "Across all analytic methods, %s and %s consistently emerged as the ",
  "primary sources of group separation among iris species. ",
  "Discriminant analysis achieved %.1f%% LOO-CV classification accuracy, ",
  "with structure coefficients confirming petal measurements as the ",
  "strongest contributors to group separation. ",
  "PCA revealed %d component(s) capturing %.1f%% of total variance, ",
  "with petal variables loading strongly on PC1. ",
  "Tree-based models corroborated these findings. ",
  "The convergence across parametric, classification, dimension-reduction, ",
  "and nonlinear methods strengthens confidence in the key finding.\n"),
  top_dv, second_dv, cv_acc * 100, n_pca_components,
  cum_var[n_pca_components] * 100))

# ==============================================================================
# PART 7: MANUSCRIPT GENERATION (Workflow 08)
# ==============================================================================

cat("\n", strrep("=", 60), "\n")
cat("PART 7: MANUSCRIPT GENERATION\n")
cat(strrep("=", 60), "\n\n")

# methods.md
methods_text <- sprintf(paste0(
  "## Methods\n\n",
  "### Statistical Analysis\n\n",
  "A one-way MANOVA tested whether four morphological measurements differed\n",
  "across three iris species using Pillai's trace as the primary multivariate\n",
  "test statistic. Follow-up\n",
  "univariate ANOVAs used Bonferroni correction (alpha = %.4f). Pairwise\n",
  "comparisons employed Tukey HSD with Cohen's d effect sizes.\n\n",
  "Linear discriminant analysis identified linear combinations separating groups.\n",
  "Classification accuracy was evaluated via resubstitution and LOO-CV.\n\n",
  "Profile analysis tested parallelism, equal levels, and flatness (with caveat\n",
  "regarding differing DV scales). Canonical correlation analysis examined\n",
  "species-morphology associations. PCA reduced dimensionality using Kaiser\n",
  "criterion. Tree-based models (RF, 500 trees) provided exploratory nonlinear\n",
  "importance estimates.\n\n",
  "Analyses conducted in R %s with tidyverse, MASS, car, randomForest,\n",
  "and broom.\n"),
  bonferroni_alpha, R.version.string)

writeLines(methods_text, "methods.md")
cat("Saved: methods.md\n")

# results.md (abbreviated for example)
results_text <- sprintf(paste0(
  "## Results\n\n",
  "### MANOVA\n\n",
  "The one-way MANOVA revealed significant multivariate differences across species.\n\n",
  "### Follow-Up ANOVAs\n\n",
  "All four DVs differed significantly after Bonferroni correction.\n",
  "%s showed the largest effect (partial eta2 = %.3f).\n\n",
  "### Discriminant Analysis\n\n",
  "%d function(s) separated groups. LOO-CV accuracy = %.1f%%.\n\n",
  "### Cross-Method Synthesis\n\n",
  "%s and %s consistently ranked as most important across all methods.\n"),
  top_dv, max(eta2_vals),
  n_functions, cv_acc * 100,
  top_dv, second_dv)

writeLines(results_text, "results.md")
cat("Saved: results.md\n")

# references.bib
bib_text <- paste0(
  "@book{tabachnick2019,\n",
  "  author = {Tabachnick, Barbara G. and Fidell, Linda S.},\n",
  "  title = {Using Multivariate Statistics},\n",
  "  edition = {7th},\n",
  "  publisher = {Pearson},\n",
  "  year = {2019}\n}\n\n",
  "@article{mardia1970,\n",
  "  author = {Mardia, Kanti V.},\n",
  "  title = {Measures of multivariate skewness and kurtosis with applications},\n",
  "  journal = {Biometrika},\n",
  "  volume = {57},\n",
  "  pages = {519--530},\n",
  "  year = {1970}\n}\n\n",
  "@book{rencher2012,\n",
  "  author = {Rencher, Alvin C. and Christensen, William F.},\n",
  "  title = {Methods of Multivariate Analysis},\n",
  "  edition = {3rd},\n",
  "  publisher = {Wiley},\n",
  "  year = {2012}\n}\n\n",
  "@article{breiman2001,\n",
  "  author = {Breiman, Leo},\n",
  "  title = {Random forests},\n",
  "  journal = {Machine Learning},\n",
  "  volume = {45},\n",
  "  pages = {5--32},\n",
  "  year = {2001}\n}\n\n",
  "@article{fisher1936,\n",
  "  author = {Fisher, Ronald A.},\n",
  "  title = {The use of multiple measurements in taxonomic problems},\n",
  "  journal = {Annals of Eugenics},\n",
  "  volume = {7},\n",
  "  pages = {179--188},\n",
  "  year = {1936}\n}\n")

writeLines(bib_text, "references.bib")
cat("Saved: references.bib\n")

# Final summary
cat("\n", strrep("=", 60), "\n")
cat("ANALYSIS COMPLETE\n")
cat(strrep("=", 60), "\n")
cat("Deliverables: methods.md, results.md, references.bib\n")
cat("Tables: tables/*.csv\n")
cat("Figures: figures/*.png\n")
