#!/usr/bin/env python3
from __future__ import annotations
"""
router.py - Multi-vertical blog pipeline input router

Reads <project-dir>/inputs/, classifies each file, expands batch tables,
writes <project-dir>/inputs/.manifest.json.

The bash orchestrator (blog-pipeline.sh) reads the manifest and dispatches
each job to the right entry stage of the pipeline (Stages 0-9).

Usage:
  router.py <project-dir>
  router.py <project-dir> --dry-run    # print manifest to stdout, don't write
  router.py <project-dir> --quiet      # write manifest, suppress stdout summary

Exit codes:
  0 = manifest written, all jobs are HIGH confidence and ready to run
  1 = fatal error (missing dir, missing config, no inputs, audit failure)
  2 = manifest written but one or more files aborted (review required)

Config:
  Reads <project-dir>/instructions/router-config.json.
  If missing, uses the built-in defaults below.
"""

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# Default config (overridden by router-config.json if present).
DEFAULTS = {
    "vertical": "blog-project",
    "batch_table_columns": [
        "Topic", "Primary Keyword", "Secondary Keywords",
        "Goal", "Seasonal Tie-In",
    ],
    "slug_source_column": "Topic",
    "brief_markers": [
        "Working title",
        "Primary keyword",
        "Secondary keywords",
        "Target audience",
        "Recommended word count",
    ],
    # Most-advanced stage first. First match wins.
    # Each stage lists the marker text to find. Stage N marker means
    # the file has completed stage N, so entry_stage = N + 1.
    "draft_stage_markers": {
        "7": ["External Link Verification"],
        "6": ["| Original Text | Linked Version |", "Internal Link Table"],
        "5": ["# Publishing Package", "Publishing Package\n* TITLE:"],
        "4": ["Recommended Titles", "SEO/Google Title"],
        "2": ["{{TLDR}}", "{{FAQ}}"],
    },
    "research_markers": ["## Direct Quotes", "## Statistics and Data"],
    "topic_seed_max_words": 500,
    "stop_words": [
        "a", "an", "the", "in", "on", "at", "to", "for", "of",
        "with", "is", "are", "and", "or", "but", "by", "from",
    ],
}


# ---------- config -------------------------------------------------------

def load_config(project_dir: Path) -> dict:
    """Load router-config.json from instructions/, merge with defaults."""
    config = dict(DEFAULTS)
    config_path = project_dir / "instructions" / "router-config.json"
    if config_path.exists():
        try:
            user_config = json.loads(config_path.read_text(encoding="utf-8"))
            config.update(user_config)
        except json.JSONDecodeError as e:
            print(f"ERROR: router-config.json is invalid JSON: {e}",
                  file=sys.stderr)
            sys.exit(1)
    return config


# ---------- slug generation ----------------------------------------------

def make_slug(text: str, stop_words: list[str], max_len: int = 60) -> str:
    """Generate a URL slug from a title string. Deterministic."""
    text = text.lower().strip()
    # Replace any non-alphanumeric run with a single hyphen.
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    # Remove stop words (but only if more than 2 tokens remain after removal).
    tokens = [t for t in text.split("-") if t]
    filtered = [t for t in tokens if t not in stop_words]
    if len(filtered) >= 2:
        tokens = filtered
    slug = "-".join(tokens)[:max_len].rstrip("-")
    return slug or "untitled"


def disambiguate_slugs(slugs: list[str]) -> list[str]:
    """Append -2, -3 etc to duplicates so every slug is unique."""
    out = []
    counts: dict[str, int] = {}
    for s in slugs:
        if s in counts:
            counts[s] += 1
            out.append(f"{s}-{counts[s]}")
        else:
            counts[s] = 1
            out.append(s)
    return out


# ---------- classification helpers ---------------------------------------

def read_text_file(path: Path) -> str | None:
    """Try to read a text file. Returns None on failure."""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return None


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def find_marker_hits(text: str, markers: list[str]) -> list[str]:
    """Case-insensitive substring search. Returns the markers that hit."""
    hits = []
    lower = text.lower()
    for marker in markers:
        if marker.lower() in lower:
            hits.append(marker)
    return hits


