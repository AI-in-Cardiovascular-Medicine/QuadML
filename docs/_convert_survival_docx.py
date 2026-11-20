"""Regenerate docs/survival + docs/assets/sa from Survival Documentation.docx."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

DOCX = Path(r"c:\Users\hmirz\Desktop\docs\Survival Documentation.docx")
DOCS = Path(__file__).resolve().parent
OUT_MD = DOCS / "survival"
OUT_IMG = DOCS / "assets" / "sa"

# GUI / Word body order (DR after Feature Selection).
SECTION_FILES = {
    "overview": "00-overview.md",
    "file selection": "01-file-selection.md",
    "data cleaning": "02-data-cleaning.md",
    "imputation": "03-imputation.md",
    "scaling": "04-scaling.md",
    "feature selection": "05-feature-selection.md",
    "dimensionality reduction": "06-dimensionality-reduction.md",
    "descriptive analysis": "07-descriptive-analysis.md",
    "survival models": "08-survival-models.md",
    "data splitting": "09-data-splitting.md",
    "parameter tuning": "10-parameter-tuning.md",
    "results": "11-results.md",
    "visualization": "12-visualization.md",
    "interpretability": "13-interpretability.md",
    "walkthrough": "walkthrough.md",
}

SECTION_ORDER = [
    "overview",
    "file selection",
    "data cleaning",
    "imputation",
    "scaling",
    "feature selection",
    "dimensionality reduction",
    "descriptive analysis",
    "survival models",
    "data splitting",
    "parameter tuning",
    "results",
    "visualization",
    "interpretability",
    "walkthrough",
]


def style_name(paragraph: Paragraph) -> str:
    try:
        return paragraph.style.name if paragraph.style else ""
    except Exception:
        return ""


def para_text(paragraph: Paragraph) -> str:
    return paragraph.text.replace("\xa0", " ").strip()


def heading_level(style: str) -> int | None:
    if style == "Title":
        return 1
    m = re.match(r"Heading\s*(\d+)", style or "", re.I)
    return int(m.group(1)) if m else None


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def table_to_md(table: Table) -> str:
    rows = []
    for row in table.rows:
        cells = [escape_cell(c.text.replace("\xa0", " ")) for c in row.cells]
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header = rows[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join("---" for _ in header) + " |",
    ]
    for r in rows[1:]:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def iter_block_items(doc: Document):
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, doc)
        elif child.tag == qn("w:tbl"):
            yield Table(child, doc)


def blip_rids(paragraph: Paragraph) -> list[str]:
    rids = []
    A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
    R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    for blip in paragraph._element.findall(f".//{{{A_NS}}}blip"):
        rid = blip.get(f"{{{R_NS}}}embed")
        if rid:
            rids.append(rid)
    return rids


def normalize_dashes(text: str) -> str:
    return text.replace("–", "—").replace("-", "—")


def section_key(text: str) -> str | None:
    t = text.strip()
    tl = normalize_dashes(t).lower()
    tl = re.sub(r"^\d+\.\s*", "", tl)
    tl = re.sub(r"^survival analysis\s*—\s*", "", tl)
    tl = tl.strip(" .")

    if "user documentation" in tl and "left-nav" not in tl:
        return "index"
    if "walkthrough" in tl or "end-to-end" in tl:
        return "walkthrough"
    if tl in ("overview",) or tl.startswith("overview"):
        return "overview"

    for key in SECTION_ORDER:
        if key == "overview":
            continue
        if key in tl and "quadml user" not in tl:
            # Avoid matching "Survival Models" inside longer unrelated lines.
            if key == "survival models" and "where:" in tl:
                return key
            if len(tl) < 80 or key in ("dimensionality reduction", "descriptive analysis", "parameter tuning", "interpretability"):
                return key
    return None


def looks_like_section_title(text: str, style: str) -> bool:
    if not text:
        return False
    t = normalize_dashes(text)
    low = t.lower()
    # Never treat "Where: …" breadcrumbs as section titles
    if low.startswith("where:"):
        return False
    if re.match(r"^\d+\.\s*survival_analysis\s*—", t, re.I):
        return True
    if re.match(r"^survival_analysis\s*—\s*", t, re.I) and len(t) < 90:
        # e.g. "Survival Analysis — Parameter Tuning"
        rest = re.sub(r"^survival_analysis\s*—\s*", "", t, flags=re.I).strip().lower()
        return any(k == rest or rest.startswith(k) for k in SECTION_ORDER if k != "overview")
    if style.startswith("Heading") and section_key(text):
        return True
    # Compact / Body Text section titles in this Word export (exact-ish matches only)
    compact_hits = {
        "survival analysis – imputation",
        "survival analysis — imputation",
        "survival analysis – scaling",
        "survival analysis — scaling",
        "survival analysis – feature selection",
        "survival analysis — feature selection",
        "5. survival analysis – feature selection",
        "5. survival analysis — feature selection",
        "6. survival analysis — dimensionality reduction",
        "6. survival analysis – dimensionality reduction",
        "7. survival analysis – descriptive analysis",
        "7. survival analysis — descriptive analysis",
        "survival analysis – descriptive analysis",
        "survival analysis — descriptive analysis",
        "survival analysis – survival models",
        "survival analysis — survival models",
        "survival analysis – data splitting",
        "survival analysis — data splitting",
        "12. survival analysis - results",
        "12. survival analysis — results",
        "survival analysis - results",
        "survival analysis — results",
        "survival analysis – results",
        "13. survival analysis – visualization",
        "survival analysis – visualization",
        "survival analysis — visualization",
    }
    # Normalize en/em dashes and hyphen variants for lookup
    norm = low.replace("–", "—").replace("-", "—")
    compact_norm = {h.replace("–", "—").replace("-", "—") for h in compact_hits}
    return low in compact_hits or norm in compact_norm


def md_heading(level: int, text: str) -> str:
    text = re.sub(r"^\d+\.\s*", "", text).strip()
    text = re.sub(r"^survival_analysis\s*[—\-–]\s*", "", text, flags=re.I).strip()
    if level <= 1:
        return ""
    # Skip redundant section-title-as-H2 when already used as page H1
    if section_key("Survival Analysis — " + text) and level == 2 and text.lower() in SECTION_FILES:
        return ""
    return f"{'#' * level} {text}"


def collapse_blank(lines: list[str]) -> list[str]:
    out: list[str] = []
    blank = 0
    for line in lines:
        if line == "":
            blank += 1
            if blank <= 1:
                out.append("")
        else:
            blank = 0
            out.append(line)
    while out and out[-1] == "":
        out.pop()
    out.append("")
    return out


def page_title(key: str, raw: str) -> str:
    pretty = re.sub(r"^\d+\.\s*", "", raw).strip()
    pretty = re.sub(r"^survival_analysis\s*[—\-–]\s*", "", pretty, flags=re.I).strip()
    if key == "overview":
        return "# Survival Analysis — overview"
    if key == "walkthrough":
        return "# Survival Analysis — end-to-end walkthrough"
    if not pretty or pretty.lower() == key:
        pretty = key.replace("-", " ").title() if False else key.title()
        pretty = {
            "file selection": "File Selection",
            "data cleaning": "Data Cleaning",
            "imputation": "Imputation",
            "scaling": "Scaling",
            "feature selection": "Feature Selection",
            "dimensionality reduction": "Dimensionality Reduction",
            "descriptive analysis": "Descriptive Analysis",
            "survival models": "Survival Models",
            "data splitting": "Data Splitting",
            "parameter tuning": "Parameter Tuning",
            "results": "Results",
            "visualization": "Visualization",
            "interpretability": "Interpretability",
        }.get(key, pretty)
    return f"# Survival Analysis — {pretty}"


def polish_pages() -> None:
    """Fix Word/export quirks so docs match the GUI (DR exists)."""
    overview = OUT_MD / "00-overview.md"
    if overview.exists():
        text = overview.read_text(encoding="utf-8")
        # Insert DR into workflow table if missing
        if "Dimensionality Reduction" not in text:
            text = text.replace(
                "| 5 | Feature Selection | Survival-aware FS methods (or None) |\n"
                "| 6 | Descriptive Analysis | Kaplan-Meier / Nelson-Aalen (no covariates) |\n"
                "| 7 | Survival Models | Cox, AFT, RSF, DeepSurv, … |\n"
                "| 8 | Data Splitting | Train/Test (or Train on all + External) |\n"
                "| 9 | Parameter Tuning | Search settings + Start Procedure |\n"
                "| 10 | Results | Pipeline metrics (Final_Results.csv) |\n"
                "| 11 | Visualization | KM, calibration, risk groups, td-AUC, … |\n"
                "| 12 | Interpretability | SurvSHAP, SurvivalLIME, Cox/AFT coefficients, … |",
                "| 5 | Feature Selection | Survival-aware FS methods (or None) |\n"
                "| 6 | Dimensionality Reduction | PCA / ICA / Kernel PCA (or None) |\n"
                "| 7 | Descriptive Analysis | Kaplan-Meier / Nelson-Aalen (no covariates) |\n"
                "| 8 | Survival Models | Cox, AFT, RSF, DeepSurv, … |\n"
                "| 9 | Data Splitting | Train/Test (or Train on all + External) |\n"
                "| 10 | Parameter Tuning | Search settings + Start Procedure |\n"
                "| 11 | Results | Pipeline metrics (Final_Results.csv) |\n"
                "| 12 | Visualization | KM, calibration, risk groups, td-AUC, … |\n"
                "| 13 | Interpretability | SurvSHAP, SurvivalLIME, Cox/AFT coefficients, … |",
            )
        # Differences list: replace no-DR claim if present; else ensure DR is mentioned
        text = text.replace(
            "- No Dimensionality Reduction page\n",
            "- Dimensionality Reduction (None / PCA / ICA / Kernel PCA) after Feature Selection; LDA is not available\n",
        )
        if "Dimensionality Reduction (None" not in text and "What is different" in text:
            text = text.replace(
                "- Descriptive Analysis page for Kaplan-Meier and Nelson-Aalen\n",
                "- Descriptive Analysis page for Kaplan-Meier and Nelson-Aalen\n"
                "- Dimensionality Reduction (None / PCA / ICA / Kernel PCA) after Feature Selection; LDA is not available\n",
            )
        # Suggested config: include DR None; prefer Fast from Word
        text = text.replace(
            "- Imputation: Simple Imputation; Scaling: Standard Scaler; FS: None (Not when the number of features is high)",
            "- Imputation: **Simple Imputation**; Scaling: **Standard Scaler**; FS: **None** (use FS when features are many); DR: **None**",
        )
        text = text.replace(
            "- Imputation: **Simple Imputation**; Scaling: **Standard Scaler**; FS: **None**; DR: **None** (Not when the number of features is high)",
            "- Imputation: **Simple Imputation**; Scaling: **Standard Scaler**; FS: **None** (use FS when features are many); DR: **None**",
        )
        text = text.replace(
            "- KM / Nelson-Aalen do not use imputation, scaling, or FS (N/A (not used) on results) and have no Interpretability\n## Suggested",
            "- KM / Nelson-Aalen do not use imputation, scaling, FS, or DR (`N/A (not used)` on results) and have no Interpretability\n\n## Suggested",
        )
        if "Then follow" not in text:
            text = text.rstrip() + "\n\nThen follow the [walkthrough](walkthrough.md).\n"
        overview.write_text(text, encoding="utf-8")

    fs = OUT_MD / "05-feature-selection.md"
    if fs.exists():
        text = fs.read_text(encoding="utf-8")
        text = text.replace(
            "There is **no Dimensionality Reduction** page in Survival.",
            "Dimensionality Reduction is the **next** page (None / PCA / ICA / Kernel PCA).",
        )
        text = text.replace(
            "There is no Dimensionality Reduction page in Survival.",
            "Dimensionality Reduction is the next page (None / PCA / ICA / Kernel PCA).",
        )
        text = text.replace(
            "Looking for PCA / LDA on this page (Survival has no DR page)",
            "Looking for PCA / ICA / Kernel PCA on this page (those live under Dimensionality Reduction; LDA is not in Survival)",
        )
        fs.write_text(text, encoding="utf-8")

    # Ensure walkthrough mentions DR
    wt = OUT_MD / "walkthrough.md"
    if not wt.exists():
        wt.write_text(
            """# Survival Analysis — end-to-end walkthrough

