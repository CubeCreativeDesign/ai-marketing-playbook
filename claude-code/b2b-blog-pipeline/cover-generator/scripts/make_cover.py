#!/usr/bin/env python3
"""Set a blog title onto a cover template and export SVG, PNG and WebP.

Usage (run from cover-generator/):
  python3 scripts/make_cover.py --title "Win More Bids|With Better Proposals: A Field Guide" \
      --slug better-proposals --date 2026-11-04 [--layout band] [--color primary] [--topic "..."]

Title rules (RULES.md):
  * the sub is everything after the first colon; a colon between digits ("5:15") is not a split
  * '::' puts the small text on top and the big text below (layouts with a "reverse" block set)
  * no colon -> the script picks a split and reports it
  * "|" is a suggested line break; the script keeps it unless a line overflows or the lines are badly unbalanced
  * "A vs B" titles use the vs layout (side A left, side B right, no sub)

Text is drawn as outlined glyph paths, so the SVG renders the same with no fonts installed.
Outputs go to output/<date>-<slug>/ (or posts/<date>-<slug>/ when that folder exists):
  <slug>.svg, <slug>-master.png (3840x2160), fulltext-<slug>.png/.webp (1920x1080),
  intro-<slug>-sm.png/.webp (960x540), report.json.

Needs: python3 + fontTools, and the resvg and cwebp command-line tools. See README.md.
"""
import argparse, hashlib, itertools, json, pathlib, re, shutil, struct, subprocess, sys
import xml.etree.ElementTree as ET

try:
    from fontTools.ttLib import TTFont
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
except ImportError:
    sys.exit('fontTools is missing. Install it with: python3 -m pip install fonttools')

ROOT = pathlib.Path(__file__).resolve().parent.parent
W, H = 1920, 1080
WEAK = {'a', 'an', 'the', 'for', 'to', 'of', 'and', 'or', 'in', 'on', 'at', 'by', 'with', 'your', 'our', 'my', 'is', 'are', 'can', 'that'}


def load_json(name):
    path = ROOT / name
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        sys.exit(f'missing {path}. See README.md.')
    except ValueError as e:
        sys.exit(f'{path} is not valid JSON: {e}')


# ---------------------------------------------------------------- fonts
class Face:
    def __init__(self, font):
        self.f = font
        self.upm = font['head'].unitsPerEm
        self.cmap = font.getBestCmap()
        self.gs = font.getGlyphSet()
        self.cap = font['OS/2'].sCapHeight / self.upm
        self.kern = self._kern()

    def _kern(self):
        """Pair kerning from the kern table and GPOS (formats 1 and 2)."""
        pairs = {}
        if 'kern' in self.f:
            for t in self.f['kern'].kernTables:
                pairs.update(t.kernTable)
        if 'GPOS' in self.f:
            gpos = self.f['GPOS'].table
            idx = {i for fr in gpos.FeatureList.FeatureRecord if fr.FeatureTag == 'kern'
                   for i in fr.Feature.LookupListIndex}
            for i in idx:
                lk = gpos.LookupList.Lookup[i]
                subs = lk.SubTable
                if lk.LookupType == 9:
                    subs = [s.ExtSubTable for s in subs]
                for st in subs:
                    if getattr(st, 'Format', None) == 1 and hasattr(st, 'PairSet'):
                        for first, ps in zip(st.Coverage.glyphs, st.PairSet):
                            for pv in ps.PairValueRecord:
                                v = getattr(pv.Value1, 'XAdvance', 0) if pv.Value1 else 0
                                pairs.setdefault((first, pv.SecondGlyph), v)
                    elif getattr(st, 'Format', None) == 2 and hasattr(st, 'Class1Record'):
                        c1 = st.ClassDef1.classDefs if st.ClassDef1 else {}
                        c2 = st.ClassDef2.classDefs if st.ClassDef2 else {}
                        seconds = {}
                        for g, c in c2.items():
                            seconds.setdefault(c, []).append(g)
                        for g1 in st.Coverage.glyphs:
                            rec = st.Class1Record[c1.get(g1, 0)]
                            for k, r2 in enumerate(rec.Class2Record):
                                v = getattr(r2.Value1, 'XAdvance', 0) if r2.Value1 else 0
                                if v:
                                    for g2 in seconds.get(k, []):
                                        pairs.setdefault((g1, g2), v)
        return pairs

    def glyphs(self, s):
        return [self.cmap.get(ord(ch), self.cmap.get(ord('?'), '.notdef')) for ch in s]

    def advances(self, s, size, track):
        """x offset of each glyph plus total width, in px."""
        names = self.glyphs(s)
        sc = size / self.upm
        xs, x = [], 0.0
        for i, g in enumerate(names):
            xs.append(x)
            x += self.gs[g].width * sc
            if i + 1 < len(names):
                x += self.kern.get((g, names[i + 1]), 0) * sc + track * size
        return names, xs, x

    def width(self, s, size, track):
        return self.advances(s, size, track)[2]

    def path(self, s, size, track, x0, baseline):
        names, xs, _ = self.advances(s, size, track)
        sc = size / self.upm
        pen = SVGPathPen(self.gs)
        for g, x in zip(names, xs):
            self.gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x0 + x, baseline)))
        return pen.getCommands()


