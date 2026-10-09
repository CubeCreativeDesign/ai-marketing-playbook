# Private School Blog Pipeline: Claude Cowork Project

> **Beta.** This pipeline is still in beta. Expect rough edges, and please [open an issue](https://github.com/yoderman94/ai-marketing-playbook/issues) when something breaks.

A blog content pipeline built for Claude's Cowork feature: Stage 0 (research) plus 8 content stages. Designed for digital marketing agencies that market TO K-12 private schools (targeting school administrators, marketing directors, and admissions teams).

This isn't a prompt template you paste into chat. It's a full Cowork project: a structured workspace with instructions, personas, reference files, and a batch processing system that Claude reads and follows automatically. It needs no code, no scripts, and no extra tools. Claude's built-in web search, web fetch, and Research do the work.

**Want a scripted version?** For a Claude Code pipeline that runs batches from the command line with automated QC scripts, see [`../../claude-code/b2b-blog-pipeline/`](../../claude-code/b2b-blog-pipeline/). It's a generic B2B template, so you'd adapt it to schools.

## What This Does

You give Claude a blog topic (or a batch of 10 at once). It runs each topic through 9 stages:

0. **Deep Research:** Searches, verifies every statistic on its source page, and saves a research file
1. **Topic Development:** Validates the topic and writes a keyword brief from the research
2. **Blog Post Writing:** Writes the full draft with citations, FAQ, TL;DR, and CTA, then runs a written self-check
3. **FAQ and TL;DR Review:** Re-runs the self-check and quality-checks the FAQ and summary sections
4. **Titles, Meta, Keywords:** Generates 5 title sets across 3 tiers, a meta description, and a keyword list
5. **URL/Slug Generation:** Creates SEO-friendly URL slugs and the Publishing Package
6. **Internal Linking:** Finds and adds links to your other content
7. **External Link Verification:** Verifies every citation source is live and contains the cited fact
8. **Link Checking:** Final independent verification of all links before publishing

Each stage has its own instruction file. Claude reads the instructions, does the work, saves to `research/` or `output/`, and moves to the next stage. You review the finished draft in the Cowork chat. Nothing publishes on its own.

## Who This Is For

- **Marketing agencies** that create blog content for private school clients
- **In-house school marketers** running their own content programs
- **Anyone** who wants to see how a production-grade Cowork project is structured

Even if you don't market to schools, the pipeline structure (research first, staged writing, batch processing, writer and reader personas, citation verification) works for any industry. Fork it and swap the vertical.

## How to Set It Up

### 1. Copy the project into a Claude Cowork workspace

Create a new Cowork project in Claude and add all the files from this directory. The `CLAUDE.md` file is read automatically as project instructions. Keep the `research/` and `output/` folders. Claude saves its work there.

### 2. Replace the placeholders

Search the project for `[YOUR` and replace each placeholder with your own details. Any placeholder you miss counts as chatbot residue in the self-check, so a forgotten one gets flagged.

| Placeholder | What it is | Where it appears |
|-------------|-----------|------------------|
| `[YOUR_AGENCY]` | Your agency's name | `CLAUDE.md`, `instructions/01`, `02`, `03`, `reference/mechanical-style-rules.md`, `reference/prohibited-phrases.md` |
| `[YOUR-AGENCY-DOMAIN]` | Your website domain, no `https://` (for example, `example-agency.com`) | `CLAUDE.md`, `instructions/02`, `05`, `06`, `08`, `reference/cta-rules.md` |
| `[YOUR_CMS]` | The CMS you build school sites on | `CLAUDE.md`, `instructions/00`, `02`, `03`, `04`, `08` |
| `[ALTERNATIVE_CMS]` | The CMS you position against. Delete the CMS Positioning section in `CLAUDE.md` if you don't take a position | `CLAUDE.md`, `instructions/00`, `02` |
| `[COMPETITOR_DOMAIN_1]` and so on | Competitor domains never to cite or link | `reference/k-12-private-school-competitors.md` |
| `[WRITER_1]` to `[WRITER_3]` | Writer voice slots. The example voices fill them | `instructions/02` (the names live in `personas/writer-profiles.md`) |
| `[PERSONA_NAME]` | Your reader persona names | `instructions/02` (the personas live in `reference/k-12-private-school-personas.md`) |

Two more things to set:

| File | What to customize |
|------|-------------------|
| `reference/cta-rules.md` | The path of your private school service page (the example is `/who-we-serve/private-school`) |
| `instructions/05-url-generation.md` and `instructions/06-internal-links.md` | Your blog URL structure (the example is `https://[YOUR-AGENCY-DOMAIN]/blog/private-school-marketing/[slug]`) and site sections |

### 3. Create your reader personas

Build 3-6 personas in `reference/k-12-private-school-personas.md`. It has a long-form template and a category guide, and `reference/READER-PERSONA-TEMPLATE.md` is a shorter fill-in version. Base them on your actual clients and prospects, with fictional names. Every post targets one of them.

### 4. Set your writer voices

`personas/writer-profiles.md` has three example voices: The Wry Strategist, The Explainer, and The Digital Native. Keep them, rename them, or write your own with `personas/WRITER-PERSONA-TEMPLATE.md`.

### 5. Set up your batch queue

Use the `batch-template.md` format to plan a month of content. The included `batch-queue.md` is a fictional example with 10 posts around a retention and re-enrollment theme. Replace it with your own topics.

### 6. Start writing

- **Single post:** Open the project in Cowork and tell Claude which topic to write about. It runs Stage 0 first, then the 8 content stages, and asks you at the approval points.
- **Batch mode:** Paste Section 1 of your batch queue into chat. Claude runs each post through all 9 stages without stopping to ask questions. Long batches use a lot of your Claude usage, so run 3 to 5 posts at a time.

## Project Structure

```
CLAUDE.md                             ← Project instructions (read automatically)
README.md                             ← You're reading this
batch-template.md                     ← Batch table format and processing rules
batch-queue.md                        ← Example topic queue (replace with yours)
.gitignore                            ← Keeps research and output files out of git

instructions/                         ← One file per pipeline stage
  00-deep-research.md
  01-topic-development.md
  02-blog-post-writing.md
  03-faq-tldr.md
  04-titles-meta-keywords.md
  05-url-generation.md
  06-internal-links.md
  07-external-links.md
  08-check-links.md

personas/
  writer-profiles.md                  ← 3 example writer voices + custom option
  WRITER-PERSONA-TEMPLATE.md          ← Template for your own writer voices

reference/
  citation-formats.md                 ← 5-format citation rotation system
  cta-rules.md                        ← CTA phrasing and link rules
  prohibited-phrases.md               ← Banned and limited phrases, in tiers
  mechanical-style-rules.md           ← House style: numbers, dates, headings, punctuation
  source-policy.md                    ← Which sources research may use, and which it never may
  k-12-private-school-competitors.md  ← Domains never to cite or link
  k-12-private-school-personas.md     ← Reader persona setup guide + template
  READER-PERSONA-TEMPLATE.md          ← Short fill-in reader persona template
  seasonal-calendar.md                ← Monthly content themes for schools

research/                             ← Stage 0 research files (gitignored)
output/                               ← Briefs and drafts (gitignored)
```

## What Makes This Different from a Prompt Template

- **Persistent context.** Claude reads the full project every session. It knows your writing rules, personas, competitors, and citation requirements without you repeating them.
- **Research before writing.** Stage 0 builds a verified research file before a word of the post is written, so the draft starts from checked facts instead of the model's memory.
- **Batch processing.** Plan a month of posts in a table, paste it in, and Claude writes them all, each through all 9 stages, without stopping to ask questions.
- **Written self-checks.** Cowork can't run QC scripts, so Stages 2 and 3 check the draft against a written checklist (prohibited-phrase tiers, a readability ceiling of grade 10 and Reading Ease 55, heading rules, em-dash limits) and leave a Self-Check block in the draft for you to review.
- **Separation of concerns.** Each stage does one thing well. Stage 0 researches. Stage 2 writes. Stage 7 verifies sources. Stage 8 independently re-checks Stage 7's work. No stage tries to do everything.

## Adapting for Other Industries

The pipeline structure works for any content vertical. To adapt:

1. Replace the school-specific topic categories in `instructions/01-topic-development.md`
2. Build new reader personas for your industry
3. Update the seasonal calendar
4. Swap the competitor list
5. Rewrite the Tier 1 source list in `reference/source-policy.md` for your industry's associations and data sources
6. Update CTA rules with your URLs
7. Swap the industry spellings at the end of `reference/mechanical-style-rules.md`

The writing rules, citation system, self-checks, batch processing logic, and stage structure all carry over as-is.
