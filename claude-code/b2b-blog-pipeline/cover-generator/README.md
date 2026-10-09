# Cover generator (Stage 10)

Puts a post's title on a branded cover template and exports SVG, PNG and WebP. It runs on your machine. Nothing is uploaded.

`scripts/blog-pipeline.sh` runs it as **Stage 10** after the QC report. It reads the draft's **Recommended Titles** (written by Stage 4): it tries the short H1 SEO title first, then the H2 article title, then the H3 image title, and uses the first one that fits. To turn it off, set `**Template cover:** off` in `reference/image-settings.md`.

## Install

| Tool | Why | macOS | Debian / Ubuntu |
|---|---|---|---|
| Python 3.9+ | runs the scripts | `brew install python` | `sudo apt install python3 python3-pip` |
| fontTools | draws the title as vector outlines | `python3 -m pip install fonttools` | same |
| resvg | renders the SVG to PNG (pixel-accurate) | `brew install resvg` | `cargo install resvg`, or a binary from https://github.com/linebender/resvg/releases |
| cwebp | makes the WebP files (optional; skipped if absent) | `brew install webp` | `sudo apt install webp` |

Check with `scripts/doctor.sh` from the repo root.

Don't swap resvg for ImageMagick's own SVG renderer. It paints some shapes and blend modes wrong.

## Make a cover by hand

```bash
cd cover-generator
python3 scripts/make_cover.py \
  --title "Win More Bids|With Better Proposals: A Field Guide for Service Firms" \
  --slug better-proposals --date 2026-11-04
```

| Option | What it does |
|---|---|
| `--layout band\|split\|stack\|vs` | Force a layout. Without it, the script alternates `band` and `split` per slug, then falls back to `stack` for long titles. |
| `--color primary\|alert\|growth` | Force a palette. Without it, the topic rules in `theme.json` decide. |
| `--topic "..."` | Extra words for the color rule, such as the primary keyword. |
| `--out DIR` | Write somewhere other than `output/<date>-<slug>/`. |
| `--svg-only` | Write the SVG only. Needs no resvg or cwebp. |

Title marks:

- `:` splits the big headline (before) from the small sub (after). A colon between digits, as in "5:15", doesn't count.
- `::` flips it: the small text goes on top and the big text below. Only the `stack` layout supports it.
- `|` suggests a line break. The script keeps it unless a line overflows.
- `A vs B` uses the `vs` layout.
- No colon: the script picks the split and tells you what it chose.

Output: `<slug>.svg`, `<slug>-master.png` (3840×2160), `fulltext-<slug>.png` and `.webp` (1920×1080), `intro-<slug>-sm.png` and `.webp` (960×540), and `report.json` with the layout, color, line breaks and sizes. Every size is rendered from the vector, so nothing is upscaled.

Make covers for every dated draft in `output/`:

```bash
python3 scripts/covers_from_drafts.py            # all drafts
python3 scripts/covers_from_drafts.py --only my-slug
```

## Make it yours

| File | What to change |
|---|---|
| `theme.json` | Your brand colors (one palette per mood), the topic rules that pick a palette, and the two fonts. |
| `templates/*.svg` | The background art. Edit them in any vector editor. Keep the `{{bg}}`, `{{accent}}`, `{{accent2}}`, `{{ink}}` and `{{paper}}` color tokens where you want brand colors. Add your logo as an `<image>` or as paths; each template has a comment that shows where. |
| `layouts.json` | Where the text goes in each template: box, anchor, size, line count, color. Change it when you move things in a template. |
| `RULES.md` | The plain-language rules. Keep it in step with `theme.json` and `layouts.json`. |

To add a layout: draw `templates/<name>.svg` at 1920×1080, add a `<name>` entry to `layouts.json` with its text slots, and add the name to `rotation` or `fallback`.

## Fonts

`fonts/` ships two free fonts under the SIL Open Font License 1.1, which allows use, bundling and redistribution:

- **Anton** (headline): `Anton-Regular.ttf`, license `OFL-Anton.txt`
- **Barlow Condensed ExtraBold** (sub): `BarlowCondensed-ExtraBold.ttf`, license `OFL-BarlowCondensed.txt`

To use your brand fonts, put the `.ttf` or `.otf` files in `fonts/` and name them in `theme.json`. Check the license first: many commercial fonts don't allow you to commit the font file to a public repository. If yours doesn't, add it to `.gitignore` and keep it local. The SVG output holds outlines, not the font, so the covers themselves are safe to publish.

## Troubleshooting

| Message | Fix |
|---|---|
| `fontTools is missing` | `python3 -m pip install fonttools` |
| `resvg is not installed` | Install resvg (table above), or use `--svg-only`. |
| `the title does not fit any layout at 80% size` | Shorten the part before the colon, or move words after a colon. |
| `uses color token(s) [...] that theme.json does not define` | Add the token to every palette in `theme.json`, or remove it from the template. |
| `size check failed` | resvg rendered at the wrong size. Update resvg. |
