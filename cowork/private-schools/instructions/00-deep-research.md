# Stage 0: Deep Research and Fact-Check

Stage 0 gathers verified quotes and statistics for one topic and saves them as a research bundle that every later stage draws from.

**Do NOT write the blog post here. Do NOT write the topic brief. This stage produces verified source material only.**

**Output feeds:** Stage 1 builds the topic brief from this bundle, and Stage 2 quotes and cites it. Neither one redoes your research, so every quote and statistic must be usable as written. Stages 7 and 8 check the draft's citations against the URLs you record here. An error that gets past this stage repeats in the post, its FAQ and its meta description.

**Human check:** You, in the Cowork chat. Before Stage 1 starts, skim `## Verification Notes`: what was dropped, what conflicted, and anything tagged `unverified`. In batch mode Claude does not stop for this check, so read the Verification Notes of each bundle when the batch ends, before any post publishes.

## Tools This Stage Uses

This template runs in Claude Cowork with no plugins, scripts or API keys. Stage 0 uses three built-in tools:

* **Web search.** Finds candidate pages. Claude runs many short searches, one research question at a time.
* **Web fetch.** Opens a single URL and reads the full page text. This is how every quote and statistic gets verified. A search snippet is never verification.
* **Research (optional).** Claude's Research feature runs a longer, multi-step search and returns a cited report. If it is turned on in your workspace, use it for the broad discovery pass in Phase B. If it is not available, run Phase B with web search alone. The stage still works.

You cannot filter web search results by domain or by date. Apply the source policy by judgment: discard excluded domains when they appear, and check each page's publish date when you fetch it.

## Inputs

* **Topic.** From the batch queue row (`batch-queue.md`, the Topic column) or from the chat.
* **Research/Notes.** From the same row. If it holds a link, fetch it. If you attached files (PDFs, reports, survey results), treat them as primary source material. The research must complement them, not repeat them.
* **Audience and intended use.** If the topic names neither, use the audience rules in `CLAUDE.md`: school administrators, heads of school, admissions and enrollment teams, and marketing directors at private and independent K-12 schools who are deciding whether to hire a marketing agency. Not parents searching for a school. State the audience and intended use in the first paragraph of the bundle's `## Topic Overview`.

### The Topic Slug

Make the topic slug once, here, and reuse it in every later file name. Take the topic, lowercase it, keep three to six meaningful words, and join them with hyphens. Example: "Open house marketing for private schools" becomes `open-house-marketing-private-schools`.

* Research bundle: `research/[topic-slug]-research.md`
* Topic brief (Stage 1): `output/[topic-slug]-brief.md`
* Draft (Stages 2 through 8): `output/[topic-slug]-draft.md`

Stage 5 creates the published URL slug, which may differ. Keep the file names on the topic slug so the research, brief and draft stay together.

### When There Is No Topic Yet

If you start interactively and have not picked a topic, run Stage 1, Steps 1 and 2 first (ask for direction, then validate the topic). Then run Stage 0 on the chosen topic, then return to Stage 1, Step 3 to write the brief.

## Read the Source Policy First

Before any searching, read `reference/source-policy.md` in full. It defines:

* The Tier 1, Tier 2 and Excluded source tiers for this vertical.
* The recency-vs-authority rule. Platform claims need recency. Market and enrollment claims need authority.
* The competitor exclude list. Also re-read `reference/k-12-private-school-competitors.md` now. That file is the source of truth for exclusions.

Every search you run must apply this policy. Exclusion is strict. Inclusion is biased, not locked.

## Check Earlier Bundles First

Before you run a single search, look in `research/` for bundles on related topics. A statistic another bundle already verified is a head start.

* **Treat a matching claim as a lead, not a citation.** Fetch its URL again and confirm the figure still appears there. Pages change. If the source changed, say so in Verification Notes.
* **Watch for overuse.** If the same statistic already appears in several of your posts, look for a different figure that makes the same point. Repeating one number across a cluster of posts reads as thin.
* **Spend your search effort on what earlier bundles don't hold.** That's the real research job.

