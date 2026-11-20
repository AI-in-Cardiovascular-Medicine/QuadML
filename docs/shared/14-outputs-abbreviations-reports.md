# Shared — Outputs, abbreviations, and reports

How QuadML names pipelines on screen, on disk, and in exported reports.

---

## Abbreviation layers

| Layer | Example | Where |
|-------|---------|--------|
| Display (Results, plots) | `IQR \| SimpImp(med) \| StdSc \| SKB \| LR` | GUI tables and figures |
| GUI method cards | `Interquartile Range (IQR)` | Configuration pages |
| Filesystem / compact IDs | `IQR_SimpImp_med_StdSc_SKB_LR` | Plot stems, CSV/PKL names |

Keep-all stages are shown explicitly as `No cleaning`, `No scaling`, `No selection`, `No DR` (display) or `None` in compact IDs — not silently omitted.

Order follows pipeline implementation: Cleaning → Imputation → Scaling → FS → (DR) → Model.

---

## Typical run folder contents

Under `Output Directory / <dated run>/` (names may vary slightly by mode):

- `Final_Results.csv` — one row per combination
- `combo_results/*.json` — per-combination payloads for rebuild
- Fitted pipeline `.pkl` files
- Prepared / intermediate data as written by the search
- Plot caches used by Visualization
- Optional sidecars (for example class-balance report when imbalance reporting ran; Survival / Clustering extras as applicable)

---

## Procedure Report

1. On Parameter Tuning / Search Settings, click **Export Procedure Report**.
2. QuadML snapshots the current GUI configuration (files, roles, cleaning, correlation, imputation, scaling, FS, models, split, search/CV/budget, imbalance, bootstrap, CPU/RAM / n_jobs).
3. Save as text and/or DOCX as the dialog offers.
4. Clustering omits correlation and CV sections; survival adds duration/event; bootstrap sections follow mode rules.

---

## Rebuild Results

If a run was interrupted, **Rebuild Results** rebuilds `Final_Results.csv` from `combo_results/*.json` in the search folder when enough JSON remains.

---

## Common mistakes

- Comparing abbreviated labels across modes without checking whether DR is in the string
- Editing `Final_Results.csv` by hand then expecting Rebuild to preserve those edits
- Confusing display labels (`|` separators) with filesystem stems (`_` separators)
