# Shared — Visualization

**Where**: Any mode → **Visualization**

Charts for metrics and diagnostics from the completed (or loaded) run. Plot lists differ by mode. Prefer **Test** or **External** when judging generalization in supervised modes.

---

## What to click

1. Load **`Final_Results.csv`** in **Results** first (or confirm the active run folder).
2. Open **Visualization** and choose which results / pipelines to display.
3. Work in single-pipeline or comparison views as the mode offers.
4. Click **Plot Explanations** for figure-specific wording.
5. Use **Analyze** (Plot Analyzer) on a figure when available.
6. Export or refresh controls as shown on the page.

Some modes build charts live from caches and CSVs rather than writing every PNG during search.

---

## Common mistakes

- Opening Visualization before any successful combination finished
- Mixing plots from an older dated folder after starting a new run without noticing the active output path
- Reading Train-only plots as trustworthy absolute performance

---

## Mode manuals

- [Classification — Visualization](../classification/11-visualization.md)
- [Regression — Visualization](../regression/11-visualization.md)
- [Survival — Visualization](../survival/12-visualization.md)
- [Clustering — Visualization](../clustering/10-visualization.md)
