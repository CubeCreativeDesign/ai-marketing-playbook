# Stage 5: URL/Slug Generation

## Purpose
Generate the best URL slug from the selected title in Stage 4 and SEO best practices. Then build the Publishing Package at the top of the draft.

**Output feeds:** Stage 6 checks this URL for a live page. The Publishing Package is the record the post is published from: TITLE, URL, META DESCRIPTION, AUTHOR, and KEYWORDS. The draft file keeps its working name; the `[topic-slug]` in the file name does not need to match this URL slug (see `batch-template.md`).

**Human check:** You, in the Cowork chat (or the person who runs the project), read the Publishing Package at the top of the draft before the post publishes. Run the Duplicate Check below with web search. If the slug may already exist on the site, say so in a line under the package so that person sees it first.

---

## URL Structure
All private school blog posts follow this path:
```
https://[YOUR-AGENCY-DOMAIN]/blog/private-school-marketing/[slug]
```

**Customize this:** If your blog uses a different folder, change the path here and in Stages 6 and 8.

---

## Slug Generation Rules

### Process
1. Read the recommended SEO title from Stage 4 at the top of the draft. (In batch mode, accept Stage 4's recommended titles as the selections.)
2. Pull out the core keyword phrase.
3. Remove stop words (unless they are part of the primary keyword).
4. Hyphenate.
5. Generate 2 or 3 options with reasoning.

### Best Practices
- Use the primary keyword in the slug
- Keep it short: 3 to 6 words maximum
- Use hyphens between words (not underscores)
- All lowercase
- Remove stop words (a, an, the, in, on, at, to, for, of, with, is, are) unless they are part of the primary keyword
- No dates in the URL (content should be evergreen)
- No special characters
- Use numbers only if they are directly relevant to the content (for example, a list post)
- Ignore any content inside parentheses in the title
- Do not repeat words already in the folder path (don't repeat "marketing" or "private-school," since they are already in `/private-school-marketing/`)
- Put readability and keyword clarity ahead of brevity

### Examples

| Selected Title | Generated Slug |
|----------------|----------------|
| How Can Private Schools Improve Enrollment with Email Marketing? | `email-enrollment-strategies` |
| 7 Email Sequences Every Private School Needs | `email-sequences-enrollment` |
| The Enrollment Funnel Most Private Schools Are Missing | `enrollment-funnel-missing` |

---

## Generate 2 or 3 Options
Present the slug options with reasoning and a clear recommendation. In batch mode, select the recommended option and keep going.

```
Option 1: email-enrollment-strategies
  - Matches the primary keyword exactly
  - 3 words, concise
  - Recommended

Option 2: enrollment-email-sequences
  - Primary keyword present but split
  - Still readable

Option 3: improve-enrollment-email
  - Action-oriented
  - Missing specificity
```

---

## Duplicate Check
Before you finalize, use web search to check that the slug doesn't already exist on the site:
```
site:[YOUR-AGENCY-DOMAIN]/blog/private-school-marketing/[proposed-slug]
```
Also search `site:[YOUR-AGENCY-DOMAIN] [primary keyword]` for a live post on the same topic. If you find a match, pick a different slug and tell the user in one line under the Publishing Package. A new post that repeats a live one competes with it in search.

---

## Output

Open `output/[topic-slug]-draft.md` and add this block at the top of the file, above the Stage 4 title package:

```
# Publishing Package
* TITLE: [Selected title from Stage 4]
* URL: https://[YOUR-AGENCY-DOMAIN]/blog/private-school-marketing/[slug]
* META DESCRIPTION: [Meta description from Stage 4]
* AUTHOR: [writer persona used]
* FUNNEL STAGE: [TOFU / MOFU / BOFU]
* GOAL: [Awareness / Lead Gen / Thought Leadership]

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

Copy the 10 keywords directly from Stage 4's keyword list.

This block puts all publishing metadata in one place at the top of the draft. Do not create a separate file.
