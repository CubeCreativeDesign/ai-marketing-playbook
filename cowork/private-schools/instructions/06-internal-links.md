# Stage 6: Internal Linking

## Purpose
Find relevant pages on [YOUR-AGENCY-DOMAIN] and add internal links to them in the blog post draft. Also check whether the blog post's own URL is live.

**Output feeds:** Stages 7 and 8 protect the links you add and re-test them, and Stage 8 checks every internal URL again. The `# Links` heading holds the Stage 3 Self-Check and the Stage 6, 7, and 8 tables. Everything under it is internal notes and never goes live.

**Human check:** You, in the Cowork chat (or the person who runs the project), read the finished draft before it publishes. Put any dead, redirected, or not-yet-live destination first in the Link Summary, so Stage 8 carries it into `# Publication Status`.

---

## Pre-Linking Checks

### Check the Blog Post URL
Before you add any internal links, check the blog post's own URL from the Publishing Package at the top of the draft:
1. Use web search or fetch to check whether `https://[YOUR-AGENCY-DOMAIN]/blog/private-school-marketing/[slug]` returns a live page.
2. If the URL is not live yet (expected for an unpublished draft), note it for the user.
3. If the URL returns a different page or redirects, flag it right away.

### Catalog Existing Links
Read the entire draft and list every link already in the content:
- The anchor text and destination URL
- The section where each link sits
- These links are protected. Never replace or change them.

---

## Process

### Step 1: Identify Linkable Topics
Read the draft and find:
- Key concepts that have their own pages on [YOUR-AGENCY-DOMAIN]
- Service mentions that could link to service pages
- References to other blog topics you have already published
- General marketing terms that could link to educational content on the site

### Step 2: Search [YOUR-AGENCY-DOMAIN]
For each linkable topic, search with `site:[YOUR-AGENCY-DOMAIN] [topic]`. Look for:
- Blog posts in `/blog/private-school-marketing/`
- Blog posts in other verticals that may be relevant (for example `/blog/small-business-marketing/` or `/blog/[other-vertical]-marketing/`)
- Service pages, for example in `/school-marketing-services/` or `/services/`
- The who-we-serve page: `/who-we-serve/private-school`
- The contact page: `/contact`

**Customize this:** Replace the paths above with your site's real structure.

### Step 3: Verify Destination URLs
Before you add any link:
1. Fetch the destination URL and confirm it returns a live page.
2. If a URL returns a 404, redirects, or is broken in any other way, do NOT use it.
3. Link only to verified live pages.

### Step 4: Evaluate Link Relevance
Before you add a link, confirm:
- The destination page is directly relevant to the context
- The anchor text fits naturally in the sentence
- The link adds real value for the reader
- The context makes sense. Do not force links.
- The text does not already contain a link
- The destination URL is not already linked elsewhere in the content

### Step 5: Apply Links
Insert the approved links directly into the draft content.

---

## Linking Rules

### Density
- Maximum 5 internal links per 1,000 words
- For posts over 1,500 words, work in sections of about 1,000 words, with up to 5 links per section
- Spread links through the content. Do not cluster them in one section.
- Never link the same destination URL twice in the post
- Always keep the contact page CTA link at the end (Stage 2 should have added it)

### Anchor Text
**Good anchor text is descriptive and natural:**
- "private school enrollment strategies"
- "learn how to improve your school's online presence"
- "admissions marketing tactics for independent schools"

**Bad anchor text. Never use:**
- "click here"
- "read more"
- "this article"
- Exact-match keyword stuffing

### Link Placement Priority
**High-value positions:**
- Within the first 100 words (for important pages)
- In section introductions
- Within actionable advice sections
- In the conclusion or CTA area

**Low-value positions. Avoid:**
- Forced into lists
- Several links in the same sentence
- Headings or subheadings (never link these)
- Image captions (unless highly relevant)

---

## Existing Link Protection
- Never replace or change any existing link
- If text already contains a link, do not add another link to that text
- If a URL is already linked anywhere in the content, do not add it again
- The who-we-serve link that Stage 2 added in the introduction is protected. Do not move, change, or duplicate it.

---

## Output

### Apply to Draft
1. Apply the links throughout the draft content.
2. Find the `# Links` H1 heading after the FAQ section. Add the internal link table and Link Summary below the Stage 3 Self-Check block. If `# Links` does not exist, create it as an H1 heading after `{{endFAQ}}`, then add the table below it.
3. All link tables from Stages 6, 7, and 8 belong under this `# Links` heading.
4. Save to `output/[topic-slug]-draft.md` (overwrite the existing draft). Do not create a separate file.

### Internal Link Table Format (added under `# Links`)

```
### Internal Links

| Original Text | Linked Version | Destination URL | Verified |
|---------------|----------------|-----------------|----------|
| private school marketing | [private school marketing](https://[YOUR-AGENCY-DOMAIN]/who-we-serve/private-school) | /who-we-serve/private-school | ✅ |
| improve your enrollment | [improve your enrollment](https://[YOUR-AGENCY-DOMAIN]/blog/private-school-marketing/enrollment-tips) | /blog/private-school-marketing/enrollment-tips | ✅ |
```

### Link Summary (added after the table)

```
#### Link Summary
- Destinations that are dead, redirected, or not yet live: [list first, or "None"]
- Total existing links in draft: [number]
- Total new links added: [number]
- Combined links per 1,000 words: [ratio]
- Blog post URL status: [live / not yet published / issue found]
- All destination URLs verified: [yes / list any issues]
```
