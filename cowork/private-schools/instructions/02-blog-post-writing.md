# Stage 2: Blog Post Writing

Stage 2 writes the full draft from the Stage 1 brief and the Stage 0 research bundle, then checks it against a written self-check before saving.

**Output feeds:** Stage 3 runs the full self-check on this draft and refines its FAQ and TL;DR. Stage 4 writes titles and the meta description from it. Stages 6, 7 and 8 add and verify links under the `# Links` heading you create. Every statistic you cite here goes live, so each one must trace to a source you fetched.

**Human check:** You, in the Cowork chat. In interactive mode, you approve the outline before drafting and give feedback section by section. In batch mode Claude writes the whole draft in one pass, so read the `## Stage 2 Self-Check` block at the end of the draft: anything it marks for human review is yours to decide before the post publishes.

## Purpose
Write the full blog post based on the topic brief from Stage 1. Accept the topic brief as your starting point. Do not re-decide keywords, audience, content balance, or word count. Those decisions are already made.

## Who We Are
**[YOUR_AGENCY]** markets TO private schools as clients. We are not writing on behalf of schools to parents. Our audience is school administrators, marketing directors, and admissions teams evaluating whether to hire a marketing agency.

Parent researchers are a secondary audience: schools share our content, and it builds topical authority. Write for the administrator first, but content that a prospective-family researcher would also find credible is a bonus, not a distraction.

**Internal Link Requirement:** Every blog post introduction must include ONE natural link to your who-we-serve page. See `reference/cta-rules.md` for the URL, approved anchor text options, and CTA format.

---

## Batch Mode
When processing from a batch table (see `batch-template.md`; the active queue is `batch-queue.md`), skip all Pre-Writing Setup questions. Pull Writer Persona, Reader Persona, and Content Balance directly from the table row. Skip outline approval and section-by-section feedback. Write the full draft in one continuous pass and save.

---

## Pre-Writing Setup

### Select Writer Persona
*In batch mode, use the Writer Persona from the table row.*