One happy path. Use a table with a duration column, an event/censor column, and features.

## 1. Start

1. Open QuadML → **Survival Analysis** → **File Selection**.
2. **Select File → Browse** and set **Output Directory**.
3. Set **Duration Column** and **Event / Censor Column** (**Auto-Detect** if names are obvious).
4. Set **Event Coding** so 1 means event observed unless your file is coded the other way.
5. Leave **Eval. Horizons** on **Auto from follow-up**.
6. Optional: ID Column; External file must also have duration + event.

## 2. Preprocess (keep it small)

| Step | Choice |
|------|--------|
| Data Cleaning | None (or one feature-level method) |
| Imputation | Simple Imputation |
| Scaling | Standard Scaler |
| Feature Selection | None |
| Dimensionality Reduction | None |

## 3. Models

- **Descriptive Analysis:** Kaplan-Meier
- **Survival Models:** Cox Proportional Hazards

You can run descriptive only, covariate only, or both. Start Procedure needs at least one model on either page.

## 4. Split and run

1. **Data Splitting:** 80/20, Train on all data off.
2. **Parameter Tuning:** Random Search or Grid Search, **Fast** budget, CPU/RAM 50/50.
3. Review the configuration tree → **Start Procedure**.

## 5. Read output

1. **Results:** open **Metric Explanations**. Do not pick by C-index alone if absolute risk matters — check Mean Calibration, Slope, and ICI, then Test C-index among well-calibrated rows.
2. **Visualization:** Risk Group KM and Calibration Plot for the Cox pipeline; KM curve for Kaplan-Meier.
3. **Interpretability:** Load the Cox `.pkl` + matching CSVs; try Cox Coefficients and/or SurvSHAP.

