# Stage 5: URL/Slug Generation

## Purpose
Generate the best URL slug based on the selected title from Stage 4 and SEO best practices.

---

## URL Structure
All private school blog posts follow this path:
```
https://yoursite.com/blog/private-school-marketing/[slug]
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
- Do not repeat words already in the folder path (e.g., don't repeat "marketing" or "private-school" since they're in `/private-school-marketing/`)
- Prioritize readability and keyword clarity over brevity

### Examples

| Selected Title | Generated Slug |
|----------------|----------------|
| How Can Private Schools Improve Enrollment with Email Marketing? | `email-enrollment-strategies` |
| 7 Email Sequences Every Private School Needs | `email-sequences-enrollment` |
| The Enrollment Funnel Most Private Schools Are Missing | `enrollment-funnel-missing` |

---

## Generate 2-3 Options
Present slug options with reasoning and a clear recommendation. In batch mode, auto-select the recommended option and proceed.

```
Option 1: email-enrollment-strategies
  - Matches primary keyword exactly
  - 3 words, concise
  - Recommended ✅

Option 2: enrollment-email-sequences
  - Primary keyword present but split
  - Still readable

Option 3: improve-enrollment-email
  - Action-oriented
  - Missing specificity
```

---

## Duplicate Check
Before finalizing, remind the user to verify the slug doesn't already exist. Suggest searching:
```
site:yoursite.com/blog/private-school-marketing/[proposed-slug]
```

---

## Output

Open `output/[topic-slug]-draft.md` and add the following block at the top of the file, above the Stage 4 title package:

```
# Publishing Package
* TITLE: [Selected title from Stage 4]
* URL: https://yoursite.com/blog/private-school-marketing/[slug]
* META DESCRIPTION: [Meta description from Stage 4]
* AUTHOR: [writer persona used]

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

Pull the top 10 keywords directly from Stage 4's keyword list.

This consolidates all publishing metadata into one block at the top of the draft. Do not create a separate file.
