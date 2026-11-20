"""Regenerate docs/clustering + docs/assets/cluster from Documentation Clustering.docx."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

DOCX = Path(r"c:\Users\hmirz\Desktop\docs\Documentation Clustering.docx")
DOCS = Path(__file__).resolve().parent
OUT_MD = DOCS / "clustering"
OUT_IMG = DOCS / "assets" / "cluster"

SECTION_FILES = {
    "overview": "00-overview.md",
    "file selection": "01-file-selection.md",
    "data cleaning": "02-data-cleaning.md",
    "imputation": "03-imputation.md",
    "scaling": "04-scaling.md",
    "feature selection": "05-feature-selection.md",
    "dimensionality reduction": "06-dimensionality-reduction.md",
    "clustering models": "07-clustering-models.md",
    "search settings": "08-search-settings.md",
    "results": "09-results.md",
    "visualization": "10-visualization.md",
    "end-to-end walkthrough": "walkthrough.md",
    "walkthrough": "walkthrough.md",
}


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


def section_key(h1: str) -> str | None:
    t = h1.strip().lower()
    t = re.sub(r"^clustering\s*[—\-–]\s*", "", t)
    t = re.sub(r"^quadml\s*[—\-–]\s*", "", t)
    if "user documentation" in t and "left-nav" not in t:
        return "index"
    if "walkthrough" in t or "end-to-end" in t:
        return "walkthrough"
    for key in SECTION_FILES:
        if key in t:
            return key
    if t == "overview" or t.startswith("overview"):
        return "overview"
    return None


def md_heading(level: int, text: str) -> str:
    text = re.sub(r"^clustering\s*[—\-–]\s*", "", text, flags=re.I).strip()
    if level <= 1:
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


def convert() -> None:
    if not DOCX.exists():
        raise SystemExit(f"Missing {DOCX}")

    doc = Document(str(DOCX))
    if OUT_IMG.exists():
        shutil.rmtree(OUT_IMG)
    OUT_IMG.mkdir(parents=True)

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

    sections: dict[str, list[str]] = {k: [] for k in list(SECTION_FILES.values()) + ["index.md"]}
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

        if level == 1 and text:
            key = section_key(text)
            if key == "index":
                current = "index.md"
                sections[current] = [
                    "# Clustering — QuadML user documentation",
                    "",
                ]
                continue
            if key is None:
                current = None
                continue
            fname = SECTION_FILES[key] if key != "walkthrough" else "walkthrough.md"
            current = fname
            if key == "walkthrough":
                title = "# Clustering — end-to-end walkthrough"
            elif key == "overview":
                title = "# Clustering — overview"
            else:
                pretty = key.replace("-", " ").title() if False else text
                pretty = re.sub(r"^clustering\s*[—\-–]\s*", "", text, flags=re.I).strip()
                title = f"# Clustering — {pretty}"
            sections[current] = [title, ""]
            continue

        if not current or current not in sections:
            continue

        if level and text:
            md = md_heading(level, text)
            if md:
                sections[current].append(md)
                sections[current].append("")
            for rid in rids:
                name = ensure_image(rid)
                sections[current].append(f"![](../assets/cluster/{name})")
                sections[current].append("")
            continue

        if text:
            list_styles = {"List Paragraph", "Compact", "ui-markdown__list-item"}
            if style in list_styles or style.startswith("List"):
                sections[current].append(f"- {text}")
            else:
                sections[current].append(text)
                sections[current].append("")

        for rid in rids:
            name = ensure_image(rid)
            alt = Path(name).stem
            sections[current].append(f"![{alt}](../assets/cluster/{name})")
            sections[current].append("")

    # Write pages
    for fname, lines in sections.items():
        if not lines or (len(lines) <= 2 and not any("![" in x for x in lines)):
            # keep index special-cased below
            if fname != "index.md":
                continue
        path = OUT_MD / fname
        path.write_text("\n".join(collapse_blank(lines)), encoding="utf-8")
        print(f"wrote {fname}: {len(lines)} raw lines")

    index_md = """# Clustering — QuadML user documentation

This section documents the **Clustering** mode of QuadML.
It follows the left-nav step order in the GUI.

**App version:** 1.0
**Do not confuse with:** in-app help buttons (**?** / **i**), Metric Explanations, Plot Explanations (those remain inside the app for full metric/plot text).

Screenshots on these pages come from the Clustering Word manual (embedded figures, document order).

---

## Left-nav steps (Clustering)

1. [File Selection](01-file-selection.md)
2. [Data Cleaning](02-data-cleaning.md)
3. [Imputation](03-imputation.md)
4. [Scaling](04-scaling.md)
5. [Feature Selection](05-feature-selection.md)
6. [Dimensionality Reduction](06-dimensionality-reduction.md)
7. [Clustering Models](07-clustering-models.md)
8. [Search Settings](08-search-settings.md)
9. [Results](09-results.md)
10. [Visualization](10-visualization.md)

Also: [Mode overview](00-overview.md) · [End-to-end walkthrough](walkthrough.md)

---

## How to use these pages

- Screenshots are embedded next to the matching GUI step.
- Clustering has **no Data Splitting**, **no Parameter Tuning** page name (use **Search Settings**), and **no Interpretability** page.
- Clustering also hides **External Test Data**, the **ID Column** picker, sample-level cleaning, and Correlation Analysis on Data Cleaning. **Exact Duplicate Rows** and **Missing / Outlier Threshold** remain available.
- Clustering Models is a **two-panel** page: cluster-count models share **Number of clusters**; the **Density-Based** panel (HDBSCAN / DBSCAN / OPTICS) ignores that setting. Density hyperparameters are data-derived during search and ranked by **DISCO** (DBCV is still reported).
- For numeric definitions of metrics and plots, open **Metric Explanations** / **Plot Explanations** in the running app after a search.
"""
    (OUT_MD / "index.md").write_text(index_md, encoding="utf-8")
    print("wrote index.md (nav template)")
    print(f"images extracted: {img_seq}")


if __name__ == "__main__":
    convert()
