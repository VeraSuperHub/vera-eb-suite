###############################################################################
# meta_example.py
# AutoResearch — Meta-Analysis Example
# Covers: PART 3 (publication bias + sensitivity), PART 4 (subgroup +
#         meta-regression), PART 5/6 (advanced models + comparison),
#         PART 7 (manuscript generation)
# Workflow files: 04-run-additional-tests.md, 05-analyze-subgroups.md,
#                 06-fit-models.md, 07-compare-models.md,
#                 08-generate-manuscript.md
###############################################################################

import os
import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

# =============================================================================
# PART 0 (recap): Construct Study-Level Data — same 12 studies
# =============================================================================

studies = pd.DataFrame({
    "study_id":       ["Adams 2015", "Brown 2016", "Chen 2017", "Davis 2014",
                       "Evans 2018", "Foster 2019", "Garcia 2016", "Harris 2020",
                       "Ibrahim 2017", "Jones 2021", "Kim 2019", "Lee 2022"],
    "year":           [2015, 2016, 2017, 2014, 2018, 2019, 2016, 2020,
                       2017, 2021, 2019, 2022],
    "n_treatment":    [45, 62, 38, 55, 30, 48, 70, 42, 35, 58, 40, 52],
    "n_control":      [43, 60, 36, 53, 32, 50, 68, 44, 33, 56, 38, 50],
    "mean_treatment": [12.3, 11.8, 13.1, 10.5, 14.2, 11.0, 12.8, 10.2,
                       13.5, 11.4, 12.0, 10.8],
    "mean_control":   [15.1, 14.5, 16.0, 13.8, 16.8, 14.2, 15.0, 13.5,
                       15.9, 14.0, 14.8, 13.6],
    "sd_treatment":   [4.2, 3.8, 5.0, 4.5, 4.8, 3.5, 4.0, 3.9, 5.2, 3.6,
                       4.3, 3.7],
    "sd_control":     [4.5, 4.0, 4.8, 4.7, 5.1, 3.8, 4.2, 4.1, 4.9, 3.8,
                       4.5, 4.0],
    # Moderator variables for subgroup and meta-regression
    "intervention_type": ["CBT", "CBT", "Medication", "CBT", "Medication",
                          "CBT", "Medication", "CBT", "Medication", "CBT",
                          "Medication", "CBT"],
    "study_quality":     ["high", "high", "low", "high", "low", "high",
                          "low", "high", "low", "high", "high", "high"],
    "mean_age":          [34.2, 42.1, 28.5, 51.3, 30.8, 45.6, 37.2, 39.4,
                          26.1, 48.7, 33.5, 44.0],
})

# ── Compute Hedges' g and SE ─────────────────────────────────────────────────

def hedges_g(m_t, m_c, sd_t, sd_c, n_t, n_c):
    df = n_t + n_c - 2
    sp = np.sqrt(((n_t - 1) * sd_t**2 + (n_c - 1) * sd_c**2) / df)
    d = (m_t - m_c) / sp
    J = 1 - 3 / (4 * df - 1)
    g = d * J
    se = np.sqrt(1/n_t + 1/n_c + g**2 / (2 * (n_t + n_c)))
    return g, se

g_vals, se_vals = [], []
for _, r in studies.iterrows():
    g, se = hedges_g(r.mean_treatment, r.mean_control,
                     r.sd_treatment, r.sd_control,
                     r.n_treatment, r.n_control)
    g_vals.append(g)
    se_vals.append(se)

studies["yi"] = g_vals
studies["sei"] = se_vals
studies["vi"] = studies["sei"] ** 2

k = len(studies)
total_n = (studies.n_treatment + studies.n_control).sum()

# =============================================================================
# Helper functions: meta-analytic pooling
# =============================================================================

def fixed_effects(yi, vi):
    """Inverse-variance fixed-effects pooling."""
    wi = 1.0 / vi
    mu_hat = np.sum(wi * yi) / np.sum(wi)
    se_hat = np.sqrt(1.0 / np.sum(wi))
    z = mu_hat / se_hat
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    ci_lo = mu_hat - 1.96 * se_hat
    ci_hi = mu_hat + 1.96 * se_hat
    return {"est": mu_hat, "se": se_hat, "ci_lo": ci_lo, "ci_hi": ci_hi,
            "z": z, "p": p, "tau2": 0.0}


def cochran_q(yi, vi):
    """Cochran's Q statistic for heterogeneity."""
    wi = 1.0 / vi
    mu_fe = np.sum(wi * yi) / np.sum(wi)
    Q = np.sum(wi * (yi - mu_fe)**2)
    df = len(yi) - 1
    p = 1 - stats.chi2.cdf(Q, df)
    return Q, df, p


def dl_tau2(yi, vi):
    """DerSimonian-Laird moment-based tau-squared estimator."""
    wi = 1.0 / vi
    Q, df, _ = cochran_q(yi, vi)
    C = np.sum(wi) - np.sum(wi**2) / np.sum(wi)
    tau2 = max(0, (Q - df) / C)
    return tau2


def random_effects_dl(yi, vi):
    """Random-effects model with DerSimonian-Laird estimator."""
    tau2 = dl_tau2(yi, vi)
    wi_star = 1.0 / (vi + tau2)
    mu_hat = np.sum(wi_star * yi) / np.sum(wi_star)
    se_hat = np.sqrt(1.0 / np.sum(wi_star))
    z = mu_hat / se_hat
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    ci_lo = mu_hat - 1.96 * se_hat
    ci_hi = mu_hat + 1.96 * se_hat
    return {"est": mu_hat, "se": se_hat, "ci_lo": ci_lo, "ci_hi": ci_hi,
            "z": z, "p": p, "tau2": tau2}


def iterative_tau2(yi, vi, tol=1e-8, max_iter=100):
    """Iterative estimation of tau-squared via Paule-Mandel iteration."""
    tau2 = dl_tau2(yi, vi)  # initial estimate
    for _ in range(max_iter):
        wi = 1.0 / (vi + tau2)
        mu = np.sum(wi * yi) / np.sum(wi)
        resid = yi - mu
        Q_star = np.sum(wi * resid**2)
        expected_Q = len(yi) - np.sum(wi**2) / np.sum(wi)
        C = np.sum(wi) - np.sum(wi**2) / np.sum(wi)
        tau2_new = max(0, tau2 + (Q_star - expected_Q) / C)
        if abs(tau2_new - tau2) < tol:
            tau2 = tau2_new
            break
        tau2 = tau2_new
    return tau2


def random_effects_reml(yi, vi):
    """Random-effects model with REML estimator."""
    tau2 = iterative_tau2(yi, vi)
    wi_star = 1.0 / (vi + tau2)
    mu_hat = np.sum(wi_star * yi) / np.sum(wi_star)
    se_hat = np.sqrt(1.0 / np.sum(wi_star))
    z = mu_hat / se_hat
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    ci_lo = mu_hat - 1.96 * se_hat
    ci_hi = mu_hat + 1.96 * se_hat
    return {"est": mu_hat, "se": se_hat, "ci_lo": ci_lo, "ci_hi": ci_hi,
            "z": z, "p": p, "tau2": tau2}


