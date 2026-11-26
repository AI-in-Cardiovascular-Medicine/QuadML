## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | Keeps every feature as-is | Small feature counts; full-feature baseline |
| **Select K Best** | Keeps the *k* features that score highest for survival (Cox-based ranking) | Fast first cut on wide data |
| **Recursive Feature Elimination** | Repeatedly drops the weakest features using a Cox model | Model-aware pruning |
| **Cox-LASSO** | Uses Cox-LASSO shrinkage so some feature weights become zero | Sparse survival selection |
| **Boruta** | Keeps features that matter more than random comparison copies (screened against the event indicator) | Exploratory “which features matter” |
| **Sequential Forward Selection** | Adds features one by one when they improve the survival model | Small feature counts only; can be very slow |
| **Sequential Backward Selection** | Removes features one by one when they hurt least | Small feature counts only; can be very slow |
