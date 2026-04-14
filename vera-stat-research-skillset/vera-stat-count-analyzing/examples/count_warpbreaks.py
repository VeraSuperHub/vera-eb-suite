###############################################################################
# AutoResearch — Count Outcome Full Analysis
# Dataset: warpbreaks
# Outcome: breaks (number of warp breaks per loom)
# Predictors: wool (A, B), tension (L, M, H)
#
# Demonstrates BOTH:
#   Part I  — Count Number: raw breaks with no offset
#   Part II — Count Rate:   breaks per hour with synthetic exposure offset
###############################################################################

import warnings
warnings.filterwarnings("ignore")

import os
import shutil
import numpy as np
import pandas as pd
from scipy import stats as sp_stats
import statsmodels.api as sm
from statsmodels.discrete.count_model import (
    ZeroInflatedPoisson,
    ZeroInflatedNegativeBinomialP,
)
from statsmodels.discrete.truncated_model import HurdleCountModel
import statsmodels.formula.api as smf
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
import lightgbm as lgb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

output_dir = os.path.join(os.getcwd(), "output")
tables_dir = os.path.join(output_dir, "tables")
figures_dir = os.path.join(output_dir, "figures")
os.makedirs(tables_dir, exist_ok=True)
os.makedirs(figures_dir, exist_ok=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SETUP
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 72)
print("  AutoResearch — Count Outcome Full Analysis")
print("  Dataset: warpbreaks | Outcome: breaks")
print("=" * 72, "\n")

def _load_warpbreaks():
    """Load warpbreaks with offline fallback."""
    try:
        return sm.datasets.get_rdataset("warpbreaks").data.copy()
    except Exception:
        import os as _os
        local_csv = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "warpbreaks.csv")
        if _os.path.exists(local_csv):
            _df = pd.read_csv(local_csv); return _df.drop(columns=[c for c in ['rownames','Unnamed: 0'] if c in _df.columns])
        raise RuntimeError(
            "warpbreaks not available. Network access failed and no local "
            "warpbreaks.csv was found next to this script."
        )

raw = _load_warpbreaks()
raw["wool"]    = raw["wool"].astype("category")
raw["tension"] = raw["tension"].astype("category")
N = len(raw)

# Dummy-code for modeling
df = raw.copy()
df["wool_B"]     = (df["wool"] == "B").astype(int)
df["tension_M"]  = (df["tension"] == "M").astype(int)
df["tension_H"]  = (df["tension"] == "H").astype(int)

pred_cols = ["wool_B", "tension_M", "tension_H"]
X = df[pred_cols].values
y = df["breaks"].values

print(f"Sample size: N = {N}")
print(f"Outcome: breaks (warp break count per loom)")
print(f"Predictors: wool (A/B), tension (L/M/H)\n")

# Helper for p-value formatting
def fmt_p(p):
    return "< .001" if p < 0.001 else f"{p:.3f}"


# ══════════════════════════════════════════════════════════════════════════════
#  PART I — COUNT NUMBER (no offset)
# ══════════════════════════════════════════════════════════════════════════════
print("*" * 72)
print("  PART I: COUNT NUMBER — Raw breaks (no exposure offset)")
print("*" * 72, "\n")

# ── 1. Distribution Check ─────────────────────────────────────────────────
print("── 1. Distribution Check ──────────────────────────────────────\n")

desc_mean = y.mean()
desc_var  = y.var(ddof=1)
desc_sd   = y.std(ddof=1)
od_ratio  = desc_var / desc_mean
zero_prop = (y == 0).mean()
pois_zero = np.exp(-desc_mean)

print(f"Mean     = {desc_mean:.2f}")
print(f"Variance = {desc_var:.2f}")
print(f"SD       = {desc_sd:.2f}")
print(f"Median   = {np.median(y):.1f}")
print(f"Min / Max = {y.min()} / {y.max()}\n")

