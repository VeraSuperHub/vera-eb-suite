"""
Nominal Outcome Analysis: Iris Species Classification
Outcome: Species (setosa, versicolor, virginica) -- 3-class nominal
Predictors: Sepal.Length, Sepal.Width, Petal.Length, Petal.Width
"""

import warnings
warnings.filterwarnings("ignore")

import os
import shutil
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import statsmodels.api as sm
from statsmodels.discrete.discrete_model import MNLogit
import lightgbm as lgb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

output_dir = os.path.join(os.getcwd(), "output")
tables_dir = os.path.join(output_dir, "tables")
figures_dir = os.path.join(output_dir, "figures")
os.makedirs(tables_dir, exist_ok=True)
os.makedirs(figures_dir, exist_ok=True)

# ==============================================================================
# PART 0: Setup
# ==============================================================================

iris = load_iris()
df = pd.DataFrame(iris.data, columns=["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"])
df["Species"] = pd.Categorical(iris.target_names[iris.target])

outcome_var = "Species"
pred_vars = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]
class_names = list(iris.target_names)
N = len(df)

print(f"Dataset: iris")
print(f"N = {N}")
print(f"Outcome: {outcome_var} (nominal, {len(class_names)} classes)")
print(f"Predictors: {', '.join(pred_vars)}\n")

# Helper
def fmt_p(p):
    return "< .001" if p < 0.001 else f"{p:.3f}"

# ==============================================================================
# PART 5A: Multinomial Logistic Regression
# ==============================================================================

print("=" * 70)
print("MULTINOMIAL LOGISTIC REGRESSION")
print("=" * 70)

# Reference category: most frequent (all equal here; use setosa = index 0)
ref_cat = "setosa"
print(f"\nReference category: {ref_cat}")

X = df[pred_vars].copy()
y = df[outcome_var].copy()

# Encode outcome numerically with setosa = 0 as reference
class_map = {name: i for i, name in enumerate(class_names)}
y_num = y.map(class_map)

# Standardize predictors for comparable coefficients
scaler = StandardScaler()
X_std = pd.DataFrame(scaler.fit_transform(X), columns=pred_vars)
X_std_const = sm.add_constant(X_std)

# Fit MNLogit
mnl_model = MNLogit(y_num, X_std_const)
mnl_result = mnl_model.fit(method="newton", disp=0, maxiter=200)

print("\nModel summary: log-likelihood = {:.2f}, AIC = {:.2f}, BIC = {:.2f}".format(
    mnl_result.llf, mnl_result.aic, mnl_result.bic))

# McFadden pseudo R-squared
mnl_null = MNLogit(y_num, sm.add_constant(np.ones((N, 1))))
mnl_null_res = mnl_null.fit(method="newton", disp=0, maxiter=200)
mcfadden_r2 = 1 - (mnl_result.llf / mnl_null_res.llf)
print(f"McFadden pseudo-R-squared: {mcfadden_r2:.3f}")

# Extract coefficients and RRR for each non-reference class
# MNLogit params shape: (n_features, n_classes - 1)
params = mnl_result.params    # columns = non-ref classes (versicolor=1, virginica=2)
bse = mnl_result.bse
pvalues = mnl_result.pvalues
conf = mnl_result.conf_int()

non_ref_classes = [c for c in class_names if c != ref_cat]
coef_names = ["const"] + pred_vars

print("\nRelative Risk Ratios (RRR = exp(B)) with 95% CI:")
print("-" * 70)

# Store standardized coefficients for importance
mnl_std_coefs = {}
mnl_rows = []

