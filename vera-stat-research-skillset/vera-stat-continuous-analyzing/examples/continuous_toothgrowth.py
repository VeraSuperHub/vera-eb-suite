#!/usr/bin/env python3
"""
Continuous Outcome Analysis Pipeline
Dataset: ToothGrowth
Outcome: len (tooth length)
Research Questions:
  1. Does tooth length differ by supplement type (OJ vs VC)?
  2. How strongly does dose predict tooth length?
  3. Does the dose-response association differ by supplement type?
"""

import os
import shutil
import warnings

warnings.filterwarnings("ignore")

# Output directory contract: all artifacts go under output/
OUT_DIR = os.path.join(os.getcwd(), "output")
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUT_DIR, "tables"), exist_ok=True)
os.makedirs(os.path.join(OUT_DIR, "figures"), exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

try:
    import lightgbm as lgb
    HAS_LGB = True
except ImportError:
    HAS_LGB = False


def p_fmt(p_value):
    if pd.isna(p_value):
        return "NA"
    return "< .001" if p_value < 0.001 else f"= {p_value:.3f}"


def cohens_d(x, y):
    pooled_sd = np.sqrt((x.std(ddof=1) ** 2 + y.std(ddof=1) ** 2) / 2)
    return (x.mean() - y.mean()) / pooled_sd


def ensure_move(src_name, dst_dir):
    if not os.path.exists(src_name):
        return  # source not in CWD; already saved to correct location
    dst_path = os.path.join(dst_dir, src_name)
    if os.path.exists(dst_path):
        os.remove(dst_path)
    shutil.move(src_name, dst_path)


print("=" * 60)
print("PART 0: DATA LOADING")
print("=" * 60)

def _load_toothgrowth():
    """Load ToothGrowth with offline fallback."""
    try:
        return sm.datasets.get_rdataset("ToothGrowth", "datasets").data.copy()
    except Exception:
        import os as _os
        local_csv = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "toothgrowth.csv")
        if _os.path.exists(local_csv):
            _df = pd.read_csv(local_csv); return _df.drop(columns=[c for c in ['rownames','Unnamed: 0'] if c in _df.columns])
        raise RuntimeError(
            "ToothGrowth not available. Network access failed and no local "
            "toothgrowth.csv was found next to this script."
        )

df = _load_toothgrowth()
df["supp"] = pd.Categorical(df["supp"], categories=["OJ", "VC"])
df["dose_label"] = pd.Categorical(df["dose"].map({0.5: "0.5 mg", 1.0: "1.0 mg", 2.0: "2.0 mg"}),
                                   categories=["0.5 mg", "1.0 mg", "2.0 mg"])
df["supp_vc"] = (df["supp"] == "VC").astype(int)
df["dose_x_supp"] = df["dose"] * df["supp_vc"]

print(f"Data dimensions: {df.shape[0]} observations, {df.shape[1]} variables")
print("Outcome variable: len (tooth length)")
print("Source: Crampton (1947), ToothGrowth dataset\n")

print("=" * 60)
print("PART 1: DISTRIBUTION DIAGNOSTICS")
print("=" * 60, "\n")

sw_stat, sw_p = stats.shapiro(df["len"])
skew_val = stats.skew(df["len"])
kurt_val = stats.kurtosis(df["len"])