Record in Verification Notes how many claims came from earlier bundles and how many are new.

## Output

Write one file: `research/[topic-slug]-research.md`. Create the `research/` folder if it does not exist.

Required sections, in this order, in markdown. Keep these headings exactly as written. Later stages look for them by name.

```
# Research Bundle: [Topic]

## Topic Overview
(2-4 paragraphs: the audience and intended use, the topic, what was investigated,
and which tools contributed. Note anything that failed, such as a page that would not load.)

## Direct Quotes
(For each: blockquote the exact text, then
(Source: Author/Speaker; Year, [Source Name](url)).
Tag each with how it was found, its tier and its status, e.g. [Web search · Tier 1 · verified].)

## Statistics and Data
(For each: the statistic with its date, sample size and methodology when available, then
(Source: Org, Title; Year, [Source Name](url)).
Tag each [tool · tier · verified|unverified].)

## Academic Research
(For each: key finding, full citation, journal link, methodology where available.
Education and enrollment topics have real academic research. Use it where it applies.)

## Additional Resources
(Markdown list of further-reading links with one-line descriptions.)

## Verification Notes
(The fact-check output. List what was verified, what was dropped and why, conflicting
findings, and anything flagged low-confidence. Every item in Direct Quotes and
Statistics and Data must be accounted for here.)

## Sources Visited
(Plain list of every URL opened, one per line. Stages 7 and 8 use it to check citations.)
```

Tool tags to use: `Web search`, `Web fetch`, `Research`, or `Attached file`.

---

## Operating Procedure

Run the phases in order. If one tool or one page fails, note it and continue. The bundle must still be produced from whatever succeeded.

### Phase A: Plan the Research Questions

1. Derive 4-8 research questions from the topic, the Research/Notes column and any attached files.
2. For each question, note the claim type: platform/algorithm (needs recency) or market/enrollment/demographic (needs authority). The source policy treats them differently.
3. For each question, name the Tier 1 source most likely to answer it. Examples: NCES for enrollment counts, NAIS for independent school trends, EdChoice for school choice data, Google Business Profile Help for how reviews affect local ranking.

### Phase B: Broad Discovery (Research or Web Search)

**If Research is available,** run it once with the steering prompt at the bottom of this file, with `[TOPIC]` replaced by the topic. Treat its report as a list of leads. Do not copy its numbers into the bundle until Phase D confirms them.

**If Research is not available,** or to fill gaps it left, run web searches for each research question:

* Write queries that describe the ideal Tier 1 page, not just keywords. Examples:
  * "NAIS research independent school enrollment trends tuition"
  * "NCES Private School Universe Survey enrollment by region"
  * "Google Business Profile help how reviews affect local ranking"
* Add the organization's name to the query when you want a specific Tier 1 source (for example "nces.ed.gov private school enrollment").
* For platform and algorithm claims, add the current year to the query and prefer official documentation.
* For market and enrollment claims, do not chase recency. Let authority win.
* Discard any result from a domain in `reference/k-12-private-school-competitors.md`, and anything that reads as a content farm.

### Phase C: Targeted Search and Full-Page Reads

1. For each research question that still lacks a strong Tier 1 source, run more targeted searches. Try the stat's likely original publisher, the report's title, or the survey name.
2. For recent developments (platform changes, policy news, announcements from the past 90 days), search news coverage and then trace each story to the primary source it cites.
3. Use **web fetch** on every page you intend to cite. Read the full page. Do not trust a search snippet or a Research summary for a statistic or a quote.
4. When a Tier 2 page restates a statistic, trace it to the original and cite the original instead.
5. When you fetch a page for a platform claim, check its publish or update date. Prefer pages from the last 18 months. An older platform page needs a note in Verification Notes saying why it still holds.

### Phase D: Merge and Dedupe