for j, cls in enumerate(non_ref_classes):
    print(f"\n  {cls} vs {ref_cat}:")
    for i, vname in enumerate(coef_names):
        b = params.iloc[i, j]
        se = bse.iloc[i, j]
        p = pvalues.iloc[i, j]
        rrr = np.exp(b)
        ci_lo = np.exp(b - 1.96 * se)
        ci_hi = np.exp(b + 1.96 * se)
        print(f"    {vname:15s}  B = {b:7.3f}  RRR = {rrr:7.2f}  95% CI [{ci_lo:.2f}, {ci_hi:.2f}]  p = {fmt_p(p)}")
        mnl_rows.append({
            "Comparison": f"{cls} vs {ref_cat}",
            "Predictor": vname,
            "B": b,
            "RRR": rrr,
            "CI_lower": ci_lo,
            "CI_upper": ci_hi,
            "p_value": p,
            "Abs_B": abs(b),
        })

        if vname != "const":
            if vname not in mnl_std_coefs:
                mnl_std_coefs[vname] = []
            mnl_std_coefs[vname].append(abs(b))  # already standardized

# Average |standardized coef| across non-ref classes
mnl_importance_raw = {v: np.mean(mnl_std_coefs[v]) for v in pred_vars}

# ==============================================================================
# PART 5B: Linear Discriminant Analysis (LDA)
# ==============================================================================

print("\n" + "=" * 70)
print("LINEAR DISCRIMINANT ANALYSIS (LDA)")
print("=" * 70)

X_arr = X.values
y_arr = iris.target

lda = LinearDiscriminantAnalysis()
lda.fit(X_arr, y_arr)
lda_pred = lda.predict(X_arr)
lda_acc = accuracy_score(y_arr, lda_pred)

# Discriminant function loadings (scalings)
n_functions = lda.scalings_.shape[1]
print(f"\nNumber of discriminant functions: {n_functions}")

# Explained variance ratio
ev_ratio = lda.explained_variance_ratio_
print("\nDiscriminant function explained variance:")
for k in range(n_functions):
    print(f"  LD{k+1}: {ev_ratio[k]*100:.1f}%")

# Wilks' lambda approximation
# Lambda = product of 1/(1 + eigenvalue_i) for unused functions
# For overall test: product of all
eigenvalues = lda.explained_variance_ratio_ / (1 - lda.explained_variance_ratio_ + 1e-15)
# Better: compute from class separation
from scipy import stats as sp_stats

# Wilks' lambda via MANOVA-style computation
from numpy.linalg import det

overall_mean = X_arr.mean(axis=0)
W = np.zeros((X_arr.shape[1], X_arr.shape[1]))
B = np.zeros((X_arr.shape[1], X_arr.shape[1]))
for c in range(len(class_names)):
    Xc = X_arr[y_arr == c]
    nc = len(Xc)
    class_mean = Xc.mean(axis=0)
    diff = class_mean - overall_mean
    B += nc * np.outer(diff, diff)
    W += (Xc - class_mean).T @ (Xc - class_mean)

wilks_lambda = det(W) / det(W + B)

# Approximate F-test for Wilks' lambda
p_vars = X_arr.shape[1]
k = len(class_names)
n = N
# Rao's F approximation
df1 = p_vars * (k - 1)
df2_num = n - 1 - (p_vars + k) / 2
s = np.sqrt((p_vars**2 * (k-1)**2 - 4) / (p_vars**2 + (k-1)**2 - 5)) if (p_vars**2 + (k-1)**2 - 5) > 0 else 1
df2 = df2_num * s - (df1 / 2) + 1
lam_power = wilks_lambda ** (1.0 / s) if s != 0 else wilks_lambda
f_approx = ((1 - lam_power) / lam_power) * (df2 / df1)
wilks_p = 1 - sp_stats.f.cdf(f_approx, df1, df2)

print(f"\nWilks' lambda = {wilks_lambda:.4f}")
print(f"Approximate F({df1:.0f}, {df2:.0f}) = {f_approx:.2f}, p = {fmt_p(wilks_p)}")
print(f"In-sample accuracy: {lda_acc*100:.1f}%")

# Structure matrix / loadings
print("\nDiscriminant function loadings (structure matrix):")
print(f"  {'Variable':20s}", end="")
for k in range(n_functions):
    print(f"  LD{k+1:d}", end="")