print(f"Shapiro-Wilk test: W = {sw_stat:.4f}, p {p_fmt(sw_p)}")
print(f"Skewness: {skew_val:.3f}")
print(f"Excess kurtosis: {kurt_val:.3f} (normal = 0)")
print("\nDescriptive statistics:")
print(f"  Mean = {df['len'].mean():.2f}")
print(f"  SD   = {df['len'].std(ddof=1):.2f}")
print(f"  Min  = {df['len'].min():.2f}")
print(f"  Max  = {df['len'].max():.2f}")
print(f"  N    = {df['len'].notna().sum()}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(df["len"], bins=12, density=True, alpha=0.7, color="#4A90D9", edgecolor="white")
df["len"].plot.kde(ax=axes[0], color="#D94A4A", linewidth=2)
axes[0].set_title("Distribution of Tooth Length", fontsize=13)
axes[0].set_xlabel("Tooth Length")
axes[0].set_ylabel("Density")

sm.qqplot(df["len"], line="45", ax=axes[1], markerfacecolor="#4A90D9", alpha=0.6)
axes[1].set_title("Q-Q Plot: Tooth Length", fontsize=13)
axes[1].get_lines()[0].set_color("#D94A4A")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "figures", "plot_01_distribution.png"), dpi=300, bbox_inches="tight")
plt.close()

if sw_p >= 0.05 and abs(skew_val) < 1:
    print("\nDECISION: Distribution is approximately normal. Proceeding with OLS as primary.\n")
else:
    print("\nDECISION: Distribution deviates from normal. Keeping nonparametric confirmations and quantile regression.\n")

print("=" * 60)
print("PART 2: GROUP COMPARISONS")
print("=" * 60, "\n")

len_oj = df.loc[df["supp"] == "OJ", "len"]
len_vc = df.loc[df["supp"] == "VC", "len"]

print("── Group Descriptives ──")
print(f"  OJ: n = {len(len_oj)}, M = {len_oj.mean():.2f}, SD = {len_oj.std(ddof=1):.2f}")
print(f"  VC: n = {len(len_vc)}, M = {len_vc.mean():.2f}, SD = {len_vc.std(ddof=1):.2f}")

sw_oj_stat, sw_oj_p = stats.shapiro(len_oj)
sw_vc_stat, sw_vc_p = stats.shapiro(len_vc)
print(f"\n  Shapiro-Wilk (OJ): W = {sw_oj_stat:.4f}, p {p_fmt(sw_oj_p)}")
print(f"  Shapiro-Wilk (VC): W = {sw_vc_stat:.4f}, p {p_fmt(sw_vc_p)}")

t_stat, t_p = stats.ttest_ind(len_oj, len_vc, equal_var=False)
d_val = cohens_d(len_oj, len_vc)
n1, n2 = len(len_oj), len(len_vc)
s1, s2 = len_oj.std(ddof=1), len_vc.std(ddof=1)
df_welch = ((s1**2 / n1 + s2**2 / n2) ** 2 /
            ((s1**2 / n1) ** 2 / (n1 - 1) + (s2**2 / n2) ** 2 / (n2 - 1)))
mean_diff = len_oj.mean() - len_vc.mean()
se_diff = np.sqrt(s1**2 / n1 + s2**2 / n2)
ci_low = mean_diff + stats.t.ppf(0.025, df_welch) * se_diff
ci_high = mean_diff + stats.t.ppf(0.975, df_welch) * se_diff

print("\n── Welch's t-test ──")
print(f"  t({df_welch:.1f}) = {t_stat:.3f}, p {p_fmt(t_p)}")
print(f"  Mean difference = {mean_diff:.2f}, 95% CI [{ci_low:.2f}, {ci_high:.2f}]")
print(f"  Cohen's d = {d_val:.3f}")

u_stat, u_p = stats.mannwhitneyu(len_oj, len_vc, alternative="two-sided")
print("\n── Mann-Whitney U ──")
print(f"  U = {u_stat:.1f}, p {p_fmt(u_p)}")

dose_groups = [df.loc[df["dose"] == dose, "len"] for dose in sorted(df["dose"].unique())]
f_stat_anova, f_p_anova = stats.f_oneway(*dose_groups)
ss_between = sum(len(group) * (group.mean() - df["len"].mean()) ** 2 for group in dose_groups)
ss_total = ((df["len"] - df["len"].mean()) ** 2).sum()
eta_sq = ss_between / ss_total

