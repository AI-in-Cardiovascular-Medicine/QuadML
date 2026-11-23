# QuadML
QuadML: A General-Purpose, Open-Source Executable Machine Learning Framework For Supervised and Unsupervised Learning
![QuadML](QuadML-V02.jpg)

## Overview

Applying machine learning correctly takes a long chain of interdependent decisions: data cleaning, encoding, imputation, scaling, feature selection, model choice, tuning, evaluation, and interpretation. Subtle errors such as **data leakage** can silently inflate reported performance.

**QuadML** puts that whole chain into one guided, point-and-click workflow for the four main families of tabular analysis:

| | Task | What it answers |
|---|---|---|
| 🟦 | **Classification** | Which class does a sample belong to? (binary and multiclass) |
| 🟩 | **Regression** | What is the value of a continuous outcome? |
| 🟥 | **Survival analysis** | How does risk evolve over time, with right-censored follow-up? |
| 🟨 | **Clustering** | Which natural groups exist in unlabeled data? |

QuadML runs **entirely on your own computer**, so sensitive data never has to leave the PC. It exposes the **full table of every evaluated pipeline**, not just a single "winner", and the final choice of model stays with the investigator.

> QuadML is developed by the [AI in Cardiovascular Medicine (AI-CVM) group](https://ai-cvm.org/), Department of Cardiology, Inselspital Bern University Hospital, and Department of Digital Medicine, University of Bern, Switzerland.

---

## Features

### One workflow, four tasks

| Stage | Options |
|---|---|
| **Data input** | CSV or Excel; target, ID, and (for survival) duration and event columns picked manually or auto-detected; optional external validation file (supervised tasks) or benchmark label (clustering) |
| **Quality screening and cleaning** | Missing-value marker normalization; removal of empty, constant, placeholder, and duplicate columns, duplicate rows, and all-zero rows/columns |
| **Outlier detection** | Feature-level: IQR, Z-score, modified Z-score. Sample-level (supervised): Isolation Forest, Local Outlier Factor, DBSCAN, One-Class SVM |
| **Correlation filter** | Optional Pearson/Spearman redundancy filter (supervised), fitted on the training partition |
| **Encoding** | Automatic type detection, binary/one-hot/integer encoding, identifier handling, protected targets |
| **Imputation** | Simple (mean/median/mode/constant), KNN, iterative (MICE-style), MissForest-style, SoftImpute |
| **Scaling** | Standard, Min-Max, Max-Abs, Robust, Normalizer, Quantile, Power (Yeo-Johnson/Box-Cox), or none |
| **Feature selection** | Filter, wrapper, and embedded methods (Select K Best, Select Percentile, Mutual Information, Variance Threshold, RFE, SFS/SBS, Select-from-Model, tree-based, LASSO/Cox-LASSO, Boruta-style), plus clustering-specific selectors (correlation thresholding, feature agglomeration, Laplacian score) |
| **Dimensionality reduction** | PCA, ICA, Kernel PCA, LDA (classification) |
| **Hyperparameter search** | Grid or randomized search with fast / balanced / thorough budget profiles; shuffle-split, k-fold, stratified k-fold, or leave-one-out cross-validation; class-imbalance handling with class weights or SMOTE |
| **Evaluation** | Task-appropriate metrics on training, test, and external data, with optional bootstrap confidence intervals |
| **Interpretability** | SHAP, Kernel SHAP, LIME, permutation importance, PDP/ICE; for survival, SurvSHAP(t), SurvLIME, and Cox/AFT coefficient views |
| **Visualization** | Publication-ready figures, cross-pipeline comparison charts, and a plot analyzer that explains each figure in plain language |

### Learning algorithms

<details>
<summary><b>Classification: 15 algorithms</b></summary>

Logistic regression (L2, plus L1/LASSO and elastic-net variants) · Gaussian naive Bayes · k-nearest neighbors · Support vector machine · Decision tree · Random forest · Extra trees · Bagging · AdaBoost · Gradient boosting · XGBoost · Multilayer perceptron · Stacking ensemble
</details>

<details>
<summary><b>Regression: 15 algorithms</b></summary>

Linear regression · Ridge · LASSO · Elastic net · k-nearest neighbors · Support vector regression · Decision tree · Random forest · Extra trees · Bagging · AdaBoost · Gradient boosting · XGBoost · Multilayer perceptron · Stacking ensemble
</details>

<details>
<summary><b>Survival analysis: 11 methods (right-censored data)</b></summary>

*Descriptive:* Kaplan-Meier · Nelson-Aalen
*Semi-parametric and parametric:* Cox proportional hazards · Weibull AFT · Log-normal AFT · Log-logistic AFT (elastic-net penalized)
*Machine learning:* Random survival forest · Extra survival trees · Survival gradient boosting · Survival support vector machine
*Deep learning:* DeepSurv
</details>

<details>
<summary><b>Clustering: 9 algorithms</b></summary>

k-means · Agglomerative clustering · Genie · Gaussian mixture model · Spectral clustering · BIRCH · DBSCAN · HDBSCAN · OPTICS
</details>

### Combinatorial pipeline search

QuadML builds the Cartesian product of the selected imputation, scaling, feature-selection, dimensionality-reduction, and model options. It then tunes **every configuration over its own hyperparameter space**. With all options enabled, the number of distinct pipelines is:

| Task | Per run (one cleaning choice) | Across all cleaning options |
|---|---:|---:|
| Classification | 36,000 | 288,000 |
| Regression | 28,800 | 230,400 |
| Survival analysis | 2,522 | 20,176 |
| Clustering | 4,590 | 18,360 |
| **Total** | **71,912** | **556,936** |

CPU and memory targets are user-set. An adaptive scheduler plans how many configurations and cross-validation workers run in parallel and adjusts them during the run.

---

## Installation

### Option 1: Packaged application (recommended)

- **Windows:** Setup / portable builds on the [Releases](https://github.com/AI-in-Cardiovascular-Medicine/QuadML/releases) page (primary installer path). No Python installation is needed.
- **macOS (Apple Silicon):** `QuadML-macOS.app.zip` on [Releases](https://github.com/AI-in-Cardiovascular-Medicine/QuadML/releases) when a maintainer attaches the CI zip. The Mac build is currently **unsigned** (first open: Right-click → Open). Short-lived smoke builds: Actions → **Build macOS app** (`workflow_dispatch` only — not an automatic signed release). Canonical wording: `shared.app.mac_modifications.mac_readme_packaged_app_blurb()`.

### Option 2: Install from source

QuadML has been developed and built with **Python 3.11**; Python 3.10–3.12 are expected to work. Use a clean virtual environment. Do not install into the Anaconda base environment.

```bash
# 1. Clone the repository
git clone https://github.com/AI-in-Cardiovascular-Medicine/QuadML.git
cd QuadML

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install the pinned dependencies
pip install --upgrade pip
# Windows / Linux:
pip install -r requirements.txt
# macOS (Apple Silicon): pip install -r requirements-mac.txt

# 4. (Optional) verify the installation
python src/verify_quadml_bundle.py
```

> **Note on versions.** `requirements.txt` pins the exact environment that defines QuadML v1.0, for example `scikit-learn==1.5.2` for compatibility with `scikit-survival==0.23.1`. On **macOS**, use `requirements-mac.txt` instead (`PyQt5==5.15.11`; see `mac_readme_source_deps_note()`). Please keep these pins: serialized pipelines reload only with compatible library versions.

---

## Quick start

```bash
python src/quadml_entry.py
```

1. **Choose a task**: Classification, Regression, Survival Analysis, or Clustering.
2. **File Selection**: load your CSV/Excel file, choose an output folder, and select the target (or duration and event for survival). Optionally add an external validation file.
3. **Configure each step** from the sidebar: Data Cleaning → Imputation → Scaling → Feature Selection → Dimensionality Reduction → Models → Data Splitting → Parameter Tuning.
4. **Start Procedure.** Progress, CPU, and memory use are shown live. Every finished configuration is saved immediately.
5. **Results**: filter, sort, and compare all configurations.
6. **Visualization**: per-pipeline diagnostics and cross-pipeline comparisons, each with a plain-language plot analyzer.
7. **Interpretability** (supervised tasks): explain any selected pipeline with SHAP, LIME, PDP/ICE, permutation importance, or SurvSHAP(t)/SurvLIME.

Each run is written to its own time-stamped subfolder of the chosen output directory.

---

## Methodological safeguards

QuadML is designed so that its defaults do not introduce common errors:

- **Leakage-safe pipelines.** Outlier cleaning (feature-level masking and sample-level row drops), imputation, scaling, feature selection, dimensionality reduction, and SMOTE are steps inside a single scikit-learn / imbalanced-learn `Pipeline`. They are refitted within every cross-validation fold, so validation, test, and external data never inform preprocessing.
- **Training-only fitting.** The optional correlation filter is fitted on the training partition after the train–test split. Outlier feature-level bounds are fitted inside each CV fold (and again on full train at final refit); test and external data are transformed with those fitted values. Sample-level detectors drop training rows only.
- **Frozen external validation.** External datasets are encoded with the training encoding, aligned to the training feature schema, and scored by the frozen pipelines without refitting.
- **Selection on cross-validation.** Hyperparameters are tuned by cross-validation within the training data only. The results table can be ranked by cross-validated scores rather than held-out metrics.
- **Censoring-aware survival evaluation.** Harrell's and Uno's C-index, time-dependent AUC, integrated Brier score, and calibration (mean calibration, calibration slope, ICI), with inverse-probability-of-censoring weights estimated on the training partition.
- **Transparency over automation.** QuadML does not pick a single winner for you. Every configuration, metric, and figure is exposed, and model selection remains an explicit, documented decision.

> ⚠️ **Good practice.** Selecting the best of thousands of pipelines is itself a source of optimism. Report the number of configurations compared, report cross-validated and test performance side by side, and fix the champion **before** looking at external results. QuadML cannot detect study-design flaws such as outcome-proxy features or inappropriate cohort definitions.

---

## Outputs and reproducibility

For every executed configuration, QuadML saves:

- the **fitted pipeline** (`.pkl`/`.joblib`; supervised tasks);
- a **JSON record** of the configuration, best hyperparameters, and metrics for every partition;
- **training/test feature tables** used for interpretation;
- **cached plot data**, so figures can be regenerated without retraining;
- **cluster assignments and profiles** (clustering);
- a consolidated **results table** (CSV), a run-level configuration record, an environment manifest, and an exportable **procedure report** (text or Word).

A fixed random seed is used for data splitting, cross-validation shuffling, randomized search, SMOTE, and the seeded estimators. Results are written atomically, so completed work survives interruptions and the results table can be **rebuilt from disk**.

> 🔒 Serialized pipelines are pickle files. Load them only from trusted sources.

---

## Project structure

```text
QuadML/
├── assets/                        # Icons and logos
├── src/
│   ├── quadml_entry.py            # Application entry point
│   ├── main_window.py             # Main window and workflow orchestration
│   ├── worker_main.py             # Headless worker processes
│   ├── shared/                    # Task-agnostic components
│   │   ├── data/                  #   Load, clean and encode the input table
│   │   ├── pipeline/              #   Imputation, scaling, feature selection steps
│   │   ├── search/                #   Search workers, parallelism, progress, failures
│   │   ├── results/               #   Metrics, labels and reports after a run
│   │   ├── interpretability/      #   SHAP, LIME, PDP/ICE sessions and plots
│   │   ├── plots/                 #   Charts and Plot Analyzer text
│   │   ├── gui/                   #   PyQt5 widgets for each step
│   │   └── app/                   #   Paths, logging, seed, macOS helpers, loaders
│   ├── classification/            # Models, search driver, metrics, plots, explanations
│   ├── regression/
│   ├── survival_analysis/
│   ├── clustering/
│   └── tests/                     # pytest suite
├── .github/workflows/             # Windows and macOS build pipelines (manual)
├── requirements.txt               # Pinned v1.0 environment (Windows / Linux)
├── requirements-mac.txt           # macOS pins (PyQt5==5.15.11)
├── LICENSE.md                     # CC BY-NC 4.0
└── README.md
```

---

## Running the tests

```bash
pip install pytest
pytest src/tests -q
```

The suite covers components such as data cleaning and encoding, metric computation, pipeline assembly, search grids, cross-validation ranking, and bootstrap intervals.

---

## Building the executables

The packaged applications are built with PyInstaller using the spec files in `src/`:

```bash
# Windows
pyinstaller src/QuadML.spec
# macOS
pyinstaller src/QuadML_mac.spec
```

- **Windows:** GitHub Actions → **Build Windows exe** (manual, or on a `vX.Y.Z` tag) builds `QuadML_Setup_<version>.exe` with the same `src/build_windows.ps1` used locally; tag builds attach the installer to the Release.
- **macOS:** GitHub Actions → **Build macOS app** is **manual** (`workflow_dispatch` on Apple Silicon). The zip is for smoke testing or attaching to [Releases](https://github.com/AI-in-Cardiovascular-Medicine/QuadML/releases); it is **not** an automatic notarized Mac release. See [`docs/getting-started/04-macos-notes.md`](docs/getting-started/04-macos-notes.md) (`mac_readme_build_blurb()`).

---

## Documentation

- 📖 **Online user guide:** [https://ai-in-cardiovascular-medicine.github.io/QuadML/](https://ai-in-cardiovascular-medicine.github.io/QuadML/) (MkDocs Material, published from `docs/` via GitHub Pages)
- 📁 **Source manuals:** [`docs/`](docs/) (Getting started, Classification, Regression, Survival, Clustering, Shared)
- Preview locally:

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

- 🎥 **Video tutorials:** https://www.youtube.com/@AI-CVM/videos
- 🧭 **In-app help:** every option has an ⓘ button, and every metric and plot has a plain-language explanation panel.

---

## Citation

If you use QuadML in your research, please cite:

```bibtex
@article{quadml2026,
  title   = {QuadML: A General-Purpose, Open-Source Executable Machine Learning Framework for Supervised and Unsupervised Learning},
  author  = {Mirzakhani, Hamed and Baj, Giovanni and Mohammadi Kazaj, Pooya, and Chaimae Bahou,
             Hashemi Gheinani, Ali and Gräni, Christoph and Shiri, Isaac},
  year    = {2026},
  note    = {}
}
```

---

## License

QuadML is released under the **[Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](LICENSE.md)** license.
It is free for academic and other **non-commercial** use with attribution. For commercial licensing, please [contact us](#contact).

---



## Acknowledgments

QuadML builds on outstanding open-source libraries, including
[scikit-learn](https://scikit-learn.org/), [scikit-survival](https://scikit-survival.readthedocs.io/), [lifelines](https://lifelines.readthedocs.io/), [pycox](https://github.com/havakv/pycox), [XGBoost](https://xgboost.ai/), [imbalanced-learn](https://imbalanced-learn.org/), [SHAP](https://github.com/shap/shap), [LIME](https://github.com/marcotcr/lime), [survshap](https://github.com/MI2DataLab/survshap), [genieclust](https://genieclust.gagolewski.com/), [HDBSCAN](https://hdbscan.readthedocs.io/), [UMAP](https://umap-learn.readthedocs.io/), [fancyimpute](https://github.com/iskandr/fancyimpute), [statsmodels](https://www.statsmodels.org/), [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/), and [PyQt5](https://riverbankcomputing.com/software/pyqt/).

<div align="center">
</div>
