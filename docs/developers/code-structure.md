# Code structure

Maintainer map of the application tree: process roles, main GUI host, and `src/shared/` backends. User-facing Pipeline / Results pages do not list these paths.

The public **QuadML** GitHub repository is **documentation only**. Application source access is arranged separately — see [Contributing](contributing.md).

---

## Process roles

Entry: `src/quadml_entry.py`. Environment variable **`QUADML_ROLE`** selects the process before any Qt import:

| Role | Purpose |
|------|---------|
| **gui** (default) | Main window (`main_window.main()`); hosts left-nav steps and Start/Stop |
| **search** | ML search child (no `QApplication`); runs the combination search |
| **worker** | Outer combination / pool client for parallel work |

Frozen builds ship companion binaries (`QuadML` / `QuadML.exe` and `QuadML_Worker` / `QuadML_Worker.exe`) so relaunches keep the same role check. Search/worker children force a non-Qt matplotlib backend.

---

## Main window and entry

| File | Role |
|------|------|
| `src/main_window.py` | `MLPipelineGUI` — Welcome, nav, theme, File Selection, Cleaning, Splitting, hosts Shared GUIs, Start/Stop wiring |
| `src/quadml_entry.py` | Process entry; `QUADML_ROLE` → GUI / search / worker |

---

## Step GUIs (left-nav widgets)

| File | Left-nav / UI |
|------|----------------|
| `imputation_gui.py` | Imputation |
| `scaling_gui.py` | Scaling |
| `feature_selection_gui.py` | Feature Selection |
| `hyperparameter_tuning_gui.py` | Parameter Tuning / Search Settings, Start/Stop, Procedure Report / Rebuild |
| `results_gui.py` | Results |
| `visualization_gui.py` | Visualization |
| `interpretability_gui.py` | Interpretability |

---

## Data and preprocessing backends

| File | Role |
|------|------|
| `data_reading.py` | Load datasets |
| `data_clean.py` | Cleaning execution |
| `data_identifier.py` | Column / type identification |
| `imputation.py` | Imputation execution / grids |
| `scaling.py` | Scaling execution / grids |
| `feature_selector.py` | Feature selection backends |
| `missing_values.py` | Missing-value helpers |
| `categorical_preprocessing.py` | Categorical encoding helpers |
| `correlation_methods.py` | Correlation filter methods |
| `sample_id.py` | Record ID / no-ID option |

---

## Search, parallel, progress

| File | Role |
|------|------|
| `parallel_config.py` | CPU/RAM % → jobs, BLAS limits, adaptive throttle |
| `outer_pool.py` | Outer combination worker pool |
| `worker_entry.py` | Worker-side entry helpers |
| `ml_search_subprocess.py` | Search child process orchestration |
| `search_progress.py` | Progress / cancel files for the GUI |
| `search_failures.py` | Failure recording / surfacing |
| `resource_monitor.py` | CPU/RAM sampling during a run |
| `pipeline_cache.py` | Pipeline caching helpers |
| `bootstrap_ci.py` | Bootstrap CI enablement by mode |

---

## Results, plots, interpretability

| File | Role |
|------|------|
| `results_format.py` | Result table formatting |
| `combo_results_store.py` | `combo_results` JSON store / rebuild |
| `abbreviations.py` | Display / GUI / filesystem abbreviations |
| `plotting.py` | Plot generation |
| `plot_analyzer.py` | Plot analysis helpers |
| `interpretability.py` | Interpretability core |
| `interpretability_pipeline.py` | Explanation pipeline |
| `interpretability_artifacts.py` | Saved explanation artifacts |
| `interpretability_messages.py` | User-facing interpretability messages |
| `interpretability_plot_style.py` | Plot styling |
| `interpretability_plot_analyzer.py` | Interpretability plot analysis |

---

## Reports, layout, theme, loaders

| File | Role |
|------|------|
| `procedure_report.py` | Procedure reports |
| `run_config_report.py` | Run configuration helpers |
| `selected_configuration_summary.py` | Selected-configuration tree / summary |
| `select_all_toggle.py` | Select-all bars on method pages |
| `gui_layout.py` / `gui_theme.py` | Layout constants / light–dark theme |
| `app_paths.py` | Application path helpers |
| `survival_loader.py` / `clustering_loader.py` | Lazy / guarded mode stack loading |

---

## Mode packages

Classifiers, Regressors, Survival Models, Clustering Models, Descriptive Analysis, and mode-specific SEARCH modules live under the **mode packages** (not under `shared/`). Shared step GUIs above are reused across modes.

See also: [Python requirements](python-requirements.md) · [Build and package](build-and-package.md)