You should find `Final_Results.csv` under `YourFolder\\YYYY-MM-DD_HH-MM-SS\\`.
""",
            encoding="utf-8",
        )
    else:
        text = wt.read_text(encoding="utf-8")
        text = text.replace("(No Dimensionality Reduction page.)\n", "")
        text = text.replace(
            "| Feature Selection | None |\n\n",
            "| Feature Selection | None |\n| Dimensionality Reduction | None |\n\n",
        )
        if "Dimensionality Reduction | None" not in text:
            text = text.replace(
                "| Feature Selection | None |",
                "| Feature Selection | None |\n| Dimensionality Reduction | None |",
            )
        wt.write_text(text, encoding="utf-8")


def write_index() -> None:
    index_md = """# Survival Analysis — QuadML user documentation

This section documents the **Survival Analysis** mode of QuadML.
It follows the left-nav step order in the GUI.

**App version:** 1.0
**Do not confuse with:** in-app help buttons (**?** / **i**), Metric Explanations, Plot Explanations (those remain inside the app for full metric/plot text).

Screenshots on these pages come from the Survival Word manual (embedded figures, document order).

---

## Left-nav steps (Survival Analysis)

1. [File Selection](01-file-selection.md)
2. [Data Cleaning](02-data-cleaning.md)
3. [Imputation](03-imputation.md)
4. [Scaling](04-scaling.md)
5. [Feature Selection](05-feature-selection.md)
6. [Dimensionality Reduction](06-dimensionality-reduction.md)
7. [Descriptive Analysis](07-descriptive-analysis.md)
8. [Survival Models](08-survival-models.md)
9. [Data Splitting](09-data-splitting.md)
10. [Parameter Tuning](10-parameter-tuning.md)
11. [Results](11-results.md)
12. [Visualization](12-visualization.md)
13. [Interpretability](13-interpretability.md)

