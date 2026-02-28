# Stage 3: FAQ and TL;DR Review

## Purpose
Review and improve the FAQ and TL;DR sections created in Stage 2. This is a quality control pass — not a rebuild. Stage 2 owns structure and formatting. Stage 3 ensures accuracy, completeness, consistency, and quality.

---

## What Stage 3 Does NOT Do
- Does not change the structural format established by Stage 2
- Does not generate FAQ or TL;DR from scratch
- Does not add links to the TL;DR section (no links in TL;DR, ever)
- Does not rewrite the main blog content

---

## TL;DR Review

### Review Criteria
Read the full blog post, then evaluate the existing TL;DR against these standards:

1. **Accuracy** — Does every bullet correctly represent what the main content actually says? Flag and fix anything that overstates, understates, or misrepresents a point.
2. **Completeness** — Are all major takeaways captured? If the post has a key insight that a busy school administrator would need to know, it must be in the TL;DR.
3. **Consistency** — Do the statistics and claims in the TL;DR match the main content exactly? No rounding, no paraphrasing numbers differently.
4. **Conciseness** — Each bullet should be 1-2 sentences. Cut anything that restates what another bullet already covers.
5. **Value** — Would a school admin who ONLY reads the TL;DR walk away with the right takeaways? If not, fix it.
6. **Voice** — Does it match the writer persona used in the post?
7. **Introduction Heading** — Does the `## Introduction:` heading contain a short, SEO-focused title (under 80 characters)? Does it include the primary keyword? Is it inside the wrapper (before `{{endTLDR}}`) with the intro paragraph outside?

### TL;DR Rules
- 3-5 bullet points maximum
- Each bullet: 1-2 sentences
- Include the most compelling statistic from the post
- End with the action item or CTA
- **NO links in the TL;DR — none, ever**
- Bold key numbers and critical terms within bullets

### TL;DR Template Tag Format
The TL;DR section MUST be wrapped in CMS template tags exactly as shown. The introduction paragraph follows the TL;DR inside the wrapper — this keeps both the TL;DR and intro from showing in the blog feed.

```
### TL;DR
{{TLDR}}

[TL;DR bullet points here]

## Introduction: [Short SEO Title, Under 80 Characters]
{{endTLDR}}

[Introduction paragraph starts here — outside the wrapper]
```

Do NOT deviate from this format. The `{{TLDR}}` and `{{endTLDR}}` tags are required for the CMS automation. The introduction heading sits inside the wrapper. The introduction paragraph sits outside.

### Improvement Actions
- Replace weak bullets with stronger takeaways from the main content
- Tighten language — remove filler words and vague phrasing
- Ensure the most important point comes first
- Verify every number matches its citation in the main content

---

## FAQ Review

### Review Criteria
Read the full blog post, then evaluate each FAQ question and answer:

1. **Relevance** — Are these the questions a school administrator would actually ask after reading this post? Replace any weak questions with stronger ones based on:
   - What would someone Google after reading this?
   - What objections might make a school admin hesitate?
   - How do they actually implement this?
   - What's the investment and return?
   - How does this compare to alternatives?

2. **Accuracy** — Does every answer correctly reflect the main content? No contradictions, no invented claims, no statistics that don't appear in the post.

3. **Completeness** — Does each answer fully address the question? A school admin reading just the FAQ should get a useful, actionable response.

4. **Consistency** — Do the answers align with the tone, data, and recommendations in the main post? If the post recommends X but the FAQ implies Y, fix it.

5. **Voice** — Do the answers match the writer persona? If the post is written in Chad's voice with analogies and approachable language, the FAQ shouldn't suddenly sound clinical.

6. **Scannability** — Can a busy reader quickly find the key information in each answer? Answers should use:
   - Bold emphasis on key numbers, benchmarks, and critical takeaways
   - Short paragraphs (2-4 sentences max)
   - Bullet points or numbered lists where appropriate within answers
   - Clear opening statement that directly answers the question

### FAQ Rules
- 3-5 questions (match what Stage 2 produced unless a question is clearly weak)
- Questions phrased the way a school admin would actually ask them
- Answers: 2-4 sentences for simple questions, structured with subheadings/bullets for complex ones
- At least one question should naturally link to your service page or another blog topic
- Format for FAQ schema markup compatibility (JSON-LD)

### FAQ Template Tag Format
The FAQ section MUST be wrapped in CMS template tags and use H3 headers for questions with answers directly below. No extra formatting between question and answer.

```
## Frequently Asked Questions
{{FAQ}}

### This Is the First FAQ Question?
This is the direct answer to the question. Keep it concise and actionable.

### This Is the Second FAQ Question?
And this is the answer to that question. No blank lines or extra formatting between the H3 and the answer text.

{{endFAQ}}
```

Do NOT deviate from this format. The `{{FAQ}}` and `{{endFAQ}}` tags are required for the CMS automation.

### Improvement Actions
- Replace any question that no real school admin would ask
- Strengthen weak answers with specific data from the main post
- Add a linking opportunity if none exists (one question should point toward a service page or related content)
- Ensure no two questions cover essentially the same ground
- Tighten answer language — cut fluff, get to the point

---

## Process

1. Read the full blog post draft from Stage 2
2. Review the TL;DR section against the criteria above
3. Review the FAQ section against the criteria above
4. Update both sections directly in the draft — do not create a separate analysis document
5. If changes are minimal (minor wording fixes), make them silently
6. If changes are significant (replaced a question, rewrote a bullet), briefly note what changed and why to the user

## Output
Save the updated draft to `output/[topic-slug]-draft.md` (overwrite the Stage 2 file)