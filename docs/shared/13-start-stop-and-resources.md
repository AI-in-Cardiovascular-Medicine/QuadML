# Shared — Start, Stop, and resources

**Where**: Parameter Tuning / Search Settings (**Start Procedure**, **Stop Procedure**, **Resource Usage**)

This page describes what happens when you start or stop a run, independent of mode.

---

## Start Procedure — sequence

1. **Guards:** not already running; input file exists; split rules OK; Output Directory set; data loaded from File Selection; survival horizon confirmations when required.
2. Creates a **new dated run folder** under the Output Directory parent.
3. Collects GUI configuration (all checked stages and search settings).
4. Starts **resource monitoring** (CPU/RAM sampling).
5. Runs data reading / cleaning / identification on the main path.
6. Launches the **ML search child** (`QUADML_ROLE=search`) so Stop can terminate the process tree.
7. Updates progress UI from search progress files; writes `Final_Results.csv` and combo JSON as combinations finish.

---

## Stop Procedure

- Requests cancel and clears/sets cancel markers used by the search child.
- Partial combination results under `combo_results/` may remain.
- Use **Rebuild Results** later to reconstruct `Final_Results.csv` from surviving JSON when possible.

Prefer **Stop Procedure** over closing the app when you need an orderly cancel.

---

## Resource Usage

| Control | Role |
|---------|------|
| CPU % | Budget for parallel work (outer combinations × inner CV) |
| RAM % | Caps how many outer workers fit |

Shared parallel config maps these percentages to `n_jobs`-style settings and may adaptively throttle under pressure. Defaults are commonly **50% / 50%**.

---

## One search at a time

If a pipeline is already running in another mode, **Start Procedure** shows a **Pipeline Running** warning. Switch to that mode to monitor, or **Stop** before starting elsewhere.

See also [Application shell](01-application-shell.md) and [Parameter Tuning / Search Settings](09-parameter-tuning.md).

---

## Common mistakes

- Closing the app instead of **Stop** — prefer Stop so cancel is orderly
- Setting CPU/RAM to 100% on a machine you still need for other work
- Starting again without noticing a new dated folder was created
- Ignoring the Pipeline Running warning and wondering why the second mode did not start
