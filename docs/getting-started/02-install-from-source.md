# Getting started — Install from source

Install QuadML from the **GitHub** repository in a project virtual environment, then launch the GUI from `src`.

On Windows, if you only need a ready-to-run app (no Python), download the **`.exe`** from [www.ai-cvm.org](https://www.ai-cvm.org) instead — see [Install Windows executable](03-install-windows-exe.md).

---

## 1. Get the code

1. Clone the QuadML repository from [GitHub](https://github.com/AI-in-Cardiovascular-Medicine/QuadML) (or copy an existing clone) to a writable folder (example: `L:\QuadML`):

```text
git clone https://github.com/AI-in-Cardiovascular-Medicine/QuadML.git
```

2. Open a terminal at the **repo root** (where `requirements.txt` lives).

---

## 2. Create and activate a venv

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (cmd):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Use this project `.venv`, not Anaconda **base**. Mixed base environments often miss packages or conflict with the pinned versions in `requirements.txt`.

---

## 3. Install dependencies

Upgrade `pip` once, then install the pinned stack:

```text
python -m pip install -U pip
```

**Windows / Linux** (use `requirements.txt`):

```text
pip install -r requirements.txt
```

**macOS (Apple Silicon)** (use `requirements-mac.txt` so PyQt5 has an arm64 wheel):

```text
pip install -r requirements-mac.txt
```

Do **not** use `requirements-mac.txt` on Windows or Linux. On Apple Silicon, do **not** install from `requirements.txt` alone (PyQt5 5.15.9 has no macOS arm64 wheel). See [macOS notes](04-macos-notes.md) and [Python requirements](06-python-requirements.md).

The install includes PyQt5, scikit-learn 1.5.2, survival and interpretability stacks, torch/pycox, PyInstaller, and related pins. First install can take a long time (large wheels, especially torch).

---

## 4. Verify the bundle

From the repo root (venv active):

**Windows:**

```text
python src\verify_quadml_bundle.py
```

**macOS / Linux:**

```text
python src/verify_quadml_bundle.py
```

Fix any missing imports before launching or packaging.

---

## 5. Launch the GUI

From the repo root (venv active):

**Windows:**

```text
python src\quadml_entry.py
```

**macOS / Linux:**

```text
python src/quadml_entry.py
```

This is the preferred entry point (it selects GUI vs search/worker roles via `QUADML_ROLE` when needed).

---

## 6. Optional: run tests

```text
pytest src/tests -q
```

(`pytest` is included in `requirements.txt` under optional/dev.)

---

## Common mistakes

- Installing into Anaconda base instead of `.venv`
- Using Python outside **3.9–3.12**
- On macOS Apple Silicon: installing only `requirements.txt` instead of `requirements-mac.txt`
- Adding **eli5** (pulls scikit-learn ≥ 1.6 and conflicts with scikit-survival — see `requirements.txt` notes)
- Launching without activating the venv (wrong `python` on PATH)