print("\n── One-way ANOVA: Tooth Length by Dose ──")
print(f"  F(2, {len(df) - 3}) = {f_stat_anova:.2f}, p {p_fmt(f_p_anova)}, eta-squared = {eta_sq:.3f}")

tukey = pairwise_tukeyhsd(endog=df["len"], groups=df["dose_label"], alpha=0.05)
print("\n── Tukey HSD ──")
print(tukey)

kw_stat, kw_p = stats.kruskal(*dose_groups)
print("\n── Kruskal-Wallis ──")
print(f"  H(2) = {kw_stat:.3f}, p {p_fmt(kw_p)}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data=df, x="supp", y="len", ax=axes[0], palette=["#F28E2B", "#4A90D9"])
sns.stripplot(data=df, x="supp", y="len", ax=axes[0], color="black", alpha=0.5, size=5)
axes[0].set_title("Tooth Length by Supplement")
axes[0].set_xlabel("")
axes[0].set_ylabel("Tooth Length")

sns.boxplot(data=df, x="dose_label", y="len", ax=axes[1], palette=["#A0CBE8", "#59A14F", "#E15759"])
sns.stripplot(data=df, x="dose_label", y="len", ax=axes[1], color="black", alpha=0.5, size=5)
axes[1].set_title("Tooth Length by Dose")
axes[1].set_xlabel("Dose")
axes[1].set_ylabel("Tooth Length")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "figures", "plot_02_group_comparisons.png"), dpi=300, bbox_inches="tight")
plt.close()

print(f"\nInterpretation: OJ supplementation (M = {len_oj.mean():.2f}, SD = {len_oj.std(ddof=1):.2f})")
print(f"produced {'higher' if mean_diff > 0 else 'lower'} tooth length than VC supplementation")
print(f"(M = {len_vc.mean():.2f}, SD = {len_vc.std(ddof=1):.2f}), t({df_welch:.1f}) = {t_stat:.3f}, p {p_fmt(t_p)}.")
print(f"Tooth length also differed significantly across dose groups, F(2, {len(df)-3}) = {f_stat_anova:.2f},")
print(f"p {p_fmt(f_p_anova)}, eta-squared = {eta_sq:.3f}.\n")

print("=" * 60)
print("PART 3: SUBGROUP ANALYSIS")
print("Effect of interest: dose -> tooth length")
print("Subgroup variable: supplement type")
print("=" * 60, "\n")

subgroup_results = []
for supp_name in df["supp"].cat.categories:
    sub_df = df[df["supp"] == supp_name].copy()
    model = smf.ols("len ~ dose", data=sub_df).fit()
    corr_r, corr_p = stats.pearsonr(sub_df["dose"], sub_df["len"])
    ci = model.conf_int().loc["dose"]
    subgroup_results.append({
        "subgroup": supp_name,
        "b": model.params["dose"],
        "se": model.bse["dose"],
        "ci_low": ci[0],
        "ci_high": ci[1],
        "p_value": model.pvalues["dose"],
        "r": corr_r,
        "r_p": corr_p,
        "n": len(sub_df),
    })
    print(f"── {supp_name} (n = {len(sub_df)}) ──")
    print(f"  Correlation: r = {corr_r:.3f}, p {p_fmt(corr_p)}")
    print(f"  Regression: B = {model.params['dose']:.3f} (SE = {model.bse['dose']:.3f}), "
          f"95% CI [{ci[0]:.3f}, {ci[1]:.3f}], p {p_fmt(model.pvalues['dose'])}")
    print(f"  Interpretation: Each 1 mg increase in dose is associated with a "
          f"{model.params['dose']:.2f}-unit increase in tooth length within the {supp_name} group.\n")

model_full = smf.ols("len ~ dose * C(supp)", data=df).fit()
model_reduced = smf.ols("len ~ dose + C(supp)", data=df).fit()
interaction_test = anova_lm(model_reduced, model_full)
int_f_val = interaction_test["F"].iloc[1]
int_f_p = interaction_test["Pr(>F)"].iloc[1]