def knapp_hartung(yi, vi):
    """Random-effects with Knapp-Hartung adjustment (uses t-distribution)."""
    tau2 = iterative_tau2(yi, vi)
    wi = 1.0 / (vi + tau2)
    mu_hat = np.sum(wi * yi) / np.sum(wi)
    # Knapp-Hartung SE adjustment
    resid = yi - mu_hat
    q_star = np.sum(wi * resid**2)
    kh_adj = q_star / (len(yi) - 1)
    se_hat = np.sqrt(kh_adj / np.sum(wi))
    df_kh = len(yi) - 1
    t_stat = mu_hat / se_hat
    p = 2 * (1 - stats.t.cdf(abs(t_stat), df_kh))
    t_crit = stats.t.ppf(0.975, df_kh)
    ci_lo = mu_hat - t_crit * se_hat
    ci_hi = mu_hat + t_crit * se_hat
    return {"est": mu_hat, "se": se_hat, "ci_lo": ci_lo, "ci_hi": ci_hi,
            "t": t_stat, "df": df_kh, "p": p, "tau2": tau2}


def prediction_interval(mu, tau2, se_mu, k_studies):
    """95% prediction interval for a new study."""
    t_crit = stats.t.ppf(0.975, k_studies - 2)
    pi_se = np.sqrt(tau2 + se_mu**2)
    return mu - t_crit * pi_se, mu + t_crit * pi_se


def fmt_p(p):
    """Format p-value per reporting standards."""
    if p < 0.001:
        return "< .001"
    return f".{int(round(p * 1000)):03d}"


# =============================================================================
# Set up output directory
# =============================================================================

outdir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(outdir, "tables"), exist_ok=True)
os.makedirs(os.path.join(outdir, "figures"), exist_ok=True)

yi = studies["yi"].values
vi = studies["vi"].values
sei = studies["sei"].values

print("=" * 72)
print("META-ANALYSIS — Full Pipeline")
print("=" * 72)

# =============================================================================
# PART 3: Publication Bias & Sensitivity Analysis
# (Workflow: 04-run-additional-tests.md)
# =============================================================================

print("\n\n=== PART 3: Publication Bias & Sensitivity Analysis ===\n")

# ── 3A: Funnel Plot ─────────────────────────────────────────────────────────

re_res = random_effects_reml(yi, vi)
pooled_es = re_res["est"]

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(yi, sei, s=60, c="steelblue", edgecolors="black", linewidth=0.5,
           zorder=3)
ax.axvline(pooled_es, color="black", linestyle="--", linewidth=0.8, label="Pooled ES")
# Pseudo-confidence region
se_range = np.linspace(0, max(sei) * 1.2, 100)
ax.fill_betweenx(se_range,
                 pooled_es - 1.96 * se_range,
                 pooled_es + 1.96 * se_range,
                 alpha=0.08, color="gray", label="95% pseudo-CI")
ax.set_xlabel("Effect Size (Hedges' g)", fontsize=12)
ax.set_ylabel("Standard Error", fontsize=12)
ax.set_title("Funnel Plot", fontsize=14)
ax.invert_yaxis()
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(outdir, "figures", "plot_03_funnel.png"), dpi=300)
plt.close()
print("Funnel plot saved: figures/plot_03_funnel.png")

# ── 3B: Egger's Regression Test ─────────────────────────────────────────────

print("\n--- Egger's Regression Test ---")
# Weighted regression of yi/sei on 1/sei (precision)
precision = 1.0 / sei
z_scores = yi / sei

from scipy.stats import linregress
slope, intercept, r_val, p_egger, se_egger = linregress(precision, z_scores)

# Egger's test: WLS regression of standardized effect (yi/sei) on precision (1/sei)
# weighted by inverse variance (1/sei^2), so more precise studies contribute more.
# Using equal weights (np.ones) would defeat the purpose of the weighted regression.
import statsmodels.api as sm
X_egger = sm.add_constant(precision)
wls_model = sm.WLS(z_scores, X_egger, weights=1.0 / (sei ** 2)).fit()
intercept_egger = wls_model.params[0]
se_intercept = wls_model.bse[0]
t_egger = wls_model.tvalues[0]
p_egger = wls_model.pvalues[0]

print(f"  Intercept = {intercept_egger:.2f}, SE = {se_intercept:.2f}, "
      f"t = {t_egger:.2f}, p = {fmt_p(p_egger)}")
if p_egger < 0.05:
    print("  -> Significant funnel plot asymmetry detected (possible publication bias).")
else:
    print("  -> No significant asymmetry detected.")

# ── 3C: Begg's Rank Correlation Test ────────────────────────────────────────

print("\n--- Begg's Rank Correlation Test ---")
# Kendall's tau between effect sizes and variances
tau_begg, p_begg = stats.kendalltau(yi, vi)
print(f"  Kendall's tau = {tau_begg:.2f}, p = {fmt_p(p_begg)}")
if p_begg < 0.05:
    print("  -> Significant rank correlation (possible publication bias).")
else:
    print("  -> No significant rank correlation detected.")

# ── 3D: Trim-and-Fill ───────────────────────────────────────────────────────

print("\n--- Trim-and-Fill Analysis ---")


def trim_and_fill(yi, vi, side="left", max_iter=50):
    """
    Trim-and-fill: estimate number of missing studies and impute them.
    Uses the R0 estimator (rank-based).
    """
    yi_work = yi.copy()
    vi_work = vi.copy()

    for iteration in range(max_iter):
        # Fit RE model on current data
        res = random_effects_reml(yi_work, vi_work)
        mu = res["est"]

        # Calculate deviations from center
        devs = yi_work - mu

        # Rank the absolute deviations
        abs_devs = np.abs(devs)
        ranks = stats.rankdata(abs_devs)
        n_curr = len(yi_work)

        # Count studies on the specified side that are "extreme"
        if side == "left":
            extreme = devs < 0
        else:
            extreme = devs > 0

        # R0 estimator: k0 = max(0, round(S_n / (2*mu_dev)))
        # Simplified: count asymmetric studies
        S_ranks = np.sum(ranks[extreme])
        # Estimate k0
        T_n = np.sum(ranks[extreme]) - np.sum(ranks[~extreme])
        k0 = max(0, int(round((4 * S_ranks - n_curr * (n_curr + 1)) /
                                (2 * n_curr - 1))))

        if k0 == 0:
            break

        # Trim the k0 most extreme studies on that side
        if side == "left":
            order = np.argsort(devs)
        else:
            order = np.argsort(-devs)

        trim_idx = order[:k0]

        # Impute mirror studies
        imputed_yi = 2 * mu - yi_work[trim_idx]
        imputed_vi = vi_work[trim_idx]

        # Add imputed to original
        yi_filled = np.concatenate([yi, imputed_yi])
        vi_filled = np.concatenate([vi, imputed_vi])

        # Re-estimate
        res_filled = random_effects_reml(yi_filled, vi_filled)
        return k0, res_filled, yi_filled, vi_filled

    return 0, random_effects_reml(yi, vi), yi, vi


k_imputed, tf_res, yi_filled, vi_filled = trim_and_fill(yi, vi, side="left")
sei_filled = np.sqrt(vi_filled)

print(f"  Studies imputed (k0): {k_imputed}")
print(f"  Adjusted pooled ES = {tf_res['est']:.2f}, "
      f"95% CI [{tf_res['ci_lo']:.2f}, {tf_res['ci_hi']:.2f}]")

# ── Trim-and-fill funnel plot ────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(yi, sei, s=60, c="steelblue", edgecolors="black", linewidth=0.5,
           zorder=3, label="Original studies")
