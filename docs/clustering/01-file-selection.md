# Clustering — File selection

Load the dataset and choose the Output Directory for unlabeled clustering. Nothing is written until **Start Procedure** on Search Settings. There is no External Test Data and no ID Column picker. An optional **Benchmark Label** can score ARI / NMI / FMI after clustering; it is **not** used for training or for ranking pipelines, leave **(None)** unless you intentionally want those reference metrics. Prefer mostly numeric features.

![File Selection](../assets/cluster/2.png)

## Controls

| Control | What it does | When to use it |
|---------|--------------|----------------|
| **Select File** | Loads the main dataset | Always |
| **Output Directory** | Parent folder for dated run outputs | Always |
| **Benchmark Label** | Known class column for ARI / NMI / FMI only | Optional external validation of clusters |
| **Column Removal** | Drops listed columns at Start | IDs, text, unused columns |
| **Data Description** / **Clear** | Summary / reset | As needed |

![Select File, Output Directory, Benchmark Label, and Column Removal](../assets/cluster/3.png)

## Common mistakes

- Starting without an Output Directory  
- Treating Benchmark Label as a training target  
- Leaving ID / text columns in as features  
