# Survival Analysis — Data splitting

**Where**: Survival Analysis → **Data Splitting**

Chooses Train/Test (and optional External-only evaluation). The outcome is duration + event, not a single label.

![Data Splitting](../assets/sa/28.png)

--8<-- "_snippets/data-splitting.md"

**Survival note:** Check cohort-comparison p-values on Results when comparing Train and Test.

## Common mistakes

- Checking **Train on all data** without External — **Start Procedure** will refuse
- Comparing Test metrics from a normal split with External metrics from a train-on-all run as if they were the same design
- Extremely small test percentages on tiny datasets
