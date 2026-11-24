## Search controls

1. **Search Budget:** Fast / Balanced / Thorough scales search richness (for example Random Search iterations and suggested CV folds). It does **not** remove methods you already checked.
2. **Search algorithm:** **Grid Search** or **Random Search** when shown (Random Search exposes **Iterations**).
3. **Cross-validation** method and splits when the mode uses CV (Clustering omits CV fold controls on Search Settings).

For a first run, **Fast** or **Balanced** is enough.

---

## Bootstrap CIs and resources

4. Optional **Bootstrap CIs** (Classification / Regression / Survival) 95% percentile intervals on scalar metrics. Enable and re-run; evaluation resamples without refitting pipelines. Not shown in Clustering.
5. **Resource Usage:** CPU % and RAM % (defaults often 50 / 50).

---

## Configuration tree and actions

6. Review the **selected configuration** tree (product of checked stages × models).
7. **Start Procedure** prepare data, launch search, write results.
8. **Stop Procedure** cancel; partial combo results may remain.
9. Other actions as labeled: **Reset Configuration**, **Export Procedure Report**, **Rebuild Results** (full steps in Troubleshooting).

---

## What is written to disk

In the dated run folder (typical):

- `Final_Results.csv`
- `combo_results/` JSON to let you rebuild final_results file when procedure crashes
- Fitted pipelines (`.pkl`), prepared data, plot caches
- Procedure report if you export it
