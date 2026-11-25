## Start Procedure — sequence

1. **Guards:** not already running; input file exists; split rules OK (supervised); Output Directory set; data loaded from File Selection; survival horizon confirmations when required.
2. Creates a **new folder** under the Output Directory parent.
3. Collects GUI configuration (all checked stages and search settings).
4. Starts **resource monitoring** (CPU/RAM sampling).
5. Prepares data on the main path, then launches the search so **Stop** can cancel the process tree.
6. Updates progress UI; writes `Final_Results.csv` and combo JSON as combinations finish.

---

## Stop Procedure

- Cancels the run; partial `combo_results/` may remain.
- Use **Rebuild Results** later to reconstruct `Final_Results.csv` from finished `combo_results/*.json` when possible.
- Prefer **Stop Procedure** over closing the app.

---

## Resource Usage

| Control | Role |
|---------|------|
| CPU % | Budget for parallel work (outer combinations × inner CV) |
| RAM % | Caps how many outer workers fit |

Defaults are commonly **50% / 50%**.

---

## One search at a time

If a pipeline is already running in another mode, **Start Procedure** shows a **Pipeline Running** warning. Switch to that mode to monitor, or **Stop** before starting elsewhere.