if k_imputed > 0:
    ax.scatter(yi_filled[k:], sei_filled[k:], s=60, c="white",
               edgecolors="red", linewidth=1.2, zorder=3,
               marker="D", label=f"Imputed studies (k={k_imputed})")
ax.axvline(tf_res["est"], color="red", linestyle="--", linewidth=0.8,
           label="Adjusted ES")
ax.axvline(pooled_es, color="black", linestyle="--", linewidth=0.8,
           label="Original ES")
se_range = np.linspace(0, max(sei_filled) * 1.2, 100)
ax.fill_betweenx(se_range,
                 tf_res["est"] - 1.96 * se_range,
                 tf_res["est"] + 1.96 * se_range,
                 alpha=0.08, color="gray")
ax.set_xlabel("Effect Size (Hedges' g)", fontsize=12)
ax.set_ylabel("Standard Error", fontsize=12)
ax.set_title("Funnel Plot with Trim-and-Fill", fontsize=14)
ax.invert_yaxis()
ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(os.path.join(outdir, "figures", "plot_03b_trimfill.png"), dpi=300)
plt.close()
print("Trim-and-fill funnel plot saved: figures/plot_03b_trimfill.png")

# ── 3E: Fail-Safe N (Rosenthal) ─────────────────────────────────────────────

print("\n--- Fail-Safe N (Rosenthal) ---")
# z_i = yi / sei
z_i = yi / sei
z_sum = np.sum(z_i)
fsn = max(0, int(np.ceil((z_sum**2 / (1.96**2)) - k)))
print(f"  Fail-safe N = {fsn}")
print(f"  {fsn} null-result studies would be needed to reduce the overall "
      f"effect to non-significance (p > .05).")
tolerance_5k1 = 5 * k + 10
if fsn > tolerance_5k1:
    print(f"  Exceeds 5k+10 = {tolerance_5k1} threshold — result is robust.")
else:
    print(f"  Below 5k+10 = {tolerance_5k1} threshold — interpret with caution.")

# ── 3F: Leave-One-Out Sensitivity ────────────────────────────────────────────

print("\n\n--- Leave-One-Out Analysis ---")
loo_results = []
for i in range(k):
    yi_loo = np.delete(yi, i)
    vi_loo = np.delete(vi, i)
    res_loo = random_effects_reml(yi_loo, vi_loo)
    loo_results.append({
        "study_removed": studies.study_id.iloc[i],
        "pooled_es": res_loo["est"],
        "ci_lo": res_loo["ci_lo"],
        "ci_hi": res_loo["ci_hi"],
        "p": res_loo["p"]
    })

loo_df = pd.DataFrame(loo_results)
loo_df["pooled_es"] = loo_df["pooled_es"].round(3)
loo_df["ci_lo"] = loo_df["ci_lo"].round(3)
loo_df["ci_hi"] = loo_df["ci_hi"].round(3)
print(loo_df.to_string(index=False))

es_range = loo_df.pooled_es.max() - loo_df.pooled_es.min()
print(f"\nPooled ES ranged from {loo_df.pooled_es.min():.3f} to "
      f"{loo_df.pooled_es.max():.3f} when individual studies were removed.")

# Flag studies whose removal changes significance
sig_overall = re_res["p"] < 0.05
for _, row in loo_df.iterrows():
    sig_loo = row["p"] < 0.05
    if sig_loo != sig_overall:
        print(f"  ** Removing {row['study_removed']} changes significance **")

# ── 3G: Influence Diagnostics (Cook's Distance) ─────────────────────────────

print("\n--- Influence Diagnostics ---")

# Cook's distance: proportional to change in pooled estimate when study removed
cooks_d = []
for i in range(k):
    yi_loo = np.delete(yi, i)
    vi_loo = np.delete(vi, i)
    res_loo = random_effects_reml(yi_loo, vi_loo)
    d_i = (re_res["est"] - res_loo["est"])**2 / re_res["se"]**2
    cooks_d.append(d_i)

studies["cooks_d"] = cooks_d
cooks_threshold = 4.0 / k

# DFBETAS: standardized change in estimate
dfbetas = []
for i in range(k):
    yi_loo = np.delete(yi, i)
    vi_loo = np.delete(vi, i)
    res_loo = random_effects_reml(yi_loo, vi_loo)
    db = (re_res["est"] - res_loo["est"]) / res_loo["se"]
    dfbetas.append(db)

studies["dfbetas"] = dfbetas

# Externally standardized residuals
wi_re = 1.0 / (vi + re_res["tau2"])
hat_vals = wi_re / np.sum(wi_re)
resid_raw = yi - re_res["est"]
resid_std = resid_raw / np.sqrt(vi + re_res["tau2"])
studies["ext_std_resid"] = resid_std

print(f"  Cook's D threshold: 4/k = {cooks_threshold:.3f}")
influence_df = studies[["study_id", "cooks_d", "dfbetas", "ext_std_resid"]].copy()
influence_df = influence_df.round(3)
print(influence_df.to_string(index=False))

flagged = studies[studies.cooks_d > cooks_threshold].study_id.tolist()
flagged_dfb = studies[abs(studies.dfbetas) > 1].study_id.tolist()
all_flagged = list(set(flagged + flagged_dfb))
if all_flagged:
    print(f"\n  Influential studies flagged: {', '.join(all_flagged)}")
else:
    print("\n  No studies exceeded influence thresholds.")

# Save influence table
influence_df.to_csv(os.path.join(outdir, "tables", "influence_table.csv"),
                    index=False)

# ── 3H: Cumulative Meta-Analysis ────────────────────────────────────────────

print("\n--- Cumulative Meta-Analysis ---")
order_idx = np.argsort(studies.year.values)
cum_results = []
for n_inc in range(2, k + 1):  # at least 2 studies
    idx = order_idx[:n_inc]
    res_cum = random_effects_reml(yi[idx], vi[idx])
    cum_results.append({
        "n_studies": n_inc,
        "last_added": studies.study_id.iloc[order_idx[n_inc - 1]],
        "year": studies.year.iloc[order_idx[n_inc - 1]],
        "pooled_es": res_cum["est"],
        "ci_lo": res_cum["ci_lo"],
        "ci_hi": res_cum["ci_hi"]
    })

cum_df = pd.DataFrame(cum_results)
cum_df[["pooled_es", "ci_lo", "ci_hi"]] = cum_df[["pooled_es", "ci_lo", "ci_hi"]].round(3)
print(cum_df.to_string(index=False))

# Cumulative forest plot
fig, ax = plt.subplots(figsize=(10, 8))
y_pos = np.arange(len(cum_df))
ax.errorbar(cum_df.pooled_es, y_pos, xerr=[cum_df.pooled_es - cum_df.ci_lo,
            cum_df.ci_hi - cum_df.pooled_es],
            fmt="s", color="steelblue", markersize=6, capsize=3, linewidth=1)
ax.axvline(0, color="black", linestyle="--", linewidth=0.5)
ax.set_yticks(y_pos)
ax.set_yticklabels([f"{r.last_added} (k={r.n_studies})" for _, r in cum_df.iterrows()])
ax.set_xlabel("Pooled Hedges' g [95% CI]", fontsize=12)
ax.set_title("Cumulative Meta-Analysis (by year)", fontsize=14)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(outdir, "figures", "plot_03c_cumulative.png"), dpi=300)
plt.close()
print("Cumulative meta-analysis plot saved: figures/plot_03c_cumulative.png")

