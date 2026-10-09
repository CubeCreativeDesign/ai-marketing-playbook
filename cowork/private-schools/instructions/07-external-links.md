# Stage 7: External Link Verification

## Purpose
Verify that every external link in the blog post is live, points to an approved source, contains the data being cited, and does not link to a competitor domain. Fix what's broken. Replace what's from competitors. Remove what can't be verified.

Stage 7 does NOT rewrite content, restructure sections, or improve the draft. It verifies and corrects external sources only.

**Output feeds:** Stage 8 re-verifies every citation from scratch and cross-checks your External Link Verification table, so each row needs the draft claim, the source text found, and a status. The citations you keep go live in the post.

**Human check:** You, in the Cowork chat (or the person who runs the project), read the finished draft before it publishes. Every `⚠️ Kept` row goes in Competitor Links Retained with its reason, so Stage 8 can carry it into `# Publication Status`.

---

## Core Principles

- **Verify before trusting.** Fetch and check every external link. No assumptions.
- **Do NOT link to competitor domains.** See `reference/k-12-private-school-competitors.md` for the competitor list. If a citation points to a competitor, find a non-competitor source for the same data.
- **Honesty over polish.** Removing a statistic you can't verify is always better than keeping a good-sounding number that can't be backed up. School administrators check numbers, and one bad stat costs the whole post its trust.

For how to weigh a source's recency against its authority, see `reference/source-policy.md`.

---

## Pre-Verification Setup

### Load the Competitor List
Before you verify any links, read `reference/k-12-private-school-competitors.md` and make a working list of competitor domains to check against.

### Extract All Claims
Read the entire draft and find every:
- Specific statistic (percentages, dollar amounts, growth rates, ratios)
- Direct quote attributed to a source
- Factual claim that needs backing ("research shows...", "studies indicate...", "data suggests...")
- Industry benchmark or average
- Link already in the content that points to an external source

---

## Verification Process

For each claim or existing external link:

### Step 1: Check for Competitor Domains
- Compare every external URL against the competitor list.
- If a link points to a competitor domain, replace it with a non-competitor source.
- If the statistic is only available from a competitor, find similar data from an approved source tier.
- **Exception:** If one of the Competitor Exceptions below applies, the link may stay.

### Step 2: Verify the URL Is Live
- Fetch the URL and confirm it returns a live page (not a 404, redirect loop, or error).
- If the URL is broken, find another working source for the same data.
- If no alternative exists, remove the statistic and adjust the sentence.

### Step 3: Tiered Content Verification (Critical)
Fetch the source page and verify the claim with this three-tier system.

#### Tier 1: Exact Match (Preferred)
The exact number, data point, or quote in the draft appears on the source page in the correct context.

- The draft says "62% of families research schools online before visiting," and the source page contains "62%" in a passage about families researching schools.
- **Result:** ✅ Verified (Exact)

#### Tier 2: Supported Paraphrase (Acceptable with Guardrails)
The draft uses a paraphrased or rounded version of the data, but the source contains the underlying number that supports it.

- The draft says "nearly two-thirds of families research schools online," and the source page contains "62% of families research schools online."
- **Result:** ✅ Verified (Paraphrased)

**Tier 2 guardrails:**
- The paraphrase cannot change the direction of the data (42% cannot become "a majority").
- Rounded numbers must round honestly (42% can be "over 40%" or "nearly half," but 38% is NOT "about half").
- Dollar amounts stay exact. Do not turn "$36 return for every $1 spent" into "roughly $35 per dollar."
- Named study results and specific findings stay exact.
- Direct quotes stay verbatim. Never paraphrase someone's quoted words.
- If the paraphrase overstates, understates, or misrepresents the source, correct the draft text to match the source.

#### Tier 3: Unsupported (Must Fix or Remove)
The source page does not contain data that supports the claim as written.

- The draft says "62% of families research schools online," but the source says "62% of consumers research products online." The context is different: families vs. consumers, schools vs. products.
- The number does not appear on the page at all.
- The page topic matches, but the specific data point is not there.
- **Result:** Find a source that supports the claim, correct the draft to match what the source says, or remove the statistic.

**What "Verified" means.** A citation is verified ONLY when ALL of these are true:
- The link returns a live page.
- The exact number or supporting data point appears on that page.
- The draft uses the stat in the same context the source does (not out of context, not paraphrased into a different meaning).
- The source is in an approved tier.

Do NOT mark a citation ✅ Verified if you matched the topic but could not find the specific number on the page.

### Step 4: Check Source Credibility and Recency
- Confirm the source falls in an approved tier (see below).
- Prefer sources from the last 2 years.
- For sources older than 3 years, search for more recent data from the same organization.
- If a newer version exists, swap it in.

