#!/usr/bin/env python3
"""Move everything for one blog post into posts/<date>-<slug>/.

A post's files are spread across a pipeline while it's being made:

  output/[_done/]          the draft, -sources.md, -images.md, -cover-<model>.png photos
  cover-generator/output/[_done/]<date>-<slug>/   the covers (options/ subfolders too)
  briefs/<slug>-brief.md   the brief, under the final or the topic slug
  research/<slug>-research.md   the research, under the topic slug

This moves them all into posts/<date>-<slug>/, flat. A file from a subfolder of
the cover folder keeps its path in its name (options/flux-2/x.webp becomes
options-flux-2-x.webp), so nothing collides.

Stage 5 renames a post from its topic slug to an SEO slug. The pair comes from
the slug map that blog-pipeline.sh writes: <project-dir>/logs/blog-slug-map.log,
or $BLOG_LOG_DIR/blog-slug-map.log, or the file named with --slug-map. Research
and briefs filed under the topic slug still reach the right post.

Never overwrites: a name clash is skipped and reported. Running it again on a
collected post moves nothing. Dry run unless --apply.

Usage:
  collect-post.py <project-dir> --date-slug 2026-11-04-some-slug [--apply]
  collect-post.py <project-dir> --all [--apply]
  collect-post.py <project-dir> --date-slug ... --slug-map path/to/blog-slug-map.log
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

DRAFT_RE = re.compile(r"(\d{4}-\d{2}-\d{2})-([a-z0-9][a-z0-9-]*?)-draft\.md$")
# What may follow "<date>-<slug>" in an output/ file name for it to belong to the post.
OUTPUT_SUFFIX_RE = re.compile(r"^(?:-draft|-sources|-images)?(?:-cover-[a-z0-9-]+)?\.[A-Za-z0-9]+$")
SKIP_NAMES = {".DS_Store", ".gitkeep"}


# Set in main(). blog-pipeline.sh writes the map and passes the same path here.
SLUG_MAP: Path | None = None


def default_slug_map(project_dir: Path) -> Path:
    """The slug map blog-pipeline.sh writes: $BLOG_LOG_DIR, else <project-dir>/logs."""
    log_dir = os.environ.get("BLOG_LOG_DIR")
    return (Path(log_dir).expanduser() if log_dir else project_dir / "logs") / "blog-slug-map.log"


def topic_slugs(project: str, slug: str) -> set[str]:
    """Every topic slug the slug map pairs with this final slug, plus the slug itself."""
    slugs = {slug}
    if SLUG_MAP is not None and SLUG_MAP.exists():
        for line in SLUG_MAP.read_text(encoding="utf-8", errors="replace").splitlines():
            parts = line.split("\t")
            if len(parts) >= 4 and parts[1] == project and parts[3] == slug and parts[2]:
                slugs.add(parts[2])
    return slugs


def find_posts(project_dir: Path) -> dict[str, str]:
    """date-slug -> date, for every dated draft in output/, output/_done/ or posts/."""
    found = {}
    for folder in (project_dir / "output", project_dir / "output" / "_done"):
        if folder.is_dir():
            for f in folder.iterdir():
                m = DRAFT_RE.search(f.name)
                if f.is_file() and m:
                    found[f"{m.group(1)}-{m.group(2)}"] = m.group(1)
    return found


def undated_drafts(project_dir: Path) -> list[Path]:
    out = []
    for folder in (project_dir / "output", project_dir / "output" / "_done"):
        if folder.is_dir():
            out += [f for f in folder.iterdir()
                    if f.is_file() and f.name.endswith("-draft.md") and not DRAFT_RE.search(f.name)]
    return out


def plan_post(project_dir: Path, date_slug: str) -> list[tuple[Path, str]]:
    """(source file, name inside the post folder) for everything belonging to the post."""
    date, slug = date_slug[:10], date_slug[11:]
    slugs = topic_slugs(project_dir.name, slug)
    keys = {f"{date}-{s}" for s in slugs}
    moves: list[tuple[Path, str]] = []

    # output/, output/_done/, output/images/: names carrying <date>-<slug>
    for folder in ("output", "output/_done", "output/images"):
        d = project_dir / folder
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if not f.is_file() or f.name in SKIP_NAMES:
                continue
            for key in keys:
                i = f.name.find(key)
                # The key must start the name or follow a non-slug character
                # ("DRAFT Blog WCM 2026-…"), and what follows must be a known suffix.
                if i >= 0 and (i == 0 or not re.match(r"[a-z0-9-]", f.name[i - 1])) \
                        and OUTPUT_SUFFIX_RE.match(f.name[i + len(key):]):
                    moves.append((f, f.name))
                    break
            else:
                # Hidden markers such as .ai-covers-<date-slug>.done
                if f.name.startswith(".") and any(f.name.endswith(f"-{k}.done") for k in keys):
                    moves.append((f, f.name))

    # Fallback for output/ files filed under a topic slug the slug map doesn't
    # know: when this post is the only one on its date, a file starting with that
    # date and no other post's key is this post's.
    same_day = [ds for ds in find_posts(project_dir) if ds[:10] == date]

    def words(text: str) -> set[str]:
        return {w.rstrip("s") for w in text.split("-") if len(w) > 2}

    def owner(name: str) -> str | None:
        """The same-day post whose slug shares the most words with the file's, if clear."""
        if same_day == [date_slug]:
            return date_slug
        stem = re.sub(r"-(sources|images|draft)\.md$|-cover-[a-z0-9-]+\.[a-z]+$", "", name)[11:]
        scores = sorted(((len(words(stem) & words(ds[11:])), ds) for ds in same_day), reverse=True)
        if scores and scores[0][0] >= 2 and (len(scores) == 1 or scores[0][0] > scores[1][0]):
            return scores[0][1]
        return None

    if date_slug in same_day:
        claimed = {src for src, _ in moves}
        for folder in ("output", "output/_done"):
            d = project_dir / folder
            if d.is_dir():
                for f in sorted(d.iterdir()):
                    if f.is_file() and f not in claimed and f.name.startswith(f"{date}-") \
                            and not DRAFT_RE.search(f.name) \
                            and re.search(r"-(sources|images)\.md$|-cover-[a-z0-9-]+\.[a-z]+$", f.name) \
                            and owner(f.name) == date_slug:
                        moves.append((f, f.name))

    # cover-generator/output/[_done/]<date>-<slug>/ — flattened
    for folder in ("cover-generator/output", "cover-generator/output/_done"):
        for key in keys:
            d = project_dir / folder / key
            if not d.is_dir():
                continue
            for root, _dirs, files in os.walk(d):
                rel = Path(root).relative_to(d)
                for name in sorted(files):
                    if name in SKIP_NAMES:
                        continue
                    flat = "-".join([*rel.parts, name]) if rel.parts else name
                    # A cover folder left under the topic slug (Stage 5 renamed the
                    # post afterwards) holds files like report.json that would clash
                    # with the final cover's. Tag them with the old slug.
                    old_slug = key[11:]
                    if key != date_slug and old_slug not in flat:
                        flat = f"{old_slug}-{flat}"
                    moves.append((Path(root) / name, flat))

    # briefs/ and research/ under the final or the topic slug
    for s in sorted(slugs):
        for f in (project_dir / "briefs" / f"{s}-brief.md",
                  project_dir / "research" / f"{s}-research.md"):
            if f.is_file():
                moves.append((f, f.name))

    return moves


