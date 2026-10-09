# Stage 8: Link Checking and Final Review

## Purpose
Final verification pass before publishing. Test every link in the blog post, internal and external, to confirm it works, points to the right destination, and still contains the cited content. Fix what can be fixed. Flag what can't. Then write the `# Publication Status` section.

This is the last stage of the pipeline (Stage 0 plus 8 content stages). After Stage 8, the draft should be ready to publish.

**Stage 8 is an independent verification, not a rubber stamp of Stage 7.** Re-verify every external citation from scratch with the same tiered system. If Stage 7 marked something verified but you can't confirm it, flag the discrepancy.

**Output feeds:** The person who runs the project publishes the post. They copy the Publishing Package fields (title, URL slug, meta description, author, keywords) into the post's settings in [YOUR_CMS], and paste the body from the TL;DR through the FAQ. Everything from `# Links` down, and the title package above the body, stays out of the published post. Add a cover image before it goes live.

**Human check:** `# Publication Status` is this stage's review step. You, in the Cowork chat (or the person who runs the project), read it before the post publishes. Put these first, above everything else in it:
- Every ❌ link that is still broken
- Every 🚩 Stage 7 discrepancy
- Every attributed quote the Stage 3 Self-Check listed under "Needs human review"
- Every dead, redirected, or not-yet-live internal destination from the Stage 6 Link Summary
- Every `⚠️ Kept` competitor link from Stage 7

Keep the heading text exactly `Publication Status`.

---

## Process

### Step 1: Extract All Links
List every URL in the document:
- Internal links ([YOUR-AGENCY-DOMAIN])
- External citation and source links
- CTA links (contact page)
- The who-we-serve link from the introduction
- Any other embedded links

### Step 2: Test Each Link
Fetch each URL and check:
- **Does the page load?** (HTTP 200)
- **Is there a redirect?** (301/302. Note the final destination.)
- **Is it broken?** (404, 500, timeout)
- **Is the page behind a paywall or login?**

If a link times out, try at least twice before you mark it broken.

### Step 3: Tiered Content Verification (External Links, Independent Re-Verification)
For every external citation, run a full, independent verification with the same three-tier system as Stage 7. Do NOT rely on Stage 7's findings. Fetch each source page and search it for the cited data yourself.

#### Tier 1: Exact Match (Preferred)
The exact number, data point, or quote in the draft appears on the source page in the correct context.
- **Result:** ✅ Verified (Exact)

#### Tier 2: Supported Paraphrase (Acceptable with Guardrails)
The draft uses a paraphrased or rounded version of the data, but the source contains the underlying number that supports it.
- **Result:** ✅ Verified (Paraphrased)

**Tier 2 guardrails (same as Stage 7):**
- The paraphrase cannot change the direction of the data
- Rounded numbers must round honestly
- Dollar amounts stay exact
- Named study results and specific findings stay exact
- Direct quotes stay verbatim
- If the paraphrase breaks any guardrail, correct the draft text

#### Tier 3: Unsupported (Must Fix or Remove)
The source page does not contain data that supports the claim as written.
- **Result:** Find a new source, correct the draft, or remove the statistic

### Step 4: Cross-Check Against Stage 7
After your independent verification, compare your findings to Stage 7's External Link Verification table:
- If Stage 7 marked a citation ✅ Verified but you can't confirm the data on the page, flag it 🚩 Discrepancy.
- If Stage 7 marked something 🔄 Replaced and the replacement link works and contains the data, confirm it ✅ Working.
- If Stage 7 removed a statistic (🗑️) and the surrounding sentence reads naturally, confirm it as acceptable.
- If Stage 7 missed a citation entirely, verify it now and add it to the report.

### Step 5: Fix Issues
Apply fixes directly. Do not present them for review.

**Broken external links:**
1. Search for the source's updated URL.
2. Check whether the content moved to a new page.
3. Check for an archived version (Wayback Machine).
4. If you find no fix, find an alternative source from the approved tiers in Stage 7.
5. If no alternative exists, remove the citation and adjust the surrounding sentence so it reads naturally.

**Redirect chains:**
- Update the link to the final destination URL.
- Do not leave links that redirect more than once.

**Paywalled content:**
- Check that the cited statistic is visible in the free preview.
- If it isn't visible without a login, find an open-access alternative.
- If no alternative exists, remove the citation and adjust the sentence.

**Outdated content:**
- If the source page has changed a lot, check that the cited data still appears.
- If the data was revised, update the citation in the post to the current data.
- If the data was removed, find an alternative source or remove the citation.

**Broken internal links:**
- Check whether the page exists at a different URL on [YOUR-AGENCY-DOMAIN].
- If the page was removed or moved, remove the link but keep the anchor text as plain text.
- Flag it for the user so they can decide whether the page needs to be rebuilt.

### Step 6: Final Self-Check on Changed Text
Stages 6, 7, and 8 can change sentences after Stage 3 checked them. Before you write the report, re-run the Stage 3 checks (`instructions/03-faq-tldr.md`, Phase 1) on every sentence that Stages 6 to 8 added or rewrote:
- No prohibited phrases (required fixes fixed, quotes kept verbatim)
- No new structure problems (bold-as-heading, horizontal rules, H4 or deeper)
- Em dashes still at 1 per 300 words or fewer in the body
- No links in the TL;DR

