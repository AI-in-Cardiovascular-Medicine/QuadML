# Shared — Data Splitting

**Where**: Supervised modes → **Data Splitting** (Classification, Regression, Survival). Clustering has **no** Train/Test split — follow [Clustering — Search Settings](../clustering/08-search-settings.md).

Set the Train percentage (Test is auto-calculated). Optionally **Train on all data** and evaluate on **External Test Data** from File Selection.

---

## What to click

1. Set **Train Data (%)** — **Test Data** updates so totals stay 100% (Train is clamped so Test stays at least 1%).
2. Leave **Train on all data (evaluate on External only)** unchecked for a normal internal Train/Test split.
3. If you check **Train on all data**:
   - There is no internal Test split; External is the only unseen set.
   - Provide **External Test Data** on File Selection (same outcome columns and compatible features).
4. Read the on-page note and hint label for the current checkbox state.

Optional External **without** the checkbox: you still have Train/Test, and External is scored as a third split.

Classification may use stratified splitting by class; Regression and Survival do not stratify by class labels (Survival CV can still use event-aware folds on Parameter Tuning).

---

## Validation on Start Procedure

**Start Procedure** rejects invalid split setups (for example Train on all without a usable external file when the mode requires it). Fix File Selection / Data Splitting, then start again.

---

## Common mistakes

- Train on all data without browsing External Test Data
- Extremely small test percentages on tiny datasets
- Comparing Test metrics from a normal split with External metrics from a train-on-all run as if they were the same design
- Looking for Data Splitting in Clustering

---

## Mode manuals

- [Classification — Data Splitting](../classification/08-data-splitting.md)
- [Regression — Data Splitting](../regression/08-data-splitting.md)
- [Survival — Data Splitting](../survival/09-data-splitting.md)