def collect(project_dir: Path, date_slug: str, apply: bool) -> tuple[int, list[str]]:
    dest = project_dir / "posts" / date_slug
    moved, problems = 0, []
    seen: set[str] = set()

    for src, name in plan_post(project_dir, date_slug):
        target = dest / name
        if name in seen or target.exists():
            problems.append(f"name clash, left in place: {src.relative_to(project_dir)} -> posts/{date_slug}/{name}")
            continue
        seen.add(name)
        print(f"  {'mv' if apply else 'would mv'} {src.relative_to(project_dir)} -> posts/{date_slug}/{name}")
        if apply:
            dest.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(target))
        moved += 1

    if apply:
        # Remove the now-empty cover folders (and their empty subfolders).
        for folder in ("cover-generator/output", "cover-generator/output/_done"):
            for key in {f"{date_slug[:10]}-{s}" for s in topic_slugs(project_dir.name, date_slug[11:])}:
                d = project_dir / folder / key
                if d.is_dir():
                    for root, dirs, files in os.walk(d, topdown=False):
                        for junk in set(files) & SKIP_NAMES:
                            (Path(root) / junk).unlink()
                        try:
                            Path(root).rmdir()
                        except OSError:
                            pass
    return moved, problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("project_dir")
    ap.add_argument("--date-slug", help="one post, e.g. 2026-11-04-google-business-profile-checklist")
    ap.add_argument("--slug-map", help="slug map file (default: $BLOG_LOG_DIR or <project-dir>/logs/blog-slug-map.log)")
    ap.add_argument("--all", action="store_true", help="every dated draft in output/ and output/_done/")
    ap.add_argument("--apply", action="store_true", help="move files (default: dry run)")
    a = ap.parse_args()

    project_dir = Path(a.project_dir).expanduser().resolve()
    if not (project_dir / "output").is_dir():
        sys.exit(f"not a blog pipeline (no output/): {project_dir}")
    if bool(a.date_slug) == a.all:
        sys.exit("give exactly one of --date-slug or --all")
    if a.date_slug and not re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9][a-z0-9-]*$", a.date_slug):
        sys.exit(f"not a <YYYY-MM-DD>-<slug>: {a.date_slug}")

    global SLUG_MAP
    SLUG_MAP = Path(a.slug_map).expanduser() if a.slug_map else default_slug_map(project_dir)
    if not SLUG_MAP.exists():
        print(f"note: no slug map at {SLUG_MAP}. Research or briefs filed under an older "
              "topic slug won't be found. Pass --slug-map if it lives elsewhere.")

    posts = sorted(find_posts(project_dir)) if a.all else [a.date_slug]
    total, problems = 0, []
    planned = {src for ds in posts for src, _ in plan_post(project_dir, ds)}
    for ds in posts:
        print(f"{ds}:")
        n, p = collect(project_dir, ds, a.apply)
        total += n
        problems += p
        if n == 0 and not p:
            print("  nothing to move")

    print(f"\n{'Moved' if a.apply else 'Would move'} {total} file(s) for {len(posts)} post(s) in {project_dir.name}.")
    if a.all:
        for f in undated_drafts(project_dir):
            problems.append(f"undated draft, left in place: {f.relative_to(project_dir)}")
        # Dated files no post claimed: usually research or sources filed under a
        # topic slug the slug map doesn't know. Listed so they can be moved by hand.
        for folder in ("output", "output/_done", "output/images", "research", "briefs"):
            d = project_dir / folder
            if d.is_dir():
                for f in sorted(d.iterdir()):
                    if f.is_file() and f not in planned and re.search(r"\d{4}-\d{2}-\d{2}-", f.name) \
                            and not DRAFT_RE.search(f.name):
                        problems.append(f"no post matched, left in place: {f.relative_to(project_dir)}")
    for p in problems:
        print(f"  ! {p}")
    if not a.apply:
        print("Dry run. Add --apply to move.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