def detect_draft_stage(text: str, stage_markers: dict) -> tuple[int | None, list[str]]:
    """Walk stage markers most-advanced first. Returns (completed_stage, evidence)."""
    # Sort stage keys numerically, descending.
    stages = sorted((int(k) for k in stage_markers), reverse=True)
    for stage in stages:
        markers = stage_markers[str(stage)]
        hits = find_marker_hits(text, markers)
        if hits:
            return stage, hits
    return None, []


# ---------- batch table parsing ------------------------------------------

def parse_csv_or_tsv(path: Path, expected_columns: list[str]) -> tuple[list[dict] | None, str]:
    """Parse a CSV or TSV file as a batch table. Returns (rows, error_or_evidence)."""
    delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
    try:
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            rows = [r for r in reader if any((v or "").strip() for v in r.values())]
            if not rows:
                return None, "no data rows"
            headers = reader.fieldnames or []
            matched = [c for c in expected_columns if c in headers]
            if len(matched) < 2:
                return None, f"headers {headers} don't match expected batch columns"
            return rows, f"parsed {len(rows)} rows; matched columns: {matched}"
    except (OSError, UnicodeError, csv.Error) as e:
        return None, f"parse error: {type(e).__name__}: {e}"


def parse_markdown_table(text: str, expected_columns: list[str]) -> tuple[list[dict] | None, str]:
    """Parse a markdown pipe table as a batch table. Returns (rows, error_or_evidence).

    Looks for the first table whose header matches expected columns.
    """
    lines = text.splitlines()
    # Find a header row: starts with |, contains expected column names.
    header_idx = -1
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("|") or "|" not in stripped[1:]:
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        matched = [c for c in expected_columns if c in cells]
        if len(matched) >= 2:
            # Verify next line is a separator row.
            if i + 1 < len(lines) and re.match(r"^\s*\|[\s\-:|]+\|\s*$", lines[i + 1]):
                header_idx = i
                break
    if header_idx < 0:
        return None, "no markdown table with matching headers found"

    headers = [c.strip() for c in lines[header_idx].strip("|").split("|")]
    rows = []
    for line in lines[header_idx + 2:]:
        stripped = line.strip()
        if not stripped.startswith("|"):
            break  # end of table
        if re.match(r"^\s*\|[\s\-:|]+\|\s*$", stripped):
            continue  # extra separator
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) != len(headers):
            continue  # malformed row, skip
        row = dict(zip(headers, cells))
        if any(v for v in row.values()):
            rows.append(row)

    if not rows:
        return None, "matched header but no data rows"
    return rows, f"parsed {len(rows)} rows from markdown table"


# ---------- per-file classification --------------------------------------

