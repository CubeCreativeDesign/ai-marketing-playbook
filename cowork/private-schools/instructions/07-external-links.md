# Stage 7: External Link Verification

## Purpose
Verify that every external link in the blog post is live, points to an approved source, contains the data being cited, and is not linking to a competitor domain. Fix what's broken. Replace what's from competitors. Remove what can't be verified.

Stage 7 does NOT rewrite content, restructure sections, or improve the draft. It verifies and corrects external sources only.

---

## Core Principles

- **Verify before trusting.** Every external link gets fetched and checked. No assumptions.
- **Do NOT link to competitor domains.** See `reference/k-12-private-school-competitors.md` for the competitor list. If a citation points to a competitor, find an alternative non-competitor source for the same data.
- **Honesty over polish.** Removing an unverifiable statistic is always better than keeping a good-sounding number that can't be backed up.

---

## Pre-Verification Setup

### Load Competitor List
Before verifying any links, read `reference/k-12-private-school-competitors.md` and create a working list of competitor domains to check against.

### Extract All Claims
Read through the entire draft and identify every:
- Specific statistic (percentages, dollar amounts, growth rates, ratios)
- Direct quotes attributed to a source
- Factual claims that need backing ("research shows...", "studies indicate...", "data suggests...")
- Industry benchmarks or averages
- Any link already in the content pointing to an external source

---

## Verification Process

For each claim or existing external link:

### Step 1: Check for Competitor Domains
- Compare every external URL against the competitor list
- If a link points to a competitor domain, it must be replaced with an alternative non-competitor source
- If the statistic is only available from a competitor, find similar data from an approved source tier
- **Exception:** If an exception applies (see Competitor Exceptions section below), the link may be kept

### Step 2: Verify the URL Is Live
- Use web_fetch to confirm the URL returns a live page (not a 404, redirect loop, or error)
- If the URL is broken, find an alternative working source for the same data
- If no alternative exists, remove the statistic and adjust the sentence

### Step 3: Tiered Content Verification — CRITICAL
Use web_fetch to load the source page and verify the claim using this three-tier system:

#### Tier 1: Exact Match (Preferred)
The exact number, data point, or quote in the draft appears on the source page in the correct context.

- The draft says "62% of families research schools online before visiting" and the source page contains "62%" in a context about families researching schools
- **Result:** ✅ Verified — Exact

#### Tier 2: Supported Paraphrase (Acceptable with Guardrails)
The draft uses a paraphrased or rounded version of the data, but the source contains the underlying number that supports it.

- The draft says "nearly two-thirds of families research schools online" and the source page contains "62% of families research schools online"
- **Result:** ✅ Verified — Paraphrased

**Tier 2 Guardrails:**
- The paraphrase cannot change the direction of the data (42% cannot become "a majority")
- Rounded numbers must round honestly (42% can be "over 40%" or "nearly half" but NOT "about half" if the source says 38%)
- Dollar amounts must stay exact — do not paraphrase "$36 return for every $1 spent" into "roughly $35 per dollar"
- Named study results and specific findings must stay exact
- Direct quotes must be verbatim — no paraphrasing someone's quoted words
- If the paraphrase overstates, understates, or misrepresents the source data, correct the draft text to accurately reflect the source

#### Tier 3: Unsupported (Must Fix or Remove)
The source page does not contain data that supports the claim as written.

- The draft says "62% of families research schools online" but the source page says "62% of consumers research products online" (different context — families vs. consumers, schools vs. products)
- The number does not appear on the page at all
- The page topic matches but the specific data point cannot be found
- **Result:** Find a source that supports the claim, correct the draft to match what the source actually says, or remove the statistic

**What "Verified" Means:**
A citation is ONLY verified when ALL of the following are true:
- The link returns a live page
- The exact number or supporting data point appears on that page
- The context in which the stat is used in the draft matches how the source presents it (not taken out of context, not paraphrased into a different meaning)
- The source is from an approved tier

Do NOT mark a citation as ✅ Verified if you matched the topic but could not find the specific number on the page.

### Step 4: Check Source Credibility and Recency
- Confirm the source falls within an approved tier (see below)
- Prefer sources from the last 2 years
- For sources older than 3 years, actively search for more recent data from the same organization
- If a more recent version exists, swap it in