def load_faces(theme):
    faces = {}
    for role, fname in theme['fonts'].items():
        path = ROOT / 'fonts' / fname
        if not path.exists():
            sys.exit(f'font file missing: {path}. See README.md, "Fonts".')
        faces[role] = Face(TTFont(path))
    return faces


# ---------------------------------------------------------------- title parsing
def split_title(title):
    """Return (main, sub, how). Sub starts after the first colon that is not between digits.
    '::' means reverse: the front is the small text on top, the tail is the big text below."""
    if '::' in title:
        front, tail = title.split('::', 1)
        return tail.strip(), front.strip(), 'reverse'
    for m in re.finditer(r':', title):
        i = m.start()
        if 0 < i < len(title) - 1 and title[i - 1].isdigit() and title[i + 1].isdigit():
            continue
        return title[:i].strip(), title[i + 1:].strip(), 'colon'
    return title.strip(), '', 'none'


def vs_split(title):
    m = re.split(r'\s+(?:vs\.?|versus)\s+', title, maxsplit=1, flags=re.I)
    return (m[0].strip(), m[1].strip()) if len(m) == 2 else None


def words_and_hints(text, upper):
    """Words (in caps when the block says so) plus the word indexes where a | hint breaks."""
    words, hints = [], set()
    for k, part in enumerate(text.split('|')):
        w = part.split()
        if k and words and w:
            hints.add(len(words))
        words += w
    words = [w.replace("'", '’') for w in words]       # typographer's apostrophe
    return ([w.upper() for w in words] if upper else words), hints


# ---------------------------------------------------------------- fitting
def first_baseline(slot, n, size, face):
    """Baseline of line 1 for a block of n lines at this size."""
    lh = slot['lh'] * size
    cap = face.cap * size
    if slot['anchor'] == 'bottom':                 # y = baseline of the last line
        return slot['y'] - (n - 1) * lh
    if slot['anchor'] == 'middle':                 # y = middle of the block (cap top to last baseline)
        return slot['y'] - ((n - 1) * lh + cap) / 2 + cap
    return slot['y'] + cap                         # top: y = cap top of line 1


def fit_block(text, slot, faces, floor):
    """Best line breaks and size for one text block, or None if it can't reach the floor."""
    face = faces[slot['font']]
    words, hints = words_and_hints(text, slot.get('upper', True))
    if not words:
        return {'lines': [], 'size': slot['size'], 'scale': 1.0, 'hint_kept': True, 'note': ''}
    width = slot['right'] - slot['left']
    best = None
    for k in range(1, min(slot['max_lines'], len(words)) + 1):
        for cuts in itertools.combinations(range(1, len(words)), k - 1):
            bounds = (0,) + cuts + (len(words),)
            lines = [' '.join(words[bounds[i]:bounds[i + 1]]) for i in range(k)]
            widest = max(face.width(l, slot['size'], slot['track']) for l in lines)
            scale = min(1.0, width / widest)
            if scale < floor - 0.001:
                continue
            size = slot['size'] * scale
            top = first_baseline(slot, k, size, face) - face.cap * size
            bottom = first_baseline(slot, k, size, face) + (k - 1) * slot['lh'] * size
            if top < slot.get('top_min', 0) or bottom > slot.get('bottom_max', H):
                continue
            widths = [face.width(l, 1, slot['track']) for l in lines]
            balance = (max(widths) - min(widths)) / max(widths) if k > 1 else 0
            widow = k > 1 and len(lines[-1].split()) == 1 and len(words) > 2
            dangling = sum(1 for l in lines[:-1] if l.split()[-1].strip(',.').lower() in WEAK)
            hint_match = set(cuts) == hints if hints else False
            # higher is better: size first, then your hints, then balance, then no widows
            score = (round(scale, 2) + (0.08 if hint_match else 0)
                     - 0.15 * balance - (0.12 if widow else 0) - 0.15 * dangling - 0.02 * (k - 1))
            if best is None or score > best['score']:
                best = {'score': score, 'lines': lines, 'scale': scale, 'size': size,
                        'cuts': cuts, 'hint_kept': (hint_match or not hints)}
    if best:
        best['note'] = '' if best['hint_kept'] else f"changed your | breaks to fit: {' / '.join(best['lines'])}"
    return best


