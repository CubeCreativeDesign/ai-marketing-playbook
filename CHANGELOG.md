# Changelog

Changes to the AI Marketing Playbook as a whole. Each pipeline folder also keeps its own changelog where it has one.

## 2026-10-09

### Added
- `claude-code/b2b-blog-pipeline/`: the scripted Claude Code blog pipeline for agencies that market to service businesses (template v2.0.2). It used to live in its own repo.
- `projects/prompt-check.md`: grade any prompt against the Trust Insights frameworks and get a fixed version back.
- `CHANGELOG.md` (this file).

### Changed
- `README.md`: a "pick your starting point" table, every template in one index, and a short Cowork vs Claude Code guide. The "coming soon" list is gone.
- `getting-started/`: adds Claude Code and a "which tool should I use" table.
- `projects/`: titles, meta, link-check and prompt templates updated: SEO title max 60 characters (about 561px) and different from the H1, meta max 160 with no phone CTA, tiered banned words, three-tier link verification, and the Trust Insights prompt frameworks.
- `cowork/private-schools/`: refreshed to the current production rules. See the entries below.

### Cowork private-schools pipeline
- New **Stage 0: research** (`instructions/00-deep-research.md`). It uses only Claude's built-in web search, web fetch and Research. Every stat and quote gets fetched or tagged `unverified` before Stage 1. Bundles go to `research/`.
- One topic slug names every file: `research/[topic-slug]-research.md`, `output/[topic-slug]-brief.md`, `output/[topic-slug]-draft.md`.
- Stages 2 and 3 end with a written **Self-Check** in place of a QC script: prohibited-phrase tiers, readability (grade 10 or lower, Reading Ease 55 or higher), structure rules, em dashes at most 1 per 300 words.
- Stage 4: SEO title max 60 characters (about 561px), meta description max 160 with no phone CTA.
- Every stage gains **Output feeds** and **Human check** lines.
- New reference files: `mechanical-style-rules.md`, `source-policy.md`, `READER-PERSONA-TEMPLATE.md`, and `personas/WRITER-PERSONA-TEMPLATE.md`.
- `prohibited-phrases.md` is now tiered (hard ban, `[headings]`, `[limit 1]`, `[unless sourced]`, `[needs proof]`, `[with stats]`, `[avoid]`, `[residue]`), with a key at the top.
- The example writer voices are now The Wry Strategist, The Explainer and The Digital Native (`[WRITER_1..3]`).
- One placeholder style throughout: `[YOUR_AGENCY]`, `[YOUR-AGENCY-DOMAIN]`, `[YOUR_CMS]`.
