"""Regenerate docs/classification + docs/assets/class from Classification Documentation.docx."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

DOCX = Path(r"c:\Users\hmirz\Desktop\docs\Classification Documentation.docx")
DOCS = Path(__file__).resolve().parent
OUT_MD = DOCS / "classification"
OUT_IMG = DOCS / "assets" / "class"

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

SECTION_FILES = {
    1: "00-overview.md",
    2: "01-file-selection.md",
    3: "02-data-cleaning.md",
    4: "03-imputation.md",
    5: "04-scaling.md",
    6: "05-feature-selection.md",
    7: "06-dimensionality-reduction.md",
    8: "07-classifiers.md",
    9: "08-data-splitting.md",
    10: "09-parameter-tuning.md",
    11: "10-results.md",
    12: "11-visualization.md",
    13: "12-interpretability.md",
    14: "index.md",
    15: "walkthrough.md",
}

H1_RE = re.compile(
    r"^(?:Classification User Documentation[^\n]*|"
    r"(\d+)\.\s*classification\s*[—\-–]\s*(.+))$",
    re.I,
)


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
    for blip in paragraph._element.findall(f".//{{{A_NS}}}blip"):
        rid = blip.get(f"{{{R_NS}}}embed")
        if rid:
            rids.append(rid)
    return rids


def save_image(doc: Document, rid: str, dest: Path) -> None:
    rel = doc.part.rels[rid]
    data = rel.target_part.blob
    dest.write_bytes(data)


def section_number(text: str) -> tuple[int | None, str]:
    m = re.match(r"^(\d+)\.\s*classification\s*[—\-–]\s*(.+)$", text, re.I)
    if m:
        return int(m.group(1)), m.group(2).strip()
    if re.search(r"User Documentation", text, re.I) and "Classification" in text:
        return 0, "intro"
    return None, text


def md_heading(level: int, text: str) -> str:
    # Drop leading "N. Classification —" noise inside page titles
    text = re.sub(r"^\d+\.\s*classification\s*[—\-–]\s*", "", text, flags=re.I)
    text = text.strip()
    if level == 1:
        # page title set separately
        return ""
    return f"{'#' * level} {text}"


def boldify_gui_terms(text: str) -> str:
    # Keep plain; Word already has structure. Light cleanup only.
    return text


def convert() -> None:
    if not DOCX.exists():
        raise SystemExit(f"Missing {DOCX}")

    doc = Document(str(DOCX))

    if OUT_IMG.exists():
        shutil.rmtree(OUT_IMG)
    OUT_IMG.mkdir(parents=True)

    # rid -> ClassNN.png (reuse when same rid appears twice)
    rid_to_name: dict[str, str] = {}
    img_seq = 0

    sections: dict[int, list[str]] = {k: [] for k in SECTION_FILES}
    # 0 = preamble / TOC before section 1
    current = 0
    pending_title: dict[int, str] = {}

    def ensure_image(rid: str) -> str:
        nonlocal img_seq
        if rid in rid_to_name:
            return rid_to_name[rid]
        img_seq += 1
        name = f"Class{img_seq:02d}.png"
        # preserve original extension if not png
        rel = doc.part.rels[rid]
        content_type = getattr(rel.target_part, "content_type", "") or ""
        blob = rel.target_part.blob
        if "jpeg" in content_type or blob[:3] == b"\xff\xd8\xff":
            name = f"Class{img_seq:02d}.jpg"
        elif "gif" in content_type:
            name = f"Class{img_seq:02d}.gif"
        elif "emf" in content_type or "wmf" in content_type:
            name = f"Class{img_seq:02d}.bin"
        path = OUT_IMG / name
        path.write_bytes(blob)
        rid_to_name[rid] = name
        return name

    for block in iter_block_items(doc):
        if isinstance(block, Table):
            if current in sections:
                sections[current].append(table_to_md(block))
                sections[current].append("")
            continue

        paragraph = block
        text = para_text(paragraph)
        style = style_name(paragraph)
        level = heading_level(style)
        rids = blip_rids(paragraph)

        if level == 1 and text:
            num, title = section_number(text)
            if num is None:
                # Title / unnumbered H1
                if "Table of Contents" in text:
                    current = 0
                    continue
                if "User Documentation" in text:
                    current = 0
                    continue
                current = 0
                continue
            if num == 0:
                current = 0
                continue
            current = num
            pending_title[num] = title
            # Start page with H1
            page_title = title
            if num == 14:
                sections[current].append("# Classification — QuadML user documentation")
            elif num == 15:
                sections[current].append("# Classification — end-to-end walkthrough")
            else:
                sections[current].append(f"# Classification — {page_title}")
            sections[current].append("")
            continue

        if current not in sections:
            # Preamble / TOC — ignore text and images until numbered H1 sections.
            continue

        if level and text:
            md = md_heading(level, text)
            if md:
                sections[current].append(md)
                sections[current].append("")
            for rid in rids:
                name = ensure_image(rid)
                sections[current].append(f"![](../assets/class/{name})")
                sections[current].append("")
            continue

        if text:
            list_styles = {
                "List Paragraph",
                "Compact",
                "ui-markdown__list-item",
            }
            if style in list_styles or style.startswith("List"):
                sections[current].append(f"- {boldify_gui_terms(text)}")
            else:
                sections[current].append(boldify_gui_terms(text))
                sections[current].append("")

        for rid in rids:
            name = ensure_image(rid)
            alt = text[:80] if text else Path(name).stem
            # Prefer clean ClassNN alt text over truncated caption leftovers
            if alt.startswith("Decision Threshold") or len(alt) > 60:
                alt = Path(name).stem
            sections[current].append(f"![{alt}](../assets/class/{name})")
            sections[current].append("")

    # Write section files; skip empty preamble. Index is written from a fixed template.
    for num, fname in SECTION_FILES.items():
        if num == 14:
            continue
        lines = sections.get(num, [])
        # Collapse excessive blank lines
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
        path = OUT_MD / fname
        path.write_text("\n".join(out), encoding="utf-8")
        print(f"wrote {fname}: {len(out)} lines")

    index_md = """# Classification — QuadML user documentation