print()
print("  " + "-" * (20 + n_functions * 8))

lda_loadings = {}
for i, v in enumerate(pred_vars):
    print(f"  {v:20s}", end="")
    abs_loads = []
    for k in range(n_functions):
        val = lda.scalings_[i, k]
        print(f"  {val:7.3f}", end="")
        abs_loads.append(abs(val) * ev_ratio[k])  # weight by explained variance
    print()
    lda_loadings[v] = sum(abs_loads)

# LDA scatter plot
X_lda = lda.transform(X_arr)
plt.figure(figsize=(8, 6))
colors_lda = ["#4C72B0", "#DD8452", "#55A868"]
for c, cname in enumerate(class_names):
    mask = y_arr == c
    plt.scatter(X_lda[mask, 0], X_lda[mask, 1], c=colors_lda[c],
                label=cname, alpha=0.7, edgecolors="k", linewidths=0.3, s=50)
plt.xlabel(f"LD1 ({ev_ratio[0]*100:.1f}%)")
plt.ylabel(f"LD2 ({ev_ratio[1]*100:.1f}%)")
plt.title("LDA Discriminant Score Scatter: LD1 vs LD2")
plt.legend(title="Species")
plt.tight_layout()
plt.savefig("plot_06_lda_scores.png", dpi=300)
plt.close()
print("\nSaved: plot_06_lda_scores.png")

# ==============================================================================
# PART 5C: CART (Classification Tree)
# ==============================================================================

print("\n" + "=" * 70)
print("CLASSIFICATION TREE (CART)")
print("=" * 70)

cart = DecisionTreeClassifier(max_depth=4, random_state=42)
cart.fit(X_arr, y_arr)
cart_pred = cart.predict(X_arr)
cart_acc = accuracy_score(y_arr, cart_pred)

print(f"\nIn-sample accuracy: {cart_acc*100:.1f}%")
print("\nTree rules:")
print(export_text(cart, feature_names=pred_vars, max_depth=4))

cart_imp = dict(zip(pred_vars, cart.feature_importances_))
print("CART variable importance:")
for v in pred_vars:
    print(f"  {v:20s}  {cart_imp[v]:.3f}")

# ==============================================================================
# PART 5D: Random Forest
# ==============================================================================

print("\n" + "=" * 70)
print("RANDOM FOREST")
print("=" * 70)

rf = RandomForestClassifier(n_estimators=500, random_state=42)
rf.fit(X_arr, y_arr)
rf_pred = rf.predict(X_arr)
rf_acc = accuracy_score(y_arr, rf_pred)

print(f"\nIn-sample accuracy: {rf_acc*100:.1f}%")

# Permutation importance (more reliable than Gini for correlated features)
perm_imp = permutation_importance(rf, X_arr, y_arr, n_repeats=30, random_state=42)
rf_importance_raw = dict(zip(pred_vars, perm_imp.importances_mean))

print("\nRF permutation importance:")
for v in pred_vars:
    print(f"  {v:20s}  {rf_importance_raw[v]:.4f}")

# RF importance plot
plt.figure(figsize=(8, 5))
sorted_rf = sorted(rf_importance_raw.items(), key=lambda x: x[1], reverse=True)
plt.barh([x[0] for x in sorted_rf], [x[1] for x in sorted_rf], color="#4C72B0")
plt.xlabel("Permutation Importance")
plt.title("Random Forest: Variable Importance")
plt.tight_layout()
plt.savefig("plot_08_rf_importance.png", dpi=300)
plt.close()
print("Saved: plot_08_rf_importance.png")

# ==============================================================================
# PART 5E: LightGBM
# ==============================================================================

print("\n" + "=" * 70)
print("LightGBM")
print("=" * 70)

