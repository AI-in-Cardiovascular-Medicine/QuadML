# Clustering — Tutorial

End-to-end click path for a first Clustering run. Keep the search small.

---

## 1. Start

1. Open QuadML → **Clustering** → **File Selection**.
2. **Select File → Browse** — mostly numeric `.csv` / `.xlsx`.
3. **Output Directory → Browse** — writable parent folder.
4. Leave **Benchmark Label** on **(None)** unless you want ARI / NMI / FMI only.
5. Optional: **Column Removal** (no External file or ID Column in Clustering).

![File Selection](../assets/cluster/2.png)

---

## 2. Preprocess

| Step | Choice |
|------|--------|
| Data Cleaning | **None** |
| Imputation | **Simple Imputation** |
| Scaling | **Standard Scaler** |
| Feature Selection | **None** |
| Dimensionality Reduction | **None** |

---

## 3. Models

1. **Clustering Models:** **K-Means** only.
2. **Number of clusters:** **Auto**.

---

## 4. Run

1. **Search Settings:** **Fast**, CPU/RAM 50/50.
2. Review the tree → **Start Procedure** → wait (or **Stop** to cancel).

---

## 5. Read output

1. **Metrics:** Silhouette with CH / DB; check cluster sizes.
2. **Visualization:** Feature Space or Reduced Components; Cluster Profile Heatmap for segments.

There is **no** Interpretability step in Clustering.

Success: `Final_Results.csv` under `Your Folder\YYYY-MM-DD_HH-MM-SS\`.
