# Classification — File selection

This step is for loading your dataset, choosing the **Output Directory** where QuadML saves run results, and setting the class **Label Column** plus related options (Task Type, Decision Threshold, optional ID Column, External Test Data, and Column Removal). Use a `.csv` or `.xlsx` file with a header row as input dataset.

![File Selection](../assets/class/Class03.png)

## Setting

| Setting | What it does | When to use it |
|---------|--------------|----------------|
| **Select File** | Loads the main dataset (header row required) | Always |
| **Output Directory** | Parent folder for dated run outputs | Always required before Start |
| **External Test Data** | Second labeled file with the same features and label | Hold-out cohort |
| **Label Column** | Class outcome (Auto-Detect for names like `label`, `class`) | Always |
| **ID Column** | Record ID, or **No ID Column** for synthetic IDs | When you have stable IDs |
| **Task Type** | Auto / Binary / Multi-class | Override Auto only if needed |
| **Decision Threshold** | Probability cut for metrics that use a yes/no class call (for example Accuracy or F1) | Binary tasks; default Youden (Train) is fine to start |
| **Column Removal** | Drops listed columns at Start Procedure | IDs, text, unused columns |
| **Data Description** / **Clear** | Summary / reset | As needed |

Main file, Output Directory, and optional External file:

![Select File, Output Directory, External Test Data](../assets/class/Class04.png)

Label Column, ID Column, and Task Type:

![Label, ID, and Task Type](../assets/class/Class05.png)

Binary tasks can set a **Decision Threshold** for metrics that use a yes/no class call (for example Accuracy or F1).

| Decision Threshold | Meaning |
|--------------------|---------|
| Youden (Train) | Maximize Sensitivity + Specificity − 1 on Train ROC (default) |
| Prevalence (Train) | Positive-class fraction on Train |
| Manual | Probability in (0, 1) |
| 0.5 | Fixed cut |

The threshold is set on Train and frozen for Test/External. Multi-class picks the class with the highest probability (no threshold control).

![Decision Threshold options](../assets/class/Class07.png)

Column Removal, Data Description, and Clear:

![Column Removal and helpers](../assets/class/Class08.png)

## Common mistakes

- Starting without an Output Directory
- External file with different column names
- Expecting Decision Threshold on multi-class
- Leaving ID columns in as features
