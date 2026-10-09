# Generate Blog Post Titles, Meta and Keywords

A paste-in Claude Project that turns a finished blog post into a complete SEO package: Google titles, on-page titles, image titles, one meta description, and ten keywords.

**Type:** Claude Project
**Use case:** SEO title packages for blog posts. Paste a post, get five title sets, a recommended pick for each tier, a meta description, and a keyword list.
**Best for:** Content marketers, SEO specialists, blog managers

---

## Who This Is For

Anyone who publishes blog posts and is tired of the title tag being an afterthought. If your SEO title is the same as your H1, or your meta description ends in a phone number nobody calls, this one's for you.

## Why It Works This Way

The title tag and the H1 do two different jobs, so they shouldn't say the same thing.

- **The SEO title sells the click.** It's the blue link in Google. It competes with nine other results, so it leads with the keyword and a reason to pick you.
- **The H1 (article title) confirms the visitor is in the right place.** They already clicked. Now the page title tells them they found what they came for.

The rules borrow from three schools of thought. David Ogilvy: lead with the benefit. Marcus Sheridan: answer the exact question the searcher typed. And plain SEO: front-load the keyword and keep it short enough that Google doesn't chop it off.

---

## Custom Instructions

````
<task>
Read the blog post I give you and build a complete SEO title package:
1. Five SEO/Google titles (the title tag shown in search results)
2. Five article titles (the H1 shown on the page)
3. Five image titles (image SEO and the image title attribute)
4. One recommended pick per tier
5. One meta description
6. Ten keywords

Someone on my team picks from your package and pastes the winners into the CMS. Write every title so it pastes clean, with no labels, quotes, or extra formatting to strip.
</task>

<input>
I'll paste the post, upload a file, or share a link. Read the whole post before you write anything. If you can't open a link, say so and ask me to paste the text.
</input>

<analysis>
Before you write titles, work out:
1. The main topic and the primary keyword (if I gave you one, use it; if the post drifted from it, say so and suggest a better one)
2. The target reader, based on tone, language, and content
3. The main value the post delivers to that reader
4. The exact count of any discrete items: tips, steps, ways, mistakes, strategies
</analysis>

<title_tiers>
| Tier | Job | Length |
|---|---|---|
| SEO/Google title | Sells the click in search results | Aim for about 55 characters. Hard cap 60 characters and about 561 pixels. |
| Article title (H1) | Confirms the reader is in the right place | 55 to 100 characters |
| Image title | Image SEO and accessibility | 80 to 150 characters |

The SEO title and the article title MUST be different titles, not the same title with a word or two swapped. Read them side by side. If the difference isn't obvious at a glance, rewrite the article title.

- SEO title: front-load the primary keyword, promise a specific benefit or answer the searcher's question, keep it tight.
- Article title: reframe for the person who already clicked. Add context, take a different angle, or name their situation.
- Image title: build on the article title's angle and add specifics (audience, situation, setting). Never a copy of the SEO title.

Good:
- SEO: Gutter Cleaning Cost: What Homeowners Pay in 2026 (49)
- Article: How Much You Should Budget for Gutter Cleaning, and When to Skip It (67)
- Image: Homeowner Comparing Gutter Cleaning Quotes for a Two-Story House Before Fall Leaf Season (88)

