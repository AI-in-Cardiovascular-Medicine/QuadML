# Python requirements

For developers and source installs. Packaged-app users can skip this page — see [Installation](../getting-started/installation.md).

Canonical pin file (Windows / Linux): **`requirements.txt`** at the application repo root.  
Install with: `pip install -r requirements.txt` inside the project `.venv`.

**macOS:** use **`requirements-mac.txt`** (same stack; **PyQt5==5.15.11** for arm64 wheels). Pin constants and helpers: `src/shared/app/mac_modifications.py`. Windows/Linux keep **`requirements.txt`** unchanged.

---

## Version policy

| Item | Guidance |
|------|----------|
| Python | **3.9–3.12** recommended |
| Install style | Exact pins in `requirements.txt` (Windows/Linux) or `requirements-mac.txt` (macOS) |
| GUI toolkit (Windows/Linux) | **PyQt5==5.15.9** |
| GUI toolkit (macOS) | **PyQt5==5.15.11** (`requirements-mac.txt`) |
| Core ML pin | **scikit-learn==1.5.2** (required by **scikit-survival==0.23.1**, which needs sklearn &lt; 1.6) |

Do not casually upgrade scikit-learn past the pin. Related pins that stay on the sklearn 1.5 line include **hdbscan==0.8.40** (newer hdbscan wants sklearn ≥ 1.6).

---

## Major dependency groups

| Group | Examples (pinned in the requirements files) |
|-------|---------------------------------------------|
| GUI | PyQt5 |
| Core ML / data | numpy, pandas, scipy, scikit-learn, imbalanced-learn, joblib, threadpoolctl |
| Clustering | genieclust, hdbscan |
| Visualization | matplotlib, seaborn, pillow, umap-learn, pynndescent |
| Imputation | fancyimpute (Windows also pins **cvxpy** / **osqp** for solver stability) |
| Feature selection | **boruta** (wrapped by `shared.pipeline.feature_selector.BorutaSelector`) |
| I/O | openpyxl, python-docx |
| Boosting | xgboost |
| Interpretability | shap, lime, scikit-image, numba, llvmlite, cloudpickle, jinja2 |
| Survival | lifelines, scikit-survival, statsmodels, patsy, survshap |
| Deep survival | torch, pycox, torchtuples |
| Utilities | tqdm, loguru, psutil |
| Dev | pytest |
| Packaging | pyinstaller |

Exact versions change only when maintainers update `requirements.txt` / `requirements-mac.txt` — always trust those files over this summary.

---

## Do **not** install (conflicts)

| Package | Why |
|---------|-----|
| **eli5** | Would pull scikit-learn ≥ 1.6; conflicts with scikit-survival. Permutation Importance uses `sklearn.inspection`. |
| **survlimepy** | GPLv3; QuadML implements native Survival LIME in-project instead. |
| Forced upgrades of **hdbscan** past **0.8.40** | Newer releases declare sklearn ≥ 1.6 and break the survival pin. |

**boruta** *is* required (`boruta==0.4.3`). Do not remove it or replace it with a different Boruta package.

---

## Survival / deep-learning runtime notes

| Topic | Detail |
|-------|--------|
| DeepSurv / pycox data dirs (frozen) | Windows `%LOCALAPPDATA%\QuadML\pycox_data`; macOS `~/Library/Application Support/QuadML/pycox_data` |
| SurvSHAP on packaged Mac | Frozen `.app` may force SurvSHAP Compute to `n_jobs=1` (**H11**) — slower than Windows/Linux; source Mac / other OSes stay parallel |
| `survshap` | Required for native SurvSHAP(t); prefer a full successful verify |

## macOS runtime notes

| Topic | Detail |
|-------|--------|
| Soft throttle | Resource Usage still plans the search; under memory pressure QuadML may shrink concurrency or defer the next combination (does not kill an in-flight combo) |
| Logs / data | `~/Library/Application Support/QuadML` (`logs/`, `pycox_data/`) |
| Requirements | Always use `requirements-mac.txt` on Apple Silicon |

---

## Verify after install

**Windows:**

```text
python src\verify_quadml_bundle.py
```

**macOS / Linux:**

```text
python src/verify_quadml_bundle.py
```

Checks critical imports (PyQt5, sklearn, shap, sksurv, survshap, torch/pycox, genieclust, hdbscan, boruta, …) and presence of entry files / packaged source trees.

---

## Disk and time

- Full install includes **PyTorch** and a large scientific stack.
- Plan for multi‑GB download/cache on a clean machine.

See also: [Build and package](build-and-package.md) · [Code structure](code-structure.md)
