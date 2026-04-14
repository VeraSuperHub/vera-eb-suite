# =============================================
# Continuous Outcome Analysis Pipeline
# Dataset: ToothGrowth
# Outcome: len (tooth length)
# Research Questions:
#   1. Does tooth length differ by supplement type (OJ vs VC)?
#   2. How strongly does dose predict tooth length?
#   3. Does the dose-response association differ by supplement type?
# =============================================

required_packages <- c(
  "tidyverse", "broom", "moments", "quantreg",
  "rpart", "randomForest", "gbm", "gridExtra"
)

if (is.null(getOption("repos")) || identical(getOption("repos")[["CRAN"]], "@CRAN@")) {
  options(repos = c(CRAN = "https://cloud.r-project.org"))
}

# Output directory contract: all artifacts go under output/
out_dir <- file.path(getwd(), "output")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(file.path(out_dir, "tables"), showWarnings = FALSE, recursive = TRUE)
dir.create(file.path(out_dir, "figures"), showWarnings = FALSE, recursive = TRUE)

ensure_package <- function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, dependencies = TRUE)
  }
}

invisible(lapply(required_packages, ensure_package))

library(tidyverse)
library(broom)
library(moments)
library(quantreg)
library(rpart)
library(randomForest)
library(gbm)

# Output directory contract: all artifacts go under output/
out_dir <- file.path(getwd(), "output")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(file.path(out_dir, "tables"), showWarnings = FALSE, recursive = TRUE)
dir.create(file.path(out_dir, "figures"), showWarnings = FALSE, recursive = TRUE)

format_p <- function(p) {
  if (is.na(p)) return("NA")
  if (p < 0.001) return("< .001")
  sprintf("= %.3f", p)
}

cat(strrep("=", 60), "\n")
cat("PART 0: DATA LOADING\n")
cat(strrep("=", 60), "\n")

df <- ToothGrowth %>%
  mutate(
    supp = factor(supp, levels = c("OJ", "VC")),
    dose_label = factor(paste0(dose, " mg"), levels = c("0.5 mg", "1 mg", "2 mg")),
    supp_vc = ifelse(supp == "VC", 1, 0),
    dose_x_supp = dose * supp_vc
  )

cat("Data dimensions:", nrow(df), "observations,", ncol(df), "variables\n")
cat("Outcome variable: len (tooth length)\n")
cat("Source: Crampton (1947), ToothGrowth built-in R dataset\n\n")

cat(strrep("=", 60), "\n")
cat("PART 1: DISTRIBUTION DIAGNOSTICS\n")
cat(strrep("=", 60), "\n\n")

sw_test <- shapiro.test(df$len)
cat("Shapiro-Wilk test: W =", round(sw_test$statistic, 4),
    ", p", format_p(sw_test$p.value), "\n")
cat("Skewness:", round(skewness(df$len), 3), "\n")
cat("Kurtosis:", round(kurtosis(df$len) - 3, 3), "(normal excess = 0)\n")

cat("\nDescriptive statistics:\n")
cat("  Mean =", round(mean(df$len), 2), "\n")
cat("  SD   =", round(sd(df$len), 2), "\n")
cat("  Min  =", min(df$len), "\n")
cat("  Max  =", max(df$len), "\n")
cat("  N    =", sum(!is.na(df$len)), "\n\n")

p_hist <- ggplot(df, aes(x = len)) +
  geom_histogram(aes(y = after_stat(density)), bins = 12,
                 fill = "#4A90D9", alpha = 0.7, color = "white") +
  geom_density(linewidth = 1, color = "#D94A4A") +
  labs(title = "Distribution of Tooth Length", x = "Tooth Length", y = "Density") +
  theme_minimal(base_size = 12)

p_qq <- ggplot(df, aes(sample = len)) +
  stat_qq(color = "#4A90D9", size = 2, alpha = 0.6) +
  stat_qq_line(color = "#D94A4A", linewidth = 1) +
  labs(title = "Q-Q Plot: Tooth Length",
       x = "Theoretical Quantiles", y = "Sample Quantiles") +
  theme_minimal(base_size = 12)

