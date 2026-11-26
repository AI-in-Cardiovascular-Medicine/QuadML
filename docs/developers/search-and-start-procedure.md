# Search and Start Procedure

Technical detail for maintainers. User-facing Parameter Tuning / Search Settings pages stay short; this page covers search controls, disk layout, and the Start/Stop sequence.

Related code: `hyperparameter_tuning_gui.py`, `parallel_config.py`, `ml_search_subprocess.py`, `search_progress.py`, `bootstrap_ci.py` — see [Code structure](code-structure.md).

---

## Search controls

1. **Search Budget:** Fast / Balanced / Thorough scales search richness (for example Random Search iterations and suggested CV folds). It does **not** remove methods already checked.
2. **Search algorithm:** **Grid Search** or **Random Search** when shown (Random Search exposes **Iterations**).
3. **Cross-validation** method and splits when the mode uses CV (Clustering omits CV fold controls on Search Settings).
4. Optional **Bootstrap CIs** (Classification / Regression / Survival): 95% percentile intervals on scalar metrics. Enable and re-run; evaluation resamples without refitting pipelines. Not shown in Clustering.
5. **Resource Usage:** CPU % and RAM % (defaults often 50 / 50). CPU budgets parallel work (outer combinations × inner CV); RAM caps how many outer workers fit.
6. Review the **selected configuration** tree (product of checked stages × models).
7. Actions: **Start Procedure**, **Stop Procedure**, **Reset Configuration**, **Export Procedure Report**, **Rebuild Results** (also see Troubleshooting).

---

## What is written to disk

In the dated run folder (typical):

- `Final_Results.csv`
- `combo_results/` JSON used to rebuild `Final_Results.csv` when a procedure crashes
- Fitted pipelines (`.pkl`), prepared data, plot caches
- Procedure report if exported

---

## Start Procedure — sequence

1. **Guards:** not already running; input file exists; split rules OK (supervised); Output Directory set; data loaded from File Selection; survival horizon confirmations when required.
2. Creates a **new folder** under the Output Directory parent.
3. Collects GUI configuration (all checked stages and search settings).
4. Starts **resource monitoring** (CPU/RAM sampling).
5. Prepares data on the main path, then launches the search so **Stop** can cancel the process tree.
6. Updates progress UI; writes `Final_Results.csv` and combo JSON as combinations finish.

---

## Stop Procedure and Rebuild

- **Stop** cancels the run; partial `combo_results/` may remain.
- **Rebuild Results** reconstructs `Final_Results.csv` from finished `combo_results/*.json` when possible.
- Prefer **Stop Procedure** over closing the app.

---

## One search at a time

If a pipeline is already running in another mode, **Start Procedure** shows a **Pipeline Running** warning. Switch to that mode to monitor, or **Stop** before starting elsewhere.
