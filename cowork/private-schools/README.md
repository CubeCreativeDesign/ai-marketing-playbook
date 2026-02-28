# Private School Blog Pipeline — Claude Cowork Project

An 8-stage blog content pipeline built for Claude's Cowork feature. Designed for digital marketing agencies that market TO K-12 private schools (targeting school administrators, marketing directors, and admissions teams).

This isn't a prompt template you paste into chat. It's a full Cowork project — a structured workspace with instructions, personas, reference files, and a batch processing system that Claude reads and follows automatically.

## What This Does

You give Claude a blog topic (or a batch of 14 at once). It runs each topic through 8 stages:

1. **Topic Development** — Validates the topic, generates a keyword brief
2. **Blog Post Writing** — Writes the full draft with citations, FAQ, TL;DR, and CTA
3. **FAQ & TL;DR Review** — Quality checks the FAQ and summary sections
4. **Titles, Meta, Keywords** — Generates 5 title sets across 3 tiers, meta description, and keyword list
5. **URL/Slug Generation** — Creates SEO-friendly URL slugs
6. **Internal Linking** — Finds and adds links to your other content
7. **External Link Verification** — Verifies every citation source is live and accurate
8. **Link Checking** — Final independent verification of all links before publishing

Each stage has its own instruction file. Claude reads the instructions, does the work, saves to the output folder, and moves to the next stage.

## Who This Is For

- **Marketing agencies** that create blog content for private school clients
- **In-house school marketers** running their own content programs
- **Anyone** who wants to see how a production-grade Cowork project is structured

Even if you don't market to schools, the pipeline structure (8 stages, batch processing, writer/reader personas, citation verification) works for any industry. Fork it and swap the vertical.

## How to Set It Up

### 1. Copy the project into a Claude Cowork workspace

Create a new Cowork project in Claude and add all the files from this directory. The `CLAUDE.md` file will be read automatically as project instructions.

### 2. Customize the placeholder files

Several files contain `yoursite.com` placeholders and setup instructions. You need to replace these with your own info:

| File | What to customize |
|------|-------------------|
| `CLAUDE.md` | Your agency name and description |
| `reference/cta-rules.md` | Your contact page URL and service page URL |
| `reference/k-12-private-school-personas.md` | Build your own reader personas using the template provided |
| `reference/k-12-private-school-competitors.md` | Add your actual competitor domains |
| `instructions/01-topic-development.md` | Your agency description in the "Who We Are" section |
| `instructions/02-blog-post-writing.md` | Your agency description and reader persona table |
| `instructions/05-url-generation.md` | Your blog URL structure |
| `instructions/06-internal-links.md` | Your site structure for internal linking |

### 3. Create your reader personas

The personas file (`reference/k-12-private-school-personas.md`) includes a template and category guide. Create 3-6 personas based on your actual clients and prospects. These are used in every blog post to target specific audience segments.

### 4. Set up your batch queue

Copy `batch-template.md` format to plan a month of content. The included `batch-queue.md` is an example showing 14 posts around a retention/re-enrollment theme. Replace it with your own topics.

### 5. Start writing

- **Single post:** Open the project in Cowork and tell Claude which topic to write about
- **Batch mode:** Paste your batch queue into chat and Claude will process each post through all 8 stages automatically

## Project Structure

```
CLAUDE.md                           ← Project instructions (read automatically)
README.md                          ← You're reading this
batch-template.md                   ← Batch table format and processing rules
batch-queue.md                      ← Example topic queue (replace with yours)
.gitignore                          ← Keeps output files and .DS_Store out of git

instructions/                       ← One file per pipeline stage
  01-topic-development.md
  02-blog-post-writing.md
  03-faq-tldr.md
  04-titles-meta-keywords.md
  05-url-generation.md
  06-internal-links.md
  07-external-links.md
  08-check-links.md

personas/
  writer-profiles.md                ← 3 writer voices + custom option

reference/
  citation-formats.md               ← 5-format citation rotation system
  cta-rules.md                      ← CTA phrasing and link rules
  prohibited-phrases.md             ← Banned words (AI-sounding phrases, buzzwords)
  k-12-private-school-competitors.md ← Domains to avoid linking
  k-12-private-school-personas.md   ← Reader persona setup guide + template
  seasonal-calendar.md              ← Monthly content themes for schools

output/                             ← Drafts saved here (gitignored)
```

## What Makes This Different from a Prompt Template

- **Persistent context.** Claude reads the full project every session. It knows your writing rules, personas, competitors, and citation requirements without you repeating them.
- **Batch processing.** Plan 14 posts in a table, paste it in, and Claude writes them all — each through all 8 stages — without stopping to ask questions.
- **Quality guardrails.** Prohibited phrases, citation verification, competitor link blocking, and independent link re-checking are built into the pipeline.
- **Separation of concerns.** Each stage does one thing well. Stage 2 writes. Stage 7 verifies sources. Stage 8 independently re-checks Stage 7's work. No stage tries to do everything.

## Adapting for Other Industries

The pipeline structure works for any content vertical. To adapt:

1. Replace the school-specific topic categories in `01-topic-development.md`
2. Build new reader personas for your industry
3. Update the seasonal calendar
4. Swap the competitor list
5. Adjust the approved source tiers in `07-external-links.md`
6. Update CTA rules with your URLs

The writing rules, citation system, batch processing logic, and 8-stage structure all carry over as-is.