def blocks_overlap(slots, fits, faces):
    """True if two fitted blocks' vertical extents touch (with a small gap)."""
    spans = []
    for name, fit in fits.items():
        if not fit['lines']:
            continue
        slot, face = slots[name], faces[slots[name]['font']]
        n = len(fit['lines'])
        b1 = first_baseline(slot, n, fit['size'], face)
        top = b1 - face.cap * fit['size']
        bottom = b1 + (n - 1) * slot['lh'] * fit['size'] + 0.12 * fit['size']   # descenders
        if slot['left'] < W and slot['right'] > 0:
            spans.append((top, bottom, slot['left'], slot['right']))
    for (t1, b1, l1, r1), (t2, b2, l2, r2) in itertools.combinations(spans, 2):
        if l1 < r2 and l2 < r1 and t1 < b2 + 24 and t2 < b1 + 24:
            return True
    return False


def layout_fits(layout_def, block_set, main, sub, faces, floor):
    slots = layout_def[block_set]
    h = fit_block(main, slots['headline'], faces, floor)
    s = fit_block(sub, slots['sub'], faces, floor) if sub else \
        {'lines': [], 'scale': 1.0, 'size': 0, 'hint_kept': True, 'note': ''}
    if not h or not s:
        return None
    fits = {'headline': h, 'sub': s}
    if blocks_overlap(slots, fits, faces):
        return None
    return slots, fits


def natural_split(title, layout_def, faces, floor):
    """No colon: try every main/sub split point, keep the one that fits best."""
    plain = [w for w in title.replace('|', ' | ').split() if w != '|']
    best = None
    for i in range(2, len(plain) - 1):
        main, sub = ' '.join(plain[:i]), ' '.join(plain[i:])
        r = layout_fits(layout_def, 'blocks', main, sub, faces, floor)
        if not r:
            continue
        h, s = r[1]['headline'], r[1]['sub']
        joint = 0.05 if plain[i].lower() in {'on', 'in', 'for', 'to', 'with', 'when', 'and', 'from', 'that', 'can', 'is', 'are'} else 0
        score = h['scale'] + s['scale'] + joint - 0.03 * abs(i - 4)
        if best is None or score > best[0]:
            best = (score, main, sub)
    return (best[1], best[2]) if best else (title, '')


# ---------------------------------------------------------------- color and layout choice
def pick_color(theme, title, topic, override):
    if override:
        return override, 'set by --color'
    text = f'{title} {topic or ""}'.lower()
    for color, pat in theme.get('topic_rules', {}).items():
        if re.search(pat, text):
            return color, f'topic rule ({color})'
    return theme['default_color'], 'default'


def rotation_order(slug, names):
    start = int(hashlib.md5(slug.encode()).hexdigest(), 16) % len(names)
    return names[start:] + names[:start]


# ---------------------------------------------------------------- render
def resolve_color(value, palette):
    """A block color is a palette key ("ink") or a literal ("#ffffff")."""
    if value is None:
        return None
    return palette.get(value, value)


