#!/usr/bin/env python3
"""Make a cover for every blog draft, using its Recommended Titles.

For each output/<date>-<slug>-draft.md:
  1. try the H1 SEO title (Stage 4 writes it at 55 chars or less; a colon marks the sub)
  2. if it can't fit at the size floor, fall back to the H2 article title
  3. then to the H3 image title (80-150 chars, rarely fits)
Run by blog-pipeline.sh Stage 10 with --only <slug>; a single-slug run merges into the day's batch file.
Writes covers to cover-generator/output/<date>-<slug>/ and a batch summary to
cover-generator/output/batch-<YYYY-MM-DD>.json.

Usage (from cover-generator/): python3 scripts/covers_from_drafts.py [--only SLUG ...]
"""
import argparse, datetime, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAFTS = ROOT.parent / 'output'


def titles(md):
    """H1/H2/H3 under '## Recommended Titles', with the '(NN)' character counts removed."""
    block = md.split('## Recommended Titles', 1)
    if len(block) < 2:
        return {}
    out = {}
    for line in block[1].splitlines():
        m = re.match(r'^(#{1,3}) (.+)$', line)
        if m:
            lvl = len(m.group(1))
            if lvl in out:
                break
            out[lvl] = re.sub(r'\s*\(\d+\)\s*$', '', m.group(2)).strip()
        if all(k in out for k in (1, 2, 3)):
            break
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*')
    a = ap.parse_args()
    results = []
    # Finished posts live in ../posts/<date>-<slug>/ (collect-post.py). Re-make one
    # only when it's named with --only, so a bulk run doesn't redo every finished cover.
    drafts = sorted(DRAFTS.glob('*draft.md'))
    if a.only:
        drafts += sorted((ROOT.parent / 'posts').glob('*/*draft.md'))
    for f in drafts:
        m = re.search(r'(20\d\d-\d\d-\d\d)-(.+?)-draft\.md$', f.name)
        if not m:
            continue
        date, slug = m.groups()
        if a.only and slug not in a.only:
            continue
        t = titles(f.read_text())
        row = {'date': date, 'slug': slug, 'draft': f.name, 'used': None, 'title': None, 'tried': []}
        for lvl, label in ((1, 'SEO title (H1)'), (2, 'article title (H2)'), (3, 'image title (H3)')):
            if lvl not in t:
                continue
            r = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'make_cover.py'), '--title', t[lvl],
                                '--slug', slug, '--date', date], capture_output=True, text=True, cwd=ROOT)
            row['tried'].append(label)
            if r.returncode == 0:
                row.update(used=label, title=t[lvl], log=r.stdout.strip())
                break
        print(f"{date} {slug:55} {row['used'] or 'FAILED'}")
        results.append(row)
    out = ROOT / 'output' / f'batch-{datetime.date.today()}.json'
    if a.only and out.exists():                      # merge single-post runs into the day's file
        keep = [r for r in json.loads(out.read_text()) if r['slug'] not in {x['slug'] for x in results}]
        results = keep + results
    out.write_text(json.dumps(results, indent=2))
    ok = sum(1 for r in results if r['used'])
    print(f'{ok}/{len(results)} covers made -> {out.relative_to(ROOT)}')
    if a.only and not all(r['used'] for r in results if r['slug'] in a.only):
        sys.exit(1)


if __name__ == '__main__':
    main()
