# Clustering — File Selection

**Where**: Clustering → **File Selection**

**Attention**: This is the first step. Nothing is written to the run folder until **Start Procedure** on Search Settings.

![the Clustering File Selection page](../assets/cluster/2.png)

## What you need

- A file with **.csv** or **.xlsx** format (first row = column names; mostly numeric features work best)
- A writable **Output Directory** (parent folder; each run creates a dated subfolder `YYYY-MM-DD_HH-MM-SS`)
- No target column is required

See also [Prepare the data](../getting-started/07-prepare-the-data.md).

---

## What to click

### Input and Output Directory

1. **Select File → Browse** — choose the main dataset (`Select .xlsx or .csv file`).
2. **Output Directory → Browse** — choose a parent folder (`Parent folder — each run saves to a dated subfolder`).

**External Test Data** is not shown in Clustering. Clustering never reads a second file. “External” metrics (ARI / NMI / FMI) compare clusters to an optional **Benchmark Label** in the same dataset.

### Benchmark Label

3. **Benchmark Label** (optional) — known class column for benchmark datasets. Used only to compute Adjusted Rand Index (ARI), Normalized Mutual Information (NMI), and Fowlkes–Mallows Index (FMI) after clustering. It is **not** used for training or for ranking pipelines. Choose **(None)** to skip.

**Auto-Detect** suggests a column only when the header looks explicitly label-like (for example exact `label` / `class`, or a suffix such as `true_label`). Covariates whose names merely contain tokens like group, class, or sex are not auto-picked; leave **(None)** if nothing matches.

There is **no ID Column** picker in Clustering. Assignments still carry stable sample identifiers written by the pipeline (and kept after cleaning drops rows).

### Column Removal and helpers

4. **Column Removal** — pick columns to exclude from modeling (**Add to list** / **Unselect**): IDs, text, or unused columns (including a benchmark column you do not want as a feature — when Auto-Detect picks a label, that column is excluded from features). Columns in the removal list are dropped when you start the procedure, not merely by listing them.
5. **Data Description** — after load, shows a pandas-style summary; can export CSV/Excel.
6. **Clear** — clears selected files and Output Directory so you can choose new ones.

![Benchmark Label, Column Removal, and helpers](../assets/cluster/3.png)

---

## What is written to disk

Nothing yet. The dated run folder is created when you click **Start Procedure**.

---

## Common mistakes

- Starting without an **Output Directory**
- Treating **Benchmark Label** as a training target
- Expecting External Test Data or an ID Column row (they are hidden in Clustering)
- Leaving ID / text columns in as features instead of using **Column Removal**
