# Regression — Data splitting

**Where**: Regression → **Data Splitting**

Chooses Train/Test (and optional External-only evaluation).

![Data Splitting](../assets/reg/23.png)

--8<-- "_snippets/data-splitting.md"

**Regression note:** Splits are **not** stratified by class — the outcome is continuous.

## Common mistakes

- Checking **Train on all data** without External — **Start Procedure** will refuse
- Comparing Test metrics from a normal split with External metrics from a train-on-all run as if they were the same design
- Extremely small test percentages on tiny datasets
