# Stage 7: External Link Verification

## Purpose
Verify that every external link in the blog post is live, points to an approved source, contains the data being cited, and is not linking to a competitor domain. Fix what's broken. Replace what's from competitors. Remove what can't be verified.

Stage 7 does NOT rewrite content, restructure sections, or improve the draft. It verifies and corrects external sources only.

**Output feeds:** Stage 8 re-verifies every citation from scratch and cross-checks your External Link Verification table, so each row needs the draft claim, the source text found and a status. The citations you keep go live in the post.

**Human check:** None inside the pipeline: this stage runs unattended under `claude -p`. Drafts stay in `output/`, with no Drive upload, and an editor reads the finished draft there before it publishes. Every `⚠️ Kept` row goes in Competitor Links Retained with its reason, so the editor sees it first.

---

## Core Principles

- **Verify before trusting.** Every external link gets fetched and checked. No assumptions.
- **Do NOT link to competitor domains.** See `reference/competitors.md` for the competitor list. If a citation points to a competitor, find an alternative non-competitor source for the same data.
- **Honesty over polish.** Removing an unverifiable statistic is always better than keeping a good-sounding number that can't be backed up. [YOUR_VERTICAL] business owners will fact-check claims and dismiss content that doesn't hold up.

---

## Pre-Verification Setup

### Load Competitor List
Before verifying any links, read `reference/competitors.md` and create a working list of competitor domains to check against.

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

- The draft says "[YOUR_VERTICAL] industry revenue reached $[X] billion in [YEAR]" and the source page contains "$23 billion" in a context about [YOUR_VERTICAL] industry revenue
- **Result:** ✅ Verified — Exact

#### Tier 2: Supported Paraphrase (Acceptable with Guardrails)
The draft uses a paraphrased or rounded version of the data, but the source contains the underlying number that supports it.

- The draft says "nearly a quarter of [YOUR_VERTICAL] companies" and the source page contains "[X]% of [YOUR_VERTICAL] companies"
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

- The draft says "62% of homeowners research [YOUR_VERTICAL] online" but the source page says "62% of consumers research home services online" (different context — homeowners vs. consumers, [YOUR_VERTICAL] vs. home services broadly)
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
- If a statistic covers "home services" broadly but is used as if it applies specifically to [YOUR_VERTICAL], either find a [YOUR_VERTICAL]-specific source or adjust the language to acknowledge the broader scope
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

### Tier 1: [YOUR_VERTICAL] Industry, Government, and University Research (Preferred)

**National Industry Organizations:**
- [YOUR_VERTICAL_ASSOCIATION] — [association-domain.org]
- [YOUR_VERTICAL_PUBLICATION] Magazine — [publication-domain.com]
- [SECOND_TRADE_PUBLICATION] — [domain]
- Federal agencies that regulate or measure your vertical (for example OSHA, EPA, the U.S. Census Bureau, the Bureau of Labor Statistics at bls.gov, the SBA at sba.gov)
- [YOUR_VERTICAL_ASSOCIATION]'s research or marketing arm, if it has one

**University Programs and Research Centers:**
- [RELEVANT_UNIVERSITY_DEPARTMENT] — leading research institution for your vertical
- [RELEVANT_UNIVERSITY_DEPARTMENT] — secondary research institution for your vertical
- [YOUR_STATE_UNIVERSITY] — [YOUR_VERTICAL]-related department or extension program
- State university cooperative extension services (.edu domains with [YOUR_VERTICAL] content)

**State [YOUR_VERTICAL] Associations:**
State-level [YOUR_VERTICAL] associations are approved Tier 1 sources. These include but are not limited to associations in any U.S. state (e.g., [Your State] [YOUR_VERTICAL] Association, etc.). If the association is a state-level affiliate or chapter of [YOUR_VERTICAL_ASSOCIATION] or an independent state [YOUR_VERTICAL] organization, it qualifies as Tier 1.

### Tier 2: Marketing Research
- HubSpot — hubspot.com
- BrightLocal — brightlocal.com (local SEO data)
- WordStream — wordstream.com (PPC/ad benchmarks)
- Campaign Monitor — campaignmonitor.com (email benchmarks)
- Mailchimp — mailchimp.com (email benchmarks)
- Constant Contact — constantcontact.com (email benchmarks)
- Litmus — litmus.com (email marketing data)
- ServiceTitan — servicetitan.com (home services industry data)
- Housecall Pro — housecallpro.com (home services business data)

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
- Search Engine Journal (SEO data)
- Google Search Central Blog (official search guidance)
- Statista — statista.com
- IBISWorld — ibisworld.com (industry reports)

### Tier 4: Credible Secondary Sources
- Forbes, Inc., Entrepreneur (business context)
- Home Services trade publications
- Search Engine Journal (SEO data)
- [YOUR_VERTICAL] Technology (if not already covered by [YOUR_VERTICAL_PUBLICATION])
- Local business and franchise publications
- Harvard Business Review (business strategy)
- Think with Google — thinkwithgoogle.com

### Sources to AVOID
- Random blog posts without original data
- Sources older than 3 years (unless historically significant)
- Aggregator sites that don't cite their own sources
- Wikipedia (as a direct citation — fine for background research)
- AI-generated content farms
- Sites with obvious bias or sales agenda presenting as research
- Any domain listed in `reference/competitors.md`

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
| [YOUR_VERTICAL] industry revenue $[X]B | "$[X] billion in revenue" | [YOUR_VERTICAL_ASSOCIATION] | [link] | Exact | ✅ Verified |
| Nearly a quarter of companies | "[X]% of [YOUR_VERTICAL] companies" | [YOUR_VERTICAL_PUBLICATION] | [link] | Paraphrased | ✅ Verified |
| 88% trust online reviews | "88% of consumers trust online reviews as much as personal recommendations" | BrightLocal | [link] | Exact | ✅ Verified |
| Most homeowners research online | "62% of consumers search online for home services" | — | — | Unsupported | 🔄 Corrected — 62% ≠ "most" |
| 80% lack a strategy | Not found | — | — | No match | 🗑️ Removed |
| Average cost per lead $[X] | "$[X] average cost per lead for [YOUR_VERTICAL]" | [VERTICAL_SOFTWARE_VENDOR] | — | Exact | 🔄 Replaced — competitor source |
| Field service software features | Product page content | GorillaDesk | [link] | N/A — subject link | ⚠️ Kept — competitor is the subject |

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
This is Stage 7 of the pipeline. Stage 2 wrote the content and formatted citations. Stage 6 handled internal links. Stage 7 verifies and corrects all external sources. Stage 8 performs a full independent link check across the entire draft — it will re-verify every citation using the same tiered system and cross-check against Stage 7's findings.