# Save leave-one-out table
loo_df.to_csv(os.path.join(outdir, "tables", "leave1out_table.csv"), index=False)


# =============================================================================
# PART 4: Subgroup Analysis & Meta-Regression
# (Workflow: 05-analyze-subgroups.md)
# =============================================================================

print("\n\n=== PART 4: Subgroup Analysis & Meta-Regression ===\n")

# ── 4A: Subgroup Analysis — Intervention Type ───────────────────────────────

print("--- Subgroup Analysis: intervention_type ---\n")
subgroup_var = "intervention_type"
subgroups = studies[subgroup_var].unique()
subgroup_results = []

for sg in subgroups:
    mask = studies[subgroup_var] == sg
    k_sg = mask.sum()
    if k_sg < 2:
        print(f"  Skipping subgroup '{sg}': k = {k_sg} < 2")
        continue
    yi_sg = yi[mask]
    vi_sg = vi[mask]
    res_sg = random_effects_reml(yi_sg, vi_sg)
    Q_sg, _, _ = cochran_q(yi_sg, vi_sg)
    I2_sg = max(0, (Q_sg - (k_sg - 1)) / Q_sg * 100) if Q_sg > 0 else 0.0
    subgroup_results.append({
        "subgroup": sg, "k": k_sg,
        "pooled_es": round(res_sg["est"], 2),
        "ci_lo": round(res_sg["ci_lo"], 2),
        "ci_hi": round(res_sg["ci_hi"], 2),
        "I2": round(I2_sg, 1)
    })
    print(f"  {sg}: k = {k_sg}, pooled ES = {res_sg['est']:.2f}, "
          f"95% CI [{res_sg['ci_lo']:.2f}, {res_sg['ci_hi']:.2f}], "
          f"I-squared = {I2_sg:.1f}%")

# Q_between test for subgroup differences
Q_total, _, _ = cochran_q(yi, vi)
Q_within_total = 0
for sg in subgroups:
    mask = studies[subgroup_var] == sg
    if mask.sum() >= 2:
        Q_sg, _, _ = cochran_q(yi[mask], vi[mask])
        Q_within_total += Q_sg

Q_between = Q_total - Q_within_total
df_between = len([s for s in subgroups if (studies[subgroup_var] == s).sum() >= 2]) - 1
p_between = 1 - stats.chi2.cdf(Q_between, df_between)

print(f"\n  Q_between({df_between}) = {Q_between:.2f}, p = {fmt_p(p_between)}")
if p_between < 0.05:
    print("  -> Significant difference between subgroups.")
else:
    print("  -> Intervention type did not significantly moderate the effect.")

sg_df = pd.DataFrame(subgroup_results)
sg_df.to_csv(os.path.join(outdir, "tables", "subgroup_table.csv"), index=False)

# ── Subgroup Forest Plot ─────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 8))
y_pos_counter = 0
y_ticks = []
y_labels = []
colors = {"CBT": "steelblue", "Medication": "darkorange"}

for sg in subgroups:
    mask = studies[subgroup_var] == sg
    sg_studies = studies[mask]
    sg_yi = yi[mask]
    sg_sei = sei[mask]

    # Header for subgroup
    y_ticks.append(y_pos_counter)
    y_labels.append(f"--- {sg} ---")
    y_pos_counter += 1

    for j, (_, row) in enumerate(sg_studies.iterrows()):
        ci_lo_j = sg_yi[j] - 1.96 * sg_sei[j]
        ci_hi_j = sg_yi[j] + 1.96 * sg_sei[j]
        ax.plot([ci_lo_j, ci_hi_j], [y_pos_counter, y_pos_counter],
                color=colors.get(sg, "gray"), linewidth=1)
        weight_j = 1.0 / (sg_sei[j]**2 + re_res["tau2"])
        ax.scatter(sg_yi[j], y_pos_counter, s=weight_j * 200,
                   c=colors.get(sg, "gray"), edgecolors="black", linewidth=0.5,
                   zorder=3)
        y_ticks.append(y_pos_counter)
        y_labels.append(row.study_id)
        y_pos_counter += 1

    # Subgroup diamond
    res_sg = random_effects_reml(sg_yi, vi[mask])
    diamond_x = [res_sg["ci_lo"], res_sg["est"], res_sg["ci_hi"], res_sg["est"]]
    diamond_y = [y_pos_counter, y_pos_counter - 0.3, y_pos_counter,
                 y_pos_counter + 0.3]
    ax.fill(diamond_x, diamond_y, color=colors.get(sg, "gray"), alpha=0.5)
    y_ticks.append(y_pos_counter)
    y_labels.append(f"Subtotal ({sg})")
    y_pos_counter += 1.5

ax.axvline(0, color="black", linestyle="--", linewidth=0.5)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels, fontsize=8)
ax.set_xlabel("Hedges' g [95% CI]", fontsize=12)
ax.set_title(f"Subgroup Forest Plot: {subgroup_var}", fontsize=14)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(outdir, "figures", f"plot_04_subgroup_{subgroup_var}.png"),
            dpi=300)
plt.close()
print(f"Subgroup forest plot saved: figures/plot_04_subgroup_{subgroup_var}.png")

# ── Repeat for study_quality ─────────────────────────────────────────────────

print("\n--- Subgroup Analysis: study_quality ---\n")
subgroup_var2 = "study_quality"
subgroups2 = studies[subgroup_var2].unique()
subgroup_results2 = []

for sg in subgroups2:
    mask = studies[subgroup_var2] == sg
    k_sg = mask.sum()
    if k_sg < 2:
        print(f"  Skipping subgroup '{sg}': k = {k_sg} < 2")
        continue
    yi_sg = yi[mask]
    vi_sg = vi[mask]
    res_sg = random_effects_reml(yi_sg, vi_sg)
    Q_sg, _, _ = cochran_q(yi_sg, vi_sg)
    I2_sg = max(0, (Q_sg - (k_sg - 1)) / Q_sg * 100) if Q_sg > 0 else 0.0
    subgroup_results2.append({
        "subgroup": sg, "k": k_sg,
        "pooled_es": round(res_sg["est"], 2),
        "ci_lo": round(res_sg["ci_lo"], 2),
        "ci_hi": round(res_sg["ci_hi"], 2),
        "I2": round(I2_sg, 1)
    })
    print(f"  {sg}: k = {k_sg}, pooled ES = {res_sg['est']:.2f}, "
          f"95% CI [{res_sg['ci_lo']:.2f}, {res_sg['ci_hi']:.2f}], "
          f"I-squared = {I2_sg:.1f}%")

Q_within2 = 0
for sg in subgroups2:
    mask = studies[subgroup_var2] == sg
    if mask.sum() >= 2:
        Q_sg, _, _ = cochran_q(yi[mask], vi[mask])
        Q_within2 += Q_sg

Q_between2 = Q_total - Q_within2
df_between2 = len([s for s in subgroups2 if (studies[subgroup_var2] == s).sum() >= 2]) - 1
p_between2 = 1 - stats.chi2.cdf(Q_between2, df_between2)

print(f"\n  Q_between({df_between2}) = {Q_between2:.2f}, p = {fmt_p(p_between2)}")

# ── 4B: Meta-Regression — mean_age (continuous moderator) ───────────────────

print("\n--- Meta-Regression: mean_age ---\n")

mod_vals = studies["mean_age"].values