def classify_file(path: Path, config: dict) -> dict:
    """Classify a single input file. Returns a dict describing the result.

    Result keys:
      kind: 'batch_table' | 'brief' | 'draft' | 'topic_seed' | 'research' | 'abort'
      entry_stage: int (for non-batch, non-research kinds)
      confidence: 'HIGH' | 'MEDIUM' | 'LOW'
      evidence: human-readable string
      rows: list of dicts (only for batch_table)
      completed_stage: int (only for draft)
      proposed_slug: str (best guess for non-batch kinds)
    """
    name = path.name.lower()
    suffix = path.suffix.lower()
    default_year = datetime.now(timezone.utc).year

    # Empty file.
    try:
        if path.stat().st_size == 0:
            return {
                "kind": "abort",
                "confidence": "LOW",
                "evidence": "file is empty",
            }
    except OSError as e:
        return {"kind": "abort", "confidence": "LOW",
                "evidence": f"cannot stat file: {e}"}

    # Hidden files and the manifest itself.
    if name.startswith(".") or name == ".manifest.json":
        return {"kind": "skip", "evidence": "hidden file"}

    # CSV / TSV always treated as batch tables.
    if suffix in (".csv", ".tsv"):
        rows, evidence = parse_csv_or_tsv(path, config["batch_table_columns"])
        if rows is None:
            return {"kind": "abort", "confidence": "LOW",
                    "evidence": f"{suffix} file but not a valid batch table: {evidence}"}
        return {"kind": "batch_table", "confidence": "HIGH",
                "evidence": evidence, "rows": rows}

    # PDF: assume research bundle (we can't easily classify content without external libs).
    if suffix == ".pdf":
        return {"kind": "research", "confidence": "MEDIUM",
                "evidence": "PDF file treated as research/supporting material"}

    # Text-based files from here on.
    text = read_text_file(path)
    if text is None:
        return {"kind": "abort", "confidence": "LOW",
                "evidence": "cannot read file as text"}

    if not text.strip():
        return {"kind": "abort", "confidence": "LOW",
                "evidence": "file contains only whitespace"}

    # Research bundle (Stage 0 output format).
    research_hits = find_marker_hits(text, config["research_markers"])
    if len(research_hits) >= 2:
        return {"kind": "research", "confidence": "HIGH",
                "evidence": f"research bundle markers found: {research_hits}"}

    # Markdown table batch.
    if suffix in (".md", ".markdown") and "|" in text:
        rows, evidence = parse_markdown_table(text, config["batch_table_columns"])
        if rows is not None:
            return {"kind": "batch_table", "confidence": "HIGH",
                    "evidence": evidence, "rows": rows}

    # Draft detection (walk stages most-advanced first).
    completed_stage, draft_evidence = detect_draft_stage(
        text, config["draft_stage_markers"]
    )
    if completed_stage is not None:
        slug = extract_slug_from_draft(text, path, config)
        # Map completed stage to entry stage.
        # Stage 7 done -> enter stage 8. Stage 6 done -> stage 7. Stage 5 done -> 6.
        # Stage 4 done -> 5. Stage 2 done -> 3 (we can't distinguish 2 from 3).
        entry_stage = completed_stage + 1
        return {
            "kind": "draft",
            "confidence": "HIGH",
            "evidence": f"matched stage {completed_stage} markers: {draft_evidence}",
            "completed_stage": completed_stage,
            "entry_stage": entry_stage,
            "proposed_slug": slug,
            "publish_date": extract_publish_date_from_text(text, default_year),
        }

    # Brief detection.
    brief_hits = find_marker_hits(text, config["brief_markers"])
    required_for_high = max(3, len(config["brief_markers"]) - 1)
    if len(brief_hits) >= required_for_high:
        slug = extract_slug_from_brief(text, path, config)
        return {
            "kind": "brief",
            "confidence": "HIGH",
            "evidence": f"matched {len(brief_hits)}/{len(config['brief_markers'])} brief markers: {brief_hits}",
            "entry_stage": 2,
            "proposed_slug": slug,
            "publish_date": extract_publish_date_from_text(text, default_year),
        }
    if 2 <= len(brief_hits) < required_for_high:
        # Ambiguous - between topic seed and brief.
        return {
            "kind": "abort",
            "confidence": "LOW",
            "evidence": (f"partial brief markers ({len(brief_hits)}/{len(config['brief_markers'])}: "
                         f"{brief_hits}) - not enough to classify as brief, "
                         f"too many for topic seed"),
        }

    # Topic seed (short prose, no markers).
    wc = word_count(text)
    if wc <= config["topic_seed_max_words"]:
        slug = extract_slug_from_topic_seed(text, path, config)
        return {
            "kind": "topic_seed",
            "confidence": "HIGH",
            "evidence": f"short prose ({wc} words), no brief or draft markers",
            "entry_stage": 1,
            "proposed_slug": slug,
            "publish_date": extract_publish_date_from_text(text, default_year),
        }

    # Long prose, no markers - probably a brief in non-standard format, or
    # an article from another source. Don't guess.
    return {
        "kind": "abort",
        "confidence": "LOW",
        "evidence": (f"long prose ({wc} words) with no brief, draft, or research markers; "
                     f"cannot determine entry stage"),
    }


# ---------- slug extraction from content ---------------------------------

def extract_slug_from_draft(text: str, path: Path, config: dict) -> str:
    """Pull slug from Publishing Package URL line, then H1, then filename."""
    # Try URL line in Publishing Package.
    m = re.search(r"^\*\s*URL:\s*https?://[^\s]+?/([a-z0-9\-]+)/?\s*$",
                  text, re.MULTILINE)
    if m:
        return m.group(1)
    # Try first H1.
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return make_slug(m.group(1), config["stop_words"])
    return slug_from_filename(path, config)


