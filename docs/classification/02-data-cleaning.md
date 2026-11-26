# Classification — Data cleaning

Data cleaning removes or corrects problematic values before modeling. It is applied when you click **Start Procedure** and offers:

- **Outlier detection, feature-level:** single extreme values are set to missing, then filled in by Imputation
- **Outlier detection, sample-level:** whole samples with unusual values overall are removed
- **Exact duplicate rows:** identical samples are removed (on by default)
- **Missing / outlier threshold:** features or samples with too many missing or outlier values are removed
- **Correlation analysis:** remove one feature from each highly correlated pair

![Data Cleaning](../assets/class/Class09.png)

--8<-- "_snippets/data-cleaning-feature-level.md"

![Feature-level cleaning methods](../assets/class/Class10.png)

**More Configs…** opens thresholds for the selected feature-level method:

![More Configs for feature-level methods](../assets/class/Class11.png)

--8<-- "_snippets/data-cleaning-sample-level.md"

![Sample-level cleaning methods](../assets/class/Class13.png)

**Exact Duplicate Rows** removes identical samples (on by default):

![Exact Duplicate Rows](../assets/class/Class14.png)

**Correlation Analysis** (Pearson / Spearman + threshold) removes one feature from each highly correlated pair:

![Correlation Analysis](../assets/class/Class15.png)

**Missing / Outlier Threshold** removes features or samples with too many missing or outlier values:

![Missing / Outlier Threshold](../assets/class/Class17.png)

## Common mistakes

- Expecting the preview to change before **Start Procedure**
- Feature-level cleaning without Imputation for new missing values
- Low correlation thresholds that drop many useful features