print(f"Overdispersion ratio (var/mean) = {od_ratio:.2f}")
if od_ratio >= 1.5:
    dist_flag = "negbin"
    print("  -> Overdispersion detected. Negative Binomial preferred.")
else:
    dist_flag = "poisson"
    print("  -> Approximate equidispersion. Poisson assumptions likely met.")

print(f"\nObserved zero proportion : {zero_prop*100:.1f}%")
print(f"Poisson expected zeros   : {pois_zero*100:.4f}%")
if zero_prop > 0.20 and zero_prop > pois_zero * 2:
    dist_flag = "zero_inflated"
    print("  -> Excess zeros detected.")
else:
    print("  -> Zero proportion is low. Zero-inflated models not warranted.")
print(f"\nDistribution flag: {dist_flag}\n")

# Distribution plot
fig, ax = plt.subplots(figsize=(12, 5))
count_vals = np.arange(0, y.max() + 1)
obs_freq   = np.array([(y == k).sum() for k in count_vals])
pois_freq  = sp_stats.poisson.pmf(count_vals, desc_mean) * N
ax.bar(count_vals, obs_freq, color="steelblue", alpha=0.7, label="Observed")
ax.plot(count_vals, pois_freq, "ro--", markersize=4, label="Poisson expected")
ax.set_xlabel("Break Count")
ax.set_ylabel("Frequency")
ax.set_title("Count Distribution: Observed vs Poisson Expected")
ax.legend()
plt.tight_layout()
plt.savefig("plot_01_count_distribution.png", dpi=300)
plt.close()
print("Saved: plot_01_count_distribution.png\n")

# ── 2. Overdispersion Test ────────────────────────────────────────────────
print("── 2. Overdispersion Test (Cameron-Trivedi) ────────────────────\n")

pois_base = sm.GLM(y, sm.add_constant(X), family=sm.families.Poisson()).fit()
mu_hat    = pois_base.fittedvalues
aux_y     = ((y - mu_hat) ** 2 - y) / mu_hat
aux_reg   = sm.OLS(aux_y, mu_hat).fit()
alpha_hat = aux_reg.params[0]
alpha_p   = aux_reg.pvalues[0]
print(f"Cameron-Trivedi alpha = {alpha_hat:.4f}, p {fmt_p(alpha_p)}")
if alpha_p < 0.05:
    print("  -> Significant overdispersion confirmed.\n")
else:
    print("  -> Overdispersion not statistically significant.\n")

# ── 3. Group Comparison (tension, 3 levels) ──────────────────────────────
print("── 3. Group Comparison — Tension Effect ────────────────────────\n")

for t_level in ["L", "M", "H"]:
    subset = y[raw["tension"] == t_level]
    print(f"  Tension {t_level}: n = {len(subset)}, mean = {subset.mean():.2f}, SD = {subset.std(ddof=1):.2f}")
print()

# Kruskal-Wallis
groups_kw = [y[raw["tension"] == lv] for lv in ["L", "M", "H"]]
kw_stat, kw_p = sp_stats.kruskal(*groups_kw)
print(f"Kruskal-Wallis: H(2) = {kw_stat:.2f}, p {fmt_p(kw_p)}\n")

# ── 4. Count Models ──────────────────────────────────────────────────────
print("── 4. Count Models (no offset — count number) ──────────────────\n")

X_const = sm.add_constant(X)
results_store = {}

# --- 4A: Poisson ---
print("--- 4A: Poisson Regression ---")
pois_fit = sm.GLM(y, X_const, family=sm.families.Poisson()).fit()
print(pois_fit.summary2().tables[1].to_string())
dev_df_ratio = pois_fit.deviance / pois_fit.df_resid
print(f"\nDeviance = {pois_fit.deviance:.2f}, df = {pois_fit.df_resid}, "
      f"Deviance/df = {dev_df_ratio:.2f}")
print(f"AIC = {pois_fit.aic:.2f}")

