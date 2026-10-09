# Cover rules

Plain-language rules for the cover generator. The script reads its numbers from `layouts.json` and `theme.json`. Keep this file in step with them.

## Splitting the title

- The **sub** is everything after the **first colon**.
- A colon between digits, as in "5:15", is **not** a split point.
- With no colon, the script picks a natural split (after the subject phrase) and reports it.
- **The colon is never drawn.** It only marks the split.
- **`::` (double colon) flips the order:** the front part becomes small text on top and the tail becomes the big text below. Use it when the end of the title is the punch, as in `The Quote That Lost the Job:: Speed Beats Price`. Only layouts with a `reverse` block set accept it (`stack` out of the box). Keep the big tail to about 24 characters.
- `|` marks a **suggested** line break. The script tries it first and changes it only when a line overflows or the lines are badly unbalanced. It reports the change.
- Text is set in ALL CAPS (`"upper": true` in `layouts.json`).

## Choosing the layout

- **"A vs. B" titles** use `vs`. Side A goes left and side B goes right, with no sub.
- **Otherwise** the script alternates the `rotation` layouts (`band`, `split`) by slug, so neighboring posts don't match.
- A rotation layout wins when its text fits at 90% of full size or more.
- **Long titles** fall back to `stack`, which has the widest text area.
- `--layout` always overrides these.

## Color by topic

| Palette | Topics |
|---|---|
| **primary** | SEO, websites, how-to and process posts. The default. |
| **alert** | Warnings, mistakes, penalties, fake reviews, "stop doing this" posts, and costs that went up |
| **growth** | Revenue, ROI, budgets, growth, pricing and winning work |

The patterns live in `theme.json` under `topic_rules`. `--color` always overrides them.

## Sizing

- Start at the size in `layouts.json`.
- The floor is 80% of that size (`floor`). Below it, the script tries another layout instead of shrinking further.
- No single word alone on the last line (no widows) unless the headline is short.
- No line ends on a small word such as "for", "to" or "your".

## Output

- Local only: `output/<publish-date>-<slug>/`, or `posts/<publish-date>-<slug>/` once the post is collected.
- SVG, a 3840×2160 master PNG, PNG and WebP at 1920×1080 and 960×540, and `report.json`.
