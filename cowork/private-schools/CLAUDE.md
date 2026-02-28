# K-12 Private School Blog Pipeline — Cowork Project

## About This Workspace
This is a content creation workspace for a digital marketing agency that markets TO private schools as clients. The content targets school administrators, marketing directors, and admissions teams — not parents.

**Customize this:** Replace references to your agency name, website URLs, and service pages throughout this project to match your own business.

**Note:** If you run multiple verticals (home services, pest control, etc.), create separate Cowork projects for each. This workspace covers K-12 private and independent school marketing only.

## How to Use This System

### Quick Start
Open your batch queue and paste it into chat to begin processing blog posts, or start a new topic interactively.

### Pipeline Overview
This workspace contains an 8-stage blog post creation pipeline. Each stage has its own instruction file in `instructions/`. Always read the relevant instruction file before executing any stage.

1. **Topic Development** → `instructions/01-topic-development.md`
2. **Blog Post Writing** → `instructions/02-blog-post-writing.md`
3. **FAQ and TL;DR Review** → `instructions/03-faq-tldr.md`
4. **Titles, Meta Description, and Keywords** → `instructions/04-titles-meta-keywords.md`
5. **URL/Slug Generation** → `instructions/05-url-generation.md`
6. **Internal Linking** → `instructions/06-internal-links.md`
7. **External Link Verification** → `instructions/07-external-links.md`
8. **Link Checking** → `instructions/08-check-links.md`

Run all 8 stages in sequence on each post. All stages save to the same file: `output/[topic-slug]-draft.md`.

## Batch Mode
For processing multiple topics from a table, see `batch-template.md` for the required table format and batch mode rules. The active queue is `batch-queue.md`. In batch mode, all approval gates and questions are skipped — inputs come from the table.

## Cross-Vertical Adaptation
Some posts may be adapted from other industry verticals. When the user provides source content from another vertical, adapt it for private schools by swapping industry-specific examples, personas, keywords, and data points. The user will specify whether to keep the same structure or write fresh from the same angle.

## Project Structure

```
CLAUDE.md                           ← This file (project instructions)
batch-template.md                   ← Batch table format and rules
batch-queue.md                      ← Active topic queue (example included)
instructions/
  01-topic-development.md
  02-blog-post-writing.md
  03-faq-tldr.md
  04-titles-meta-keywords.md
  05-url-generation.md
  06-internal-links.md
  07-external-links.md
  08-check-links.md
personas/
  writer-profiles.md                ← Writer voice personas
reference/
  citation-formats.md               ← 5-format citation rotation system
  cta-rules.md                      ← Contact CTA and service page link rules
  prohibited-phrases.md             ← Banned words and phrases for all content
  k-12-private-school-competitors.md ← Competitor domains to avoid linking
  k-12-private-school-personas.md   ← Reader persona setup guide
  seasonal-calendar.md              ← Seasonal content planning
output/                             ← All draft files saved here
```

## Global Writing Rules (Apply to ALL Content)
- AP Style with Oxford comma
- Short paragraphs (2-4 sentences)
- Active voice preferred
- No em dashes (use semicolons, periods, parentheses)
- Maximum 1 em dash per 200 words if unavoidable
- No emojis in blog content
- Include specific data points and statistics where relevant — every statistic must be cited
- All blog posts end with a CTA linking to your contact page
- All content should position your agency as the knowledgeable, approachable expert

### Words and Phrases to NEVER Use
- "landscape", "crucial", "critical", "it's important to note", "it's worth noting"
- "in today's digital age", "in today's fast-paced world", "in the ever-evolving landscape"
- "game-changer", "dive into", "deep dive", "navigate", "leverage", "robust"
- "streamline", "cutting-edge", "holistic", "synergy", "paradigm shift", "utilize"
- "showcasing", "testament", "vibrant"
- "unlock", "discover", "boost", "grow", "optimize", "delve", "revolutionize"

See `reference/prohibited-phrases.md` for the complete list.
