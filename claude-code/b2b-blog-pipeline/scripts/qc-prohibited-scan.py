#!/usr/bin/env python3
from __future__ import annotations
"""
qc-prohibited-scan.py

Scans a blog draft for prohibited phrases listed in
reference/prohibited-phrases.md. Classifies each hit as:
  - in_blockquote: line starts with `>` (markdown blockquote)
  - proper_noun: the match is an acronym or part of a real program name
  - in_url: the match is inside a URL or markdown link target
  - in_attributed_quote: between quotation marks with attribution language nearby
  - own_voice: the post's own writing — must be rewritten

Outputs JSON to stdout.

Usage:
  qc-prohibited-scan.py <draft.md> [--reference path/to/prohibited-phrases.md]

Exit codes:
  0 = scan completed (even if hits found)
  1 = file not found or parse error
  2 = invalid arguments
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path


# Attribution patterns that signal a quote is attributed to a source.
# If any of these appear within ATTRIBUTION_WINDOW chars of the quoted text,
# we classify the quote as attributed.
ATTRIBUTION_PATTERNS = [
    r'\bsaid\b',
    r'\bsays\b',
    r'\btold\b',
    r'\baccording to\b',
    r'\bas\s+(?:[A-Z][a-zA-Z\.\-\']+\s+){1,4}(?:put|noted|observed|explained|wrote|said|put it|writes)',
    r'\bput it\b',
    r'\bnoted\b',
    r'\bobserved\b',
    r'\bexplained\b',
    r'\bwrote\b',
    r'\bwrites\b',
    r'\bstated\b',
    r'\bremarked\b',
    r'\bcommented\b',
    r'\bin (?:an?|the) (?:interview|statement|report)',
]
ATTRIBUTION_RE = re.compile('|'.join(ATTRIBUTION_PATTERNS), re.IGNORECASE)
ATTRIBUTION_WINDOW = 150  # chars before/after the hit to scan for attribution


def find_project_root(start_path: Path) -> Path | None:
    """Walk up from start_path looking for reference/prohibited-phrases.md."""
    current = start_path.resolve()
    if current.is_file():
        current = current.parent
    for parent in [current] + list(current.parents):
        if (parent / 'reference' / 'prohibited-phrases.md').exists():
            return parent
    return None


TIER_RE = re.compile(r'\[(avoid|limit\s+\d+|unless sourced|needs proof|headings|with stats|residue)\]', re.IGNORECASE)


def tier_for_heading(heading: str) -> str:
    """Section tier from a marker in its heading (added 2026-09-29):
      [avoid]          -> warning only ("use only if necessary")
      [limit N]        -> warning once a draft uses the group more than N times
      [unless sourced] -> required fix unless the sentence names a source
      [needs proof]    -> warning unless the sentence or the next one carries a number,
                          a link, or a named source
      [headings]       -> checked in headings only, a warning unless the heading carries
                          a number. Body copy is ignored.
      [residue]        -> required fix, except inside quotes (example dialogue)
      [with stats]     -> warning only in a sentence that carries a number or a link:
                          use the exact figure
      (no marker)      -> required fix, the original behavior
    """
    m = TIER_RE.search(heading)
    if not m:
        return 'ban'
    return m.group(1).lower().replace('  ', ' ')


def parse_prohibited_terms(reference_path: Path) -> list[str]:
    """Extract prohibited terms from the reference file.

    Handles common formats:
      - Bullet lines with quoted comma-separated lists: - "term1", "term2"
      - Bullet lines with a single term: * term
      - Inline backtick terms: `term`
      - Plain bullets without quotes

    Skips markdown headings, code fences, and prose paragraphs.
    """
    text = reference_path.read_text(encoding='utf-8')
    terms: set[str] = set()
    in_code_fence = False
    tier = 'ban'

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith('```'):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        if line.startswith('#'):
            tier = tier_for_heading(line)
            continue
        if not line:
            continue

        # Only process lines that look like bullets or explicit term lines.
        # This avoids pulling stray quoted phrases out of prose paragraphs.
        is_bullet = bool(re.match(r'^\s*[-*+]\s', raw_line))
        if not is_bullet:
            continue

        # Strip the bullet marker.
        stripped = re.sub(r'^\s*[-*+]\s+', '', raw_line)

        # Remove parenthetical replacement hints before extracting terms.
        # e.g. `"in order to" (just use "to")` -> `"in order to"`
        # Without this, quoted words inside the hint get added to the
        # prohibited-terms list as false positives.
        term_source = re.sub(r'\s*\([^)]*\)', '', stripped).strip()

        # Find all double-quoted phrases.
        quoted = re.findall(r'"([^"]+)"', term_source)
        quoted += re.findall(r'[\u201c\u201d]([^\u201c\u201d]+)[\u201c\u201d]', term_source)
        # Single-quoted (but not apostrophes — require the quote to be at a word boundary).
        quoted += re.findall(r"(?:^|\s)'([^']+)'(?:\s|$|[,.!?])", term_source)

        if quoted:
            for q in quoted:
                cleaned = q.strip().strip('.,;:?').strip()
                if not cleaned.endswith('!'):
                    cleaned = cleaned.strip('!').strip()
                if cleaned and len(cleaned) >= 2:
                    terms.add((cleaned.lower(), tier))
        else:
            # Treat the entire bullet as a single term if it's reasonably short.
            cleaned = term_source.strip().strip('.,;:!?').strip()
            # Skip lines that are clearly prose (have sentence-ending punctuation
            # mid-line, or are very long).
            if cleaned and 2 <= len(cleaned) <= 80 and not re.search(r'[.!?]\s+[A-Z]', cleaned):
                terms.add((cleaned.lower(), tier))

    # A term listed in more than one section keeps its strictest tier.
    rank = {'ban': 0, 'residue': 1, 'unless sourced': 2, 'needs proof': 3}
    best: dict[str, str] = {}
    # [headings] terms are a separate check, so a word can be both a heading verb
    # and an [avoid] word in body copy ("delve").
    heading_terms = sorted((term, t) for term, t in terms if t == 'headings')
    terms = {(term, t) for term, t in terms if t != 'headings'}
    for term, t in terms:
        if term not in best or rank.get(t, 9) < rank.get(best[term], 9):
            best[term] = t
    return sorted(best.items()) + heading_terms


def build_term_pattern(term: str) -> re.Pattern:
    """Build a case-insensitive regex that matches the term with flexible
    whitespace/hyphenation. Matches at word boundaries."""
    # Split term by whitespace and hyphens to allow flexible separator matching.
    tokens = [t for t in re.split(r'[\s\-]+', term) if t]
    if not tokens:
        return re.compile(r'(?!x)x')  # never matches
    pattern_parts = [re.escape(t) for t in tokens]
    body = r'[\s\-]+'.join(pattern_parts)
    # Allow common suffixes (s, ed, ing) on the final token for single-word terms.
    # For multi-word phrases, require exact word-boundary match.
    if len(tokens) == 1 and len(tokens[0]) >= 4:
        # Allow optional inflection on single-word terms. Words ending in "e"
        # drop it before -ing/-ed (delve -> delving, enhance -> enhanced).
        t = tokens[0]
        if t.lower().endswith('e'):
            body = re.escape(t[:-1]) + r'(?:e|es|ed|ing|er|ely)?'
        else:
            body = body + r'(?:s|ed|ing|er|ly)?'
    # Word boundaries only where the term starts or ends with a word character,
    # so terms like "[insert" and "certainly!" still match.
    pre = r'\b' if re.match(r'\w', tokens[0]) else ''
    post = r'\b' if re.search(r'\w$', tokens[-1]) else ''
    return re.compile(pre + body + post, re.IGNORECASE)


def line_is_blockquote(line: str) -> bool:
    """Return True if the line is a markdown blockquote line."""
    return bool(re.match(r'^\s*>\s', line)) or line.strip() == '>'


def hit_is_in_attributed_quote(text: str, match_start: int, match_end: int) -> bool:
    """Determine whether the hit at [match_start:match_end] sits inside an
    attributed quote on the same paragraph.

    Rules:
      - Hit must be enclosed by quote marks within the same paragraph
        (paragraphs are separated by one or more blank lines).
      - An attribution phrase must appear within the same paragraph.
    """
    # Identify paragraph by scanning outward from the hit position for blank-line
    # boundaries. A blank line is two consecutive newlines.
    para_start = 0
    blank_before = text.rfind('\n\n', 0, match_start)
    if blank_before >= 0:
        para_start = blank_before + 2

    para_end = len(text)
    blank_after = text.find('\n\n', match_end)
    if blank_after >= 0:
        para_end = blank_after

    paragraph = text[para_start:para_end]
    hit_in_para_start = match_start - para_start
    hit_in_para_end = match_end - para_start

    if hit_in_para_start < 0 or hit_in_para_end > len(paragraph):
        return False

    # Find quoted spans within the paragraph by pairing quote marks.
    quote_chars = {'"', '\u201c', '\u201d'}
    spans: list[tuple[int, int]] = []
    open_pos = -1
    for idx, ch in enumerate(paragraph):
        if ch in quote_chars:
            if open_pos < 0:
                open_pos = idx
            else:
                spans.append((open_pos, idx))
                open_pos = -1

    # Hit must fall inside one of those spans.
    inside_quote = any(start < hit_in_para_start and hit_in_para_end <= end
                       for start, end in spans)
    if not inside_quote:
        return False

    # And the paragraph must contain an attribution phrase.
    return bool(ATTRIBUTION_RE.search(paragraph))


# Proper-noun exception. A banned word can also be the legal name of a real program,
# and renaming a real program is a factual error, not a style fix. Maryland's
# "Broadening Options and Opportunities for Students Today" is BOOST; it read as 4
# hard FIX hits on the October 2026 Financial Aid pillar. State scholarship programs
# collide with this list often, so exempt them structurally instead of one at a time.
#
# Two narrow rules, both requiring the ORIGINAL casing to differ from prose:
#   1. The matched text is an all-caps acronym of 3+ characters (BOOST, GROW, ESA).
#   2. The matched text is capitalized AND is followed by a program-noun within a few
#      words (Program, Scholarship, Act, Fund, Grant, Account, Initiative, Tax Credit),
#      with every intervening word capitalized. That is a proper name, not the post's own voice.
PROGRAM_NOUNS = (
    'Program', 'Programs', 'Scholarship', 'Scholarships', 'Act', 'Fund', 'Grant',
    'Grants', 'Account', 'Accounts', 'Initiative', 'Credit', 'Credits', 'Award',
    'Awards', 'Trust', 'Voucher', 'Vouchers',
)
PROPER_NAME_LOOKAHEAD = 5  # words


def hit_is_proper_noun(text: str, match_start: int, match_end: int) -> bool:
    """Return True if the matched text is part of a proper name, not the post's own voice."""
    matched = text[match_start:match_end]

    # Rule 1: all-caps acronym.
    if len(matched) >= 3 and matched.isupper() and matched.isalpha():
        return True

    # Rule 2: capitalized word leading into a program noun, all words capitalized.
    if not matched[:1].isupper():
        return False
    tail = text[match_end:match_end + 120]
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", tail)[:PROPER_NAME_LOOKAHEAD]
    for w in words:
        if w in PROGRAM_NOUNS:
            return True
        # A lowercase word breaks the proper-name run. Small connectors are allowed
        # because real program names contain them ("Opportunities for Students").
        if w[:1].islower() and w.lower() not in ('for', 'of', 'and', 'the', 'to'):
            return False
    return False