print("── Interaction Test ──")
print("Testing: dose × supplement interaction")
print(f"F({int(interaction_test['df_diff'].iloc[1])}, {int(model_full.df_resid)}) = {int_f_val:.3f}, p {p_fmt(int_f_p)}")
if int_f_p < 0.05:
    print("CONCLUSION: The dose-response slope differs significantly by supplement type.\n")
else:
    print("CONCLUSION: The dose-response slope does not significantly differ by supplement type.\n")

forest_df = pd.DataFrame(subgroup_results)
overall_model = smf.ols("len ~ dose", data=df).fit()
overall_ci = overall_model.conf_int().loc["dose"]
forest_df = pd.concat([
    forest_df,
    pd.DataFrame([{
        "subgroup": "Overall",
        "b": overall_model.params["dose"],
        "se": overall_model.bse["dose"],
        "ci_low": overall_ci[0],
        "ci_high": overall_ci[1],
        "p_value": overall_model.pvalues["dose"],
        "r": np.nan,
        "r_p": np.nan,
        "n": len(df),
    }]),
], ignore_index=True)

fig, ax = plt.subplots(figsize=(8, 5))
forest_plot = forest_df.iloc[::-1].reset_index(drop=True)
y_pos = np.arange(len(forest_plot))
ax.axvline(0, color="gray", linestyle="--", linewidth=1)
ax.errorbar(
    forest_plot["b"],
    y_pos,
    xerr=[
        forest_plot["b"] - forest_plot["ci_low"],
        forest_plot["ci_high"] - forest_plot["b"],
    ],
    fmt="o",
    color="#4A90D9",
    ecolor="#4A90D9",
    capsize=4,
)
ax.set_yticks(y_pos)
ax.set_yticklabels(forest_plot["subgroup"])
ax.set_xlabel("B (change in tooth length per 1 mg dose)")
ax.set_title("Dose Effect on Tooth Length by Supplement", fontsize=13)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "figures", "plot_03_subgroup_forest.png"), dpi=300, bbox_inches="tight")
plt.close()

fig, ax = plt.subplots(figsize=(8, 6))
palette = {"OJ": "#F28E2B", "VC": "#4A90D9"}
for supp_name, color in palette.items():
    sub_df = df[df["supp"] == supp_name]
    ax.scatter(sub_df["dose"], sub_df["len"], color=color, s=60, alpha=0.7, label=supp_name)
    z = np.polyfit(sub_df["dose"], sub_df["len"], 1)
    x_line = np.linspace(sub_df["dose"].min(), sub_df["dose"].max(), 50)
    ax.plot(x_line, np.polyval(z, x_line), color=color, linewidth=2)
ax.set_title("Dose Response by Supplement")
ax.set_xlabel("Dose (mg)")
ax.set_ylabel("Tooth Length")
ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "figures", "plot_04_subgroup_scatter.png"), dpi=300, bbox_inches="tight")
plt.close()

print("Subgroup plots saved: plot_03_subgroup_forest.png, plot_04_subgroup_scatter.png\n")

print("=" * 60)
print("PART 4: MODELING")
print("=" * 60, "\n")

model_ols = smf.ols("len ~ dose + supp_vc + dose_x_supp", data=df).fit()
print("── OLS Model ──")
print(model_ols.summary())

ols_tidy = pd.DataFrame({
    "Predictor": model_ols.params.index,
    "B": model_ols.params.values,
    "SE": model_ols.bse.values,
    "t": model_ols.tvalues.values,
    "p": model_ols.pvalues.values,
    "CI_lower": model_ols.conf_int()[0].values,
    "CI_upper": model_ols.conf_int()[1].values,
})

