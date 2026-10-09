# Stage 11: AI Cover Image + Alt Text

## Purpose
Turn the finished draft into a cover/hero image. Generate four candidates from
four models so a human picks one, then write the alt text for the picked image.

This stage runs **after** Stage 9 (QC report) and the optional Stage 10 template
cover, on a draft that is otherwise publication-ready. Stage 10 sets the title on a
branded template. This stage makes AI photographs instead. Use either or both. It reads the finished blog post. It does not read the topic
line or the brief.

**Output feeds:** Nothing later in the pipeline reads it. The cover a human picks and your alt text are published with the post.

**Human check:** This stage runs in an interactive session, not under `claude -p`. Its human check is already named below: the Cover Image Options table is where a person picks the final cover. Say there if a render needed a substitute model or showed painted text.

---

## Read this before your first run

### This stage is interactive only
Magnific (`mcp__magnific__*`) is a claude.ai OAuth connector. Its auth is bound
to an interactive Claude Code session and does **not** transfer into a headless
`claude -p` subprocess: `mcp__magnific__account_balance` reports unauthorized
under `-p` even when the connector is authorized in the session that launched
the script.

So `scripts/blog-pipeline.sh` does not run this stage and cannot be made to. You
run Stage 11 by hand, in an interactive session, after a batch finishes:

```
claude
> Run Stage 11 (instructions/11-ai-cover-image.md) on posts/2026-11-04-my-slug/
```

### Requirements
This stage reads four rule files that ship with this template:

```
reference/image-rules/style-anchors.md
reference/image-rules/composition-standards.md
reference/image-rules/vertical-aesthetics.md
reference/image-rules/alt-text-rules.md
```

Stage 11 will not work without them. Do not try to work from memory of what
they say. Edit them to match your house style.

You also need a Magnific account with the Magnific connector added and
authorized in your Claude Code session (see `docs/TOOLS.md#magnific`). Check
with `mcp__magnific__account_balance` before you start a batch. Magnific
charges per generation.

---

## Gate: check the settings file first

Read `reference/image-settings.md` before you touch anything else.

- File missing, or `AI cover: off` → **skip the whole project.** Say so and stop.
  Never guess a setting.
- `AI cover: on` → take `Aspect ratio` and `Minimum resolution` from that file
  and use them for every generation in this run.

---

## Which drafts to process

- Given a project path: every `output/*-draft.md` and `posts/*/*-draft.md` that
  does not already have at least one matching `[slug]-cover-*.png` beside it.
- Given one draft path or slug: just that one. A named re-run always
  regenerates, even if covers already exist.

The slug comes from the draft filename: strip any leading `YYYY-MM-DD-` prefix
and the `-draft.md` suffix. If the filename is generic, slug the post's H1.

---

## Operating procedure

### Step 1 — Confirm the model slugs (once per run, not per draft)

Query `mcp__magnific__images_models_list` with `search:"<name>"` for each of the
four models in Step 3. Magnific renames and retires slugs.

If a slug is gone, pick the closest photorealism-category replacement from the
live catalog (`images_models_list` with no search, or `onlyRecommended: true`)
and say which model you substituted and why. **Never silently drop to three
models.**

Reuse the confirmed slugs for every draft in the run.

Two things not to do:

- Do **not** use the Magnific marketing docs page
  (`https://www.magnific.com/ai/docs/image-ai-models`) to pick slugs. Its model
  names do not reliably map to what `images_models_list` exposes as callable.
  Several models listed on that page have been missing from the live catalog.

### Step 2 — Build the cover prompt

Read the finished draft **in full**, including the conclusion. The cover comes
from what the post actually argues, not from its title.

The lesson that cost six rounds on a real batch: read the conclusion, then ask
what a photographer would actually shoot.

Then read the three rule files:

- `reference/image-rules/style-anchors.md`
- `reference/image-rules/composition-standards.md`
- `reference/image-rules/vertical-aesthetics.md`

Run the six-part content analysis: main topic, key concepts, emotional tone,
target audience, visual elements named in the text, and metaphors that could be
made literal.

Detect the vertical from the content. Never ask which vertical it is.
`vertical-aesthetics.md` profiles B2B service businesses, trades and
professional services, and has a fallback clause for anything else. For this
template's vertical, [YOUR_VERTICAL], use the matching profile if there is one,
otherwise infer the audience and register from the draft itself.

Build **one** photographic prompt. Include subject, setting, lighting with both
direction and quality, a palette of 3 to 5 colors, composition, lens and
perspective, up to two style anchors, and technical cues.

Hard rules for the prompt:

- Photorealism only. One coherent scene. No split narrative, no montage.
- Maximum two style anchors, from photography and editorial traditions only.
- No face-forward or identifiable people. Rear-facing or over the shoulder.
- No legible text on any surface: no signage, screens, vehicle wraps, name tags.
- Reserve negative space in the upper-left third for the client's text overlay.
  Cover images only.
- No flat-lay or overhead for a cover. No logos or real-world brand marks.

**Prompt text bleed.** Some models paint the words of your prompt into the
picture as readable type. Seedream 4.5 has rendered palette hex codes and a
named photographer into the reserved overlay zone. So:

- Name the palette colors in words. Never write hex codes in the prompt.
- Never name a photographer in the prompt.
- Never name a document, form, sign, screen, or field. Describe printed matter
  as "abstract illegible texture" instead.

Then look at the render. This failure is silent, and only your eye catches it.

### Step 3 — Generate four candidates

| Model | Magnific slug | Resolutions |
|---|---|---|
| Google Nano Banana Pro | `imagen-nano-banana-2` | 1k / 2k / 4k |
| Google Nano Banana 2 | `imagen-nano-banana-2-flash` | 1k / 2k / 4k |
| Seedream 4.5 | `seedream-4-5` | 2k / 4k |
| Flux.2 Pro | `flux-2` | 1k / 2k |

Call `mcp__magnific__images_generate` once per model, with the **same** prompt,
the aspect ratio from the gate, and `resolution: 2k`. All four support 2k, and
2k clears both 1920x1080 and 1080x1080.

In past runs Nano Banana Pro gave the best light, the deepest subject separation
and the cleanest overlay space. Run it first if you are saving credits.

**Models snap to their own pixel dimensions.** At `16:9` and `resolution: 2k`, a
real run returned 2752x1536, 2688x1536, and 2048x1168. All clear a 1920x1080
minimum, but none is exactly 16:9. Check the delivered dimensions rather than
assuming. Crop later if the layout needs an exact ratio.

Only deviate from this set if a human asks for different candidates on a given
run, or asks you to re-evaluate the default set from scratch.

### Step 4 — Download

Poll with `mcp__magnific__creations_wait`. Download each result next to the
draft (in `output/`, or in the post's `posts/<date>-<slug>/` folder):

```
[slug]-cover-[model-slug].png
```

If one model fails, log why, skip it, and continue with the rest. Do not retry a
hard failure more than once. Do not abort the batch over one draft.

### Step 5 — Append the options table to the draft

Append a `## Cover Image Options` section below the Stage 9 QC report:

```
## Cover Image Options

Generated YYYY-MM-DD via Magnific at `resolution: 2k`, 16:9. Every candidate
clears this project's 1920x1080 minimum. Models snap to their own pixel
dimensions, so the delivered ratio is approximately 16:9, not exactly.

| File | Model | Dimensions | Magnific link |
|---|---|---|---|
| `output/[slug]-cover-imagen-nano-banana-2.png` | Nano Banana Pro | WxH | [webUrl] |
| `output/[slug]-cover-imagen-nano-banana-2-flash.png` | Nano Banana 2 | WxH | [webUrl] |
| `output/[slug]-cover-seedream-4-5.png` | Seedream 4.5 | WxH | [webUrl] |
| `output/[slug]-cover-flux-2.png` | Flux.2 Pro | WxH | [webUrl] |

**Cover alt text:** [see Step 6]

Concept: [one line on what you shot and why, read from the body and the
conclusion. Note that you checked Seedream for painted text.]
```

Fill the Dimensions column from the real files, for example with
`python3 -c "import struct,sys; d=open(sys.argv[1],'rb').read(24); print(*struct.unpack('>II', d[16:24]), sep='x')" file.png`
(works on macOS and Linux; `sips -g pixelWidth -g pixelHeight` also works on macOS). State what was generated, not the minimum. This block is where a
human picks the final cover before publishing.

### Step 6 — Write the cover alt text

Write the alt text for the **image you generated**, not for the image you
described. Look at the render first.

Follow `reference/image-rules/alt-text-rules.md`:

- Under 125 characters.
- Describe it accurately for someone who cannot see it.
- Be specific. "Technician checking a rooftop HVAC unit at dusk" beats
  "a worker on a roof."
- No "image of" or "picture of". Screen readers already announce it is an image.
- No em dashes. Use commas or periods.
- Work in the target keyword or a natural variant **only** when it honestly fits
  what the image shows. Never keyword-stuff.

If the four candidates differ enough that one alt text cannot cover them, write
one line per candidate in the table instead of one line below it.

This is the **cover** alt text. In-body alt-text suggestions come from Stage 2.

---

## QA checklist

Before you call the stage done:

- [ ] `reference/image-settings.md` was read, and its ratio and minimum were
      actually used
- [ ] All four model slugs were confirmed live, or a substitution was stated
- [ ] The prompt contains no hex codes, no photographer name, and no named
      document, sign, or screen
- [ ] The prompt reserves negative space in the upper-left third
- [ ] Four PNGs exist at `[slug]-cover-*.png` beside the draft, or every failure is logged
- [ ] Each PNG clears the minimum resolution and matches the aspect ratio
- [ ] The Seedream render was eyeballed for painted text in the overlay zone
- [ ] The Cover Image Options table is appended below the QC report
- [ ] The alt text is under 125 characters, has no em dash, and describes the
      render rather than the plan

---

## Output

At the end of a run, print:

- Which drafts were processed
- Which were skipped, and why: covers already existed, project disabled, no
  settings file
- Any model substitution you made
- Any generation failures, with the reason