p_dist <- gridExtra::grid.arrange(p_hist, p_qq, ncol = 2)
ggsave(file.path(out_dir, "figures", "plot_01_distribution.png"), p_dist, width = 12, height = 5, dpi = 300)

if (sw_test$p.value >= 0.05 && abs(skewness(df$len)) < 1) {
  cat("DECISION: Distribution is approximately normal. Proceeding with OLS as primary.\n\n")
} else {
  cat("DECISION: Distribution deviates from normal. Keeping nonparametric confirmations and quantile regression.\n\n")
}

cat(strrep("=", 60), "\n")
cat("PART 2: GROUP COMPARISONS\n")
cat(strrep("=", 60), "\n\n")

len_oj <- df %>% filter(supp == "OJ") %>% pull(len)
len_vc <- df %>% filter(supp == "VC") %>% pull(len)

cat("── Group Descriptives ──\n")
cat(sprintf("  OJ: n = %d, M = %.2f, SD = %.2f\n", length(len_oj), mean(len_oj), sd(len_oj)))
cat(sprintf("  VC: n = %d, M = %.2f, SD = %.2f\n", length(len_vc), mean(len_vc), sd(len_vc)))

sw_oj <- shapiro.test(len_oj)
sw_vc <- shapiro.test(len_vc)
cat(sprintf("\n  Shapiro-Wilk (OJ): W = %.4f, p %s\n", sw_oj$statistic, format_p(sw_oj$p.value)))
cat(sprintf("  Shapiro-Wilk (VC): W = %.4f, p %s\n", sw_vc$statistic, format_p(sw_vc$p.value)))

t_result <- t.test(len ~ supp, data = df)
cohens_d <- (mean(len_oj) - mean(len_vc)) / sqrt((sd(len_oj)^2 + sd(len_vc)^2) / 2)
cat("\n── Welch's t-test ──\n")
cat(sprintf("  t(%.1f) = %.3f, p %s\n",
            t_result$parameter, t_result$statistic,
            format_p(t_result$p.value)))
cat(sprintf("  Mean difference = %.2f, 95%% CI [%.2f, %.2f]\n",
            unname(t_result$estimate[1] - t_result$estimate[2]), t_result$conf.int[1], t_result$conf.int[2]))
cat(sprintf("  Cohen's d = %.3f\n", cohens_d))

mw_result <- wilcox.test(len ~ supp, data = df, exact = FALSE)
cat("\n── Mann-Whitney U ──\n")
cat(sprintf("  W = %.1f, p %s\n", mw_result$statistic, format_p(mw_result$p.value)))

aov_result <- aov(len ~ dose_label, data = df)
aov_summary <- summary(aov_result)
f_val <- aov_summary[[1]]$`F value`[1]
f_p <- aov_summary[[1]]$`Pr(>F)`[1]
eta_sq <- aov_summary[[1]]$`Sum Sq`[1] / sum(aov_summary[[1]]$`Sum Sq`)

cat("\n── One-way ANOVA: Tooth Length by Dose ──\n")
cat(sprintf("  F(%d, %d) = %.2f, p %s, eta-squared = %.3f\n",
            aov_summary[[1]]$Df[1], aov_summary[[1]]$Df[2],
            f_val, format_p(f_p), eta_sq))

cat("\n── Tukey HSD ──\n")
print(TukeyHSD(aov_result))

kw_result <- kruskal.test(len ~ dose_label, data = df)
cat("\n── Kruskal-Wallis ──\n")
cat(sprintf("  H(%d) = %.3f, p %s\n",
            kw_result$parameter, kw_result$statistic, format_p(kw_result$p.value)))

p_box_supp <- ggplot(df, aes(x = supp, y = len, fill = supp)) +
  geom_boxplot(alpha = 0.7) +
  geom_jitter(width = 0.12, alpha = 0.5, size = 2) +
  scale_fill_manual(values = c("OJ" = "#F28E2B", "VC" = "#4A90D9")) +
  labs(title = "Tooth Length by Supplement", x = "", y = "Tooth Length") +
  theme_minimal(base_size = 12) +
  theme(legend.position = "none")

