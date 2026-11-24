# Clustering — File selection

**Where**: Clustering → **File Selection**

Load the dataset and choose the Output Directory. Nothing is written until **Start Procedure** on Search Settings.

![File Selection](../assets/cluster/2.png)

## What this step does

Points QuadML at your `.csv` / `.xlsx` (mostly numeric features work best), optional Benchmark Label, and the **Output Directory** parent folder.

## Controls

| Control | What it does | When to use it |
|---------|--------------|----------------|
| **Select File** | Loads the main dataset | Always |
| **Output Directory** | Parent folder for dated run outputs | Always |
| **Benchmark Label** | Known class column for ARI / NMI / FMI only | Optional external validation of clusters |
| **Column Removal** | Drops listed columns at Start | IDs, text, unused columns |
| **Data Description** / **Clear** | Summary / reset | As needed |

**Task notes:** No External Test Data and no ID Column picker. Benchmark Label is **not** used for training or for ranking pipelines — leave **(None)** unless you intentionally want ARI / NMI / FMI.

## Common mistakes

- Starting without an Output Directory  
- Treating Benchmark Label as a training target  
- Leaving ID / text columns in as features  
