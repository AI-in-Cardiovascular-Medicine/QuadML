# Clustering — Data cleaning

Data cleaning removes or corrects problematic values before clustering. It is applied when you click **Start Procedure** and offers:

- **Outlier detection, feature-level:** single extreme values are set to missing, then filled in by Imputation
- **Exact duplicate rows:** identical samples are removed (on by default)
- **Missing / outlier threshold:** features or samples with too many missing or outlier values are removed

Sample-level outlier methods and Correlation Analysis are hidden in Clustering.

![Data Cleaning](../assets/cluster/4.png)

--8<-- "_snippets/data-cleaning-feature-level.md"

![Feature-level cleaning methods](../assets/cluster/5.png)

**More Configs…** opens thresholds for the selected feature-level method (for example Z-Score):

![More Configs for feature-level methods](../assets/cluster/6.png)

**Exact Duplicate Rows** removes identical samples (on by default):

![Exact Duplicate Rows](../assets/cluster/7.png)

**Missing / Outlier Threshold** removes features or samples with too many missing or outlier values:

![Missing / Outlier Threshold](../assets/cluster/8.png)

## Common mistakes

- Expecting the preview to change before **Start Procedure**
- Feature-level cleaning without Imputation for new missing values
- Looking for Isolation Forest / LOF / Correlation Analysis on this page (hidden in Clustering)