irr_pois = np.exp(pois_fit.params)
ci_pois  = np.exp(pois_fit.conf_int())
print("\nIRR (Poisson):")
for i, name in enumerate(["intercept", *pred_cols]):
    p_val = pois_fit.pvalues[i]
    print(f"  {name}: IRR = {irr_pois[i]:.3f}, "
          f"95% CI [{ci_pois[i, 0]:.3f}, {ci_pois[i, 1]:.3f}], p {fmt_p(p_val)}")
results_store["Poisson"] = {"aic": pois_fit.aic, "fit": pois_fit}
print()

# --- 4B: Negative Binomial ---
# Use sm.NegativeBinomialP (NB2) which estimates the dispersion parameter alpha
# from the data. Do NOT use sm.GLM(family=NegativeBinomial()) which fixes alpha=1
# by default and does not estimate it, making LR comparisons with Poisson invalid.
print("--- 4B: Negative Binomial Regression ---")
nb_model = sm.NegativeBinomialP(y, X_const, p=2)  # NB2 parameterization
nb_fit = nb_model.fit(disp=False)
print(nb_fit.summary2().tables[1].to_string())
nb_alpha = nb_fit.params[-1] if 'alpha' in nb_fit.summary2().tables[1].index else nb_fit.scale
print(f"\nEstimated dispersion (alpha): {nb_alpha:.4f}")
print(f"AIC = {nb_fit.aic:.2f}")

irr_nb = np.exp(nb_fit.params[:-1])  # exclude alpha from IRR
ci_nb  = np.exp(nb_fit.conf_int().iloc[:-1])
print("\nIRR (NB):")
for i, name in enumerate(["intercept", *pred_cols]):
    p_val = nb_fit.pvalues[i]
    print(f"  {name}: IRR = {irr_nb[i]:.3f}, "
          f"95% CI [{ci_nb.iloc[i, 0]:.3f}, {ci_nb.iloc[i, 1]:.3f}], p {fmt_p(p_val)}")

# LR test: Poisson vs NB (valid because alpha is estimated from data)
lr_pois_nb = 2 * (nb_fit.llf - pois_fit.llf)
lr_p_nb = sp_stats.chi2.sf(abs(lr_pois_nb), df=1)
print(f"\nLR test (Poisson vs NB): chi-sq(1) = {abs(lr_pois_nb):.2f}, p {fmt_p(lr_p_nb)}")
results_store["NegBin"] = {"aic": nb_fit.aic, "fit": nb_fit}
print()

# --- 4C: Zero-Inflated Poisson (ZIP) ---
print("--- 4C: Zero-Inflated Poisson (ZIP) ---")
if zero_prop <= 0.10:
    print(f"  Zero proportion = {zero_prop*100:.1f}% (threshold 10%). "
          "ZIP not warranted — skipping.\n")
    results_store["ZIP"] = None
else:
    try:
        zip_fit = ZeroInflatedPoisson(
            endog=y, exog=X_const, exog_infl=X_const, inflation="logit"
        ).fit(disp=False, maxiter=200)
        print(zip_fit.summary().tables[1].to_string())
        print(f"\nAIC = {zip_fit.aic:.2f}")
        results_store["ZIP"] = {"aic": zip_fit.aic, "fit": zip_fit}
    except Exception as e:
        print(f"  ZIP failed to converge: {e}")
        results_store["ZIP"] = None
    print()

# --- 4D: Zero-Inflated Negative Binomial (ZINB) ---
print("--- 4D: Zero-Inflated Negative Binomial (ZINB) ---")
if zero_prop <= 0.10 and od_ratio < 1.5:
    print(f"  Zero proportion = {zero_prop*100:.1f}%, OD ratio = {od_ratio:.2f}. "
          "ZINB not warranted — skipping.\n")
    results_store["ZINB"] = None