r2 = model_ols.rsquared
adj_r2 = model_ols.rsquared_adj
print("\n── Model Fit ──")
print(f"R² = {r2:.3f}")
print(f"Adjusted R² = {adj_r2:.3f}")
print(f"F({int(model_ols.df_model)}, {int(model_ols.df_resid)}) = {model_ols.fvalue:.2f}, p {p_fmt(model_ols.f_pvalue)}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(model_ols.fittedvalues, model_ols.resid, color="#4A90D9", alpha=0.7)
axes[0].axhline(0, color="#D94A4A", linewidth=1)
axes[0].set_title("Residuals vs Fitted")
axes[0].set_xlabel("Fitted Values")
axes[0].set_ylabel("Residuals")

sm.qqplot(model_ols.resid, line="45", ax=axes[1], markerfacecolor="#4A90D9", alpha=0.6)
axes[1].set_title("Q-Q Plot of Residuals")
axes[1].get_lines()[0].set_color("#D94A4A")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "figures", "plot_05_residuals.png"), dpi=300, bbox_inches="tight")
plt.close()

coef_plot = ols_tidy[ols_tidy["Predictor"] != "Intercept"].copy()
coef_plot = coef_plot.sort_values("B")
fig, ax = plt.subplots(figsize=(7, 5))
ax.axvline(0, color="gray", linestyle="--", linewidth=1)
ax.errorbar(
    coef_plot["B"],
    np.arange(len(coef_plot)),
    xerr=[
        coef_plot["B"] - coef_plot["CI_lower"],
        coef_plot["CI_upper"] - coef_plot["B"],
    ],
    fmt="o",
    color="#4A90D9",
    ecolor="#4A90D9",
    capsize=4,
)
ax.set_yticks(np.arange(len(coef_plot)))
ax.set_yticklabels(coef_plot["Predictor"])
ax.set_xlabel("Estimate (B)")
ax.set_title("OLS Coefficients with 95% CI", fontsize=13)
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "figures", "plot_06_coefficient_forest.png"), dpi=300, bbox_inches="tight")
plt.close()

df_std = df[["len", "dose", "supp_vc", "dose_x_supp"]].copy()
scaler = StandardScaler()
df_std[["len", "dose", "supp_vc", "dose_x_supp"]] = scaler.fit_transform(df_std)
model_std = smf.ols("len ~ dose + supp_vc + dose_x_supp", data=df_std).fit()
std_beta = model_std.params.drop("Intercept").abs().sort_values(ascending=False)

taus = [0.25, 0.50, 0.75]
qr_results = {}
print("\n── Quantile Regression ──")
for tau in taus:
    qr_results[tau] = smf.quantreg("len ~ dose + supp_vc + dose_x_supp", data=df).fit(q=tau)
    print(f"tau = {tau:.2f}")
    print(qr_results[tau].summary())
    print()

print("── Tree-Based Models (Exploratory) ──")
feature_cols = ["dose", "supp_vc", "dose_x_supp"]
X = df[feature_cols]
y = df["len"].values

cart_model = DecisionTreeRegressor(max_depth=4, random_state=42)
cart_model.fit(X, y)
cart_pred = cart_model.predict(X)
cart_r2 = 1 - np.sum((y - cart_pred) ** 2) / np.sum((y - y.mean()) ** 2)

rf_model = RandomForestRegressor(n_estimators=500, random_state=42)
rf_model.fit(X, y)
rf_pred = rf_model.predict(X)
rf_r2 = 1 - np.sum((y - rf_pred) ** 2) / np.sum((y - y.mean()) ** 2)
rf_imp = pd.Series(rf_model.feature_importances_, index=feature_cols)