Also: [Mode overview](00-overview.md) · [End-to-end walkthrough](walkthrough.md)

---

## How to use these pages

- Screenshots are embedded next to the matching GUI step.
- Survival includes **Dimensionality Reduction** (None / PCA / ICA / Kernel PCA) after Feature Selection. **LDA** is not available. Kaplan–Meier / Nelson–Aalen skip imputation, scaling, FS, and DR.
- For numeric definitions of metrics and plots, open **Metric Explanations** / **Plot Explanations** in the running app after a search.
"""
    (OUT_MD / "index.md").write_text(index_md, encoding="utf-8")


def convert() -> None:
    if not DOCX.exists():
        raise SystemExit(f"Missing {DOCX}")

    doc = Document(str(DOCX))
    if OUT_IMG.exists():
        shutil.rmtree(OUT_IMG)
    OUT_IMG.mkdir(parents=True)

    # Remove old survival pages so renumbered files do not linger.
    # Keep walkthrough.md text if Word has no walkthrough section (polish may refresh it).
    saved_walkthrough = None
    if OUT_MD.exists():
        wt_path = OUT_MD / "walkthrough.md"
        if wt_path.exists():
            saved_walkthrough = wt_path.read_text(encoding="utf-8")
        for p in OUT_MD.glob("*.md"):
            p.unlink()
    else:
        OUT_MD.mkdir(parents=True)

    rid_to_name: dict[str, str] = {}
    img_seq = 0

    def ensure_image(rid: str) -> str:
        nonlocal img_seq
        if rid in rid_to_name:
            return rid_to_name[rid]
        blob = doc.part.rels[rid].target_part.blob
        name = f"{img_seq}.png"
        if blob[:3] == b"\xff\xd8\xff":
            name = f"{img_seq}.jpg"
        (OUT_IMG / name).write_bytes(blob)
        rid_to_name[rid] = name
        img_seq += 1
        return name

    sections: dict[str, list[str]] = {fname: [] for fname in SECTION_FILES.values()}
    current: str | None = None

    for block in iter_block_items(doc):
        if isinstance(block, Table):
            if current and current in sections:
                sections[current].append(table_to_md(block))
                sections[current].append("")
            continue

        paragraph = block
        text = para_text(paragraph)
        style = style_name(paragraph)
        level = heading_level(style)
        rids = blip_rids(paragraph)

        if text and looks_like_section_title(text, style):
            key = section_key(text)
            if key == "index":
                current = None
                continue
            if key is None:
                current = None
                continue
            fname = SECTION_FILES[key]
            current = fname
            sections[current] = [page_title(key, text), ""]
            continue

        if not current or current not in sections:
            continue

        if level and text:
            # Avoid reprinting the page H1 as an H2
            md = md_heading(level, text)
            if md and not md.lower().endswith(current.replace(".md", "").split("-", 1)[-1].replace("-", " ")):
                # Filter empty / duplicate titles
                title_only = re.sub(r"^#+\s*", "", md).strip().lower()
                page_stub = re.sub(r"^\d+-", "", current.replace(".md", "")).replace("-", " ")
                if title_only != page_stub and "survival analysis —" not in title_only:
                    sections[current].append(md)
                    sections[current].append("")
            for rid in rids:
                name = ensure_image(rid)
                sections[current].append(f"![{Path(name).stem}](../assets/sa/{name})")
                sections[current].append("")
            continue

        if text:
            list_styles = {
                "List Paragraph",
                "Compact",
                "ui-markdown__list-item",
            }
            if style in list_styles or style.startswith("List"):
                sections[current].append(f"- {text}")
            else:
                sections[current].append(text)
                sections[current].append("")

        for rid in rids:
            name = ensure_image(rid)
            sections[current].append(f"![{Path(name).stem}](../assets/sa/{name})")
            sections[current].append("")

    for fname, lines in sections.items():
        if not lines:
            continue
        path = OUT_MD / fname
        path.write_text("\n".join(collapse_blank(lines)), encoding="utf-8")
        print(f"wrote {fname}: {len(lines)} raw lines")

    write_index()
    if saved_walkthrough and not (OUT_MD / "walkthrough.md").exists():
        (OUT_MD / "walkthrough.md").write_text(saved_walkthrough, encoding="utf-8")
    polish_pages()
    # Light formatting on DR page
    dr = OUT_MD / "06-dimensionality-reduction.md"
    if dr.exists():
        t = dr.read_text(encoding="utf-8")
        t = t.replace(
            "Where: Survival Analysis → Dimensionality Reduction\n\n"
            "This page compresses covariates after Feature Selection and before the survival model:\n\n"
            "Order: Imputation → Scaling → Feature Selection → Dimensionality Reduction → Survival model\n\n"
            "- None — keep selected features as they are (default)\n"
            "- PCA — linear principal components\n"
            "- ICA — independent components\n"
            "- Kernel PCA — non-linear PCA (rbf, poly, sigmoid, cosine)\n"
            "![23](../assets/sa/23.png)",
            "**Where:** Survival Analysis → **Dimensionality Reduction**\n\n"
            "This page compresses covariates after Feature Selection and before the survival model.\n\n"
            "**Order:** Imputation → Scaling → Feature Selection → Dimensionality Reduction → Survival model\n\n"
            "- **None** — keep selected features as they are (default)\n"
            "- **PCA** — linear principal components\n"
            "- **ICA** — independent components\n"
            "- **Kernel PCA** — non-linear PCA (rbf, poly, sigmoid, cosine)\n\n"
            "![Dimensionality Reduction methods](../assets/sa/23.png)",
        )
        t = t.replace(
            "LDA is not available here. DR methods are unsupervised (they do not use event/duration). Kaplan–Meier and Nelson–Aalen do not use this step.\n",
            "**LDA** is not available here. DR methods are unsupervised (they do not use event/duration). Kaplan–Meier and Nelson–Aalen do not use this step.\n",
        )
        t = t.replace(
            "Continue to Survival Models, then Start Procedure.\n\n![24](../assets/sa/24.png)",
            "Continue to **Descriptive Analysis** / **Survival Models**, then **Start Procedure**.\n\n"
            "![Dimensionality Reduction configs](../assets/sa/24.png)",
        )
        dr.write_text(t, encoding="utf-8")
    print("wrote index.md + polish")
    print(f"images extracted: {img_seq}")


if __name__ == "__main__":
    convert()
