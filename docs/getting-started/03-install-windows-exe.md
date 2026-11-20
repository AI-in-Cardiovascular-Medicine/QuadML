# Getting started — Install Windows executable

On **64-bit Windows 10 / 11** you can run QuadML in either of these ways:

| Option | Who it is for | Where to start |
|--------|----------------|----------------|
| **Windows `.exe` installer** | End users who want a ready-to-run app (no Python) | Download from **[www.ai-cvm.org](https://www.ai-cvm.org)** — this page |
| **Install from source** | Developers / contributors who want the full repository | Clone from [GitHub](https://github.com/AI-in-Cardiovascular-Medicine/QuadML), then follow [Install from source](02-install-from-source.md) |

---

## What you download from the website

| Artifact | Description |
|----------|-------------|
| Windows installer (`.exe`) | Setup program from [www.ai-cvm.org](https://www.ai-cvm.org) (e.g. `QuadML_Setup_*.exe`) |

Prefer the official download on **[www.ai-cvm.org](https://www.ai-cvm.org)**. How maintainers build these artifacts is under [Build / package](09-build-and-package.md).

---

## Install with Setup

1. Download the Windows `.exe` from [www.ai-cvm.org](https://www.ai-cvm.org).
2. Run the installer.
3. Follow the wizard (install location, Start Menu / desktop shortcuts).
4. Launch **QuadML** from the Start Menu or desktop shortcut.

---

## Portable / folder build

1. Extract or copy the full `QuadML` folder to a writable location.
2. Run `QuadML.exe` from that folder.
3. Keep the folder intact — do **not** move `QuadML.exe` alone. Search needs `QuadML_Worker.exe` and the bundled `_internal` (and related) files beside it.

---

## Writable user data

The frozen app stores caches, logs, and related data under a **per-user** folder (not under Program Files):

- `%LOCALAPPDATA%\QuadML` (for example logs and `pycox_data`)

**Pipeline outputs** (results, plots, saved models) go to the **Output Directory** you set on File Selection (dated subfolders for each run).

---

## After install

Continue with [First run](05-first-run.md).

If you cloned the repository instead of using the website installer, use [Install from source](02-install-from-source.md), then [First run](05-first-run.md).

---

## Common mistakes

- Copying only `QuadML.exe` without the rest of the freeze folder
- Looking for results under Program Files — use **Output Directory** on File Selection
- Installing a build from an untrusted source (prefer [www.ai-cvm.org](https://www.ai-cvm.org))
- Expecting the `.exe` installer steps when you cloned the repo — use [Install from source](02-install-from-source.md) instead