def render_svg(template, palette, slots, fits, faces):
    text = template.read_text()
    for key, val in palette.items():
        text = text.replace('{{' + key + '}}', val)
    left = sorted(set(re.findall(r'\{\{(\w+)\}\}', text)))
    if left:
        sys.exit(f'{template.name} uses color token(s) {left} that theme.json does not define')
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    root = ET.fromstring(text)
    ns = '{http://www.w3.org/2000/svg}'
    root.attrib.update({'width': str(W), 'height': str(H), 'viewBox': f'0 0 {W} {H}'})
    group = ET.SubElement(root, ns + 'g', {'id': 'cover-text'})
    for name, fit in fits.items():
        slot, face = slots[name], faces[slots[name]['font']]
        n = len(fit['lines'])
        if not n:
            continue
        b1 = first_baseline(slot, n, fit['size'], face)
        fill = resolve_color(slot['fill'], palette)
        stroke = resolve_color(slot.get('stroke'), palette)
        for i, line in enumerate(fit['lines']):
            w = face.width(line, fit['size'], slot['track'])
            align = slot['align']
            x = slot['left'] if align == 'left' else slot['right'] - w if align == 'right' \
                else (slot['left'] + slot['right']) / 2 - w / 2
            attrs = {'d': face.path(line, fit['size'], slot['track'], x, b1 + i * slot['lh'] * fit['size']),
                     'fill': fill}
            if stroke:
                attrs.update({'stroke': stroke, 'stroke-linejoin': 'round', 'paint-order': 'stroke',
                              'stroke-width': f"{slot.get('stroke_width', 0) * fit['scale']:.2f}"})
            ET.SubElement(group, ns + 'path', attrs)
    return ET.ElementTree(root)


