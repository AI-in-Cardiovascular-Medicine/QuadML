# Shared — Parameter Tuning / Search Settings

**Where**:

- Classification / Regression / Survival → **Parameter Tuning**
- Clustering → **Search Settings**

Choose **how** QuadML searches the combinations you selected, set resources, review the configuration tree, then **Start Procedure**.

---

## What to click (shared)

### Search controls

1. **Search Budget:** Fast / Balanced / Thorough — scales Random Search `n_iter` and suggested CV folds (or Clustering’s discrete/continuous search richness). It does **not** remove methods you already checked.
2. **Search algorithm:** **Grid Search** or **Random Search** when shown (Random Search exposes **Iterations** / `n_iter`).
3. **Cross-validation** method and splits when the mode uses CV. Clustering omits CV fold controls — follow Clustering Search Settings.

For a first run, **Fast** or **Balanced** is enough.

### Bootstrap CIs and resources

4. Optional **Bootstrap CIs** on Classification / Regression / Survival — 95% percentile intervals on scalar metrics. Enable and re-run; evaluation resamples without refitting pipelines (see in-app **?**). Not shown in Clustering.
5. **Resource Usage:** CPU % and RAM % (defaults often 50 / 50) — drives outer/inner parallel jobs. Details: [Start, Stop, and resources](13-start-stop-and-resources.md).

### Configuration tree and actions

6. Review the **selected configuration** tree (product of checked stages × models).
7. **Start Procedure** — collect config, prepare data, launch search child, write results.
8. **Stop Procedure** — cancel; partial `combo_results` may remain.
9. If the procedure stops or crashes mid-run, click **Rebuild Results** to rebuild `Final_Results.csv` from finished `combo_results/*.json` when possible.
10. Other actions as labeled: **Reset Configuration**, **Export Procedure Report**, **Rebuild Results**.

---

## Mode-only controls (summary)

| Control | Modes |
|---------|--------|
| Imbalance Handling (+ SMOTE) | Classification |
| Bootstrap CIs | Classification, Regression, Survival (not Clustering) |
| Stratified / event-aware CV options | Classification (class); Survival (event-aware) |
| Page title **Search Settings** | Clustering |
| Survival horizon confirmations | Survival (on start) |

---

## What is written to disk

In the dated run folder (typical):

- `Final_Results.csv`
- `combo_results/` JSON (Rebuild Results can recover the CSV)
- Fitted pipelines (`.pkl`), prepared data, plot caches
- Optional class-balance / mode-specific sidecars
- Procedure report if you export it

See also [Outputs, abbreviations, and reports](14-outputs-abbreviations-reports.md).

---

## Common mistakes

- Starting with every method checked — combination count is a product
- Ignoring Resource Usage on large searches
- Changing File Selection roles after configuring without re-checking the tree
- Looking for Imbalance Handling or Bootstrap CIs in Clustering

---

## Mode manuals

- [Classification — Parameter Tuning](../classification/09-parameter-tuning.md)
- [Regression — Parameter Tuning](../regression/09-parameter-tuning.md)
- [Survival — Parameter Tuning](../survival/10-parameter-tuning.md)
- [Clustering — Search Settings](../clustering/08-search-settings.md)