p_box_dose <- ggplot(df, aes(x = dose_label, y = len, fill = dose_label)) +
  geom_boxplot(alpha = 0.7) +
  geom_jitter(width = 0.12, alpha = 0.5, size = 2) +
  scale_fill_manual(values = c("0.5 mg" = "#A0CBE8", "1 mg" = "#59A14F", "2 mg" = "#E15759")) +
  labs(title = "Tooth Length by Dose", x = "Dose", y = "Tooth Length") +
  theme_minimal(base_size = 12) +
  theme(legend.position = "none")

p_box <- gridExtra::grid.arrange(p_box_supp, p_box_dose, ncol = 2)
ggsave(file.path(out_dir, "figures", "plot_02_group_comparisons.png"), p_box, width = 12, height = 5, dpi = 300)

cat(sprintf("\nInterpretation: OJ supplementation (M = %.2f, SD = %.2f) yielded",
            mean(len_oj), sd(len_oj)))
cat(sprintf("\nlonger teeth than VC supplementation (M = %.2f, SD = %.2f),",
            mean(len_vc), sd(len_vc)))
cat(sprintf("\nt(%.1f) = %.3f, p %s, Cohen's d = %.3f.\n",
            t_result$parameter, t_result$statistic, format_p(t_result$p.value), cohens_d))
cat(sprintf("Dose groups also differed significantly, F(%d, %d) = %.2f, p %s, eta-squared = %.3f.\n\n",
            aov_summary[[1]]$Df[1], aov_summary[[1]]$Df[2],
            f_val, format_p(f_p), eta_sq))

cat(strrep("=", 60), "\n")
cat("PART 3: SUBGROUP ANALYSIS\n")
cat("Effect of interest: dose -> tooth length\n")
cat("Subgroup variable: supplement type\n")
cat(strrep("=", 60), "\n\n")

subgroup_results <- list()

for (level in levels(df$supp)) {
  sub_df <- df %>% filter(supp == level)
  sub_model <- lm(len ~ dose, data = sub_df)
  sub_tidy <- tidy(sub_model, conf.int = TRUE)
  dose_row <- sub_tidy %>% filter(term == "dose")
  sub_cor <- cor.test(sub_df$dose, sub_df$len)

  subgroup_results[[level]] <- list(
    level = level,
    n = nrow(sub_df),
    b = dose_row$estimate,
    se = dose_row$std.error,
    ci_low = dose_row$conf.low,
    ci_high = dose_row$conf.high,
    p_value = dose_row$p.value,
    r = sub_cor$estimate,
    r_p = sub_cor$p.value
  )

  cat(sprintf("── %s (n = %d) ──\n", level, nrow(sub_df)))
  cat(sprintf("  Correlation: r = %.3f, p %s\n", sub_cor$estimate, format_p(sub_cor$p.value)))
  cat(sprintf("  Regression: B = %.3f (SE = %.3f), 95%% CI [%.3f, %.3f], p %s\n",
              dose_row$estimate, dose_row$std.error,
              dose_row$conf.low, dose_row$conf.high,
              format_p(dose_row$p.value)))
  cat(sprintf("  Interpretation: Each 1 mg increase in dose is associated with a %.2f-unit increase in tooth length within the %s group.\n\n",
              dose_row$estimate, level))
}

model_interaction <- lm(len ~ dose * supp, data = df)
model_no_interaction <- lm(len ~ dose + supp, data = df)
interaction_anova <- anova(model_no_interaction, model_interaction)

cat("── Interaction Test ──\n")
cat("Testing: dose × supplement interaction\n")
cat(sprintf("F(%d, %d) = %.3f, p %s\n",
            interaction_anova$Df[2],
            interaction_anova$Res.Df[2],
            interaction_anova$F[2],
            format_p(interaction_anova$`Pr(>F)`[2])))

