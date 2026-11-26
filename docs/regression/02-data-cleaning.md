# Regression — Data cleaning

Data cleaning removes or corrects problematic values before modeling. It is applied when you click **Start Procedure** and offers:

- **Outlier detection, feature-level:** single extreme values are set to missing, then filled in by Imputation
- **Outlier detection, sample-level:** whole samples with unusual values overall are removed
- **Exact duplicate rows:** identical samples are removed (on by default)
- **Missing / outlier threshold:** features or samples with too many missing or outlier values are removed
- **Correlation analysis:** remove one feature from each highly correlated pair

![Data Cleaning](../assets/reg/4.png)

--8<-- "_snippets/data-cleaning-feature-level.md"

![Feature-level cleaning methods](../assets/reg/5.png)

**More Configs…** opens thresholds for the selected feature-level method (for example Modified Z-Score):

![More Configs for feature-level methods](../assets/reg/6.png)

--8<-- "_snippets/data-cleaning-sample-level.md"

Sample-level methods appear in the same Data Cleaning panel (below Feature-level):

![Sample-level cleaning methods](../assets/reg/5.png)

**Exact Duplicate Rows** removes identical samples (on by default):

![Exact Duplicate Rows](../assets/reg/7.png)

**Correlation Analysis** finds highly correlated feature pairs (Pearson or Spearman) and keeps the member of each pair that is more associated with the continuous target:

![Correlation Analysis](../assets/reg/8.png)

**Missing / Outlier Threshold** removes features or samples with too many missing or outlier values:

![Missing / Outlier Threshold](../assets/reg/9.png)

## Common mistakes

- Expecting the preview to change before **Start Procedure**
- Feature-level cleaning without Imputation for new missing values
- Low correlation thresholds that drop many useful features
