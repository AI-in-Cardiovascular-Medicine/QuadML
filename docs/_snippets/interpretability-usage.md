## How to use the Interpretability screen

Interpretability explains a **loaded fitted pipeline**. It does **not** replace Test or External metrics for ranking. Clustering has no Interpretability step.

1. **Results** — load `Final_Results.csv` from the dated run folder.
2. **Interpretability** — Select Pipeline → **Load files** (model `.pkl` + matching feature CSVs) from that same run.
3. Choose a method compatible with the detected model.
4. Click **Prepare Explainer** / **Compute** as shown — plot buttons stay disabled until this finishes.
5. Open plots from the grouped buttons; use in-app help for method limits.
6. Save or browse artifacts when offered.

Most methods do **not** retrain the pipeline; they explain the loaded `.pkl`.

Point Results and Interpretability at the **same** dated run folder under your **Output Directory**.
