# Custom PDF Generator (ReportLab)

A modular Python project for producing **pixel‑controlled, designed PDF documents** with [ReportLab](https://www.reportlab.com/). Rather than a simple "text → PDF" dump, it lays out multi‑page documents with custom fonts, coloured page backgrounds, breadcrumb‑style headers, page indices, decorative grid lines, and multi‑column frames — the kind of output you'd expect from a designed template (e.g. a "Theory / Assessment" style booklet).

> Note: despite the repository name, this is **not** the ReportLab library itself — it's an application that *uses* ReportLab (`reportlab==4.1.0`).

---

## Table of Contents

- [What It Produces](#what-it-produces)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Customisation](#customisation)
- [License](#license)

---

## What It Produces

Running the project renders `output.pdf`, a letter‑size document assembled page by page. Each page can have:

- Its own **background colour** and **primary/secondary colour scheme** (e.g. a light "Theory" page and a dark `#233137` "Assessment" page).
- A **header** with a breadcrumb navigation path (e.g. `Section › Subsection › Page`), a page index badge (`01`, `02`, …) and a separator line.
- Optional **decorative grid lines** (horizontal + vertical) drawn across the header and body.
- One or more **content frames** (columns) populated with flowables (paragraphs, images, spacers) using custom registered fonts.

---

## How It Works

The rendering is split into focused modules that each own one concern:

- **`main.py`** — the driver. Creates a ReportLab `Canvas` + `BaseDocTemplate`, then builds each page by constructing a `Flowables` object with the page's colours/index, collecting that page's frame content, and calling `generate_pdf(...)`. It advances pages with `canvas.showPage()` and finalises with `canvas.save()`.
- **`generate_pdf.py`** — the per‑page renderer. Paints the background, draws the header (via `HeaderHandler`), optionally draws the header/body grid lines, creates the page's frames (via `FrameHandler`), and flows each frame's content onto the canvas.
- **`flowables.py`** — `Flowables`: builds the actual content (paragraphs, images, tables, spacers) for each page/frame, e.g. `get_page1_frame1_flowables()`.
- **`headerhandler.py`** — `HeaderHandler`: draws the breadcrumb navigation path, page index and separator line in the page header.
- **`framehandler.py`** — `FrameHandler`: computes and creates the column frames for a page based on `frame_count`.
- **`styles.py`** — registers custom TrueType fonts (NeueMontreal, NeueMontreal‑Light, F37 Zagma Mono) and defines `ParagraphStyle`/`TableStyle` styles.
- **`docs_texts.py`** — the text content and navigation labels (`PAGE_NAVIGATIONS`, paths) used across pages.
- **`assets/`** — fonts (`.ttf`) and images used in the document.

---

## Tech Stack

| Component | Purpose |
|-----------|---------|
| Python 3 | Runtime |
| **ReportLab 4.1.0** | PDF canvas, platypus flowables, frames, fonts, colours |
| Pillow 10.2.0 | Image handling for embedded images |
| chardet 5.2.0 | Text encoding detection |

---

## Project Structure

```
reportlab/
├── main.py            # Entry point — builds each page and saves output.pdf
├── generate_pdf.py    # Per-page rendering (background, header, grids, frames)
├── flowables.py       # Flowables — page/frame content builders
├── headerhandler.py   # HeaderHandler — breadcrumb header, page index, separators
├── framehandler.py    # FrameHandler — column frame creation
├── styles.py          # Custom font registration + paragraph/table styles
├── docs_texts.py      # Document text content + navigation labels
├── requirements.txt   # reportlab, pillow, chardet
└── assets/
    ├── fonts/         # NeueMontreal, F37 Zagma Mono, etc. (.ttf)
    └── images/        # left_image.jpg, right_img.jpg, …
```

---

## Getting Started

### Prerequisites

- **Python 3.9+**

### Installation

```bash
git clone https://github.com/alexander01202/reportlab.git
cd reportlab

python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

> The custom fonts under `assets/fonts/` are required — `styles.py` registers them by path at import time, so keep the `assets/` folder in place.

---

## Usage

Generate the PDF:

```bash
python main.py
```

This writes **`output.pdf`** in the project root. To change the output filename, edit the `filename` value at the bottom of `main.py` (or call `main("your-name.pdf")`).

---

## Customisation

- **Add or reorder pages:** in `main.py`, set the page's colours and `PAGE_INDEX`, build its frame flowables from a `Flowables` instance, and call `generate_pdf(...)` followed by `canvas.showPage()`.
- **Change content:** edit the builders in `flowables.py` and the text in `docs_texts.py`.
- **Restyle:** adjust colours/fonts/spacing in `styles.py`; toggle the decorative grids with the `draw_line` flag; change columns via `frame_count`.
- **Swap fonts/images:** drop new files into `assets/` and update the registrations in `styles.py`.

---

## License

No license file is included. Add one if you intend to share it; otherwise treat it as private.