### Step 5: Verify Context Accuracy
- Confirm the statistic is used in the right context and is not misrepresented.
- If a statistic covers "K-12 schools" or "education" broadly but the draft uses it as if it applies only to private or independent schools, find a private-school-specific source or adjust the wording to show the broader scope.
- If the source says something different from how the draft uses it, correct the usage.

---

## When Fixing Issues

### Broken Link
1. Search for the same data from another approved source.
2. If you find it, swap the link and update the citation.
3. If not, remove the statistic and adjust the surrounding sentence so it reads naturally.

### Competitor Link
1. Search for the same data from a non-competitor source.
2. If the same data exists elsewhere, swap the source.
3. If not, find similar data from an approved source and adjust the statistic to match.
4. Never leave a competitor link in the content, **unless one of the exceptions below applies.**

### Competitor Exceptions: When Linking Is Allowed
A competitor link may stay in the content in these cases:

**Exception 1: The competitor is the subject of the content.**
When the post is about the competitor (a software roundup, tool comparison, or vendor review), removing the link would undercut the post's purpose.

**Exception 2: No alternative source exists.**
When a statistic matters to the content and no non-competitor source has the same or equivalent data, the competitor source may stay.

**For both exceptions:**
- Do NOT swap or remove these links.
- Flag every retained competitor link in the verification table with one of these statuses:
  - `⚠️ Kept: competitor is the subject`
  - `⚠️ Kept: no alternative source available`
- Add a **Competitor Links Retained** section at the bottom of the verification summary. List each one with a short reason.
- If you are unsure whether a competitor link qualifies, keep it and flag it. Do not remove it.

### Uncited Claim
1. Search several approved sources for verification.
2. If you verify it, add the proper citation.
3. If you can't verify it anywhere, remove it and adjust the sentence.
4. Never keep an unverifiable claim in the content.

### Outdated Source
1. Search for updated data from the same organization.
2. If updated data exists, swap the statistic and update the citation.
3. If no update exists but the original is still valid, keep it.
4. If newer research contradicts the data, replace it.

---

## Approved Source Tiers

### Tier 1: Education and Government (Preferred)
**National education organizations:**
- NAIS (National Association of Independent Schools): nais.org
- NCES (National Center for Education Statistics): nces.ed.gov
- CAPE (Council for American Private Education): capenet.org
- ISM (Independent School Management): isminc.com
- AISAP (Association of Independent School Admission Professionals)
- ACSI (Association of Christian Schools International): acsi.org
- NACAC (National Association for College Admission Counseling): nacacnet.org
- NBOA (National Business Officers Association): nboa.org
- Enrollment Management Association: enrollment.org
- EdChoice: edchoice.org
- U.S. Department of Education: ed.gov

**Regional independent school associations:**
- SAIS (Southern Association of Independent Schools): sais.org
- NYSAIS (New York State Association of Independent Schools): nysais.org
- CAIS (Connecticut Association of Independent Schools): caisct.org
- CAIS (California Association of Independent Schools): caisca.org
- AIMS (Association of Independent Maryland & DC Schools): aimsmddc.org
- ISANNE (Independent Schools Association of Northern New England): isanne.org
- PAIS (Pennsylvania Association of Independent Schools): paispa.org
- VAIS (Virginia Association of Independent Schools): vais.org
- FCIS (Florida Council of Independent Schools): fcis.org
- ISAS (Independent Schools Association of the Southwest): isasw.org
- NCIS (Northwest Council for Independent Schools)
- Your own state's independent school association, if it isn't listed

**Regional accrediting bodies:**
- Cognia (formerly AdvancED): cognia.org
- WASC (Western Association of Schools and Colleges)
- NEASC (New England Association of Schools and Colleges)
- MSA-CESS (Middle States Association of Colleges and Schools)

For state school-choice programs (vouchers, education savings accounts, tax-credit scholarships), cite the state's own program pages or EdChoice. Check the current program page every time. These programs change often.

### Tier 2: Marketing Research
- HubSpot: hubspot.com
- Litmus: litmus.com (email marketing data)
- BrightLocal: brightlocal.com (local SEO data)
- WordStream: wordstream.com (PPC and ad benchmarks)
- Campaign Monitor: campaignmonitor.com (email benchmarks)
- Mailchimp: mailchimp.com (email benchmarks)
- Constant Contact: constantcontact.com (email benchmarks)

### Tier 3: Industry, SEO, and Research
- Pew Research: pewresearch.org
- SEMrush: semrush.com (SEO and marketing data)
- Ahrefs: ahrefs.com (SEO and backlink data)
- SpyFu: spyfu.com (competitive research data)
- Backlinko: backlinko.com (SEO studies)
- Moz: moz.com (SEO data)
- RivalIQ: rivaliq.com (social media benchmarks)
- Sprout Social: sproutsocial.com (social media data)
- Vista Social: vistasocial.com (social media data)
- Hootsuite: hootsuite.com (social media benchmarks)
- Buffer: buffer.com (social media data)
- Search Engine Journal (SEO data)
- Google Search Central Blog (official search guidance)
- Statista: statista.com

