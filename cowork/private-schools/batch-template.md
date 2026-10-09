# Batch Processing Template

## Purpose
This template defines the table format for running the blog pipeline (Stage 0 plus 8 content stages) in batch mode. Each row represents one blog post. All stages pull their inputs from this table instead of asking questions.

---

## Required Table Format

| Column | Description | Example Values | Used By |
|--------|-------------|----------------|---------|
| **Topic** | The blog post topic or angle | "Email marketing for private school enrollment" | Stage 0, 1, 2 |
| **Primary Keyword** | Main keyword to target | "private school email marketing" | Stage 0, 1, 2, 4, 5 |
| **Secondary Keywords** | Supporting keywords (comma-separated) | "enrollment emails, admissions follow-up, school drip campaigns" | Stage 1, 2, 4 |
| **Writer Persona** | Which voice to write in. Use the voice name from `personas/writer-profiles.md`. The three examples fill the `[WRITER_1]`, `[WRITER_2]`, and `[WRITER_3]` slots that Stage 2 refers to. | The Wry Strategist ([WRITER_1], default), The Explainer ([WRITER_2]), The Digital Native ([WRITER_3]), or Custom | Stage 2 |
| **Reader Persona** | Target audience persona. Use a persona name from your copy of `reference/k-12-private-school-personas.md` (Stage 2 calls these `[PERSONA_NAME]`). | Your persona names go here | Stage 1, 2 |
| **Content Balance** | SEO vs. narrative ratio | SEO-Heavy (70/30), Balanced (50/50), Narrative-Heavy (30/70) | Stage 2 |
| **Goal** | Primary content objective | Awareness, Lead Generation, Thought Leadership | Stage 1 |
| **Word Count Guideline** | Approximate main-body length (intro through conclusion, not counting the TL;DR and FAQ) | 1200, 1500, 2000 (a guideline, not a cap) | Stage 2 |
| **Seasonal Tie-In** | Seasonal relevance, if any. See `reference/seasonal-calendar.md`. | "Spring enrollment push", "Back to school", "None" | Stage 1, 2 |
| **Research/Notes** | Extra research or context. Stage 0 writes its own research file, so use this column for anything on top of that. | A URL, a file you uploaded to the project, special instructions, or "None" | Stage 0, 1, 2 |
| **Publish Date** *(optional)* | Your scheduled publish date, for your own content calendar. The stages don't use it, and it does not change the file name. Use ISO form (`2027-04-05`). Leave it blank if the date isn't set. | "2027-04-05", blank | You (planning) |

---

## Example Table

| Topic | Primary Keyword | Secondary Keywords | Writer | Reader | Balance | Goal | Word Count | Seasonal | Research/Notes | Publish Date |
|-------|----------------|-------------------|--------|--------|---------|------|------------|----------|----------------|--------------|
| Email marketing for private school enrollment | private school email marketing | enrollment emails, admissions follow-up, school drip campaigns | The Explainer | Your Marketing Director Persona | Balanced 50/50 | Lead Generation | 1500 | Spring enrollment push | None | 2027-03-01 |
| How private schools can improve their Google Business Profile | private school Google Business Profile | school GBP optimization, local SEO for schools | The Wry Strategist | Your Head of School Persona | SEO-Heavy 70/30 | Awareness | 1200 | None | None | 2027-03-03 |
| Social media strategies for faith-based schools | faith-based school social media | church school marketing, religious school Facebook | The Digital Native | Your Faith-Based Admin Persona | Narrative-Heavy 30/70 | Thought Leadership | 1800 | Back to school | Focus on Instagram and Facebook groups | 2027-03-05 |

---

## Batch Mode Behavior

When processing from this table, all stages operate in batch mode. You still review the finished drafts. Batch mode only skips the questions in between.

### Stage 0: Deep Research
- Use the Topic, Primary Keyword, and Reader Persona to frame the research questions
- Follow `reference/source-policy.md`: skip competitor domains, prefer Tier 1 sources, and confirm every statistic on the source page
- If Research/Notes contains a link or an uploaded file, read it and fold it in
- Save to `research/[topic-slug]-research.md` and proceed immediately

### Stage 1: Topic Development
- Skip "Ask for Direction." All inputs come from the table row and the Stage 0 research file
- Generate the topic brief directly using the provided Topic, Primary Keyword, Secondary Keywords, Goal, Seasonal Tie-In, and Research/Notes
- Save the brief to `output/[topic-slug]-brief.md` and proceed immediately

### Stage 2: Blog Post Writing
- Skip persona selection questions. Use Writer Persona and Reader Persona from the table
- Skip content balance confirmation. Use Content Balance from the table
- Skip the outline approval gate. Write the full draft in one pass
- Skip section-by-section approval. Write all sections continuously
- Use Word Count Guideline as a guideline, not a hard limit
- Run the written Self-Check and add the `## Stage 2 Self-Check` block at the end of the draft
- Save to `output/[topic-slug]-draft.md` and proceed immediately

### Stage 3: FAQ and TL;DR Review
- No changes needed. Stage 3 has no approval gates
- Read the draft, review, update, re-run the Self-Check, write the `## Stage 3 Self-Check` block, save

### Stage 4: Titles, Meta Description, and Keywords
- Generate all 5 complete title sets (SEO + Article + Image). Do not skip to just the recommendation
- Auto-select the recommended titles (the best pick from each tier becomes the selection)
- Generate all deliverables and insert at top of draft

### Stage 5: URL/Slug Generation
- Auto-accept Stage 4's recommended SEO title as input
- Generate slug options and auto-select the recommended option
- Add the Publishing Package to the top of the draft
- Note the duplicate-check reminder for the user but do not pause

### Stage 6: Internal Linking
- No changes needed. Stage 6 already applies without asking
- Note blog post URL status but do not pause

### Stage 7: External Link Verification
- No changes needed. Stage 7 already applies without asking

### Stage 8: Link Checking
- No changes needed. Stage 8 already applies without asking
- Perform full independent re-verification. Do not rubber-stamp Stage 7

---

## Processing Order
For each row in the table, run Stage 0 and all 8 content stages in sequence before moving to the next row:
1. Stage 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
2. Move to the next row
3. Repeat

Long batches use a lot of your Claude usage. If you're on a plan with a usage window, run 3 to 5 posts at a time and check the drafts between runs.

---

## File Naming Convention
The `[topic-slug]` used in file names should be a short, hyphenated version of the topic:
- "Email marketing for private school enrollment" → `email-marketing-enrollment`
- "How private schools can improve their Google Business Profile" → `school-google-business-profile`

Each post produces three files:
- `research/[topic-slug]-research.md` (Stage 0)
- `output/[topic-slug]-brief.md` (Stage 1)
- `output/[topic-slug]-draft.md` (Stages 2 through 8 all update this one file)

The slug used in file names does NOT need to match the final URL slug generated in Stage 5. It's just for organizing output files.
