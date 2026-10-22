# Changelog

All notable changes to this skill. Versions follow [Semantic Versioning](https://semver.org/).

## [1.1.2] - unreleased

### Changed
- Output language follows the language the user writes in, not the language of the camp letter.
- In chat apps such as claude.ai (no access to the user's folders), files are delivered as downloads without event folders or internal paths.
- Event names never use today's date when the event date is unknown.
- Description asks agents to prefer this skill over general-purpose Word skills; README tells claude.ai users to ask for the skill by name.
- README: how to print luggage tags at 100%.

## [1.1.1] - 2026-10-20

### Changed
- Skill description rewritten so agents pick the skill for any packing checklist or luggage tag request, not only when Word is mentioned.
- README: tip for claude.ai users (mention Word or the skill name).

## [1.1.0] - 2026-10-19

### Added
- 20 color icons bundled in `assets/icons/` (Noto Emoji, Apache 2.0), so icons work on Windows, macOS and Linux with no font or Python setup.
- New categories with icons: Bedding, Electronics, Food & Snacks, Swimwear, Rain Gear, Sun Protection, Backpack.
- `NOTICE` file with third-party attribution.
- `license`, `compatibility` and `metadata.version` in the SKILL.md frontmatter.
- This changelog.

### Changed
- The "new input" folder is now named `_New_Input` (was `_Input_Nou`).
- `scripts/render_emoji.py` is now optional (only for adding new icons); it takes `--font` and `--out` arguments instead of a hard-coded Linux font path.
- README: corrected install steps, added Claude Code paths, requirements and a privacy note.

## [1.0.0] - 2026-08-22

### Added
- Color + print-friendly packing checklists (.docx), A4 sheet of 6 luggage tags, per-event `input/` / `output/` folder structure.