# A banned word inside a URL is part of an address, not the post's own voice. Rewording it would
# break the link, for example /blog/local-seo/why-review-sites-are-crucial-for-small-firms.
URL_RE = re.compile(r'https?://\S+|\]\([^)]+\)|/[a-z0-9]+(?:[/-][a-z0-9]+)+')


def hit_is_in_url(text: str, match_start: int, match_end: int) -> bool:
    """Return True if the match sits inside a URL or a markdown link target."""
    window_start = max(0, match_start - 400)
    window = text[window_start:match_end + 400]
    for m in URL_RE.finditer(window):
        if m.start() + window_start <= match_start and match_end <= m.end() + window_start:
            return True
    return False


def hit_is_in_quoted_table_cell(line: str, line_start: int,
                                match_start: int, match_end: int) -> bool:
    """Return True if the match sits inside a quoted span in a markdown table row.

    Stage 7 and Stage 8 verification tables carry a source's verbatim words in one column and
    the attribution in another. hit_is_in_attributed_quote() looks for attribution language in
    the same paragraph and misses that layout, which is why the same quote could pass in one
    table and fail in another. Recorded as a known miss in the September 2026 batch.
    """
    if not line.lstrip().startswith('|'):
        return False
    rel_start = match_start - line_start
    rel_end = match_end - line_start
    if rel_start < 0 or rel_end > len(line):
        return False
    quote_chars = {'"', '\u201c', '\u201d'}
    spans, open_at = [], None
    for i, ch in enumerate(line):
        if ch in quote_chars:
            if open_at is None:
                open_at = i
            else:
                spans.append((open_at, i))
                open_at = None
    return any(a < rel_start and rel_end <= b for a, b in spans)