def extract_slug_from_brief(text: str, path: Path, config: dict) -> str:
    """Pull slug from 'Working title' field, then H1, then filename.

    Handles two brief formats:
    - Inline:  'Working title: The Title Here'
    - Heading: '## Working title\\n**"The Title Here"**' (title on next line)
    """
    # Heading format: ## Working title [...]\n<actual title on next line>
    m = re.search(r"##\s*working title[^\n]*\n\s*(.+)", text, re.IGNORECASE)
    if m:
        line = m.group(1).strip()
        # Strip bold markers, option prefixes (Primary:, Title:), quotes, backticks
        line = re.sub(r"^\*{1,2}(?:Primary|Title|Recommended)[:\s]+\*{0,2}", "", line, flags=re.IGNORECASE)
        line = re.sub(r"[\*`\"']", "", line).strip()
        if len(line.split()) >= 2:
            return make_slug(line, config["stop_words"])
    # Inline format: 'Working title: The Title'
    m = re.search(r"working title[:\s]+(.+?)(?:\n|$)", text, re.IGNORECASE)
    if m:
        candidate = m.group(1).strip("*` \"'()")
        if len(candidate.split()) >= 2:
            return make_slug(candidate, config["stop_words"])
    # Fall through to H1
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return make_slug(m.group(1), config["stop_words"])
    return slug_from_filename(path, config)


def extract_slug_from_topic_seed(text: str, path: Path, config: dict) -> str:
    """Pull slug from H1 or first sentence, then filename."""
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return make_slug(m.group(1), config["stop_words"])
    # First sentence, first 8 words.
    first = text.strip().split("\n", 1)[0]
    first = re.sub(r"[^\w\s]", " ", first)
    words = first.split()[:8]
    if words:
        return make_slug(" ".join(words), config["stop_words"])
    return slug_from_filename(path, config)


def slug_from_filename(path: Path, config: dict) -> str:
    stem = path.stem
    # Strip common prefixes/suffixes.
    stem = re.sub(r"^(input|brief|draft|topic)[-_]", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"[-_](brief|draft|input|final)$", "", stem, flags=re.IGNORECASE)
    return make_slug(stem, config["stop_words"])


# ---------- publish-date extraction ---------------------------------------

_MONTH_NAMES = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3,
    "apr": 4, "april": 4, "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
    "aug": 8, "august": 8, "sep": 9, "sept": 9, "september": 9, "oct": 10,
    "october": 10, "nov": 11, "november": 11, "dec": 12, "december": 12,
}

# Column headers that may carry a scheduled publish date in a batch table.
# First match wins, checked case-insensitively.
DATE_COLUMN_CANDIDATES = [
    "Publish Date", "Scheduled Publish Date", "Date / Status", "Date/Status", "Date",
]

