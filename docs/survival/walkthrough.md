# Survival Analysis — Tutorial

A short end-to-end click path for a first Survival Analysis run: load duration and event data, keep preprocess light, enable Kaplan–Meier plus Cox, run a small search, then read Metrics, Visualization, and Interpretability. Keep the search small so the first run finishes quickly. For method details and full option tables, use the Pipeline and Results pages.

---

## 1. Start

1. Open QuadML and select **Survival Analysis** from left paned and click on **File Selection**.
2. Click on **Browse** in Select File and upload a `.csv` or `.xlsx` file with duration, event, and features.
3. Click on **Browse** in Output Directory and select a path for output results and files.
4. Set **Duration Column** and **Event / Censor Column** (or **Auto-Detect**).
5. Set **Event Coding** so **1 = event observed** unless your file differs.
6. Leave **Eval. Horizons** on **Auto from follow-up**.
7. Optional: ID Column, Column Removal, External file (must include duration + event).

![File Selection](../assets/sa/2.png)

---

## 2. Preprocess

Select preferred methods for preprocessing from Cleaning to Feature Selection.

---

## 3. Models and split

1. **Descriptive Analysis:** **Kaplan-Meier** and **Nelson-Aalen**.
2. **Survival Models: Select preferred ones.
3. **Data Splitting:** 80/20, Train on all data **off**.

---

## 4. Run

1. **Parameter Tuning:** Random Search or Grid Search, **Fast**, CPU/RAM 50/50.
2. Review the tree: **Start Procedure** and wait (or **Stop** to cancel).

---

## 5. Read output

1. **Metrics:** prefer **Test** calibration (Mean Cal / Slope / ICI), then C-index / td-AUC.
2. **Visualization:** KM curve; Risk Group KM / Calibration for Cox.
3. **Interpretability:** Load the Cox pipeline; try coefficients or SurvSHAP.

**Success**: Final_Results.csv  under `Your Folder\YYYY-MM-DD_HH-MM-SS\`.