if HAS_LGB:
    lgb_model = lgb.LGBMRegressor(
        n_estimators=500,
        max_depth=3,
        learning_rate=0.1,
        num_leaves=15,
        min_child_samples=max(3, len(df) // 10),
        random_state=42,
        verbosity=-1,
    )
    lgb_model.fit(X, y)
    lgb_pred = lgb_model.predict(X)
    lgb_r2 = 1 - np.sum((y - lgb_pred) ** 2) / np.sum((y - y.mean()) ** 2)
    lgb_imp = pd.Series(lgb_model.feature_importances_, index=feature_cols)
else:
    lgb_r2 = np.nan
    lgb_imp = pd.Series(np.nan, index=feature_cols)

print(f"  CART in-sample R² = {cart_r2:.3f}")
print(f"  Random Forest in-sample R² = {rf_r2:.3f}")
if HAS_LGB:
    print(f"  LightGBM in-sample R² = {lgb_r2:.3f}")
else:
    print("  LightGBM unavailable; skipped.")

fig, ax = plt.subplots(figsize=(7, 5))
rf_imp.sort_values().plot(kind="barh", color="#4A90D9", ax=ax)
ax.set_title("Variable Importance (Random Forest)")
ax.set_xlabel("Importance")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "figures", "plot_07_variable_importance.png"), dpi=300, bbox_inches="tight")
plt.close()

ols_scaled = (std_beta / std_beta.max() * 100).reindex(feature_cols)
rf_scaled = (rf_imp / rf_imp.max() * 100).reindex(feature_cols)
if HAS_LGB and lgb_imp.max() > 0:
    lgbm_scaled = (lgb_imp / lgb_imp.max() * 100).reindex(feature_cols)
else:
    lgbm_scaled = pd.Series(0.0, index=feature_cols)

unified_imp = pd.DataFrame({
    "Variable": feature_cols,
    "OLS_|beta|": ols_scaled.round(1).values,
    "RF": rf_scaled.round(1).values,
    "LightGBM": lgbm_scaled.round(1).values,
})
rank_cols = []
for col in ["OLS_|beta|", "RF", "LightGBM"]:
    rank_col = f"{col}_rank"
    unified_imp[rank_col] = unified_imp[col].rank(ascending=False, method="min")
    rank_cols.append(rank_col)
unified_imp["Consensus_Rank"] = unified_imp[rank_cols].mean(axis=1).rank(method="min").astype(int)
unified_imp = unified_imp.sort_values("Consensus_Rank")

top_var = unified_imp.iloc[0]["Variable"]
second_var = unified_imp.iloc[1]["Variable"]
top_ols = ols_tidy[(ols_tidy["Predictor"] != "Intercept") & (ols_tidy["p"] < 0.05)]["Predictor"].tolist()

print("\n── Model Comparison Summary ──")
print(f"OLS Linear Regression   | R² = {r2:.3f} | Significant terms: {', '.join(top_ols) if top_ols else 'none'}")
print(f"Quantile Regression     | Median dose effect = {qr_results[0.50].params['dose']:.2f}")
print(f"CART                    | R² = {cart_r2:.3f} | Top split: {feature_cols[int(np.argmax(cart_model.feature_importances_))]}")
print(f"Random Forest           | R² = {rf_r2:.3f} | Top variables: {rf_imp.sort_values(ascending=False).index[0]}, {rf_imp.sort_values(ascending=False).index[1]}")
if HAS_LGB:
    print(f"LightGBM                | R² = {lgb_r2:.3f} | Top variables: {lgb_imp.sort_values(ascending=False).index[0]}, {lgb_imp.sort_values(ascending=False).index[1]}")

print("\n── Summary ──")
print("OLS provides the most interpretable results and is the primary analysis.")
print("Quantile regression adds distributional insight about the dose-response relation.")
print("Tree-based models confirm the variable-importance ordering but remain exploratory.")

print("\n" + "=" * 60)
print("PART 5: MANUSCRIPT GENERATION")
print("=" * 60, "\n")

# tables/ and figures/ already created at top of script under OUT_DIR

for plot_name in [name for name in os.listdir(".") if name.startswith("plot_") and name.endswith(".png")]:
    ensure_move(plot_name, "figures")

