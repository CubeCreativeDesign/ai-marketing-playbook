# Batch Processing Template

## Purpose
This template defines the table format for running the 8-stage blog pipeline in batch mode. Each row represents one blog post. All stages pull their inputs from this table instead of asking questions.

---

## Required Table Format

| Column | Description | Example Values | Used By |
|--------|-------------|----------------|---------|
| **Topic** | The blog post topic or angle | "Email marketing for private school enrollment" | Stage 1, 2 |
| **Primary Keyword** | Main keyword to target | "private school email marketing" | Stage 1, 2, 4, 5 |
| **Secondary Keywords** | Supporting keywords (comma-separated) | "enrollment emails, admissions follow-up, school drip campaigns" | Stage 1, 2, 4 |
| **Writer Persona** | Which voice to write in. See `personas/writer-profiles.md` for options. | Adam, Chad, Hannah, or Custom | Stage 2 |
| **Reader Persona** | Target audience persona from your persona set. See `reference/k-12-private-school-personas.md` for setup guide. | Your persona names go here | Stage 2 |
| **Content Balance** | SEO vs. narrative ratio | SEO-Heavy (70/30), Balanced (50/50), Narrative-Heavy (30/70) | Stage 2 |
| **Goal** | Primary content objective | Awareness, Lead Generation, Thought Leadership | Stage 1 |
| **Word Count Guideline** | Approximate length target | 1200, 1500, 2000 (treat as guideline, not hard limit) | Stage 2 |
| **Seasonal Tie-In** | Seasonal relevance, if any | "Spring enrollment push", "Back to school", "None" | Stage 1, 2 |
| **Research/Notes** | Deep Research link or additional context | URL to research doc, special instructions, or "None" | Stage 1, 2 |

---

## Example Table

| Topic | Primary Keyword | Secondary Keywords | Writer | Reader | Balance | Goal | Word Count | Seasonal | Research/Notes |
|-------|----------------|-------------------|--------|--------|---------|------|------------|----------|----------------|
| Email marketing for private school enrollment | private school email marketing | enrollment emails, admissions follow-up, school drip campaigns | Adam | Marketing Director Persona | Balanced 50/50 | Lead Generation | 1500 | Spring enrollment push | None |
| How private schools can improve their Google Business Profile | private school Google Business Profile | school GBP optimization, local SEO for schools | Adam | Principal Persona | SEO-Heavy 70/30 | Awareness | 1200 | None | None |
| Social media strategies for faith-based schools | faith-based school social media | church school marketing, religious school Facebook | Hannah | Faith-Based Admin Persona | Narrative-Heavy 30/70 | Thought Leadership | 1800 | Back to school | https://docs.google.com/doc/d/xxx |

---

## Batch Mode Behavior

When processing from this table, all stages operate in batch mode:

### Stage 1: Topic Development
- Skip "Ask for Direction" — all inputs come from the table row
- Generate the topic brief directly using the provided Topic, Primary Keyword, Secondary Keywords, Goal, Seasonal Tie-In, and Research/Notes
- If Research/Notes contains a link, fetch and integrate that research
- Save the brief to `output/[topic-slug]-brief.md` and proceed immediately

### Stage 2: Blog Post Writing
- Skip persona selection questions — use Writer Persona and Reader Persona from the table
- Skip content balance confirmation — use Content Balance from the table
- Skip outline approval gate — write the full draft in one pass
- Skip section-by-section approval — write all sections continuously
- Use Word Count Guideline as a guideline, not a hard limit
- Save to `output/[topic-slug]-draft.md` and proceed immediately

### Stage 3: FAQ and TL;DR Review
- No changes needed — Stage 3 has no approval gates
- Read the draft, review, update, save

### Stage 4: Titles, Meta Description, and Keywords
- Generate all 5 complete title sets (SEO + Article + Image) — do not skip to just the recommendation
- Auto-select the recommended titles (the best pick from each tier becomes the selection)
- Generate all deliverables and insert at top of draft

### Stage 5: URL/Slug Generation
- Auto-accept Stage 4's recommended SEO title as input
- Generate slug options and auto-select the recommended option
- Add Publishing Package to top of draft
- Note the duplicate check reminder for the user but do not pause

### Stage 6: Internal Linking
- No changes needed — Stage 6 already applies without asking
- Note blog post URL status but do not pause

### Stage 7: External Link Verification
- No changes needed — Stage 7 already applies without asking

### Stage 8: Link Checking
- No changes needed — Stage 8 already applies without asking
- Perform full independent re-verification using the tiered system — do not rubber-stamp Stage 7

---

## Processing Order
For each row in the table, run all 8 stages in sequence before moving to the next row:
1. Stage 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
2. Move to next row
3. Repeat

---

## File Naming Convention
The `[topic-slug]` used in file names should be a short, hyphenated version of the topic:
- "Email marketing for private school enrollment" → `email-marketing-enrollment`
- "How private schools can improve their Google Business Profile" → `school-google-business-profile`

The slug used in file names does NOT need to match the final URL slug generated in Stage 5. It's just for organizing output files.