# Inline markers recognized in topic-seed / brief free text, e.g.
# "Publish Date: 2026-09-02" or "Scheduled: Sep 30".
_INLINE_DATE_RE = re.compile(
    r"^\s*\**\s*(?:Publish(?:ing)? Date|Scheduled(?: Publish)?|Date)\s*:\s*(.+?)\s*\**\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def parse_publish_date(raw: str, default_year: int) -> str | None:
    """Best-effort parse of a human-written publish date into YYYY-MM-DD.

    Returns None for vague/unparseable values ("flex (Sep)", "TBD", "ongoing",
    a blank cell) rather than guessing — an empty publish_date means the
    pipeline falls back to no date prefix, which is safer than a wrong one.
    """
    if not raw:
        return None
    value = raw.strip()
    if not value:
        return None

    # Already ISO (YYYY-MM-DD).
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", value)
    if m:
        return value

    # "Sep 2", "Sep 2, 2026", "September 2 2026", "Sept. 30".
    m = re.match(
        r"^([A-Za-z]{3,9})\.?\s+(\d{1,2})(?:,?\s+(\d{4}))?$", value
    )
    if m:
        month_name, day, year = m.group(1).lower(), int(m.group(2)), m.group(3)
        month = _MONTH_NAMES.get(month_name)
        if month:
            year = int(year) if year else default_year
            try:
                return f"{year:04d}-{month:02d}-{day:02d}"
            except ValueError:
                return None

    # Anything else ("flex (Sep)", "TBD", "No publish (Thanksgiving)", "—") is
    # deliberately left unparsed rather than guessed at.
    return None


def extract_publish_date_from_row(row: dict, config: dict, default_year: int) -> str:
    """Look for a recognized date column in a batch-table row (case-insensitive)."""
    lower_row = {k.strip().lower(): v for k, v in row.items()}
    for candidate in config.get("date_column_candidates", DATE_COLUMN_CANDIDATES):
        v = lower_row.get(candidate.strip().lower())
        if v:
            parsed = parse_publish_date(str(v), default_year)
            if parsed:
                return parsed
    return ""


def extract_publish_date_from_text(text: str, default_year: int) -> str:
    """Look for an inline 'Publish Date: ...' style marker in free text."""
    m = _INLINE_DATE_RE.search(text)
    if m:
        parsed = parse_publish_date(m.group(1), default_year)
        if parsed:
            return parsed
    return ""


# ---------- manifest assembly --------------------------------------------

def build_manifest(project_dir: Path, config: dict) -> tuple[dict, int]:
    """Process inputs/, return (manifest_dict, exit_code).

    exit_code is 0 if all jobs HIGH confidence, 2 if any aborts, 1 on fatal.
    """
    inputs_dir = project_dir / "inputs"
    if not inputs_dir.exists():
        print(f"ERROR: inputs/ directory not found at {inputs_dir}", file=sys.stderr)
        sys.exit(1)

    # List input files (skip hidden, directories, and well-known non-topic files).
    _SKIP_NAMES = {"readme.md", "readme.txt", "readme", ".gitkeep"}
    input_files = sorted(
        p for p in inputs_dir.iterdir()
        if p.is_file()
        and not p.name.startswith(".")
        and p.name.lower() not in _SKIP_NAMES
    )

    if not input_files:
        print(f"ERROR: no files in {inputs_dir}", file=sys.stderr)
        sys.exit(1)

    # Classify every file.
    classifications: list[tuple[Path, dict]] = []
    for path in input_files:
        result = classify_file(path, config)
        classifications.append((path, result))

    # Build jobs from classifications.
    jobs: list[dict] = []
    aborted: list[dict] = []
    pending_research: list[Path] = []  # supporting files awaiting a job

    # First pass: create jobs from non-research, non-abort classifications.
    for path, result in classifications:
        kind = result["kind"]
        rel_path = str(path.relative_to(project_dir))

        if kind == "skip":
            continue

        if kind == "abort":
            aborted.append({
                "path": rel_path,
                "reason": result["evidence"],
                "confidence": result["confidence"],
            })
            continue

        if kind == "research":
            pending_research.append(path)
            continue

        if kind == "batch_table":
            # One job per row.
            raw_slugs = []
            row_topics = []
            for row in result["rows"]:
                topic = row.get(config["slug_source_column"], "").strip()
                if not topic:
                    aborted.append({
                        "path": rel_path,
                        "reason": f"batch row missing {config['slug_source_column']}: {row}",
                        "confidence": "LOW",
                    })
                    continue
                raw_slugs.append(make_slug(topic, config["stop_words"]))
                row_topics.append((topic, row))
            slugs = disambiguate_slugs(raw_slugs)
            default_year = datetime.now(timezone.utc).year
            for slug, (topic, row) in zip(slugs, row_topics):
                jobs.append({
                    "job_id": len(jobs) + 1,
                    "slug": slug,
                    "primary_input_path": rel_path,
                    "supporting_inputs": [],
                    "classification": "batch_table_row",
                    "entry_stage": 1,
                    "confidence": "HIGH",
                    "evidence": (f"row from batch table; topic='{topic}'; "
                                 f"batch_table_evidence: {result['evidence']}"),
                    "batch_row": row,
                    "publish_date": extract_publish_date_from_row(row, config, default_year),
                })
            continue

        # brief, draft, or topic_seed - one job each.
        jobs.append({
            "job_id": len(jobs) + 1,
            "slug": result["proposed_slug"],
            "primary_input_path": rel_path,
            "supporting_inputs": [],
            "classification": kind,
            "entry_stage": result["entry_stage"],
            "confidence": result["confidence"],
            "evidence": result["evidence"],
            "publish_date": result.get("publish_date", ""),
        })

    # Disambiguate slugs across all jobs (batch rows already disambiguated within
    # their table, but a topic seed could clash with a batch row).
    if jobs:
        all_slugs = disambiguate_slugs([j["slug"] for j in jobs])
        for job, new_slug in zip(jobs, all_slugs):
            job["slug"] = new_slug

    # Attach pending research files to jobs.
    # Strategy: distribute round-robin across jobs created so far. If no jobs,
    # orphan them.
    orphaned: list[dict] = []
    if pending_research:
        if not jobs:
            for r in pending_research:
                orphaned.append({
                    "path": str(r.relative_to(project_dir)),
                    "reason": "no primary job to attach to",
                })
        else:
            for i, r in enumerate(pending_research):
                target = jobs[i % len(jobs)]
                target["supporting_inputs"].append(str(r.relative_to(project_dir)))

    # Self-audit.
    audit_failures = run_self_audit(input_files, jobs, aborted, orphaned, project_dir)
    if audit_failures:
        print("ERROR: router self-audit failed:", file=sys.stderr)
        for f in audit_failures:
            print(f"  - {f}", file=sys.stderr)
        sys.exit(1)

    manifest = {
        "router_version": "1.0",
        "vertical": config["vertical"],
        "project_dir": str(project_dir),
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "total_input_files": len(input_files),
        "jobs": jobs,
        "aborted_files": aborted,
        "orphaned_supporting_files": orphaned,
    }

    exit_code = 2 if (aborted or orphaned) else 0
    return manifest, exit_code


def run_self_audit(input_files, jobs, aborted, orphaned, project_dir) -> list[str]:
    """Verify every file is accounted for and every job has required fields."""
    failures = []

    accounted: set[str] = set()
    for j in jobs:
        accounted.add(j["primary_input_path"])
        for s in j["supporting_inputs"]:
            accounted.add(s)
    for a in aborted:
        accounted.add(a["path"])
    for o in orphaned:
        accounted.add(o["path"])

    expected = {str(p.relative_to(project_dir)) for p in input_files}
    missing = expected - accounted
    if missing:
        failures.append(f"files not accounted for: {sorted(missing)}")

    seen_slugs: set[str] = set()
    for j in jobs:
        for field in ("slug", "entry_stage", "primary_input_path", "classification",
                      "confidence", "evidence"):
            if field not in j or j[field] in (None, ""):
                failures.append(f"job {j.get('job_id')} missing field: {field}")
        if j["slug"] in seen_slugs:
            failures.append(f"duplicate slug: {j['slug']}")
        seen_slugs.add(j["slug"])
        if not isinstance(j["entry_stage"], int) or not (0 <= j["entry_stage"] <= 8):
            failures.append(f"job {j.get('job_id')} has invalid entry_stage: {j['entry_stage']}")

    return failures


# ---------- summary printing ---------------------------------------------

def print_summary(manifest: dict) -> None:
    print("=" * 64)
    print(f"ROUTER MANIFEST - {manifest['vertical']}")
    print(f"Generated: {manifest['run_timestamp']}")
    print("=" * 64)
    print(f"Input files processed: {manifest['total_input_files']}")
    print(f"Jobs created:          {len(manifest['jobs'])}")
    print(f"Files aborted:         {len(manifest['aborted_files'])}")
    print(f"Orphaned supporting:   {len(manifest['orphaned_supporting_files'])}")
    print()
    if manifest["jobs"]:
        print("JOBS:")
        for j in manifest["jobs"]:
            supp = f"  (+{len(j['supporting_inputs'])} supporting)" if j["supporting_inputs"] else ""
            print(f"  #{j['job_id']:>2}  stage {j['entry_stage']}  "
                  f"{j['classification']:<18}  {j['slug']}{supp}")
        print()
    if manifest["aborted_files"]:
        print("ABORTED:")
        for a in manifest["aborted_files"]:
            print(f"  - {a['path']}: {a['reason']}")
        print()
    if manifest["orphaned_supporting_files"]:
        print("ORPHANED (research with no job to attach to):")
        for o in manifest["orphaned_supporting_files"]:
            print(f"  - {o['path']}: {o['reason']}")
        print()


# ---------- main ---------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--dry-run", action="store_true",
                        help="print manifest to stdout, do not write file")
    parser.add_argument("--quiet", action="store_true",
                        help="suppress summary, just write manifest")
    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    if not project_dir.is_dir():
        print(f"ERROR: not a directory: {project_dir}", file=sys.stderr)
        sys.exit(1)

    config = load_config(project_dir)
    manifest, exit_code = build_manifest(project_dir, config)

    if args.dry_run:
        print(json.dumps(manifest, indent=2))
    else:
        manifest_path = project_dir / "inputs" / ".manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        if not args.quiet:
            print_summary(manifest)
            print(f"Manifest written to: {manifest_path}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