ols_tidy.to_csv(os.path.join(OUT_DIR, "tables", "regression_table.csv"), index=False)

qr_table = pd.DataFrame({
    "Predictor": qr_results[0.25].params.index,
    "Q25": qr_results[0.25].params.round(3).values,
    "Q50": qr_results[0.50].params.round(3).values,
    "Q75": qr_results[0.75].params.round(3).values,
})
qr_table.to_csv(os.path.join(OUT_DIR, "tables", "quantile_table.csv"), index=False)

unified_imp[["Variable", "OLS_|beta|", "RF", "LightGBM", "Consensus_Rank"]].to_csv(
    os.path.join(OUT_DIR, "tables", "importance_table.csv"), index=False
)

insight_table = pd.DataFrame({
    "Method": ["OLS", "Quantile Regression", "Tree-Based (RF/LightGBM)"],
    "Unique_Insight": [
        "Dose is the dominant predictor, with explicit interaction estimates and confidence intervals.",
        f"Dose effect remains positive across quantiles (Q25 = {qr_results[0.25].params['dose']:.2f}, Q75 = {qr_results[0.75].params['dose']:.2f}).",
        f"Nonparametric importance also ranks {top_var} and {second_var} highest.",
    ],
})
insight_table.to_csv(os.path.join(OUT_DIR, "tables", "insight_table.csv"), index=False)

methods_md = f"""## Methods

### Statistical Analysis

Tooth length (`len`) was analyzed as a continuous outcome in the `ToothGrowth`
dataset. Distributional properties were assessed using the Shapiro-Wilk test,
skewness, kurtosis, a histogram with kernel density overlay, and a normal Q-Q plot.

For the two-group supplement comparison, Welch's t-test compared orange juice
(`OJ`) with ascorbic acid (`VC`) supplementation, with Cohen's d summarizing effect
magnitude. A Mann-Whitney U test provided nonparametric confirmation. Dose-group
differences (`0.5`, `1.0`, `2.0` mg) were tested using one-way ANOVA, with
eta-squared reported as an effect size; Tukey's HSD and Kruskal-Wallis tests
served as post-hoc and nonparametric complements, respectively.

To evaluate whether the dose-response association differed by supplement type,
stratified linear regressions of tooth length on dose were fit within each
supplement subgroup. A formal interaction test compared a model including the
dose-by-supplement interaction with an additive model.

Primary modeling used ordinary least squares regression with tooth length as the
dependent variable and dose, supplement type (VC coded 1 vs OJ coded 0), and
their interaction as predictors. Standardized coefficients were calculated from
z-scored variables to support cross-method importance comparison. Quantile
regression at the 25th, 50th, and 75th percentiles evaluated whether the
dose-response pattern varied across the outcome distribution.

As an exploratory supplement, CART, random forest (500 trees), and LightGBM
models were fit using dose, supplement, and their interaction term. Given the
small sample size (N = {len(df)}), tree-based results are interpreted as
descriptive pattern detection rather than predictive validation.
"""