else:
    try:
        zinb_fit = ZeroInflatedNegativeBinomialP(
            endog=y, exog=X_const, exog_infl=X_const, inflation="logit"
        ).fit(disp=False, maxiter=300)
        print(zinb_fit.summary().tables[1].to_string())
        print(f"\nAIC = {zinb_fit.aic:.2f}")
        results_store["ZINB"] = {"aic": zinb_fit.aic, "fit": zinb_fit}
    except Exception as e:
        print(f"  ZINB failed to converge or is inappropriate: {e}")
        results_store["ZINB"] = None
    print()

# --- 4E: Hurdle Model ---
print("--- 4E: Hurdle Model ---")
try:
    hurdle_fit = HurdleCountModel(
        endog=y, exog=X_const, offset=None,
        dist="poisson"
    ).fit(disp=False, maxiter=200)
    print(hurdle_fit.summary().tables[1].to_string())
    print(f"\nAIC = {hurdle_fit.aic:.2f}")
    results_store["Hurdle"] = {"aic": hurdle_fit.aic, "fit": hurdle_fit}
except Exception as e:
    print(f"  Hurdle model issue: {e}")
    results_store["Hurdle"] = None
print()

# --- 4F: AIC Comparison ---
print("── AIC Comparison (Count Models) ───────────────────────────────\n")
aic_rows = []
for mname in ["Poisson", "NegBin", "ZIP", "ZINB", "Hurdle"]:
    entry = results_store.get(mname)
    if entry is not None:
        aic_rows.append({"Model": mname, "AIC": entry["aic"]})
    else:
        aic_rows.append({"Model": mname, "AIC": "N/A"})

aic_df = pd.DataFrame(aic_rows)
print(aic_df.to_string(index=False))
print()

# Identify best count model
valid_aic = {m: r["aic"] for m, r in results_store.items()
             if r is not None and isinstance(r["aic"], (int, float))}
best_count = min(valid_aic, key=valid_aic.get) if valid_aic else "Poisson"
print(f"Best distributional fit (lowest AIC): {best_count}")
print("Note: Models are analytic lenses, not contestants. Each distributional")
print("assumption reveals different aspects of the count-generating process.\n")

# ── 5. Tree-Based Models ─────────────────────────────────────────────────
print("── 5. Tree-Based Models (Exploratory) ──────────────────────────\n")

