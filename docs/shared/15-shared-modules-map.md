# Shared — modules map

Reference map from `src/shared/` (and closely related entry/main files) to user-facing behavior. Not every helper has its own left-nav page. Intended for maintainers and advanced users who need file ↔ UI mapping.

---

## Main window and entry

| File | Role |
|------|------|
| `src/main_window.py` | `MLPipelineGUI` — Welcome, nav, theme, File Selection, Cleaning, Correlation, Splitting, hosts Shared GUIs, Start/Stop wiring |
| `src/quadml_entry.py` | Process entry; `QUADML_ROLE` → GUI / search / worker (no Qt import before role check) |

---

## Step GUIs (left-nav widgets)

| File | Left-nav / UI |
|------|----------------|
| `imputation_gui.py` | Imputation |
| `scaling_gui.py` | Scaling |
| `feature_selection_gui.py` | Feature Selection |
| `hyperparameter_tuning_gui.py` | Parameter Tuning / Search Settings, Start/Stop chrome, Procedure Report / Rebuild entry points |
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
| `parallel_config.py` | CPU/RAM % → outer/inner jobs, BLAS limits, adaptive throttle |
| `outer_pool.py` | Outer combination worker pool |
| `worker_entry.py` | Worker-side entry helpers |
| `ml_search_subprocess.py` | Search child process orchestration |
| `search_progress.py` | Progress / cancel files for the GUI |
| `search_failures.py` | Failure recording / surfacing |
| `resource_monitor.py` | CPU/RAM sampling during a run |
| `pipeline_cache.py` | Pipeline caching helpers |
| `bootstrap_ci.py` | Bootstrap CI enablement rules by mode |

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
| `procedure_report.py` | Collect / format / save procedure reports |
| `run_config_report.py` | Run configuration reporting helpers |
| `selected_configuration_summary.py` | Selected-configuration tree / summary |
| `select_all_toggle.py` | Select-all bars on method pages |
| `gui_layout.py` | Shared layout constants / helpers |
| `gui_theme.py` | Light/dark theme tokens |
| `app_paths.py` | Application path helpers |
| `survival_loader.py` | Lazy / guarded survival stack loading |
| `clustering_loader.py` | Lazy / guarded clustering stack loading |

---

## Mode packages (not under shared/)

Classifiers, Regressors, Survival Models, Clustering Models, Descriptive Analysis, and mode-specific SEARCH modules live under the mode packages. Shared docs link to mode manuals for those pages.