# A banned word can be part of the real, published title of a post we cite. Rewording it
# misquotes the source: a cited post titled "Why Review Sites Are Crucial for Small Firms"
# would otherwise read as the post's own voice. Only title-case link text qualifies, so ordinary prose inside a link
# still fails.
MD_LINK_RE = re.compile(r'\[([^\]]+)\]\(')
TITLE_CASE_MINOR = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'of', 'on', 'or',
                    'the', 'to', 'with', 'is', 'are', 'that'}


def hit_is_in_cited_title(text: str, match_start: int, match_end: int) -> bool:
    """Return True if the match sits inside title-case markdown link text."""
    if not text[match_start:match_start + 1].isupper():
        return False
    window_start = max(0, match_start - 300)
    for m in MD_LINK_RE.finditer(text[window_start:match_end + 300]):
        a = m.start(1) + window_start
        b = m.end(1) + window_start
        if not (a <= match_start and match_end <= b):
            continue
        words = re.findall(r"[A-Za-z][A-Za-z'\-]*", text[a:b])
        if len(words) < 3:
            return False
        major = [w for w in words if w.lower() not in TITLE_CASE_MINOR]
        if not major:
            return False
        capped = sum(1 for w in major if w[:1].isupper())
        return capped / len(major) >= 0.8
    return False