1. Combine everything into the required section structure.
2. Dedupe. When two sources give the same statistic, keep one entry and note the other as corroboration in Verification Notes. When two sources conflict, keep both and flag the conflict.
3. Preserve every direct quote and statistic verbatim. Do not paraphrase.
4. Tag each quote and statistic with `[tool · tier]` so the fact-check and later stages know where it came from.
5. Drop anything from an excluded domain that slipped through.

### Phase E: Fact-Check Gate

This is the quality gate. Nothing leaves Stage 0 unverified and unflagged.

1. **Verify every entry** in `## Direct Quotes` and `## Statistics and Data`. Use web fetch to open each cited URL and confirm the quote or statistic appears in the page text, word for word for quotes and figure for figure for statistics. If a bundle carries more than 40 quotes and statistics, verify the 40 that matter most, tag the rest `unverified`, and say so in Verification Notes. A bundle that large means the research went too wide.
2. If web fetch cannot open a page (paywall, block, timeout), the claim is unverified. Try another copy of the same source, such as the publisher's PDF. If none loads, tag it `unverified`.
3. Confirm each statistic carries a date, and a sample size and methodology where the source gives them.
4. Mark each confirmed item `verified`. If a quote or statistic cannot be confirmed on its page:
   * Trace the citation chain to find the original source for the same claim.
   * If you find it and it confirms the claim, swap in that source.
   * If not, drop the item, or move it down and tag it `unverified`. Never let an unverified statistic sit in the bundle unflagged.
5. Confirm no cited domain is on the exclude list.
6. Write the result of every check into `## Verification Notes`: counts verified vs. dropped, swaps made, conflicts, and low-confidence flags.

A bundle that reaches Stage 1 must be one where every kept quote and statistic was confirmed against its source, or is clearly flagged. Private school administrators cross-check statistics. This gate is why the content holds up.

### Why Every AI-Sourced Number Gets Re-Checked

AI research reports, including Claude's own Research feature, are excellent for finding leads, story angles and sources you would not have searched for. They are not proof. In production use of this pipeline, about 30% of the unique numbers and named claims in AI deep-research reports failed verification. Failures included invented statistics, a journal citation that did not exist, made-up named-school case studies, findings reported backwards, and statistics passed through aggregator blogs that had lost the original source. Treat every number in a Research report as a lead until Phase E confirms it at the primary source.

---

## Gate Before Stage 1

Do not start Stage 1 until the bundle passes all of these:

* `research/[topic-slug]-research.md` exists.
* It contains both `## Direct Quotes` and `## Statistics and Data`, and each holds real, sourced entries. A bundle with empty sections, placeholder text or only a few thin lines is a fail.
* Phase E ran, and its results are written in `## Verification Notes`.

If the gate fails, say so in the chat with the reason. In batch mode, skip that topic, note it in the chat, and move to the next row. Do not write a post on research that did not pass.

A tool that was unavailable (for example, Research turned off) does not fail the gate by itself, as long as web search and web fetch produced a passing, fact-checked bundle.

---

## Research Steering Prompt

Use this prompt for the Phase B Research run, with `[TOPIC]` replaced by the topic. You can also paste it into a separate Research chat and bring the report back as an attached file.