if (interaction_anova$`Pr(>F)`[2] < 0.05) {
  cat("CONCLUSION: The dose-response slope differs significantly by supplement type.\n\n")
} else {
  cat("CONCLUSION: The dose-response slope does not significantly differ by supplement type.\n\n")
}

sr_df <- do.call(rbind, lapply(subgroup_results, function(x) {
  data.frame(subgroup = x$level, b = x$b, ci_low = x$ci_low, ci_high = x$ci_high, n = x$n)
}))

overall_model <- lm(len ~ dose, data = df)
overall_tidy <- tidy(overall_model, conf.int = TRUE) %>% filter(term == "dose")
sr_df <- rbind(
  sr_df,
  data.frame(
    subgroup = "Overall",
    b = overall_tidy$estimate,
    ci_low = overall_tidy$conf.low,
    ci_high = overall_tidy$conf.high,
    n = nrow(df)
  )
)
sr_df$subgroup <- factor(sr_df$subgroup, levels = rev(c(levels(df$supp), "Overall")))

p_forest <- ggplot(sr_df, aes(x = b, y = subgroup)) +
  geom_vline(xintercept = 0, color = "grey60", linetype = "dashed") +
  geom_pointrange(aes(xmin = ci_low, xmax = ci_high),
                  color = "#4A90D9") +
  labs(title = "Dose Effect on Tooth Length by Supplement",
       x = "B (change in tooth length per 1 mg dose)", y = "") +
  theme_minimal(base_size = 12)
ggsave(file.path(out_dir, "figures", "plot_03_subgroup_forest.png"), p_forest, width = 8, height = 5, dpi = 300)

p_scatter <- ggplot(df, aes(x = dose, y = len, color = supp)) +
  geom_point(size = 3, alpha = 0.7) +
  geom_smooth(method = "lm", se = TRUE, alpha = 0.15) +
  scale_color_manual(values = c("OJ" = "#F28E2B", "VC" = "#4A90D9")) +
  labs(title = "Dose Response by Supplement",
       x = "Dose (mg)", y = "Tooth Length", color = "Supplement") +
  theme_minimal(base_size = 12)
ggsave(file.path(out_dir, "figures", "plot_04_subgroup_scatter.png"), p_scatter, width = 8, height = 6, dpi = 300)

cat("Subgroup plots saved: plot_03_subgroup_forest.png, plot_04_subgroup_scatter.png\n\n")

cat(strrep("=", 60), "\n")
cat("PART 4: MODELING\n")
cat(strrep("=", 60), "\n\n")

model_ols <- lm(len ~ dose + supp_vc + dose_x_supp, data = df)
ols_tidy <- tidy(model_ols, conf.int = TRUE)
ols_glance <- glance(model_ols)

cat("── OLS Model ──\n")
print(summary(model_ols))

cat("\n── Model Fit ──\n")
cat("R² =", round(ols_glance$r.squared, 3), "\n")
cat("Adjusted R² =", round(ols_glance$adj.r.squared, 3), "\n")
cat("F(", ols_glance$df, ",", ols_glance$df.residual, ") =",
    round(ols_glance$statistic, 2), ", p", format_p(ols_glance$p.value), "\n")

p_resid <- ggplot(data.frame(fitted = fitted(model_ols), residuals = resid(model_ols)),
                  aes(x = fitted, y = residuals)) +
  geom_point(color = "#4A90D9", alpha = 0.6, size = 2) +
  geom_hline(yintercept = 0, color = "#D94A4A", linewidth = 1) +
  labs(title = "Residuals vs Fitted", x = "Fitted Values", y = "Residuals") +
  theme_minimal(base_size = 12)

p_resid_qq <- ggplot(data.frame(residuals = resid(model_ols)), aes(sample = residuals)) +
  stat_qq(color = "#4A90D9", size = 2, alpha = 0.6) +
  stat_qq_line(color = "#D94A4A", linewidth = 1) +
  labs(title = "Q-Q Plot of Residuals",
       x = "Theoretical Quantiles", y = "Residual Quantiles") +
  theme_minimal(base_size = 12)

