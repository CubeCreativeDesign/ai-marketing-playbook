# Batch Processing Template

## Purpose
This template defines the table format for running the 8-stage blog pipeline in batch mode. Each row represents one blog post. All stages pull their inputs from this table instead of asking questions.

---

## Required Table Format

| Column | Description | Example Values | Used By |
|--------|-------------|----------------|---------|
| **Topic** | The blog post topic or angle | "Google Ads strategies for [YOUR_VERTICAL] companies" | Stage 1, 2 |
| **Primary Keyword** | Main keyword to target | "[YOUR_VERTICAL] Google Ads" | Stage 1, 2, 4, 5 |
| **Secondary Keywords** | Supporting keywords (comma-separated) | "[YOUR_VERTICAL] PPC, [SERVICE_PROVIDER] ads, [YOUR_VERTICAL] lead generation" | Stage 1, 2, 4 |
| **Writer Persona** | Which voice to write in. **[PERSONA_NAME_1]** is the default writer. **[PERSONA_NAME_2]** is used for heavy business or PPC/LSA content. **[PERSONA_NAME_3]** is used only for social media content. | [PERSONA_NAME_1] (default), [PERSONA_NAME_2] (business/PPC), [PERSONA_NAME_3] (social media only), or Custom | Stage 2 |
| **Reader Persona** | Target audience by company size tier | Startup (1-5), Growing (5-10), Mid-Size (11-30), Established (31-50), Regional (51-100), Enterprise (101-150) | Stage 2 |
| **Content Balance** | SEO vs. narrative ratio | SEO-Heavy (70/30), Balanced (50/50), Narrative-Heavy (30/70) | Stage 2 |
| **Goal** | Primary content objective | Awareness, Lead Generation, Thought Leadership | Stage 1 |
| **Word Count Guideline** | Approximate length target | 1200, 1500, 2000 (treat as guideline, not hard limit) | Stage 2 |
| **Seasonal Tie-In** | Seasonal relevance, if any | "[PEAK_SEASON]", "[OFF_SEASON] service demand", "None" | Stage 1, 2 |
| **Research/Notes** | Deep Research link or additional context | URL to research doc, special instructions, or "None" | Stage 1, 2 |
| **Publish Date** *(optional)* | Scheduled publish date. When present, the router carries it through to the output filename (`YYYY-MM-DD-[slug]-draft.md`). Recognized headers: "Publish Date", "Scheduled Publish Date", "Date / Status", "Date". Accepts ISO (`2026-09-02`) or human form (`Sep 2`, `Sept 30, 2026` — year defaults to the current calendar year if omitted). Vague values ("flex (Sep)", "TBD") are left unparsed rather than guessed at — leave the cell blank or fix the date once it's fixed. | "2026-09-02", "Sep 30", "None" | Router |

For a single topic seed or brief file (not a batch table), the same date can be set with an inline marker anywhere in the file: `Publish Date: 2026-09-02` or `Scheduled: Sep 30`.

---

## Example Table

| Topic | Primary Keyword | Secondary Keywords | Writer | Reader | Balance | Goal | Word Count | Seasonal | Research/Notes |
|-------|----------------|-------------------|--------|--------|---------|------|------------|----------|----------------|
| Google Ads strategies for [YOUR_VERTICAL] companies | [YOUR_VERTICAL] Google Ads | [YOUR_VERTICAL] PPC, [SERVICE_PROVIDER] ads, [YOUR_VERTICAL] lead generation | [WRITER_2] | Growing (5-10) | Balanced 50/50 | Lead Generation | 1500 | None | None |
| How [YOUR_VERTICAL] companies can improve their Google Business Profile | [YOUR_VERTICAL] Google Business Profile | GBP optimization [YOUR_VERTICAL], local SEO for [SERVICE_PROVIDER]s | [WRITER_1] | Startup (1-5) | SEO-Heavy 70/30 | Awareness | 1200 | None | None |
| Social media strategies for [YOUR_VERTICAL] companies | [YOUR_VERTICAL] social media | [SERVICE_PROVIDER] Facebook marketing, [YOUR_VERTICAL] Instagram | [WRITER_3] | Mid-Size (11-30) | Narrative-Heavy 30/70 | Thought Leadership | 1800 | None | https://docs.google.com/doc/d/xxx |

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
- No changes needed — Stage 4 has no approval gates
- IMPORTANT: Generate all 5 complete title sets (SEO + Article + Image) as specified in the instructions — do not skip to just the recommendation
- After generating all 5 sets, auto-select the recommended titles (the best pick from each tier becomes the selection)
- Generate all deliverables (titles, meta description, keywords) and insert at top of draft

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
- Since Stage 8 runs immediately after Stage 7, focus on link-alive testing; only re-verify content match if a link status appears to have changed

---

## Processing Order
For each row in the table, run all 8 stages in sequence before moving to the next row:
1. Stage 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
2. Move to next row
3. Repeat

---

## File Naming Convention
The `[topic-slug]` used in file names should be a short, hyphenated version of the topic:
- "Google Ads strategies for [YOUR_VERTICAL] companies" → `google-ads-strategies`
- "How [YOUR_VERTICAL] companies can improve their Google Business Profile" → `google-business-profile`

The slug used in file names does NOT need to match the final URL slug generated in Stage 5. It's just for organizing output files.