### Step 5: Verify Context Accuracy
- Confirm the statistic is being used in the correct context (not taken out of context or misrepresented)
- If the original source says something different from how the draft uses it, correct the usage

---

## When Fixing Issues

### Broken Link
1. Search for the same data from another approved source
2. If found, swap the link and update the citation
3. If not found, remove the statistic and adjust the surrounding sentence to read naturally

### Competitor Link
1. Search for the same data from a non-competitor source
2. If the same data exists elsewhere, swap the source
3. If not, find similar data from an approved source and adjust the statistic accordingly
4. Never leave a competitor link in the content — **unless one of the exceptions below applies**

### Competitor Exceptions: When Linking Is Allowed
Competitor links may remain in the content under these conditions:

**Exception 1: Competitor is the subject of the content**
When the post is specifically about the competitor (software roundup, tool comparison, vendor review), removing the link would undermine the content's purpose.

**Exception 2: No alternative source exists**
When a statistic is important to the content and no non-competitor source can be found for the same or equivalent data, the competitor source may be kept.

**For both exceptions:**
- Do NOT swap or remove these links
- Flag every retained competitor link in the verification table with the appropriate status:
  - `⚠️ Kept — competitor is the subject`
  - `⚠️ Kept — no alternative source available`
- Add a **Competitor Links Retained** section at the bottom of the verification summary listing each one with a brief reason
- If unsure whether a competitor link qualifies for an exception, keep it and flag it — do not remove it

### Uncited Claim
1. Search multiple approved sources for verification
2. If verified elsewhere, add the proper citation
3. If it cannot be verified anywhere, remove it and adjust the sentence
4. Do not keep unverifiable claims in the content

### Outdated Source
1. Search for updated data from the same organization
2. If updated data exists, swap the statistic and update the citation
3. If no update exists but the original is still valid, keep it
4. If the data has been contradicted by newer research, replace it

---

## Approved Source Tiers

### Tier 1: Education and Government (Preferred)
**National Education Organizations:**
- NAIS (National Association of Independent Schools) — nais.org
- NCES (National Center for Education Statistics) — nces.ed.gov
- CAPE (Council for American Private Education) — capenet.org
- ISM (Independent School Management) — isminc.com
- AISAP (Association of Independent School Admission Professionals)
- ACSI (Association of Christian Schools International) — acsi.org
- NACAC (National Association for College Admission Counseling) — nacacnet.org
- NBOA (National Business Officers Association) — nboa.org
- Enrollment Management Association — enrollment.org
- EdChoice — edchoice.org
- Department of Education — ed.gov

**Regional Independent School Associations:**
- SAIS (Southern Association of Independent Schools) — sais.org
- NYSAIS (New York State Association of Independent Schools) — nysais.org
- CAIS (Connecticut Association of Independent Schools) — caisct.org
- CAIS (California Association of Independent Schools) — caisca.org
- AIMS (Association of Independent Maryland & DC Schools) — aimsmddc.org
- ISANNE (Independent Schools Association of Northern New England) — isanne.org
- PAIS (Pennsylvania Association of Independent Schools) — paispa.org
- VAIS (Virginia Association of Independent Schools) — vais.org
- FCIS (Florida Council of Independent Schools) — fcis.org
- ISAS (Independent Schools Association of the Southwest) — isasw.org
- NCIS (Northwest Council for Independent Schools)

**Regional Accrediting Bodies:**
- Cognia (formerly AdvancED) — cognia.org
- WASC (Western Association of Schools and Colleges)
- NEASC (New England Association of Schools and Colleges)
- MSA-CESS (Middle States Association of Colleges and Schools)

### Tier 2: Marketing Research
- HubSpot — hubspot.com
- Litmus — litmus.com (email marketing data)
- BrightLocal — brightlocal.com (local SEO data)
- WordStream — wordstream.com (PPC/ad benchmarks)
- Campaign Monitor — campaignmonitor.com (email benchmarks)
- Mailchimp — mailchimp.com (email benchmarks)
- Constant Contact — constantcontact.com (email benchmarks)

