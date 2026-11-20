# Regression — Data Splitting

**Where**: Regression → **Data Splitting**

**Data Splitting** decides how the main dataset is divided into Train and Test (and whether an optional External file is the only hold-out). Cross-validation during Parameter Tuning uses folds **inside Train**; the Test split is held out for reporting. Unlike Classification, the split is **not** stratified by class labels — the outcome is a continuous **Target Column**.

![the Regression Data Splitting page](../assets/reg/23.png)

---

## Default

An internal **Train / Test** split of the uploaded file, **80% / 20%**. Leave **Train on all data (evaluate on External only)** unchecked for a normal first run.

---

## What to click

1. Set Train / Test percentages if you do not want 80/20 (Train is clamped so Test stays at least 1%).
2. Leave **Train on all data (evaluate on External only)** **unchecked** unless you have a labeled External file and you intend to fit on 100% of the main file.

### When “Train on all data” is checked

- There is **no** internal Test split
- **External** is the only unseen set
- Results cards pair **Train** with **External**
- Ranking uses External metrics
- Do **not** treat Train scores as generalization
- A labeled **External Test Data** file on File Selection is **required** (same numeric target column and compatible features)

Optional External **without** the checkbox: you still have Train/Test, and External is scored as a third split.

![the Train on all data checkbox and split percentage controls](../assets/reg/24.png)

---

## What is written to disk

Split membership and prepared Train/Test (and External) datasets live in the dated run folder. Results always center on **`Final_Results.csv`** after the search.

---

## Common mistakes

- Checking **Train on all data** without External — **Start Procedure** will refuse
- Comparing Test metrics from a normal split with External metrics from a train-on-all run as if they were the same design
- Expecting Classification-style stratified splitting by class (not used in Regression)
