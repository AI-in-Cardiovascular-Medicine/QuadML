# QuadML user documentation

**QuadML** is a point-and-click machine-learning framework for tabular data. You choose cleaning, imputation, scaling, feature selection, dimensionality reduction, and models; QuadML searches the combinations you enable, then reports metrics, plots, and explanations. Everything runs **locally** — no data is uploaded.

**App version:** 1.0

Button and method names in these pages match the GUI. In-app **"i"** buttons, **Metric Explanations**, and **Plot Explanations** remain the source for full on-screen definitions.

![QuadML Welcome](assets/getting-started/welcome.png)

---

## Start here

| Goal | Go to |
|------|--------|
| Install, first launch, data prep, troubleshooting | [Getting started](getting-started/index.md) · [Quick start walkthrough](getting-started/walkthrough.md) |
| First successful run in one task | That mode’s **walkthrough** (links below) |
| Controls shared across modes (Welcome, Start/Stop, outputs) | [Shared](shared/index.md) |
| Authors, citation, license | [About](getting-started/10-about.md) |

---

## Modes

Each mode follows the left-nav step order in the app. Every mode section has an **Introduction**, step pages, and an end-to-end **walkthrough**.

| Mode | Outcome | Start |
|------|---------|--------|
| [Classification](classification/index.md) | Discrete classes (binary / multi-class) | [Introduction](classification/00-introduction.md) · [Walkthrough](classification/walkthrough.md) |
| [Regression](regression/index.md) | Continuous numeric target | [Introduction](regression/00-introduction.md) · [Walkthrough](regression/walkthrough.md) |
| [Survival Analysis](survival/index.md) | Duration + event / censor | [Introduction](survival/00-introduction.md) · [Walkthrough](survival/walkthrough.md) |
| [Clustering](clustering/index.md) | Unlabeled groups | [Introduction](clustering/00-introduction.md) · [Walkthrough](clustering/walkthrough.md) |

**Quick differences**

- **Classification** — Label Column, Task Type, Decision Threshold (binary), Imbalance Handling, LDA available
- **Regression** — numeric Target (Label Column in the GUI); error / fit metrics (MAE, RMSE, R², …); no class imbalance / LDA
- **Survival** — Duration + Event, Eval. Horizons, Descriptive Analysis (KM / Nelson–Aalen), SurvSHAP; calibrate before ranking on C-index alone
- **Clustering** — optional Benchmark Label only; **Search Settings** (no Data Splitting / Parameter Tuning); no Interpretability page

---

## Shared

Cross-mode pages for the application shell and reusable steps under `src/shared/` (File Selection through Interpretability, Start/Stop, abbreviations, procedure reports):

→ **[Shared documentation](shared/index.md)** · [Cross-mode walkthrough](shared/walkthrough.md) · [Introduction](shared/00-introduction.md)

Use Shared when a control appears in more than one mode, or when you need Welcome, theme, Start/Stop, or run-folder outputs. Use a mode manual for outcome-specific metrics, models, and plots.

---

## Typical workflow

1. Install and launch — [Getting started](getting-started/index.md)
2. Prepare a `.csv` / `.xlsx` — [Prepare the data](getting-started/07-prepare-the-data.md)
3. Open one mode → **File Selection** (roles + **Output Directory**)
4. Keep preprocessing small → pick a few models → **Start Procedure**
5. Read **Results** → **Visualization** → **Interpretability** (where available)

Each **Start Procedure** writes a dated folder `YYYY-MM-DD_HH-MM-SS` under your Output Directory, including `Final_Results.csv`.