Then update the counts and the **Overall** line in the `## Stage 3 Self-Check` block if anything changed. If Overall is FAIL, fix the open items before you finish.

---

## When Replacing Citations

When you must replace a broken or outdated source, follow these rules.

### Verify Before You Insert
- Fetch the replacement URL and confirm it is live.
- Search the fetched content for the EXACT statistic you are citing.
- If the statistic is not on the page, do NOT use that source. Find another.
- Never insert a citation without personally confirming the link works and contains the data.

### Citation Format
When you insert a replacement citation, follow the 5-format rotation in `reference/citation-formats.md`. Match the format of the citation you are replacing when you can. If the section already uses that format, pick a different one for variety.

### Rules
- Follow every citation rule in `reference/citation-formats.md`
- Use "According to" for no more than 10% of all citations in the post
- Present statistics in the most reader-friendly format for the context

### Topic Relevance
A replacement statistic must be directly relevant to the post's topic. Before you insert it, confirm:
- The statistic supports the point being made in that spot
- The source falls in the approved tiers from Stage 7
- The data is from the last 2 to 3 years when possible

---

## Status Codes

| Status | Meaning |
|--------|---------|
| ✅ Working | Page loads, content verified (Exact or Paraphrased match) |
| ⚠️ Warning | Redirects, paywall, or content may have changed |
| ❌ Broken | 404, timeout, or page removed |
| 🔄 Fixed | Was broken or wrong, now corrected |
| 🗑️ Removed | Could not fix, citation removed from draft |
| 🚩 Discrepancy | Stage 7 said verified, but Stage 8 could not confirm |

---

## Output

### Apply All Fixes
Fix every issue directly in the draft. Do not present fixes for review.

### Add the Link Check Report Under `# Links`
Below the Stage 6 and Stage 7 tables under the `# Links` heading, add the link check report. Then add `# Publication Status` as the last section of the file.

```
### Link Check Report

| Link | Type | Draft Claim | Source Text Found | Match Type | Status | Action Taken |
|------|------|-------------|-------------------|------------|--------|--------------|
| https://[YOUR-AGENCY-DOMAIN]/contact | Internal | n/a | n/a | n/a | ✅ Working | None |
| https://nais.org/research/enrollment | External | 62% research online | "62% of families research schools online" | Exact | ✅ Working | None |
| https://brightlocal.com/research | External | 88% trust reviews | "88% of consumers trust online reviews" | Exact | ✅ Working | None |
| https://hubspot.com/stats | External | Email ROI $36:$1 | "$36 for every $1 spent" | Exact | ✅ Working | None |
| https://nais.org/old-report | External | 73% of parents | Not found on page | No match | 🚩 Discrepancy | Stage 7 said ✅, cannot confirm. Replaced with [new URL] |
| https://example.com/deleted-page | External | Source page | n/a | n/a | 🗑️ Removed | No alternative found, citation removed |

#### Link Check Summary
- Total links checked: [number]
- ✅ Working (verified): [number]
  - Exact matches: [number]
  - Supported paraphrases: [number]
- 🔄 Fixed: [number]
- ⚠️ Warnings: [number]
- 🗑️ Removed: [number]
- 🚩 Discrepancies with Stage 7: [number]
- ❌ Still broken (needs user attention): [number]

#### Stage 7 Cross-Check
- Stage 7 verifications confirmed: [number]
- Stage 7 verifications that could not be confirmed: [number]
- Citations Stage 7 missed: [number]

# Publication Status
**Ready to publish:** [Yes / No, with the reason]

**Needs your attention before publishing:**
- [Each ❌ still-broken link]
- [Each 🚩 Stage 7 discrepancy]
- [Each attributed quote from the Stage 3 Self-Check "Needs human review" list]
- [Each dead, redirected, or not-yet-live internal destination from Stage 6]
- [Each ⚠️ Kept competitor link from Stage 7, with its reason]
- [Write "None" if the list is empty]

**Final Self-Check:** [PASS / WARN, from the updated Stage 3 Self-Check block]

**To publish:** Copy the Publishing Package fields into [YOUR_CMS], paste the body from the TL;DR through the FAQ, leave out everything under `# Links`, and add the cover image.
```

### Save
Save to `output/[topic-slug]-draft.md` (overwrite the existing draft). Do not create a separate file.

---

## Pipeline Awareness
This is Stage 8, the final stage. The draft at this point should contain:
- The Publishing Package at the top (from Stage 5)
- Title options and recommendations (from Stage 4)
- The full blog content with TL;DR, FAQ, and CTA (from Stages 2 and 3)
- The `# Links` heading with:
  - The Stage 3 Self-Check block (updated in Step 6)
  - The internal link table (from Stage 6)
  - The external link verification table (from Stage 7)
  - The link check report (this stage)
- `# Publication Status` as the last section

After Stage 8, the draft goes to the person who publishes it. In batch mode, tell the user in one line which drafts are ready and which need attention, then start the next topic.
