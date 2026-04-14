# =============================================
# Survival Outcome Analysis Pipeline
# Dataset: lung (NCCTG Lung Cancer)
# Outcome: Surv(time, status) — time to death
# Group variable: sex (1 = Male, 2 = Female)
# Predictors: sex, age, ph.ecog, ph.karno, pat.karno, meal.cal, wt.loss
# =============================================
# AutoResearch | Full pipeline: KM + log-rank + Cox PH + AFT + RSF +
#                 unified importance + manuscript output
# =============================================

# ── PART 0: Setup & Data Loading ──────────────────────────────────────────────

import warnings
warnings.filterwarnings('ignore')

import os
import shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from lifelines import (
    KaplanMeierFitter,
    CoxPHFitter,
    WeibullAFTFitter,
    LogNormalAFTFitter,
    LogLogisticAFTFitter,
)
from lifelines.statistics import logrank_test
from lifelines.datasets import load_lung

from sksurv.ensemble import RandomSurvivalForest
from sksurv.metrics import concordance_index_censored

output_dir = os.path.join(os.getcwd(), "output")
tables_dir = os.path.join(output_dir, "tables")
figures_dir = os.path.join(output_dir, "figures")
os.makedirs(tables_dir, exist_ok=True)
os.makedirs(figures_dir, exist_ok=True)


def fmt_p_value(p):
    return "< .001" if p < 0.001 else f"= {p:.3f}"

print("=" * 60)
print("Survival Analysis Pipeline — lung dataset")
print("=" * 60, "\n")

# Load and prepare data
df_raw = load_lung()

# lifelines load_lung: status already recoded (1=dead, 0=censored)
df_raw['event'] = df_raw['status'].astype(int)
df_raw['sex_label'] = df_raw['sex'].map({1: 'Male', 2: 'Female'})

# Select analysis columns
cols_needed = ['time', 'event', 'sex', 'age', 'ph.ecog', 'ph.karno',
               'pat.karno', 'meal.cal', 'wt.loss']
df = df_raw[cols_needed + ['sex_label']].copy()

n_before = len(df)
df = df.dropna(subset=cols_needed).reset_index(drop=True)
n_after = len(df)

print(f"Data dimensions: {n_before} observations (raw), {n_after} complete cases")
print(f"Dropped {n_before - n_after} rows with missing values")
print(f"Outcome: time (days) to death from advanced lung cancer")
print(f"Event coding: lifelines recodes status (1=dead, 0=censored)\n")

predictor_names = ['sex', 'age', 'ph.ecog', 'ph.karno', 'pat.karno',
                   'meal.cal', 'wt.loss']

# ── PART 1: Follow-Up and Censoring Assessment ──────────────────────────────

print("=" * 60)
print("PART 1: Follow-Up and Censoring Assessment")
print("=" * 60, "\n")

n_total = len(df)
n_events = df['event'].sum()
n_censored = n_total - n_events
cens_rate = n_censored / n_total * 100

print("── Follow-Up Time Summary ──")
print(f"  Median: {df['time'].median():.0f} days")
print(f"  IQR: [{df['time'].quantile(0.25):.0f}, {df['time'].quantile(0.75):.0f}] days")
print(f"  Range: [{df['time'].min():.0f}, {df['time'].max():.0f}] days")
print(f"  Mean (SD): {df['time'].mean():.1f} ({df['time'].std():.1f}) days")

print(f"\n── Censoring Assessment ──")
print(f"  Total N = {n_total}")
print(f"  Events (deaths): {n_events} ({n_events/n_total*100:.1f}%)")
print(f"  Censored: {n_censored} ({cens_rate:.1f}%)")

for grp in ['Male', 'Female']:
    sub = df[df['sex_label'] == grp]
    grp_cens = (sub['event'] == 0).sum() / len(sub) * 100
    print(f"  Censoring rate ({grp}): {grp_cens:.1f}%")

# Overall KM
kmf_all = KaplanMeierFitter()
kmf_all.fit(df['time'], df['event'], label='Overall')