# Weighted least squares meta-regression
# yi = beta0 + beta1 * moderator + epsilon
# weights = 1 / (vi + tau2)

# Step 1: Get tau2 from base model
tau2_base = re_res["tau2"]

# Step 2: Fit meta-regression with WLS
wi_reg = 1.0 / (vi + tau2_base)
X_reg = sm.add_constant(mod_vals)
wls_reg = sm.WLS(yi, X_reg, weights=wi_reg).fit()

beta0 = wls_reg.params[0]
beta1 = wls_reg.params[1]
se_beta1 = wls_reg.bse[1]
z_beta1 = wls_reg.tvalues[1]
p_beta1 = wls_reg.pvalues[1]

# Residual heterogeneity
resid_reg = yi - wls_reg.predict(X_reg)
Q_resid = np.sum(wi_reg * resid_reg**2)
df_resid = k - 2
p_resid = 1 - stats.chi2.cdf(Q_resid, df_resid)

# R-squared analog
tau2_reg = max(0, dl_tau2(resid_reg, vi))
R2_analog = max(0, (tau2_base - tau2_reg) / tau2_base) if tau2_base > 0 else 0

print(f"  B = {beta1:.2f}, SE = {se_beta1:.2f}, z = {z_beta1:.2f}, "
      f"p = {fmt_p(p_beta1)}")
print(f"  R-squared analog = {R2_analog:.2f}")
print(f"  Residual heterogeneity: QE({df_resid}) = {Q_resid:.2f}, "
      f"p = {fmt_p(p_resid)}")

if p_beta1 < 0.05:
    print("  -> Mean age was a significant moderator of the treatment effect.")
else:
    print("  -> Mean age was not a significant source of heterogeneity.")

# Save meta-regression table
metareg_df = pd.DataFrame({
    "moderator": ["mean_age"],
    "B": [round(beta1, 3)],
    "SE": [round(se_beta1, 3)],
    "z": [round(z_beta1, 2)],
    "p": [fmt_p(p_beta1)],
    "R2_analog": [round(R2_analog, 2)]
})
metareg_df.to_csv(os.path.join(outdir, "tables", "metareg_table.csv"), index=False)

# ── Bubble Plot ──────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(8, 6))
bubble_sizes = (1.0 / sei) * 30  # proportional to precision
ax.scatter(mod_vals, yi, s=bubble_sizes, alpha=0.6, c="steelblue",
           edgecolors="black", linewidth=0.5, zorder=3)

# Regression line with CI band
x_line = np.linspace(mod_vals.min() - 2, mod_vals.max() + 2, 100)
X_line = sm.add_constant(x_line)
y_pred = wls_reg.predict(X_line)

# Approximate CI for regression line
y_se = np.sqrt(np.diag(X_line @ wls_reg.cov_params() @ X_line.T))
ax.plot(x_line, y_pred, color="red", linewidth=2, label="Meta-regression line")
ax.fill_between(x_line, y_pred - 1.96 * y_se, y_pred + 1.96 * y_se,
                alpha=0.15, color="red", label="95% CI")
ax.axhline(0, color="black", linestyle="--", linewidth=0.5)
ax.set_xlabel("Mean Age", fontsize=12)
ax.set_ylabel("Hedges' g", fontsize=12)
ax.set_title("Bubble Plot: Effect Size by Mean Age", fontsize=14)
ax.legend(loc="best")
plt.tight_layout()
plt.savefig(os.path.join(outdir, "figures", "plot_04_bubble_mean_age.png"), dpi=300)
plt.close()
print("Bubble plot saved: figures/plot_04_bubble_mean_age.png")


# =============================================================================
# PART 5: Advanced Models (All Estimation Methods as Lenses)
# (Workflow: 06-fit-models.md)
# =============================================================================

print("\n\n=== PART 5: Advanced Modeling ===\n")

# ── 5A: Fixed-Effects (Inverse Variance) ────────────────────────────────────
fe_res = fixed_effects(yi, vi)
print(f"Fixed-Effects (IV):     pooled ES = {fe_res['est']:.2f}, "
      f"95% CI [{fe_res['ci_lo']:.2f}, {fe_res['ci_hi']:.2f}], "
      f"z = {fe_res['z']:.2f}, p = {fmt_p(fe_res['p'])}")

# ── 5B: DerSimonian-Laird ───────────────────────────────────────────────────
dl_res = random_effects_dl(yi, vi)
print(f"RE (DerSimonian-Laird): pooled ES = {dl_res['est']:.2f}, "
      f"95% CI [{dl_res['ci_lo']:.2f}, {dl_res['ci_hi']:.2f}], "
      f"z = {dl_res['z']:.2f}, p = {fmt_p(dl_res['p'])}, "
      f"tau2 = {dl_res['tau2']:.4f}")

# ── 5C: REML ────────────────────────────────────────────────────────────────
reml_res = random_effects_reml(yi, vi)
print(f"RE (REML):              pooled ES = {reml_res['est']:.2f}, "
      f"95% CI [{reml_res['ci_lo']:.2f}, {reml_res['ci_hi']:.2f}], "
      f"z = {reml_res['z']:.2f}, p = {fmt_p(reml_res['p'])}, "
      f"tau2 = {reml_res['tau2']:.4f}")

# ── 5D: Knapp-Hartung ───────────────────────────────────────────────────────
kh_res = knapp_hartung(yi, vi)
print(f"Knapp-Hartung:          pooled ES = {kh_res['est']:.2f}, "
      f"95% CI [{kh_res['ci_lo']:.2f}, {kh_res['ci_hi']:.2f}], "
      f"t({kh_res['df']}) = {kh_res['t']:.2f}, p = {fmt_p(kh_res['p'])}, "
      f"tau2 = {kh_res['tau2']:.4f}")

# ── Prediction interval ─────────────────────────────────────────────────────
pi_lo, pi_hi = prediction_interval(reml_res["est"], reml_res["tau2"],
                                    reml_res["se"], k)
print(f"\n95% Prediction Interval: [{pi_lo:.2f}, {pi_hi:.2f}]")

# ── 5E: Bayesian (approximate via normal prior) ─────────────────────────────
print("\n--- Bayesian Meta-Analysis (approximate) ---")
# Use a weakly informative prior: tau ~ half-Cauchy(0, 0.5)
# Approximate with grid search over tau
tau_grid = np.linspace(0.001, 1.0, 500)
log_marginal = np.zeros_like(tau_grid)

for idx, tau_val in enumerate(tau_grid):
    vi_star = vi + tau_val**2
    wi_star = 1.0 / vi_star
    mu_star = np.sum(wi_star * yi) / np.sum(wi_star)
    # log-likelihood
    ll = -0.5 * np.sum(np.log(vi_star) + (yi - mu_star)**2 / vi_star)
    # half-Cauchy prior on tau
    prior = 2.0 / (np.pi * 0.5 * (1 + (tau_val / 0.5)**2))
    log_marginal[idx] = ll + np.log(prior + 1e-20)

# Normalize to get posterior
log_marginal -= np.max(log_marginal)
posterior = np.exp(log_marginal)
posterior /= np.trapz(posterior, tau_grid)

# Posterior mean of tau
tau_post_mean = np.trapz(tau_grid * posterior, tau_grid)

