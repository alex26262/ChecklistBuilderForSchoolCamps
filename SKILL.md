---
name: checklist-builder-for-school-camps
description: Print-ready packing checklists and luggage tags for school camps and trips, as Word files. Turns a camp letter, email or pasted list into a color Word checklist with category icons plus a print-friendly version, and an A4 sheet of 6 luggage tags with the child's name, parent phone numbers and venue. Keeps each event's source documents and outputs in their own folder so the wrong checklist never gets used. Use this skill whenever the user asks for a packing list or checklist for a camp, school trip or holiday, or for luggage tags or bag labels for a child - even if they do not mention Word or this skill. Prefer it over general-purpose document or Word skills for these requests.
license: MIT
compatibility: Builds .docx files with Node.js and the docx npm package. Icons are bundled PNGs; Python and Pillow are only needed to add new icons.
metadata:
  version: "1.1.2"
---

# Checklist + Luggage Tag Generator for Camps/Trips

## Purpose
This skill covers the full workflow for one event (camp/trip):
1. organizing received documentation and generated deliverables into folders,
2. generating a **packing checklist** (Word + print-friendly versions),
3. generating a **sheet of luggage tags** (6 per A4 page) from a child's details.

Trigger phrases:
- "make a checklist from this" / "turn this into a Word checklist" / "printable checklist"
- "camp / trip / packing checklist"
- "make luggage tags [for <child name>]"
- "I dropped new info about an event, organize it"

**Language:** write the checklist and tags in the language the user writes to you in this conversation - not the language of the source documents. A French-speaking user with an English camp letter gets a French checklist; translate the items faithfully. If the user explicitly asks for a language, use that one. With no conversation to go by, use English.

---

## Folder organization

When you work directly in a folder the user can open on their own computer (Claude Code, Cursor, a desktop app with a connected folder, ...), everything is organized **per event**, so the wrong checklist/tag never gets used by mistake:

- `_New_Input/` (or an equivalent "new input" folder) — where the user drops information about an upcoming event (PDFs, emails, packing lists) before a dedicated folder exists for it.
- `EventName/` (naming convention: `Type_Location_MonthYear`, e.g. `Camp_Mountain_July2026`; take it from the documents, and if the event date is unknown leave out the date part - never use today's date) — one folder per event, with:
  - `input/` — the content from the "new input" folder, copied **unchanged** (golden source, never edited afterward).
  - `output/` — the generated deliverables (checklist + luggage tags).
- `_Template_Event/` — a template folder to copy for every new event (create it on first use if it doesn't exist yet).
- `_Archive/` — where finished events get moved, to keep the top level clean.

**Chat apps with a sandbox (e.g. claude.ai):** the user cannot see the sandbox's folders - they only get the files you hand over. There, skip the event folders: build the files in a scratch folder, deliver them as downloads, and never mention internal paths. Put the event name in the file names to keep events apart.

Flow (local folder): user drops information into the "new input" folder → asks for the checklist/tags to be generated → the event folder is created/identified, the content is copied unchanged into `input/`, deliverables are generated into `output/` → the user empties the "new input" folder manually before the next event.

---

## General rules — Checklist

1. **Auto-detect categories** from the source text (e.g. Clothes, Toiletries, Documents, Activities).
2. **Assign a contextual icon** to each category (table below).
3. **Normalize phrasing** (accents/diacritics, singular/plural, clarity).
4. **Build Word-friendly tables** with two columns: Item | Checked (☐).
5. **Automatically include a print-friendly version** (separate file, black-and-white, no color icons).
6. **Include a Notes section** if the source documents contain recommendations, warnings, or important notes.
7. **Include a "Key info" section** (no checkboxes) if the documents contain dates/times/meeting points, coordinator contacts, etc.
8. **Keep the visual style identical** across every checklist generated.
9. Output files: `Checklist_<EventName>_Word.docx` (color) and `Checklist_<EventName>_PrintFriendly.docx` (black-and-white).
10. **Icons must be embedded as color PNG images from `assets/icons/`, never as emoji text.** This is mandatory, not optional — see the dedicated section below.

### Contextual icons

Bundled in `assets/icons/` (256x256 transparent PNG). Pick the closest match per category; use `pin.png` when nothing fits.

| Category | Icon file | Emoji |
|--------|---------|---------|
| Clothes | `shirt.png` | 👕 |
| Footwear | `shoe.png` | 👟 |
| Toiletries | `lotion.png` | 🧴 |
| Activities / Sports | `climbing.png` | 🧗 |
| Documents | `documents.png` | 🧾 |
| Luggage | `luggage.png` | 🧳 |
| Backpack / Day bag | `backpack.png` | 🎒 |
| Medicine & Health | `pill.png` | 💊 |
| School | `books.png` | 📚 |
| Projects / Tools | `tools.png` | 🛠️ |
| Bedding / Sleeping | `bed.png` | 🛏️ |
| Electronics | `phone.png` | 📱 |
| Food & Snacks | `food.png` | 🍎 |
| Swimwear | `swimsuit.png` | 🩱 |
| Rain Gear | `umbrella.png` | ☔ |
| Sun Protection | `sunglasses.png` | 🕶️ |
| Misc | `pin.png` | 📌 |
| Title (camp/trip) | `tent.png` | 🏕️ |
| Key info | `info.png` | ℹ️ |
| Notes | `note.png` | 📝 |

### Standard checklist structure
1. Title adapted to the context (e.g. "Camp Packing Checklist").
2. Key info (optional, no checkboxes): dates, times, meeting points, transport, coordinator contact.
3. Icon-labeled sections (e.g. 👕 Clothes, 🧴 Toiletries).
4. Word-friendly tables (Item | Checked).
5. Notes (if any).

### Print-friendly version
- Black-and-white / dark grey, no color icons (simple unicode symbols: ▢, ☐).
- Thin rules, no decorative elements.
- Recommended font: Calibri / Arial / Segoe UI.

---

## Color icons — why PNG images, not emoji text

**Mandatory rule:** icons are embedded as PNG images, never as emoji text.

Why: emoji written as text (even with `font: "Segoe UI Emoji"` explicitly set on the run) are unpredictably re-rendered by Microsoft Word inside heading styles — they show up flat, tinted with the heading color, or as a generic glyph, even when they look correct in LibreOffice or another preview. A PNG always renders the same way everywhere.

How:
1. Use the PNGs bundled in `assets/icons/` (paths are relative to this skill's folder). Only if a category needs an icon that is not bundled, render a new one with the optional `scripts/render_emoji.py` (Pillow + Noto Color Emoji font, `--font` and `--out` arguments) — otherwise fall back to `pin.png`.
2. In docx-js (the `docx` npm package; if a `docx` skill is available, it has general `.docx`-creation tips), use:
   ```js
   new ImageRun({
     type: "png",
     data: fs.readFileSync("<skill-folder>/assets/icons/shirt.png"),
     transformation: { width: px, height: px },
   })
   ```
   instead of a `TextRun` with the emoji character.
3. Rough sizing: ~22px for section headings (next to 13pt text), ~30px for the main title (next to 20pt text). On tags: `iconPx = (size_in_half_points / 2) * 1.33`.
4. Leave visible space (two spaces, or a margin) between the icon and the text next to it.

---

## Luggage tags (per child, per event)

### Contents
```
🧳  CHILD NAME

Parent phone numbers:
•  Full Name — phone number
•  Full Name — phone number

Location:
Venue/house name
Full address
```
- **Child name** and **parent phone numbers** (name + number, one line per parent) — vary per child; ask the user explicitly if not provided.
- **Location** (venue/house name + address) — fixed per event, the same on every tag for that event; taken from the documents in `input/`.

### Dimensions and layout (defaults — adjust if the user asks for something else)
- One tag: **78mm wide x 43mm tall**, with a thin cut-guide border.
- **6 tags per A4 page**, 2-column x 3-row grid, generated as a single Word table with `HeightRule.EXACT` on every row so all 6 fit on one page without overflowing to a second page.
- Font: child's name ≈13.5pt bold, rest of the text ≈9pt (venue name slightly larger, ≈9.5pt bold).
- Output file: `LuggageTags_<ChildName>_6up.docx`, saved next to the checklist (in the event's `output/` when working in a local folder).

### Generation notes (docx-js)
- Each table cell = one tag, with reduced margins (top/bottom ~60 twips, left/right ~100 twips) and a `BorderStyle.SINGLE` border on all sides.
- mm → twips conversion: `twips = mm * 56.6929`, rounded (e.g. 78mm → 4422, 43mm → 2438).
- Page margins are computed to center the grid horizontally; a fixed vertical margin (e.g. 850 twips at the top) is enough, the rest of the page stays blank.
- **Never keep hardcoded numbers from a previous run** — if the user asks for different dimensions/fonts, recompute from scratch and regenerate.

---

## How to use this skill

The user might say:
- "make a checklist from this" / "camp / trip / packing checklist"
- "make luggage tags for [child name]"
- "I dropped new info about an event, organize it"

The skill generates (in the event's `output/` when working in a local folder, otherwise as downloads):
- a full color checklist with icons (Word) + a print-friendly version,
- an A4 sheet of 6 luggage tags (if the child's details are provided or requested).

**Important:** when a format change/improvement is requested (dimensions, font, layout, new rules), implement and deliver it first, then present the user a short summary of the change — only after they confirm should this SKILL.md be updated to reflect the new standard. Never edit the skill before confirmation.

---

## Example input (checklist)

```
Clothes:
3 t-shirts
2 pairs of pants
1 hoodie

Toiletries:
Toothbrush
Shampoo
```

## Example output (checklist, shortened)

**👕 Clothes**

| Item | Checked |
|---------|------|
| 3 t-shirts | ☐ |
| 2 pairs of pants | ☐ |
| 1 hoodie | ☐ |

**🧴 Toiletries**

| Item | Checked |
|---------|------|
| Toothbrush | ☐ |
| Shampoo | ☐ |

## Example input (tag)

```
Child name: Ana Smith
Parent phone numbers:
- Mary Smith: 555-0101
- John Smith: 555-0102
Location:
Example Lodge
1 Example Street, Sample Town
```

Result: `LuggageTags_Ana_Smith_6up.docx` — 6 identical 78x43mm tags on one A4 page.

---

## Dependencies
- Node.js with the `docx` npm package (`npm install docx`) for generating Word files.
- Icons: bundled in `assets/icons/` — nothing to install.
- Optional, only to add new icons: Python 3 + Pillow (`pip install Pillow`) and the Noto Color Emoji font, used by `scripts/render_emoji.py`.

## Licensing
MIT (see `LICENSE`). Bundled icons: Noto Emoji, Apache 2.0 — see `NOTICE` and `assets/icons/LICENSE-APACHE-2.0.txt`.