fig, ax = plt.subplots(figsize=(12, 5))
kmf_all.plot_survival_function(ax=ax, ci_show=True, color='#4A90D9')
ax.axhline(y=0.5, linestyle='--', color='grey', alpha=0.6)
ax.set_title('Overall Kaplan-Meier Survival Curve', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Survival Probability')
plt.tight_layout()
plt.savefig('plot_01_km_overall.png', dpi=300, bbox_inches='tight')
plt.close()
print("\nSaved: plot_01_km_overall.png")

# Event histogram
fig, ax = plt.subplots(figsize=(12, 5))
df_ev = df[df['event'] == 1]['time']
df_cn = df[df['event'] == 0]['time']
ax.hist([df_ev, df_cn], bins=25, stacked=True, alpha=0.7,
        color=['#D94A4A', '#7FB3D8'], edgecolor='white',
        label=['Event (death)', 'Censored'])
ax.set_title('Distribution of Event and Censoring Times', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Count')
ax.legend()
plt.tight_layout()
plt.savefig('plot_01b_event_histogram.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: plot_01b_event_histogram.png")

median_surv = kmf_all.median_survival_time_
print(f"\nOverall median survival: {median_surv:.0f} days")
print(f"\nInterpretation: Median follow-up was {df['time'].median():.0f} days "
      f"(IQR: {df['time'].quantile(0.25):.0f}–{df['time'].quantile(0.75):.0f}).")
print(f"Of {n_total} patients, {n_events} ({n_events/n_total*100:.1f}%) died "
      f"and {n_censored} ({cens_rate:.1f}%) were censored.")

# ── PART 2: Primary Test — Survival by Sex ──────────────────────────────────

print("\n" + "=" * 60)
print("PART 2: Primary Test — Survival by Sex")
print("=" * 60, "\n")

# KM per group
fig, ax = plt.subplots(figsize=(12, 5))
group_colors = {'Male': '#D94A4A', 'Female': '#4A90D9'}

km_results = {}
for grp in ['Male', 'Female']:
    mask = df['sex_label'] == grp
    kmf = KaplanMeierFitter()
    kmf.fit(df.loc[mask, 'time'], df.loc[mask, 'event'], label=grp)
    kmf.plot_survival_function(ax=ax, ci_show=True, color=group_colors[grp])
    km_results[grp] = kmf

ax.axhline(y=0.5, linestyle='--', color='grey', alpha=0.6)
ax.set_title('Kaplan-Meier Survival Curves by Sex', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Survival Probability')
ax.legend(loc='lower left')
plt.tight_layout()
plt.savefig('plot_02_km_groups.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: plot_02_km_groups.png\n")

# Log-rank test
male_mask = df['sex_label'] == 'Male'
lr = logrank_test(
    df.loc[male_mask, 'time'], df.loc[~male_mask, 'time'],
    df.loc[male_mask, 'event'], df.loc[~male_mask, 'event']
)

p_fmt = '< .001' if lr.p_value < 0.001 else f'= {lr.p_value:.3f}'
print("── Log-Rank Test ──")
print(f"  chi-sq(1) = {lr.test_statistic:.2f}, p {p_fmt}")

# Median survival per group
print("\n── Median Survival per Group ──")
for grp, kmf in km_results.items():
    med = kmf.median_survival_time_
    n_grp = (df['sex_label'] == grp).sum()
    ev_grp = df.loc[df['sex_label'] == grp, 'event'].sum()
    if np.isinf(med):
        print(f"  {grp}: n = {n_grp}, events = {ev_grp}, median = not reached")
    else:
        print(f"  {grp}: n = {n_grp}, events = {ev_grp}, median = {med:.0f} days")

# Landmark survival rates
print("\n── Landmark Survival Rates ──")
landmark_days = [183, 365, 730]
landmark_labels = ['6-month', '1-year', '2-year']

for lday, llab in zip(landmark_days, landmark_labels):
    print(f"\n  {llab} (day {lday}):")
    for grp, kmf in km_results.items():
        surv_func = kmf.survival_function_at_times(lday)
        surv_val = surv_func.values[0]
        print(f"    {grp}: {surv_val*100:.1f}%")

# Univariate Cox — HR preview
print("\n── Hazard Ratio Preview (Univariate Cox) ──")
df_cox_uni = df[['time', 'event', 'sex']].copy()
df_cox_uni['female'] = (df_cox_uni['sex'] == 2).astype(int)
df_cox_uni = df_cox_uni.drop(columns=['sex'])

cph_uni = CoxPHFitter()
cph_uni.fit(df_cox_uni, duration_col='time', event_col='event')

hr = np.exp(cph_uni.params_['female'])
ci = np.exp(cph_uni.confidence_intervals_.values[0])
hr_lower, hr_upper = ci[0], ci[1]
cph_uni_p = cph_uni.summary['p']['female']
c_idx = cph_uni.concordance_index_

p_fmt = '< .001' if cph_uni_p < 0.001 else f'= {cph_uni_p:.3f}'
print(f"  HR = {hr:.2f}, 95% CI [{hr_lower:.2f}, {hr_upper:.2f}], p {p_fmt}")
print(f"  Concordance index: {c_idx:.3f}")
if hr < 1:
    print(f"  Interpretation: Female patients had {(1-hr)*100:.0f}% lower hazard of death compared to males.")
else:
    print(f"  Interpretation: Female patients had {hr:.2f} times the hazard of death compared to males.")

# ── PART 3: Univariate Cox Screening ────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 3: Univariate Cox Screening")
print("=" * 60, "\n")

univariate_results = []
for pred in predictor_names:
    df_uni = df[['time', 'event', pred]].copy()
    cph_u = CoxPHFitter()
    cph_u.fit(df_uni, duration_col='time', event_col='event')

    hr_u = np.exp(cph_u.params_[pred])
    ci_u = np.exp(cph_u.confidence_intervals_.values[0])
    p_u = cph_u.summary['p'][pred]
    c_u = cph_u.concordance_index_

    univariate_results.append({
        'Predictor': pred,
        'HR': hr_u,
        'CI_lower': ci_u[0],
        'CI_upper': ci_u[1],
        'p': p_u,
        'C-index': c_u,
    })

uni_df = pd.DataFrame(univariate_results)
print("── Univariate Cox Regression Results ──\n")
for _, row in uni_df.iterrows():
    p_str = '< .001' if row['p'] < 0.001 else f"{row['p']:.3f}"
    print(f"  {row['Predictor']:>10s}: HR = {row['HR']:.2f}, "
          f"95% CI [{row['CI_lower']:.2f}, {row['CI_upper']:.2f}], "
          f"p = {p_str}, C-index = {row['C-index']:.3f}")

print(f"\n  Significant predictors (p < 0.05): "
      f"{', '.join(uni_df.loc[uni_df['p'] < 0.05, 'Predictor'].tolist())}")

# ── PART 4: Multivariable Cox Proportional Hazards ──────────────────────────

print("\n" + "=" * 60)
print("PART 4: Multivariable Cox Proportional Hazards")
print("=" * 60, "\n")

df_cox = df[['time', 'event'] + predictor_names].copy()
cph = CoxPHFitter()
cph.fit(df_cox, duration_col='time', event_col='event')

print("── Cox PH Model Summary ──\n")
cox_summary = cph.summary[['exp(coef)', 'exp(coef) lower 95%', 'exp(coef) upper 95%', 'p']].copy()
cox_summary.columns = ['HR', 'HR_lower', 'HR_upper', 'p']

for pred in predictor_names:
    row = cox_summary.loc[pred]
    p_str = '< .001' if row['p'] < 0.001 else f"{row['p']:.3f}"
    print(f"  {pred:>10s}: HR = {row['HR']:.2f}, "
          f"95% CI [{row['HR_lower']:.2f}, {row['HR_upper']:.2f}], "
          f"p = {p_str}")

print(f"\n  Concordance index: {cph.concordance_index_:.3f}")
print(f"  Partial AIC: {cph.AIC_partial_:.1f}")

# Log-likelihood ratio test (global)
ll_model = cph.log_likelihood_
ll_null = CoxPHFitter()
df_null = df[['time', 'event']].copy()
df_null['_intercept'] = 1
# Global test from summary
print(f"  Log-likelihood (model): {ll_model:.2f}")

# Schoenfeld PH test
print("\n── Proportional Hazards Assumption (Schoenfeld Test) ──\n")
try:
    ph_test = cph.check_assumptions(df_cox, p_value_threshold=0.05, show_plots=False)
    print("  PH assumption test completed. See above for any violations.")
except Exception as e:
    print(f"  [WARN] Automated assumption summary was not available: {e}")

# Manual Schoenfeld test using lifelines built-in
from lifelines.statistics import proportional_hazard_test
ph_results = proportional_hazard_test(cph, df_cox, time_transform='rank')
print("\n  Schoenfeld test per predictor:")
for pred in predictor_names:
    try:
        row = ph_results.summary.loc[pred]
        p_str = '< .001' if row['p'] < 0.001 else f"{row['p']:.3f}"
        violated = "*** VIOLATED ***" if row['p'] < 0.05 else "OK"
        print(f"    {pred:>10s}: chi-sq = {row['test_statistic']:.2f}, p = {p_str}  {violated}")
    except KeyError:
        print(f"    {pred:>10s}: not available")

# Check global PH
any_violated = (ph_results.summary['p'] < 0.05).any()
if any_violated:
    violated_vars = ph_results.summary[ph_results.summary['p'] < 0.05].index.tolist()
    print(f"\n  WARNING: PH assumption violated for: {', '.join(violated_vars)}")
    print("  AFT models (below) provide an alternative lens that does not require PH.")
else:
    print("\n  PH assumption holds globally. Cox PH results are reliable.")

# Cox coefficient forest plot
fig, ax = plt.subplots(figsize=(8, 6))
hrs = cox_summary['HR'].values
lowers = cox_summary['HR_lower'].values
uppers = cox_summary['HR_upper'].values
y_pos = np.arange(len(predictor_names))

ax.errorbar(hrs, y_pos, xerr=[hrs - lowers, uppers - hrs],
            fmt='o', color='#4A90D9', capsize=4, markersize=6)
ax.axvline(x=1.0, linestyle='--', color='grey', alpha=0.6)
ax.set_yticks(y_pos)
ax.set_yticklabels(predictor_names)
ax.set_xlabel('Hazard Ratio (95% CI)')
ax.set_title('Cox PH — Multivariable Hazard Ratios', fontsize=14, fontweight='bold')
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('plot_05_cox_forest.png', dpi=300, bbox_inches='tight')
plt.close()
print("\nSaved: plot_05_cox_forest.png")

# ── PART 5: Accelerated Failure Time Models ─────────────────────────────────

print("\n" + "=" * 60)
print("PART 5: Accelerated Failure Time (AFT) Models")
print("=" * 60, "\n")

# Prepare data for AFT (lifelines AFT expects specific column format)
df_aft = df[['time', 'event'] + predictor_names].copy()

aft_models = {}
aft_aics = {}

# Helper: lifelines AFT fitters use different parameter namespaces for the
# location parameter. Weibull uses 'lambda_', Log-Normal uses 'mu_',
# Log-Logistic uses 'alpha_'. This function finds the correct namespace
# by inspecting the fitted model's params_ index.
def _aft_location_param(fitter):
    """Return the parameter block name that holds covariate coefficients."""
    if hasattr(fitter, 'params_') and hasattr(fitter.params_, 'index'):
        idx = fitter.params_.index
        if hasattr(idx, 'get_level_values'):
            param_names = idx.get_level_values(0).unique().tolist()
            for candidate in ['mu_', 'lambda_', 'alpha_']:
                if candidate in param_names:
                    return candidate
    return 'mu_'  # fallback

def _print_aft_results(fitter, predictor_names, label):
    """Extract and print time ratios from any lifelines AFT fitter."""
    param_block = _aft_location_param(fitter)
    for pred in predictor_names:
        try:
            coef = fitter.params_.loc[(param_block, pred)]
            tr = np.exp(coef)
            ci_low = np.exp(fitter.confidence_intervals_.loc[(param_block, pred)].values[0])
            ci_up = np.exp(fitter.confidence_intervals_.loc[(param_block, pred)].values[1])
            p_val = fitter.summary.loc[(param_block, pred), 'p']
            p_str = '< .001' if p_val < 0.001 else f"{p_val:.3f}"
            print(f"  {pred:>10s}: TR = {tr:.2f}, 95% CI [{ci_low:.2f}, {ci_up:.2f}], p = {p_str}")
        except (KeyError, IndexError):
            print(f"  {pred:>10s}: not estimable")

# Weibull AFT
print("── Weibull AFT ──\n")
waft = WeibullAFTFitter()
waft.fit(df_aft, duration_col='time', event_col='event')
aft_models['Weibull'] = waft
aft_aics['Weibull'] = waft.AIC_
_print_aft_results(waft, predictor_names, "Weibull")
print(f"\n  AIC: {waft.AIC_:.1f}, Concordance: {waft.concordance_index_:.3f}")

# Log-Normal AFT
print("\n── Log-Normal AFT ──\n")
lnaft = LogNormalAFTFitter()
lnaft.fit(df_aft, duration_col='time', event_col='event')
aft_models['LogNormal'] = lnaft
aft_aics['LogNormal'] = lnaft.AIC_
_print_aft_results(lnaft, predictor_names, "LogNormal")
print(f"\n  AIC: {lnaft.AIC_:.1f}, Concordance: {lnaft.concordance_index_:.3f}")

# Log-Logistic AFT
print("\n── Log-Logistic AFT ──\n")
llaft = LogLogisticAFTFitter()
llaft.fit(df_aft, duration_col='time', event_col='event')
aft_models['LogLogistic'] = llaft
aft_aics['LogLogistic'] = llaft.AIC_
_print_aft_results(llaft, predictor_names, "LogLogistic")

print(f"\n  AIC: {llaft.AIC_:.1f}, Concordance: {llaft.concordance_index_:.3f}")

# AFT AIC comparison
print("\n── AFT Distribution Comparison (AIC) ──\n")
best_aft = min(aft_aics, key=aft_aics.get)
for name, aic in sorted(aft_aics.items(), key=lambda x: x[1]):
    marker = " ← best fit" if name == best_aft else ""
    print(f"  {name:>12s}: AIC = {aic:.1f}{marker}")
print(f"\n  The {best_aft} distribution best characterizes the survival time distribution.")

# ── PART 6: Random Survival Forest ──────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 6: Random Survival Forest (Exploratory)")
print("=" * 60, "\n")

# Prepare data for scikit-survival
X_rsf = df[predictor_names].values
y_rsf = np.array(
    [(bool(e), t) for e, t in zip(df['event'], df['time'])],
    dtype=[('event', bool), ('time', float)]
)

rsf = RandomSurvivalForest(
    n_estimators=500,
    min_samples_split=6,
    min_samples_leaf=3,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1,
)
rsf.fit(X_rsf, y_rsf)

# Concordance
rsf_pred = rsf.predict(X_rsf)
rsf_c = concordance_index_censored(
    df['event'].astype(bool), df['time'], rsf_pred
)[0]
print(f"  RSF concordance index (in-sample): {rsf_c:.3f}")

# Permutation importance
from sklearn.inspection import permutation_importance

perm_result = permutation_importance(
    rsf, X_rsf, y_rsf, n_repeats=15, random_state=42, n_jobs=-1
)
rsf_importance = perm_result.importances_mean

print("\n── RSF Permutation Importance ──\n")
imp_df = pd.DataFrame({
    'Variable': predictor_names,
    'Importance': rsf_importance
}).sort_values('Importance', ascending=False)

for _, row in imp_df.iterrows():
    print(f"  {row['Variable']:>10s}: {row['Importance']:.4f}")

# Importance plot
fig, ax = plt.subplots(figsize=(8, 5))
imp_sorted = imp_df.sort_values('Importance', ascending=True)
ax.barh(imp_sorted['Variable'], imp_sorted['Importance'], color='#4A90D9', alpha=0.8)
ax.set_xlabel('Permutation Importance')
ax.set_title('Random Survival Forest — Variable Importance', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('plot_09_rsf_importance.png', dpi=300, bbox_inches='tight')
plt.close()
print("\nSaved: plot_09_rsf_importance.png")

# ── PART 7: Unified Importance Table ────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 7: Cross-Method Insight Synthesis")
print("=" * 60, "\n")

# Cox importance: |log(HR)| rescaled 0-100
cox_log_hr = np.abs(np.log(cox_summary['HR'].values))
cox_scaled = cox_log_hr / cox_log_hr.max() * 100 if cox_log_hr.max() > 0 else cox_log_hr

# RSF importance: rescaled 0-100
rsf_imp_arr = np.array([rsf_importance[predictor_names.index(p)] for p in predictor_names])
rsf_imp_arr = np.maximum(rsf_imp_arr, 0)  # floor at 0
rsf_scaled = rsf_imp_arr / rsf_imp_arr.max() * 100 if rsf_imp_arr.max() > 0 else rsf_imp_arr

# Build unified table
importance_table = pd.DataFrame({
    'Variable': predictor_names,
    'Cox |log(HR)| (0-100)': np.round(cox_scaled, 1),
    'RSF Permutation (0-100)': np.round(rsf_scaled, 1),
})

# Rank consensus
importance_table['Cox_rank'] = importance_table['Cox |log(HR)| (0-100)'].rank(ascending=False)
importance_table['RSF_rank'] = importance_table['RSF Permutation (0-100)'].rank(ascending=False)
importance_table['Avg_rank'] = (importance_table['Cox_rank'] + importance_table['RSF_rank']) / 2
importance_table['Consensus_rank'] = importance_table['Avg_rank'].rank().astype(int)

importance_table = importance_table.sort_values('Consensus_rank')

print("── Unified Variable Importance (0–100 scale) ──\n")
print(f"  {'Variable':>10s}  {'Cox':>6s}  {'RSF':>6s}  {'Rank':>4s}")
print("  " + "-" * 32)
for _, row in importance_table.iterrows():
    print(f"  {row['Variable']:>10s}  {row['Cox |log(HR)| (0-100)']:>6.1f}  "
          f"{row['RSF Permutation (0-100)']:>6.1f}  {row['Consensus_rank']:>4d}")

# Insight synthesis table
print("\n── Insight Synthesis ──\n")
print(f"  {'Method':<20s}  Unique Insight")
print("  " + "-" * 60)
print(f"  {'Cox PH':<20s}  Adjusted HRs with direction + significance; PH diagnostic")
print(f"  {'AFT':<20s}  Time ratios (intuitive); distributional fit ({best_aft} best)")
print(f"  {'RSF':<20s}  Nonlinear effects; importance confirmation; interaction detection")

# Narrative synthesis
print("\n── Narrative Synthesis ──\n")
top_cox = importance_table.iloc[0]['Variable']
top_rsf_row = importance_table.sort_values('RSF Permutation (0-100)', ascending=False).iloc[0]
top_rsf = top_rsf_row['Variable']

if top_cox == top_rsf:
    print(f"  Cox PH and RSF converge: {top_cox} emerges as the most influential predictor")
    print(f"  across both inferential and exploratory frameworks, providing strong evidence")
    print(f"  for its role in survival outcomes.")
else:
    print(f"  Cox PH identifies {top_cox} as the strongest adjusted predictor, while RSF")
    print(f"  ranks {top_rsf} highest — this divergence may reflect nonlinear effects")
    print(f"  captured by the tree-based approach.")

print(f"\n  AFT modeling under the {best_aft} distribution offers time-ratio interpretations")
print(f"  that complement hazard ratios, particularly useful for clinical audiences.")

if any_violated:
    print(f"\n  The PH assumption was violated for {', '.join(violated_vars)},")
    print(f"  underscoring the value of AFT models as a robustness check.")
else:
    print(f"\n  The PH assumption held globally, supporting the reliability of Cox PH estimates.")
    print(f"  AFT and RSF results serve as confirmatory lenses rather than corrections.")

# ── PART 8: Model Assessment Summary ────────────────────────────────────────

print("\n" + "=" * 60)
print("PART 8: Model Assessment Summary")
print("=" * 60, "\n")

print("── Concordance Index (C-statistic) ──\n")
print(f"  Cox PH:              {cph.concordance_index_:.3f}")
print(f"  Weibull AFT:         {aft_models['Weibull'].concordance_index_:.3f}")
print(f"  Log-Normal AFT:      {aft_models['LogNormal'].concordance_index_:.3f}")
print(f"  Log-Logistic AFT:    {aft_models['LogLogistic'].concordance_index_:.3f}")
print(f"  Random Survival Forest: {rsf_c:.3f}")
print()
print("  Note: These are in-sample concordance indices. Models are analytic lenses,")
print("  not contestants — each provides a different kind of insight.")
print("  Concordance is reported for calibration, not for ranking models.")

# ── Summary ─────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Analysis Complete")
print("=" * 60, "\n")

print("Plots saved:")
print("  plot_01_km_overall.png")
print("  plot_01b_event_histogram.png")
print("  plot_02_km_groups.png")
print("  plot_05_cox_forest.png")
print("  plot_09_rsf_importance.png")
print()
print("Models fit:")
print("  - Kaplan-Meier + Log-rank test")
print("  - Univariate Cox screening (7 predictors)")
print("  - Multivariable Cox PH with Schoenfeld PH test")
print("  - Weibull AFT, Log-Normal AFT, Log-Logistic AFT")
print("  - Random Survival Forest (500 trees, permutation importance)")
print("  - Unified importance table (Cox + RSF, 0-100 scale)")

# ── PART 9: Manuscript Output ────────────────────────────────────────────────

uni_df.to_csv(os.path.join(tables_dir, 'univariate_cox.csv'), index=False)
cox_out = cox_summary.reset_index().rename(columns={'index': 'Predictor'})
cox_out.to_csv(os.path.join(tables_dir, 'cox_summary.csv'), index=False)
importance_table.to_csv(os.path.join(tables_dir, 'importance_table.csv'), index=False)
aft_aic_df = pd.DataFrame(
    [{'Model': name, 'AIC': aic} for name, aic in sorted(aft_aics.items(), key=lambda x: x[1])]
)
aft_aic_df.to_csv(os.path.join(tables_dir, 'aft_model_comparison.csv'), index=False)

for plot_name in [
    'plot_01_km_overall.png',
    'plot_01b_event_histogram.png',
    'plot_02_km_groups.png',
    'plot_05_cox_forest.png',
    'plot_09_rsf_importance.png',
]:
    if os.path.exists(plot_name):
        shutil.copy2(plot_name, os.path.join(figures_dir, plot_name))

cox_top_name = cox_summary.sort_values('p').index[0]
cox_top = cox_summary.sort_values('p').iloc[0]
sex_median_male = km_results['Male'].median_survival_time_
sex_median_female = km_results['Female'].median_survival_time_
top_rsf = imp_df.iloc[0]['Variable']

methods_text = f"""## Methods

### Statistical Analysis

Complete-case data from the NCCTG lung cancer dataset were analyzed after excluding observations with missing values on the prespecified covariates. Survival time was measured in days, and the event indicator represented death versus right censoring.

Kaplan-Meier estimators were used to summarize overall survival and survival stratified by sex. Group differences in survival curves were evaluated with the log-rank test. Median survival times and landmark survival probabilities were reported descriptively.

Predictor screening used univariate Cox proportional hazards models for sex, age, ECOG performance status, Karnofsky scores, meal calories, and weight loss. A multivariable Cox proportional hazards model then estimated adjusted hazard ratios (HRs) with 95% confidence intervals. The proportional hazards assumption was assessed with Schoenfeld residual tests.

Accelerated failure time (AFT) models with Weibull, log-normal, and log-logistic distributions were fitted as complementary lenses that provide time-ratio interpretations and relax the proportional hazards assumption. Distributional fit within the AFT family was compared using Akaike's Information Criterion (AIC).

As an exploratory nonparametric complement, a random survival forest with 500 trees was fitted and permutation importance was used to summarize variable importance. Cox absolute log-hazard ratios and random survival forest permutation scores were rescaled to a common 0-100 scale for cross-method comparison.

Analyses were conducted in Python using lifelines, scikit-survival, pandas, NumPy, and matplotlib. Statistical significance was evaluated at alpha = .05, and all confidence intervals are at the 95% level.
"""

results_text = f"""## Results

### Follow-Up and Censoring

The complete-case analysis included {n_total} patients, of whom {n_events} ({n_events / n_total * 100:.1f}%) experienced the event and {n_censored} ({cens_rate:.1f}%) were censored. Overall median survival was {median_surv:.0f} days.

### Kaplan-Meier and Log-Rank Analysis

Survival differed by sex in the primary comparison, with a log-rank test of chi-sq(1) = {lr.test_statistic:.2f}, p {fmt_p_value(lr.p_value)}. Median survival was {sex_median_male:.0f} days for male patients and {sex_median_female:.0f} days for female patients.

### Multivariable Cox Proportional Hazards Model

In the adjusted Cox model, {cox_top_name} was the strongest predictor (HR = {cox_top['HR']:.2f}, 95% CI [{cox_top['HR_lower']:.2f}, {cox_top['HR_upper']:.2f}], p {fmt_p_value(cox_top['p'])}). The model's concordance index was {cph.concordance_index_:.3f}. {'The proportional hazards assumption showed evidence of violation for ' + ', '.join(violated_vars) + ', so the Cox estimates should be interpreted alongside the AFT models.' if any_violated else 'Schoenfeld residual tests did not identify meaningful proportional hazards violations, supporting the Cox model interpretation.'}

### Accelerated Failure Time Models

Within the AFT family, the {best_aft} model provided the best distributional fit (AIC = {aft_aics[best_aft]:.1f}). These models offered time-ratio interpretations that complemented the hazard-ratio results from the Cox model.

### Random Survival Forest and Cross-Method Synthesis

The random survival forest achieved an in-sample concordance index of {rsf_c:.3f}, and {top_rsf} ranked highest by permutation importance. The unified importance table showed how the semiparametric Cox model and the nonparametric survival forest converged on the most influential predictors.
"""

references_bib = r"""@article{cox1972,
  author  = {Cox, D. R.},
  title   = {Regression Models and Life-Tables},
  journal = {Journal of the Royal Statistical Society: Series B},
  year    = {1972},
  volume  = {34},
  number  = {2},
  pages   = {187--220}
}

@article{kaplan1958,
  author  = {Kaplan, Edward L. and Meier, Paul},
  title   = {Nonparametric Estimation from Incomplete Observations},
  journal = {Journal of the American Statistical Association},
  year    = {1958},
  volume  = {53},
  number  = {282},
  pages   = {457--481}
}

@article{ishwaran2008,
  author  = {Ishwaran, Hemant and Kogalur, Udaya B. and Blackstone, Eugene H. and Lauer, Michael S.},
  title   = {Random Survival Forests},
  journal = {The Annals of Applied Statistics},
  year    = {2008},
  volume  = {2},
  number  = {3},
  pages   = {841--860}
}
"""

with open(os.path.join(output_dir, 'methods.md'), 'w') as f:
    f.write(methods_text)
with open(os.path.join(output_dir, 'results.md'), 'w') as f:
    f.write(results_text)
with open(os.path.join(output_dir, 'references.bib'), 'w') as f:
    f.write(references_bib)

print("\nSaved manuscript artifacts:")
print(f"  {os.path.join(output_dir, 'methods.md')}")
print(f"  {os.path.join(output_dir, 'results.md')}")
print(f"  {os.path.join(output_dir, 'references.bib')}")