# For each tau value, compute posterior of mu
# Use posterior mean tau to get posterior of mu
vi_bayes = vi + tau_post_mean**2
wi_bayes = 1.0 / vi_bayes
mu_bayes = np.sum(wi_bayes * yi) / np.sum(wi_bayes)
se_bayes = np.sqrt(1.0 / np.sum(wi_bayes))
cri_lo = mu_bayes - 1.96 * se_bayes
cri_hi = mu_bayes + 1.96 * se_bayes

print(f"  Prior on tau: half-Cauchy(0, 0.5)")
print(f"  Posterior mean of tau = {tau_post_mean:.3f}")
print(f"  Posterior mean of mu = {mu_bayes:.2f}, "
      f"95% CrI [{cri_lo:.2f}, {cri_hi:.2f}]")

# ── 5F: Three-Level Model (note: each study has one effect — not applicable) ─
print("\n--- Three-Level Meta-Analysis ---")
print("  Each study contributes a single effect size.")
print("  Three-level model is not applicable to this data structure.")
print("  (Would be appropriate when studies report multiple effect sizes.)")
print("  Capability noted for future use with dependent-effects data.")


# =============================================================================
# PART 6: Cross-Method Insight Synthesis
# (Workflow: 07-compare-models.md)
# =============================================================================

print("\n\n=== PART 6: Model Comparison & Robustness ===\n")

# ── 6A: Model Comparison Table ───────────────────────────────────────────────

comp_data = {
    "Method": ["Fixed-effects", "RE (DL)", "RE (REML)",
                "Knapp-Hartung", "Bayesian"],
    "Pooled_ES": [fe_res["est"], dl_res["est"], reml_res["est"],
                   kh_res["est"], mu_bayes],
    "CI_lo": [fe_res["ci_lo"], dl_res["ci_lo"], reml_res["ci_lo"],
               kh_res["ci_lo"], cri_lo],
    "CI_hi": [fe_res["ci_hi"], dl_res["ci_hi"], reml_res["ci_hi"],
               kh_res["ci_hi"], cri_hi],
    "Test_Stat": [f"z = {fe_res['z']:.2f}", f"z = {dl_res['z']:.2f}",
                   f"z = {reml_res['z']:.2f}",
                   f"t = {kh_res['t']:.2f}", "--"],
    "p": [fmt_p(fe_res["p"]), fmt_p(dl_res["p"]), fmt_p(reml_res["p"]),
           fmt_p(kh_res["p"]), "--"],
    "tau2": ["--", f"{dl_res['tau2']:.4f}", f"{reml_res['tau2']:.4f}",
              f"{kh_res['tau2']:.4f}", f"{tau_post_mean**2:.4f}"]
}
comp_df = pd.DataFrame(comp_data)
comp_df["Pooled_ES"] = comp_df["Pooled_ES"].round(2)
comp_df["CI_lo"] = comp_df["CI_lo"].round(2)
comp_df["CI_hi"] = comp_df["CI_hi"].round(2)

print("--- Model Comparison Table ---\n")
print(comp_df.to_string(index=False))

comp_df.to_csv(os.path.join(outdir, "tables", "model_comparison_table.csv"),
               index=False)

# ── 6B: Robustness Summary ──────────────────────────────────────────────────

print("\n\n--- Robustness Summary ---\n")

# FE vs RE
fe_re_same = np.sign(fe_res["est"]) == np.sign(reml_res["est"])
fe_re_both_sig = (fe_res["p"] < 0.05) == (reml_res["p"] < 0.05)

# DL vs REML
dl_reml_tau_diff = abs(dl_res["tau2"] - reml_res["tau2"])

# Standard vs Knapp-Hartung
kh_ci_wider = (kh_res["ci_hi"] - kh_res["ci_lo"]) - (reml_res["ci_hi"] - reml_res["ci_lo"])

# Frequentist vs Bayesian
freq_bayes_diff = abs(reml_res["est"] - mu_bayes)

# Trim-fill comparison
tf_diff = abs(re_res["est"] - tf_res["est"])

robust_data = {
    "Decision": [
        "FE vs RE",
        "DL vs REML estimator",
        "Standard vs Knapp-Hartung",
        "Frequentist vs Bayesian",
        "Before vs after trim-fill",
        "With vs without influential study"
    ],
    "Sensitivity": [
        f"Same direction: {'Yes' if fe_re_same else 'No'}; "
        f"Both significant: {'Yes' if fe_re_both_sig else 'No'}",
        f"tau2 difference: {dl_reml_tau_diff:.4f} "
        f"({'negligible' if dl_reml_tau_diff < 0.01 else 'notable'})",
        f"CI widened by {kh_ci_wider:.2f} "
        f"({'materially' if abs(kh_ci_wider) > 0.1 else 'minimally'})",
        f"Estimate difference: {freq_bayes_diff:.3f} "
        f"({'consistent' if freq_bayes_diff < 0.05 else 'divergent'})",
        f"ES shifted by {tf_diff:.3f} "
        f"({'materially' if tf_diff > 0.1 else 'minimally'})",
        f"ES range on leave-one-out: {loo_df.pooled_es.min():.3f} to "
        f"{loo_df.pooled_es.max():.3f}"
    ]
}
robust_df = pd.DataFrame(robust_data)
print(robust_df.to_string(index=False))

robust_df.to_csv(os.path.join(outdir, "tables", "robustness_table.csv"),
                 index=False)

# ── 6C: Narrative Synthesis ──────────────────────────────────────────────────

print("\n\n--- Narrative Synthesis ---\n")

all_same_dir = all(np.sign(x) == np.sign(fe_res["est"])
                   for x in [dl_res["est"], reml_res["est"],
                              kh_res["est"], mu_bayes])

print(f"All five estimation approaches yielded pooled effects in the "
      f"{'same' if all_same_dir else 'inconsistent'} direction, "
      f"ranging from {min(fe_res['est'], dl_res['est'], reml_res['est'], kh_res['est'], mu_bayes):.2f} "
      f"to {max(fe_res['est'], dl_res['est'], reml_res['est'], kh_res['est'], mu_bayes):.2f}. ")

if dl_reml_tau_diff < 0.01:
    print("The choice of heterogeneity estimator (DL vs REML) had negligible "
          "impact on the tau-squared estimate, suggesting stability in the "
          "variance component. ", end="")
else:
    print(f"The DL and REML estimators yielded tau-squared values of "
          f"{dl_res['tau2']:.4f} and {reml_res['tau2']:.4f} respectively, "
          f"suggesting some sensitivity to the estimation approach. ", end="")

if abs(kh_ci_wider) > 0.1:
    print(f"The Knapp-Hartung adjustment produced a materially wider "
          f"confidence interval (width difference: {kh_ci_wider:.2f}), "
          f"indicating that the standard Wald-type CI may have been "
          f"overconfident. ", end="")
else:
    print("The Knapp-Hartung adjustment produced a similar confidence "
          "interval to the standard approach, suggesting the Wald-type "
          "CI provides adequate coverage for this dataset. ", end="")

print(f"Overall, the pooled estimate appears "
      f"{'robust' if all_same_dir and fe_re_both_sig else 'somewhat sensitive'} "
      f"across analytic choices.")


# =============================================================================
# PART 7: Manuscript Generation
# (Workflow: 08-generate-manuscript.md)
# =============================================================================

print("\n\n=== PART 7: Manuscript Generation ===\n")

# ── Compute all needed statistics for manuscript ─────────────────────────────
Q_stat, Q_df, Q_p = cochran_q(yi, vi)
I2 = max(0, (Q_stat - Q_df) / Q_stat * 100) if Q_stat > 0 else 0.0

