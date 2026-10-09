# Stage 3: Draft Self-Check, FAQ, and TL;DR Review

## Purpose
Stage 3 is the quality control checkpoint for the draft produced by Stage 2. It runs in two phases:

1. **Draft Self-Check.** Read the draft against the written checklist below: prohibited phrases, readability, and structure. Fix every required item, then write a short `## Stage 3 Self-Check` block into the draft. Also do the two judgment checks (standalone sections, H2 answer pattern).
2. **FAQ and TL;DR Review.** Review the FAQ and TL;DR sections for accuracy, completeness, consistency, and voice. This is a refinement pass, not a rebuild.

Run Phase 1 end to end before you start Phase 2. Cowork has no QC script, so you apply every check by reading. The Self-Check block is the evidence that the checks happened. Count what you can count. Label anything you estimate as an estimate.

**Output feeds:** Stage 4 reads this draft to write the titles, meta description and keywords, and counts its list items for any number in a title, so the body, TL;DR and FAQ must be final here. The TL;DR and FAQ ship as written inside their template tags. Stage 8 reads your Self-Check block and carries its flagged items into `# Publication Status`.

**Human check:** You, in the Cowork chat (or the person who runs the project), read the finished draft before it publishes. The items that person must see are the attributed quotes Step 4 flags for review. List them first under "Needs human review" in the Self-Check block, so Stage 8 can carry them into `# Publication Status`.

---

## What Stage 3 Does NOT Do
- Does not rewrite the main blog content beyond fixing prohibited phrases, structure violations, and readability problems
- Does not change the structural format established by Stage 2 (TL;DR wrapper, FAQ wrapper, `# Links` heading)
- Does not generate the FAQ or TL;DR from scratch
- Does not add links to the TL;DR section (no links in the TL;DR, ever)
- Does not handle internal or external link verification. Stages 6, 7, and 8 do that.

---

# Phase 1: Draft Self-Check

## What to Measure, and What to Skip
Measure readability on the **main body only**: from the introduction paragraph through the conclusion. Leave these out of the readability numbers:
- The TL;DR block (everything between `{{TLDR}}` and `{{endTLDR}}`)
- The FAQ block (everything between `{{FAQ}}` and `{{endFAQ}}`)
- Everything from the `# Links` heading to the end of the file
- Any title package or Publishing Package above `{{TLDR}}` (later stages add these)

Scan prohibited phrases and structure across everything above `# Links`, including the TL;DR and FAQ. Everything under `# Links` is internal notes and never goes live, so it is not scanned.

## Step 1: Prohibited-Phrase Scan
Read `reference/prohibited-phrases.md`. Check the draft for every listed term, in its common word forms (for example "leverage," "leverages," "leveraging").

Each section of that file can carry a tier marker in its heading. The marker sets how a hit is treated:

| Marker in the section heading | How to treat a hit in your own writing |
|---|---|
| (no marker) | **Required fix.** Rewrite the sentence. |
| `[residue]` | **Required fix.** Chatbot residue ("I hope this helps," "Great question") never ships. The one exception: inside quotation marks as example dialogue. |
| `[unless sourced]` | **Required fix,** unless the same sentence names its source. "Studies show" with no named study must go. |
| `[needs proof]` | **Warning,** unless the same sentence or the next one carries a number, a link, or a named source. |
| `[headings]` | Checked in headings only. **Warning,** unless the heading carries a number. Body copy is ignored. |
| `[with stats]` | **Warning,** only in a sentence that carries a number or a link (a year alone doesn't count). Use the exact figure instead of the vague word. |
| `[limit N]` | Fine for the first N uses in the draft. **Warning** for each use after that. |
| `[avoid]` | **Warning.** Use the word only if nothing plainer works. |

Also flag every **emoji** in the copy above `# Links` as a warning.

Some hits are not your writing, so you must not reword them. Leave these as they are:
- **Blockquotes:** the line starts with `>`. Keep verbatim.
- **Attributed quotes:** the term sits inside quotation marks with attribution nearby ("said," "says," "told," "according to," "noted," "wrote," "explained," "stated," "in an interview," and similar). Keep verbatim, and flag the quote for human review (Step 4).
- **Proper nouns:** the match is an acronym or part of a real program or product name. Do not reword.
- **Inside a URL:** the match is part of a link target. Rewording would break the link.
- **A cited post or report title:** rewording would misquote it.

## Step 2: Readability Check
Check the main body against these targets. A miss is a **warning**, never a fail. Readability alone never blocks a draft, but fix what you can.

| Check | Target | How to check in Cowork |
|---|---|---|
| Flesch-Kincaid grade | 10 or lower | Estimate. Long sentences and many three-syllable words push it up. |
| Flesch Reading Ease | 55 or higher | Estimate. Easier is never a miss. |
| Average sentence length | Under 22 words | Count a sample of sentences across sections. |
| Passive voice | Under 15% of sentences | Count "was/were/is/are/been/being + past participle" sentences. |
| Em dashes | No more than 1 per 300 words | Count every em dash (—) in the body. |
| Intro first sentence | 12 words or fewer | Count the first sentence under `## Introduction:`. |
| Weak openers | 3 or fewer | Count sentences that start "There is," "There are," "There's," or "It is." |
| Intensifiers | Zero | Count "very" and "really." |
| Reader first | "we/our/us" count no higher than "you/your" count | Count both. |

Grade 10 and Reading Ease 55 are ceilings for this audience. School administrators are educated readers, so plain grade 8 to 10 prose fits. Prose that reads easier than the target is fine.

## Step 3: Structure Check
These are **required fixes**:
- **Bold-as-heading:** a line that is only bold text (`**Text.**` or `**Text**`) with a paragraph under it. Replace it with a real H3 (`### Text`).
- **Horizontal rules in the body:** a line that is only `---`, `***`, or `___`. Remove it. If it was a section divider, use a heading instead. [YOUR_AGENCY] uses heading hierarchy, not horizontal rules, for visual separation.
- **H4 or deeper headings:** `####` or more. Promote to H3, or fold the content into the H2/H3 structure. Posts use H1 to H3 only.

## Step 4: Fix Required Items
For every own-voice hit that is a required fix:
- Find the term in context.
- Rewrite the sentence with a natural alternative. Do not just delete the word. Restructure so the new wording reads as if it were always there.
- Test the rewrite against the grade 10 ceiling and the persona voice.

Common replacements:
- "leverage" → use, apply, draw on, take advantage of
- "streamline" → simplify, tighten, speed up, clean up
- "dive into" → look at, cover, get into, walk through
- "in today's [landscape/world/market]" → today, currently, right now (or delete it and start the sentence directly)
- "robust" → strong, solid, well-built, thorough
- "unlock" → reach, find, get to
- "delve" → look at, explore, examine
- "navigate" → handle, work through, get through
- "holistic" → complete, full-picture, end-to-end
- "cutting-edge" → current, modern, recent (or name the specific feature)
- "utilize" → use
- "foster" → build, grow, encourage
- "harness" → use, put to work

These are starting points. Pick the word that fits the sentence, not the closest synonym.

For blockquote and attributed-quote hits:
- Leave the quote text as it is. Verbatim quotes stay verbatim, even when they contain banned terms. "Fixing" a term inside a quote misrepresents the source.
- For an attributed quote, add it to "Needs human review" in the Self-Check block. The reviewer may swap the source or paraphrase instead of quoting. That decision is not yours to make at this stage.

Apply every structure fix from Step 3.

## Step 5: Address Warnings
Warnings do not block the draft, but fix them where you can do it cleanly:
- **Grade too high or Reading Ease too low:** Break long sentences. Swap long jargon for common words. Rewrite the densest paragraphs first.
- **Em dashes over 1 per 300 words:** Replace the extras with periods, semicolons, commas, or parentheses. Pick the punctuation that fits the sentence. Never put a second em dash in the same paragraph or in back-to-back paragraphs. Always fix this one, even though it is only a warning.
- **Average sentence length 22 or more:** Split the longest sentences into two or three. Active voice helps.
- **Passive voice 15% or more:** Flip sentences to active voice ("the admissions team launched the campaign," not "the campaign was launched by the admissions team").
- **Intro first sentence over 12 words:** Cut it to 12 or fewer. Lead with the point.
- **Weak openers, intensifiers, "we" over "you":** Rewrite the sentence around a real subject, cut "very" and "really," and turn "we" sentences toward the reader.
- **Tier warnings** (`[needs proof]`, `[with stats]`, `[limit N]`, `[avoid]`, `[headings]`, emoji): add the proof or exact figure, or reword.

## Step 6: Judgment Checks No Scan Can Do

### 6a. Standalone Section Check
For each H2 and H3 section in the main body, ask: if a reader pulled this section out of context, or an AI search engine cited only this block, would it still make sense?

Watch for sections that start with:
- "This approach..."
- "As mentioned above..."
- "The next step is..."
- "Building on that..."
- "However, this only works if..."

These depend on earlier context. Fix them with a short framing sentence at the start that names the topic, so the block stands alone. This matters for human skimmers and for AI search engines that cite content at the heading-and-answer level.

### 6b. H2 Question and Answer Pattern Check
For each question-format H2, confirm all four:
1. The answer follows the heading right away. No image, list, or other content sits between them.
2. The answer is about 50 words (40 to 60).
3. The first sentence answers the question directly: a definition, a recommendation, or a yes/no. Not backstory.
4. The next sentences give detail, reasoning, or an example.

If a section opens with context before the answer, restructure so the answer leads. Tighten or expand the answer to fit 40 to 60 words.

## Step 7: Write the Self-Check Block
Put the block directly under the `# Links` heading, as the first thing there. Stage 2 created `# Links` after `{{endFAQ}}`. If it is missing, create it. Because the block sits under `# Links`, it never goes live and never counts in the body measurements.

Delete the `## Stage 2 Self-Check` block that Stage 2 left at the end of the draft, and any Stage 3 block from an earlier pass. Never keep two Self-Check blocks.

Use this format:

```
## Stage 3 Self-Check

**Overall:** PASS / WARN / FAIL

### Needs human review
- [Each attributed quote that contains a prohibited term, with its line or section. Write "None" if there are none.]

### Prohibited phrases
- Required fixes found and fixed: [number]
- Required fixes still open: [number, should be 0]
- Kept verbatim (blockquote, attributed quote, proper noun, URL, cited title): [number]
- Warnings left as is: [number, with a short reason each]

### Readability (main body only)
- Word count: [number]
- Em dashes: [number] ([ratio] per 300 words, limit 1)
- Intro first sentence: [number] words (limit 12)
- Weak openers: [number] (limit 3)
- Intensifiers ("very," "really"): [number] (limit 0)
- we/our/us vs. you/your: [number] vs. [number]
- Flesch-Kincaid grade (estimate): [number] (ceiling 10)
- Flesch Reading Ease (estimate): [number] (floor 55)
- Average sentence length (estimate): [number] words (under 22)
- Passive voice (estimate): [percent] (under 15%)

### Structure
- Bold-as-heading: [number]
- Horizontal rules in body: [number]
- H4 or deeper: [number]

### Judgment checks
- Standalone sections: [done, with any sections you reframed]
- H2 answer pattern: [done, with any answers you restructured]
```

How to set **Overall**:
- **FAIL:** any required prohibited-phrase fix or any structure violation is still open. Fix it and redo the block. Do not move on with a FAIL.
- **WARN:** no required fixes are open, but one or more readability targets or tier warnings are still missed.
- **PASS:** nothing is open and every target is met.

Once the block shows PASS or WARN with no required fixes open, Phase 1 is complete. Go to Phase 2.

---

# Phase 2: FAQ and TL;DR Review

This phase refines the FAQ and TL;DR sections. Phase 1 already cleaned up prohibited phrases and structure across the whole draft, including the FAQ and TL;DR. Phase 2 focuses on the content quality of those two sections.

## TL;DR Review

### Review Criteria
Read the full blog post, then evaluate the existing TL;DR against these standards:

1. **Accuracy:** Does every bullet correctly represent what the main content says? Fix anything that overstates, understates, or misrepresents a point.
2. **Completeness:** Are all major takeaways captured? If the post has a key insight a busy school administrator needs, it must be in the TL;DR.
3. **Consistency:** Do the statistics and claims in the TL;DR match the main content exactly? No rounding, no paraphrasing numbers differently.
4. **Conciseness:** Each bullet should be 1 to 2 sentences. Cut anything another bullet already covers.
5. **Value:** Would a school administrator who ONLY reads the TL;DR walk away with the right takeaways? If not, fix it.
6. **Voice:** Does it match the writer persona used in the post?
7. **Introduction heading:** Does the `## Introduction:` heading hold a short, SEO-focused title (under 80 characters) with the primary keyword? Is it inside the wrapper (before `{{endTLDR}}`), with the intro paragraph outside?

### TL;DR Rules
- 3 to 5 bullet points maximum
- Each bullet: 1 to 2 sentences
- Include the most compelling statistic from the post
- End with the action item or CTA
- **No links in the TL;DR. None, ever.**
- Bold key numbers and critical terms within bullets

### TL;DR Template Tag Format
The TL;DR section MUST be wrapped in CMS template tags exactly as shown. The introduction heading sits inside the wrapper, which keeps both the TL;DR and the intro heading out of the blog feed.

```
### TL;DR
{{TLDR}}

[TL;DR bullet points here]

## Introduction: [Short SEO Title, Under 80 Characters]
{{endTLDR}}

[Introduction paragraph starts here, outside the wrapper]
```

Do NOT change this format. [YOUR_CMS] needs the `{{TLDR}}` and `{{endTLDR}}` tags to place the block. The introduction heading sits inside the wrapper. The introduction paragraph sits outside.

### Improvement Actions
- Replace weak bullets with stronger takeaways from the main content
- Tighten language and remove filler and vague phrasing
- Put the most important point first
- Check that every number matches its citation in the main content

---

## FAQ Review

### Review Criteria
Read the full blog post, then evaluate each FAQ question and answer:

1. **Relevance:** Are these the questions a school administrator would actually ask after reading this post? Replace weak questions with stronger ones based on:
   - What would someone Google after reading this?
   - What objections might make a school administrator hesitate?
   - How do they carry this out with their team and budget?
   - What is the investment, and what return can they expect?
   - How does this compare to what other schools are doing?

2. **Accuracy:** Does every answer reflect the main content? No contradictions, no invented claims, no statistics that don't appear in the post.

3. **Completeness:** Does each answer fully address the question? A school administrator who reads only the FAQ should get a useful, actionable answer.

4. **Consistency:** Do the answers match the tone, data, and recommendations in the main post? If the post recommends X but the FAQ implies Y, fix it.

5. **Voice:** Do the answers match the writer persona? If the post uses an approachable, analogy-driven voice, the FAQ shouldn't suddenly sound clinical.

6. **Scannability:** Can a busy reader find the key information in each answer quickly? Answers should use:
   - Bold emphasis on key numbers, benchmarks, and critical takeaways
   - Short paragraphs (2 to 4 sentences max)
   - Bullet points or numbered lists where they help
   - A clear opening statement that answers the question directly

### FAQ Rules
- 3 to 5 questions (keep what Stage 2 produced unless a question is clearly weak)
- Questions phrased the way a school administrator would actually ask them
- Question headings (H3) use AP title case, like every other heading. See the Capitalization section of `reference/mechanical-style-rules.md` (the single source of truth).
- Answers: 2 to 4 sentences for simple questions, structured with bullets for complex ones
- At least one question should naturally link to a [YOUR_AGENCY] service page or another blog topic
- Format for FAQ schema markup compatibility (JSON-LD)

### FAQ Template Tag Format
The FAQ section MUST be wrapped in CMS template tags and use H3 headings for questions, with answers directly below. No extra formatting between question and answer.

```
## Frequently Asked Questions
{{FAQ}}

### This Is the First FAQ Question?
This is the direct answer to the question. Keep it concise and actionable.

### This Is the Second FAQ Question?
And this is the answer to that question. No blank lines or extra formatting between the H3 and the answer text.

{{endFAQ}}
```

Do NOT change this format. [YOUR_CMS] needs the `{{FAQ}}` and `{{endFAQ}}` tags to place the block.

### Improvement Actions
- Replace any question no real school administrator would ask
- Strengthen weak answers with specific data from the main post
- Add a linking opportunity if none exists (one question should point toward a service page or related content)
- Make sure no two questions cover the same ground
- Tighten answer language. Cut fluff and get to the point.

## Phase 2 Re-Check
If you changed content in the TL;DR or FAQ during Phase 2 (replaced a bullet, rewrote an answer), run Steps 1 and 3 again on the changed text. Confirm you added no prohibited phrases or structure problems. Update the Self-Check block if any count changed.

---

## Process Summary

1. **Phase 1: Draft Self-Check**
   - Step 1: Scan for prohibited phrases by tier
   - Step 2: Check readability on the main body
   - Step 3: Check structure
   - Step 4: Fix every required item (leave quotes verbatim and flag attributed quotes)
   - Step 5: Fix warnings where you can, and always fix em-dash overuse
   - Step 6: Judgment checks (standalone sections, H2 answer pattern)
   - Step 7: Write the `## Stage 3 Self-Check` block under `# Links`
2. **Phase 2: FAQ and TL;DR Review**
   - Review the TL;DR against the criteria above
   - Review the FAQ against the criteria above
   - Make changes directly in the draft
   - Re-check any text you edited and update the Self-Check block

## Output
Save the updated draft to `output/[topic-slug]-draft.md` (overwrite the Stage 2 file). Do not create a separate file.

The draft at this point should contain:
- The Stage 2 draft content, now checked and refined
- The `# Links` heading, with the `## Stage 3 Self-Check` block showing PASS or WARN as the first thing under it

Stages 6, 7, and 8 add their tables below the Self-Check block. Everything under `# Links` stays out of the published post.

If changes in Phase 2 were significant (you replaced a question or rewrote a bullet), tell the user in one or two lines what changed and why.