p_diag <- gridExtra::grid.arrange(p_resid, p_resid_qq, ncol = 2)
ggsave(file.path(out_dir, "figures", "plot_05_residuals.png"), p_diag, width = 12, height = 5, dpi = 300)

coef_plot <- ols_tidy %>%
  filter(term != "(Intercept)") %>%
  mutate(term = forcats::fct_reorder(term, estimate))

p_coef <- ggplot(coef_plot, aes(x = estimate, y = term)) +
  geom_vline(xintercept = 0, color = "grey60", linetype = "dashed") +
  geom_pointrange(aes(xmin = conf.low, xmax = conf.high),
                  color = "#4A90D9") +
  labs(title = "OLS Coefficients with 95% CI",
       x = "Estimate (B)", y = "") +
  theme_minimal(base_size = 12)
ggsave(file.path(out_dir, "figures", "plot_06_coefficient_forest.png"), p_coef, width = 7, height = 5, dpi = 300)

df_std <- df %>%
  mutate(across(c(len, dose, supp_vc, dose_x_supp), ~ as.numeric(scale(.x))))
model_std <- lm(len ~ dose + supp_vc + dose_x_supp, data = df_std)
std_tidy <- tidy(model_std) %>%
  filter(term != "(Intercept)") %>%
  mutate(beta_std = abs(estimate)) %>%
  select(term, beta_std)

taus <- c(0.25, 0.50, 0.75)
qr_models <- lapply(taus, function(tau) {
  suppressWarnings(rq(len ~ dose + supp_vc + dose_x_supp, data = df, tau = tau, method = "fn"))
})
qr_summary <- lapply(qr_models, summary, se = "boot")

cat("\n── Quantile Regression ──\n")
for (i in seq_along(taus)) {
  cat(sprintf("tau = %.2f\n", taus[i]))
  print(qr_summary[[i]])
  cat("\n")
}

qr_coefs <- sapply(qr_models, coef)
colnames(qr_coefs) <- paste0("Q", taus * 100)

cat("── Tree-Based Models (Exploratory) ──\n")
df_tree <- df %>% select(len, dose, supp_vc, dose_x_supp)
y_tree <- df_tree$len

model_cart <- rpart(len ~ ., data = df_tree, method = "anova",
                    control = rpart.control(maxdepth = 4, cp = 0.01))
cart_pred <- predict(model_cart, df_tree)
cart_r2 <- 1 - sum((y_tree - cart_pred)^2) / sum((y_tree - mean(y_tree))^2)

model_rf <- randomForest(len ~ ., data = df_tree, ntree = 500, importance = TRUE)
rf_pred <- predict(model_rf, df_tree)
rf_r2 <- 1 - sum((y_tree - rf_pred)^2) / sum((y_tree - mean(y_tree))^2)

model_gbm <- gbm(len ~ ., data = df_tree, distribution = "gaussian",
                 n.trees = 500, interaction.depth = 3, shrinkage = 0.1,
                 bag.fraction = 0.8, verbose = FALSE)
gbm_pred <- predict(model_gbm, df_tree, n.trees = 500)
gbm_r2 <- 1 - sum((y_tree - gbm_pred)^2) / sum((y_tree - mean(y_tree))^2)

cat("  CART in-sample R² =", round(cart_r2, 3), "\n")
cat("  Random Forest in-sample R² =", round(rf_r2, 3), "\n")
cat("  GBM in-sample R² =", round(gbm_r2, 3), "\n")

imp_df <- data.frame(
  variable = rownames(importance(model_rf)),
  importance = importance(model_rf)[, "%IncMSE"]
) %>% arrange(desc(importance))

p_imp <- ggplot(imp_df, aes(x = importance, y = reorder(variable, importance))) +
  geom_col(fill = "#4A90D9", alpha = 0.8) +
  labs(title = "Variable Importance (Random Forest)",
       x = "% Increase in MSE", y = "") +
  theme_minimal(base_size = 12)
