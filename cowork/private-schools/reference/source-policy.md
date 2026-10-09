# Source Policy: K-12 Private School Marketing Research

This file governs what kinds of sources Stage 0 research may pull from, and how Claude's
research tools in Cowork (web search, web fetch, and Research) should be steered. It is
read by `instructions/00-deep-research.md` before any searching, and again by Stage 7
when it verifies external links. The principle is simple:

**Exclusion is strict. Inclusion is biased, not locked.**

Hard-block competitors and junk. Bias hard toward authoritative primary sources, but do
not forbid a good source just because it is not on the preferred list.

---

## Setup: what you must fill in

Most of this file transfers as written. Two things are yours to set:

1. **Competitors.** Fill in `reference/k-12-private-school-competitors.md`. The
   Excluded list below is built from that file at run time. Do not keep a second copy
   of the list here. It will drift.
2. **Tier 1 additions.** If your region or niche has its own association, state agency,
   or trade publication, add it to Tier 1.

---

## Why this matters for this audience

Your readers are private school administrators, admissions teams, and marketing
directors. They are detail-oriented professionals who cross-check statistics and lose
trust in content that does not hold up. In the marketing-advice niche, plain web search
rewards exactly the wrong pages: SEO content farms, AI-spun listicles that recycle
fabricated numbers, and your own competitors.

For this audience, source survivability beats source breadth. Accept slightly thinner
research in exchange for every stat holding up under scrutiny.

---

## The two-axis rule: recency against authority

Source quality is not one scale. Weight the two axes by claim type.

**Platform, algorithm, and product claims.** Google Business Profile, Google Ads
mechanics, Google local ranking, AI search features, social platform features, ad
products, and marketing automation features. These change constantly.

- **Recency dominates.** A current mid-tier source beats a three-year-old authoritative
  one, because the product changed.
- Check the page date. Drop platform claims from pages older than **18 months**, and
  drop undated pages for these claims.
- Prefer official platform documentation as the primary source.

**Market, enrollment, and demographic claims.** Private school enrollment trends,
tuition data, school choice and voucher data, demographic shifts, family
decision-making behavior, and retention benchmarks.

- **Authority dominates.** Age is acceptable if it is the authoritative dataset.
- Do not date-gate these. The best source may be the most recent government or
  association release, even if it is a couple of years old. Always state the year.

---

## Tier 1: Actively seek

Name these sources in your search terms and in the Research prompt. Ask Research to
prioritize them.

**Platform and official documentation**
- Google Business Profile Help, Google Ads Help
- Google Search Central and the Search Central Blog
- Think with Google (thinkwithgoogle.com)

**Government and education data**
- National Center for Education Statistics (nces.ed.gov)
- U.S. Census Bureau (census.gov)
- U.S. Department of Education (ed.gov)
- IPEDS and the Private School Universe Survey (PSS)
- Your state's department of education, for state program facts

**Private school associations and research**
- National Association of Independent Schools (nais.org), research and StatsOnline
- Independent School Management (isminc.com)
- EdChoice (edchoice.org), school choice and voucher data
- National Catholic Educational Association (ncea.org)
- Council for American Private Education (CAPE, capenet.org)
- Niche.com, as a data source on school search behavior, with attribution

**Marketing research with disclosed methodology**
- BrightLocal (local consumer review and search surveys)
- Pew Research Center (pewresearch.org)
- Moz (moz.com, Local Search Ranking Factors)
- Search Engine Land and Search Engine Journal, for articles citing primary data. Never
  as the primary source themselves.
- Statista, only when the underlying source is named and traceable

---

## Tier 2: Acceptable with caution

Usable, but verify the underlying data and prefer a Tier 1 source if one exists for the
same claim.

- Mainstream business, education, and trade press, with a named author and a date
- Vendor or software research that discloses its methodology and sample
- Reputable non-competitor SEO and marketing blogs

If a Tier 2 page only restates a statistic, trace it to the original and cite that
instead.

---

## Excluded: Hard block, never cite, never link

**Competitor agencies.** Every domain in `reference/k-12-private-school-competitors.md`.
Re-read that file at the start of each run. Discard any search result from those
domains before you open it, and never link to them in any stage.

**Junk and unreliable sources.** Exclude by judgment. Never cite as a source for a
statistic:

- Content farms and auto-generated listicle sites
- Stat-aggregator pages that cite each other in a circle, such as "99 stats" roundups,
  with no traceable original
- Undated pages making time-sensitive platform claims
- Reddit, Quora, and forum posts as a **primary** statistic source. Fine as a lead to
  find the real source, never as the citation.
- Press releases dressed as research, with no methodology

---

## Note on academic sources

Education and enrollment topics have real academic and association research, so academic
sources rank higher here than in most marketing verticals. Use them where they genuinely
apply: enrollment behavior, family decision research, and education policy.

For platform and marketing-tactic claims, industry and platform primary sources outrank
journals. There is no peer-reviewed literature on Google Business Profile optimization,
and chasing journal articles for tactic claims wastes the research pass.

---

## How each Cowork tool applies this policy

- **Web search.** Discovery. It has no domain filter, so apply the competitor list by
  hand: discard every competitor result before you open the page. For platform claims,
  add the current year to the query and check each page's date.
- **Web fetch.** Confirmation. Open the page and confirm the statistic appears on it,
  word for word or number for number, before it goes in the research file. A snippet or
  a summary is not confirmation.
- **Research.** The deep narrative pass. Steer it with prompt text only: name the Tier 1
  sources, paste the competitor list as domains to ignore, and ask for a link for every
  number. Treat its output as leads. Re-verify every number it returns at the primary
  source with web fetch, because deep-research tools invent statistics and citations
  often enough that none can be trusted unchecked.

Every URL from any tool must pass the Stage 0 fact-check step before it is cited.
