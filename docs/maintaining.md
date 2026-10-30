# Maintaining the data files and fixing lint findings

`README.md` and `helper/datasets.md` are the source of truth. Everything in `data/` is generated from them, so never edit the JSON by hand.

## 1. Update the JSON after a change

```
python3 scripts/parse.py      # rewrite data/papers.json, datasets.json, leaderboards.json, meta.json
python3 scripts/lint.py       # rewrite docs/lint-report.md and data/lint.json
git add README.md helper/ data/ docs/
```

Commit the Markdown change and the regenerated files together. Only the Python 3 standard library is needed (tested with Python 3.10); nothing is downloaded.

- `python3 scripts/parse.py --check` and `python3 scripts/lint.py --check` exit 1 if the generated files are stale. They are meant for CI or a pre-commit hook.
- If `parse.py` prints `SELF-CHECK FAILED`, a line in the Markdown was not understood (a paper bullet or table row was skipped). Fix the line, or the parser if the format is legitimate.
- `data/meta.json` lists `parse_warnings` such as rows whose cell count differs from the header. Rows with a mismatch are kept, but their `venue` and `code` are set to null because the cells are shifted.
- On a merge conflict in `data/` or `docs/lint-report.md`, resolve the Markdown first, then regenerate. Do not merge generated files by hand.

## 2. Formats the parser expects

**Paper** (under `#### <year>` and `##### Conference | Journal | ArXiv | Workshop | Others`):

```
- **[Venue]** `ShortName` Title of the paper. [Paper](https://...) | [Code](https://...)
```

`ShortName` and `[Code]` are optional. A long title may wrap onto the next line. Entries inside a `<details>` "Earlier" block get no year.

**Leaderboard row**: one row per model, cells in the column order of the table header (`Model Name | Year | ... | Conference/Journal | Code`). The model name links to the paper. Use `-` for an empty cell.

**Dataset**: one row in `helper/datasets.md` with all 17 columns (`Dataset | Year | Language | Vocabulary Size | Duration | #Samples | #Signers | Domain | Collection Source | Resolution | Modality | Hand Dominance | Publication | Website | Available | Task | Baseline Model Accuracy`). If the dataset is in a README summary table, keep Year, Language, #Samples and #Signers the same in both places.

## 3. Read the lint report

`docs/lint-report.md` has a summary table, dataset completeness, and the findings grouped by rule. `data/lint.json` has every finding with `rule`, `severity`, `file`, `line` and `detail`.

| Severity | Meaning |
|---|---|
| `error` | Renders wrong or is a dead link. Fix it. |
| `warn` | Probably wrong; a person has to decide which side is right. |
| `info` | Hygiene. Fix when you touch the line anyway. |

Line numbers refer to the source files at the hashes printed at the top of the report. After editing, rerun both scripts: line numbers move.

The lint checks formatting and internal consistency only. It does not open links, compare a title with its link, or verify metric values. Open the link yourself before changing it.

## 4. How to fix each kind of finding

| Rule | What to do |
|---|---|
| `link-no-scheme` | Add `https://`. |
| `column-count` | Make the row have as many cells as the header. Find the missing or extra cell by comparing with the neighbouring rows, and check the header is not missing a column. |
| `leaderboard-link-differs` | Open both links. Make the leaderboard link equal to the paper-list link of the same model, or fix the paper-list entry if that one is wrong. Same paper under two URLs: use one canonical URL (arXiv, DOI or publisher page). |
| `leaderboard-year-mismatch`, `leaderboard-venue-mismatch` | Decide on the repository convention (for example: final venue and year when published, arXiv otherwise) and make the leaderboard and the paper list agree. If they differ because the link points to a different paper, fix the link first. |
| `venue-typo` | Correct the label in the `**[...]**` tag. |
| `dataset-publication-mismatch` | Replace the Publication and Website cells with those of the right paper. |
| `readme-summary-mismatch` | Check the dataset's paper, then update whichever of the README summary table or `datasets.md` is wrong. |
| `paper-link-shared`, `paper-duplicate-in-section` | Remove the repeated entry or correct its link. Listing a paper in two different sections (for example SLT and SLP) is intentional and is not reported. |
| `paper-no-link`, `paper-no-venue` | Add the link or the `**[Venue]**` tag. |
| `url-signed-expiring` | Replace with a stable link (publisher page, DOI or arXiv). The signed link stops working. |
| `url-tracking-token` | Delete the `?casa_token=...` part (everything from `?`) and check the link still opens. |
| `url-non-canonical-host` | Prefer arXiv, DOI or the publisher page over ResearchGate, Google Drive or file mirrors. |
| `row-no-leading-pipe` | Add the leading `\|`. |
| `known-typo` | Correct the spelling (`Avaliable` -> `Available`). To check a new word, add it to `KNOWN_TYPOS` in `scripts/lint.py`. |
| `label-case-variant` | Use `ArXiv` everywhere. |
| `language-label-style`, `missing-marker-mixed` | Use the language or nationality (`German`, not `Germany`) and a single `-` for missing values. |
| `leaderboard-not-numeric`, `leaderboard-order` | Keep metric cells numeric and tables sorted by the main metric (WER ascending, BLEU-4 descending). |
| `leaderboard-link-unmatched`, `dataset-year-range` | Check the link is in the paper list, and the year is a four-digit year. |

## 5. A false positive

If a finding is correct data that the rule does not understand, do not change the data to silence it. Add the exception to `scripts/lint.py` with a comment saying why (for example `REAL_VENUES` lists venues that look like typos of other venues but are real).
