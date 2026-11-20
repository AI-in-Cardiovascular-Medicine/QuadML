# Getting started — macOS notes

macOS is a **supported packaged path** on **Apple Silicon**: install from source, or use the CI-built **`QuadML.app`**. Packaging helpers live in `src/shared/app/mac_modifications.py`.

---

## Source install on macOS

Clone from [GitHub](https://github.com/AI-in-Cardiovascular-Medicine/QuadML) and follow [Install from source](02-install-from-source.md), using the **Mac** requirements file:

1. Python **3.9–3.12** (CI uses **3.11**).
2. `python3 -m venv .venv` → activate → `pip install -r requirements-mac.txt`.
3. `python src/verify_quadml_bundle.py`.
4. `python src/quadml_entry.py`.

**Why `requirements-mac.txt`?** `PyQt5==5.15.9` has no macOS arm64 wheel. The Mac file pins **PyQt5==5.15.11**. Pin helpers live in `src/shared/app/mac_modifications.py`. Do **not** use `requirements.txt` alone on Apple Silicon.

Apple Silicon: prefer arm64 wheels from PyPI; first install of torch can be large.

---

## Packaged `.app` (maintainers / CI)

Supported Mac freeze. Canonical step lists: `shared.app.mac_modifications.mac_maintainer_ci_build_steps()` / `mac_release_attach_steps()` / `mac_end_user_unsigned_open_steps()`.

Summary:

- Spec: `src/QuadML_mac.spec`
- Workflow: **Build macOS app** (`workflow_dispatch`, **`macos-15`**, Python `architecture: arm64`)
- Architecture: **arm64 only** (`target_arch='arm64'` in `QuadML_mac.spec`). The workflow runs `assert_mac_app_arm64` and fails if any Mach-O inside `QuadML.app` has no arm64 slice. That stops macOS from showing **Finding software** (Rosetta) when a search worker starts. An older Intel `.app` still does that — replace it with this build.
- Deps: committed **`requirements-mac.txt`** (via `assert_mac_requirements_file`)
- Artifact: **QuadML-macOS-app**[-date-sha] → `QuadML-macOS.app.zip`
- Durable channel: **GitHub Releases** (attach the same zip — see below)
- Signing: currently **unsigned** (codesign/notarization are a later step)

### Maintainer flow (GitHub Actions)

1. Commit/push Mac packaging inputs (`QuadML_mac.spec`, `requirements-mac.txt`, Mac workflow).
2. GitHub → **Actions** → **Build macOS app** → **Run workflow** (long run; full ML stack; runner **macos-15** / Apple Silicon).
3. Open the green run → **Artifacts** → download **QuadML-macOS-app** (name may include `-YYYYMMDD-sha`).
4. Extract `QuadML-macOS.app.zip` → `QuadML.app`.
5. On an Apple Silicon Mac: **Right-click → Open** (Gatekeeper).
6. Smoke: Welcome → short Classification/Clustering → **Stop**; check Output Directory; logs under `~/Library/Application Support/QuadML/logs` if needed.

### Durable distribution (GitHub Releases)

Actions artifacts expire (~14 days). For each version tag / release, attach `QuadML-macOS.app.zip` so Mac users keep a permanent download. Canonical list: `mac_release_attach_steps()`.

1. Obtain `QuadML-macOS.app.zip` (from the Actions artifact above).
2. Create or open the GitHub Release for that version tag.
3. Attach `QuadML-macOS.app.zip` (UI drag-and-drop, or `gh release upload vX.Y.Z QuadML-macOS.app.zip --clobber`).
4. Publish the release.
5. Note in the release body that the Mac build is **unsigned** (Right-click → Open) until notarization.

Automated `gh release upload` from CI is optional later; the manual attach is the supported durable path today.

### End-user open (unsigned zip)

1. Extract the zip you received.
2. Put `QuadML.app` somewhere convenient (e.g. Applications).
3. First launch: Right-click → **Open** → confirm the Gatekeeper dialog.
4. Later launches can use double-click once allowed.
5. Expect a large download / disk footprint.

More packaging context: [Build / package](09-build-and-package.md).

---

## Resource Usage on Mac (soft throttle)

**Resource Usage** (CPU% / RAM%) still sets the search plan. On macOS, QuadML adds a **soft** throttle in `shared.app.mac_modifications`: it can shrink concurrency or wait before the next combination under pressure. It does **not** kill a combination that is already running.

### Planning

- Outer width = floor of **(user RAM budget = RAM% × machine RAM) ÷ per-combo estimate**. Machine size is **not** a hard switch (e.g. a 16 GB Mac is not forced to 1×1).
- Per-combo RAM estimate is scaled up on Darwin (**× 2.2**) because frozen `.app` workers are heavier.
- **Inner** jobs follow the **RAM%** slider: low → inner 1; mid → inner ≤ 2; high → leftover cores uncapped.
- System RAM guard is earlier on Mac (**80%** machine RAM → throttle red).

### Adaptive behaviour (Mac only)

- With Adaptive on, the **first wave starts at 1×1**; Adaptive may raise toward the slider plan only while RAM stays green (`mac_adaptive_start_outer` / `mac_adaptive_start_inner`). Outer does **not** increase on yellow/orange/red RAM (`mac_should_block_outer_increase`).
- When outer is already at 1, orange/red RAM may shrink **inner** further (`mac_should_shrink_inner_on_ram_red`).
- Between waves, high RAM pressure can **defer** the next combo (~5 s) or clamp this wave’s outer to 1 (`mac_should_defer_next_combo` / `mac_clamp_wave_outer`).
- Frozen explicit-role pools spawn only the **current** outer count (`mac_explicit_role_pool_size`), not unused capacity.

### Memory sampling

- Process RAM uses **`proc_pid_rusage` / `ri_phys_footprint`** (same ledger as Activity Monitor / jetsam), not fragile `task_for_pid`.
- Search/worker siblings are attached so Adaptive and the Resource chip see one tree.
- Adaptive **resamples during a combo wave** (about every 4 s), not only between waves, so the line is not stuck at `CPU 0.00 · RAM 0.00`.

If Activity Monitor climbs, lower Resource Usage % and prefer a Fast budget with fewer models for first smoke runs. Status helpers: `mac_resource_soft_throttle_status()` / `mac_memory_sampling_method()`.

---

## SurvSHAP on packaged Mac (H11)

Policy **H11**: while `MAC_SURVSHAP_H11_FORCE_SERIAL` is on, a **frozen** macOS `.app` forces SurvSHAP Compute to **`n_jobs=1`**. Enforcement is `mac_survshap_effective_n_jobs()` in `survshap_explainer` (backend stays **loky** on every OS). Canonical text: `mac_survshap_h11_status()` / `mac_survshap_h11_doc_bullets()`.

- **Frozen Mac only** — serial until Darwin loky workers are verified; expect slower Compute than parallel runs
- **Source Mac / Windows / Linux** (including frozen Windows/Linux) — parallel SurvSHAP unchanged
- Frozen spawn path still uses the **GUI binary** (`QuadML`) with `popen_loky_posix` / **Agg**, not `QuadML_Worker` (same design as Windows)
- Logs: `~/Library/Application Support/QuadML/logs` if a SurvSHAP run fails

---

## Writable user data

On macOS, per-user data defaults under:

`~/Library/Application Support/QuadML`

| Subfolder | Contents |
|-----------|----------|
| `logs/` | Frozen / worker / early stdio logs (`quadml_*.log`, `quadml_worker_*.log`) |
| `pycox_data/` | Writable pycox datasets (DeepSurv) |

---

## Common mistakes

- Expecting a notarized Mac App Store–style installer (not documented as the default release path)
- Relying only on Actions artifacts for Mac distribution (they expire; use GitHub Releases)
- Mixing x86_64 and arm64 Python environments
- Installing with `requirements.txt` on Apple Silicon (use `requirements-mac.txt` instead)
- Looking for Mac logs under `%LOCALAPPDATA%` (use Application Support instead)
- Expecting packaged-Mac SurvSHAP to be as fast as Windows (H11 forces `n_jobs=1` on frozen `.app` until Darwin parallel is verified)
