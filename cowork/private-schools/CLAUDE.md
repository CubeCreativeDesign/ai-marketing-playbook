# K-12 Private School Blog Pipeline: Cowork Project

## About This Workspace
This is a content creation workspace for [YOUR_AGENCY], a digital marketing agency that markets TO private schools as clients. The content targets school administrators, marketing directors, and admissions teams, not parents.

**Customize this:** Replace every `[YOUR_...]` placeholder in this project with your own details. `README.md` lists each placeholder and the file it lives in.

**Note:** If you run multiple verticals (home services, pest control, and so on), create a separate Cowork project for each. This workspace covers K-12 private and independent school marketing only.

**Want a scripted, automated version?** This project runs inside the Claude Cowork chat with no code. For a Claude Code version that runs batches from the command line with automated QC scripts, see `../../claude-code/b2b-blog-pipeline/`. That one is a generic B2B template, so you'd adapt it to schools.

## How to Use This System

### Quick Start
Paste your batch queue (Section 1 of `batch-queue.md`) into chat to process a batch of posts, or name a single topic to work on it interactively.

### Pipeline Overview
This workspace runs 9 stages: Stage 0 (research) plus 8 content stages. Each stage has its own instruction file in `instructions/`. Always read the relevant instruction file before executing any stage.

0. **Deep Research** → `instructions/00-deep-research.md`
1. **Topic Development** → `instructions/01-topic-development.md`
2. **Blog Post Writing** → `instructions/02-blog-post-writing.md`
3. **FAQ and TL;DR Review** → `instructions/03-faq-tldr.md`
4. **Titles, Meta Description, and Keywords** → `instructions/04-titles-meta-keywords.md`
5. **URL/Slug Generation** → `instructions/05-url-generation.md`
6. **Internal Linking** → `instructions/06-internal-links.md`
7. **External Link Verification** → `instructions/07-external-links.md`
8. **Link Checking** → `instructions/08-check-links.md`

Run Stage 0 and then Stages 1 through 8 in sequence on each post. Files:

- Stage 0 saves its research to `research/[topic-slug]-research.md`.
- Stage 1 saves the brief to `output/[topic-slug]-brief.md`.
- Stages 2 through 8 all update one file: `output/[topic-slug]-draft.md`. Stages 4 and 5 add the title package and the Publishing Package at the top. The Self-Check blocks sit at the end.

The person running the project reviews each finished draft in the Cowork chat before anything is published. Nothing in this pipeline publishes on its own.

### Self-Check instead of QC scripts
Cowork has no scripts, so quality checks are written self-checks. Claude reads the draft against the rules below, `reference/prohibited-phrases.md`, and `reference/mechanical-style-rules.md`, then writes a short Self-Check block into the draft. Stage 2 writes `## Stage 2 Self-Check` and Stage 3 writes `## Stage 3 Self-Check`, both under the `# Links` heading at the end of the draft. Each block lists every check as PASS or WARN with the reason, and flags anything that needs your decision. The blocks are internal notes: they don't count toward the word count, and you remove them before publishing. Stages 2 and 3 give the full checklist.

## Batch Mode
For processing multiple topics from a table, see `batch-template.md` for the required table format and batch mode rules. The active queue is `batch-queue.md`. In batch mode, all approval gates and questions are skipped. Inputs come from the table.

## Cross-Vertical Adaptation
Some posts may be adapted from other industry verticals. When the user provides source content from another vertical, adapt it for private schools by swapping industry-specific examples, personas, keywords, and data points. The user will specify whether to keep the same structure or write fresh from the same angle.

## Project Structure

```
CLAUDE.md                             ← This file (project instructions)
README.md                             ← Setup guide
batch-template.md                     ← Batch table format and rules
batch-queue.md                        ← Active topic queue (example included)
instructions/
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
  writer-profiles.md                  ← Writer voices ([WRITER_1] to [WRITER_3] + custom)
  WRITER-PERSONA-TEMPLATE.md          ← Template for your own writer voices
reference/
  citation-formats.md                 ← 5-format citation rotation system
  cta-rules.md                        ← Contact CTA and who-we-serve link rules
  prohibited-phrases.md               ← Banned and limited phrases, by tier
  mechanical-style-rules.md           ← Numbers, dates, headings, punctuation
  source-policy.md                    ← Which sources research may use
  k-12-private-school-competitors.md  ← Competitor domains never to cite or link
  k-12-private-school-personas.md     ← Reader persona setup guide
  READER-PERSONA-TEMPLATE.md          ← Short fill-in reader persona template
  seasonal-calendar.md                ← Seasonal content planning
research/                             ← Stage 0 research files
output/                               ← Briefs and drafts
```

## Global Writing Rules (Apply to ALL Content)
- AP Style with Oxford comma. `reference/mechanical-style-rules.md` has the full house style.
- Short paragraphs (2-4 sentences)
- Active voice preferred
- Contractions are welcome. They read faster.
- Em dashes: at most 1 per 300 words of main body. Each one has to earn its place. Replace extras with a period, a comma, or parentheses.
- Readability ceiling: Flesch-Kincaid grade 10 or lower, and Flesch Reading Ease 55 or higher, measured on the main body. Copy that reads easier is never a miss. Past the ceiling, note it in the Self-Check as a warning.
- The intro's first sentence is 12 words or fewer and names the reader's problem or the takeaway.
- Headings: H1 to H3 only, AP title case. No bold text used as a heading, and no horizontal rules in the body.
- No emojis in blog content
- Include specific data points and statistics where relevant. Every statistic must be cited and confirmed on its source page.
- All claims must be verifiable. Private school administrators are detail-oriented professionals who cross-check statistics and lose trust in content that doesn't hold up.
- All blog posts end with one primary CTA linking to: https://[YOUR-AGENCY-DOMAIN]/contact
- All content should position [YOUR_AGENCY] as the knowledgeable, approachable expert who understands K-12 private school marketing and the enrollment funnel.

### CMS Positioning
- [YOUR_AGENCY] is a [YOUR_CMS] shop. Always position [YOUR_CMS] as the preferred CMS.
- Never recommend [ALTERNATIVE_CMS] as a first choice.
- If [ALTERNATIVE_CMS] comes up, acknowledge its market share, then pivot to its real drawbacks: security vulnerabilities, plugin dependency bloat, update breakage, and the true cost of ongoing maintenance.
- Never write content that makes [ALTERNATIVE_CMS] sound like the safer or easier choice.
- Delete this section if your agency doesn't take a CMS position.

### Words and Phrases
`reference/prohibited-phrases.md` is the source of truth. Its tiers decide how strict each entry is. The short version:

- **Never use (hard ban):** "leverage", "utilize", "robust", "synergy", "streamline", "cutting-edge", "holistic", "paradigm shift", "game-changer", "showcasing", "testament", "vibrant", "crucial", "critical", "landscape", "in today's digital age", "in today's fast-paced world", "in the ever-evolving landscape", "it's important to note", "it's worth noting", "dive into", "deep dive", "navigate", "at the end of the day", "move the needle", "in order to"
- **Headings only:** "unlock", "discover", "boost", "grow", "optimize", "delve", "revolutionize" are a warning in a heading unless it carries a number. They're fine in body copy, though "unlock" and "delve" sit on the avoid list there.
- **Everything else** (vague attribution, unproven claims, AI-tell words, chatbot residue, contrast frames) follows its tier in `reference/prohibited-phrases.md`.
