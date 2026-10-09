# Cover Image Settings: [YOUR_VERTICAL] Blogs

Two cover stages read this file:

- **Stage 10, template cover.** `scripts/blog-pipeline.sh` runs it after the QC
  report when `cover-generator/` is present. It sets the post title on a branded
  template (see `cover-generator/README.md`). No API, no cost.
- **Stage 11, AI cover photos.** You run it by hand in an interactive Claude
  Code session, with `instructions/11-ai-cover-image.md`. It needs a Magnific
  account, which charges per image. It never runs in the batch script, because
  Magnific's sign-in doesn't carry into a headless `claude -p` run.

- **Template cover:** on
- **AI cover:** off
- **Aspect ratio:** 16:9
- **Minimum resolution:** 1920x1080

## Changing these

- **Template cover:** `on` or `off`. `off` makes the batch script skip Stage 10.
- **AI cover:** `on` or `off`. Stage 11 skips the project and says so when it's
  `off` or this file is missing. Turn it on once Magnific is connected.
- **Aspect ratio** is a variable, not a constant. 16:9 is the standard blog hero
  shape. Use 1:1 if your covers get reused on social more than as heroes. It
  applies to Stage 11. Stage 10 templates are 16:9.
- **Minimum resolution** is a floor, not a target. Stage 11 generates at
  Magnific's `2k`, which clears both 1920x1080 and 1080x1080.

Keep the field names and their spelling exactly as they are. The batch script
and Stage 11 read this file by those labels.
