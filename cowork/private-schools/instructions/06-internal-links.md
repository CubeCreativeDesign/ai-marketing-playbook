# Stage 6: Internal Linking

## Purpose
Find and add relevant internal links from yoursite.com to the blog post draft. Also verify the blog post's own URL slug is live.

---

## Pre-Linking Checks

### Verify Blog Post URL
Before adding any internal links, verify the blog post's own URL from the Publishing Package at the top of the draft:
1. Use web search to check if `https://yoursite.com/blog/private-school-marketing/[slug]` returns a live page
2. If the URL is not live yet (expected for unpublished drafts), note this for the user
3. If the URL returns a different page or redirect, flag it immediately

### Catalog Existing Links
Read through the entire draft and catalog every link already in the content:
- Note the anchor text and destination URL
- Note the section/location of each link
- These links are protected — never suggest replacing or modifying them

---

## Process

### Step 1: Identify Linkable Topics
Read through the draft and identify:
- Key concepts that have dedicated pages on yoursite.com
- Service mentions that could link to service pages
- References to other blog topics already published
- Generic marketing terms that could link to educational content on the site

### Step 2: Search Your Site
For each linkable topic, search for relevant pages using `site:yoursite.com [topic]`:
- Blog posts in your blog directory
- Blog posts in other verticals that may be relevant
- Service pages
- Your main service/industry page
- Contact page

**Customize this:** Replace the paths above with your actual site structure.

### Step 3: Verify Destination URLs
Before recommending any link:
1. Verify the destination URL actually exists and returns a live page
2. If a URL returns a 404, redirect, or is otherwise broken, do NOT recommend it
3. Only recommend links to verified live pages

### Step 4: Evaluate Link Relevance
Before adding a link, confirm:
- The destination page is directly relevant to the context
- The anchor text fits naturally in the sentence
- The link adds genuine value for the reader
- The context makes sense — do not force links
- The text does not already contain a link
- The destination URL is not already linked elsewhere in the content

### Step 5: Apply Links
Insert the approved links directly into the draft content.

---

## Linking Rules

### Density
- Maximum 5 internal links per 1,000 words
- For posts over 1,500 words, process in ~1,000 word sections with up to 5 links per section
- Spread links throughout the content — not clustered in one section
- Never link the same destination URL twice in the entire post
- Always include the contact page CTA link at the end (this should already exist from Stage 2)

### Anchor Text
**Good anchor text — descriptive and natural:**
- "private school enrollment strategies"
- "learn how to improve your school's online presence"
- "admissions marketing tactics for independent schools"

**Bad anchor text — never use:**
- "click here"
- "read more"
- "this article"
- Exact-match keyword stuffing

### Link Placement Priority
**High-value positions:**
- Within the first 100 words (for important pages)
- In section introductions
- Within actionable advice sections
- In the conclusion/CTA area

**Low-value positions — avoid:**
- Forced into lists
- Multiple links in the same sentence
- Headlines or subheadings (never link these)
- Image captions (unless highly relevant)

---

## Existing Link Protection
- Never suggest replacing or modifying any existing links
- If text already contains a link, do not add another link to that same text
- If a URL is already linked anywhere in the content, do not suggest adding it again
- The who-we-serve link added in the introduction during Stage 2 is protected — do not move, change, or duplicate it

---

## Output

### Apply to Draft
1. Apply the links throughout the draft content
2. Look for the `# Links` H1 heading after the FAQ section. If it exists, add the internal link table and link summary below it. If it does not exist, create `# Links` as an H1 heading after `{{endFAQ}}` and then add the table below it.
3. All link-related tables from Stages 6, 7, and 8 belong under this `# Links` heading
4. Save to `output/[topic-slug]-draft.md` (overwrite the existing draft). Do not create a separate file.

# Links

### Internal Link Table Format (added to bottom of draft)

| Original Text | Linked Version | Destination URL | Verified |
|---------------|----------------|-----------------|----------|
| private school marketing | [private school marketing](https://yoursite.com/who-we-serve/private-school) | /who-we-serve/private-school | ✅ |
| improve your enrollment | [improve your enrollment](https://yoursite.com/blog/private-school-marketing/enrollment-tips) | /blog/private-school-marketing/enrollment-tips | ✅ |

### Link Summary (added to bottom of draft, after table)
- Total existing links in draft: [number]
- Total new links recommended: [number]
- Combined links per 1,000 words: [ratio]
- Blog post URL status: [live / not yet published / issue found]
- All destination URLs verified: [yes / list any issues]