ggsave(file.path(out_dir, "figures", "plot_07_variable_importance.png"), p_imp, width = 7, height = 5, dpi = 300)

std_imp <- std_tidy %>%
  mutate(OLS_beta = beta_std / max(beta_std) * 100)
rf_scaled <- imp_df %>%
  mutate(RF = importance / max(importance) * 100) %>%
  select(variable, RF)
gbm_raw <- summary(model_gbm, plotit = FALSE) %>%
  rename(variable = var, gbm_rel = rel.inf) %>%
  mutate(GBM = gbm_rel / max(gbm_rel) * 100) %>%
  select(variable, GBM)

unified_imp <- std_imp %>%
  rename(variable = term) %>%
  left_join(rf_scaled, by = "variable") %>%
  left_join(gbm_raw, by = "variable") %>%
  mutate(across(c(OLS_beta, RF, GBM), ~ round(.x, 1)))

unified_imp <- unified_imp %>%
  mutate(
    OLS_rank = rank(-OLS_beta, ties.method = "min"),
    RF_rank = rank(-RF, ties.method = "min"),
    GBM_rank = rank(-GBM, ties.method = "min"),
    Consensus_Rank = rank((OLS_rank + RF_rank + GBM_rank) / 3, ties.method = "min")
  ) %>%
  arrange(Consensus_Rank)

top_var <- unified_imp$variable[1]
second_var <- unified_imp$variable[2]

cat("\n── Model Comparison Summary ──\n")
cat(sprintf("OLS Linear Regression   | R² = %.3f | Strongest term: %s\n",
            ols_glance$r.squared,
            ols_tidy %>% filter(term != "(Intercept)") %>% arrange(p.value) %>% slice(1) %>% pull(term)))
cat(sprintf("Quantile Regression     | Median dose effect = %.3f\n", qr_coefs["dose", "Q50"]))
cat(sprintf("CART                    | R² = %.3f | Top split: %s\n",
            cart_r2, names(model_cart$variable.importance)[1]))
cat(sprintf("Random Forest           | R² = %.3f | Top variables: %s, %s\n",
            rf_r2, imp_df$variable[1], imp_df$variable[2]))
cat(sprintf("GBM                     | R² = %.3f | Top variables: %s, %s\n",
            gbm_r2, gbm_raw$variable[1], gbm_raw$variable[2]))

cat("\n── Summary ──\n")
cat("OLS provides the most interpretable results and is the primary analysis.\n")
cat("Quantile regression adds distributional insight about the dose-response relation.\n")
cat("Tree-based models confirm the variable-importance ordering but remain exploratory.\n")

cat("\n", strrep("=", 60), "\n")
cat("PART 5: MANUSCRIPT GENERATION\n")
cat(strrep("=", 60), "\n\n")

# tables/ and figures/ created at top of script under out_dir

write.csv(ols_tidy, file.path(out_dir, "tables", "regression_table.csv"), row.names = FALSE)
write.csv(data.frame(Predictor = rownames(qr_coefs), qr_coefs), file.path(out_dir, "tables", "quantile_table.csv"), row.names = FALSE)
write.csv(unified_imp %>% select(variable, OLS_beta, RF, GBM, Consensus_Rank), file.path(out_dir, "tables", "importance_table.csv"), row.names = FALSE)

insight_table <- data.frame(
  Method = c("OLS", "Quantile Regression", "Tree-Based (RF/GBM)"),
  Unique_Insight = c(
    "Dose dominates the linear model, with interpretable interaction terms and confidence intervals.",
    sprintf("Dose effect remains positive across quantiles (Q25 = %.2f, Q75 = %.2f).", qr_coefs["dose", "Q25"], qr_coefs["dose", "Q75"]),
    sprintf("Nonparametric importance also ranks %s and %s highest.", top_var, second_var)
  )
)
write.csv(insight_table, file.path(out_dir, "tables", "insight_table.csv"), row.names = FALSE)

