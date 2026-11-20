# Getting started — Troubleshooting

---

## Install / launch

| Symptom | What to try |
|---------|-------------|
| `ModuleNotFoundError` / import errors | Activate project `.venv`; re-run `pip install -r requirements.txt` (Windows/Linux) or `requirements-mac.txt` (macOS); run `python src/verify_quadml_bundle.py` |
| Wrong Python / Anaconda base | Recreate `.venv`; do not use base env |
| GUI never opens (source) | Confirm `python src/quadml_entry.py` (Windows: `src\quadml_entry.py`) with venv active; check PyQt5 in verify |
| Frozen Windows app fails immediately | Keep the full folder intact (`QuadML.exe` + `QuadML_Worker.exe` + `_internal`); do not move the exe alone |
| Frozen Windows app exits silently (0xC0000005 / fancyimpute) | Official builds strip PyQt5’s old `msvcp140.dll` from the venv before freeze. Prefer the website installer / a full rebuild via `build_windows.ps1`, not a hand-copied exe |
| macOS “damaged” / blocked app | Unsigned artifact: Right-click → **Open**; see [macOS notes](04-macos-notes.md) |
| macOS **Finding software** (Rosetta) when a worker starts | Old Intel `.app`; replace with the current **arm64** CI build (`macos-15`) |

---

## Start Procedure guards

| Message / symptom | Fix |
|-------------------|-----|
| **Input Error** — invalid / missing file | File Selection → Browse a real `.csv` / `.xlsx` ([Prepare the data](07-prepare-the-data.md)) |
| **Output Error** — output directory | Browse a writable **parent** folder |
| **Data Processing Error** — complete Data Loading | Load the file and finish File Selection identification first |
| **Data Splitting** validation | Fix **Train on all data** / External Test combination |
| **External Test Set Columns** | Align external feature / role columns with the training file |
| **Pipeline Running** | Switch to the running mode or **Stop Procedure** before starting another |
| **Survival horizon confirmation cancelled** | Re-start and accept / adjust **Eval. Horizons** as prompted |

---

## Search / resources

| Symptom | What to try |
|---------|-------------|
| Extremely slow or machine freezes | Lower Resource Usage CPU/RAM %; use **Fast** budget; reduce checked methods / models |
| macOS RAM climbs / Adaptive stuck low | Soft throttle may shrink concurrency or defer the next combo — lower Resource Usage %; see [Resource Usage on Mac](04-macos-notes.md#resource-usage-on-mac-soft-throttle) |
| Stop leaves incomplete CSV | Stop may write a **partial** `Final_Results.csv`; use **Rebuild Results** on Parameter Tuning / Search Settings from `combo_results/*.json` |
| Procedure **crashes mid-run** (no / incomplete `Final_Results.csv`) | On Parameter Tuning / Search Settings, click **Rebuild Results**. It rebuilds `Final_Results.csv` from every finished combination in `combo_results/*.json` (point at that dated run folder if asked) |
| Many rows in `Failed_Combinations.csv` | Check role columns, Boruta failures, and oversized model grids; shrink the search |
| Random encoding / console crashes on Windows (source prints) | Prefer `quadml_entry` (UTF-8 stdio); avoid exotic console code pages |

---

## Survival / DeepSurv / pycox

| Symptom | What to try |
|---------|-------------|
| Crash creating pycox datasets under a read-only install | Frozen builds set writable `PYCOX_DATA_DIR`: Windows `%LOCALAPPDATA%\QuadML\pycox_data`; macOS `~/Library/Application Support/QuadML/pycox_data` |
| Native SurvSHAP missing | Confirm `survshap` import via verify; reinstall from the platform requirements file |
| SurvSHAP very slow on frozen macOS `.app` | Expected under **H11** (`n_jobs=1`). Windows/Linux keep parallel loky. See [SurvSHAP H11](04-macos-notes.md#survshap-on-packaged-mac-h11) |

---

## Dependency conflicts

| Symptom | What to try |
|---------|-------------|
| sklearn / sksurv conflict after pip upgrades | Reinstall exact pins from `requirements.txt` or `requirements-mac.txt`; do not install **eli5** |
| Unexpected Boruta package errors | Keep pinned `boruta==0.4.3`; QuadML wraps it via `BorutaSelector` |
| hdbscan / sklearn conflict | Stay on **hdbscan==0.8.40** (newer wants sklearn ≥ 1.6) |

See [Python requirements](06-python-requirements.md).

---

## Results / Interpretability

| Symptom | What to try |
|---------|-------------|
| Empty Results / missing `Final_Results.csv` after a crash | Open the dated run folder that still has `combo_results/`, then click **Rebuild Results** to create `Final_Results.csv` for the combinations that finished |
| Interpretability needs a pipeline | Complete a successful fit; load the `.pkl` the UI expects |
| Clustering has no Interpretability step | Expected — use Results / Visualization only |

---

## Still stuck

1. Note **mode**, **Python / exe / .app**, and the **exact dialog text**.
2. Check the dated Output Directory for partial logs / `combo_results` / `Failed_Combinations.csv`.
3. Inspect frozen logs if present: Windows `%LOCALAPPDATA%\QuadML\logs`; macOS `~/Library/Application Support/QuadML/logs` (see [macOS notes](04-macos-notes.md)).
4. Re-run `verify_quadml_bundle.py` on source installs.