min_child = max(3, N // 10)
lgb_model = lgb.LGBMClassifier(
    objective="multiclass",
    n_estimators=500,
    max_depth=3,
    learning_rate=0.1,
    num_leaves=15,
    min_child_samples=min_child,
    random_state=42,
    verbose=-1,
    num_classes=3,
)
lgb_model.fit(X_arr, y_arr)
lgb_pred = lgb_model.predict(X_arr)
lgb_acc = accuracy_score(y_arr, lgb_pred)

print(f"\nHyperparameters: n_estimators=500, max_depth=3, lr=0.1, num_leaves=15, min_child_samples={min_child}")
print(f"In-sample accuracy: {lgb_acc*100:.1f}%")

lgb_gain = dict(zip(pred_vars, lgb_model.feature_importances_))
print("\nLightGBM gain importance:")
for v in pred_vars:
    print(f"  {v:20s}  {lgb_gain[v]}")

# LightGBM importance plot
plt.figure(figsize=(8, 5))
sorted_lgb = sorted(lgb_gain.items(), key=lambda x: x[1], reverse=True)
plt.barh([x[0] for x in sorted_lgb], [x[1] for x in sorted_lgb], color="#DD8452")
plt.xlabel("Gain Importance")
plt.title("LightGBM: Variable Importance")
plt.tight_layout()
plt.savefig("plot_09_lgbm_importance.png", dpi=300)
plt.close()
print("Saved: plot_09_lgbm_importance.png")

# ==============================================================================
# PART 5F: Confusion Matrices (All Models)
# ==============================================================================

print("\n" + "=" * 70)
print("CONFUSION MATRICES & PER-CLASS METRICS")
print("=" * 70)
print(f"\nNote: In-sample metrics (N = {N}). No train/test split due to sample size.")

models_preds = {
    "Multinomial Logistic": mnl_result.predict().argmax(axis=1),
    "LDA": lda_pred,
    "CART": cart_pred,
    "Random Forest": rf_pred,
    "LightGBM": lgb_pred,
}

summary_rows = []
for mname, ypred in models_preds.items():
    cm = confusion_matrix(y_arr, ypred)
    acc = accuracy_score(y_arr, ypred)
    report = classification_report(y_arr, ypred, target_names=class_names, output_dict=True)

    print(f"\n--- {mname} (accuracy: {acc*100:.1f}%) ---")
    cm_df = pd.DataFrame(cm, index=class_names, columns=class_names)
    print(cm_df.to_string())

    row = {"Model": mname, "Accuracy": f"{acc*100:.1f}%"}
    for cname in class_names:
        prec = report[cname]["precision"]
        rec = report[cname]["recall"]
        row[f"{cname}_Prec"] = f"{prec:.2f}"
        row[f"{cname}_Rec"] = f"{rec:.2f}"
        print(f"  {cname}: precision = {prec:.2f}, recall = {rec:.2f}")
    summary_rows.append(row)

print("\n\nSummary table:")
summary_df = pd.DataFrame(summary_rows)
print(summary_df.to_string(index=False))

# ==============================================================================
# PART 6: Unified Variable Importance (0-100 scale)
# ==============================================================================

print("\n" + "=" * 70)
print("UNIFIED VARIABLE IMPORTANCE (0-100 SCALE)")
print("=" * 70)
print("\nModels are analytic lenses, not contestants. Each method provides a")
print("different kind of insight into which predictors matter most.\n")

def rescale_0_100(d):
    """Rescale dictionary values to 0-100 (max = 100)."""
    max_val = max(d.values())
    if max_val == 0:
        return {k: 0 for k in d}
    return {k: (v / max_val) * 100 for k, v in d.items()}

mnl_scaled = rescale_0_100(mnl_importance_raw)
lda_scaled = rescale_0_100(lda_loadings)
rf_scaled = rescale_0_100(rf_importance_raw)
lgb_scaled = rescale_0_100(lgb_gain)

# Build table
imp_rows = []
for v in pred_vars:
    scores = [mnl_scaled[v], lda_scaled[v], rf_scaled[v], lgb_scaled[v]]
    imp_rows.append({
        "Variable": v,
        "Multinomial": f"{mnl_scaled[v]:.0f}",
        "LDA": f"{lda_scaled[v]:.0f}",
        "RF": f"{rf_scaled[v]:.0f}",
        "LightGBM": f"{lgb_scaled[v]:.0f}",
        "Mean": np.mean(scores),
    })

imp_df = pd.DataFrame(imp_rows)
imp_df = imp_df.sort_values("Mean", ascending=False)

# Rank consensus
for method in ["Multinomial", "LDA", "RF", "LightGBM"]:
    imp_df[f"rank_{method}"] = imp_df[method].astype(float).rank(ascending=False)

imp_df["Rank_Consensus"] = imp_df[[f"rank_{m}" for m in ["Multinomial", "LDA", "RF", "LightGBM"]]].mean(axis=1)
imp_df = imp_df.sort_values("Rank_Consensus")
imp_df["Rank_Consensus"] = imp_df["Rank_Consensus"].map(lambda x: f"{x:.1f}")

display_cols = ["Variable", "Multinomial", "LDA", "RF", "LightGBM", "Rank_Consensus"]
print(imp_df[display_cols].to_string(index=False))

# Unified importance bar chart
plt.figure(figsize=(10, 6))
bar_df = imp_df[["Variable", "Multinomial", "LDA", "RF", "LightGBM"]].copy()
bar_df = bar_df.set_index("Variable")
bar_df = bar_df.astype(float)
bar_df.plot(kind="barh", figsize=(10, 5), color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
plt.xlabel("Importance (0-100)")
plt.title("Unified Variable Importance Across Methods")
plt.legend(title="Method", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig("plot_10_unified_importance.png", dpi=300)
plt.close()
print("\nSaved: plot_10_unified_importance.png")

# ==============================================================================
# PART 6B: Insight Synthesis
# ==============================================================================

print("\n" + "=" * 70)
print("INSIGHT SYNTHESIS")
print("=" * 70)

top_var = imp_df.iloc[0]["Variable"]
print(f"""
Across all four analytic methods, {top_var} emerges as the strongest predictor
of species membership. The multinomial logistic model reveals the direction
and magnitude of class-specific effects via relative risk ratios, showing how
each unit increase in standardized predictors shifts the probability of class
membership relative to {ref_cat}. LDA identifies {n_functions} discriminant
functions, with LD1 explaining {ev_ratio[0]*100:.1f}% of between-class variance,
confirming that petal measurements drive the primary axis of separation. Tree-based
methods (RF, LightGBM) corroborate this ranking through nonparametric importance
measures, with classification accuracy at or near ceiling for this well-separated
dataset. The convergence of importance rankings across parametric, discriminant,
and ensemble methods strengthens confidence in the key predictors identified.
""")

print("=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)

# ==============================================================================
# PART 7: Manuscript Output
# ==============================================================================

mnl_df = pd.DataFrame(mnl_rows)
mnl_df.to_csv(os.path.join(tables_dir, "multinomial_rrr.csv"), index=False)
summary_df.to_csv(os.path.join(tables_dir, "classification_summary.csv"), index=False)
imp_df[display_cols].to_csv(os.path.join(tables_dir, "importance_table.csv"), index=False)

for plot_name in [
    "plot_06_lda_scores.png",
    "plot_08_rf_importance.png",
    "plot_09_lgbm_importance.png",
    "plot_10_unified_importance.png",
]:
    if os.path.exists(plot_name):
        shutil.copy2(plot_name, os.path.join(figures_dir, plot_name))

class_counts = df["Species"].value_counts().reindex(class_names)
best_model_row = summary_df.assign(
    Accuracy_num=summary_df["Accuracy"].str.rstrip("%").astype(float)
).sort_values("Accuracy_num", ascending=False).iloc[0]
strongest_mnl = mnl_df[mnl_df["Predictor"] != "const"].sort_values("Abs_B", ascending=False).iloc[0]

methods_text = f"""## Methods

### Statistical Analysis

The nominal outcome example used the iris dataset with three unordered species categories and four continuous floral measurements as predictors. Predictors were standardized before multinomial logistic regression so that relative risk ratios and coefficient magnitudes were comparable across features.

Multinomial logistic regression was fitted with setosa as the reference category. Relative risk ratios with 95% confidence intervals were obtained by exponentiating the model coefficients. Linear discriminant analysis (LDA) was used as a complementary projection-based method, with Wilks' lambda and discriminant loadings summarizing class separation.

As exploratory classification lenses, a classification tree, random forest, and LightGBM multiclass model were fit using the same predictor set. In-sample confusion matrices, overall accuracy, and per-class precision and recall were used to summarize classification performance. Variable importance from multinomial coefficients, LDA loadings, random forest permutation importance, and LightGBM gain were each rescaled to a common 0-100 scale for cross-method comparison.

Analyses were conducted in Python using statsmodels, scikit-learn, LightGBM, pandas, NumPy, SciPy, and matplotlib. Statistical significance was evaluated at alpha = .05, and all confidence intervals are at the 95% level.
"""

results_text = f"""## Results

### Class Distribution

The analysis included {N} flowers, with {class_counts['setosa']} setosa, {class_counts['versicolor']} versicolor, and {class_counts['virginica']} virginica observations.

### Multinomial Logistic Regression

Multinomial logistic regression yielded McFadden pseudo-R-squared = {mcfadden_r2:.3f}. The strongest standardized coefficient was for {strongest_mnl['Predictor']} in the {strongest_mnl['Comparison']} contrast (RRR = {strongest_mnl['RRR']:.2f}, 95% CI [{strongest_mnl['CI_lower']:.2f}, {strongest_mnl['CI_upper']:.2f}], p {'< .001' if strongest_mnl['p_value'] < 0.001 else f'= {strongest_mnl["p_value"]:.3f}'}).

### Linear Discriminant Analysis

LDA produced {n_functions} discriminant functions, with LD1 accounting for {ev_ratio[0] * 100:.1f}% of between-class variance. Wilks' lambda was {wilks_lambda:.4f}, with approximate F({df1:.0f}, {df2:.0f}) = {f_approx:.2f}, p {'< .001' if wilks_p < 0.001 else f'= {wilks_p:.3f}'}. This indicates strong multivariate separation among species.

### Classification Performance

The highest in-sample accuracy was achieved by {best_model_row['Model']} ({best_model_row['Accuracy']}). Across models, petal measurements dominated the classification boundary, while sepal measurements contributed more modestly.

### Cross-Method Synthesis

The unified importance table ranked {top_var} as the most influential predictor across multinomial logistic regression, LDA, random forest, and LightGBM. Agreement across these parametric, projection-based, and tree-based approaches strengthens confidence that the main species differences are concentrated in that measurement axis.
"""

references_bib = r"""@article{fisher1936,
  author  = {Fisher, R. A.},
  title   = {The Use of Multiple Measurements in Taxonomic Problems},
  journal = {Annals of Eugenics},
  year    = {1936},
  volume  = {7},
  number  = {2},
  pages   = {179--188}
}

@book{agresti2018,
  author    = {Agresti, Alan},
  title     = {An Introduction to Categorical Data Analysis},
  edition   = {3rd},
  year      = {2018},
  publisher = {Wiley}
}
"""

with open(os.path.join(output_dir, "methods.md"), "w") as f:
    f.write(methods_text)
with open(os.path.join(output_dir, "results.md"), "w") as f:
    f.write(results_text)
with open(os.path.join(output_dir, "references.bib"), "w") as f:
    f.write(references_bib)

print("Saved manuscript artifacts to output/")
