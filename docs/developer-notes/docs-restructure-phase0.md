# Docs restructure — Phase 0 (frozen decisions)

Status: **locked for Phase 1+**. Edit this file only if the plan changes on purpose.  
Not published on the docs site (`exclude_docs: developer-notes/`).

Source: `Documentation feedback.docx` + agreed workflow (edit QuadML-private, sync public QuadML docs).

---

## 1. Target navigation (frozen)

```
Home
Getting started
  Installation
  Troubleshooting
Classification
  Overview
  Pipeline
    File selection
    Data cleaning
    Imputation
    Scaling
    Feature selection
    Dimensionality reduction
    Models
    Data splitting
    Parameter tuning
  Results
    Metrics
    Visualization
    Interpretability
  Tutorial
Regression
  (same as Classification)
Survival analysis
  (same as Classification, plus Descriptive analysis in Pipeline before Models)
Clustering
  (same as Classification, but no Data splitting / Interpretability;
   Search settings replaces Parameter tuning)
About
  About QuadML
  Changelog
For developers
  Code structure
  Build and package
  Contributing
```

### Mode exceptions (frozen)

| Mode | Pipeline / Results differences |
|------|--------------------------------|
| Classification | Full pattern above |
| Regression | Same as Classification |
| Survival | + **Descriptive analysis** before Models |
| Clustering | No Data splitting; no Interpretability; **Search settings** instead of Parameter tuning |

### Explicitly out of public user nav

- **Shared** as a top-level section (redundant for users; content becomes snippets and/or For developers)
- Developer file paths / code layout on user-facing Pipeline / Results / Tutorial pages

---

## 2. Snippet root (frozen)

| Decision | Choice |
|----------|--------|
| Snippet directory | `docs/_snippets/` (new; include-only) |
| Public nav | `_snippets` is **not** a nav section |
| Existing `docs/shared/` | Keep as source material during Phase 3; remove from public nav in Phase 1; retire or thin after snippets exist |
| Include syntax | MkDocs `pymdownx.snippets` — e.g. `--8<-- "_snippets/imputation.md"` |
| Task-specific notes | Written on the mode page, **not** inside shared snippets |

Enable in Phase 1: add `pymdownx.snippets` under `markdown_extensions` in `mkdocs.yml`.

---

## 3. Public sync rule (frozen)

| Item | Rule |
|------|------|
| Edit location | `L:\QuadML` → GitHub **QuadML-private** |
| Publish location | `L:\QuadML-docs` → GitHub **QuadML** (public) |
| When to sync | After each publishable milestone (or when ready to update the live site) |
| What to copy | At least `docs/` (except do not require publishing `developer-notes/`), `mkdocs.yml`; plus `README.md` / `.github/workflows/docs.yml` only if those changed for the public site |
| Source of truth for manuals | Private repo until intentionally synced |

Example sync (when publishing):

```powershell
Copy-Item L:\QuadML\mkdocs.yml L:\QuadML-docs\mkdocs.yml -Force
Copy-Item L:\QuadML\docs L:\QuadML-docs\docs -Recurse -Force
cd L:\QuadML-docs
git add mkdocs.yml docs
git commit -m "docs: sync from QuadML-private"
git push
```

---

## Phase 0 exit checklist

- [x] Target nav frozen (section 1)
- [x] Snippet root frozen (`docs/_snippets/`)
- [x] Public sync rule frozen (private edit → public copy)

**Next:** Phase 1 — site plumbing only (`mkdocs.yml` nav + snippets enable + Shared out of nav; no content rewrite yet).

---

## Phase 1 status

Done in private repo:

- `navigation.expand` removed; `pymdownx.snippets` enabled (`base_path: docs`)
- Public nav matches Phase 0 shape; **Shared** removed from nav (files kept for Phase 3)
- `docs/_snippets/` created (excluded from standalone pages)
- Minimal stubs only: `getting-started/installation.md`, `about/changelog.md`, `developers/contributing.md`
- `mkdocs build --strict` succeeds (orphan pages under old getting-started / shared / mode indexes are expected until later phases)

## Phase 2 status

Done:

- Home rewritten as promo landing (what / why / who / downloads / citation)
- Installation merged with Material tabs (Windows / macOS / Linux / From source) + first run + short prepare-data
- Troubleshooting user-first; Rebuild Results once; report-an-issue; technical pins pointed to For developers
- About QuadML + Changelog; Python requirements under For developers nav; Contributing stub filled
- `pymdownx.tabbed` enabled in `mkdocs.yml`

## Phase 3 status

Done:

- Snippet library under `docs/_snippets/` (imputation, scaling, data-cleaning, feature-selection, dimensionality-reduction, data-splitting, search-run, start-stop-resources, results-usage, visualization-usage, interpretability-usage)
- Mode Pipeline / Results / Visualization / Interpretability pages include snippets via `--8<--`; task-specific notes stay on the mode page
- Shared folder kept on disk (out of nav) as legacy source material

## Phase 4 status

Done (Classification = golden template):

- Overview with clinical examples; File selection control table (no long click lists)
- Pipeline pages: purpose + Method/What/When via snippets; ≤1 screenshot; task notes
- Models table (How it works + short code); Parameter tuning includes search + Start/Stop snippets + imbalance
- Metrics / Visualization / Interpretability tables per feedback
- Tutorial = click path with screenshots; snippets updated to What/When (no click steps)

## Phase 5 status

Done (Regression / Survival / Clustering cloned from Classification template):

- Regression: full Pipeline / Results / Tutorial; continuous metrics; residual viz; no class/threshold notes
- Survival: + Descriptive analysis; duration/event File selection; models + KM/NA; survival metrics/viz/interp (SurvSHAP)
- Clustering: Search settings (no Data splitting / Interpretability); unsupervised FS notes; metric + profiling viz tables
- Mode exceptions from Phase 0 preserved; snippets reused; task notes stay on mode pages

## Phase 6 status

Done (For developers):

- `developers/code-structure.md` — process roles (GUI/search/worker) + modules map from Shared
- `developers/python-requirements.md` — pins, conflicts, DeepSurv/pycox/SurvSHAP notes moved off Troubleshooting
- `developers/build-and-package.md` — Windows / macOS / Linux freeze paths
- `developers/contributing.md` — bugs, docs policy, public docs-only vs private application source
- Nav points at `developers/*`; old getting-started/shared paths are short “Moved” stubs (Phase 7 cleanup)
- User Pipeline / Results / Tutorial pages remain free of developer file paths

## Phase 7 status

Done (cleanup):

- Removed `docs/shared/` (snippets + For developers replaced it)
- Removed redundant getting-started pages (old install/first-run/prepare/macos/overview/index/walkthrough + Moved stubs)
- Removed orphan mode `index.md` files
- Mac maintainer notes folded into `developers/python-requirements.md` / `build-and-package.md`
- README docs links updated (no Shared; Mac packaging → For developers)
- Rebuild Results: full wording once in Troubleshooting; snippets keep short mentions only