This section documents the **Classification** mode of QuadML.
It follows the left-nav step order in the GUI.

**App version:** 1.0
**Do not confuse with:** in-app help buttons (**?** / **i**), Metric Explanations, Plot Explanations (those remain inside the app for full metric/plot text).

Screenshots on these pages come from the Classification Word manual (embedded figures, document order).

---

## Left-nav steps (Classification)

1. [File Selection](01-file-selection.md)
2. [Data Cleaning](02-data-cleaning.md)
3. [Imputation](03-imputation.md)
4. [Scaling](04-scaling.md)
5. [Feature Selection](05-feature-selection.md)
6. [Dimensionality Reduction](06-dimensionality-reduction.md)
7. [Classifiers](07-classifiers.md)
8. [Data Splitting](08-data-splitting.md)
9. [Parameter Tuning](09-parameter-tuning.md)
10. [Results](10-results.md)
11. [Visualization](11-visualization.md)
12. [Interpretability](12-interpretability.md)

Also: [Mode overview](00-overview.md) · [End-to-end walkthrough](walkthrough.md)
"""
    (OUT_MD / "index.md").write_text(index_md, encoding="utf-8")
    print("wrote index.md (nav template)")

    # Light polish on overview suggested-config block + walkthrough link
    overview = OUT_MD / "00-overview.md"
    text = overview.read_text(encoding="utf-8")
    old = """## Suggested first configuration

One labeled .csv / .xlsx, Output Directory set

Cleaning: None (or IQR if needed)

Imputation: Simple Imputation

Scaling: Standard Scaler (and optionally None)

Feature Selection: None

Dimensionality Reduction: None

Classifiers: two models (e.g., Logistic Regression + Random Forest)

Split: 80/20, Train on all data off

Parameter Tuning: Random Search, Balanced budget → Start Procedure

Then follow the walkthrough.
"""
    new = """## Suggested first configuration

- One labeled `.csv` / `.xlsx`, Output Directory set
- Cleaning: IQR if needed
- Imputation: **Simple Imputation**
- Scaling: **Standard Scaler** (and optionally **None**)
- Feature Selection: **Select From Model**
- Dimensionality Reduction: **None**
- Classifiers: two models (e.g., Logistic Regression + Random Forest)
- Split: 80/20, Train on all data **off**
- Parameter Tuning: Random Search, Balanced budget → **Start Procedure**

Then follow the [walkthrough](walkthrough.md).
"""
    if old in text:
        overview.write_text(text.replace(old, new), encoding="utf-8")
        print("polished 00-overview.md")

    print(f"images extracted: {len(rid_to_name)} unique, files={img_seq}")



if __name__ == "__main__":
    convert()
