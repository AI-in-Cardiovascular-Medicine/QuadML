# Classification — Data splitting

Data splitting divides the dataset into a training set, used to build and tune the models, and a test set, kept aside to evaluate them on unseen data. Cross-validation during Parameter tuning uses only the training set, so test results are not influenced by the model choice. In classification, the split is stratified, so both sets keep the same proportion of each class. When an external test set is provided, the internal test set can be set to zero: all data is then used for tuning and training, and the models are evaluated only on the external set.

![Data Splitting](../assets/class/Class31.png)

## Settings

| Setting | What it does |
|---------|--------------|
| **Train / Test %** | Share of the main file used for Train vs Test (default **80% / 20%**) |
| **External Test Data** | Optional second labeled file set on File Selection; scored as an extra hold-out when present |
| **Train on all data (evaluate on External only)** | Uses 100% of the main file for Train; requires External and removes the internal Test split |

![Train on all data (External only)](../assets/class/Class32.png)

## Evaluation designs

| Design | What happens |
|--------|----------------|
| **Train / Test** (default) | Internal 80/20 (or your %) split; no External file |
| **Train / Test + External** | Internal Train/Test plus External scored as a third set |
| **Train on all data + External** | No internal Test; External is the only evaluation set |

**Start Procedure** rejects invalid setups (for example Train on all without a usable External file).

## Common mistakes

- Checking **Train on all data** without External — **Start Procedure** will refuse
- Comparing Test metrics from a normal split with External metrics from a train-on-all run as if they were the same design
- Extremely small test percentages on tiny datasets
