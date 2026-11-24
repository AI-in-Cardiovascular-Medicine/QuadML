## Default

An internal **Train / Test** split of the uploaded file, often **80% / 20%**. Leave **Train on all data (evaluate on External only)** unchecked for a normal first run.

Cross-validation during Parameter Tuning uses folds **inside Train**; the Test split is held out for reporting.

---

## What to click

1. Set Train / Test percentages if you do not want 80/20 (Train is clamped so Test stays at least 1%).
2. Leave **Train on all data** **unchecked** unless you have External Test Data and intend to fit on 100% of the main file.

### When “Train on all data” is checked

- There is **no** internal Test split
- **External** is the only unseen set
- Results cards pair **Train** with **External**
- Do **not** treat Train scores as generalization
- An **External Test Data** file on File Selection is **required** (compatible features and the same outcome roles)

Optional External **without** the checkbox: you still have Train/Test, and External is scored as a third split.

---

## Validation on Start Procedure

**Start Procedure** rejects invalid split setups (for example Train on all without a usable external file). Fix File Selection / Data Splitting, then start again.

---

## What is written to disk

Split membership and prepared Train/Test (and External) datasets live in the dated run folder. Results center on **`Final_Results.csv`**.