Ask the user which voice to use. See `personas/writer-profiles.md` for full profile details. (Create that file from `personas/WRITER-PERSONA-TEMPLATE.md` if it doesn't exist yet.)

| Persona | Style | Best For |
|---------|-------|----------|
| **[WRITER_1]** | Professional with sarcasm, witty | Technical topics, strategy, data-heavy (DEFAULT) |
| **[WRITER_2]** | Professional with analogies, dad jokes | How-to guides, broad audience, introductory |
| **[WRITER_3]** | Millennial/Gen Z, casual professional | Social media, parent engagement, modern tactics |
| **Custom** | User-specified | Ask for style, tone, reading level, voice references |

### Select Target Reader Persona
*In batch mode, use the Reader Persona from the table row.*

Ask the user which reader persona the content should target. See `reference/k-12-private-school-personas.md` for full persona details, and `reference/READER-PERSONA-TEMPLATE.md` to add your own.

| Persona | Role | Focus |
|---------|------|-------|
| **[PERSONA_NAME]** | Director of Admissions & Marketing | Enrollment, brand, vendor decisions, $50K-$250K budget |
| **[PERSONA_NAME]** | Head of School/Principal (Mid-Range) | Strategic oversight, faculty, board relations, 260 students |
| **[PERSONA_NAME]** | Principal/Director (Lower-Cost) | Budget-conscious, mission-driven, hands-on, $3K-$5K tuition |
| **[PERSONA_NAME]** | Director of Virtual Academy | Online education, national reach, tech-forward |
| **[PERSONA_NAME]** | Principal, Faith-Based K-8 | Church-affiliated, smaller school, community marketing |
| **[PERSONA_NAME]** | Parent Researcher/Influencer | Active volunteer, word-of-mouth driver, quality evaluator |

Use the persona names from your copy of `reference/k-12-private-school-personas.md` in the first column.

Tailor language, examples, pain points, and solutions to the selected reader persona. **Ground every example in the selected persona's school type, enrollment, tuition, and budget** as documented in `reference/k-12-private-school-personas.md`. A 165-student faith-based K-8 on a $3K-$5K tuition does not market the way a 600-student college prep does. If the user wants to target multiple personas, optimize the primary sections for the lead persona and include secondary angles where natural.

### Confirm Content Balance
*In batch mode, use the Content Balance from the table row.*

Verify with the user (or accept from the Stage 1 brief):
- **SEO-Heavy (70/30)**: Keyword-dense, featured snippet targeting, structured for search
- **Balanced (50/50)**: Equal emphasis on readability and optimization
- **Narrative-Heavy (30/70)**: Story-driven, brand voice forward, light optimization

---

## Evidence: The Stage 0 Research Bundle

Open `research/[topic-slug]-research.md` before you write. It is your primary evidence. Stage 0 already searched, fetched and fact-checked it, and the Stage 1 brief lists the items the angle rests on.

- **Start with the bundle's verified items.** Use its quotes and statistics before you search for new ones.
- **The bundle narrows, it does not authorize.** Before a claim goes in the draft, fetch its URL with web fetch and confirm the figure is still on the page. Pages change between research and writing.
- **Earlier bundles in `research/` are a second pass.** A claim from another topic's bundle can still apply where the audience genuinely matches. Re-verify it the same way. If you've already used a statistic in several posts, prefer an unused one that makes the same point.

## Research and Verification

### Before Writing, You Must:
1. Read the Stage 0 bundle, then run web searches for anything the outline needs that the bundle does not cover
2. Identify key statistics with their original sources
3. Verify all statistics and claims through authoritative sources
4. Focus on recent data (within 2-3 years) unless historical context is needed
5. Prioritize sources: NAIS, NCES, Cognia, CAPE, ISM, AISAP, educational journals, government education data, EdTech publications. Follow `reference/source-policy.md` and never cite a domain in `reference/k-12-private-school-competitors.md`.

### Credibility Standard: Critical
Private school administrators are educated, detail-oriented professionals. They read widely, compare vendors carefully, and will lose trust in content that overstates outcomes or cites numbers that don't hold up. Every statistic, benchmark, and claim must be:

- Verifiable from a specific, credible source
- Realistic for the school type and size being targeted
- Presented honestly without exaggeration or rounding that changes the meaning

If you cannot verify a specific number, use broader trend language instead. A vague but honest statement is always better than a precise but fabricated one.

### Extra Research the User Provides
If the user attached research of their own (a report, a Research chat, a Research/Notes link):
- Cross-reference the draft against those findings
- Identify gaps where the research covers something the draft does not
- Verify that statistics match the research sources, at the primary source
- Add relevant data points that strengthen the argument, once verified

### Handling `unverified` Items from the Stage 0 Bundle

Stage 0's fact-check gate tags every quote and statistic it could not confirm against its source page as `unverified`. Treat that tag as **blocking**:

- Never state an `unverified` number as fact.
- Either verify it yourself per the rules below, replace it with a verified equivalent, or drop it and use broader trend language.
- Never launder it by rewording ("studies suggest," "roughly"). The problem is that nobody confirmed the number, and rewording hides that instead of fixing it.
- If the draft would be materially weaker without it, say so in your Stage 2 Self-Check block rather than shipping the claim.

### Source Verification Rules: Blocking, Not Aspirational

- EVERY link must be verified as working AND containing the cited statistic.
- "Verified" means: you fetched the URL with web fetch during Stage 2 and saw the specific number or quote in the page text. Reading a Research report, a search snippet or a secondary summary is NOT verification.
- If web fetch cannot open the page (paywall, block, timeout), the claim is unverified. Find another copy of the same source, or treat it as unverified.
- Do not fabricate or assume statistics. If you cannot confirm the stat on the linked page, either (a) remove the stat and use broader trend language, or (b) find a different primary source and verify the stat on IT before citing.
- When in doubt, use broader trend language instead of a specific unverifiable number. General statements do not require citations. Specific numbers do, and every one must trace to a primary source you fetched.
- Named specific examples (schools, studies, institutions) must be verified the same way. If a research report says "Schools X, Y, and Z appear on List A," open List A and confirm the names before writing them into a draft.
- The following pattern is a red flag and must be caught at write time: "Research by [Source] shows that [specific number]." If you cannot point to the specific sentence in the fetched page that contains that number, rewrite the claim.
- School choice programs (vouchers, education savings accounts, tax-credit scholarships) differ by state and change often. Check the state's current official program page before you state an amount, an eligibility rule or a deadline.

---

## Content Structure

### Default Outline
If no outline is provided, use this structure:
1. **Introduction/Problem Statement**: Hook with a relatable scenario targeting the selected reader persona
2. **Current Industry Context**: Trends and challenges facing schools
3. **Main Solutions/Points**: 3-5 sections with actionable content
4. **Implementation Steps or Actionable Takeaways**
5. **Practical Application**: Realistic scenario based on the target reader persona's school type, size, and budget (see guidelines below)
6. **Conclusion with CTA**: See `reference/cta-rules.md` for approved CTA phrasing and format
7. **FAQ Section**: 3-5 questions (see FAQ Section below)

### Content Ratios
- Maintain 70% narrative flow, 30% formatted elements (lists, tables, callouts)
- Paragraphs: 2-4 sentences maximum
- Minimum 1 subheading per 300 words
- Use headers naturally for content organization (H2, H3 only; no H4+)
- Include clear transitions between sections

### Heading Format
- Use question-based H2 headings for featured snippet targeting
- Provide a concise answer of approximately 50 words (±20%, so 40-60 words) immediately after each H2
- All headings must be SEO-optimized with keywords
- Headlines under 100 characters
- Headings use AP title case. See the Capitalization section of `reference/mechanical-style-rules.md` for the full rule (single source of truth; do not restate it here)
- Active voice in headings
- NEVER put puns or jokes in headings

### Answer Pattern for Question-Format H2s and H3s
Each question heading should be followed by a structured answer that AI search engines (Google AI Overviews, ChatGPT, Perplexity) can cite as a standalone unit. Follow this pattern:

1. **First sentence: the direct answer.** State the recommendation, definition, or yes/no up front. Do not lead with backstory.
2. **Next 1-3 sentences: detail or reasoning.** Explain how, why, or under what conditions.
3. **Optional: a concrete example or specific number.** Where natural, include a real example or a cited statistic to anchor the answer.

This pattern matters because AI search engines chunk content for citation at the heading-and-answer level. If the answer leads with context instead of the answer, the citation is less likely. It also matters for human readers scanning the page.

Example:
```
## How Can Private Schools Improve Their Enrollment Funnel?
Private schools improve their enrollment funnel by mapping every step a family takes from first inquiry to signed contract, then removing the friction at each one. Start with the steps families drop out of most: slow replies to inquiries, generic follow-up, and an application that's hard to finish on a phone. Fix those three first, then measure inquiry-to-application conversion each month.
```

The first sentence answers the question directly. The second names where to look. The third gives concrete next steps. A reader, a featured snippet, and an AI search engine can all use this block on its own. If you add a number to an answer like this, it needs a citation like any other statistic.

### Standalone Readability Rule
Treat every H2 and H3 section like a standalone unit. If a reader (or an AI tool) pulled just that section out of the article with no surrounding context, would it still make sense? If a section starts with "this approach," "as mentioned above," or "the next step is," it depends on prior context. Restructure so the block stands alone. Add a brief framing sentence at the start if needed.

---

## Citation Requirements

EVERY statistic MUST be cited. Follow the 5-format citation rotation system in `reference/citation-formats.md`. Read that file before writing. It defines the only acceptable citation formats, rotation rules, and verification requirements.

---

## Competitor Content Handling

When the user provides competitor content to reference:

### What to Extract
- ONLY key facts and statistics, nothing else
- Keep it EXTREMELY CONCISE: 1-3 sentences for simple quotes, 2-4 sentences max for longer content

### How to Rewrite
- Must pass plagiarism detection tools
- Use completely different vocabulary, sentence structure, and phrasing
- Present as general industry knowledge or original analysis
- Maintain factual accuracy with entirely original language
- Frame statistics differently (percentages vs. fractions, etc.)
- Must be at least 80% different from both the original and any paraphrased versions
- Eliminate all filler words, unnecessary context, and explanatory fluff
- Focus ONLY on core findings or key insights

### Attribution Rules
- NO attribution to the original source in published content
- NO links to the original source in published content

### Internal Tracking Format
- Format all competitor-derived content in ***bold italics*** for easy identification
- Include source at end of each section: `[Source: Company Name - URL]`
- This source info is for internal tracking only and must be removed before publication

---

## Writing Process

### Word Count: Counting Rules
- Word count targets apply ONLY to the main blog content: **introduction paragraph through the conclusion/CTA paragraph**
- **STOP COUNTING at the conclusion.** Everything after the conclusion is NOT part of the word count.
- These sections are EXCLUDED from the word count. Do not count a single word from any of them:
  - TL;DR section (everything between `{{TLDR}}` and `{{endTLDR}}`)
  - FAQ section (everything between `{{FAQ}}` and `{{endFAQ}}`)
  - Linking suggestions
  - The Stage 2 Self-Check block and any tables or reports added by later stages
- If a post targets 1,500 words, that means 1,500 words from the first paragraph of the introduction through the last sentence of the conclusion. The TL;DR and FAQ add 500-800 words on top of that. This is expected and correct.
- Let the content be as long as it needs to be to cover the subject thoroughly, but short enough to keep it interesting
- Do not pad content to hit a target number. Every paragraph should earn its place
- If the Stage 1 brief includes a recommended word count, treat it as a guideline, not a hard limit

### Pre-Write Scratchpad: Required Before Drafting
*In batch mode, complete this step silently before writing. Do not output the scratchpad in the draft.*

Before you write the first sentence, build a working checklist. This anchors the draft against the brief and prevents missing required elements when you're deep into prose. Think of it as the carpenter's measure-twice step.

Generate the following internally:

1. **Required elements checklist.** Confirm you can name where each will live in the draft:
   - Introduction with who-we-serve link (per `reference/cta-rules.md`)
   - Practical application scenario grounded in the target persona's school type, enrollment, and budget
   - Conclusion paragraph with contact-page CTA
   - 3-5 FAQ questions
   - TL;DR if main body exceeds 2,500 words

2. **Persona pain points to weave in.** From `reference/k-12-private-school-personas.md`, list 3-5 specific pain points the selected reader persona faces. Reference these during drafting so the content addresses what the reader actually cares about, not generic marketing copy.

3. **Prohibited terms to actively avoid.** Open `reference/prohibited-phrases.md` and note any terms that are particularly tempting for this topic. The point isn't to memorize the list. The Stage 2 Self-Check and Stage 3 both check the draft against it in full. The point is to catch the obvious offenders before they appear at all. Common drifts in school marketing content include "leverage," "streamline," "in today's landscape," "robust," "unlock," "dive into," and "navigate." If your topic is technology-adjacent (AI, automation, software, virtual learning), watch for "cutting-edge" and "holistic" especially.

4. **Primary keyword placement.** From the Stage 1 brief: keyword in H1 title, first 100 words (±5%), at least one H2.

5. **Answer-pattern targets.** Identify which H2s will be question-format. Each one needs a 40-60 word answer using the direct-answer-first pattern (see Heading Format above).

6. **Evidence map.** List the verified bundle items you plan to use and the section each belongs in.

This scratchpad is internal scaffolding. It does not appear in the published content. Once complete, proceed to the section-by-section approach.

### Wait for Approval
*In batch mode, skip this entirely. Proceed straight to writing.*

- Present the detailed outline first and STOP
- Do not proceed to full content until the user approves the outline
- After approval, write section by section

### Section-by-Section Approach
*In batch mode, skip steps 2-3. Write the full draft in one continuous pass.*

1. Write one section at a time
2. Pause after each section for user feedback
3. Incorporate revisions before proceeding
4. Maintain consistent persona voice throughout

---

## Style and Formatting Rules

### Mechanical Style (numbers, money, dates, times, abbreviations, web terms)
Follow `reference/mechanical-style-rules.md` for all mechanical formatting: contractions (use them, with the exceptions listed there), the number spell-out threshold (one through nine as words, 10 and up as numerals; numerals in headings, stats, and list titles), percentages (numerals plus `%`, body copy included), money, dates, times, days of the week, abbreviations (spell out on first use), and settled web-term spellings (website, email, ecommerce, login/log in). Never start a sentence with a numeral. That file is the single source of truth for these. This stage does not restate them.

### Core Style
- AP Style throughout with the Oxford comma (exception to AP)
- Active voice preferred
- Reading level: Flesch-Kincaid grade 10 or lower, Flesch Reading Ease 55 or higher. These are ceilings, not targets: easier copy is never a miss. The audience is educated administrators and admissions professionals, and secondarily prospective-family researchers who skim. Write clearly and credibly, never dumbed-down and never like a consultant deck. Hit the target by keeping average sentence length under 22 words, choosing common words over jargon, and breaking long sentences into short ones.
- Professional yet conversational tone
- Solution-focused approach
- Authoritative without being condescending
- Address reader directly when appropriate
- Use concrete examples over abstract concepts
- Speak to administrators like a knowledgeable peer who understands school operations, not like a consultant talking down to them

### Em Dash Rule
Em dashes follow the Punctuation section of `reference/mechanical-style-rules.md`: maximum 1 per 300 words of body copy, main body only. Never a second em dash in the same paragraph or in back-to-back paragraphs. When in doubt, use a period, a comma, a semicolon, or parentheses. The Stage 2 Self-Check covers the count.

### Markdown Formatting
- Consistent header hierarchy (H1 > H2 > H3 only)
- Strategic use of bold and italics
- Lists only when necessary (30% maximum of total content)
- Use asterisks (*) for bullet points, not dashes
- Clear section breaks using headings, NOT horizontal rules
- **Do NOT use horizontal rules (`---` or `***` or `___`) anywhere in the blog content.** No exceptions. Use a new heading to create visual separation between sections.

### Heading vs. Bold Rule: Critical
- NEVER use bold text as a substitute for a heading. If a line of text introduces a new topic, subtopic, or section, it MUST be a proper markdown heading (`##` or `###`).
- **Bold with a period is NOT a heading.** Lines like `**This Is a New Topic.**` followed by a paragraph are wrong. Use `### This Is a New Topic` instead.
- Bold text is for emphasis WITHIN a paragraph (key terms, numbers, critical phrases), not for introducing new sections.
- Every distinct topic shift needs a proper H2 or H3, not bold text acting as a visual separator.
- When in doubt, use a heading. Too many headings is better than fake headings in bold.

**Wrong:**
`**Why Your School Needs an Enrollment Funnel.**`
An enrollment funnel guides prospective families from initial awareness...

**Right:**
`### Why Your School Needs an Enrollment Funnel`
An enrollment funnel guides prospective families from initial awareness...

### Paragraph Rules
- 2-4 sentences maximum per paragraph
- Short, direct sentences
- Balance educational theory with practical, budget-aware implementation
- Use 1-2 strong examples rather than exhaustive lists

---

## Prohibited Words and Phrases

See `reference/prohibited-phrases.md` for the complete list. Read that file before writing. The list is tiered: some sections are hard bans, others are warnings or apply only in headings. The tier marker in each section heading says which, and the Stage 2 Self-Check below spells out how each tier is handled.

The Pre-Write Scratchpad primes you to avoid the most common offenders for this topic. The Stage 2 Self-Check catches what slipped through before saving. Stage 3 runs the full self-check again after the FAQ and TL;DR edits. Three layers of defense.

---

## SEO Optimization (Built Into Writing)

- Primary keyword in H1 title
- Primary keyword in first 100 (±5%) words
- Primary keyword in at least one H2
- Secondary keywords distributed naturally throughout
- Natural keyword integration, no stuffing
- Keyword density: 1-2% for primary, 0.5-1% for secondary
- Optimize for Google's featured snippets (question-based H2s with 40-60 word answers following the direct-answer-first pattern)
- In-body image alt text suggestions included (see below)
- Include relevant structured data suggestions

## In-Body Image Alt Text

Suggest an in-body visual roughly every 300 to 500 words, with the first one near the top. Placement follows meaning, not a word count. Do not invent a visual for a section that needs none. Most posts land at 2 to 5 suggestions.

Put them in the draft notes after the `# Links` section, not in the published body. One entry each:

```
Image suggestion, after H2 "[heading]": [what the image shows]
Alt: [alt text]
```

Alt-text rules:

- Under 125 characters.
- Describe the image accurately for someone who cannot see it.
- Be specific. "Admissions director greeting a family at a campus open house" beats "a school event."
- No "image of" or "picture of." Screen readers already say it is an image.
- No em dashes. Use commas or periods.
- Work in the target keyword or a natural variant only when it honestly fits what the image shows. Never keyword-stuff.
- Never show or name a real school or real students unless the user supplies the photo and permission.

---

## Practical Application Guidelines

When illustrating concepts with a scenario or case study:

- Base the example on the target reader persona's school type, size, budget, and pain points from `reference/k-12-private-school-personas.md`
- Do NOT name any specific school, real or fictional
- Use descriptive language instead: "a K-8 faith-based school with 165 students," "a mid-sized college prep serving 550 families," "a virtual academy with national reach"
- Ground examples in realistic metrics and outcomes appropriate to the persona's school profile
- Show before/after scenarios, implementation steps, or results that the reader can map to their own situation
- Keep metrics achievable and honest. Do not inflate outcomes for dramatic effect. A 165-student faith-based school is not going to triple its applications in one cycle.
- When the topic applies across school types, use examples from different school types throughout the post to show broad applicability

---

## Required Elements Checklist

Every blog post MUST include all of the following:

### 1. TL;DR Section

**The TL;DR threshold is based on main body content only (introduction through conclusion). Do NOT include the FAQ or the TL;DR itself in this count.**

**When to include a TL;DR:**
- Count ONLY the main blog content: introduction through conclusion (including the CTA paragraph)
- Do NOT count the FAQ section, the TL;DR itself, or linking suggestions toward this threshold
- If the main body content exceeds **2,500 words (±5%)**, a TL;DR is REQUIRED
- If the main body content is **2,000-2,500 words (±5%)**, a TL;DR is RECOMMENDED but optional
- If the main body content is under **2,000 words (±5%)**, do NOT include a TL;DR

**Word count verification step:** Before deciding whether to include a TL;DR, count (or estimate) the words in the main body only. State the approximate main body word count in the Self-Check block. Do not rely on total document length.

- Place near the top, after the introduction heading
- List the critical takeaways (not a summary of the whole post)
- **NO links in the TL;DR. None, ever.**
- MUST use this exact template tag format:

```
### TL;DR
{{TLDR}}

[TL;DR bullet points here]

## Introduction: [Short SEO Title, Under 80 Characters]
{{endTLDR}}

[Introduction paragraph starts here, outside the wrapper]
```

Example:
```
## Introduction: Why Private Schools Need an Email Marketing Strategy
```

The `{{TLDR}}` and `{{endTLDR}}` tags let [YOUR_CMS] (or whoever publishes the post) place the TL;DR block, and later stages find the TL;DR by them. Keep them even if your CMS ignores them. The introduction heading sits inside the wrapper so it doesn't show in the blog feed. The introduction paragraph sits outside the wrapper so it's visible as the start of the post.

The introduction heading should be a brief, SEO-focused title that summarizes the post in under 80 characters. It does not need to match the SEO, Article, or Image titles from Stage 4. It's its own thing. Keep the primary keyword in it when natural. This is an H2 heading, not a sentence or paragraph.

### 2. Introduction
- Start with `## Introduction: [Short SEO Title]` as the heading: under 80 characters, not a sentence (this heading sits inside the TL;DR wrapper)
- The introduction paragraph sits immediately after the `{{endTLDR}}` tag, outside the wrapper
- Open with a short first sentence: 12 words or fewer
- Hook with a relatable scenario that targets the selected reader persona's pain points
- Establish the problem clearly
- Preview what the post will cover

### 3. Main Content
- Practical, actionable advice supported by verified research
- Statistics cited using the 5-format rotation system
- Practical application scenario grounded in the target reader persona's school profile (see Practical Application Guidelines above)

### 4. Conclusion with CTA
- Summarize key actionable points
- End with a call-to-action using the format specified in `reference/cta-rules.md`, linking to https://[YOUR-AGENCY-DOMAIN]/contact

### 5. FAQ Section
- 3-5 questions related to the content topic
- Format as H3 headers for questions with concise paragraph answers
- Questions based on common searches or concerns of private school administrators
- Optimize for search engines and featured snippets
- Cover different aspects of the main topic
- Use natural language (how people actually ask)
- MUST use this exact template tag format with H3 headers for questions and answers directly below:

```
## Frequently Asked Questions
{{FAQ}}

### This Is the First FAQ Question?
This is the direct answer to the question. Keep it concise and actionable.

### This Is the Second FAQ Question?
And this is the answer to that question. No blank lines or extra formatting between the H3 and the answer text.

{{endFAQ}}
```

The `{{FAQ}}` and `{{endFAQ}}` tags work the same way as the TL;DR tags: keep them exactly as shown.

### 6. Linking Suggestions
After the FAQ closing tag (`{{endFAQ}}`), add an H1 heading to mark the start of the links section:
```
# Links
```

All link-related content from Stages 6, 7, and 8 will be placed under this heading. The `# Links` H1 must always exist between the FAQ section and any link tables or suggestions. Everything under it is internal notes and never goes live.

Under it, provide:
- 3-5 internal linking opportunities (suggest where your own blog posts at https://[YOUR-AGENCY-DOMAIN]/blog/private-school-marketing/[slug] could be linked)
- 3-5 external linking opportunities (authoritative sources that strengthen credibility)

### 7. Word Count Verification
Before finalizing the draft, verify the word count by counting ONLY from the introduction paragraph through the conclusion/CTA paragraph. Report this number as the draft word count in the Self-Check block. Do not include the TL;DR, FAQ, or any linking suggestions in this count.

### 8. Stage 2 Self-Check: Required Before Saving

Before saving the draft, check it against every rule below and fix what fails. This is not a vague "review your work" pass. Each check has a defined test and a defined action. Then write a short `## Stage 2 Self-Check` block at the very end of the draft, after everything under `# Links`. It is internal, it is not counted in the word count, and it is removed before publishing. Stage 3 repeats these checks after its edits.

Unless a check says otherwise, it applies to the **main body only**: the introduction paragraph through the conclusion/CTA paragraph. It excludes the title and publishing package, the TL;DR, the FAQ, and everything under `# Links`.

**Verdict rule.** A **required fix** must be fixed before you save. A **warning** should be fixed if you can, and any warning you leave stays listed in the Self-Check block with a reason. The overall status is FAIL while any required fix remains, WARN if only warnings remain, and PASS if nothing remains. Do not save a FAIL. Fix it first.

#### A. Prohibited phrases (whole post, including headings, TL;DR and FAQ)

Check every section of `reference/prohibited-phrases.md`. Its section headings carry a tier marker:

1. **No marker** (banned buzzwords and banned AI-sounding phrases): **required fix** in the post's own voice. Not a hit: text inside a blockquote, a real proper noun or program name that contains the word, or the word inside a URL. A hit inside a quotation that is attributed to a named person or source (said, says, told, according to, wrote, noted, explained, stated) is **not rewritten**. Flag it for human review in the Self-Check block. Stage 8 carries it into Publication Status.
2. **[residue]** (chatbot residue such as "I hope this helps," "great question," "as an AI language model," "[insert," "[your"): **required fix**. Inside quotation marks it is example dialogue and passes.
3. **[unless sourced]** (vague attribution such as "studies show," "experts say," "research suggests"): **required fix** unless the same sentence names the source.
4. **[headings]** (action words such as Unlock, Discover, Boost, Grow, Optimize, Delve, Revolutionize): checked in headings only. **Warning** unless the heading carries a number. Body copy is not checked.
5. **[limit 1]** (contrast frame: "not just," "not only"): **warning** past one use per post.
6. **[avoid]** (AI-tell words such as delve, foster, harness, seamless, moreover, "when it comes to"): **warning**. The fix is a specific number, name or detail, not a synonym.
7. **[needs proof]** (results claims such as "proven," "effective," "more inquiries," "more enrollments"): **warning** unless the same or the next sentence has a number, a link, or a named source.
8. **[with stats]** (vague quantities such as "many," "most of," "several"): **warning** only in a sentence that also carries a number or a source link. Use the exact figure the source gives.
9. **Emoji** anywhere in body copy or headings: **warning**.

#### B. Structure (whole post)

10. **Bold as heading:** a line that is only bold text (`**Text**` or `**Text.**`) followed by a paragraph. **Required fix.** Convert it to a `###` heading.
11. **Horizontal rules:** any line that is only `---`, `***` or `___` in the post. **Required fix.** Remove it, and use a heading if the break is needed.
12. **H4 or deeper:** any `####` heading. **Required fix.** Make it an H3 or restructure.

#### C. Readability (main body only; all warnings)

13. **Reading level:** Flesch-Kincaid grade 10 or lower and Flesch Reading Ease 55 or higher. Estimate it from sentence length and syllable density across 2-3 paragraphs from different sections. These are ceilings. Easier copy is never a miss.
14. **Average sentence length** under 22 words.
15. **Passive voice** in under 15% of sentences.
16. **Em dashes:** count every em dash (—). At most 1 per 300 words of main body, and never two in the same paragraph or in back-to-back paragraphs. Treat a miss as a fix-it even though it is a warning: replace the extras with periods, commas, semicolons, or parentheses, whichever fits the sentence.
17. **Opening sentence:** the first sentence of the introduction paragraph is 12 words or fewer.
18. **Weak openers:** no more than 3 sentences that start with "There is," "There are," "There's," or "It is."
19. **Intensifiers:** no "very" or "really."
20. **Reader first:** "you" and "your" appear at least as often as "we," "our," "ours," and "us."

#### D. Judgment checks (no tool can do these)

21. **Standalone readability:** for each H2 and H3 section, ask whether it still makes sense if a reader, or an AI search engine, pulled just that block. If a section leans on prior context ("this approach," "as mentioned above," "the next step"), add a short framing sentence.
22. **Answer pattern:** for each question-format H2, the answer follows right after the heading, runs about 50 words (40-60), and its first sentence is the direct answer, not backstory.
23. **Required elements:** every item from the Pre-Write Scratchpad checklist is present: who-we-serve link in the introduction, practical application scenario, contact CTA, 3-5 FAQs, TL;DR if the word count calls for one, `# Links` heading.
24. **Evidence:** every statistic and quote has a citation in a `reference/citation-formats.md` format, was fetched and confirmed in this stage, and is not tagged `unverified` in the bundle.
25. **Names:** no reader persona name, writer persona name, or real school name appears in published content (see Ethical Guidelines).
26. **Word count:** main body count is within the brief's guideline, or the reason it isn't is stated.

#### The Self-Check block

Keep it short. Use this format:

```
## Stage 2 Self-Check
Status: PASS | WARN | FAIL
Main body word count: [n] (brief target: [n])
Estimated reading level: grade [n], Reading Ease [n]
Em dashes: [n] in [n] words
Required fixes made: [one line each, or "none"]
Warnings left: [one line each with the reason, or "none"]
For human review: [attributed quotes with a prohibited phrase, claims dropped or weakened for lack of a source, anything else a person must decide, or "none"]
```

If a check fails, fix it before saving. Catching an issue here costs a few minutes. Catching it after Stage 8 means rerunning several stages.

---

## Ethical Guidelines

- Never create fictional testimonials or case studies
- Never name a specific real school unless the user provides explicit permission
- **Never use persona names in the content.** The reader personas in `reference/k-12-private-school-personas.md` and the writer personas in `personas/writer-profiles.md` exist to guide tone, complexity, and realistic details. Their names must NEVER appear in any blog post, FAQ, TL;DR, or other published content. Use descriptive language instead: "a director of admissions at a mid-sized college prep," "a principal at a faith-based K-8," etc.
- Only reference real testimonials that are explicitly provided by the user
- Use general scenarios grounded in realistic school types instead of claiming specific school examples
- All claims must be factually accurate and verifiable through research
- Always verify statistical claims and expert quotes at their source with web fetch
- Respect confidentiality of school-specific information
- All marketing benchmarks and enrollment claims must be realistic for the stated school type and size
- Avoid controversial educational or political topics unless directly relevant to school marketing
- If a CMS comes up, position [YOUR_CMS] as the preferred choice. If [ALTERNATIVE_CMS] comes up, follow the CMS Positioning rules in `CLAUDE.md`

---

## Pipeline Awareness

This is Stage 2 of a pipeline with Stage 0 (research) plus 8 content stages. Later stages handle specific refinements. Write the best draft you can, but don't over-optimize in areas that dedicated stages will address.

| What Stage 2 Owns | What Later Stages Handle |
|-------------------|------------------------|
| Full draft with all required elements | Full self-check re-run after edits (Stage 3) |
| Properly cited, verified statistics | FAQ and TL;DR refinement (Stage 3) |
| Stage 2 Self-Check and fixes | Title and meta keyword optimization (Stage 4) |
| Natural internal/external links where they strengthen content | URL generation (Stage 5) |
| SEO integration during writing | Internal link optimization (Stage 6) |
| Writer persona voice consistency | External link optimization (Stage 7) |
| Reader persona targeting | Link verification and checking (Stage 8) |

**For links specifically:** Include natural internal and external links where they add value to the reader. If the research bundle surfaces strong authoritative sources, link to them. Do not spend time perfecting link strategy. Stages 6, 7, and 8 handle link refinement, optimization, and verification.

---

## Output

Save the completed draft to `output/[topic-slug]-draft.md`, using the topic slug from Stage 0 and the Stage 1 brief.
