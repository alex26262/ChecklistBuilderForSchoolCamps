# Checklist Builder for School Camps

An agent skill (SKILL.md) that turns a camp or school-trip packing list into ready-to-print documents, and - when the agent works in your folders - keeps every event's source documents and generated files in their own folder so you never grab the wrong checklist.

Works with Claude (claude.ai, Claude Code) and other agents that support the SKILL.md format.

## What it produces, per event

- **Packing checklist** — a color Word document with category icons (Clothes, Toiletries, Documents, ...) and checkboxes, plus a black-and-white print-friendly version.
- **Luggage tags** — an A4 sheet of 6 tags (78×43 mm each, with a cut guide) showing the child's name, parent phone numbers and the event's location.

## Folder structure it maintains

Used when the agent works in a folder on your computer (Claude Code, Cursor, ...). In chat apps such as claude.ai you simply download the files.

```
your-project/
├── _New_Input/              # drop new event info here (PDF, email, list)
├── Camp_Mountain_July2026/  # one folder per event: Type_Location_MonthYear
│   ├── input/               # source docs, copied unchanged
│   └── output/              # generated checklist + luggage tags
├── _Template_Event/         # template copied for each new event
└── _Archive/                # finished events
```

## Install

Get the skill folder: download `checklist-builder-for-school-camps_vX.Y.Z.zip` from the [Releases](../../releases) page (the zip already has the right structure), or clone this repository — the repository root is the skill folder.

**claude.ai**
1. Go to **Customize → Skills**, click **Add**, and select the release zip.
2. Enable the skill.

**Claude Code**
Unzip (or clone) so that `SKILL.md` ends up at:
- `~/.claude/skills/checklist-builder-for-school-camps/SKILL.md` — available in all your projects, or
- `.claude/skills/checklist-builder-for-school-camps/SKILL.md` — only in the current project.

**Other agents**
Copy the folder into the agent's skills directory (see your agent's documentation).

Then ask, for example: *"Make a packing checklist from this camp letter"* or *"Make luggage tags for Ana Smith"*.

**On claude.ai, ask for the skill by name** - for example *"Use the checklist-builder-for-school-camps skill to make a packing checklist from this camp letter"*. Without the name, claude.ai may answer with its own built-in Word or on-screen tools instead of this skill.

## Requirements

- Node.js with the `docx` package (`npm install docx`) to build the Word files.
- Icons are bundled — nothing else to install.
- Optional, only to add new icons: Python 3, Pillow and the Noto Color Emoji font (`scripts/render_emoji.py --help`).

## Privacy

Everything is generated locally from the documents you provide. The skill makes no network calls and sends nothing anywhere. Children's names and parent phone numbers stay in your event folders.

## Why icons are PNG images, not emoji text

Microsoft Word unpredictably re-renders emoji characters inside heading styles — they can show up flat or tinted with the heading color. This skill embeds real color PNG icons instead, so they look the same in every copy of Word.

## License

MIT — see [LICENSE](LICENSE). Bundled icons are from [Noto Emoji](https://github.com/googlefonts/noto-emoji) (Apache 2.0) — see [NOTICE](NOTICE). Changes are listed in [CHANGELOG.md](CHANGELOG.md).
