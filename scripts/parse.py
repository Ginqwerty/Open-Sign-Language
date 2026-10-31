#!/usr/bin/env python3
"""Parse README.md and helper/datasets.md into machine-readable JSON.

Deterministic, standard library only, read-only on the source files, no network.

    python3 scripts/parse.py           # (re)write data/*.json
    python3 scripts/parse.py --check   # exit 1 if data/*.json are out of date

The parser reports what the source files say. It does not fix, normalise or
judge them: wrong links, typos and inconsistent labels are kept as written.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data"
README = "README.md"
DATASETS = "helper/datasets.md"
SCHEMA_VERSION = 1

LINK_RE = re.compile(r"\[([^\]]*)\]\(((?:[^()\s]|\([^()]*\))+)\)")
HEADING_RE = re.compile(r"^\s*(#{1,6})\s+(.*?)\s*$")
BULLET_RE = re.compile(r"^\s*[-*]\s+(.*)$")
SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
YEAR_RE = re.compile(r"^(\d{4})$")
STRICT_ENTRY_RE = re.compile(r"^\s*[-*]\s+\*\*\[")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
DOI_RE = re.compile(r"doi\.org/(10\.[^\s?#]+)", re.I)
KINDS = {"conference": "Conference", "journal": "Journal", "arxiv": "ArXiv",
         "workshop": "Workshop", "others": "Others"}  # level-5 headings under a year


# ---------------------------------------------------------------- helpers
def clean_heading(text):
    text = re.sub(r"^:\w+:\s*", "", text.strip())
    return re.sub(r"^[^\w(]+", "", text).strip()


def cell(raw):
    """Return (text with link markup removed, [urls])."""
    urls = [m.group(2) for m in LINK_RE.finditer(raw)]
    return LINK_RE.sub(lambda m: m.group(1), raw).strip(), urls


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def norm_header(h):
    return re.sub(r"\s+", " ", h).strip()


def unique(names):
    seen, out = {}, []
    for n in names:
        seen[n] = seen.get(n, 0) + 1
        out.append(n if seen[n] == 1 else "%s #%d" % (n, seen[n]))
    return out


def snake(h):
    return re.sub(r"[^a-z0-9]+", "_", h.lower().replace("#", "")).strip("_")


def norm_name(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def dataset_key(s):
    """Join key for dataset names. Keeps '+' because ChicagoFSWild and ChicagoFSWild+ are different datasets."""
    return re.sub(r"[^a-z0-9+]+", "", s.lower())


def to_int(s):
    return int(s) if s and re.fullmatch(r"\d{4}", s.strip()) else None


def read_table(lines, i):
    """lines[i] is a header row and lines[i+1] the separator. Returns
    (header_cells, [(lineno, cells)], next_index)."""
    header = unique([norm_header(c) for c in split_row(lines[i])])
    rows, j = [], i + 2
    while j < len(lines) and lines[j].strip() and "|" in lines[j]:
        rows.append((j + 1, split_row(lines[j])))
        j += 1
    return header, rows, j


def is_table_start(lines, i):
    return "|" in lines[i] and i + 1 < len(lines) and bool(SEP_RE.match(lines[i + 1]))


def fields_from(header, cells, warns, file, lineno):
    if len(cells) != len(header):
        warns.append({"file": file, "line": lineno, "code": "column-count",
                      "message": "row has %d cells, header has %d" % (len(cells), len(header))})
    fields, links = {}, {}
    for h, c in zip(header, cells):
        t, u = cell(c)
        fields[h] = t
        if u:
            links[h] = u
    if len(cells) > len(header):
        extra = [cell(c)[0] for c in cells[len(header):]]
        fields["_extra"] = extra
    return fields, links


# ---------------------------------------------------------------- README
def make_paper(start, texts, section, year, kind, earlier):
    body = BULLET_RE.match(texts[0]).group(1)
    for extra in texts[1:]:
        body += " " + extra.strip()
    venue = short = None
    m = re.match(r"\*\*\[([^\]]*)\]\*\*\s*(.*)", body)
    if m:
        venue, body = m.group(1).strip(), m.group(2)
    m = re.match(r"`([^`]+)`\s*(.*)", body)
    if m:
        short, body = m.group(1).strip(), m.group(2)
    first = LINK_RE.search(body)
    title = (body[:first.start()] if first else body).strip().rstrip(".").strip()
    links = [{"label": m.group(1), "url": m.group(2)} for m in LINK_RE.finditer(body)]
    arxiv = doi = None
    for l in links:
        a, d = ARXIV_RE.search(l["url"]), DOI_RE.search(l["url"])
        arxiv = arxiv or (a.group(1) if a else None)
        doi = doi or (d.group(1) if d else None)
    key = hashlib.sha1(norm_name(title).encode()).hexdigest()[:10] if title else None
    return {"key": key, "title": title, "short_name": short, "venue": venue,
            "year": year, "kind": kind, "earlier": earlier, "section": list(section),
            "arxiv_id": arxiv, "doi": doi, "links": links,
            "source": {"file": README, "line": start}}


def parse_readme(lines, warns):
    papers, board, summary = [], [], []
    region = None
    stack = {}
    year = kind = None
    earlier, saved = False, (None, None)
    task = dataset = group = None
    summary_category = None
    buf = None  # [start_line, [raw lines]]

    def flush():
        nonlocal buf
        if buf:
            papers.append(make_paper(buf[0], buf[1], [stack[k] for k in sorted(stack)],
                                     year, kind, earlier))
        buf = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if is_table_start(lines, i):
            flush()
            header, rows, i = read_table(lines, i)
            if region == "leaderboard":
                for lineno, cells in rows:
                    fields, links = fields_from(header, cells, warns, README, lineno)
                    first = header[0]
                    mismatch = len(cells) != len(header)  # cells are shifted: do not trust derived columns
                    vcol = next((h for h in header if "conference" in h.lower() or "venue" in h.lower()), None)
                    board.append({
                        "task": task, "dataset": dataset, "group": group,
                        "table_columns": header,
                        "model": fields.get(first),
                        "model_url": (links.get(first) or [None])[0],
                        "year": to_int(fields.get("Year")),
                        "venue": None if mismatch else (fields.get(vcol) if vcol else None),
                        "code": None if mismatch else fields.get("Code"),
                        "code_url": None if mismatch else (links.get("Code") or [None])[0],
                        "column_mismatch": mismatch,
                        "fields": fields, "links": links,
                        "source": {"file": README, "line": lineno}})
            elif region == "datasets":
                keys = [snake(h) for h in header]
                for lineno, cells in rows:
                    fields, links = fields_from(header, cells, warns, README, lineno)
                    summary.append({"name": fields.get(header[0]), "category": summary_category,
                                    "fields": {k: fields[h] for k, h in zip(keys, header)},
                                    "links": {k: links[h] for k, h in zip(keys, header) if h in links},
                                    "source": {"file": README, "line": lineno}})
            else:
                warns.append({"file": README, "line": i, "code": "table-outside-region",
                              "message": "table ignored (not in Datasets or Leaderboard)"})
            continue

        m = HEADING_RE.match(line)
        if m and not stripped.startswith("#!"):
            flush()
            lv, text = len(m.group(1)), clean_heading(m.group(2))
            low = text.lower()
            if lv == 2:
                stack.clear()
                year = kind = None
                region = ("datasets" if "datasets" in low else "papers" if "papers" in low
                          else "leaderboard" if "leaderboard" in low else None)
            elif region == "papers":
                if YEAR_RE.match(text):
                    year, kind = int(text), None
                elif low in KINDS and lv >= 5:
                    kind = KINDS[low]
                else:
                    for k in [k for k in stack if k >= lv]:
                        del stack[k]
                    stack[lv] = text
                    year = kind = None
            elif region == "leaderboard":
                if lv == 3:
                    mm = re.match(r"Results on (.+?) dataset", text, re.I)
                    if mm:
                        dataset, group = mm.group(1).strip(), None
                    elif "leaderboard" in low:
                        task, dataset, group = text.split()[0], None, None
                elif lv == 4:
                    group = text
            elif region == "datasets" and lv == 3:
                summary_category = next((c for c in ("fingerspelling", "isolated", "continuous") if c in low), None)
            i += 1
            continue

        if stripped.startswith("<details"):
            flush()
            earlier, saved = True, (year, kind)
            year = kind = None
        elif stripped.startswith("</details"):
            flush()
            earlier, (year, kind) = False, saved
        elif region == "papers":
            bm = BULLET_RE.match(line.rstrip())
            if bm:
                flush()
                body = bm.group(1)
                if re.match(r"\*\*\[", body) or LINK_RE.search(body):
                    buf = [i + 1, [line.rstrip()]]
                else:
                    warns.append({"file": README, "line": i + 1, "code": "bullet-not-entry",
                                  "message": "bullet in Papers has no venue tag or link; skipped"})
            elif not stripped:
                flush()
            elif buf and not stripped.startswith(("<", "*", "-")):
                buf[1].append(line.rstrip())  # wrapped continuation of the previous entry
            else:
                flush()
        i += 1
    flush()
    return papers, board, summary


# ---------------------------------------------------------------- datasets.md
def parse_datasets_md(lines, warns):
    out, category, i = [], None, 0
    while i < len(lines):
        m = HEADING_RE.match(lines[i])
        if m:
            low = m.group(2).lower()
            if len(m.group(1)) == 2:
                category = next((c for c in ("fingerspelling", "isolated", "continuous") if c in low), None)
            i += 1
        elif is_table_start(lines, i):
            header, rows, i = read_table(lines, i)
            keys = [snake(h) for h in header]
            for lineno, cells in rows:
                fields, links = fields_from(header, cells, warns, DATASETS, lineno)
                out.append({"name": fields.get(header[0]), "category": category,
                            "fields": {k: fields[h] for k, h in zip(keys, header)},
                            "links": {k: links[h] for k, h in zip(keys, header) if h in links},
                            "readme_summary": None,
                            "source": {"file": DATASETS, "line": lineno}})
        else:
            i += 1
    return out


# ---------------------------------------------------------------- self-check
def verify(readme_lines, ds_lines, papers, board, datasets):
    problems = []

    # README region boundaries (h2 headings)
    regions, cur = {}, None
    for n, l in enumerate(readme_lines, 1):
        m = HEADING_RE.match(l)
        if m and len(m.group(1)) == 2:
            low = clean_heading(m.group(2)).lower()
            cur = ("datasets" if "datasets" in low else "papers" if "papers" in low
                   else "leaderboard" if "leaderboard" in low else None)
        regions[n] = cur

    parsed = {p["source"]["line"] for p in papers}
    for n, l in enumerate(readme_lines, 1):
        if regions[n] == "papers" and STRICT_ENTRY_RE.match(l) and n not in parsed:
            problems.append("README line %d looks like a paper entry but was not parsed" % n)

    def table_rows(lines, accept):
        rows = set()
        for n, l in enumerate(lines, 1):
            if not accept(n) or l.count("|") < 3 or SEP_RE.match(l):
                continue
            nxt = lines[n] if n < len(lines) else ""
            if SEP_RE.match(nxt):  # header row
                continue
            rows.add(n)
        return rows

    want = table_rows(readme_lines, lambda n: regions[n] == "leaderboard")
    got = {r["source"]["line"] for r in board}
    if want != got:
        problems.append("leaderboard rows differ: missing %s, unexpected %s"
                        % (sorted(want - got)[:10], sorted(got - want)[:10]))
    want = table_rows(ds_lines, lambda n: True)
    got = {r["source"]["line"] for r in datasets}
    if want != got:
        problems.append("datasets.md rows differ: missing %s, unexpected %s"
                        % (sorted(want - got)[:10], sorted(got - want)[:10]))
    return problems


# ---------------------------------------------------------------- main
def build():
    texts = {}
    for f in (README, DATASETS):
        texts[f] = (ROOT / f).read_text(encoding="utf-8")
    rl, dl = texts[README].split("\n"), texts[DATASETS].split("\n")
    warns = []
    papers, board, summary = parse_readme(rl, warns)
    datasets = parse_datasets_md(dl, warns)

    by_name = {}
    for s in summary:
        by_name.setdefault(dataset_key(s["name"] or ""), []).append(s)
    for d in datasets:
        hit = by_name.get(dataset_key(d["name"] or ""))
        if hit:
            best = next((s for s in hit if s["name"] == d["name"]), hit[0])
            d["readme_summary"] = {k: best[k] for k in ("category", "fields", "links", "source")}
    matched = {dataset_key(d["name"] or "") for d in datasets}
    readme_only = [s["name"] for s in summary if dataset_key(s["name"] or "") not in matched]

    counts = {"papers": len(papers),
              "papers_without_links": sum(1 for p in papers if not p["links"]),
              "leaderboard_rows": len(board),
              "leaderboard_rows_by_task": {},
              "datasets": len(datasets),
              "readme_summary_rows": len(summary),
              "readme_summary_rows_not_in_datasets_md": readme_only,
              "parse_warnings": len(warns)}
    for r in board:
        counts["leaderboard_rows_by_task"][r["task"]] = counts["leaderboard_rows_by_task"].get(r["task"], 0) + 1
    meta = {"schema_version": SCHEMA_VERSION,
            "generator": "scripts/parse.py",
            "sources": {f: {"sha256": hashlib.sha256(t.encode("utf-8")).hexdigest(),
                            "lines": len(t.split("\n"))} for f, t in texts.items()},
            "counts": counts, "parse_warnings": warns}
    result = {"papers.json": papers, "leaderboards.json": board,
              "datasets.json": datasets, "meta.json": meta}
    return result, verify(rl, dl, papers, board, datasets)


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="fail if data/*.json are out of date")
    args = ap.parse_args()
    result, problems = build()
    for p in problems:
        print("SELF-CHECK FAILED:", p, file=sys.stderr)
    if problems:
        return 2
    if args.check:
        stale = [n for n, obj in result.items()
                 if not (OUT / n).exists() or (OUT / n).read_text(encoding="utf-8") != dump(obj)]
        if stale:
            print("out of date:", ", ".join(stale), file=sys.stderr)
            return 1
        print("data/ is up to date")
        return 0
    OUT.mkdir(exist_ok=True)
    for n, obj in result.items():
        (OUT / n).write_text(dump(obj), encoding="utf-8", newline="\n")
    c = result["meta.json"]["counts"]
    print("papers=%(papers)d leaderboard_rows=%(leaderboard_rows)d datasets=%(datasets)d "
          "summary_rows=%(readme_summary_rows)d parse_warnings=%(parse_warnings)d" % c)
    return 0


if __name__ == "__main__":
    sys.exit(main())