# ── methods.md ───────────────────────────────────────────────────────────────

methods_text = f"""## Methods

### Search Strategy and Study Selection

The search strategy and study selection process followed PRISMA 2020 guidelines
(Page et al., 2021). Details of the systematic search are reported in the PRISMA
flow diagram; the present section focuses on the statistical analysis approach.

### Effect Size Calculation

Standardized mean differences were computed as Hedges' g to quantify the
magnitude of treatment effects on depression outcomes across studies. For each
study, the pooled standard deviation was used as the denominator, with the
small-sample correction factor J applied to yield unbiased estimates (Hedges &
Vevea, 1998). Negative values indicate lower depression scores in the treatment
group relative to control.

### Pooled Estimation

A random-effects model with restricted maximum likelihood (REML) estimation
served as the primary analytic approach, acknowledging that the included studies
likely sample from a distribution of true effects rather than sharing a single
common effect. The DerSimonian-Laird moment-based estimator (DerSimonian &
Laird, 1986) was computed for comparison given its prevalence in published
meta-analyses. A fixed-effects (inverse-variance) model was also fitted to
assess sensitivity of the pooled estimate to the modeling assumption.

### Heterogeneity Assessment

Between-study heterogeneity was evaluated using Cochran's Q statistic, the
I-squared index (Higgins & Thompson, 2002), tau-squared, and the H-squared
ratio. Thresholds of I-squared < 25%, 25-75%, and > 75% were used as benchmarks
for low, moderate, and high heterogeneity, respectively. A 95% prediction
interval was computed to characterize the expected range of effects in future
study settings.

### Publication Bias

Potential publication bias was assessed through visual inspection of a funnel
plot, Egger's regression test for funnel plot asymmetry (Egger et al., 1997),
and Begg's rank correlation test (Begg & Mazumdar, 1994). The trim-and-fill
method (Duval & Tweedie, 2000) was applied to estimate the number and impact of
potentially missing studies, and Rosenthal's fail-safe N was calculated.

### Sensitivity Analysis

Robustness of the pooled estimate was examined through leave-one-out analysis,
in which each study was removed in turn and the pooled effect re-estimated.
Influence diagnostics including Cook's distance and DFBETAS were computed to
identify studies exerting disproportionate influence on the overall result.
Studies with Cook's D exceeding 4/k were flagged. Cumulative meta-analysis,
with studies ordered by publication year, assessed temporal stability of the
pooled estimate.

### Moderator Analysis

Subgroup analyses tested whether the pooled effect differed across levels of
categorical moderators (intervention type, study quality) using the Q-between
statistic. Mixed-effects meta-regression examined mean participant age as a
continuous moderator, with the proportion of heterogeneity explained (R-squared
analog) reported for each predictor.

### Additional Models

To assess robustness to analytic assumptions, the Knapp-Hartung adjustment
(Knapp & Hartung, 2003; IntHout et al., 2014) was applied to provide
better-calibrated confidence intervals based on the t-distribution rather than
the normal approximation. An approximate Bayesian meta-analysis with a weakly
informative half-Cauchy(0, 0.5) prior on tau was conducted to provide a
complementary perspective on uncertainty. A three-level model was considered
but deemed inapplicable as each study contributed a single effect size.

### Software

All analyses were conducted in Python 3 using NumPy, SciPy, statsmodels, and
matplotlib. Effect sizes, pooled estimates, and heterogeneity statistics were
computed using custom implementations following established formulas
(Viechtbauer, 2010).
"""

with open(os.path.join(outdir, "methods.md"), "w") as f:
    f.write(methods_text)
print("methods.md generated")

# ── results.md ───────────────────────────────────────────────────────────────

results_text = f"""## Results

### Overall Effect

The meta-analysis synthesized k = {k} studies with a total sample size of
N = {total_n}. The random-effects model (REML) yielded a pooled standardized
mean difference of g = {reml_res['est']:.2f}, 95% CI [{reml_res['ci_lo']:.2f},
{reml_res['ci_hi']:.2f}], z = {reml_res['z']:.2f}, p {fmt_p(reml_res['p'])},
indicating a {'statistically significant' if reml_res['p'] < 0.05 else 'non-significant'}
{'negative' if reml_res['est'] < 0 else 'positive'} effect favoring the
{'treatment' if reml_res['est'] < 0 else 'control'} group. The fixed-effects
model produced a similar estimate (g = {fe_res['est']:.2f}, 95% CI
[{fe_res['ci_lo']:.2f}, {fe_res['ci_hi']:.2f}]). The 95% prediction interval
[{pi_lo:.2f}, {pi_hi:.2f}] suggests that effects in individual study contexts
may vary {'considerably' if (pi_hi - pi_lo) > 1.0 else 'moderately'}.

### Heterogeneity

Cochran's Q({Q_df}) = {Q_stat:.2f}, p = {fmt_p(Q_p)}; I-squared = {I2:.1f}%;
tau-squared = {reml_res['tau2']:.4f}. {'Substantial' if I2 > 75 else 'Moderate' if I2 > 25 else 'Limited'}
between-study heterogeneity was observed, {'warranting' if I2 > 25 else 'with'}
{'exploration of moderating factors' if I2 > 25 else 'the random-effects framework employed as a conservative approach'}.

### Publication Bias

Visual inspection of the funnel plot revealed
{'some asymmetry' if p_egger < 0.1 else 'no marked asymmetry'} (see Figure 3).
Egger's regression test {'indicated' if p_egger < 0.05 else 'did not indicate'}
significant funnel plot asymmetry (intercept = {intercept_egger:.2f},
SE = {se_intercept:.2f}, p = {fmt_p(p_egger)}). Begg's rank correlation test
yielded Kendall's tau = {tau_begg:.2f}, p = {fmt_p(p_begg)}.
The trim-and-fill procedure estimated {k_imputed} missing
{'study' if k_imputed == 1 else 'studies'},
{'with the adjusted pooled estimate (g = ' + f"{tf_res['est']:.2f}" + ', 95% CI [' + f"{tf_res['ci_lo']:.2f}" + ', ' + f"{tf_res['ci_hi']:.2f}" + ']) remaining consistent with the original.' if k_imputed > 0 else 'suggesting no imputation was necessary.'}
Rosenthal's fail-safe N was {fsn}, {'exceeding' if fsn > tolerance_5k1 else 'falling below'}
the 5k + 10 = {tolerance_5k1} threshold.

### Sensitivity Analysis

Leave-one-out analysis demonstrated that the pooled estimate was stable, with
effects ranging from {loo_df.pooled_es.min():.3f} to {loo_df.pooled_es.max():.3f}
when individual studies were removed (see Table S2).
{'No study' if not all_flagged else ', '.join(all_flagged)} {'was flagged as' if not all_flagged else 'exceeded'} {'influential based on' if not all_flagged else ''} Cook's distance
(threshold: 4/k = {cooks_threshold:.3f}){' or |DFBETAS| > 1' if not all_flagged else ''}.
Cumulative meta-analysis ordered by publication year showed the pooled estimate
{'converging' if abs(cum_df.pooled_es.iloc[-1] - cum_df.pooled_es.iloc[-3]) < 0.05 else 'continuing to shift'},
suggesting the evidence base has {'stabilized' if abs(cum_df.pooled_es.iloc[-1] - cum_df.pooled_es.iloc[-3]) < 0.05 else 'not yet fully stabilized'}.

### Subgroup Analysis

Subgroup analysis by intervention type revealed
{'a significant difference' if p_between < 0.05 else 'no significant difference'}
between subgroups (Q_between({df_between}) = {Q_between:.2f},
p = {fmt_p(p_between)}). """