### Tier 4: Credible Secondary Sources
- Forbes, Inc., Entrepreneur (business context)
- EdWeek, Education Next (education policy)
- EdSurge: edsurge.com
- The 74: the74million.org
- EdTech Magazine: edtechmagazine.com
- Independent School Magazine
- Harvard Educational Review
- Think with Google: thinkwithgoogle.com

### Sources to AVOID
- Random blog posts without original data
- Sources older than 3 years (unless historically significant)
- Aggregator sites that don't cite their own sources
- Wikipedia as a direct citation (fine for background research)
- AI-generated content farms
- Sites with obvious bias or a sales agenda dressed up as research
- Any domain listed in `reference/k-12-private-school-competitors.md`

---

## Citation Format Verification

Stage 7 does not change the citation format. It only verifies that:
- Every statistic has a citation (no uncited claims)
- Every citation has a working hyperlink
- Citation formats vary (the same lead-in phrase is not repeated)
- No parenthetical citation exists without the "Source:" prefix
- No competitor domain is linked

If a citation format is wrong, fix it with the 5-format rotation in `reference/citation-formats.md`.

### Hyperlink Coverage Check (Required Every Pass)
Do this for every source cited in the draft, not just the first mention of each:
1. List every sentence in the body that carries a statistic and names a source (by organization name, "the survey," "that data," and so on).
2. For each one, confirm a hyperlink to that source is attached to that sentence. A link somewhere earlier in the same paragraph or section does not count.
3. If a statistic-bearing sentence names its source with no hyperlink of its own, add one directly. Reusing the same URL across several sentences for the same source is fine. The internal-link rule "never link the same destination twice" does not apply to external citations.
4. Separately, confirm the URL in the verification table for each claim matches the URL hyperlinked in the body for that claim, not a different page from the same organization that covers similar data.
5. TL;DR bullets and FAQ answers that restate a body statistic without naming a source don't need their own link if the body already cites it.

Why this check exists: a common miss is a stat-bearing sentence that names its source in plain text one sentence after the paragraph's only hyperlink. A page-level "every source has at least one live link" check misses this. Check sentence by sentence.

---

## Output

### Apply All Fixes Directly
Do not present fixes for review. Apply every correction directly to the draft:
- Swap broken links for working alternatives
- Replace competitor links with non-competitor sources
- Remove unverifiable statistics and adjust the surrounding sentences
- Update outdated sources with current data
- Fix citation format issues
- Correct any Tier 2 paraphrase that breaks a guardrail

If you rewrote a sentence, re-check it against `reference/prohibited-phrases.md` and the em-dash limit (1 per 300 words) before you move on.

### Add the Verification Table Under `# Links`
Below the Stage 6 internal link table, add the external link verification table:

```
### External Link Verification

| Draft Claim | Source Text Found | Source | URL | Match Type | Status |
|-------------|-------------------|--------|-----|------------|--------|
| 62% research online | "62% of families research schools online before visiting" | NAIS | [link] | Exact | ✅ Verified |
| Nearly two-thirds research online | "62% of families research schools online" | NAIS | [link] | Paraphrased | ✅ Verified |
| 88% trust online reviews | "88% of consumers trust online reviews as much as personal recommendations" | BrightLocal | [link] | Exact | ✅ Verified |
| Most families research online | "62% of families research schools online" | NAIS | [link] | Unsupported | 🔄 Corrected: 62% is not "most" |
| 80% lack a strategy | Not found | n/a | n/a | No match | 🗑️ Removed |
| Average cost per inquiry $125 | "$125 average cost per inquiry for private schools" | Finalsite | n/a | Exact | 🔄 Replaced: competitor source |
| Enrollment platform features | Product page content | Element451 | [link] | N/A (subject link) | ⚠️ Kept: competitor is the subject |
| Website builder market share | "43% of independent schools" | Finalsite | [link] | Exact | ⚠️ Kept: no alternative source available |

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
- [URL]: [brief reason it was kept]
```

The vendor names in the example rows are examples only. Check against the domains in your own competitor list.

### Save
Save to `output/[topic-slug]-draft.md` (overwrite the existing draft). Do not create a separate file.

---

## Pipeline Awareness
This is Stage 7. Stage 2 wrote the content and formatted citations. Stage 6 handled internal links. Stage 7 verifies and corrects all external sources. Stage 8 runs a full, independent link check across the entire draft. It re-verifies every citation with the same tiered system and cross-checks Stage 7's findings.
