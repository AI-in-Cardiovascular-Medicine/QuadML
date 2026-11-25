# Survival Analysis — Data cleaning

Choose how QuadML detects and handles outliers before modeling. Feature-level methods (IQR, Z-Score, Modified Z-Score) mask extreme cells as missing so Imputation can fill them later; sample-level methods (Isolation Forest, LOF, DBSCAN, One-Class SVM) drop entire outlier rows. You can also enable exact-duplicate removal, missing/outlier row thresholds, and Correlation Analysis. Selecting no method card means **None** (baseline hygiene only). Cleaning is applied at **Start Procedure**, not when you change a card. After sample-level drops, confirm that enough events and censoring remain for reliable survival estimates.

![Data Cleaning](../assets/sa/6.png)

--8<-- "_snippets/data-cleaning.md"

Feature-level methods mask outlier cells to NaN (filled later in Imputation):

![Feature-level cleaning methods](../assets/sa/7.png)

Sample-level methods drop entire outlier rows:

![Sample-level cleaning methods](../assets/sa/8.png)

## Common mistakes

- Expecting the preview to change before **Start Procedure**
- Feature-level cleaning without Imputation for new NaNs
- Low correlation thresholds that drop many useful features
