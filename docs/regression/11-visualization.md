# Regression — Visualization

Plots for comparing pipelines and inspecting residual diagnostics on one selected pipeline. Load Final_Results.csv file in **Results** first.

![Visualization](../assets/reg/34.png)

--8<-- "_snippets/visualization-usage.md"

Choose **Single Pipeline**, **Pipelines Comparison**, or **Plot Analyzer**:

![Visualization mode tabs](../assets/reg/35.png)

**Single Pipeline** — pick a pipeline and set **Results to display** (prefer **Test** or **External**):

![Single Pipeline and Results to display](../assets/reg/36.png)

## Comparing pipelines

| Plot | What it shows |
|------|----------------|
| Single-metric plots | One metric (e.g. MAE, RMSE, R²) across pipelines |
| Metrics comparison | Several metrics together |
| Heatmaps (where offered) | Metric values across preprocessing × model grids |

**Pipelines Comparison** → Combined Plot → Metric Comparison (for example Adjusted R²):

![Metric Comparison across pipelines](../assets/reg/41.png)

Heatmap of one metric (model × dimensionality reduction):

![Heatmap One metric](../assets/reg/43.png)

Heatmap of all metrics for selected pipelines:

![Heatmap All metrics](../assets/reg/44.png)

**Side by Side** comparison for selected pipelines:

![Side by Side RMSE comparison](../assets/reg/45.png)

## One pipeline

| Plot | What it shows |
|------|----------------|
| Residuals vs Predicted | Structure or bias in errors |
| Predicted vs Actual | Agreement with the target |
| Residual distribution | Spread of errors |
| Other residual / QQ-style views | As offered in the GUI |

Residuals vs Predicted:

![Residuals vs Predicted](../assets/reg/37.png)

True vs Predicted:

![True vs Predicted](../assets/reg/38.png)

Q-Q plot of residuals:

![Q-Q Plot of Residuals](../assets/reg/39.png)

Residual distribution (histogram):

![Residual Distribution](../assets/reg/40.png)

**Plot Analyzer** adds a plain-language reading next to the chart:

![Plot Analyzer](../assets/reg/46.png)

Use **Plot Explanations** / **Analyze** for in-app help.

## Common mistakes

- Opening Visualization before any successful combination finished
- Mixing plots from an older dated folder after starting a new run
- Reading Train-only plots as trustworthy absolute performance
