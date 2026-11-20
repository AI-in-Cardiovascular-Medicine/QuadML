# Shared — Introduction

**Shared** documents the **cross-mode** surfaces of QuadML: the main application shell and the reusable left-nav steps that Classification, Regression, Survival Analysis, and Clustering all use (or adapt). Mode-specific wording — Label vs Target, Decision Threshold, imbalance, LDA, duration/event, Search Settings vs Parameter Tuning — lives in each mode folder. Use those pages when you are already inside one task.

Most preparation, search, results, plot, and explanation widgets live under `src/shared/`. The main window (`src/main_window.py`) owns Welcome, mode switching, File Selection, Data Cleaning (plus Correlation Analysis where shown), Data Splitting, theme, and the wiring that starts and stops a search. Everything runs locally — no data is uploaded.

![QuadML Welcome](../assets/getting-started/welcome.png)

---

## Ownership map (user-facing)

| Surface | Owned mainly by |
|---------|-----------------|
| Welcome, left nav, Back/Next, light/dark theme | `main_window.py` |
| File Selection, Data Cleaning, Correlation, Data Splitting | `main_window.py` (+ Shared data helpers) |
| Imputation, Scaling, Feature Selection, Parameter Tuning / Search Settings, Results, Visualization, Interpretability | `shared/*GUI.py` |
| Mode model pages (Classifiers, Regressors, Survival Models, Clustering Models, Descriptive Analysis, …) | Mode packages + `main_window` hosts |
| Abbreviations on Results / plots / filenames | `shared/results/abbreviations.py` |
| Procedure Report export | `shared/results/procedure_report.py` (+ Parameter Tuning UI) |
| CPU/RAM → parallel jobs | `shared/search/parallel_config.py` + Resource Usage UI |
| Process roles (GUI / search / worker) | `quadml_entry.py` |

---

## Four modes, one shell

Expand **Classification**, **Regression**, **Survival Analysis**, or **Clustering** on the left. Each mode keeps its own widget state when you switch. Only one pipeline search may run at a time; if a search is active in another mode, **Start Procedure** warns you to switch back or **Stop** first.

---

## Shared pipeline order (conceptual)

Cleaning → Imputation → Scaling → Feature Selection → (Dimensionality Reduction where available) → Model → evaluate / results / plots / interpretability.

Classification, Regression, Clustering, and Survival all insert Dimensionality Reduction in the combination product (Survival has no LDA; KM / Nelson–Aalen skip DR). Survival also adds duration/event roles and Descriptive Analysis. Classification adds Decision Threshold and Imbalance Handling. Clustering uses **Search Settings** instead of Data Splitting + Parameter Tuning and has no Interpretability step.

---

## Suggested reading order

1. [Application shell](01-application-shell.md)
2. Shared steps in left-nav order (File Selection → Interpretability)
3. [Start, Stop, and resources](13-start-stop-and-resources.md)
4. [Outputs, abbreviations, and reports](14-outputs-abbreviations-reports.md)
5. [Shared modules map](15-shared-modules-map.md) when you need file ↔ UI mapping

For a first successful run in one mode, use that mode’s walkthrough instead — or the [cross-mode walkthrough](walkthrough.md) here for the shared path.
