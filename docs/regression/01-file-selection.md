# Regression — File selection

**Where**: Regression → **File Selection**

Load the dataset, set the numeric outcome, and choose where run outputs will be saved. Nothing is written to disk until **Start Procedure**.

![File Selection](../assets/reg/2.png)

## What this step does

Points QuadML at your `.csv` / `.xlsx`, the numeric **Target** (Label Column in the GUI), optional ID / External file, and the **Output Directory** parent folder.

## Controls

| Control | What it does | When to use it |
|---------|--------------|----------------|
| **Select File** | Loads the main dataset | Always |
| **Output Directory** | Parent folder for dated run outputs | Always |
| **External Test Data** | Second file with the same features and numeric target | Hold-out; required if Train on all data is on |
| **Label Column** | Numeric continuous outcome (Auto-Detect for names like `target`, `y`) | Always |
| **ID Column** | Record ID, or **No ID Column** | When you have stable IDs |
| **Column Removal** | Drops listed columns at Start | IDs, text, unused columns |
| **Data Description** / **Clear** | Summary / reset | As needed |

**Task note:** No Task Type or Decision Threshold in Regression.

## Common mistakes

- Starting without an Output Directory  
- Using a class/categorical column as the target (use Classification)  
- External file with different column names  