def classify_hit(draft_text: str, lines: list[str], line_idx: int,
                  match_start_in_doc: int, match_end_in_doc: int,
                  line_start_in_doc: int = 0) -> str:
    """Classify a hit by its surrounding context."""
    line = lines[line_idx]
    if line_is_blockquote(line):
        return 'in_blockquote'
    if hit_is_in_url(draft_text, match_start_in_doc, match_end_in_doc):
        return 'in_url'
    if draft_text[match_start_in_doc:match_start_in_doc + 1] == '[':
        close = draft_text.find(']', match_start_in_doc)
        if close != -1 and draft_text[close + 1:close + 2] == '(':
            return 'link_text'
        # A bracket inside quotes is an example query, not a leftover placeholder:
        # "plumber near [your city]".
        before = line[:match_start_in_doc - line_start_in_doc]
        if before.count('"') % 2 == 1 or before.count('\u201c') > before.count('\u201d'):
            return 'example_query'
    if hit_is_in_quoted_table_cell(line, line_start_in_doc,
                                   match_start_in_doc, match_end_in_doc):
        return 'in_attributed_quote'
    if hit_is_in_attributed_quote(draft_text, match_start_in_doc, match_end_in_doc):
        return 'in_attributed_quote'
    if hit_is_proper_noun(draft_text, match_start_in_doc, match_end_in_doc):
        return 'proper_noun'
    if hit_is_in_cited_title(draft_text, match_start_in_doc, match_end_in_doc):
        return 'cited_title'
    return 'own_voice'


def section_heading_for_line(lines: list[str], line_idx: int) -> str:
    """Find the most recent markdown heading at or above line_idx."""
    for i in range(line_idx, -1, -1):
        line = lines[i]
        m = re.match(r'^(#{1,3})\s+(.+?)\s*$', line)
        if m:
            return m.group(2).strip()
    return '(top of document)'


def strip_qc_report(text: str) -> str:
    """Strip any existing auto-generated QC report block from the draft.
    This makes re-runs idempotent — the scanner never sees its own output."""
    return re.sub(
        r'\n*##?#?\s+Stage\s+3\s+QC\s+Report\s+\(auto-generated by qc.sh\).*',
        '',
        text,
        flags=re.DOTALL,
    )


