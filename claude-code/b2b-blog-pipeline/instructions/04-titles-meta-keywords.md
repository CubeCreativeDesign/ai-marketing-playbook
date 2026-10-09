# Stage 4: Titles, Meta Description, and Keywords

## Purpose
Generate optimized title options across three tiers, a meta description, and a keyword list for the blog post. Read the full draft from Stage 2/3 before generating anything.

**Output feeds:** Stage 5 auto-accepts the Recommended Titles and meta description and builds the slug and Publishing Package from them.

**Human check:** None inside the pipeline: this stage runs unattended under `claude -p`. Drafts stay in `output/`, with no Drive upload, and an editor reads the finished draft there before it publishes. If a title could not meet its character limit or its number does not match the body count, say so first in the Analysis Summary.

---

## Pre-Generation Analysis

Before creating any deliverables, analyze the draft for:
1. Main topic and subject matter
2. Target audience based on tone, language, and content
3. Writing style and persona voice used
4. Key themes and concepts
5. Primary value proposition for readers
6. **Count any discrete items, tips, steps, ways, methods, or strategies in the content** — this number must be exact if used in any title

---

## Title Generation

### Three-Tier Title System
Every blog post needs three related titles that build on each other:

| Tier | Purpose | Character Limit |
|------|---------|----------------|
| **SEO/Google Title** | Optimized for SERPs | 55 characters max |
| **Article Title** | Display on the actual page | 55-100 characters max |
| **Image Title** | Image SEO and accessibility | 80-150 characters max |

### Title Relationship Rules
Each set of three must maintain the same core concept but be meaningfully different from each other:
1. **SEO title** = concise, keyword-front, optimized for search. This is what shows in Google results.
2. **Article title** = a DIFFERENT title that expands the concept for humans reading the page. Do NOT just add "Your" to the SEO title and call it done. The article title should reframe, add context, or take a different angle on the same topic. It must be clearly distinguishable from the SEO title at a glance.
3. **Image title** = builds on the article title by adding audience specificity, industry details, or situational context for image SEO.

**The SEO title and Article title must NOT be the same title with minor word swaps.** They should feel like two different ways to describe the same post. If someone read both titles side by side, the difference should be obvious.

**Example of proper relationship:**
- SEO: Local SEO Tips for [YOUR_VERTICAL] Companies (42)
- Article: How to Get Your [YOUR_VERTICAL] Company to Show Up in Google's Map Pack (63)
- Image: How to Get Your [YOUR_VERTICAL] Company to Show Up in Google's Map Pack for Local Homeowner Searches (96)

**Example of what NOT to do:**
- SEO: Local SEO Tips for [YOUR_VERTICAL] Companies (42)
- Article: Local SEO Tips to Help Your [YOUR_VERTICAL] Company Get Found (55) ← TOO SIMILAR, just added "to Help Your" and "Get Found"
- These are essentially the same title with filler words added

### Generate 5 Sets
Produce 5 complete sets (SEO + Article + Image) using a mix of these title styles:
1. **Question format**: "How Can [YOUR_VERTICAL] Companies Rank Higher in Local Search?"
2. **Number/List format**: "5 Google Ads Mistakes [YOUR_VERTICAL] Companies Keep Making"
3. **How-to format**: "How to Build a Lead Generation System That Fills Your Route Board"
4. **Statement format**: "The Google Business Profile Mistakes Costing You Calls"
5. **Benefit-driven**: "Turn More Website Visitors into Booked Service Calls"
6. **Curiosity/hook**: "Why Your [YOUR_VERTICAL] Website Isn't Converting (And How to Fix It)"
7. **Data-driven**: "Companies Using These 3 Email Sequences See 28% More Recurring Revenue"

### Best Title Recommendation
After generating all 5 sets, present a consolidated "Recommended Titles" section with the best pick from each tier. Format each recommended title as a heading at its corresponding level:
- SEO/Google Title → H1 (`#`)
- Article Title → H2 (`##`)
- Image Title → H3 (`###`)

Below each heading, add a short line identifying the tier and explaining the recommendation. This format makes each title copy-paste ready without needing to strip out labels or formatting.

Write out the full title text with character count — do not just reference a number from the list. Include a brief explanation of why it was chosen. Consider:
- Click appeal (would a [YOUR_VERTICAL] business owner actually click this?)
- Search intent match
- Primary keyword placement (near the beginning)
- Emotional resonance
- Specificity to [YOUR_VERTICAL] (avoid generic titles that could apply to any industry)

### Title Rules
- Primary keyword near the beginning of SEO titles
- No clickbait — deliver on the promise
- Match search intent (informational, how-to, comparison)
- Active voice only — mandatory
- Use AP title case for all titles, exactly as defined in the Capitalization section of `reference/mechanical-style-rules.md` (single source of truth — it covers that short verbs, pronouns, and subordinating conjunctions stay capitalized, and that articles, coordinating conjunctions, and short prepositions go lowercase mid-title)
- Do NOT capitalize power words just because they are power words — AP title case governs, not emphasis
- Never put quotation marks around titles in the output

### Numerical Accuracy — CRITICAL
Before suggesting any title with a number:
1. Count the EXACT number of distinct items in the content
2. Only use the precise number that appears in the content
3. If the content has 5 strategies, NEVER suggest "7 Strategies" or "10 Strategies"
4. If the content has multiple points but no clear count, avoid the number format entirely
5. State the exact count found in the Analysis Summary

