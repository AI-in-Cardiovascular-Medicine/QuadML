# Getting started — System requirements
---

## Supported platforms

| Platform | How to run QuadML |
|----------|------------------------|
| **Windows 10 / 11** (64-bit) | Download the `.exe` from [www.ai-cvm.org](https://www.ai-cvm.org), **or** clone from [GitHub](https://github.com/AI-in-Cardiovascular-Medicine/QuadML) and [install from source](02-install-from-source.md) |
| **macOS** (Apple Silicon) | Install from source with `requirements-mac.txt`, **or** use a CI-built `.app`. See [macOS notes](04-macos-notes.md) |
| **Linux** (64-bit) | Install from source, **or** use the portable archive / `.deb` package from the Linux build |

---

## Hardware (practical)

| Resource | Guidance |
|----------|----------|
| CPU | Multi-core recommended; Resource Usage (CPU %) controls parallel search |
| RAM | 8 GB minimum for small tables; 16 GB+ for larger searches / survival / deep survival (PyTorch) |
| Disk | Space for dated run folders under your Output Directory (CSV, JSON, `.pkl`, plots) |
| Display | Desktop resolution suitable for the main window + left nav |

Resource Usage defaults are often **50% CPU / 50% RAM** so the machine stays usable during a search.

---

## Software prerequisites

### Source install

- **Python 3.9–3.12** recommended (tested with a project `.venv`).
- Create and use a project virtual environment (`.venv`) — **not** Anaconda base:

```bash
python -m venv .venv
```

- Install pinned dependencies with `pip`:
  - **Windows / Linux:** `pip install -r requirements.txt`
  - **macOS (Apple Silicon):** `pip install -r requirements-mac.txt` (same stack; PyQt5 arm64 pin — see [macOS notes](04-macos-notes.md))
- Enough disk space for large wheels (especially **torch**).
- On Windows: PowerShell or Command Prompt; long paths enabled if installs fail.
- Optional check after install: `python src/verify_quadml_bundle.py`

### Packaged apps (no separate Python)

- **Windows:** download the `.exe` from [www.ai-cvm.org](https://www.ai-cvm.org) (or a portable folder build) — writable folder under `%LOCALAPPDATA%\QuadML` for caches / logs.
- **macOS:** CI-built `.app` (see [macOS notes](04-macos-notes.md)).
- **Linux:** portable archive or `.deb` package from the Linux build.

### Packaging only (maintainers)

- Source install as above (`requirements.txt` already includes **PyInstaller**).
- **Windows:** **Inno Setup 6+** for `QuadML_Setup_*.exe` ([jrsoftware.org](https://jrsoftware.org/isinfo.php)).
- **Linux / macOS:** use the project build scripts / GitHub Actions workflows for the portable archive, `.deb`, or `.app`.

---

## Network

- Source `pip install` needs network access to PyPI (torch and scientific wheels are large).
- Offline use after install: runs are local.