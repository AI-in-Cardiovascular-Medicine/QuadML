# Regression — Visualization

**Where**: Regression → **Visualization**

Charts for comparing pipelines and residual diagnostics for one pipeline.

![Visualization](../assets/reg/34.png)

--8<-- "_snippets/visualization-usage.md"

## Comparing pipelines

| Plot | What it shows |
|------|----------------|
| Single-metric plots | One metric (e.g. MAE, RMSE, R²) across pipelines |
| Metrics comparison | Several metrics together |
| Heatmaps (where offered) | Metric values across preprocessing × model grids |

## One pipeline

| Plot | What it shows |
|------|----------------|
| Residuals vs Predicted | Structure or bias in errors |
| Predicted vs Actual | Agreement with the target |
| Residual distribution | Spread of errors |
| Other residual / QQ-style views | As offered in the GUI |

Use **Plot Explanations** / **Analyze** for in-app help.

## Common mistakes

- Opening Visualization before any successful combination finished
- Mixing plots from an older dated folder after starting a new run
- Reading Train-only plots as trustworthy absolute performance
