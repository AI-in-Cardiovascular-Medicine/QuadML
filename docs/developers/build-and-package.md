# Build and package

How maintainers freeze QuadML after a working source install. End users can skip this page.

Dependency pins: [Python requirements](python-requirements.md). Process roles / binaries: [Code structure](code-structure.md).

Packaged outputs today:

| Platform | Primary path | Artifacts |
|----------|--------------|-----------|
| **Windows** | `src/build_windows.ps1` or Actions **Build Windows exe** | `QuadML_Setup_*.exe` (+ optional portable ZIP / folder) |
| **macOS** (Apple Silicon) | Actions **Build macOS app** | `QuadML-macOS.app.zip` (`QuadML.app`) |
| **Linux** (amd64) | Actions **Build Linux** | `QuadML-Linux-portable.tar.gz` + `quadml_*_amd64.deb` |

---

## Prerequisites

1. Project `.venv` with the platform pin file:
   - **Windows / Linux:** `pip install -r requirements.txt` (includes **PyInstaller==6.21.0**)
   - **macOS:** `pip install -r requirements-mac.txt` (**PyQt5==5.15.11**)
2. `python src/verify_quadml_bundle.py` succeeds.
3. **Windows installer:** [Inno Setup 6+](https://jrsoftware.org/isinfo.php) (or `winget install JRSoftware.InnoSetup`).
4. Enough disk for PyInstaller `build` / `dist` trees (Linux CI also frees runner disk before freeze).

CI builds use **Python 3.11**.

---

## Windows folder + Setup (recommended script)

From an activated venv:

```powershell
cd src
.\build_windows.ps1
```

Optional flags:

| Flag | Effect |
|------|--------|
| `-SkipInstaller` | PyInstaller folder only (no Inno) |
| `-CreateZip` | Also write a portable ZIP |

Optional environment variables (passed to Inno Setup):

| Variable | Effect |
|----------|--------|
| `QUADML_VERSION` | Installer version, e.g. `1.1.0` (default: `1.0` from the `.iss` / `QUADML_VERSION` in code) |
| `QUADML_COMPRESSION` | Inno compression, e.g. `lzma2/normal` (default: `lzma2/max`) |

Output locations (relative to `src\`):

- Folder: `src\QuadML_Installation_file\dist\QuadML\QuadML.exe` (+ `QuadML_Worker.exe` + `_internal`)
- Setup: `src\QuadML_Installation_file\installer\QuadML_Setup_1.0.exe`
- Portable ZIP: `src\QuadML_Installation_file\installer\QuadML_Portable_<date>.zip`

Steps inside the script: strip PyQt5’s old C++ runtime DLLs from the venv (avoids silent `0xC0000005` with fancyimpute/cvxpy) → verify → build icon → PyInstaller `QuadML.spec` → optional Inno (`build_installer.ps1`) → optional ZIP (`create_portable_zip.ps1`).

### GitHub Actions (no Windows machine needed)

The workflow **Build Windows exe** runs the same `build_windows.ps1` on a hosted Windows runner, installing Inno Setup if needed.

- Manual: Actions → **Build Windows exe** → Run workflow. Download the artifact **QuadML-Windows-installer** (`QuadML_Setup_<version>.exe`, 14-day retention).
- Release: push a tag `vX.Y.Z`. The installer gets version `X.Y.Z` and is attached to the GitHub Release for that tag.
- The Setup.exe is unsigned: Windows SmartScreen shows "Unknown publisher" (More info → Run anyway).
- CI verifies every bundled `msvcp140.dll` is **14.40+**.

---

## Entry points in the freeze

| Binary / role | Purpose |
|---------------|---------|
| `QuadML` / `QuadML.exe` | GUI (and relaunch helper for some child roles via `quadml_entry`) |
| `QuadML_Worker` / `QuadML_Worker.exe` | Outer combination / loky-style workers |

Do not ship the GUI binary without the worker companion and `_internal` (folder builds).

---

## macOS `.app`

Supported Apple Silicon packaged path. Helpers: `mac_packaging_overview()`, `mac_maintainer_ci_build_steps()`, `mac_release_attach_steps()`, `mac_local_pyinstaller_build_steps()` in `shared.app.mac_modifications`.

- Spec: `src/QuadML_mac.spec` (`target_arch='arm64'`)
- Deps: committed **`requirements-mac.txt`** (PyQt5==5.15.11); resolved in CI via `assert_mac_requirements_file` — does **not** rewrite Windows `requirements.txt`
- Automation: GitHub Actions **Build macOS app** (`workflow_dispatch`, runner **`macos-15`**, Python `architecture: arm64`)
- Post-build: `assert_mac_app_arm64` rejects Intel-only Mach-O (avoids Rosetta **Finding software**)
- Artifact: **QuadML-macOS-app**[-date-sha] (`QuadML-macOS.app.zip`) — **14-day** Actions retention for smoke
- Durable channel: attach the zip to **GitHub Releases** (`mac_release_attach_steps`)
- Signing: **unsigned** today — Gatekeeper: Right-click → Open

### Maintainer CI flow

Prefer CI over a local Mac freeze:

1. Push Mac packaging files → Actions → **Build macOS app** → Run workflow.
2. Download artifact **QuadML-macOS-app**[-date-sha] → extract `QuadML-macOS.app.zip` / `QuadML.app`.
3. On Apple Silicon: Right-click → Open (Gatekeeper).
4. Smoke-test (below).

### Durable Mac zip (GitHub Releases)

Do **not** treat the Actions artifact as the only distribution channel.

1. After a green Mac build, download `QuadML-macOS.app.zip`.
2. On the version’s GitHub Release, attach that zip (UI or `gh release upload vX.Y.Z QuadML-macOS.app.zip --clobber`).
3. Keep Windows Setup / portable assets on their existing release process.

### Optional local Mac freeze

1. `pip install -r requirements-mac.txt` + `verify_quadml_bundle.py`
2. `cd src` → `python build_quadml_icon.py` → `pyinstaller QuadML_mac.spec --noconfirm`
3. Open `dist/QuadML.app` (Right-click → Open if unsigned)

CI uses `--distpath ../dist_mac` / `--workpath ../build_mac`; a local freeze without those flags lands under `src/dist` by default. Do **not** run Windows `build_windows.ps1` / Inno for Mac artifacts.

---

## Linux portable + `.deb`

Workflow: **Build Linux** (`workflow_dispatch`, **`ubuntu-22.04`**). Spec: `src/QuadML_linux.spec`. Deps: **`requirements.txt`** (same pins as Windows).

Notable CI choices:

- Installs **CPU-only torch** first (`download.pytorch.org/whl/cpu`) so the bundle does not pull multi‑GB CUDA wheels.
- Frees runner disk before the freeze; headless smoke-tests the frozen GUI (`QT_QPA_PLATFORM=offscreen`).
- Archives with **tar.gz** (keeps execute bits), not zip.

### Artifacts

| Artifact | Contents |
|----------|----------|
| **QuadML-Linux-portable** | `QuadML-Linux-portable.tar.gz` → unpack and run `./QuadML/QuadML` (keep `QuadML_Worker` + `_internal`) |
| **QuadML-Linux-deb** | `quadml_<version>_amd64.deb` → installs to `/opt/quadml`, provides `quadml` command + menu entry |

`.deb` version is `QUADML_VERSION` from `shared.results.environment_manifest` plus the Actions run number (e.g. `1.0-<run>`).

Install example:

```bash
sudo apt install ./quadml_*_amd64.deb
```

**glibc note:** the portable / `.deb` need **glibc ≥ 2.35** (same or newer than ubuntu-22.04). Older distros may fail to start.

---

## After packaging

Smoke-test (Windows Setup / folder, Mac `.app`, or Linux portable / `.deb`):

1. Launch frozen GUI → Welcome.
2. Short Classification (or Clustering) search with tiny data.
3. Confirm Stop kills the search tree and Output Directory receives a dated folder.
4. If the app fails silently: Windows `%LOCALAPPDATA%\QuadML\logs`; macOS `~/Library/Application Support/QuadML/logs`.

---

## Common mistakes

- Freezing before verify passes
- Missing Inno Setup when expecting `QuadML_Setup_*.exe`
- Distributing an incomplete folder (missing worker or `_internal`)
- Using `requirements.txt` alone on Apple Silicon (use `requirements-mac.txt`)
- Shipping an old Intel Mac `.app` (Rosetta **Finding software** on workers)
- Expecting the Linux portable to run on glibc older than 2.35
- Hand-copying a Windows exe without rebuilding (old PyQt5 `msvcp140.dll` → silent crash)