```
<role>

You are an expert content research specialist for a digital marketing agency that
serves private and independent K-12 schools (excluding large national school
networks). You excel at surfacing current, primary-source statistics, expert quotes,
and case studies, and at verifying every source by tracing it to its origin.

You only deliver direct expert quotes (no paraphrasing) and actionable, sourced
findings.

</role>

<task>

* Conduct thorough research on the topic I provide.
* Gather direct quotes and statistics from authoritative primary sources.
* Verify all information and make sure links are accessible and contain the
  referenced content.
* Be honest and flag anything you cannot verify.

</task>

<audience>

The finished blog post is read by administrators, heads of school, admissions and
enrollment teams, and marketing directors at private and independent K-12 schools (not
large national networks) who are deciding whether to hire a marketing agency. They are
not parents searching for a school.

Your report is read first by a brief writer, who builds the post outline from it,
and then by the post writer, who quotes and cites it. Neither one redoes your research,
so give them findings they can use as written.

</audience>

<intent>

Your findings become the fact base for a blog post published on our agency's site,
under our byline. Every statistic and quote may be cited and linked in public, so each
one must trace to a primary source a reader can open. The same facts are reused in the
post's FAQ, its title and its meta description. An error repeats in all of them.

Not wanted: general background nobody will cite, parent-facing advice on choosing a
school, undated figures, and statistics you cannot trace to their origin.

</intent>

<source_priority>

Prioritize sources in this order for private school MARKETING and enrollment topics:

1. Official platform documentation (Google Business Profile, Google Ads, Google Search
   Central, Think with Google).
2. Government and education data (National Center for Education Statistics / nces.ed.gov,
   U.S. Census, U.S. Department of Education, IPEDS, Private School Universe Survey).
3. Private school trade bodies and research (National Association of Independent Schools
   / nais.org, Independent School Management / isminc.com, EdChoice / edchoice.org,
   National Catholic Educational Association, Council for American Private Education).
4. Marketing research firms that disclose methodology (BrightLocal, Pew Research, Moz).

Academic and education-research sources are MORE useful here than in most marketing
verticals. Enrollment behavior, family decision-making and education policy have
genuine peer-reviewed and association research. Use it where it applies. For
platform and marketing-tactic claims (for example, Google Business Profile
optimization), there is no peer-reviewed literature, so prefer platform and industry
primary sources there.

For platform and algorithm claims (anything about how Google products or ad systems
behave), prefer sources from the last 18 months. These products change constantly.
For enrollment, tuition and demographic data, the most authoritative dataset wins even
if it is a year or two old.

DO NOT cite or link any competitor agency listed below under any circumstance:
[PASTE THE DOMAINS FROM reference/k-12-private-school-competitors.md HERE]

Also avoid content farms, circular "stats roundup" aggregators with no traceable
original source, undated pages making time-sensitive claims, and forum posts as a
primary statistic source.

</source_priority>

<citation_requirements>

For every piece of information:

1. Include a direct markdown link to the source: [Source Name](url)
2. Before citing, verify the link is accessible and the information actually appears on
   the page.
3. For direct quotes, use markdown blockquotes (>) and name the author or source.
4. For statistics, give the date of the data, sample size, and methodology when
   available.
5. Evaluate source credibility on Authority, Currency, Accuracy, and Purpose.
6. Flag any information you could not adequately verify.

Never cite a link without first checking that it is accessible, contains the
referenced information, and is a credible source.

</citation_requirements>

<output_format>

Use markdown. Organize your findings as:

## Topic Overview
Brief introduction to the topic and key aspects of your research.

## Direct Quotes
For each: blockquote, then (Source: Author/Speaker; Year, [Source Name](url))

## Statistics and Data
For each: the statistic, then (Source: Organization, Title; Year, [Source Name](url)),
then **Methodology:** sample size and data collection when available.

## Academic Research
For each: key finding, full citation (Author(s) (Year). Title. Journal, Volume(Issue),
Pages. DOI), journal link, and methodology when available.

## Additional Resources
Markdown list of valuable further-reading sources with proper links.

## Verification Notes
Notes on source verification, limitations, or conflicting information.

</output_format>

The topic: [TOPIC]
```

Before you run it, replace the competitor placeholder with the current domains from `reference/k-12-private-school-competitors.md`.

---

## Project Rules Still Apply

Stage 0 writes only the research bundle. Do not change `output/`, `instructions/`, `reference/` or anything else outside `research/`.

Project rules from `CLAUDE.md` apply. The audience is private school administrators, admissions teams and marketing directors evaluating whether to hire a marketing agency, not parents searching for schools. Use AP style. Em dashes are capped at 1 per 300 words of body copy. No prohibited phrases. If a CMS comes up, position [YOUR_CMS] over [ALTERNATIVE_CMS]. Stage 0 does not write prose, but any heading or transition you write while you reformat findings must follow these rules too.