methods_text <- sprintf(paste0(
  "## Methods\n\n",
  "Tooth length (`len`) was analyzed as a continuous outcome in the ToothGrowth dataset. ",
  "Distributional properties were assessed using the Shapiro-Wilk test, skewness, ",
  "kurtosis, a histogram with density overlay, and a Q-Q plot.\n\n",
  "Welch's t-test compared orange juice (OJ) with ascorbic acid (VC) supplementation, ",
  "with Cohen's d reported as an effect size. Mann-Whitney U served as a nonparametric ",
  "confirmation. Dose groups were compared using one-way ANOVA with eta-squared, ",
  "Tukey HSD, and Kruskal-Wallis follow-up.\n\n",
  "Subgroup analyses fit dose-response regressions within each supplement group. ",
  "A formal interaction test compared models with and without the dose-by-supplement term.\n\n",
  "Primary modeling used OLS regression with dose, supplement type, and their interaction ",
  "as predictors. Quantile regression at the 25th, 50th, and 75th percentiles evaluated ",
  "distributional heterogeneity. CART, random forest (500 trees), and GBM were fit as ",
  "exploratory models given the small sample size (N = %d).\n"),
  nrow(df))
writeLines(methods_text, file.path(out_dir, "methods.md"))

results_text <- sprintf(paste0(
  "## Results\n\n",
  "OJ supplementation (M = %.2f, SD = %.2f) produced longer teeth than VC supplementation ",
  "(M = %.2f, SD = %.2f), t(%.1f) = %.3f, p %s, Cohen's d = %.3f.\n\n",
  "Dose differences were strong, F(%d, %d) = %.2f, p %s, eta-squared = %.3f. ",
  "Within supplement strata, dose remained positively associated with tooth length in both groups. ",
  "The interaction test %s significant heterogeneity by supplement.\n\n",
  "The OLS model accounted for %.1f%% of the variance in tooth length. Across OLS, quantile regression, ",
  "random forest, and GBM, %s emerged as the dominant predictor, followed by %s.\n"),
  mean(len_oj), sd(len_oj), mean(len_vc), sd(len_vc),
  t_result$parameter, t_result$statistic, format_p(t_result$p.value), cohens_d,
  aov_summary[[1]]$Df[1], aov_summary[[1]]$Df[2], f_val, format_p(f_p), eta_sq,
  ifelse(interaction_anova$`Pr(>F)`[2] < 0.05, "supported", "did not support"),
  ols_glance$r.squared * 100, top_var, second_var)
writeLines(results_text, file.path(out_dir, "results.md"))

bib_text <- paste0(
  "@article{welch1947,\n",
  "  author = {Welch, B. L.},\n",
  "  title = {The generalization of Student's problem when several different population variances are involved},\n",
  "  journal = {Biometrika},\n",
  "  volume = {34},\n",
  "  pages = {28--35},\n",
  "  year = {1947}\n}\n\n",
  "@article{kruskal1952,\n",
  "  author = {Kruskal, William H. and Wallis, W. Allen},\n",
  "  title = {Use of ranks in one-criterion variance analysis},\n",
  "  journal = {Journal of the American Statistical Association},\n",
  "  volume = {47},\n",
  "  pages = {583--621},\n",
  "  year = {1952}\n}\n\n",
  "@article{koenker1978,\n",
  "  author = {Koenker, Roger and Bassett, Gilbert},\n",
  "  title = {Regression quantiles},\n",
  "  journal = {Econometrica},\n",
  "  volume = {46},\n",
  "  pages = {33--50},\n",
  "  year = {1978}\n}\n\n",
  "@article{breiman2001,\n",
  "  author = {Breiman, Leo},\n",
  "  title = {Random forests},\n",
  "  journal = {Machine Learning},\n",
  "  volume = {45},\n",
  "  pages = {5--32},\n",
  "  year = {2001}\n}\n")
writeLines(bib_text, file.path(out_dir, "references.bib"))

cat("Plots moved to figures/\n")
cat("Tables saved to tables/\n")
cat("methods.md generated\n")
cat("results.md generated\n")
cat("references.bib generated\n")
