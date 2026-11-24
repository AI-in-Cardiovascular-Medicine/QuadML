# Classification — Data cleaning

**Where**: Classification → **Data Cleaning**

Optional outlier handling and hygiene before modeling. Applied at **Start Procedure**.

![Data Cleaning](../assets/class/Class09.png)

--8<-- "_snippets/data-cleaning.md"

Feature-level methods mask outlier cells to NaN (filled later in Imputation):

![Feature-level cleaning methods](../assets/class/Class10.png)

**More Configs…** opens thresholds for the selected feature-level method:

![More Configs for feature-level methods](../assets/class/Class11.png)

Sample-level methods drop entire outlier rows:

![Sample-level cleaning methods](../assets/class/Class13.png)

Exact duplicate rows (Active by default):

![Exact Duplicate Rows](../assets/class/Class14.png)

Correlation Analysis (Pearson / Spearman + threshold):

![Correlation Analysis](../assets/class/Class15.png)

Missing / Outlier Threshold for columns and rows:

![Missing / Outlier Threshold](../assets/class/Class17.png)

## Common mistakes

- Expecting the preview to change before **Start Procedure**
- Feature-level cleaning without Imputation for new NaNs
- Low correlation thresholds that drop many useful features
