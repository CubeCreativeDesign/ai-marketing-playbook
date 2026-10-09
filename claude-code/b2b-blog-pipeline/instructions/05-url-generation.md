# Stage 5: URL/Slug Generation

## Purpose
Generate the best URL slug based on the selected title from Stage 4 and SEO best practices.

**Output feeds:** The batch script renames the draft and the brief to the new slug, and Stage 6 checks this URL for a live page. The Publishing Package is the record the post is published from: TITLE, URL, META DESCRIPTION and AUTHOR.

**Human check:** None inside the pipeline: this stage runs unattended under `claude -p`. Drafts stay in `output/`, with no Drive upload, and an editor reads the finished draft there before it publishes. The Duplicate Check below is the editor's step: if the slug may already exist on the site, say so in a line under the package.

---

## URL Structure
All [YOUR_VERTICAL] blog posts follow this path:
```
https://[YOUR-AGENCY-DOMAIN]/blog/[YOUR_VERTICAL_SLUG]-marketing/[slug]
```

---

## Slug Generation Rules

### Process
1. Read the recommended SEO title from Stage 4 at the top of the draft (in batch mode, auto-accept Stage 4's recommended titles as the selections)
2. Extract the core keyword phrase
3. Remove stop words (unless part of the primary keyword)
4. Hyphenate
5. Generate 2-3 options with reasoning

### Best Practices
- Use the primary keyword in the slug
- Keep it short: 3-6 words maximum
- Use hyphens between words (not underscores)
- All lowercase
- Remove stop words (a, an, the, in, on, at, to, for, of, with, is, are) unless they are part of the primary keyword
- No dates in the URL (content should be evergreen)
- No special characters
- Only include numbers if they are directly relevant to the content (e.g., a list post)
- Ignore any content within parentheses in the title
- Do not repeat words already in the folder path (e.g., don't repeat "[YOUR_VERTICAL]" or "marketing" since they're in `/[YOUR_VERTICAL_SLUG]-marketing/`)
- Prioritize readability and keyword clarity over brevity

### Examples

| Selected Title | Generated Slug |
|----------------|----------------|
| How Can [YOUR_VERTICAL] Companies Rank Higher in Local Search? | `rank-higher-local-search` |
| 5 Google Ads Mistakes [YOUR_VERTICAL] Companies Keep Making | `google-ads-mistakes` |
| The Google Business Profile Mistakes Costing You Calls | `google-business-profile-mistakes` |

---

## Generate 2-3 Options
Present slug options with reasoning and a clear recommendation. In batch mode, auto-select the recommended option and proceed.

```
Option 1: google-ads-mistakes
  - Matches primary keyword exactly
  - 3 words, concise
  - Recommended ✅

Option 2: google-ads-common-mistakes
  - Adds specificity
  - Still readable

Option 3: avoid-google-ads-mistakes
  - Action-oriented
  - Slightly longer than needed
```

---

## Duplicate Check
Before finalizing, remind the user to verify the slug doesn't already exist. Suggest searching:
```
site:[YOUR-AGENCY-DOMAIN]/blog/[YOUR_VERTICAL_SLUG]-marketing/[proposed-slug]
```

---

## Output

Open `output/[topic-slug]-draft.md` and add the following block at the top of the file, above the Stage 4 title package:

```
# Publishing Package
* TITLE: [Selected title from Stage 4]
* URL: https://[YOUR-AGENCY-DOMAIN]/blog/[YOUR_VERTICAL_SLUG]-marketing/[slug]
* META DESCRIPTION: [Meta description from Stage 4]
* AUTHOR: [writer persona used]
* FUNNEL STAGE: [TOFU / MOFU / BOFU]
* GOAL: [Awareness / Lead Gen / Thought Leadership]

```

Pull the top 10 keywords directly from Stage 4's keyword list.

This consolidates all publishing metadata into one block at the top of the draft. Do not create a separate file.
