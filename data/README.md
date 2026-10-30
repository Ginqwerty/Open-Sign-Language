# Machine-readable data

JSON generated from `README.md` and `helper/datasets.md` by `scripts/parse.py`.
The files are derived: edit the Markdown sources, then regenerate.

```
python3 scripts/parse.py           # write data/*.json
python3 scripts/parse.py --check   # exit 1 if data/*.json are out of date
```

Standard library only; no network. The parser reports what the sources say and
does not fix or normalise them (typos, wrong links and inconsistent labels are kept as written).
Each record has `source.line`, the line number in its source file.

| File | Contents |
|---|---|
| `papers.json` | One record per paper bullet in README "Papers": `title`, `short_name`, `venue`, `year`, `kind` (Conference/Journal/ArXiv/...), `section` (heading path as written), `arxiv_id`, `doi`, `links`. `key` hashes the normalised title, so the same paper listed in several sections shares a key. Entries inside the "Earlier" folds have `year: null` and `earlier: true`. |
| `leaderboards.json` | One record per leaderboard table row: `task` (SLR/SLT/SLP), `dataset`, `group` (e.g. Gloss-free), `model`, `model_url`, `year`, `venue`, `code`, `code_url`, plus every column in `fields`. Rows whose cell count differs from the header have `column_mismatch: true` and `venue`/`code` set to null. |
| `datasets.json` | One record per row of `helper/datasets.md` (all 17 columns, keys in snake_case under `fields`), with `readme_summary` holding the matching row of the README summary tables when there is one. |
| `meta.json` | Source file hashes, record counts and parse warnings. |

Known limits: `section` follows the README's heading levels, so "SLP Survey Papers" appears nested under "SLT Survey Papers" because the README nests it there. Values such as ✅/❌, "Contact Author" or "-" are kept as raw text.
