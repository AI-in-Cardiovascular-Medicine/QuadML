## How to use the Results screen

1. Open **Results** after **Start Procedure** finishes (or after **Rebuild Results**). Confirm Final_Results.csv file in the output folder, or **Browse** another folder that contains that CSV file and upload that.
2. Read pipeline cards / rows (**Train** vs **Test**, or **External**, or unsupervised metrics — depending on mode).
3. Click **Metric Explanations** for the full in-app metric text.
4. Use Compare / Detailed Report / Show Selected (and filters) as labeled.

---

## Display conventions

Pipeline labels use short codes, for example:

`IQR | SimpImp(med) | StdSc | SKB | LR`

Keep-all stages show as `No cleaning`, `No scaling`, `No selection`, `No DR` rather than being omitted.

Prefer held-out metrics (**Test** / **External**) in supervised modes when choosing a pipeline. Do not treat Train scores as generalization.
