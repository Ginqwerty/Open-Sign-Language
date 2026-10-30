#!/usr/bin/env python3
"""Consistency report for the data in this repository.

Reads data/*.json (see scripts/parse.py) and the Markdown sources, and writes

    docs/lint-report.md   human-readable report
    data/lint.json        every finding, machine-readable

It never modifies README.md or helper/*.md, never uses the network and never
calls a model. It checks formatting and internal consistency only: it does NOT
check that a link is alive, that a paper title matches its link, or that a
metric value is correct.

    python3 scripts/lint.py           # write the report
    python3 scripts/lint.py --check   # exit 1 if the report is out of date
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
README, DATASETS = "README.md", "helper/datasets.md"

SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I)
DOI_RE = re.compile(r"/(10\.\d{4,9}/[^?#\s]+)", re.I)
MISSING = {"", "-", "\\-", "n/a", "na", "unknown", "none", "?"}
TRACKING = {"casa_token", "fbclid", "gclid", "authuser"}
SIGNED = {"x-amz-signature", "signature", "key-pair-id", "x-amz-expires", "expires"}
MIRROR_HOSTS = ("researchgate.net", "drive.google.com", "cloudfront.net", "pkwyx.com")
REAL_VENUES = {"EAAI", "ACCV", "IJ-AI"}  # real venues that happen to be one letter from a common one
KNOWN_TYPOS = ("Avaliable", "Papar")  # seeded from a manual read of the sources
COUNTRY_LABELS = {"germany", "netherlands", "argentina", "hong kong"}  # country used where others use a language/nationality
NON_METRIC = {"model name", "year", "architecture", "model input", "conference/journal", "code",
              "with gloss", "modality", "dataset"}

# id -> (severity, title, what it means)
RULES = {
    "link-no-scheme": ("error", "Link without http(s)://",
                       "GitHub renders it as a relative path, so the link is dead."),
    "column-count": ("error", "Table row with a different number of cells than its header",
                     "Cells after the mismatch are shifted or dropped when rendered."),
    "leaderboard-link-differs": ("warn", "Leaderboard link differs from the paper list for the same model name",
                                 "Either the leaderboard or the paper list points to the wrong paper, or both point to the same paper under different URLs."),
    "leaderboard-year-mismatch": ("warn", "Leaderboard year differs from the paper list",
                                  "Matched by link. Can be legitimate (arXiv year vs. publication year); needs a human decision."),
    "leaderboard-venue-mismatch": ("warn", "Leaderboard venue differs from the paper list",
                                   "Matched by link. Can be legitimate (preprint vs. final venue); needs a human decision."),
    "venue-typo": ("warn", "Venue label one typo away from a common label",
                   "Same length, one substitution or one swapped pair, and the other label is used 3+ times. Real venues EAAI, ACCV and IJ-AI are excluded."),
    "dataset-publication-mismatch": ("warn", "Dataset cites a publication named after a different dataset",
                                     "The publication text names another dataset (of a different language) but not this one: possible copy-paste."),
    "readme-summary-mismatch": ("warn", "README summary table differs from helper/datasets.md",
                                "The same dataset shows different values in the two places."),
    "paper-link-shared": ("warn", "Same paper link used by different paper entries",
                          "One of the links is probably a copy-paste."),
    "paper-duplicate-in-section": ("warn", "Paper listed twice in the same section", "Exact repeat under the same headings."),
    "paper-no-link": ("warn", "Paper entry without any link", "Readers cannot reach the paper."),
    "paper-no-venue": ("info", "Paper entry without a venue tag", "Every other entry starts with **[Venue]**."),
    "url-signed-expiring": ("warn", "Link with an expiring signature", "Will stop working after the signature expires."),
    "url-tracking-token": ("info", "Link carrying a session or tracking parameter",
                           "Parameters such as casa_token are session-specific and can break or leak access."),
    "url-non-canonical-host": ("info", "Link to a mirror or file host instead of the publisher/arXiv",
                               "Mirrors disappear more often than publisher pages."),
    "row-no-leading-pipe": ("info", "Table row without a leading |",
                            "GitHub still renders it; stricter Markdown parsers may not."),
    "known-typo": ("info", "Known misspelling", "Seeded list: " + ", ".join(KNOWN_TYPOS) + "."),
    "label-case-variant": ("info", "Same label with different capitalisation", "Treated as two labels by anything that groups by venue."),
    "language-label-style": ("info", "Country name used as a language label",
                             "Other rows use a language or nationality (American, Chinese)."),
    "missing-marker-mixed": ("info", "Both '-' and '\\-' used for a missing value", "Escaped and unescaped hyphens mean the same thing."),
    "leaderboard-not-numeric": ("info", "Metric cell is not a plain number", "Cannot be sorted or compared as is."),
    "leaderboard-order": ("info", "Row out of order in an otherwise sorted leaderboard", "Sorted by WER (ascending) or BLEU-4 (descending)."),
    "leaderboard-link-unmatched": ("info", "Leaderboard link not found in the paper list", "No year/venue cross-check was possible."),
    "dataset-year-range": ("info", "Dataset year outside 1990-2026", "Probably a typo."),
}
ORDER = {"error": 0, "warn": 1, "info": 2}


# ---------------------------------------------------------------- helpers
def ukey(u):
    """Identity of the document a URL points to (arXiv id, DOI, or host+path+identifying query)."""
    m = ARXIV_RE.search(u)
    if m:
        return "arxiv:" + m.group(1)
    s = urlsplit(u if "://" in u else "https://" + u)
    host = s.netloc.lower()
    if host in ("dl.acm.org", "doi.org", "dx.doi.org") or host.endswith(".wiley.com"):
        d = DOI_RE.search(s.path)
        if d:
            return "doi:" + d.group(1).lower()
    q = sorted((k, v) for k, v in parse_qsl(s.query) if k.lower() not in TRACKING | SIGNED | {"ref", "response-content-type", "response-content-disposition"})
    return (host[4:] if host.startswith("www.") else host) + s.path.rstrip("/").lower() + ("?" + "&".join("%s=%s" % kv for kv in q) if q else "")


def alnum(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def names_in(name, text):
    """True if `name` occurs in `text` as whole words (so 'iSign' does not match 'Uni-Sign')."""
    words = lambda x: " " + re.sub(r"[^a-z0-9]+", " ", x.lower()).strip() + " "
    return len(alnum(name)) >= 4 and words(name) in words(text)


def num(s):
    try:
        return float(re.sub(r"[%\s]", "", s))
    except ValueError:
        return None


def one_typo(a, b):
    a, b = a.lower(), b.lower()
    if len(a) != len(b) or len(a) < 4 or a == b:
        return False
    d = [i for i in range(len(a)) if a[i] != b[i]]
    return len(d) == 1 or (len(d) == 2 and d[1] == d[0] + 1 and a[d[0]] == b[d[1]] and a[d[1]] == b[d[0]])


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


# ---------------------------------------------------------------- checks
def run():
    papers, board = load("papers.json"), load("leaderboards.json")
    datasets, meta = load("datasets.json"), load("meta.json")
    findings = []

    def add(rule, file, line, detail):
        findings.append({"rule": rule, "severity": RULES[rule][0], "file": file, "line": line, "detail": detail})

    # --- parser warnings
    for w in meta["parse_warnings"]:
        if w["code"] == "column-count":
            add("column-count", w["file"], w["line"], w["message"])

    # --- every link in every record
    links = []  # (file, line, url, context)
    for p in papers:
        for l in p["links"]:
            links.append((README, p["source"]["line"], l["url"], p["short_name"] or p["title"][:50]))
    for b in board:
        for us in b["links"].values():
            for u in us:
                links.append((README, b["source"]["line"], u, b["model"]))
    for d in datasets:
        for us in d["links"].values():
            for u in us:
                links.append((DATASETS, d["source"]["line"], u, d["name"]))
        rs = d["readme_summary"]
        if rs:
            for us in rs["links"].values():
                for u in us:
                    links.append((README, rs["source"]["line"], u, d["name"]))
    for f, ln, u, ctx in links:
        if "://" not in u:
            add("link-no-scheme", f, ln, "%s: `%s`" % (ctx, u))
            continue
        s = urlsplit(u)
        q = {k.lower(): v for k, v in parse_qsl(s.query, keep_blank_values=True)}
        host = s.netloc.lower()
        bad = sorted(k for k in q if k in SIGNED)
        if bad:
            add("url-signed-expiring", f, ln, "%s: %s on %s" % (ctx, ", ".join(bad), host))
        tok = sorted(k for k in q if k in TRACKING or k.startswith("utm_"))
        if tok:
            add("url-tracking-token", f, ln, "%s: %s on %s" % (ctx, ", ".join(tok), host))
        if any(host.endswith(h) for h in MIRROR_HOSTS) or "githubhelp.com" in q.get("ref", ""):
            add("url-non-canonical-host", f, ln, "%s: %s" % (ctx, host if "githubhelp" not in q.get("ref", "") else host + " (ref=githubhelp.com)"))

    # --- papers
    for p in papers:
        ln = p["source"]["line"]
        if not p["links"]:
            add("paper-no-link", README, ln, p["title"])
        if p["venue"] is None:
            add("paper-no-venue", README, ln, p["title"])
    seen = collections.defaultdict(list)
    for p in papers:
        seen[(p["key"], tuple(p["section"]))].append(p)
    for (_, sec), ps in seen.items():
        if len(ps) > 1:
            add("paper-duplicate-in-section", README, ps[1]["source"]["line"],
                "%s (also line %d, under %s)" % (ps[0]["title"], ps[0]["source"]["line"], " > ".join(sec)))
    by_url = collections.defaultdict(dict)
    for p in papers:
        for l in p["links"]:
            if l["label"].lower() == "paper" and "://" in l["url"]:
                by_url[ukey(l["url"])][p["key"]] = p
    for k, ps in by_url.items():
        if len(ps) > 1:
            first = list(ps.values())
            add("paper-link-shared", README, first[1]["source"]["line"],
                "%s and %s (line %d) share one Paper link" % (first[1]["title"][:60], first[0]["title"][:60], first[0]["source"]["line"]))
    venues = collections.Counter(p["venue"] for p in papers if p["venue"])
    for v, c in venues.items():
        if c <= 2 and v not in REAL_VENUES:
            for w, c2 in venues.items():
                if c2 >= 3 and one_typo(v, w):
                    for p in papers:
                        if p["venue"] == v:
                            add("venue-typo", README, p["source"]["line"], "`%s` (x%d) vs `%s` (x%d)" % (v, c, w, c2))
    low = collections.defaultdict(set)
    for v in venues:
        low[v.lower()].add(v)
    for k, vs in sorted(low.items()):
        if len(vs) > 1:
            major = max(vs, key=lambda v: (venues[v], v))
            for p in papers:
                if p["venue"] in vs and p["venue"] != major:
                    add("label-case-variant", README, p["source"]["line"],
                        "venue tag `%s` (x%d) vs `%s` (x%d)" % (p["venue"], venues[p["venue"]], major, venues[major]))
    # the Conference/Journal/ArXiv sub-headings are read from the raw file: the JSON stores them normalised
    heads = collections.defaultdict(list)
    for n, l in enumerate((ROOT / README).read_text(encoding="utf-8").split("\n"), 1):
        m = re.match(r"^\s*#{5}\s+(Conference|Journal|ArXiv|Workshop|Others)\s*$", l, re.I)
        if m:
            heads[m.group(1).lower()].append((n, m.group(1)))
    for k, hs in sorted(heads.items()):
        counts = collections.Counter(t for _, t in hs)
        if len(counts) > 1:
            major = max(counts, key=lambda t: (counts[t], t))
            for n, t in hs:
                if t != major:
                    add("label-case-variant", README, n, "heading `%s` (x%d) vs `%s` (x%d)" % (t, counts[t], major, counts[major]))

    # --- leaderboard vs paper list
    by_key = collections.defaultdict(list)
    for p in papers:
        for l in p["links"]:
            if "://" in l["url"]:
                by_key[ukey(l["url"])].append(p)
    shorts = collections.defaultdict(set)
    for p in papers:
        if p["short_name"] and p["links"] and "://" in p["links"][0]["url"]:
            shorts[alnum(p["short_name"])].add(ukey(p["links"][0]["url"]))
    for b in board:
        ln, u = b["source"]["line"], b["model_url"]
        if not u or "://" not in u:
            continue
        base = alnum(re.sub(r"\(.*?\)", "", b["model"] or ""))
        if base in shorts and ukey(u) not in shorts[base]:
            add("leaderboard-link-differs", README, ln, "%s -> `%s`; paper list uses %s" % (
                b["model"], u[:90], ", ".join("`%s`" % k for k in sorted(shorts[base]))))
        ps = by_key.get(ukey(u))
        if not ps:
            add("leaderboard-link-unmatched", README, ln, "%s -> `%s`" % (b["model"], u[:90]))
            continue
        years = {p["year"] for p in ps if p["year"]}
        if b["year"] and years and b["year"] not in years:
            add("leaderboard-year-mismatch", README, ln, "%s: leaderboard %s, paper list %s" % (b["model"], b["year"], "/".join(map(str, sorted(years)))))
        lv = alnum(b["venue"])
        if lv:
            ok = False
            for p in ps:
                pv = alnum(p["venue"])
                ok = ok or (pv and (lv == pv or lv in pv or pv in lv)) or (lv == "arxiv" and p["kind"] == "ArXiv")
            if not ok:
                add("leaderboard-venue-mismatch", README, ln, "%s: leaderboard `%s`, paper list %s" % (
                    b["model"], b["venue"], ", ".join("`%s`" % v for v in sorted({p["venue"] or "?" for p in ps}))))

    # --- leaderboard cells
    tables = collections.OrderedDict()
    for b in board:
        tables.setdefault((b["task"], b["dataset"], b["group"]), []).append(b)
    for (task, ds, grp), rows in tables.items():
        for b in rows:
            for h, v in b["fields"].items():
                if h.lower() in NON_METRIC or h == "_extra" or h.startswith("Model"):
                    continue
                if v.strip() not in MISSING and num(v) is None and not re.search(r"[A-Za-z]{3,}", v):
                    add("leaderboard-not-numeric", README, b["source"]["line"], "%s, %s = `%s`" % (b["model"], h, v))
        col = "WER" if task == "SLR" else "BLEU-4"
        vals = [(b, num(b["fields"].get(col, ""))) for b in rows]
        vals = [(b, v) for b, v in vals if v is not None]
        if len(vals) < 5:
            continue
        asc = col == "WER"
        bad = [i for i in range(1, len(vals)) if (vals[i][1] < vals[i - 1][1] if asc else vals[i][1] > vals[i - 1][1])]
        if 0 < len(bad) <= max(1, len(vals) // 5):
            for i in bad:
                add("leaderboard-order", README, vals[i][0]["source"]["line"],
                    "%s / %s / %s: %s %s after %s" % (task, ds, grp or "-", vals[i][0]["model"], vals[i][1], vals[i - 1][1]))

    # --- datasets
    for d in datasets:
        f, ln = d["fields"], d["source"]["line"]
        y = f.get("year", "")
        if y.isdigit() and not 1990 <= int(y) <= 2026:
            add("dataset-year-range", DATASETS, ln, "%s: %s" % (d["name"], y))
        if f.get("language", "").strip().lower() in COUNTRY_LABELS:
            add("language-label-style", DATASETS, ln, "%s: `%s`" % (d["name"], f["language"]))
        rs = d["readme_summary"]
        if rs:
            for k, v in rs["fields"].items():
                if k in f and k != "dataset":
                    a, b2 = re.sub(r"[\\\s,]", "", v).lower(), re.sub(r"[\\\s,]", "", f[k]).lower()
                    if a != b2:
                        add("readme-summary-mismatch", README, rs["source"]["line"], "%s, %s: README `%s`, datasets.md `%s`" % (d["name"], k, v, f[k]))
    for d in datasets:
        pub = d["fields"].get("publication", "")
        if pub in MISSING:
            continue
        for e in datasets:
            if e is d or len(alnum(e["name"])) < 4 or e["fields"].get("language") == d["fields"].get("language"):
                continue
            if names_in(e["name"], pub) and not names_in(d["name"], pub):
                add("dataset-publication-mismatch", DATASETS, d["source"]["line"],
                    "%s (%s) cites `%s`, which names %s (%s, line %d)" % (
                        d["name"], d["fields"].get("language"), pub[:70], e["name"], e["fields"].get("language"), e["source"]["line"]))
    for col in datasets[0]["fields"]:
        vals = [d["fields"][col] for d in datasets]
        if "-" in vals and "\\-" in vals:
            add("missing-marker-mixed", DATASETS, 1, "column `%s`: `-` x%d, `\\-` x%d" % (col, vals.count("-"), vals.count("\\-")))

    # --- raw source scans
    for f in (README, DATASETS):
        lines = (ROOT / f).read_text(encoding="utf-8").split("\n")
        for i, l in enumerate(lines):
            for t in KNOWN_TYPOS:
                if t in l:
                    add("known-typo", f, i + 1, t)
            if i > 0 and SEP_RE.match(lines[i]) and "|" in lines[i - 1]:
                j = i + 1
                while j < len(lines) and lines[j].strip() and "|" in lines[j]:
                    if not lines[j].lstrip().startswith("|"):
                        add("row-no-leading-pipe", f, j + 1, lines[j].strip()[:60])
                    j += 1

    findings.sort(key=lambda x: (ORDER[x["severity"]], list(RULES).index(x["rule"]), x["file"], x["line"], x["detail"]))

    # --- stats
    cols = collections.OrderedDict()
    for col in datasets[0]["fields"]:
        miss = sum(1 for d in datasets if d["fields"][col].strip().lower() in MISSING)
        cols[col] = miss
    stats = {"dataset_rows": len(datasets), "dataset_missing_by_column": cols,
             "available_values": dict(collections.Counter(d["fields"]["available"] for d in datasets).most_common()),
             "language_values": dict(collections.Counter(d["fields"]["language"] for d in datasets).most_common())}
    return findings, stats, meta


# ---------------------------------------------------------------- report
def render(findings, stats, meta):
    by_rule = collections.defaultdict(list)
    for f in findings:
        by_rule[f["rule"]].append(f)
    out = ["# Data lint report", "",
           "Generated by `scripts/lint.py` from `data/*.json`. Nothing in `README.md` or `helper/` was changed.", "",
           "Sources checked: " + ", ".join("`%s` (sha256 `%s`)" % (n, s["sha256"][:12]) for n, s in meta["sources"].items()) + ".", "",
           "How to update the data and fix each kind of finding: [docs/maintaining.md](maintaining.md).  ",
           "A line number is the first line of the entry or table row; a paper entry that wraps onto the next lines keeps its first line's number.", "",
           "**What this checks:** formatting and internal consistency (links, tables, labels, README vs. `datasets.md`, leaderboard vs. paper list).  ",
           "**What it does not check:** whether a link is alive, whether a title matches its link, or whether a metric value is correct.", "",
           "Severity: `error` renders wrong or dead; `warn` is probably wrong and needs a human decision; `info` is hygiene.", "",
           "## Summary", "", "| Severity | Rule | Findings |", "|---|---|---:|"]
    for rule, (sev, title, _) in sorted(RULES.items(), key=lambda kv: (ORDER[kv[1][0]], list(RULES).index(kv[0]))):
        if by_rule.get(rule):
            out.append("| %s | [%s](#%s) | %d |" % (sev, title.replace("|", "\\|"), rule, len(by_rule[rule])))
    out += ["", "## Dataset completeness (`helper/datasets.md`, %d rows)" % stats["dataset_rows"], "",
            "| Column | Missing | Share |", "|---|---:|---:|"]
    for col, n in sorted(stats["dataset_missing_by_column"].items(), key=lambda kv: -kv[1]):
        out.append("| %s | %d | %d%% |" % (col.replace("_", " "), n, round(100 * n / stats["dataset_rows"])))
    out += ["", "A value counts as missing when it is empty, `-`, `\\-`, N/A, unknown or none.", "",
            "Values used in the `available` column: " + ", ".join("`%s` x%d" % kv for kv in stats["available_values"].items()) + ".", ""]
    clean = [r for r in RULES if not by_rule.get(r)]
    out += ["Checks that ran and found nothing: " + ", ".join("`%s`" % r for r in clean) + ".", ""]
    out.append("## Findings")
    for rule, (sev, title, desc) in sorted(RULES.items(), key=lambda kv: (ORDER[kv[1][0]], list(RULES).index(kv[0]))):
        fs = by_rule.get(rule)
        if not fs:
            continue
        out += ["", '<a id="%s"></a>' % rule, "### %s (%d)" % (title, len(fs)), "", "`%s` · %s" % (sev, desc), ""]
        cap = 25
        for f in fs[:cap]:
            out.append("- `%s:%d` %s" % (f["file"], f["line"], f["detail"]))
        if len(fs) > cap:
            out.append("- ... and %d more, all listed in `data/lint.json`." % (len(fs) - cap))
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="fail if the report is out of date")
    args = ap.parse_args()
    findings, stats, meta = run()
    counts = collections.Counter(f["severity"] for f in findings)
    js = json.dumps({"schema_version": 1, "sources": {n: s["sha256"] for n, s in meta["sources"].items()},
                     "counts": {s: counts.get(s, 0) for s in ORDER}, "stats": stats, "findings": findings},
                    ensure_ascii=False, indent=2) + "\n"
    md = render(findings, stats, meta)
    targets = {ROOT / "data" / "lint.json": js, ROOT / "docs" / "lint-report.md": md}
    if args.check:
        stale = [str(p.relative_to(ROOT)) for p, t in targets.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale:
            print("out of date:", ", ".join(stale), file=sys.stderr)
            return 1
        print("lint report is up to date")
        return 0
    (ROOT / "docs").mkdir(exist_ok=True)
    for p, t in targets.items():
        p.write_text(t, encoding="utf-8", newline="\n")
    print("error=%d warn=%d info=%d" % tuple(counts.get(s, 0) for s in ("error", "warn", "info")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