### Headline Techniques
Apply these when crafting titles:
- **Clarity & Specificity**: Include specific benefits/outcomes ("Get 30% More Calls" not "Get More Leads")
- **Curiosity Gap**: Hint at value without revealing everything
- **Value Communication**: Answer "What's in it for me?" for the reader
- **Power Words**: Use emotional triggers like "proven," "essential," "critical," "mistakes"
- **Numbers & Data**: Include specific numbers when relevant and accurate
- **Conciseness**: Remove unnecessary words while maintaining clarity
- **Rhetorical Devices**: Use alliteration or rhythm when it enhances memorability

---

## Meta Description

### Specifications
- Length: **115-125 characters EXACTLY** — no exceptions
- Include primary keyword naturally
- Focus on reader benefits and solutions
- Create urgency or curiosity without hyperbole
- Active voice exclusively
- No em dashes in meta descriptions — replace with semicolons, periods, or parentheses. Intentional override: meta gets zero, stricter than the 1-per-200 body-copy rule in mechanical-style-rules.md.
- AP style with Oxford comma
- Address reader directly when appropriate ("you" and "your")
- Professional yet conversational tone
- Do not use prohibited phrases (see below)
- Never put quotation marks around meta descriptions in the output

### Generate 1 Meta Description
Provide a single meta description with character count. Make it the strongest option — do not present alternatives.

### Template Structure
`[Key benefit/hook]. [What they'll learn]. [Why from us/CTA].`

### Meta Description Rules
- Never create fictional testimonials or case studies
- All claims must be factually accurate and match the draft content
- Use concrete language over abstract concepts
- No numerical claims that don't match the content exactly
- Solution-focused approach highlighting practical benefits

---

## Keywords

### Process
1. Review the primary keyword from the Stage 1 brief
2. Confirm it still fits the final content — if the draft shifted focus, flag this and suggest an updated primary keyword
3. Research and identify the 10 most relevant keywords for the post based on the actual content written

### Output Format
Top 10 keywords ranked by relevance to the content. No categories, no breakdown — just the best 10:

```
### Keywords
* keyword one,
* keyword two,
* keyword three,
* keyword four,
* keyword five,
* keyword six,
* keyword seven,
* keyword eight,
* keyword nine,
* keyword ten
```

Include a mix of:
- The primary keyword
- Short-tail and long-tail variations
- Question-based phrases (for featured snippet potential)
- Terms that appear naturally in the content

All lowercase, comma at end of each line.

---

## Prohibited Phrases
See `reference/prohibited-phrases.md` for the complete list. These words and phrases must never appear in titles, meta descriptions, or any output from this stage.

---

## Character Counting Rules
For ALL character counts in titles and meta descriptions:
1. Count every character including spaces and punctuation
2. Each space = 1 character
3. Each punctuation mark = 1 character
4. Count twice internally before displaying
5. Display only the final number in parentheses after each title/description

---

## Quality Checks Before Finalizing

Run these checks on every title and meta description before presenting:

- [ ] Accurate character count (counted twice)
- [ ] Active voice (mandatory)
- [ ] No prohibited phrases
- [ ] No quotation marks around titles or descriptions
- [ ] Numerical accuracy matches content exactly
- [ ] Title relationship check (article builds on SEO, image builds on article)
- [ ] Title differentiation check (article title is clearly different from SEO title — not just minor word additions)
- [ ] Primary keyword placement (near beginning for SEO titles)
- [ ] No clickbait — title delivers on its promise
- [ ] Proper title case capitalization
- [ ] Meta description: 115-125 characters exactly
- [ ] Meta description: no em dashes
- [ ] Meta description: AP style with Oxford comma
- [ ] All claims factually match the draft content

---

## Output Format

```markdown
## Analysis Summary
- Target audience identified
- Readability level chosen
- Primary emotional triggers used
- If numerical titles used, exact count found in content
- Relationship between three title tiers

### SEO/Google Titles (55 characters max)
1. Title Text Here (XX)
2. Title Text Here (XX)
3. Title Text Here (XX)
4. Title Text Here (XX)
5. Title Text Here (XX)

### Article Titles (55-100 characters max)
1. Title Text Here (XX)
2. Title Text Here (XX)
3. Title Text Here (XX)
4. Title Text Here (XX)
5. Title Text Here (XX)

### Image Titles (80-150 characters max)
1. Title Text Here (XXX)
2. Title Text Here (XXX)
3. Title Text Here (XXX)
4. Title Text Here (XXX)
5. Title Text Here (XXX)

## Recommended Titles

# Title Text Here (XX)
SEO/Google Title — [brief reason why]

## Title Text Here (XX)
Article Title — [brief reason why]

### Title Text Here (XXX)
Image Title — [brief reason why]


### Meta Description (115-125 characters)
Meta description text here (XXX)

### Keywords
* keyword one,
* keyword two,
* keyword three,
* keyword four,
* keyword five,
* keyword six,
* keyword seven,
* keyword eight,
* keyword nine,
* keyword ten
```

## End
---

## Pipeline Awareness
This is Stage 4 of the pipeline. Stage 1 established the primary keyword and audience. Stages 2-3 produced the draft with FAQ and TL;DR. Your job is to create the title/meta/keyword package based on the finished draft content. Later stages handle URL generation (Stage 5), internal links (Stage 6), external links (Stage 7), and link checking (Stage 8).

## Output

Open `output/[topic-slug]-draft.md` and insert the complete title package at the TOP of the file, above all existing content. Use the output format above. Do not create a separate file.
