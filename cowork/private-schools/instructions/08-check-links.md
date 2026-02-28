# Stage 8: Link Checking

## Purpose
Final verification pass before publishing. Test every link in the blog post — internal and external — to confirm they are working, pointing to the right destination, and still contain the cited content. Fix what can be fixed. Flag what cannot.

This is the last stage in the pipeline. After Stage 8, the draft should be publication-ready.

**Stage 8 is an independent verification — not a rubber stamp of Stage 7.** Re-verify every external citation from scratch using the same tiered system. If Stage 7 marked something as verified but this stage cannot confirm it, flag the discrepancy.

---

## Process

### Step 1: Extract All Links
Compile every URL in the document:
- Internal links (yoursite.com)
- External citation and source links
- CTA links (contact page)
- The who-we-serve link from the introduction
- Any other embedded links

### Step 2: Test Each Link
For each URL, use web_fetch to attempt to load the page and check:
- **Does the page load?** (HTTP 200)
- **Is there a redirect?** (301/302 — note the final destination)
- **Is it broken?** (404, 500, timeout)
- **Is the page behind a paywall or login?**

If a link times out, try at least twice before marking it as broken.

### Step 3: Tiered Content Verification (External Links — Independent Re-Verification)
For every external citation, perform a full independent verification using the same three-tier system from Stage 7. Do NOT rely on Stage 7's findings — verify each claim yourself by fetching the source page and searching for the cited data.

#### Tier 1: Exact Match (Preferred)
The exact number, data point, or quote in the draft appears on the source page in the correct context.
- **Result:** ✅ Verified — Exact

#### Tier 2: Supported Paraphrase (Acceptable with Guardrails)
The draft uses a paraphrased or rounded version of the data, but the source contains the underlying number that supports it.
- **Result:** ✅ Verified — Paraphrased

**Tier 2 Guardrails (same as Stage 7):**
- The paraphrase cannot change the direction of the data
- Rounded numbers must round honestly
- Dollar amounts must stay exact
- Named study results and specific findings must stay exact
- Direct quotes must be verbatim
- If the paraphrase violates any guardrail, correct the draft text

#### Tier 3: Unsupported (Must Fix or Remove)
The source page does not contain data that supports the claim as written.
- **Result:** Find a new source, correct the draft, or remove the statistic

### Step 4: Cross-Check Against Stage 7
After completing your independent verification, compare your findings to Stage 7's External Link Verification table:
- If Stage 7 marked a citation ✅ Verified but you cannot confirm the data on the page → flag as 🚩 Discrepancy
- If Stage 7 marked something as 🔄 Replaced and the replacement link works and contains the data → confirm as ✅ Working
- If Stage 7 removed a statistic (🗑️) and the surrounding sentence reads naturally → confirm as acceptable
- If Stage 7 missed a citation entirely → verify it now and add to the report

### Step 5: Fix Issues
Apply fixes directly — do not present for review.

**Broken External Links:**
1. Search for the source's updated URL
2. Check if the content moved to a new page
3. Check for an archived version (Wayback Machine)
4. If no fix is found, find an alternative source from the approved tiers in Stage 7
5. If no alternative exists, remove the citation and adjust the surrounding sentence to read naturally

**Redirect Chains:**
- Update the link to the final destination URL
- Do not leave links that redirect multiple times

**Paywalled Content:**
- Verify the cited statistic is visible in the free preview
- If not visible without login, find an alternative open-access source
- If no alternative exists, remove the citation and adjust the sentence

**Outdated Content:**
- If the source page has been significantly updated, verify the cited data still appears
- If the data has been revised, update the citation in the blog post to reflect current data
- If the data has been removed, find an alternative source or remove the citation

**Broken Internal Links:**
- Check if the page exists at a different URL on yoursite.com
- If the page was removed or moved, remove the link but keep the anchor text as plain text
- Flag for the user so they can decide if the page needs to be recreated

---

## When Replacing Citations

When a broken or outdated source must be replaced with a new one, follow these rules:

### Verification Before Inserting
- Use web_fetch to confirm the replacement URL is live
- Search the fetched content to confirm it contains the EXACT statistic being cited
- If the statistic does not appear on the page, do NOT use that source — find another
- Never insert a citation without personally verifying the link works and contains the data

### Citation Format
When inserting a replacement citation, follow the 5-format rotation system in `reference/citation-formats.md`. Match the format of the citation being replaced when possible. If the surrounding section already uses a particular format, use a different one for variety.

### Rules
- Follow all citation rules in `reference/citation-formats.md`
- Limit "According to" to no more than 10% of all citations in the post
- Present statistics in the most reader-friendly format for the context

### Topic Relevance
Replacement statistics must be directly relevant to the post's topic. Before inserting a replacement, confirm:
- The statistic directly supports the point being made in context
- The source falls within the approved tiers from Stage 7
- The data is from within the last 2-3 years when possible

---

## Status Codes

| Status | Meaning |
|--------|---------|
| ✅ Working | Page loads, content verified (Exact or Paraphrased match) |
| ⚠️ Warning | Redirects, paywall, or content may have changed |
| ❌ Broken | 404, timeout, or page removed |
| 🔄 Fixed | Was broken or problematic, now corrected |
| 🗑️ Removed | Could not fix, citation removed from draft |
| 🚩 Discrepancy | Stage 7 said verified, but Stage 8 could not confirm |

---

## Output

### Apply All Fixes
Fix every issue directly in the draft. Do not present fixes for review.

### Add Link Check Report to Bottom of Draft
After all existing content and tables (below the Stage 6 and Stage 7 tables under the `# Links` heading), add the link check report:

```
### Link Check Report

| Link | Type | Draft Claim | Source Text Found | Match Type | Status | Action Taken |
|------|------|-------------|-------------------|------------|--------|--------------|
| https://yoursite.com/contact | Internal | — | — | — | ✅ Working | None |
| https://nais.org/research/enrollment | External | 62% research online | "62% of families research schools online" | Exact | ✅ Working | None |
| https://brightlocal.com/research | External | 88% trust reviews | "88% of consumers trust online reviews" | Exact | ✅ Working | None |
| https://hubspot.com/stats | External | Email ROI $36:$1 | "$36 for every $1 spent" | Exact | ✅ Working | None |
| https://nais.org/old-report | External | 73% of parents | Not found on page | No match | 🚩 Discrepancy | Stage 7 said ✅, cannot confirm — replaced with [new URL] |
| https://example.com/deleted-page | External | Source page | — | — | 🗑️ Removed | No alternative found, citation removed |

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
- Stage 7 verifications could not be confirmed: [number]
- Citations Stage 7 missed: [number]

# Publication Status
[State whether the draft is ready to publish or if any issues need user attention before publishing]
```

### Save
Save to `output/[topic-slug]-draft.md` (overwrite the existing draft). Do not create a separate file.

---

## Pipeline Awareness
This is Stage 8, the final stage. The draft at this point should contain:
- Publishing Package at the top (from Stage 5)
- Title options and recommendations (from Stage 4)
- Full blog content with TL;DR, FAQ, and CTA (from Stages 2-3)
- `# Links` heading with:
  - Internal link table (from Stage 6)
  - External link verification table (from Stage 7)
  - Link check report (this stage)

After Stage 8, the draft is publication-ready.