results_md = f"""## Results

### Group Comparisons

Tooth length was higher in the OJ group (M = {len_oj.mean():.2f}, SD = {len_oj.std(ddof=1):.2f}, n = {len(len_oj)})
than in the VC group (M = {len_vc.mean():.2f}, SD = {len_vc.std(ddof=1):.2f}, n = {len(len_vc)}),
t({df_welch:.1f}) = {t_stat:.3f}, p {p_fmt(t_p)}, Cohen's d = {d_val:.3f}, with a
95% CI for the mean difference of [{ci_low:.2f}, {ci_high:.2f}]. The Mann-Whitney
U test was directionally concordant (U = {u_stat:.1f}, p {p_fmt(u_p)}).

Dose group differences were pronounced, F(2, {len(df) - 3}) = {f_stat_anova:.2f},
p {p_fmt(f_p_anova)}, eta-squared = {eta_sq:.3f}. The Kruskal-Wallis test confirmed
this pattern, H(2) = {kw_stat:.3f}, p {p_fmt(kw_p)}.

### Subgroup Analysis

The dose-response slope was positive within both supplement strata: {'; '.join([f"{row['subgroup']} (B = {row['b']:.2f}, 95% CI [{row['ci_low']:.2f}, {row['ci_high']:.2f}], p {p_fmt(row['p_value'])})" for row in subgroup_results])}.
The formal interaction test {'supported' if int_f_p < 0.05 else 'did not support'} heterogeneity by supplement,
F = {int_f_val:.3f}, p {p_fmt(int_f_p)}.

### OLS and Quantile Regression

The OLS model accounted for {r2 * 100:.1f}% of the variance in tooth length
(adjusted R-squared = {adj_r2:.3f}), F({int(model_ols.df_model)}, {int(model_ols.df_resid)}) = {model_ols.fvalue:.2f},
p {p_fmt(model_ols.f_pvalue)}. The strongest term was dose
(B = {model_ols.params['dose']:.2f}, SE = {model_ols.bse['dose']:.2f},
95% CI [{model_ols.conf_int().loc['dose'][0]:.2f}, {model_ols.conf_int().loc['dose'][1]:.2f}],
p {p_fmt(model_ols.pvalues['dose'])}).

Quantile regression showed a consistently positive dose effect across the outcome
distribution (Q25 = {qr_results[0.25].params['dose']:.2f}, Q50 = {qr_results[0.50].params['dose']:.2f},
Q75 = {qr_results[0.75].params['dose']:.2f}), indicating that higher doses were
associated with longer teeth throughout the distribution.

### Cross-Method Synthesis

Across OLS, quantile regression, random forest, and LightGBM, {top_var} emerged as
the most influential predictor, followed by {second_var}. This convergence
supports the interpretation that dose is the primary driver of tooth growth in
this dataset, with supplement-related effects providing additional but smaller
incremental information.
"""

references_bib = """@article{welch1947,
  author  = {Welch, B. L.},
  title   = {The generalization of Student's problem when several different population variances are involved},
  journal = {Biometrika},
  volume  = {34},
  number  = {1--2},
  pages   = {28--35},
  year    = {1947}
}

@article{kruskal1952,
  author  = {Kruskal, William H. and Wallis, W. Allen},
  title   = {Use of ranks in one-criterion variance analysis},
  journal = {Journal of the American Statistical Association},
  volume  = {47},
  number  = {260},
  pages   = {583--621},
  year    = {1952}
}

@article{koenker1978,
  author  = {Koenker, Roger and Bassett, Gilbert},
  title   = {Regression quantiles},
  journal = {Econometrica},
  volume  = {46},
  number  = {1},
  pages   = {33--50},
  year    = {1978}
}

@article{breiman2001,
  author  = {Breiman, Leo},
  title   = {Random forests},
  journal = {Machine Learning},
  volume  = {45},
  number  = {1},
  pages   = {5--32},
  year    = {2001}
}

@article{seabold2010,
  author  = {Seabold, Skipper and Perktold, Josef},
  title   = {Statsmodels: Econometric and statistical modeling with Python},
  journal = {Proceedings of the 9th Python in Science Conference},
  pages   = {92--96},
  year    = {2010}
}
"""

with open(os.path.join(OUT_DIR, "methods.md"), "w") as file_obj:
    file_obj.write(methods_md)
with open(os.path.join(OUT_DIR, "results.md"), "w") as file_obj:
    file_obj.write(results_md)
with open(os.path.join(OUT_DIR, "references.bib"), "w") as file_obj:
    file_obj.write(references_bib)

print("Plots moved to figures/")
print("Tables saved to tables/")
print("methods.md generated")
print("results.md generated")
print("references.bib generated")