SOURCE_RE = re.compile(
    r'\bin\s+(?:a|an|the|its|their)\s+(?:\d{4}\s+)?(?:[A-Z][\w&.\-]*\s*){1,6}(?:survey|study|report|analysis|census|poll)'
    r'|\baccording to\s+(?:the\s+)?[A-Z]'
    r'|\b(?:19|20)\d{2}\b.*\b[A-Z]{2,}\b'
    r'|\]\(https?://'
    r"|\b(?!(?:Recent|New|Some|Most|More|Industry|Our|This|The|Other|Current|Past|Much)\b)[A-Z][\w&.\-]*(?:['\u2019]s)?\s+(?:[a-z]+\s+){0,2}(?:research|study|studies|survey|data|analysis|report)\s+(?:shows|show|suggests|found|finds)", re.UNICODE)
EMOJI_RE = re.compile('[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2B55\u2705\u274C\u2714\u2728]')


def sentence_around(text: str, start: int, end: int) -> str:
    a = max(text.rfind('. ', 0, start), text.rfind('\n', 0, start)) + 1
    ends = [i for i in (text.find('. ', end), text.find('\n', end)) if i != -1]
    b = min(ends) if ends else len(text)
    return text[a:b]


def proof_nearby(text: str, start: int, end: int) -> bool:
    """True when the claim's sentence or the next sentence holds a number, a link, or a source."""
    a = max(text.rfind('. ', 0, start), text.rfind('\n', 0, start)) + 1
    b = end
    for _ in range(2):  # the end of this sentence, then the end of the next one
        ends = [i for i in (text.find('. ', b), text.find('\n', b)) if i != -1]
        if not ends:
            b = len(text)
            break
        b = min(ends) + 1
    window = text[a:b]
    return bool(re.search(r'\d', window) or '](' in window or SOURCE_RE.search(window))