### Tier 3: Industry, SEO, and Research
- Pew Research — pewresearch.org
- SEMrush — semrush.com (SEO/marketing data)
- Ahrefs — ahrefs.com (SEO/backlink data)
- SpyFu — spyfu.com (competitive research data)
- Backlinko — backlinko.com (SEO studies)
- Moz — moz.com (SEO data)
- RivalIQ — rivaliq.com (social media benchmarks)
- Sprout Social — sproutsocial.com (social media data)
- Vista Social — vistasocial.com (social media data)
- Hootsuite — hootsuite.com (social media benchmarks)
- Buffer — buffer.com (social media data)
- Think with Google — thinkwithgoogle.com
- Google Search Central Blog (official search guidance)
- Statista — statista.com

### Tier 4: Credible Secondary Sources
- Forbes, Inc., Entrepreneur (business context)
- EdWeek, Education Next (education policy)
- EdSurge — edsurge.com
- The 74 — the74million.org
- EdTech Magazine — edtechmagazine.com
- Independent School Magazine
- Harvard Educational Review
- Search Engine Journal (SEO data)

### Sources to AVOID
- Random blog posts without original data
- Sources older than 3 years (unless historically significant)
- Aggregator sites that don't cite their own sources
- Wikipedia (as a direct citation — fine for background research)
- AI-generated content farms
- Sites with obvious bias or sales agenda presenting as research
- Any domain listed in `reference/k-12-private-school-competitors.md`

---

## Citation Format Verification

Stage 7 does not change the format — only verify that:
- Every statistic has a citation (no uncited claims)
- Every citation includes a working hyperlink
- Citation formats are varied (not the same introductory phrase repeated)
- No parenthetical citations exist without the "Source:" prefix
- No competitor domains are linked

If a citation format is wrong, fix it using the 5-format rotation system from Stage 2.

---

## Output

### Apply All Fixes Directly
Do not present fixes for review. Apply all corrections directly to the draft:
- Swap broken links with working alternatives
- Replace competitor links with non-competitor sources
- Remove unverifiable statistics and adjust surrounding sentences
- Update outdated sources with current data
- Fix any citation format issues
- Correct any Tier 2 paraphrases that violate the guardrails

### Add Verification Table to Bottom of Draft
After all content (below the internal link table from Stage 6), add the external link verification table:

```
### External Link Verification

| Draft Claim | Source Text Found | Source | URL | Match Type | Status |
|-------------|-------------------|--------|-----|------------|--------|
| 62% research online | "62% of families research schools online before visiting" | NAIS | [link] | Exact | ✅ Verified |
| Nearly two-thirds research online | "62% of families research schools online" | NAIS | [link] | Paraphrased | ✅ Verified |
| 88% trust online reviews | "88% of consumers trust online reviews as much as personal recommendations" | BrightLocal | [link] | Exact | ✅ Verified |
| Most families research online | "62% of families research schools online" | NAIS | [link] | Unsupported | 🔄 Corrected — 62% ≠ "most" |
| 80% lack a strategy | Not found | — | — | No match | 🗑️ Removed |
| Average cost per inquiry $125 | "$125 average cost per inquiry for private schools" | Finalsite | — | Exact | 🔄 Replaced — competitor source |
| Enrollment platform features | Product page content | Element451 | [link] | N/A — subject link | ⚠️ Kept — competitor is the subject |
| Website builder market share | "43% of independent schools" | Finalsite | [link] | Exact | ⚠️ Kept — no alternative source available |

#### Verification Summary
- Total claims verified: [number]
- Exact matches: [number]
- Supported paraphrases: [number]
- Sources confirmed working: [number]
- Sources replaced (broken): [number]
- Sources replaced (competitor): [number]
- Statistics removed (unverifiable): [number]
- Paraphrases corrected (guardrail violation): [number]
- Competitor links retained: [number]

#### Competitor Links Retained
If any competitor links were kept, list them here:
- [URL] — [brief reason why it was kept]
```

### Save
Save to `output/[topic-slug]-draft.md` (overwrite the existing draft). Do not create a separate file.

---

## Pipeline Awareness
This is Stage 7 of an 8-stage pipeline. Stage 2 wrote the content and formatted citations. Stage 6 handled internal links. Stage 7 verifies and corrects all external sources. Stage 8 performs a full independent link check across the entire draft — it will re-verify every citation using the same tiered system and cross-check against Stage 7's findings.
