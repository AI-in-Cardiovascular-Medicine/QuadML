# Troubleshooting

Start here for common launch, run, and results problems. For dependency pins, packaging, or deep survival-stack notes, see [Python requirements](../developers/python-requirements.md), [Build and package](../developers/build-and-package.md), and [Contributing](../developers/contributing.md).

---

## App won't start

| Symptom | What to try |
|---------|-------------|
| Windows exe fails immediately | Keep the full install/folder intact (`QuadML.exe` + `QuadML_Worker.exe` + `_internal`). Prefer the official installer from [ai-cvm.org/QuadML](https://ai-cvm.org/QuadML/). |
| Windows exe exits silently | Prefer a full website/build installer, not a hand-copied exe. |
| macOS “damaged” / blocked | Unsigned app: **Right-click → Open** the first time. |
| macOS “Finding software” (Rosetta) when a worker starts | Replace an old Intel `.app` with the current **arm64** build. |
| Source install: GUI never opens | Activate the project `.venv`, then `python src/quadml_entry.py`. Confirm PyQt5 with `python src/verify_quadml_bundle.py`. |
| `ModuleNotFoundError` (source) | Recreate/activate `.venv`; reinstall `requirements.txt` or `requirements-mac.txt`; run verify. Do not use Anaconda **base**. |

---

## Error messages when starting a run

| Message / symptom | Fix |
|-------------------|-----|
| Invalid / missing input file | File Selection → Browse a real `.csv` / `.xlsx` |
| Output directory error | Browse a writable **parent** folder |
| Complete data loading first | Finish File Selection identification after Browse |
| Data Splitting / External validation | Fix **Train on all data** and External file columns |
| Pipeline already running | Switch to that mode or **Stop Procedure** before starting another |
| Survival horizon confirmation cancelled | Restart and accept / adjust **Eval. Horizons** |

---

## Slow runs or freezes

| Symptom | What to try |
|---------|-------------|
| Machine freezes / very slow | Lower Resource Usage CPU/RAM %; use **Fast** budget; fewer methods/models |
| macOS RAM climbs | Soft throttle may reduce concurrency — lower Resource Usage % |
| Many failed combinations | Check role columns; shrink the search grid |

---

## Missing or incomplete results

**Rebuild Results** (once): on **Parameter Tuning** or **Search Settings**, click **Rebuild Results**. QuadML rebuilds `Final_Results.csv` from finished `combo_results/*.json` in the dated run folder (browse that folder if asked). Use this after **Stop**, a crash, or an incomplete CSV — you do not need to re-run combinations that already finished.

| Symptom | What to try |
|---------|-------------|
| Empty Results / no `Final_Results.csv` | Open the dated run folder that still has `combo_results/`, then **Rebuild Results** |
| Stop left a partial CSV | **Rebuild Results** as above |
| Interpretability needs a pipeline | Complete a successful fit; load the matching `.pkl` |
| Clustering has no Interpretability | Expected — use Results / Visualization |

---

## Running from source (short)

Prefer `python src/quadml_entry.py` with the project `.venv` active. After broken upgrades, reinstall exact pins and run `verify_quadml_bundle.py`.

Full pins, conflicts (eli5 / hdbscan / boruta), and DeepSurv / SurvSHAP notes: [Python requirements](../developers/python-requirements.md). Packaging: [Build and package](../developers/build-and-package.md).

---

## Report an issue

1. Note **mode**, **Windows exe / macOS app / Linux / source**, and the **exact dialog text**.
2. Check the dated Output Directory for `combo_results/` / `Failed_Combinations.csv`.
3. Frozen logs (if present): Windows `%LOCALAPPDATA%\QuadML\logs`; macOS `~/Library/Application Support/QuadML/logs`.
4. Open an issue: [github.com/AI-in-Cardiovascular-Medicine/QuadML/issues](https://github.com/AI-in-Cardiovascular-Medicine/QuadML/issues/)  
   Or follow [Contributing](../developers/contributing.md) / contacts on [About QuadML](10-about.md).