def scan_draft(draft_path: Path, terms: list[str]) -> dict:
    """Scan the draft for each term and return structured results."""
    text = strip_qc_report(draft_path.read_text(encoding='utf-8'))
    lines = text.splitlines()

    # Pre-compute line start offsets for fast line lookup from char offset.
    line_offsets = [0]
    for line in lines:
        line_offsets.append(line_offsets[-1] + len(line) + 1)  # +1 for newline

    def line_of_offset(offset: int) -> int:
        # Binary search would be faster, but drafts are short.
        for i in range(len(line_offsets) - 1):
            if line_offsets[i] <= offset < line_offsets[i + 1]:
                return i
        return len(lines) - 1

    hits = []
    # '# Links' onward is pipeline scaffolding (link tables, stage notes). It never ships.
    _links = re.search(r'^#\s+Links\s*$', text, re.M)
    scan_end = _links.start() if _links else len(text)
    for term, tier in terms:
        pattern = build_term_pattern(term)
        for m in pattern.finditer(text, 0, scan_end):
            line_idx = line_of_offset(m.start())
            classification = classify_hit(text, lines, line_idx, m.start(), m.end(),
                                          line_offsets[line_idx])
            if tier == 'headings':
                line_here = lines[line_idx] if line_idx < len(lines) else ''
                if not line_here.lstrip().startswith('#'):
                    continue
                if classification == 'own_voice':
                    classification = 'heading_verb_ok' if re.search(r'\d', line_here) \
                        else 'heading_verb'
            if tier == 'with stats':
                sent = sentence_around(text, m.start(), m.end())
                before = text[max(0, m.start() - 4):m.start()].lower()
                no_years = re.sub(r'\b(?:19|20)\d{2}\b', '', sent)  # a year alone isn't a stat
                if not (re.search(r'\d', no_years) or '](' in sent) or before.endswith(('the ', 'at ', 'how ')):
                    continue
                if classification == 'own_voice':
                    classification = 'vague_quantity'
            if classification == 'own_voice' and tier == 'residue':
                q_before = text[line_offsets[line_idx]:m.start()]
                if q_before.count('"') % 2 == 1 or q_before.count('\u201c') > q_before.count('\u201d'):
                    classification = 'example_dialogue'
            if classification == 'own_voice' and tier == 'unless sourced' \
                    and SOURCE_RE.search(sentence_around(text, m.start(), m.end())):
                classification = 'sourced'
            elif classification == 'own_voice' and tier == 'needs proof':
                classification = 'claim_proven' if proof_nearby(text, m.start(), m.end()) \
                    else 'claim_unproven'
            hits.append({
                'term': term,
                'tier': tier,
                'matched_text': m.group(0),
                'line_number': line_idx + 1,
                'line_text': lines[line_idx].strip() if line_idx < len(lines) else '',
                'section': section_heading_for_line(lines, line_idx),
                'classification': classification,
            })

    # [limit N]: the first N uses are fine; each one past N becomes a warning.
    limit_used: dict[str, int] = {}
    for h in hits:
        if h['classification'] == 'own_voice' and h['tier'].startswith('limit'):
            n = int(h['tier'].split()[1])
            limit_used[h['tier']] = limit_used.get(h['tier'], 0) + 1
            h['classification'] = 'limit_ok' if limit_used[h['tier']] <= n else 'limit_exceeded'
        elif h['classification'] == 'own_voice' and h['tier'] == 'avoid':
            h['classification'] = 'avoid'

    # Emoji: copy only. The '# Links' block is pipeline scaffolding (link-check and
    # verification tables use check marks) and never ships.
    links_at = next((i for i, l in enumerate(lines) if re.match(r'^#\s+Links\s*$', l)), len(lines))
    for idx, line in enumerate(lines[:links_at]):
        for m in EMOJI_RE.finditer(line):
            hits.append({'term': 'emoji', 'tier': 'avoid', 'matched_text': m.group(0),
                         'line_number': idx + 1, 'line_text': line.strip(),
                         'section': section_heading_for_line(lines, idx), 'classification': 'emoji'})

    summary = {
        'total_terms_scanned': len(terms),
        'total_hits': len(hits),
        # Required fixes: banned terms, and [unless sourced] terms with no named source.
        'own_voice_hits': sum(1 for h in hits if h['classification'] == 'own_voice'),
        # Warnings (added 2026-09-29): never fail a draft on their own.
        'avoid_hits': sum(1 for h in hits if h['classification'] == 'avoid'),
        'limit_exceeded_hits': sum(1 for h in hits if h['classification'] == 'limit_exceeded'),
        'emoji_hits': sum(1 for h in hits if h['classification'] == 'emoji'),
        'sourced_hits': sum(1 for h in hits if h['classification'] == 'sourced'),
        'unproven_claim_hits': sum(1 for h in hits if h['classification'] == 'claim_unproven'),
        'proven_claim_hits': sum(1 for h in hits if h['classification'] == 'claim_proven'),
        'heading_verb_hits': sum(1 for h in hits if h['classification'] == 'heading_verb'),
        'vague_quantity_hits': sum(1 for h in hits if h['classification'] == 'vague_quantity'),
        'blockquote_hits': sum(1 for h in hits if h['classification'] == 'in_blockquote'),
        'attributed_quote_hits': sum(1 for h in hits if h['classification'] == 'in_attributed_quote'),
        'proper_noun_hits': sum(1 for h in hits if h['classification'] == 'proper_noun'),
        'url_hits': sum(1 for h in hits if h['classification'] == 'in_url'),
        'cited_title_hits': sum(1 for h in hits if h['classification'] == 'cited_title'),
    }

    return {
        'draft_path': str(draft_path),
        'reference_terms_count': len(terms),
        'summary': summary,
        'hits': hits,
    }


def main():
    parser = argparse.ArgumentParser(description='Scan a draft for prohibited phrases.')
    parser.add_argument('draft', type=Path, help='Path to the draft markdown file.')
    parser.add_argument('--reference', type=Path, default=None,
                        help='Path to prohibited-phrases.md. Auto-discovered if not provided.')
    args = parser.parse_args()

    if not args.draft.exists():
        print(json.dumps({'error': f'Draft not found: {args.draft}'}), file=sys.stderr)
        sys.exit(1)

    reference_path = args.reference
    if reference_path is None:
        root = find_project_root(args.draft)
        if root is None:
            print(json.dumps({
                'error': 'Could not auto-discover reference/prohibited-phrases.md. '
                         'Pass --reference explicitly.'
            }), file=sys.stderr)
            sys.exit(1)
        reference_path = root / 'reference' / 'prohibited-phrases.md'

    if not reference_path.exists():
        print(json.dumps({'error': f'Reference file not found: {reference_path}'}), file=sys.stderr)
        sys.exit(1)

    try:
        terms = parse_prohibited_terms(reference_path)
        result = scan_draft(args.draft, terms)
        result['reference_path'] = str(reference_path)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(json.dumps({'error': f'{type(e).__name__}: {e}'}), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