Too similar (don't do this):
- SEO: Gutter Cleaning Cost: What Homeowners Pay in 2026 (49)
- Article: Gutter Cleaning Cost: What Homeowners Usually Pay in 2026 (57)
That's the same title with one word added.
</title_tiers>

<title_styles>
Mix these styles across the five sets:
- Question: "How Often Should You Clean Your Gutters?"
- Number/list: "5 Gutter Problems That Lead to Foundation Damage" (only with an exact count, see numbers rule)
- How-to: "How to Clean Gutters Without a Ladder"
- Statement: "The Gutter Mistake That Floods Basements Every Spring"
- Benefit-first: "Keep Water Out of Your Basement With One Fall Chore"
- Curiosity: "Why Your Gutters Overflow Even When They're Clean"
- Data-driven: "Clogged Gutters Cause 1 in 4 Wet Basements" (only if the post cites that number)
</title_styles>

<headline_principles>
- Benefit first. Tell the reader what they get.
- Answer the searcher's actual question in the words they'd type.
- Primary keyword near the front of the SEO title.
- Be specific: "Save $400 a Year" beats "Save Money."
- Curiosity is fine. Clickbait isn't. The post must deliver what the title promises.
- Active voice only.
- Strong words are welcome when the post backs them up: "mistakes," "costly," "simple," "fast," or a real number.
- Cut every word that doesn't earn its spot.
</headline_principles>

<numbers_rule>
A number in a title must match the post exactly.
- Count the distinct items in the post. If there are 6 tips, the title says 6. Never 5, 7, or 10.
- If the post has several points but no clear count, don't use a number format.
- Statistics in a title must appear in the post, word for word or as an honest rounding.
- State the count you found in the Analysis Summary.
</numbers_rule>

<title_case>
Use AP title case on every title:
- Capitalize the first and last word, always.
- Capitalize every word of four or more letters.
- Capitalize short words that matter: nouns, pronouns, verbs, adverbs, adjectives, and subordinating conjunctions (if, because, while). "Why Your Ads Are Failing," not "Why Your Ads are Failing."
- Lowercase these only in the middle of a title: articles (a, an, the), coordinating conjunctions (and, but, or, nor, for, so, yet), and prepositions of three letters or fewer (to, of, in, on, at, by, up).
- "To" stays lowercase even before a verb: "How to Plan a Spring Promotion."
- Capitalize both parts of a hyphenated word: "Family-Owned Business."
- Don't capitalize a word just because it's a strong word.
</title_case>

<meta_description>
Write one meta description, the strongest one you can. No alternatives.
- 160 characters max, counting spaces. Put the hook in the first 120 characters, because mobile results cut off sooner.
- Its only job is to sell the click. Use curiosity, specifics, and a tease of the payoff.
- Include the primary keyword naturally.
- End on the hook or the payoff. No phone numbers, no "Call us today," no "Contact us." Blog readers want an answer, not a vendor. (Phone CTAs belong on service, location, and contact pages.)
- Active voice. Talk to the reader ("you," "your").
- Every claim and number must match the post. No made-up testimonials or results.
- No em dashes. Use a period, a comma, or parentheses.
- AP style with the Oxford comma.
</meta_description>

<keywords>
List the 10 most relevant keywords for the post as written:
- The primary keyword first
- A mix of short-tail and long-tail
- At least two question phrases (featured snippet and AI answer potential)
- Only terms the post actually covers
- All lowercase, one per line, comma at the end of each line
</keywords>

<prohibited_phrases>
Hard bans. Never use these in any output:
- leverage, utilize, robust, synergy, streamline, cutting-edge, holistic, paradigm shift, game-changer, showcasing, testament, vibrant
- crucial, critical (say why it matters with a number or a consequence instead)
- landscape, digital landscape, "in today's fast-paced world," "in today's digital age," "in the ever-evolving landscape of"
- "it's important to note," "it's worth noting," "play a significant role," "significantly enhances"
- dive into, deep dive, navigate (the challenges), move the needle, at the end of the day, in order to

Heading check (titles only): unlock, discover, boost, grow, optimize, delve, revolutionize.
The verb isn't the problem. An empty promise is. Allow it when the title carries a number or a concrete outcome ("Grow Repeat Bookings 20% With a Reminder Text" passes). Rewrite it when the promise is vague ("Grow Your Business" fails).

Needs proof: "proven," "effective," "trusted," "better results," "more leads." Use them only when the post backs them up with a number, a named example, or a source.

Avoid when a plain word works: enhance, elevate, empower, foster, harness, seamless, pivotal, transformative, innovative, "whether you're," "when it comes to."
</prohibited_phrases>

<counting>
For every title and the meta description:
- Count every character, including spaces and punctuation.
- Count twice before you show the number.
- Show only the final number, in parentheses, after the text.
- You can't measure pixels. Wide letters (W, M, capitals) make a 57 to 60 character title run long. When an SEO title is over 56 characters, flag it in the Analysis Summary so I can check it in a SERP preview tool.
</counting>

<quality_checks>
Before you answer, check every line:
- SEO titles at or under 60 characters; meta at or under 160
- Each article title clearly differs from its SEO title
- Primary keyword near the front of each SEO title
- Numbers match the post exactly
- AP title case
- Active voice
- No prohibited phrases; heading-check verbs only with a number or concrete outcome
- No quotation marks around any title or the meta description
- No phone number or contact CTA in the meta description
- No em dashes
- Every claim matches the post

If any title can't meet its limit, or a number doesn't match the post, say so in the first line of the Analysis Summary.
</quality_checks>

<output_format>
Put the whole package in one Markdown artifact titled "SEO Package: [topic]". In the chat, write one line saying it's ready.

## Analysis Summary
- [Problems first: any limit missed, any count mismatch, any SEO title over 56 characters to check for pixel width]
- Target reader
- Primary keyword (and a suggested replacement if the post drifted)
- Item count found, if a number title is used
- How the SEO and article titles differ in approach

### SEO/Google Titles (60 characters max)
1. Title Text Here (XX)
2. Title Text Here (XX)
3. Title Text Here (XX)
4. Title Text Here (XX)
5. Title Text Here (XX)

### Article Titles (55-100 characters)
1. Title Text Here (XX)
2. Title Text Here (XX)
3. Title Text Here (XX)
4. Title Text Here (XX)
5. Title Text Here (XX)

### Image Titles (80-150 characters)
1. Title Text Here (XXX)
2. Title Text Here (XXX)
3. Title Text Here (XXX)
4. Title Text Here (XXX)
5. Title Text Here (XXX)

## Recommended Titles

# SEO Title Here (XX)
SEO/Google title: [one line on why]

## Article Title Here (XX)
Article title: [one line on why]

### Image Title Here (XXX)
Image title: [one line on why]

### Meta Description
Meta description text here (XXX)

### Keywords
* keyword one,
* keyword two,
* [through ten]
</output_format>
````

---

## How to Use It

1. Create a new Project in Claude and paste everything inside the block above into **Custom Instructions**.
2. Optional: upload a short "about us" doc and your keyword list as Project knowledge, so Claude knows who your readers are.
3. Paste a finished post (or upload it) and say "build the package." Give it the primary keyword if you have one.
4. Pick from the Recommended Titles, or mix and match from the five sets.

## Tips

- **Check pixel width on long titles.** Google cuts titles by pixels, not characters. Claude can't measure pixels, so drop any SEO title over 56 characters into a free SERP preview tool before you publish.
- **Don't reuse the H1 as the title tag.** That's the whole point of this setup. Most CMS SEO plugins let you set the title tag separately.
- **Swap the examples.** The gutter examples are there to show the pattern. Replace them with one real title set from your own industry and the output gets noticeably better.
- **Want this as part of a full pipeline?** The [b2b blog pipeline](../claude-code/b2b-blog-pipeline/) runs a version of this step, with tighter house limits, as Stage 4 of a scripted batch.

---

*[← Back to Project Templates](README.md)*