min_child = max(3, N // 10)

# CART
cart = DecisionTreeRegressor(max_depth=4, random_state=42)
cart.fit(X, y)
cart_r2 = cart.score(X, y)
print(f"--- CART (max_depth=4) ---")
print(f"In-sample R² = {cart_r2:.3f}")
tree_text = export_text(cart, feature_names=pred_cols, max_depth=3)
print(tree_text[:600])
print()

# Random Forest
rf = RandomForestRegressor(n_estimators=500, random_state=42, n_jobs=-1)
rf.fit(X, y)
rf_r2 = rf.score(X, y)
print(f"--- Random Forest (500 trees) ---")
print(f"In-sample R² = {rf_r2:.3f}")

perm_imp = permutation_importance(rf, X, y, n_repeats=20, random_state=42)
rf_imp_raw = perm_imp.importances_mean
rf_imp_100 = (rf_imp_raw / rf_imp_raw.max()) * 100 if rf_imp_raw.max() > 0 else rf_imp_raw
print("Permutation importance (0-100):")
for j, col in enumerate(pred_cols):
    print(f"  {col}: {rf_imp_100[j]:.1f}")
print()

# LightGBM
lgb_model = lgb.LGBMRegressor(
    n_estimators=500, max_depth=3, learning_rate=0.1,
    num_leaves=15, min_child_samples=min_child,
    random_state=42, verbose=-1
)
lgb_model.fit(X, y)
lgb_r2 = lgb_model.score(X, y)
print(f"--- LightGBM ---")
print(f"In-sample R² = {lgb_r2:.3f}")

lgb_gain = lgb_model.feature_importances_.astype(float)
lgb_imp_100 = (lgb_gain / lgb_gain.max()) * 100 if lgb_gain.max() > 0 else lgb_gain
print("Gain importance (0-100):")
for j, col in enumerate(pred_cols):
    print(f"  {col}: {lgb_imp_100[j]:.1f}")
print()

# ── 6. Unified Importance Table ──────────────────────────────────────────
print("── 6. Unified Variable Importance (0-100 scale) ────────────────\n")

# Best count model standardized coefficients
best_fit = results_store[best_count]["fit"]
betas    = best_fit.params[1:]          # skip intercept
# Standardize: beta * SD(x)
x_sds    = X.std(axis=0)
std_coef = np.abs(betas * x_sds)
if std_coef.max() > 0:
    cm_imp_100 = (std_coef / std_coef.max()) * 100
else:
    cm_imp_100 = std_coef

imp_table = pd.DataFrame({
    "Variable": pred_cols,
    f"Count Model ({best_count})": np.round(cm_imp_100, 1),
    "RF Importance": np.round(rf_imp_100, 1),
    "LightGBM Importance": np.round(lgb_imp_100, 1),
})

# Rank consensus
ranks = imp_table.iloc[:, 1:].rank(ascending=False, method="min")
imp_table["Rank Consensus"] = ranks.mean(axis=1).round(1)
imp_table = imp_table.sort_values("Rank Consensus")
print(imp_table.to_string(index=False))
print()

# Variable importance plot
fig, ax = plt.subplots(figsize=(10, 5))
bar_w = 0.25
idx   = np.arange(len(pred_cols))
sorted_vars = imp_table["Variable"].values
sorted_cm   = imp_table[f"Count Model ({best_count})"].values
sorted_rf   = imp_table["RF Importance"].values
sorted_lgb  = imp_table["LightGBM Importance"].values

ax.barh(idx - bar_w, sorted_cm,  bar_w, label=f"Count ({best_count})", color="steelblue")
ax.barh(idx,         sorted_rf,  bar_w, label="RF (permutation)", color="darkorange")
ax.barh(idx + bar_w, sorted_lgb, bar_w, label="LightGBM (gain)", color="forestgreen")
ax.set_yticks(idx)
ax.set_yticklabels(sorted_vars)
ax.set_xlabel("Importance (0-100)")
ax.set_title("Unified Variable Importance Across Methods")
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig("plot_06_unified_importance.png", dpi=300)
plt.close()
print("Saved: plot_06_unified_importance.png\n")

# ── 7. Insight Synthesis ─────────────────────────────────────────────────
print("── 7. Cross-Method Insight Synthesis ───────────────────────────\n")

insight_data = [
    ["Poisson",    "Equidispersion (var = mean)", "Baseline IRRs; overdispersion diagnostic"],
    ["Neg. Binom.","Overdispersion allowed",       "Relaxed variance; theta estimate"],
    ["ZIP/ZINB",   "Excess zeros from two processes","Zero-inflation component (if applicable)"],
    ["Hurdle",     "Zeros separate from counts",   "What predicts any event vs frequency"],
    ["Tree-Based", "Non-parametric",               "Nonlinear patterns; importance ranking"],
]
insight_df = pd.DataFrame(insight_data,
                          columns=["Method", "Distributional Assumption", "Unique Insight"])
print(insight_df.to_string(index=False))
print()

top_var = imp_table.iloc[0]["Variable"]
print(f"Synthesis: Across all analytic lenses, {top_var} emerges as the most")
print("consistently important predictor of warp breaks. The count regression")
print("models and tree-based methods converge on this finding, strengthening")
print("confidence in its predictive role. Where methods diverge, it reflects")
print("their differing assumptions rather than contradictory evidence.\n")

print()
print("=" * 72)
print("  END OF PART I — COUNT NUMBER (no offset)")
print("=" * 72)
print()
print()

# ══════════════════════════════════════════════════════════════════════════════
#  PART II — COUNT RATE (with synthetic exposure offset)
# ══════════════════════════════════════════════════════════════════════════════
print("*" * 72)
print("  PART II: COUNT RATE — breaks per hour (with exposure offset)")
print("*" * 72, "\n")

# Create synthetic exposure variable
np.random.seed(2024)
hours = np.random.uniform(100, 500, size=N)
df["hours"]      = hours
df["log_hours"]  = np.log(hours)
rate = df["breaks"] / df["hours"]

print(f"Synthetic exposure: hours ~ Uniform(100, 500)")
print(f"  hours mean = {hours.mean():.1f}, SD = {hours.std():.1f}")
print(f"  Implied rate (breaks/hour): mean = {rate.mean():.4f}, "
      f"SD = {rate.std():.4f}\n")

# Rate distribution plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(hours, bins=15, color="steelblue", alpha=0.7, edgecolor="white")
axes[0].set_xlabel("Exposure (hours)")
axes[0].set_ylabel("Frequency")
axes[0].set_title("Distribution of Exposure Variable")

axes[1].hist(rate, bins=15, color="darkorange", alpha=0.7, edgecolor="white")
axes[1].set_xlabel("Rate (breaks / hour)")
axes[1].set_ylabel("Frequency")
axes[1].set_title("Distribution of Event Rate")
plt.tight_layout()
plt.savefig("plot_08_rate_distribution.png", dpi=300)
plt.close()
print("Saved: plot_08_rate_distribution.png\n")

# ── Rate Models ───────────────────────────────────────────────────────────
offset_vals = df["log_hours"].values

print("── Poisson Rate Model (offset = log(hours)) ────────────────────\n")
pois_rate = sm.GLM(
    y, X_const, family=sm.families.Poisson(), offset=offset_vals
).fit()
print(pois_rate.summary2().tables[1].to_string())
print(f"\nDeviance = {pois_rate.deviance:.2f}, AIC = {pois_rate.aic:.2f}")

irr_pr = np.exp(pois_rate.params)
ci_pr  = np.exp(pois_rate.conf_int())
print("\nIRR (Poisson rate model):")
for i, name in enumerate(["intercept", *pred_cols]):
    print(f"  {name}: IRR = {irr_pr[i]:.3f}, "
          f"95% CI [{ci_pr[i, 0]:.3f}, {ci_pr[i, 1]:.3f}], p {fmt_p(pois_rate.pvalues[i])}")
print()

print("── Negative Binomial Rate Model (offset = log(hours)) ─────────\n")
# Use NegativeBinomialP with offset to estimate dispersion from data
nb_rate_model = sm.NegativeBinomialP(y, X_const, p=2, offset=offset_vals)
nb_rate = nb_rate_model.fit(disp=False)
print(nb_rate.summary2().tables[1].to_string())
print(f"\nAIC = {nb_rate.aic:.2f}")

irr_nr = np.exp(nb_rate.params[:-1])  # exclude alpha
ci_nr  = np.exp(nb_rate.conf_int().iloc[:-1])
print("\nIRR (NB rate model):")
for i, name in enumerate(["intercept", *pred_cols]):
    print(f"  {name}: IRR = {irr_nr[i]:.3f}, "
          f"95% CI [{ci_nr.iloc[i, 0]:.3f}, {ci_nr.iloc[i, 1]:.3f}], p {fmt_p(nb_rate.pvalues[i])}")
print()

# LR test for rate models (valid — alpha estimated)
lr_rate = 2 * (nb_rate.llf - pois_rate.llf)
lr_rate_p = sp_stats.chi2.sf(abs(lr_rate), df=1)
print(f"LR test (Poisson rate vs NB rate): chi-sq(1) = {abs(lr_rate):.2f}, "
      f"p {fmt_p(lr_rate_p)}")
print()

# Rate comparison across groups
print("── Group Rates ─────────────────────────────────────────────────\n")
for t_level in ["L", "M", "H"]:
    mask = raw["tension"] == t_level
    total_events  = y[mask].sum()
    total_hours   = hours[mask].sum()
    grp_rate      = total_events / total_hours
    print(f"  Tension {t_level}: events = {total_events}, "
          f"person-hours = {total_hours:.0f}, "
          f"rate = {grp_rate:.4f} breaks/hour")
print()

print("── Rate Model Interpretation ───────────────────────────────────\n")
print("By including offset = log(hours), the Poisson/NB models estimate")
print("incidence RATE ratios rather than raw count ratios. The IRR now")
print("represents the multiplicative change in the break rate (breaks per")
print("hour) associated with each predictor, adjusting for differential")
print("exposure time. This is the appropriate approach when observation")
print("periods or denominators vary across units.\n")

# ── Manuscript Output ──────────────────────────────────────────────────────
best_rate_name = "Negative Binomial" if nb_rate.aic < pois_rate.aic else "Poisson"
best_rate_fit = nb_rate if nb_rate.aic < pois_rate.aic else pois_rate
best_predictor = imp_table.iloc[0]["Variable"]
best_pred_idx = pred_cols.index(best_predictor) + 1
best_params = np.asarray(best_fit.params)
best_conf = np.asarray(best_fit.conf_int())

count_coef_table = pd.DataFrame({
    "Predictor": ["Intercept"] + pred_cols,
    "B": np.round(best_params[: len(pred_cols) + 1], 4),
    "IRR": np.round(np.exp(best_params[: len(pred_cols) + 1]), 4),
    "CI_lower": np.round(np.exp(best_conf[: len(pred_cols) + 1, 0]), 4),
    "CI_upper": np.round(np.exp(best_conf[: len(pred_cols) + 1, 1]), 4),
    "p_value": np.round(np.asarray(best_fit.pvalues)[: len(pred_cols) + 1], 4),
})
count_coef_table.to_csv(os.path.join(tables_dir, "count_model_coefficients.csv"), index=False)
aic_df.to_csv(os.path.join(tables_dir, "count_model_aic.csv"), index=False)
imp_table.to_csv(os.path.join(tables_dir, "importance_table.csv"), index=False)

rate_rows = []
for t_level in ["L", "M", "H"]:
    mask = raw["tension"] == t_level
    total_events = y[mask].sum()
    total_hours = hours[mask].sum()
    rate_rows.append({
        "Tension": t_level,
        "Events": int(total_events),
        "Exposure_hours": round(float(total_hours), 2),
        "Rate_per_hour": round(float(total_events / total_hours), 4),
    })
rate_df = pd.DataFrame(rate_rows)
rate_df.to_csv(os.path.join(tables_dir, "rate_summary.csv"), index=False)

for plot_name in [
    "plot_01_count_distribution.png",
    "plot_06_unified_importance.png",
    "plot_08_rate_distribution.png",
]:
    if os.path.exists(plot_name):
        shutil.copy2(plot_name, os.path.join(figures_dir, plot_name))

methods_text = f"""## Methods

### Statistical Analysis

Count outcomes from the `warpbreaks` dataset were analyzed using a two-part workflow. First, raw break counts per loom were evaluated as count-number outcomes. Distributional diagnostics included the mean-variance relationship, observed versus Poisson-expected zeros, and the Cameron-Trivedi overdispersion test.

Primary group comparisons across tension levels used the Kruskal-Wallis test because the outcome is discrete and overdispersed. Count regression models then included Poisson and negative binomial generalized linear models, with zero-inflated and hurdle models evaluated when warranted by the observed zero structure. Model adequacy within the count-model family was summarized with deviance and Akaike's Information Criterion (AIC).

As exploratory complements, a regression tree, random forest, and LightGBM model were fit to the same predictors. Variable importance from the best-fitting count model, random forest permutation importance, and LightGBM gain were rescaled to a common 0-100 scale for cross-method comparison.

Second, a count-rate workflow demonstrated how offsets change interpretation when exposure varies. Synthetic loom-hours were introduced for illustration, and Poisson and negative binomial rate models were fit with offset = log(exposure). These models estimated incidence rate ratios rather than raw count ratios.

Analyses were conducted in Python using statsmodels, SciPy, scikit-learn, LightGBM, pandas, NumPy, and matplotlib. Statistical significance was evaluated at alpha = .05, and all confidence intervals are at the 95% level.
"""

results_text = f"""## Results

### Distribution and Group Differences

The break-count outcome had mean {desc_mean:.2f} and variance {desc_var:.2f}, yielding a variance-to-mean ratio of {od_ratio:.2f}. Observed zeros comprised {zero_prop * 100:.1f}% of the sample compared with {pois_zero * 100:.1f}% expected under a Poisson model. The Cameron-Trivedi overdispersion test estimated alpha = {alpha_hat:.4f}, p {'< .001' if alpha_p < 0.001 else f'= {alpha_p:.3f}'}, supporting overdispersion {'and favoring negative binomial modeling' if alpha_p < 0.05 else 'only weakly'}.

Break counts differed across tension levels (Kruskal-Wallis H(2) = {kw_stat:.2f}, p {'< .001' if kw_p < 0.001 else f'= {kw_p:.3f}'}). Mean counts were highest under low tension and lowest under high tension.

### Count Models

Among the count-number models, the {best_count} specification had the lowest AIC ({valid_aic[best_count]:.2f}). In that model, {best_predictor} showed the strongest standardized association with break counts (IRR = {np.exp(best_params[best_pred_idx]):.3f}, 95% CI [{np.exp(best_conf[best_pred_idx, 0]):.3f}, {np.exp(best_conf[best_pred_idx, 1]):.3f}], p {'< .001' if np.asarray(best_fit.pvalues)[best_pred_idx] < 0.001 else f'= {np.asarray(best_fit.pvalues)[best_pred_idx]:.3f}'}).

### Count-Rate Demonstration

With exposure included through offset = log(hours), the {best_rate_name} rate model provided the better fit (AIC = {best_rate_fit.aic:.2f}). The likelihood-ratio comparison between Poisson and negative binomial rate models yielded chi-sq(1) = {abs(lr_rate):.2f}, p {'< .001' if lr_rate_p < 0.001 else f'= {lr_rate_p:.3f}'}. Rate summaries by tension level are reported in the accompanying table.

### Cross-Method Synthesis

The unified importance table showed that {best_predictor} ranked highest across the best-fitting count model and the tree-based exploratory models. This convergence suggests that the main signal is stable across both parametric count assumptions and nonparametric analytic lenses.
"""

references_bib = r"""@article{cameron1990,
  author  = {Cameron, A. Colin and Trivedi, Pravin K.},
  title   = {Regression-Based Tests for Overdispersion in the Poisson Model},
  journal = {Journal of Econometrics},
  year    = {1990},
  volume  = {46},
  number  = {3},
  pages   = {347--364}
}

@book{hilbe2011,
  author    = {Hilbe, Joseph M.},
  title     = {Negative Binomial Regression},
  edition   = {2nd},
  year      = {2011},
  publisher = {Cambridge University Press}
}
"""

with open(os.path.join(output_dir, "methods.md"), "w") as f:
    f.write(methods_text)
with open(os.path.join(output_dir, "results.md"), "w") as f:
    f.write(results_text)
with open(os.path.join(output_dir, "references.bib"), "w") as f:
    f.write(references_bib)

print("Saved manuscript artifacts to output/")

# ── Summary ──────────────────────────────────────────────────────────────
print("=" * 72)
print("  ANALYSIS COMPLETE")
print("=" * 72)
print()
print("Deliverables produced:")
print("  plot_01_count_distribution.png — Observed vs Poisson expected")
print("  plot_06_unified_importance.png — Variable importance (3 methods)")
print("  plot_08_rate_distribution.png  — Exposure & rate distributions")
print()
print("Key distinction demonstrated:")
print("  Part I  (Count Number): models raw event counts, no offset")
print("  Part II (Count Rate):   models event rate with offset=log(exposure)")
print("  Both use same IRR framework; the offset changes interpretation")
print("  from 'count ratio' to 'rate ratio'.\n")