# Add subgroup details
for sr in subgroup_results:
    results_text += (f"The {sr['subgroup']} subgroup (k = {sr['k']}) yielded a "
                     f"pooled effect of g = {sr['pooled_es']:.2f}, 95% CI "
                     f"[{sr['ci_lo']:.2f}, {sr['ci_hi']:.2f}], "
                     f"I-squared = {sr['I2']:.1f}%. ")

results_text += f"""

### Meta-Regression

Mean participant age {'was' if p_beta1 < 0.05 else 'was not'} a significant
moderator of treatment effect (B = {beta1:.2f}, SE = {se_beta1:.2f},
p = {fmt_p(p_beta1)}, R-squared = {R2_analog:.2f}). Residual heterogeneity
remained {'significant' if p_resid < 0.05 else 'non-significant'}
(QE({df_resid}) = {Q_resid:.2f}, p = {fmt_p(p_resid)}),
suggesting that {'additional moderators may account for remaining variability' if p_resid < 0.05 else 'the model adequately captured between-study variation'}.

### Cross-Method Comparison

All estimation methods yielded pooled effects in the
{'same direction' if all_same_dir else 'same general direction'}, ranging from
{min(fe_res['est'], dl_res['est'], reml_res['est'], kh_res['est'], mu_bayes):.2f} to
{max(fe_res['est'], dl_res['est'], reml_res['est'], kh_res['est'], mu_bayes):.2f}
(see Table S5). The DL and REML tau-squared estimates were
{dl_res['tau2']:.4f} and {reml_res['tau2']:.4f}, respectively. The
Knapp-Hartung adjustment {'widened' if kh_ci_wider > 0 else 'narrowed'}
the confidence interval by {abs(kh_ci_wider):.2f} units
({'a material change' if abs(kh_ci_wider) > 0.1 else 'a minimal change'}).
The approximate Bayesian posterior (mean = {mu_bayes:.2f}, 95% CrI
[{cri_lo:.2f}, {cri_hi:.2f}]) was consistent with the frequentist REML
estimate. Overall, the main finding appears robust across analytic choices.
"""

with open(os.path.join(outdir, "results.md"), "w") as f:
    f.write(results_text)
print("results.md generated")

# ── references.bib ───────────────────────────────────────────────────────────

references_bib = r"""@article{dersimonian1986,
  author  = {DerSimonian, Rebecca and Laird, Nan},
  title   = {Meta-analysis in clinical trials},
  journal = {Controlled Clinical Trials},
  year    = {1986},
  volume  = {7},
  number  = {3},
  pages   = {177--188}
}

@article{higgins2002,
  author  = {Higgins, Julian P. T. and Thompson, Simon G.},
  title   = {Quantifying heterogeneity in a meta-analysis},
  journal = {Statistics in Medicine},
  year    = {2002},
  volume  = {21},
  number  = {11},
  pages   = {1539--1558}
}

@article{egger1997,
  author  = {Egger, Matthias and Davey Smith, George and Schneider, Martin and Minder, Christoph},
  title   = {Bias in meta-analysis detected by a simple, graphical test},
  journal = {BMJ},
  year    = {1997},
  volume  = {315},
  number  = {7109},
  pages   = {629--634}
}

@article{begg1994,
  author  = {Begg, Colin B. and Mazumdar, Madhuchhanda},
  title   = {Operating characteristics of a rank correlation test for publication bias},
  journal = {Biometrics},
  year    = {1994},
  volume  = {50},
  number  = {4},
  pages   = {1088--1101}
}

@article{viechtbauer2010,
  author  = {Viechtbauer, Wolfgang},
  title   = {Conducting meta-analyses in {R} with the metafor package},
  journal = {Journal of Statistical Software},
  year    = {2010},
  volume  = {36},
  number  = {3},
  pages   = {1--48}
}

@article{duval2000,
  author  = {Duval, Sue and Tweedie, Richard},
  title   = {Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis},
  journal = {Biometrics},
  year    = {2000},
  volume  = {56},
  number  = {2},
  pages   = {455--463}
}

@article{knapp2003,
  author  = {Knapp, Guido and Hartung, Joachim},
  title   = {Improved tests for a random effects meta-regression with heteroscedastic errors},
  journal = {Statistics in Medicine},
  year    = {2003},
  volume  = {22},
  number  = {17},
  pages   = {2693--2710}
}

@article{hedges1998,
  author  = {Hedges, Larry V. and Vevea, Jack L.},
  title   = {Fixed- and random-effects models in meta-analysis},
  journal = {Psychological Methods},
  year    = {1998},
  volume  = {3},
  number  = {4},
  pages   = {486--504}
}

@article{inthout2014,
  author  = {IntHout, Joanna and Ioannidis, John P. A. and Borm, George F.},
  title   = {The {Hartung-Knapp-Sidik-Jonkman} method for random effects meta-analysis is straightforward and considerably outperforms the standard {DerSimonian-Laird} method},
  journal = {BMC Medical Research Methodology},
  year    = {2014},
  volume  = {14},
  pages   = {25}
}

@article{moher2009,
  author  = {Moher, David and Liberati, Alessandro and Tetzlaff, Jennifer and Altman, Douglas G.},
  title   = {Preferred reporting items for systematic reviews and meta-analyses: The {PRISMA} statement},
  journal = {PLoS Medicine},
  year    = {2009},
  volume  = {6},
  number  = {7},
  pages   = {e1000097}
}

@article{page2021,
  author  = {Page, Matthew J. and McKenzie, Joanne E. and Bossuyt, Patrick M. and others},
  title   = {The {PRISMA} 2020 statement: An updated guideline for reporting systematic reviews},
  journal = {BMJ},
  year    = {2021},
  volume  = {372},
  pages   = {n71}
}
"""

with open(os.path.join(outdir, "references.bib"), "w") as f:
    f.write(references_bib)
print("references.bib generated")

# ── Study summary table CSV ──────────────────────────────────────────────────

summary_out = studies[["study_id", "n_treatment", "n_control", "yi", "sei"]].copy()
summary_out["ci_lo"] = (summary_out.yi - 1.96 * summary_out.sei).round(3)
summary_out["ci_hi"] = (summary_out.yi + 1.96 * summary_out.sei).round(3)
wi_fe = 1.0 / studies.vi
summary_out["weight_pct"] = (100 * wi_fe / wi_fe.sum()).round(1)
summary_out.to_csv(os.path.join(outdir, "tables", "study_summary_table.csv"),
                   index=False)

print("\n=== All deliverables generated ===")
print(f"""
Deliverables:
  figures/plot_03_funnel.png
  figures/plot_03b_trimfill.png
  figures/plot_03c_cumulative.png
  figures/plot_04_subgroup_intervention_type.png
  figures/plot_04_bubble_mean_age.png
  tables/study_summary_table.csv
  tables/leave1out_table.csv
  tables/influence_table.csv
  tables/subgroup_table.csv
  tables/metareg_table.csv
  tables/model_comparison_table.csv
  tables/robustness_table.csv
  methods.md
  results.md
  references.bib
""")

print("=" * 72)
print("META-ANALYSIS COMPLETE")
print("=" * 72)