def png_size(path):
    """(width, height) from a PNG header, with no image library."""
    with open(path, 'rb') as f:
        head = f.read(24)
    if head[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    return struct.unpack('>II', head[16:24])


def export(tree, out, slug, make_webp):
    out.mkdir(parents=True, exist_ok=True)
    svg = out / f'{slug}.svg'
    tree.write(svg, encoding='unicode', xml_declaration=True)
    files = {'svg': svg}
    for key, w, name in [('master', 3840, f'{slug}-master.png'), ('fulltext', 1920, f'fulltext-{slug}.png'),
                         ('intro', 960, f'intro-{slug}-sm.png')]:
        png = out / name
        subprocess.run(['resvg', '-w', str(w), str(svg), str(png)], check=True)
        files[key + '_png'] = png
        got, want = png_size(png), (w, w * 9 // 16)
        if got != want:
            sys.exit(f'size check failed: {png.name} is {got}, expected {want}')
        if key != 'master' and make_webp:
            webp = png.with_suffix('.webp')
            subprocess.run(['cwebp', '-quiet', '-q', '88', str(png), '-o', str(webp)], check=True)
            files[key + '_webp'] = webp
    return files


# ---------------------------------------------------------------- main
def main(argv=None):
    layouts = load_json('layouts.json')
    theme = load_json('theme.json')
    colors = sorted(theme['palettes'])
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--title', required=True)
    ap.add_argument('--slug', required=True)
    ap.add_argument('--date', required=True, help='publish date, YYYY-MM-DD')
    ap.add_argument('--layout', choices=sorted(layouts['layouts']))
    ap.add_argument('--color', choices=colors)
    ap.add_argument('--topic', help='extra words for the color rule, e.g. the primary keyword')
    ap.add_argument('--out', help='output folder (default output/<date>-<slug>)')
    ap.add_argument('--svg-only', action='store_true', help='write the SVG only (no resvg/cwebp needed)')
    a = ap.parse_args(argv)

    if not re.match(r'^\d{4}-\d{2}-\d{2}$', a.date):
        sys.exit('--date must be YYYY-MM-DD')
    if not re.match(r'^[a-z0-9][a-z0-9-]*$', a.slug):
        sys.exit('--slug must be lowercase letters, digits and hyphens')
    if not a.svg_only:
        for tool in ('resvg',):
            if not shutil.which(tool):
                sys.exit(f'{tool} is not installed. See README.md, "Install", or use --svg-only.')
    make_webp = bool(shutil.which('cwebp'))

    faces = load_faces(theme)
    floor = layouts.get('floor', 0.8)
    rotation = layouts['rotation']
    fallback = layouts.get('fallback', [])
    notes = []
    color, why_color = pick_color(theme, a.title, a.topic, a.color)
    palette = theme['palettes'][color]

    vs = vs_split(a.title.replace('|', ' '))
    if a.layout == 'vs' or (vs and not a.layout and 'vs' in layouts['layouts']):
        if not vs:
            sys.exit('the vs layout needs a title like "A vs B"')
        lay = layouts['layouts']['vs']
        slots = lay['blocks']
        fa, fb = fit_block(vs[0], slots['a'], faces, floor), fit_block(vs[1], slots['b'], faces, floor)
        if not fa or not fb:
            sys.exit(f'vs: a side is too long to fit at {floor:.0%} size')
        fits = {'a': fa, 'b': fb}
        if 'mark' in slots:
            fits['mark'] = fit_block(slots['mark']['text'], slots['mark'], faces, 0.1)
        layout = 'vs'
    else:
        main0, sub0, how = split_title(a.title)
        if how == 'reverse':
            names = [n for n, d in layouts['layouts'].items() if 'reverse' in d]
            if a.layout and a.layout not in names:
                sys.exit(f"'::' (small text on top) works in these layouts only: {', '.join(names)}")
            order = [a.layout] if a.layout else rotation_order(a.slug, names)
        else:
            order = [a.layout] if a.layout else rotation_order(a.slug, rotation) + fallback
        results = []
        for lay_name in order:
            lay = layouts['layouts'][lay_name]
            main_, sub = main0, sub0
            if how == 'none':
                main_, sub = natural_split(a.title, lay, faces, floor)
            r = layout_fits(lay, 'reverse' if how == 'reverse' else 'blocks', main_, sub, faces, floor)
            if not r:
                notes.append(f'layout {lay_name}: does not fit at {floor:.0%} size, skipped')
                continue
            slots, fits = r
            scale = min(fits['headline']['scale'], fits['sub']['scale'] if sub else 1)
            results.append((lay_name, slots, fits, scale, main_, sub))
        if not results:
            sys.exit(f'the title does not fit any layout at {floor:.0%} size. Shorten the part before '
                     'the colon, or move words after a colon.\n' + '\n'.join(notes))
        # rotation layouts win at 90% size or more; then the biggest text wins
        rot = [r for r in results if r[0] in rotation and r[3] >= 0.9]
        ranked = rot + sorted([r for r in results if r not in rot], key=lambda r: -r[3])
        layout, slots, fits, _, main_, sub = ranked[0]
        notes = [n for n in notes if not n.startswith(f'layout {layout}:')]
        if how == 'none':
            notes.append(f'no colon, so the script split it as: "{main_}" / "{sub}"')
        lay = layouts['layouts'][layout]

    for name, f in fits.items():
        if f.get('note'):
            notes.append(f'{name}: {f["note"]}')

    template = ROOT / 'templates' / lay['template']
    tree = render_svg(template, palette, slots, fits, faces)
    # A finished post's files live in ../posts/<date>-<slug>/ (scripts/collect-post.py);
    # a re-made cover goes there. Otherwise output/<date>-<slug>/.
    post_dir = ROOT.parent / 'posts' / f'{a.date}-{a.slug}'
    out = pathlib.Path(a.out) if a.out else (post_dir if post_dir.is_dir() else ROOT / 'output' / f'{a.date}-{a.slug}')
    if a.svg_only:
        out.mkdir(parents=True, exist_ok=True)
        svg = out / f'{a.slug}.svg'
        tree.write(svg, encoding='unicode', xml_declaration=True)
        files = {'svg': svg}
    else:
        files = export(tree, out, a.slug, make_webp)
        if not make_webp:
            notes.append('cwebp is not installed, so no WebP files were made')

    report = {
        'title': a.title, 'slug': a.slug, 'date': a.date, 'layout': layout, 'color': color,
        'color_reason': why_color, 'template': template.name,
        'blocks': {n: {'lines': f['lines'], 'size_px': round(f['size'], 1), 'scale': round(f['scale'], 3),
                       'kept_your_breaks': f['hint_kept']} for n, f in fits.items()},
        'notes': notes,
        'files': {k: str(v.relative_to(ROOT)) if v.is_relative_to(ROOT) else str(v) for k, v in files.items()},
    }
    (out / 'report.json').write_text(json.dumps(report, indent=2))
    print(f'layout {layout} | {color} ({why_color})')
    for n, f in fits.items():
        print(f"  {n:8} {f['size']:.0f}px ({f['scale']:.0%})  " + ' / '.join(f['lines']))
    for n in notes:
        print('  note:', n)
    print('  ->', out)


if __name__ == '__main__':
    main()
